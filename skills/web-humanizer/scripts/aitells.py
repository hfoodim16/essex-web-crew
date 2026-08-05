#!/usr/bin/env python3
"""aitells — website-shaped AI tells in built pages.

Usage:
    python3 skills/web-humanizer/scripts/aitells.py prospects/<slug>/mockup/index.html
    python3 skills/web-humanizer/scripts/aitells.py prospects/*/mockup/*.html
    python3 skills/web-humanizer/scripts/aitells.py <page.html> --list
    python3 skills/web-humanizer/scripts/aitells.py <page.html> --json

Companion to trade-copy's copycheck.py, not a replacement. copycheck measures
REGISTER -- em dashes, contractions, triads, motif words, cutesy language. This
measures the SHAPE of a generated web page: heroes that open with a verb any
industry could use, cards titled with two abstract nouns, pages where nothing
can be checked against reality, cards machine-stamped to the same length.

Nothing here re-checks a copycheck gate. Run copycheck first, this second, and
the client's voice-spec.md outranks both.

Real review quotes, nav, and footer are excluded from every hard check -- never
edit a real testimonial to satisfy a script.

Exit code 0 = all hard checks pass, 1 = at least one FAIL.
"""

import sys
import re
import json
import statistics
from html.parser import HTMLParser
from pathlib import Path

# ---------------------------------------------------------------- thresholds
# Calibrated against the same corpus copycheck.py uses -- dasilva-associates
# (reference) plus cedar-grove-transmission and john-sessa-cpa -- then swept
# across all 23 built pages in prospects/. Every signed-off page must exit 0
# untouched; a threshold that fails one of those is wrong, because sign-off
# freezes a prospect (CLAUDE.md) and the loop would never close.
#
# Sweep at time of writing: 0 hard-check hits across all 22 built pages. The
# checks are aimed at shapes this crew's gates already keep out by hand, so the
# script's job is to keep them out when nobody is reading closely.
#
# One threshold was loosened during that sweep, and the reason is worth keeping:
# hero_verbs originally fired on any sentence-initial hit anywhere on the page,
# which failed happy-trees-by-mgm/services.html on "Elevating consists of the
# removal, or trimming, of the lower limbs" -- the arborist's own term for the
# Tree Elevation service, on a signed-off page. The check is now scoped to
# headings and the hero subheadline, where the tell actually lives; body hits are
# an advisory. A word that is real trade vocabulary mid-page is still capped at
# two uses by copycheck.py's motif gate.
T = {
    "hero_verbs": 0,          # interchangeable hero verbs in a heading or sentence-initial
    "abstract_pairs": 0,      # two-word headings built from two abstractions
    "vocab_cluster": 2,       # <= 2 DISTINCT ai-vocab words page-wide (0 in the h1)
    "vague_audience": 0,      # "for modern homeowners", "businesses of all sizes"
    "min_falsifiable": 1,     # >= 1 visible claim carrying a checkable number
    "symmetry_run": 4,        # 4+ consecutive same-tag blocks of IDENTICAL length
    "symmetry_floor": 8,      # ...counting only blocks of 8+ words (service lists are fine)
}
ADVISORY = ["body_verb_openers", "comma_triads", "rhythm_stdev", "loose_symmetry",
            "unattributed_reviews", "no_mechanism", "vocab_hits"]

# ------------------------------------------------------------------ lexicons
# H1: the verbs that open a hero on any site in any industry. Position matters
# more than frequency here, which is why copycheck's motif cap (2 uses per page)
# does not cover it -- one "Transform your yard" in an h1 passes that cap and is
# still the loudest tell on the page. Overlap with banlist.md is deliberate and
# scoped to sentence-initial position.
HERO_VERBS = [
    "empower", "empowering", "unlock", "unlocking", "unleash", "unleashing",
    "transform", "transforming", "elevate", "elevating", "supercharge",
    "revolutionize", "revolutionise", "reimagine", "reinvent", "maximize",
    "optimize", "streamline", "amplify", "accelerate",
]
# ...plus these, which are only a tell in a heading (they are ordinary verbs in
# body copy: "you'll discover a cracked line behind the wall").
HERO_VERBS_HEADING_ONLY = ["discover", "experience", "introducing", "unveiling"]

