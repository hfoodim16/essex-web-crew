#!/usr/bin/env python3
"""design-bundle.py — turn a finished static site into a Claude Design bundle.

Deterministic, offline, no DesignSync. It only writes a bundle directory plus a
manifest; the `design-push` skill does the uploading.

    python3 design-bundle.py --src <mockup-dir> --name "Client Name" --out <dir>

Handles the three shapes the crew actually ships:
  * single-page  — one card per top-level <section>/<header>/<footer>
  * SPA          — one card per <main class="page">, plus header/footer
  * multi-page   — index.html sections, plus one card per sibling .html page

Card markers match the claude.ai/design convention (first line of every preview):
  <!-- @dsCard group="…" name="…" subtitle="…" viewport="WxH" -->
"""
import argparse, json, re, shutil, sys, pathlib

BLOCK_TAGS = ("section", "header", "footer", "main", "nav", "article", "aside")
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
             "meta", "param", "source", "track", "wbr"}

# Class tokens that name a layout or effect rather than the section's purpose. The crew's
# house convention is `class="section <modifier>"` / `class="pad …"`, so deriving a slug
# from the first class token gave EVERY unnamed section the same slug — and the old
# collision branch then silently discarded all but the first. Measured before the fix:
# john-sessa-cpa emitted 4 cards for 9 real blocks. Skip these and fall through to a
# semantic source instead.
GENERIC_CLASSES = {
    "section", "pad", "pad-sm", "pad-lg", "pad-tight", "card", "wrap", "wrapper",
    "container", "inner", "outer", "row", "col", "grid", "block", "band", "reveal",
    "content", "main", "box", "panel", "group", "stack", "flex", "full", "bleed",
    # purely visual modifiers — they describe the paint, never the purpose
    "grain", "scrim", "dark", "light", "alt", "tight", "narrow", "wide", "center",
    "centered", "ink-ground", "on-ink", "dotgrid", "tealwash", "glow", "mesh",
}
# Class tokens that ARE the section's structural role. These beat a heading-derived name,
# because for structural furniture the role is what you look for ("hero", "footer") while
# the headline is just content that changes. For a content section it's the reverse, which
# is why headings still win everywhere else — `ready-to-get-your-books-in-order` is a far
# better card name than `section-4`.
ROLE_CLASSES = {
    "hero", "nav", "navbar", "header", "footer", "trust", "cta", "contact", "about",
    "services", "service", "work", "portfolio", "gallery", "testimonials", "reviews",
    "faq", "pricing", "team", "founders", "process", "steps", "stats", "features",
    "marquee", "quote", "estimate", "rail", "drawer", "menu",
}
ASSET_DIR_NAMES = ("assets", "public", "images", "img", "media", "static")
# A nested mini-site often keeps its hero image loose beside its index.html rather than in
# an asset subdir (fora's corey-blakes-steakhouse does exactly this with hero-steak.jpg).
# Those files belong to the page and must travel with it.
ASSET_EXTS = {".webp", ".jpg", ".jpeg", ".png", ".gif", ".svg", ".avif", ".ico",
              ".woff", ".woff2", ".ttf", ".otf", ".mp4", ".webm", ".pdf"}

VIEWPORTS = {
    "header": "1200x220", "nav": "1200x220", "footer": "1200x420",
    "hero": "1280x780", "page": "1280x900", "default": "1200x700",
}

CARD_BOOT = """/* card-boot.js — makes one extracted section render on its own.

   A component card holds a fragment, but the site's main.js is written against the
   whole page and can throw on the first missing element. This runs BEFORE it and
   settles the DOM into its revealed end state, so a card is never blank whatever
   happens downstream.

   rAF-then-timeout on purpose: the rAF pass lets CSS transitions actually play in a
   real browser, and the timeout is the fallback for throttled or headless contexts
   where rAF may never fire at all. */
(function () {
  'use strict';
  document.documentElement.className += ' js';
  var done = false;
  function settle() {
    if (done) return;
    done = true;
    Array.prototype.forEach.call(document.querySelectorAll('.page'), function (p) {
      p.classList.add('is-active');
      p.removeAttribute('hidden');
    });
    Array.prototype.forEach.call(document.querySelectorAll('[class*="reveal"]'), function (e) {
      e.classList.add('in');
    });
  }
  if (window.requestAnimationFrame) {
    requestAnimationFrame(function () { requestAnimationFrame(settle); });
  }
  setTimeout(settle, 350);
})();
"""

FONT_LINK_RE = re.compile(r'<link[^>]+fonts\.(?:googleapis|gstatic)\.com[^>]*>', re.I)
ROOT_RE = re.compile(r":root\s*\{(.*?)\}", re.S)
# `;` optional: the LAST declaration in a block legally omits it, and requiring one made
# that token invisible to the whole foundations pass.
VAR_RE = re.compile(r"--([\w-]+)\s*:\s*([^;}]+)")
HEX_RE = re.compile(r"^#[0-9a-fA-F]{3,8}$")


# ───────────────────────── html scanning ─────────────────────────

def _tag_iter(html):
    """Yield (start, end, name, is_close, is_self_closing) for every tag."""
    for m in re.finditer(r"<(/?)([a-zA-Z][\w-]*)((?:[^>\"']|\"[^\"]*\"|'[^']*')*)>", html):
        yield m.start(), m.end(), m.group(2).lower(), bool(m.group(1)), m.group(3).rstrip().endswith("/")


def _strip_noise(html):
    """Blank out comments/script/style so tag scanning can't trip on them."""
    def blank(m):
        return " " * (m.end() - m.start())
    html = re.sub(r"<!--.*?-->", blank, html, flags=re.S)
    html = re.sub(r"<script\b.*?</script>", blank, html, flags=re.S | re.I)
    html = re.sub(r"<style\b.*?</style>", blank, html, flags=re.S | re.I)
    return html


