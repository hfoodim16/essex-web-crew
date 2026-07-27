#!/usr/bin/env python3
"""design-pull.py — bring edits made inside Claude Design back into the real site.

The other half of design-bundle.py. That script is deterministic and offline, which is
what makes this one possible: re-bundling the current source reproduces exactly what was
last pushed, so anything the live project holds that the fresh bundle doesn't IS an edit
someone made in Design.

    python3 design-pull.py --check --src <mockup-dir> --name "Client" --fetched <dir>
    python3 design-pull.py --apply --src <mockup-dir> --name "Client" --fetched <dir>

`--fetched` is a directory of files pulled from the project with DesignSync `get_file`,
laid out on the same project-relative paths (styles.css, components/hero.html, …). This
script never talks to DesignSync; the design-pull skill does that half.

WHY A SUBCLASS AND NOT A REIMPLEMENTATION
Slug derivation, rewrite(), and the card scaffold all live in design-bundle.py. Copying
any of that here would let the two halves drift, and a mapping that is subtly wrong is
exactly the silent failure this repo keeps getting burned by. So we import the bundler,
run it, and record what it did.

THE SAFETY PROPERTY
After writing an edit back, the source is re-bundled and the regenerated card compared to
the fetched one. Equal means the write-back was faithful — proof, not hope. Any mismatch
restores every touched file and reports, so a partial edit can never be left behind.
"""
import argparse, difflib, importlib.util, pathlib, re, shutil, sys, tempfile


def load_bundler():
    """Import design-bundle.py (hyphen in the name → no plain `import`)."""
    p = pathlib.Path(__file__).with_name("design-bundle.py")
    spec = importlib.util.spec_from_file_location("design_bundle", p)
    if spec is None or spec.loader is None:
        sys.exit(f"error: cannot load {p}")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


DB = load_bundler()

# Paths we can map back to a source file, vs. paths that exist only in bundle space.
#   foundations/*  — GENERATED from :root tokens; the edit belongs on the token.
#   templates/*    — a copy of the whole page; applying it too would double-write
#                    every section that also has its own component card.
#   readme/theme/thumbnail — bundle furniture, no source equivalent.
REPORT_ONLY_PREFIXES = ("foundations/", "templates/")
IGNORED_PREFIXES = ("assets/", "vendor/", "lib/", "_")
IGNORED_EXACT = {"readme.md", "theme.json", "thumbnail.html", "_manifest.json"}


class ProvBundler(DB.Bundler):
    """A Bundler that remembers, per card, the markup it wrapped.

    `page()` always runs before the `add()` that stores its output (it's evaluated as
    that call's argument), and `_emit()` runs before both, so a small pending-slot
    relay captures all three facts without duplicating any bundler logic.
    """

    def __init__(self, *a, **k):
        self.prov = {}
        self._pending_body = None
        super().__init__(*a, **k)

    def page(self, group, name, subtitle, viewport, body, depth=1, scripts="", inline_css=""):
        self._pending_body = (body, depth)
        return super().page(group, name, subtitle, viewport, body, depth, scripts, inline_css)

    def add(self, rel, text=None, copy_from=None):
        super().add(rel, text, copy_from)
        if self._pending_body is not None and rel.endswith(".html"):
            body, depth = self._pending_body
            self.prov[rel] = {"body": body, "depth": depth}
        self._pending_body = None


def bundle(src, name, out):
    b = ProvBundler(src, name, out)
    b.run()
    return b


# --------------------------------------------------------------------------- mapping