# H3: AI vocabulary. Kept DISJOINT from trade-copy/references/banlist.md so a
# single word is never flagged twice by two scripts with two different fixes.
# banlist.md already owns: seamless, elevate, transform, cutting-edge,
# state-of-the-art, solutions, holistic, excellence, premier, unparalleled,
# curated, bespoke, timeless, meticulous, craftsmanship, showcase, boasts.
AI_VOCAB = [
    "effortless", "effortlessly", "hassle-free", "worry-free", "leverage",
    "leveraging", "robust", "scalable", "game-changer", "game-changing",
    "world-class", "best-in-class", "industry-leading", "next-level",
    "top-notch", "one-stop", "innovative", "innovation", "synergy", "delve",
    "myriad", "plethora", "paramount", "pivotal", "vibrant", "bustling",
    "nuanced", "comprehensive", "cornerstone", "navigate",
    "future-proof", "future-ready", "turnkey", "value-added", "customer-centric",
    "results-driven", "laser-focused", "second to none", "unmatched",
]
VAGUE_AUDIENCE = re.compile(
    # "for today's homeowners" and "for today's busy homeowners" alike -- the
    # adjective stack between the opener and the plural noun is part of the shape.
    r"\bfor (?:the )?(?:modern|today's|today’s|busy|growing|discerning|savvy|"
    r"forward-thinking|ambitious)\s+(?:[\w'’-]+\s+){0,2}[\w'’-]+s\b"
    r"|\b(?:businesses|homeowners|clients|companies|teams|customers) of all sizes\b"
    r"|\bof all shapes and sizes\b", re.I)

ABSTRACT_ADJ = {
    "seamless", "effortless", "robust", "comprehensive", "innovative", "superior",
    "premium", "advanced", "complete", "total", "expert", "professional",
    "reliable", "trusted", "modern", "smart", "proven", "exceptional",
    "outstanding", "unmatched", "personalized", "tailored", "holistic",
    "strategic", "dynamic", "efficient", "streamlined", "integrated",
}
ABSTRACT_NOUN = {
    "integration", "solutions", "solution", "excellence", "innovation",
    "management", "efficiency", "quality", "results", "performance",
    "expertise", "value", "workmanship", "craftsmanship", "support",
    "delivery", "approach", "process", "standards", "commitment",
    "capabilities", "offerings", "experiences", "outcomes", "synergy",
    "optimization", "transformation", "empowerment", "care", "service",
    "services", "experience",
}
OUTCOME_VERB = re.compile(
    r"\b(?:save|saves|grow|grows|boost|boosts|improve|improves|increase|increases|"
    r"enhance|enhances|maximize|maximizes|streamline|streamlines|optimize|optimizes)\b",
    re.I)

# ------------------------------------------------------------------- parsing
# Extract, VOID_TAGS, SKIP_TAGS, SKIP_CLASS, BLOCK_TAGS and words() are vendored
# from skills/trade-copy/scripts/copycheck.py so both scripts read a page the
# same way. Vendored rather than imported: install.sh copies each skill dir into
# ~/.claude/skills/ independently, so a cross-skill import breaks the moment one
# skill is installed without the other. Port fixes in BOTH directions.
SKIP_TAGS = {"script", "style", "head", "title", "noscript", "svg", "nav", "footer", "form"}
SKIP_CLASS = re.compile(r"review|testimonial|quote|pullquote|pull-quote", re.I)
BLOCK_TAGS = {"p", "li", "h1", "h2", "h3", "h4", "h5", "h6", "dd", "dt", "figcaption", "summary"}
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
             "meta", "param", "source", "track", "wbr"}