def top_level_blocks(html, container="body", tags=BLOCK_TAGS):
    """Top-level elements inside `container`. tags=None means any element.

    Returns [(name, open_tag_text, raw_outer_html)].
    """
    scan = _strip_noise(html)
    m = re.search(rf"<{container}\b[^>]*>", scan, re.I)
    start = m.end() if m else 0
    m2 = re.search(rf"</{container}\s*>", scan, re.I)
    stop = m2.start() if m2 else len(scan)

    out, depth, open_at, open_name, open_attrs = [], 0, None, None, None
    for s, e, name, is_close, self_closing in _tag_iter(scan):
        if s < start or s >= stop:
            continue
        if name in VOID_TAGS or self_closing:
            continue
        # When filtering to a tag whitelist we only track those tags' nesting; when
        # scanning every element we must track all of them or depth drifts.
        if tags is not None and name not in tags:
            continue
        if not is_close:
            if depth == 0:
                open_at, open_name, open_attrs = s, name, scan[s:e]
            depth += 1
        else:
            if depth > 0:
                depth -= 1
                if depth == 0 and open_at is not None:
                    out.append((open_name, open_attrs, html[open_at:e]))
                    open_at = None
    return out


def local_refs(txt):
    """Every local file reference in a chunk of HTML/CSS, data: URIs excluded.

    Stripping data: URIs is fiddly and worth doing right: an inline SVG favicon contains
    single quotes, an `xmlns='http://…'`, and even a nested `filter='url(%23n)'`. A naive
    `data:[^"')]+` stops at the first inner quote and leaks the rest of the SVG, which then
    parses as a pile of imaginary broken paths. Match to the enclosing delimiter instead.
    """
    txt = re.sub(r'(?:src|href)\s*=\s*"data:[^"]*"', "", txt, flags=re.I)
    txt = re.sub(r"""url\(\s*(['"])data:.*?\1\s*\)""", "", txt, flags=re.S | re.I)
    txt = re.sub(r"url\(\s*data:[^)]*\)", "", txt, flags=re.I)

    refs = re.findall(r'(?:src|href)\s*=\s*"([^"]+)"', txt, re.I)
    refs += re.findall(r"""url\(\s*['"]?([^'")]+)""", txt, re.I)
    out = []
    for r in refs:
        r = r.split("#")[0].split("?")[0].strip()
        if r and not r.startswith(("http", "//", "mailto:", "tel:", "data:")):
            out.append(r)
    return out


def has_class(tag_text, cls):
    return cls in attr(tag_text, "class").split()


def find_class_blocks(html, cls):
    """Every element carrying `cls`, at ANY depth, skipping ones nested inside a match.

    Direct-children-only matching was a silent failure: a single wrapper <div> between
    <main> and the views produced a bundle with no cards at all for that whole region.
    Returns [(name, open_tag_text, raw_outer_html)] in document order.
    """
    scan = _strip_noise(html)
    out, stack = [], []
    for s, e, name, is_close, self_closing in _tag_iter(scan):
        if name in VOID_TAGS or self_closing:
            continue
        if not is_close:
            tag_text = scan[s:e]
            # Only record the OUTERMOST match — a `.page` inside a `.page` is content.
            hit = has_class(tag_text, cls) and not any(h for _, _, _, h in stack)
            stack.append((name, s, tag_text, hit or any(h for _, _, _, h in stack)))
        elif stack:
            for i in range(len(stack) - 1, -1, -1):
                if stack[i][0] == name:
                    nm, start, tag_text, _ = stack[i]
                    if has_class(tag_text, cls) and not any(
                            h for _, _, _, h in stack[:i]):
                        out.append((nm, tag_text, html[start:e]))
                    del stack[i:]
                    break
    return out


def activate(raw):
    """SPA views ship `hidden`, with only the current one carrying `.is-active`.
    A card has to render on its own, so drop the flag and force the active state."""
    raw = re.sub(r"\s+hidden(?=[\s/>])", "", raw, count=1)
    if not re.match(r'^<\w+[^>]*\bclass="[^"]*\bis-active\b', raw):
        raw = re.sub(r'^(<\w+[^>]*\bclass=")', r"\1is-active ", raw, count=1)
    return raw


def attr(tag_text, name):
    m = re.search(rf'{name}\s*=\s*"([^"]*)"', tag_text or "", re.I)
    return m.group(1) if m else ""


def first_heading(raw):
    m = re.search(r"<h[1-3][^>]*>(.*?)</h[1-3]>", raw, re.S | re.I)
    if not m:
        return ""
    text = re.sub(r"<[^>]+>", " ", m.group(1))          # space, not nothing — <br> joins words
    text = text.replace("&amp;", "&").replace("&nbsp;", " ")
    text = " ".join(text.split())
    return (text[:67] + "…") if len(text) > 70 else text


def slugify(s, fallback="section"):
    s = re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")
    return s or fallback


def page_slug(rel):
    """Slug for a page from its path relative to the site root.

    `work/cecere-brothers/index.html` → `work-cecere-brothers`. The whole path matters:
    keying on the filename alone collapses every nested `index.html` into one card.
    """
    p = pathlib.PurePosixPath(rel)
    parts = list(p.parts[:-1]) + ([] if p.stem == "index" else [p.stem])
    return slugify("-".join(parts) or p.stem, "page")


def section_slug(tag, attrs, raw):
    """Name a section from the most meaningful thing it carries.

    Semantic sources first, so the lossy class-token fallback almost never fires. The
    crew writes `aria-label` on nearly every section (the $10K checklist enforces it),
    which yields genuinely good names — `aria-label="At a glance"` → `at-a-glance`.
    """
    classes = [t.lower() for t in attr(attrs, "class").split()]
    if attr(attrs, "id"):
        return slugify(attr(attrs, "id"), tag)
    # Structural role beats content: a `.hero` stays "hero", not its current headline.
    for tok in classes:
        if tok in ROLE_CLASSES:
            return slugify(tok, tag)
    for cand in (attr(attrs, "aria-label"), first_heading(raw)):
        if cand and cand.strip():
            return slugify(cand, tag)
    for tok in classes:
        if tok not in GENERIC_CLASSES and "--" not in tok:
            return slugify(tok, tag)
    return slugify(tag, tag)