def unrewrite(b, txt, depth):
    """Inverse of Bundler.rewrite() for a card at `depth` dirs below the bundle root.

    Only the base==src case is inverted. A nested mini-site's markup is rewritten
    against its OWN folder with a path prefix, and reversing that is ambiguous, so
    nested pages are report-only (see appliable()).
    """
    up = "../" * depth

    # Page links first, longest rel first, mirroring rewrite()'s own ordering so
    # "work/a/index.html" wins over a bare "index.html".
    for rel, slug in sorted(b.sibling_pages.items(), key=lambda kv: -len(kv[0])):
        txt = re.sub(rf'href\s*=\s*"{re.escape(up)}pages/{re.escape(slug)}\.html((?:[?#][^"]*)?)"',
                     rf'href="{rel}\1"', txt)
    txt = re.sub(rf'href\s*=\s*"{re.escape(up)}templates/landing/index\.html((?:[?#][^"]*)?)"',
                 r'href="index.html\1"', txt)
    txt = re.sub(rf'((?:src|href)\s*=\s*"){re.escape(up)}vendor/', r'\1vendor/', txt)

    # assets/ is one bundle dir but can come from several source dirs (a site using both
    # assets/ and public/). Resolve each ref against what's actually on disk rather than
    # guessing, so a two-dir site round-trips instead of silently repointing.
    def dir_for(rest):
        # Cache-busting queries and fragments are part of the ref, never the filename
        # (`harry.webp?v=4`), so strip them before asking the disk.
        bare = re.split(r"[?#]", rest, 1)[0]
        for d in b.asset_dirs:
            if (b.src / d / bare).is_file():
                return d
        return b.asset_dirs[0] if b.asset_dirs else "assets"

    txt = re.sub(rf'((?:src|href)\s*=\s*"){re.escape(up)}assets/([^"]+)"',
                 lambda m: f'{m.group(1)}{dir_for(m.group(2))}/{m.group(2)}"', txt)
    txt = re.sub(rf"""url\(\s*['"]?{re.escape(up)}assets/([^'")]+?)['"]?\s*\)""",
                 lambda m: f'url("{dir_for(m.group(1))}/{m.group(1)}")', txt)
    return txt


def appliable(b, path):
    """(True, kind) if `path` maps to a source file we can write back to."""
    if path in IGNORED_EXACT or path.startswith(IGNORED_PREFIXES):
        return False, "ignored"
    if path.startswith(REPORT_ONLY_PREFIXES):
        return False, "generated"
    if path == "styles.css":
        # >1 linked stylesheet means the bundle concatenated them; splitting the result
        # back apart is guesswork, so say so instead of picking wrong.
        return (len(b.css_files) == 1), ("css" if len(b.css_files) == 1 else "multi-css")
    if path.startswith("components/"):
        return True, "component"
    if path.startswith("pages/"):
        slug = path[len("pages/"):-len(".html")]
        for rel, s in b.sibling_pages.items():
            if s == slug:
                # Nested mini-sites rewrite against their own folder — not invertible here.
                return ("/" not in rel), ("page" if "/" not in rel else "nested-page")
        # No sibling match → an SPA `.page` view. activate() strips `hidden` and forces
        # .is-active, a lossy transform, so this can't be reversed cleanly either.
        return False, "spa-view"
    return False, "unknown"


def edited_body(expected_card, actual_card, known_body):
    """Pull the edited markup out of a card by anchoring on the scaffold, not parsing it.

    The card is `prefix + body + suffix` where prefix/suffix are the deterministic
    scaffold page() built. Splitting the EXPECTED card on the body we know gives those
    two strings exactly, with no assumptions about defs/scripts/fonts. If the actual card
    still carries both, whatever sits between them is the edit.

    Returns (body, None) or (None, reason).
    """
    if expected_card.count(known_body) != 1:
        return None, "cannot anchor the card scaffold (body text is not unique)"
    i = expected_card.index(known_body)
    prefix, suffix = expected_card[:i], expected_card[i + len(known_body):]
    if not actual_card.startswith(prefix) or not actual_card.endswith(suffix):
        return None, "the card's scaffold (head/scripts) was edited, not just its content"
    inner = actual_card[len(prefix):len(actual_card) - len(suffix)]
    return inner, None


# --------------------------------------------------------------------------- write-back

def locate(text, exp, act, i1, i2, j1, j2, unrw):
    """Grow one changed chunk outward until its source form is unique in `text`.

    The regions around a change are identical in both bodies, so widening the window
    by k chars on the expected side means the same k chars on the actual side — which
    is why the two slices stay aligned as they grow.
    """
    lo, hi = i1, i2
    for _ in range(80):
        old = unrw(exp[lo:hi])
        if old.strip() and text.count(old) == 1:
            return old, unrw(act[j1 - (i1 - lo):j2 + (hi - i2)])
        if lo == 0 and hi == len(exp):
            return None, None
        lo, hi = max(0, lo - 60), min(len(exp), hi + 60)
    return None, None


GAP = 200   # chars: two changes closer than this are really one edit