PHONE = re.compile(r"\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}")
ZIP = re.compile(r"\b\d{5}(?:-\d{4})?\b")
PROPER = re.compile(r"(?<![.!?]\s)(?<!^)\b[A-Z][a-z]{2,}\b")
NAME_ATTRIB = re.compile(r"[—–-]\s*[A-Z][a-z]+|\b[A-Z][a-z]+\s+[A-Z]\.|\b[A-Z][a-z]+,\s+[A-Z]")


class Extract(HTMLParser):
    """Pull visible body copy, dropping chrome and real review quotes.

    Keeps an explicit element stack so unclosed/void tags cannot corrupt the
    skip state -- an earlier depth-counter version silently swallowed whole pages.
    """

    def __init__(self):
        super().__init__()
        self.blocks = []          # (tag, text, line)
        self._stack = []          # [(tag, is_skip_root)]
        self._skip = 0            # count of open skip roots
        self._buf = []
        self._cur = None
        self._line = 0

    def handle_starttag(self, tag, attrs):
        if tag in VOID_TAGS:
            return
        cls = dict(attrs).get("class", "") or ""
        is_skip = tag in SKIP_TAGS or tag == "blockquote" or bool(SKIP_CLASS.search(cls))
        self._stack.append((tag, is_skip))
        if is_skip:
            self._skip += 1
            return
        if self._skip:
            return
        if tag in BLOCK_TAGS:
            self._flush()
            self._cur = tag
            self._line = self.getpos()[0]
        elif self._cur and self._cur not in BLOCK_TAGS:
            self._flush()

    def handle_startendtag(self, tag, attrs):
        return

    def handle_endtag(self, tag):
        if tag in VOID_TAGS:
            return
        if tag in BLOCK_TAGS or (self._cur and self._cur not in BLOCK_TAGS):
            self._flush()
        for i in range(len(self._stack) - 1, -1, -1):
            if self._stack[i][0] == tag:
                for _, was_skip in self._stack[i:]:
                    if was_skip:
                        self._skip -= 1
                del self._stack[i:]
                return

    def handle_data(self, data):
        if self._skip:
            return
        if self._cur is None:
            if not data.strip() or not self._stack:
                return
            self._cur = self._stack[-1][0]
            self._line = self.getpos()[0]
        self._buf.append(data)

    def _flush(self):
        if self._cur and self._buf:
            text = re.sub(r"\s+", " ", " ".join(self._buf)).strip()
            text = re.sub(r"\s+([,.;:!?])", r"\1", text)
            if text:
                self.blocks.append((self._cur, text, self._line))
        self._buf, self._cur = [], None


class ExtractReviews(HTMLParser):
    """The inverse of Extract: capture ONLY what Extract throws away as a review.

    Read-only. Real quotes are never edited, so nothing here can hard-fail. It
    exists to catch the other failure -- a testimonial nobody wrote, with no name
    on it, which reads as invented whether or not it is.
    """

    def __init__(self):
        super().__init__()
        self.quotes = []
        self._stack = []
        self._depth = 0
        self._buf = []
        self._line = 0

    def handle_starttag(self, tag, attrs):
        if tag in VOID_TAGS:
            return
        cls = dict(attrs).get("class", "") or ""
        is_root = tag == "blockquote" or bool(SKIP_CLASS.search(cls))
        self._stack.append((tag, is_root))
        if is_root:
            if self._depth == 0:
                self._line = self.getpos()[0]
            self._depth += 1

    def handle_startendtag(self, tag, attrs):
        return

    def handle_endtag(self, tag):
        if tag in VOID_TAGS:
            return
        for i in range(len(self._stack) - 1, -1, -1):
            if self._stack[i][0] == tag:
                closed = sum(1 for _, root in self._stack[i:] if root)
                del self._stack[i:]
                if closed:
                    self._depth -= closed
                    if self._depth <= 0:
                        self._depth = 0
                        self._flush()
                return

    def handle_data(self, data):
        if self._depth:
            self._buf.append(data)

    def _flush(self):
        if self._buf:
            text = re.sub(r"\s+", " ", " ".join(self._buf)).strip()
            if len(words(text)) >= 5:
                self.quotes.append((text, self._line))
        self._buf = []