def titleize(s):
    return " ".join(w.capitalize() if w.islower() else w for w in s.replace("-", " ").split())


# ───────────────────────── bundle writing ─────────────────────────

class Bundler:
    def __init__(self, src, name, out):
        self.src, self.name, self.out = pathlib.Path(src), name, pathlib.Path(out)
        self.index = self.src / "index.html"
        if not self.index.exists():
            sys.exit(f"error: no index.html in {self.src}")
        self.html = self.index.read_text(encoding="utf-8")
        self.fonts = "\n".join(FONT_LINK_RE.findall(self.html))
        self.tokens = self._tokens()
        self.manifest = []
        self.warnings = []       # every silent skip becomes a loud one — see warn()/coverage()
        self.source_broken = []  # links already broken in the source site, reported separately
        self.used_slugs = {}     # slug -> count, so a collision suffixes instead of dropping
        # Sites often stash reusable SVG symbols (a "#contour" motif, an icon sprite) in a
        # hidden width=0/height=0 <svg><defs> sibling near the top of <body>, referenced
        # elsewhere via <use href="#id">. That block sits OUTSIDE every <section>, so no
        # component extraction ever picks it up — every card using <use> would silently
        # render without the shape it points at. Carry it into every card explicitly.
        self.defs_svg = "".join(re.findall(
            r'<svg\s+width="0"\s+height="0"[^>]*>.*?</svg>', self.html, re.S))
        self.defs_ids = re.findall(r'\bid="([^"]+)"', self.defs_svg)
        # ALL asset dirs, not just the first match. A site using both assets/ and public/
        # used to have the second silently uncopied AND its refs left unrewritten, so those
        # images pointed at paths that were never written — broken with no error.
        self.asset_dirs = [d for d in ASSET_DIR_NAMES if (self.src / d).is_dir()]
        self.asset_dir = self.asset_dirs[0] if self.asset_dirs else None
        # Multi-page sites link siblings with bare hrefs ("service-lawn-care.html",
        # "index.html") that only work because every page sits in the same folder on
        # the real site. In the bundle those pages scatter across pages/, components/,
        # and templates/landing/ — the SAME nav markup (with the SAME bare hrefs) gets
        # reused verbatim in components/nav.html, components/services.html, every
        # pages/*.html card's own header, AND templates/landing/index.html. Every one of
        # those needs the href rewritten to the sibling's real bundle location, or
        # clicking the link 404s. Built once here, applied inside rewrite().
        # rglob, not glob: fora-digital keeps its portfolio case studies at
        # work/<client>/index.html, and a non-recursive glob never saw them — the two
        # flagship links in components/work.html pointed at files that weren't in the
        # bundle. Key on the path RELATIVE TO src, never p.stem: work/a/index.html and
        # work/b/index.html both have stem "index" and would collide into one card.
        self.page_files = [p for p in sorted(self.src.rglob("*.html"))
                           if p != self.index and not self._ignored_page(p)]
        self.sibling_pages = {self._rel(p): page_slug(self._rel(p)) for p in self.page_files}
        self.signature = self._signature()

    def _rel(self, p):
        return p.relative_to(self.src).as_posix()

    def _ignored_page(self, p):
        rel = self._rel(p)
        # Never treat our own output, an asset dir's stray html, or dev scratch as a page.
        if any(part.startswith((".", "_")) for part in p.relative_to(self.src).parts):
            return True
        return rel.split("/")[0] in self.asset_dirs + ["vendor", "node_modules"]

    def warn(self, msg):
        self.warnings.append(msg)

    def _signature(self):
        """This build's signature motion, read from the design-memory row if there is one.

        Stage 8 appends a row per passing build to a project-local `design-memory.md`
        (else the skill's global `data/design-memory.md`). Its last column records the
        signature motion, which is exactly what foundations/motion.html and the readme
        should state instead of shipping a TODO.
        """
        sig, row = {}, ""
        for log in (self.src.parent / "design-memory.md",
                    self.src.parent.parent / "design-memory.md",
                    pathlib.Path.home() / ".claude/skills/web-design-ultra/data/design-memory.md"):
            if not log.is_file():
                continue
            key = self.src.parent.name.lower()
            for line in log.read_text(encoding="utf-8").splitlines():
                if line.startswith("|") and key and key in line.lower():
                    row = line
            if row:
                break
        if row:
            cells = [c.strip() for c in row.strip("|").split("|")]
            if len(cells) >= 7:
                sig["entrance + hover"] = cells[6]
            if len(cells) >= 6:
                sig["background system"] = cells[5]
        detected = sorted({m.group(1) for m in re.finditer(
            r"@keyframes\s+([\w-]+)", self.css)})
        if detected:
            sig["keyframes in styles.css"] = ", ".join(detected[:12])
        sig.setdefault("reduced motion",
                       "honoured" if "prefers-reduced-motion" in self.css else "NOT GATED — check")
        sig.setdefault("fail-visible",
                       "hidden states scoped to html.js" if ".js " in self.css or "html.js" in self.css
                       else "no html.js scoping found")
        return sig

    # -- tokens ---------------------------------------------------
    def _tokens(self):
        # EVERY stylesheet index.html links, in link order, concatenated. Breaking after
        # the first meant a site split into tokens.css + components.css lost everything
        # but the first file, while the leftover <link> kept an href that 404s.
        css = ""
        self.external_css = False
        self.css_files = []
        linked = [h for h in re.findall(r'<link[^>]+href\s*=\s*"([^"]+\.css)(?:\?[^"]*)?"',
                                        self.html, re.I)
                  if not h.startswith(("http", "//"))]
        for h in linked or ["style.css", "styles.css", "main.css"]:
            p = (self.src / h.lstrip("./"))
            if p.is_file():
                css += ("\n" if css else "") + p.read_text(encoding="utf-8")
                self.css_files.append(h)
                self.external_css = True
        if not css:
            # No shared stylesheet — this site ships fully self-contained pages, each
            # with its own <style> block (tokens + page-specific rules). index.html's
            # block still supplies the token set; extra_pages() gives every sibling
            # page its OWN style back rather than forcing index's onto it.
            m = re.search(r"<style\b[^>]*>(.*?)</style>", self.html, re.S | re.I)
            css = m.group(1) if m else ""
        self.css = css
        m = ROOT_RE.search(css)
        return dict(VAR_RE.findall(m.group(1))) if m else {}

    def own_style(self, page_html, depth, base=None):
        """That page's own inline <style> block, asset paths rewritten. Needed when the
        site has no shared stylesheet, and for nested mini-sites whose CSS the parent's
        styles.css knows nothing about."""
        blocks = re.findall(r"<style\b[^>]*>(.*?)</style>", page_html, re.S | re.I)
        return "\n".join(self.rewrite(b, depth, base=base) for b in blocks)

    def colors(self):
        return [(k, v.strip()) for k, v in self.tokens.items()
                if HEX_RE.match(v.strip()) or v.strip().startswith(("rgb", "hsl"))]

    # -- helpers --------------------------------------------------
    def add(self, rel, text=None, copy_from=None):
        dest = self.out / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        if copy_from is not None:
            shutil.copy2(copy_from, dest)
        else:
            dest.write_text(text, encoding="utf-8")
        self.manifest.append({"path": rel, "localPath": rel})

    def rewrite(self, raw, depth, base=None):
        """Fix relative URLs for a file nested `depth` dirs below the bundle root.

        `base` is the source directory the markup's relative paths were written against —
        the site root for index.html's sections, but a nested page's own folder for
        work/<client>/index.html, whose `public/hero.webp` means *its* public dir.
        """
        up = "../" * depth
        base = base or self.src
        prefix = "" if base == self.src else base.relative_to(self.src).as_posix() + "/"

        # Which asset-dir names to remap depends on the BASE, not the site root. A nested
        # mini-site can name its folder differently from its parent — fora's parent uses
        # assets/ while work/cecere-brothers/ uses public/ — and iterating only the
        # parent's dirs left every nested image pointing at a path never written.
        dirs = self.asset_dirs if base == self.src else [
            d for d in ASSET_DIR_NAMES if (base / d).is_dir()]

        for d in dirs or []:
            raw = re.sub(rf'((?:src|href)\s*=\s*")(?:\./)?{re.escape(d)}/',
                         rf'\1{up}assets/{prefix}', raw)
            # url(assets/...) — inside inline style="" attributes AND <style> blocks.
            # Always re-quote with single quotes: this text can land inside a
            # double-quoted HTML style="" attribute, where url("...") would
            # terminate the attribute early and silently truncate the markup.
            raw = re.sub(
                rf'''url\(\s*(['"]?)(?:\./)?{re.escape(d)}/([^'")]+?)\1\s*\)''',
                rf"url('{up}assets/{prefix}\2')", raw)
        raw = re.sub(r'((?:src|href)\s*=\s*")(?:\./)?vendor/', rf'\1{up}vendor/', raw)

        # Loose assets beside a nested page are referenced by bare filename
        # (url('hero-steak.jpg')), which means nothing once the card moves to pages/.
        if base != self.src:
            for a in sorted(base.iterdir()):
                if not (a.is_file() and a.suffix.lower() in ASSET_EXTS):
                    continue
                n = re.escape(a.name)
                raw = re.sub(rf'((?:src|href)\s*=\s*")(?:\./)?{n}"',
                             rf'\1{up}assets/{prefix}{a.name}"', raw)
                raw = re.sub(rf'''url\(\s*(['"]?)(?:\./)?{n}\1\s*\)''',
                             f"url('{up}assets/{prefix}{a.name}')", raw)

        # Page-to-page links resolve to their new bundle homes: pages/<slug>.html and
        # templates/landing/index.html. The SAME nav markup repeats verbatim across
        # components/nav.html, components/services.html, every pages/*.html card's own
        # header, and the landing template — all of them need this or the dropdown 404s.
        # Longest path first so "work/a/index.html" wins over a bare "index.html".
        for rel, slug in sorted(self.sibling_pages.items(), key=lambda kv: -len(kv[0])):
            for cand in {rel, rel.rsplit("/", 1)[-1] if "/" in rel else rel}:
                raw = re.sub(rf'href\s*=\s*"(?:\./)?{re.escape(cand)}((?:[?#][^"]*)?)"',
                             rf'href="{up}pages/{slug}.html\1"', raw)
        raw = re.sub(r'href\s*=\s*"(?:\./)?index\.html((?:[?#][^"]*)?)"',
                     rf'href="{up}templates/landing/index.html\1"', raw)
        # Drop the page's own script tags — card_scripts() re-adds them at the right
        # depth, so leaving these in gives a broken path and a double-load.
        raw = re.sub(r'<script\b[^>]*\bsrc\s*=\s*"(?:\./)?(?:main\.js|'
                     r'(?:\.\./)*vendor/[^"]+)(?:\?[^"]*)?"[^>]*>\s*</script>\s*',
                     "", raw, flags=re.I)
        return raw

    def page(self, group, name, subtitle, viewport, body, depth=1, scripts="", inline_css=""):
        up = "../" * depth
        # inline_css (a page's own <style> block, when the site has no shared
        # stylesheet) is placed AFTER the linked styles.css, so its rules win the
        # cascade on any selector both define — this page's own look always applies.
        extra_style = f"<style>{inline_css}</style>\n" if inline_css else ""
        # A self-contained sibling page (extra_pages()) already carries its own copy of
        # this defs block inside `body` — possibly not byte-identical (a page can carry a
        # trimmed variant), so check by id= rather than exact text, or re-adding duplicates
        # the id attribute.
        defs = "" if (self.defs_ids and all(f'id="{i}"' in body for i in self.defs_ids)) else self.defs_svg
        return (
            f'<!-- @dsCard group="{group}" name="{name}" subtitle="{subtitle}" viewport="{viewport}" -->\n'
            "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\" />\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />\n"
            f"<title>{self.name} — {name}</title>\n{self.fonts}\n"
            f'<link rel="stylesheet" href="{up}styles.css" />\n'
            f"<style>body{{margin:0}}</style>\n{extra_style}</head>\n<body>\n"
            f"{defs}{body}\n{scripts}</body>\n</html>\n"
        )

    def card_scripts(self, depth=1):
        """card-boot FIRST, then vendor, then the site's own JS.

        Order is load-bearing. A site's main.js is written against the whole page and
        will happily throw on a fragment (a real one does `getElementById("year")
        .textContent` on line 9), which would leave every `.reveal` at opacity 0 and
        the card blank. card-boot has already settled the DOM by then, so a throw
        downstream costs the animation, never the content.
        """
        up = "../" * depth
        out = f'<script src="{up}lib/card-boot.js"></script>\n'
        if (self.out / "vendor").is_dir():
            for v in sorted((self.out / "vendor").glob("*.js")):
                out += f'<script src="{up}vendor/{v.name}"></script>\n'
        if (self.out / "lib" / "site.js").exists():
            out += f'<script src="{up}lib/site.js"></script>\n'
        for extra in getattr(self, "extra_js", []):
            out += f'<script src="{up}lib/{extra}"></script>\n'
        return out

    # -- stages ---------------------------------------------------
    def copy_shared(self):
        # depth=0: styles.css sits at the bundle root, so asset refs need no "../" prefix.
        self.add("styles.css", text=self.rewrite(self.css, depth=0))

        # Every asset dir, recursively, preserving relative paths. iterdir() + is_file()
        # used to skip subtrees entirely, so the standard self-hosted-webfont layout
        # (assets/fonts/*.woff2) lost every font while rewrite() happily pointed at them.
        self.assets_copied = 0
        for d in self.asset_dirs:
            root = self.src / d
            for a in sorted(root.rglob("*")):
                if a.is_file() and not a.name.startswith("."):
                    self.add(f"assets/{a.relative_to(root).as_posix()}", copy_from=a)
                    self.assets_copied += 1
        # Nested mini-sites keep their own asset dirs; rewrite() maps them to
        # assets/<page-dir>/… so they can't collide with the parent's.
        for p in self.page_files:
            if p.parent == self.src:
                continue
            pref = p.parent.relative_to(self.src).as_posix()
            for d in ASSET_DIR_NAMES:
                root = p.parent / d
                if not root.is_dir():
                    continue
                for a in sorted(root.rglob("*")):
                    if a.is_file() and not a.name.startswith("."):
                        self.add(f"assets/{pref}/{a.relative_to(root).as_posix()}", copy_from=a)
                        self.assets_copied += 1
            # …plus any asset sitting loose beside the page itself.
            for a in sorted(p.parent.iterdir()):
                if a.is_file() and a.suffix.lower() in ASSET_EXTS and not a.name.startswith("."):
                    self.add(f"assets/{pref}/{a.name}", copy_from=a)
                    self.assets_copied += 1
                    if a.stat().st_size > 400_000:
                        self.source_broken.append(
                            f"{self._rel(a)} is {a.stat().st_size // 1024} KB — "
                            "recompress to WebP (imagery.md) before pushing")

        vend = self.src / "vendor"
        if vend.is_dir():
            for v in sorted(vend.rglob("*")):        # vendor CSS counts too, not just *.js
                if v.is_file() and not v.name.startswith("."):
                    self.add(f"vendor/{v.relative_to(vend).as_posix()}", copy_from=v)

        # Every root-level script, not just main.js. main.js becomes lib/site.js (the name
        # card_scripts() loads); anything else keeps its own name and is loaded after it.
        self.extra_js = []
        for j in sorted(self.src.glob("*.js")):
            if j.name == "main.js":
                self.add("lib/site.js", text=j.read_text(encoding="utf-8"))
            else:
                self.add(f"lib/{j.name}", text=j.read_text(encoding="utf-8"))
                self.extra_js.append(j.name)
        self.add("lib/card-boot.js", text=CARD_BOOT)

    def components(self):
        blocks = top_level_blocks(self.html)
        scripts = self.card_scripts()
        n = self.spa_pages = 0
        # If index.html links a stylesheet AND carries its own <style> block, those inline
        # rules land in templates/landing/index.html (which keeps the original HTML) but
        # reached no component card, which links only styles.css — cards rendered subtly
        # wrong. Fold them in. (When there's no external CSS, self.css already IS this
        # block and it's written to styles.css, so adding it again would duplicate it.)
        self.index_css = self.own_style(self.html, 1) if self.external_css else ""

        for tag, attrs, raw in blocks:
            if tag == "main":
                # SPA views are `.page` elements inside the main wrapper — any tag, usually
                # <div>. Search DESCENDANTS, not just direct children: one intervening
                # <div class="views"> wrapper used to yield zero page cards AND zero
                # component cards for the whole main region, reporting "0 pages" silently.
                views = find_class_blocks(raw, "page")
                if views:
                    for _, a2, r2 in views:
                        pid = attr(a2, "id") or "page"
                        self.add(f"pages/{slugify(pid)}.html",
                                 text=self.page("Pages",
                                                titleize(pid.replace("page-", "")) or "Page",
                                                first_heading(r2) or "SPA view",
                                                VIEWPORTS["page"],
                                                self.rewrite(activate(r2), 1), 1, scripts))
                        self.spa_pages += 1
                    continue
                for t2, a2, r2 in top_level_blocks(raw, container="main"):
                    n += self._emit(t2, a2, r2, scripts)
                continue
            n += self._emit(tag, attrs, raw, scripts)
        return n

    def unique(self, slug):
        """Reserve a slug, suffixing on collision. NEVER returns None.

        The old code did `if dest exists: return 0` — the single worst bug in this
        script. Two sections deriving the same slug meant the second was discarded,
        and because it returned 0 it never appeared in the printed count either, so
        the summary line looked correct while half a site went missing.
        """
        n = self.used_slugs.get(slug, 0) + 1
        self.used_slugs[slug] = n
        return slug if n == 1 else f"{slug}-{n}"

    def _emit(self, tag, attrs, raw, scripts):
        slug = section_slug(tag, attrs, raw)
        if tag in ("header", "nav") and "nav" not in self.used_slugs:
            # First header/nav is THE nav. Later ones (a mobile drawer, a footer nav)
            # keep their own semantic slug rather than colliding into "nav" and being
            # dropped — that used to cost cedar-grove and john-sessa their mobile menus.
            slug, vp = "nav", VIEWPORTS["header"]
        elif tag == "footer":
            vp = VIEWPORTS["footer"]
        elif tag in ("header", "nav"):
            vp = VIEWPORTS["header"]
        elif "hero" in slug:
            vp = VIEWPORTS["hero"]
        else:
            vp = VIEWPORTS["default"]
        final = self.unique(slug)
        if final != slug:
            self.warn(f"slug collision: <{tag}> '{slug}' already taken → emitted as '{final}'")
        self.add(f"components/{final}.html",
                 text=self.page("Components", titleize(final),
                                first_heading(raw) or f"<{tag}> from the live page",
                                vp, self.rewrite(raw, 1), 1, scripts,
                                inline_css=getattr(self, "index_css", "")))
        return 1

    def extra_pages(self):
        n = 0
        for p in self.page_files:
            rel = self._rel(p)
            slug = self.sibling_pages[rel]
            raw = p.read_text(encoding="utf-8")
            body = re.search(r"<body\b[^>]*>(.*)</body>", raw, re.S | re.I)
            inner = body.group(1) if body else raw

            # A page's own <style> block. Two cases need it:
            #  * no shared stylesheet at all — every page ships self-contained CSS
            #  * a NESTED page (work/<client>/index.html) — a separate mini-site with its
            #    own tokens and layout, which the parent's styles.css knows nothing about
            nested = "/" in rel
            own_css = (self.own_style(raw, 1, base=p.parent)
                       if (not self.external_css or nested) else "")
            if nested:
                own_css += self._nested_css(p, raw)

            # A nested mini-site's own behaviour, loaded only by its own card. The parent's
            # lib/site.js is written against the parent page and is wrong here.
            scripts = self.card_scripts(1)
            own_js = self._nested_js(p, raw, slug) if nested else None
            if own_js:
                scripts += f'<script src="../lib/{own_js}"></script>\n'

            self.add(f"pages/{slug}.html",
                     text=self.page("Pages", titleize(slug),
                                    first_heading(inner) or "Standalone page",
                                    VIEWPORTS["page"], self.rewrite(inner, 1, base=p.parent), 1,
                                    scripts, inline_css=own_css))
            n += 1
        return n

    def _nested_css(self, page, raw):
        """Inline every stylesheet a nested page links, since it lives outside styles.css."""
        out = ""
        for href in re.findall(r'<link[^>]+href\s*=\s*"([^"]+\.css)(?:\?[^"]*)?"', raw, re.I):
            if href.startswith(("http", "//")):
                continue
            f = (page.parent / href).resolve()
            if f.is_file():
                out += "\n" + self.rewrite(f.read_text(encoding="utf-8"), 1, base=page.parent)
            else:
                self.warn(f"{self._rel(page)}: linked stylesheet not found: {href}")
        return out

    def _nested_js(self, page, raw, slug):
        """Copy a nested page's own script to lib/<slug>.js and return the filename."""
        for src in re.findall(r'<script[^>]+src\s*=\s*"([^"]+\.js)(?:\?[^"]*)?"', raw, re.I):
            if src.startswith(("http", "//")):
                continue
            f = (page.parent / src).resolve()
            if f.is_file():
                name = f"{slug}.js"
                self.add(f"lib/{name}", text=f.read_text(encoding="utf-8"))
                return name
        return None

    def landing(self):
        full = self.html
        full = re.sub(r'href\s*=\s*"(?:\./)?(?:style|styles|main)\.css(?:\?[^"]*)?"',
                      'href="../../styles.css"', full)
        full = re.sub(r'src\s*=\s*"(?:\./)?main\.js(?:\?[^"]*)?"', 'src="../../lib/site.js"', full)
        full = self.rewrite(full, 2)
        # templates/<slug>/ is NOT indexed via @dsCard (that marker only feeds the
        # Components/Foundations/Pages card list). The app reads a SEPARATE
        # `@template name="…" description="…"` first-line marker into its own
        # top-level `templates` manifest array — confirmed against Modernist's
        # working templates/landing/index.html. Get this marker wrong (as the
        # @dsCard version here originally was) and the file sits in the project,
        # fully valid, and the Templates section simply never appears — no error,
        # nothing in the manifest, silently invisible.
        self.add("templates/landing/index.html",
                 text='<!-- @template name="Full page" '
                      'description="The assembled page — every component in situ" -->\n' + full)

        # A second template at phone width. Every @dsCard viewport in this bundle is
        # desktop, so without this the responsive half of the design — which the crew's
        # own checklist item 7 grades ("mobile designed, not shrunk") — is reviewable
        # nowhere in Design. Modernist proves multiple template entries work (deck + landing).
        self.add("templates/mobile/index.html",
                 text='<!-- @template name="Full page — mobile" '
                      'description="The same page at 375px, for reviewing the phone layout" -->\n'
                      + full.replace(
                          "</head>",
                          "<style>html{max-width:375px;margin:0 auto;"
                          "box-shadow:0 0 0 1px rgba(0,0,0,.12)}</style>\n</head>", 1))

    def foundations(self):
        cols = self.colors()
        demo = ("<style>.d{max-width:1000px;margin:0 auto;padding:40px 5vw 64px;"
                "font-family:system-ui,sans-serif}"
                ".h{font-size:11px;letter-spacing:.1em;text-transform:uppercase;opacity:.55;"
                "margin:36px 0 14px;font-weight:600}.h:first-child{margin-top:0}"
                ".sw{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:14px}"
                ".sw div{border:1px solid rgba(0,0,0,.12);border-radius:8px;overflow:hidden}"
                ".sw i{display:block;height:72px}.sw b{display:block;font-size:12.5px;padding:9px 11px 2px}"
                ".sw s{display:block;text-decoration:none;font-family:ui-monospace,Menlo,monospace;"
                "font-size:11px;opacity:.6;padding:0 11px 10px}"
                ".sc div{border-bottom:1px solid rgba(0,0,0,.1);padding:13px 0;display:flex;gap:20px;"
                "align-items:baseline}.sc span:first-child{font-family:ui-monospace,Menlo,monospace;"
                "font-size:11px;opacity:.6;min-width:210px;flex:none}</style>\n")

        body = '<main class="d"><p class="h">Color tokens</p><div class="sw">'
        for k, v in cols:
            body += f'<div><i style="background:{v}"></i><b>--{k}</b><s>{v}</s></div>'
        body += "</div></main>"
        self.add("foundations/color.html",
                 text=self.page("Foundations", "Color", f"{len(cols)} tokens from the site's :root",
                                "760x620", body, 1).replace("</head>", demo + "</head>"))

        # Every non-colour token, not just the ones matching a narrow name pattern. The old
        # filter was `font|fs|text|size|space|radius`, so every dur/ease/shadow/blur/border/z
        # token appeared NOWHERE in the foundations — on fora, 32 parsed and 8 shown.
        motion_re = re.compile(r"(dur|ease|delay|transition|anim|speed)", re.I)
        colour_keys = {k for k, _ in cols}
        rest = [(k, v.strip()) for k, v in self.tokens.items() if k not in colour_keys]
        sizes = [(k, v) for k, v in rest if not motion_re.search(k)]
        motion = [(k, v) for k, v in rest if motion_re.search(k)]

        def token_table(title, rows):
            out = f'<main class="d"><p class="h">{title}</p><div class="sc">'
            for k, v in rows:
                out += f"<div><span>--{k}</span><span>{v}</span></div>"
            return out + "</div></main>"

        self.add("foundations/type.html",
                 text=self.page("Foundations", "Type, spacing & effects",
                                f"{len(sizes)} non-colour tokens", "760x640",
                                token_table("Type, spacing &amp; effect tokens", sizes),
                                1).replace("</head>", demo + "</head>"))

        # foundations/motion.html — the signature move, which had no home at all. The
        # readme used to ship an italic "_Fill in the signature move…_" TODO to the client
        # instead. Named recipes live in web-design-ultra/references/motion.md.
        mbody = token_table("Motion tokens", motion) if motion else (
            '<main class="d"><p class="h">Motion tokens</p>'
            '<p style="font:14px system-ui;opacity:.6">This site tunes its motion inline '
            'rather than through <code>--dur/--ease</code> tokens — see the durations and '
            'easings in <code>styles.css</code>.</p></main>')
        mbody += ('<main class="d"><p class="h">Signature move</p><div class="sc">'
                  + "".join(f"<div><span>{k}</span><span>{v}</span></div>"
                            for k, v in self.signature.items())
                  + "</div></main>")
        self.add("foundations/motion.html",
                 text=self.page("Foundations", "Motion",
                                self.signature.get("entrance", "Signature move"),
                                "760x620", mbody, 1).replace("</head>", demo + "</head>"))

    def meta(self, counts):
        theme = {"name": self.name, "source": str(self.src),
                 "tokens": {k: v.strip() for k, v in self.tokens.items()},
                 "cards": counts}
        self.add("theme.json", text=json.dumps(theme, indent=2) + "\n")

        cols = ", ".join(f"`--{k}` {v}" for k, v in self.colors()[:8]) or "_none parsed_"
        self.add("readme.md", text=(
            f"# {self.name} design system\n\n"
            f"Extracted from the finished site at `{self.src}` — every component here is the "
            "real shipped markup, not a redrawn approximation.\n\n"
            "## How to use this\n\n"
            "- Link `styles.css` from every page and take colours, sizes and spacing from its "
            "`:root` variables. Never hard-code a value the tokens already carry.\n"
            "- Component pages are plain HTML — view source and copy the markup.\n"
            "- `templates/landing/index.html` is the assembled page.\n\n"
            f"## Color\n\n{cols}\n\n"
            "## Motion\n\n"
            + "".join(f"- **{k}** — {v}\n" for k, v in self.signature.items())
            + "\nNamed recipes live in `web-design-ultra/references/motion.md`. Hidden states "
            "are scoped to `html.js` — with no JavaScript the page renders plain, never blank.\n\n"
            "## Files\n\n"
            "- `styles.css` — the site's stylesheet(s), concatenated.\n"
            "- `foundations/` — colour, type/spacing/effect, and motion tokens from `:root`.\n"
            "- `components/` — each section of the live site.\n"
            "- `pages/` — standalone, nested and SPA page views.\n"
            "- `templates/landing/index.html` — the assembled page.\n"
            "- `templates/mobile/index.html` — the same page at 375px.\n"
            "- `lib/site.js`, `vendor/` — the site's behaviour, so cards animate.\n"))

        sw = "".join(f'<i style="flex:1;height:46px;background:{v}"></i>' for _, v in self.colors()[:6])
        self.add("thumbnail.html", text=(
            '<!-- @dsCard group="Brand" name="' + self.name +
            '" subtitle="Cover" viewport="600x360" -->\n<!doctype html>\n<html lang="en">\n<head>\n'
            '<meta charset="utf-8" /><link rel="stylesheet" href="styles.css" />\n'
            f"{self.fonts}\n<style>body{{margin:0;min-height:100vh;display:flex;align-items:center;"
            "justify-content:center;font-family:system-ui,sans-serif}"
            ".c{width:min(560px,90vw);padding:42px;border:1px solid rgba(0,0,0,.12);border-radius:12px}"
            ".m{font-size:40px;font-weight:700;line-height:1.1}"
            ".s{display:flex;margin-top:26px;border-radius:8px;overflow:hidden}</style>\n</head>\n"
            f'<body><div class="c"><p class="m">{self.name}</p>'
            f'<div class="s">{sw}</div></div></body>\n</html>\n'))

    def run(self):
        if self.out.exists():
            shutil.rmtree(self.out)
        self.out.mkdir(parents=True)
        self.copy_shared()
        comps = self.components()
        pages = self.spa_pages + self.extra_pages()
        self.landing()
        self.foundations()
        counts = {"components": comps, "pages": pages}
        self.meta(counts)
        (self.out / "_manifest.json").write_text(
            json.dumps({"name": self.name, "files": self.manifest}, indent=2) + "\n",
            encoding="utf-8")
        return counts

    def expected_blocks(self):
        """Recount, from the source, how many component cards there ought to be.

        Deliberately a SECOND walk rather than a counter incremented by the emit loop —
        a counter maintained by the code under test can't catch that code dropping things,
        which is exactly the bug this guards (`return 0` on slug collision).
        """
        n = 0
        for tag, _a, raw in top_level_blocks(self.html):
            if tag == "main":
                if find_class_blocks(raw, "page"):
                    continue                       # those become page cards, counted separately
                n += len(top_level_blocks(raw, container="main"))
            else:
                n += 1
        return n

    def coverage(self):
        """Count source truth against emitted output. This is the whole guarantee.

        Every bug this script has had was severe *specifically because it was quiet* — the
        summary line read like success while half a site went missing. So: count what the
        source has, count what we wrote, and refuse to call it a bundle if they disagree.
        """
        cards = {p["path"] for p in self.manifest}
        blocks_out = sum(1 for p in cards if p.startswith("components/"))
        pages_out = sum(1 for p in cards if p.startswith("pages/"))
        blocks_want = self.expected_blocks()
        pages_want = len(self.page_files) + self.spa_pages

        assets_want = 0
        for d in self.asset_dirs:
            assets_want += sum(1 for a in (self.src / d).rglob("*")
                               if a.is_file() and not a.name.startswith("."))
        for p in self.page_files:
            if p.parent != self.src:
                for d in ASSET_DIR_NAMES:
                    if (p.parent / d).is_dir():
                        assets_want += sum(1 for a in (p.parent / d).rglob("*")
                                           if a.is_file() and not a.name.startswith("."))
                assets_want += sum(1 for a in p.parent.iterdir()
                                   if a.is_file() and a.suffix.lower() in ASSET_EXTS
                                   and not a.name.startswith("."))

        # The @template marker regression guard. Getting this wrong is invisible: the file
        # is valid, sits in the project, and the Templates section just never appears.
        for path in sorted(p for p in cards if p.startswith("templates/")):
            first = (self.out / path).read_text(encoding="utf-8").split("\n", 1)[0]
            if "@template" not in first:
                self.warn(f"{path}: first line is not an @template marker — "
                          "it will never appear in the Templates section")
            if "@dsCard" in first:
                self.warn(f"{path}: carries @dsCard; templates/ needs @template")

        # Every local reference in every emitted file must resolve to a file we wrote.
        # This is the check that actually catches path-rewrite bugs — counting files can't:
        # a nested page's images were correctly COPIED while its markup still pointed at
        # the original `public/…`, so counts looked perfect and the card rendered blank.
        for path in sorted(p for p in cards if p.endswith((".html", ".css"))):
            f = self.out / path
            for r in local_refs(f.read_text(encoding="utf-8", errors="ignore")):
                if (f.parent / r).resolve().is_file():
                    continue
                # Distinguish "we broke it" from "the site shipped it broken". Only the
                # former is a bundler bug; the latter is worth surfacing but must not be
                # blamed on the bundle, or the gate cries wolf and stops being trusted.
                if self._in_source(r):
                    self.warn(f"{path}: dead reference '{r}' — will 404 in Design")
                else:
                    self.source_broken.append(f"{path}: '{r}'")

        return {
            "blocks": (blocks_out, blocks_want),
            "pages": (pages_out, pages_want),
            "assets": (getattr(self, "assets_copied", 0), assets_want),
            "tokens": (len(self.tokens), len(self.tokens)),
        }

    def _in_source(self, ref):
        """Does this reference resolve anywhere in the source site?"""
        name = ref.rsplit("/", 1)[-1]
        return any(p.name == name for p in self.src.rglob("*") if p.is_file())


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", required=True, help="finished site directory (contains index.html)")
    ap.add_argument("--name", required=True, help='client name, e.g. "Cecere Brothers"')
    ap.add_argument("--out", required=True, help="bundle output directory (recreated)")
    ap.add_argument("--force", "--allow-drops", dest="force", action="store_true",
                    help="exit 0 despite coverage shortfalls or warnings (default: fail loudly)")
    ap.add_argument("--quiet", action="store_true", help="summary and coverage only")
    a = ap.parse_args()

    b = Bundler(a.src, a.name, a.out)
    counts = b.run()
    cov = b.coverage()

    print(f"{a.name}: {counts['components']} components, {counts['pages']} pages, "
          f"{len(b.manifest)} files → {a.out}")
    if not a.quiet:
        for f in b.manifest:
            print("  " + f["path"])
    print("coverage: " + " · ".join(f"{k} {got}/{want}" for k, (got, want) in cov.items()))

    short = [k for k, (got, want) in cov.items() if got < want]
    for w in b.warnings:
        print("  warning: " + w, file=sys.stderr)
    # Pre-existing defects in the site itself. Reported so they get fixed, but they never
    # gate the bundle — the bundle is a faithful copy, and a copy of a broken link is
    # correct behaviour. Blaming the bundler for them would make the gate untrustworthy.
    for s in b.source_broken:
        print("  note (site defect, not bundling): " + s, file=sys.stderr)
    if short:
        print("  INCOMPLETE: " + ", ".join(short), file=sys.stderr)
    if (short or b.warnings) and not a.force:
        print("error: bundle is not a faithful copy of the site — refusing to report success.\n"
              "       Fix the cause, or re-run with --force if the gap is understood.",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