def regions(exp, act):
    """Changed spans, coalesced. Character diffing shatters one edit into slivers.

    Rewording a heading produced FOUR opcodes ('Con'->'Speak wi', +'h P', +'ul dire',
    ' the office.'->'ly'). Applied separately, each needs surrounding context to be
    locatable, those context windows overlap, and the second lookup fails because the
    first replacement already changed that text. Merging anything within GAP turns it
    back into the single edit it always was.
    """
    spans = [(i1, i2, j1, j2) for tag, i1, i2, j1, j2
             in difflib.SequenceMatcher(None, exp, act, autojunk=False).get_opcodes()
             if tag != "equal"]
    out = []
    for s in spans:
        if out and s[0] - out[-1][1] <= GAP:
            p = out[-1]
            out[-1] = (min(p[0], s[0]), max(p[1], s[1]), min(p[2], s[2]), max(p[3], s[3]))
        else:
            out.append(s)
    return out


def targeted_apply(text, exp, act, unrw):
    """Apply ONLY what changed between the two card bodies, in place.

    Deliberately not a whole-block overwrite. A card body is a LOSSY projection of the
    source: the bundler strips the page's own <script> tags (a card loads lib/site.js
    instead), so writing a card body back wholesale silently deletes them — it cost
    contact.html its main.js in testing. Replacing only the changed chunks leaves
    everything the bundler dropped exactly where it was.

    Right-to-left, so an earlier region's context is still intact when we look for it.
    """
    for i1, i2, j1, j2 in reversed(regions(exp, act)):
        old, new = locate(text, exp, act, i1, i2, j1, j2, unrw)
        if old is None:
            return None, "could not pin the edited text to one place in the source"
        text = text.replace(old, new, 1)
    return text, None


def apply_one(b, path, kind, expected_body, new_body, writes):
    """Stage the source edit for one card into `writes` (path -> new text)."""
    if kind == "css":
        # No projection loss here: styles.css is the stylesheet with url()s rewritten.
        target = b.src / b.css_files[0].lstrip("./")
        writes[target] = unrewrite(b, new_body, 0)
        return target, None

    if kind == "component":
        target = b.index
    elif kind == "page":
        slug = path[len("pages/"):-len(".html")]
        rel = next(r for r, s in b.sibling_pages.items() if s == slug)
        target = b.src / rel
    else:
        return None, f"unsupported kind: {kind}"

    depth = b.prov.get(path, {}).get("depth", 1)
    current = writes.get(target, target.read_text(encoding="utf-8"))
    out, why = targeted_apply(current, expected_body, new_body,
                              lambda s: unrewrite(b, s, depth))
    if out is None:
        return None, why
    writes[target] = out
    return target, None


# --------------------------------------------------------------------------- drift

def compare(b, out, fetched):
    """Classify every fetched path against the freshly built bundle."""
    drift, missing, clean = [], [], 0
    for f in sorted(fetched.rglob("*")):
        if not f.is_file():
            continue
        path = f.relative_to(fetched).as_posix()
        if path in IGNORED_EXACT or path.startswith(IGNORED_PREFIXES):
            continue
        built = out / path
        if not built.exists():
            missing.append(path)
            continue
        try:
            actual = f.read_text(encoding="utf-8")
            expected = built.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if actual == expected:
            clean += 1
        else:
            ok, kind = appliable(b, path)
            drift.append({"path": path, "kind": kind, "appliable": ok,
                          "expected": expected, "actual": actual})
    return drift, missing, clean


REASONS = {
    "generated": "generated from :root tokens — change the token in your stylesheet instead",
    "multi-css": "site links several stylesheets; the bundle concatenates them, so the "
                 "split back apart would be guesswork",
    "nested-page": "nested sub-site — its paths are rewritten against its own folder",
    "spa-view": "SPA view — the bundler forces it visible, which isn't cleanly reversible",
    "unknown": "no source file maps to this path (created inside Design?)",
}


def report(drift, missing, clean, verbose):
    print(f"compared {clean + len(drift)} files · {clean} unchanged · {len(drift)} edited in Design")
    for d in drift:
        mark = "APPLY" if d["appliable"] else " skip"
        why = "" if d["appliable"] else f"  ({REASONS.get(d['kind'], d['kind'])})"
        print(f"  [{mark}] {d['path']}{why}")
        if verbose:
            diff = difflib.unified_diff(
                d["expected"].splitlines(), d["actual"].splitlines(),
                fromfile="site", tofile="design", lineterm="", n=1)
            for line in list(diff)[2:40]:
                print("        " + line)
    for m in missing:
        print(f"  [ skip] {m}  (in the project but not produced by the bundler)")