def words(s):
    return re.findall(r"[A-Za-z][A-Za-z'’-]*", s)


def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


# --------------------------------------------------------------- hard checks
def _opens_with(s, vocab):
    first = (words(s) or [""])[0].lower()
    hyph = re.match(r"[A-Za-z-]+", s.strip())
    hyph = hyph.group(0).lower() if hyph else ""
    for v in vocab:
        if first == v or hyph == v:
            return v
    return None


def hero_verb_hits(blocks):
    """Verbs that open a headline on any site in any industry.

    Scoped to HEADINGS and the hero subheadline, which is where the tell lives --
    "Elevate Your Outdoor Living Experience" is a hero, and a hero is the one line
    a customer always reads. Body sentences are reported as an advisory instead
    (see body_verb_openers): several of these words are real trade vocabulary in
    the middle of a page. A tree service explaining "Elevating consists of the
    removal of the lower limbs" is using the arborist's own term for the service,
    and copycheck.py's motif cap already limits how often such a word can recur.
    """
    vocab = HERO_VERBS + HERO_VERBS_HEADING_ONLY
    hits = []
    lead = _lead_index(blocks)
    for i, (tag, text, line) in enumerate(blocks):
        if not tag.startswith("h") and i != lead:
            continue
        for s in ([text] if tag.startswith("h") else sentences(text)[:1]):
            v = _opens_with(s, vocab)
            if v:
                hits.append((line, v, s))
                break
    return hits


def _lead_index(blocks):
    """Index of the hero subheadline: the first paragraph after the h1."""
    for i, (tag, _, _) in enumerate(blocks):
        if tag == "h1":
            for j in range(i + 1, len(blocks)):
                if blocks[j][0] in {"p", "li", "dd"}:
                    return j
            return -1
    return -1


def body_verb_openers(blocks):
    """The same verbs opening a sentence in body copy. Advisory.

    Sometimes the tell has just moved down the page; sometimes the word is the
    trade's own ("Elevating consists of..." on a tree service's service page).
    A reader can tell those apart in one glance, so this reports rather than fails.
    """
    out = []
    lead = _lead_index(blocks)
    for i, (tag, text, line) in enumerate(blocks):
        if tag.startswith("h") or i == lead:
            continue
        for s in sentences(text):
            v = _opens_with(s, HERO_VERBS)
            if v:
                out.append((line, v, s))
                break
    return out


def abstract_pair_hits(blocks):
    """Card titles that name a category of goodness instead of a service.

    "Seamless Integration" over "Transmission Rebuilds". Two words, both
    abstractions, and a competitor could paste it onto their own site unchanged.
    Only h2-h4 -- an h1 is gated by copycheck's hero length and word checks.
    """
    hits = []
    for tag, text, line in blocks:
        if tag not in {"h2", "h3", "h4"}:
            continue
        w = [x.lower().strip("'’-") for x in words(text)]
        if len(w) != 2:
            continue
        a, b = w
        both_nouns = a in ABSTRACT_NOUN and b in ABSTRACT_NOUN
        adj_noun = a in ABSTRACT_ADJ and b in ABSTRACT_NOUN
        if both_nouns or adj_noun:
            hits.append((line, text))
    return hits


def vocab_hits(body, h1):
    """Distinct AI-vocabulary words page-wide, plus any in the hero.

    A cluster is the tell, not a single word: "comprehensive" alone is a word an
    accountant would use about a return. Three of these in one page is a
    fingerprint. Threshold is on DISTINCT words so a legitimately repeated one
    (a shop that really does say "turnkey") costs the page once, not four times.
    """
    found, in_h1 = {}, []
    for w in AI_VOCAB:
        pat = rf"\b{re.escape(w)}\b" if " " in w or "-" in w else rf"\b{re.escape(w)}\w*\b"
        n = len(re.findall(pat, body, re.I))
        if n:
            found[w] = n
            if re.search(pat, h1, re.I):
                in_h1.append(w)
    return dict(sorted(found.items(), key=lambda kv: -kv[1])), in_h1


def falsifiable_blocks(blocks):
    """Visible claims carrying a number a customer could check.

    Phone numbers and zips are stripped first: "Call (973) 555-0134" proves
    nothing about the business. A year, a count, a price, a response time, a
    service radius -- any of those pass. This is a FLOOR, deliberately low. One
    checkable fact on a page is the minimum, not the target.
    """
    out = []
    for tag, text, line in blocks:
        stripped = ZIP.sub(" ", PHONE.sub(" ", text))
        if re.search(r"\d", stripped):
            out.append((line, text))
    return out


def symmetry_runs(blocks, tolerance=0, floor=None, min_run=None):
    """Consecutive same-tag blocks stamped to the same length.

    Hand-written cards come out uneven because the facts are uneven. Four cards
    at exactly 27 words each means the length was the specification. Blocks under
    `floor` words are ignored -- a service list of one-word <li>s is not a tell,
    it is a list.
    """
    floor = T["symmetry_floor"] if floor is None else floor
    min_run = T["symmetry_run"] if min_run is None else min_run
    runs, cur = [], []
    for tag, text, line in blocks:
        n = len(words(text))
        if n < floor:
            if len(cur) >= min_run:
                runs.append(cur)
            cur = []
            continue
        if cur and cur[-1][0] == tag and abs(cur[-1][1] - n) <= tolerance:
            cur.append((tag, n, line, text))
        else:
            if len(cur) >= min_run:
                runs.append(cur)
            cur = [(tag, n, line, text)]
    if len(cur) >= min_run:
        runs.append(cur)
    return runs


# ---------------------------------------------------------------- advisories
def comma_triad_headings(blocks):
    """"Fast, Fair, and Local" -- the rule of three in list form.

    Advisory, not a gate. A trade site legitimately lists three services in a
    heading. It becomes a tell when all three are abstractions, and only a reader
    can tell those apart.
    """
    out = []
    for tag, text, line in blocks:
        if tag.startswith("h") and re.match(
                r"^[\w'’-]+,\s+[\w'’-]+,?\s+(?:and|&)\s+[\w'’-]+\.?$", text.strip()):
            out.append((line, text))
    return out


def rhythm_stdev(paras):
    """Sentence-length spread. Human copy varies; generated copy metronomes.

    Advisory: a page of short deliberate lines is a style, not a failure. Printed
    so a reader can decide whether the evenness is a choice.
    """
    lens = [len(words(s)) for t in paras for s in sentences(t) if len(words(s)) > 1]
    if len(lens) < 10:
        return None
    return round(statistics.pstdev(lens), 2), len(lens)


def no_mechanism(paras):
    """A promised outcome with nothing behind it.

    "We help you save money" with no number, no proper noun, no named mechanism.
    Advisory because the fix is a fact the agent may not have -- if the client
    never said it, the line gets cut, not filled in.
    """
    out = []
    for t in paras:
        for s in sentences(t):
            if OUTCOME_VERB.search(s) and not re.search(r"\d", s) and not PROPER.search(s):
                out.append(s)
    return out


def unattributed_reviews(quotes):
    """Testimonials with no name on them.

    Never a hard fail: real quotes are exempt from every rule in this project,
    and the fix for a missing name is asking the client, not editing the quote.
    """
    return [(line, t) for t, line in quotes if not NAME_ATTRIB.search(t)]