# --------------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", required=True, help="the site directory (contains index.html)")
    ap.add_argument("--name", required=True, help='client name, same as the push used')
    ap.add_argument("--fetched", required=True, help="dir of files pulled with DesignSync get_file")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="report drift, change nothing")
    mode.add_argument("--apply", action="store_true", help="write the edits back into the site")
    ap.add_argument("--verbose", action="store_true", help="show a diff per drifted file")
    a = ap.parse_args()

    src, fetched = pathlib.Path(a.src), pathlib.Path(a.fetched)
    if not fetched.is_dir():
        sys.exit(f"error: no such fetched dir: {fetched}")

    tmp = pathlib.Path(tempfile.mkdtemp(prefix="ds-pull-"))
    try:
        b = bundle(src, a.name, tmp / "expected")
        drift, missing, clean = compare(b, tmp / "expected", fetched)
        report(drift, missing, clean, a.verbose or a.check)

        if not drift:
            print("\nno Design edits to pull — the site and the project agree.")
            return 0

        todo = [d for d in drift if d["appliable"]]
        if a.check:
            print(f"\n{len(todo)} of {len(drift)} can be applied automatically. "
                  f"Re-run with --apply.")
            return 1

        if not todo:
            print("\nnothing can be applied automatically; see the reasons above.")
            return 1

        # Stage every edit in memory, then write once — so a failure part-way through
        # never leaves the site half-edited.
        writes, failures, applied = {}, [], {}
        for d in todo:
            prov = b.prov.get(d["path"])
            if not prov and d["kind"] != "css":
                failures.append((d["path"], "card not produced by this bundle"))
                continue
            if d["kind"] == "css":
                new_body = d["actual"]
            else:
                new_body, why = edited_body(d["expected"], d["actual"], prov["body"])
                if new_body is None:
                    failures.append((d["path"], why))
                    continue
            expected_body = "" if d["kind"] == "css" else prov["body"]
            target, why = apply_one(b, d["path"], d["kind"], expected_body, new_body, writes)
            if target is None:
                failures.append((d["path"], why))
            else:
                applied[d["path"]] = (d["kind"], new_body)

        for p, why in failures:
            print(f"  could not apply {p}: {why}", file=sys.stderr)
        if not writes:
            print("error: no edit could be applied.", file=sys.stderr)
            return 1

        backup = {t: t.read_text(encoding="utf-8") for t in writes}
        for t, text in writes.items():
            t.write_text(text, encoding="utf-8")
        print("\nwrote: " + ", ".join(sorted(str(t.relative_to(src)) for t in writes)))

        # The proof. Re-bundle the edited source and require each applied card to now
        # produce exactly the markup Design holds.
        #
        # Compare BODIES, not whole card files. A card's @dsCard marker carries a
        # subtitle (and name) DERIVED from the section's own heading, so editing a
        # heading legitimately changes the regenerated scaffold while the fetched copy
        # still shows the old one. Comparing whole files would fail every headline edit —
        # the most common edit there is. The body is the thing we actually wrote back.
        b2 = bundle(src, a.name, tmp / "verify")
        bad, renamed = [], []
        for path, (kind, new_body) in applied.items():
            if kind == "css":
                got = tmp / "verify" / "styles.css"
                ok = got.exists() and got.read_text(encoding="utf-8") == new_body
            elif path not in b2.prov:
                # The card no longer exists under this path. Card names come from
                # id -> role class -> aria-label -> heading, so a heading edit can
                # rename the card — and per design-push, a NEW path never appears in
                # an already-compiled project. Worth shouting about, not failing on.
                renamed.append(path)
                continue
            else:
                ok = b2.prov[path]["body"] == new_body
            if not ok:
                bad.append(path)

        if bad:
            for t, text in backup.items():
                t.write_text(text, encoding="utf-8")
            print("error: round-trip check FAILED for " + ", ".join(bad) +
                  "\n       the site has been restored; nothing was changed.", file=sys.stderr)
            return 1

        verified = len(applied) - len(renamed)
        if verified:
            print(f"round-trip verified: {verified} of {len(applied)} card(s) now rebuild "
                  f"exactly as Design has them.")
        if renamed:
            print("\nWARNING — these cards were RENAMED by the edit (card names derive from\n"
                  "the section's heading), so their bundle path changed:\n  " +
                  "\n  ".join(renamed) +
                  "\n  The edit is safely in the site, but a re-push will write the new path\n"
                  "  and the project's card index will never show it. Push to a FRESH\n"
                  "  project instead — see design-push, 're-push or fresh project?'.")
        return 1 if failures else 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