# ------------------------------------------------------------------ analysis
def analyze(path):
    # The Critic passes globs (mockup/*.html). A shell that matches nothing hands
    # the pattern through literally, and a page can move between runs -- say so
    # and keep going rather than dying on a traceback mid-audit.
    try:
        raw = Path(path).read_text(errors="replace")
    except (FileNotFoundError, IsADirectoryError):
        print(f"=== {path}\n    [SKIP] no such page", file=sys.stderr)
        return None
    p = Extract()
    p.feed(raw)
    p._flush()
    blocks = p.blocks
    q = ExtractReviews()
    q.feed(raw)
    q._flush()

    paras = [t for tag, t, _ in blocks if tag in {"p", "li", "dd"} and len(words(t)) > 2]
    h1 = next((t for tag, t, _ in blocks if tag == "h1"), "")
    body = " ".join(t for _, t, _ in blocks)
    wc = len(words(body))
    if wc == 0:
        return None

    vocab, vocab_in_h1 = vocab_hits(body, h1)
    tight = symmetry_runs(blocks, tolerance=0)
    loose = symmetry_runs(blocks, tolerance=2, min_run=3)

    return {
        "file": str(path),
        "words": wc,
        "h1": h1,
        "hero_verbs": hero_verb_hits(blocks),
        "body_verbs": body_verb_openers(blocks),
        "abstract_pairs": abstract_pair_hits(blocks),
        "vocab": vocab,
        "vocab_distinct": len(vocab),
        "vocab_in_h1": vocab_in_h1,
        "vague_audience": [(t, m.group(0)) for _, t, _ in blocks
                           for m in [VAGUE_AUDIENCE.search(t)] if m],
        "falsifiable": falsifiable_blocks(blocks),
        "symmetry": [[(n, line, text) for _, n, line, text in run] for run in tight],
        "loose_symmetry": [[(n, line, text) for _, n, line, text in run] for run in loose],
        "comma_triads": comma_triad_headings(blocks),
        "rhythm": rhythm_stdev(paras),
        "no_mechanism": no_mechanism(paras),
        "unattributed_reviews": unattributed_reviews(q.quotes),
        "reviews": len(q.quotes),
        "blocks": blocks,
    }


def verdict(r):
    """Return [(check, ok, detail), ...] for the hard gates only."""
    v = []
    v.append(("hero verb openers", len(r["hero_verbs"]) <= T["hero_verbs"],
              f"{len(r['hero_verbs'])} (max {T['hero_verbs']}): " + ", ".join(
                  f"'{w}' line {ln}" for ln, w, _ in r["hero_verbs"][:4])
              if r["hero_verbs"] else "none"))
    v.append(("abstract-pair titles", len(r["abstract_pairs"]) <= T["abstract_pairs"],
              f"{len(r['abstract_pairs'])} (max {T['abstract_pairs']}): " + ", ".join(
                  f"'{t}' line {ln}" for ln, t in r["abstract_pairs"][:4])
              if r["abstract_pairs"] else "none"))
    ok_vocab = r["vocab_distinct"] <= T["vocab_cluster"] and not r["vocab_in_h1"]
    detail = f"{r['vocab_distinct']} distinct (max {T['vocab_cluster']})"
    if r["vocab_in_h1"]:
        detail += f"; in the hero: {', '.join(r['vocab_in_h1'])}"
    if r["vocab"]:
        detail += " -- " + ", ".join(f"{w} x{c}" for w, c in list(r["vocab"].items())[:6])
    v.append(("ai-vocab cluster", ok_vocab, detail))
    v.append(("vague audience", len(r["vague_audience"]) <= T["vague_audience"],
              f"{len(r['vague_audience'])}: " + ", ".join(
                  f"'{m}'" for _, m in r["vague_audience"][:3])
              if r["vague_audience"] else "none"))
    v.append(("falsifiable claim floor", len(r["falsifiable"]) >= T["min_falsifiable"],
              f"{len(r['falsifiable'])} checkable claim(s) (min {T['min_falsifiable']})"))
    v.append(("card symmetry", not r["symmetry"],
              f"{len(r['symmetry'])} run(s) of {T['symmetry_run']}+ blocks at identical length"
              if r["symmetry"] else "none"))
    return v


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    if not args:
        print(__doc__)
        return 2

    results = [r for r in (analyze(a) for a in args) if r]

    if "--list" in flags:
        # Every visible string. Put a verdict on each line BEFORE editing:
        # fine / could be any company / no fact in it / stamped to length.
        for r in results:
            print(f"\n=== {r['file']}  ({len(r['blocks'])} visible strings)")
            for tag, text, line in r["blocks"]:
                print(f"  {line:>5}  {tag:<4}  {text}")
        print("\nAsk of every line: could a competitor paste this onto their own site?")
        return 0

    if "--json" in flags:
        for r in results:
            r.pop("blocks", None)
        print(json.dumps(results, indent=2, default=str))
        return 0

    failed = False
    for r in results:
        print(f"\n=== {r['file']}  ({r['words']} words)")
        print(f"    hero: {r['h1'][:90]}")
        for name, ok, detail in verdict(r):
            print(f"    [{'PASS' if ok else 'FAIL'}] {name:24} {detail}")
            failed |= not ok

        for ln, text in r["abstract_pairs"]:
            print(f"      line {ln}: '{text}' -- name the service, not the category")
        for ln, v, s in r["hero_verbs"][:6]:
            print(f"      line {ln} ['{v}']: {s[:120]}")
        for run in r["symmetry"]:
            print(f"      {len(run)} blocks at exactly {run[0][0]} words, "
                  f"lines {run[0][1]}-{run[-1][1]}")

        if r["body_verbs"]:
            print("    [ -- ] hero-style verb opening a body sentence (advisory; a tell that")
            print("           moved down the page, or the trade's own word -- read it):")
            for ln, v, s in r["body_verbs"][:4]:
                print(f"      line {ln} ['{v}']: {s[:120]}")
        if r["comma_triads"]:
            print("    [ -- ] comma-triad headings (advisory; fine for three real services,")
            print("           a tell when all three are abstractions):")
            for ln, t in r["comma_triads"][:4]:
                print(f"      line {ln}: {t}")
        if r["rhythm"] and r["rhythm"][0] < 3:
            sd, n = r["rhythm"]
            print(f"    [ -- ] sentence-length spread {sd} across {n} sentences   (advisory;")
            print("           under 3 means every sentence is the same size -- read it aloud)")
        if r["loose_symmetry"] and not r["symmetry"]:
            run = r["loose_symmetry"][0]
            print(f"    [ -- ] {len(run)} near-identical card lengths around {run[0][0]} words, "
                  f"lines {run[0][1]}-{run[-1][1]}   (advisory)")
        if r["no_mechanism"]:
            print("    [ -- ] outcome promised with no number, name, or mechanism (advisory;")
            print("           if the client never said it, cut the line -- do not invent one):")
            for s in r["no_mechanism"][:4]:
                print(f"      - {s[:130]}")
        if r["unattributed_reviews"]:
            print(f"    [ -- ] {len(r['unattributed_reviews'])} of {r['reviews']} review blocks "
                  "carry no name (advisory; ask the client, never edit a real quote):")
            for ln, t in r["unattributed_reviews"][:3]:
                print(f"      line {ln}: {t[:110]}")
        if r["vocab"] and r["vocab_distinct"] <= T["vocab_cluster"]:
            print("    flagged vocabulary (under the cluster threshold, still worth a look): "
                  + ", ".join(f"{w} x{c}" for w, c in r["vocab"].items()))

    if failed:
        print("\nChecks failed. Fix them, then read every line with --list -- the shapes")
        print("that matter most (could a competitor say this?) never trip a threshold.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
