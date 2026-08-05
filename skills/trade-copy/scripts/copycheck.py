#!/usr/bin/env python3
"""copycheck — mechanical copy-voice checks for Essex Web Crew mockups.

Usage:
    python3 copycheck.py prospects/<slug>/mockup/index.html
    python3 copycheck.py prospects/*/mockup/index.html --compare

Reads visible body copy out of a built page and measures the things that make
generated copy read fake. Real review quotes, nav, and footer are excluded --
never edit a real testimonial to satisfy a check.

Exit code 0 = all checks pass, 1 = at least one FAIL.
"""

import sys
import re
import json
import statistics
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path

# ---------------------------------------------------------------- thresholds
# Calibrated against dasilva-associates (reference) plus the two mockups
# whose copy already reads right (cedar-grove-transmission, john-sessa-cpa).
T = {
    "emdash_per_100w": 1.0,      # reference site sits at 0.62; every current mockup is 1.1-3.4
    "dash_paragraph_pct": 15,     # reference 6.2%; current mockups 17-67%
    "max_para_words": 60,         # reference longest is 35
    "h1_words": (2, 9),           # hero headline word count
    "formal_openers": 2,          # <= 2 "It is / There is / That is" sentence openers
    "min_contractions": 3,        # body copy must contain at least this many contractions
    "spelled_numerals": 3,        # <= 3 spelled-out numerals above ten in body copy
    "triads": 1,                  # <= 1 three-fragment ("X. Y. Z.") construction per page
    "motif_max": 2,               # no banlist or watchlist word more than twice per page
}
# Reported but never auto-failed -- these need a human read, not a threshold.
# Median paragraph length inverts (the wordiest sites use many tiny cards), and
# plain direct copy ("Get it to a shop that will tell you straight") carries no
# number or proper noun yet is exactly what we want. See references/checks.md.
ADVISORY = ["median_para_words", "noanchor_para_pct"]

SKIP_TAGS = {"script", "style", "head", "title", "noscript", "svg", "nav", "footer", "form"}
SKIP_CLASS = re.compile(r"review|testimonial|quote|pullquote|pull-quote", re.I)
BLOCK_TAGS = {"p", "li", "h1", "h2", "h3", "h4", "h5", "h6", "dd", "dt", "figcaption", "summary"}

CONTRACTIONS = re.compile(
    r"\b\w+(?:'|’)(?:s|t|re|ve|ll|d|m)\b|\b(?:won|can|don|doesn|isn|aren|didn)(?:'|’)t\b", re.I)
FORMAL_OPENER = re.compile(r"(?:^|(?<=[.!?]\s))(It|That|There) (is|was|are|were)\b")
SPELLED_NUM = re.compile(
    r"\b(eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|"
    r"forty|fifty|sixty|seventy|eighty|ninety|hundred)\b", re.I)
# "X. Y. Z." -- three terminated fragments of <= 4 words each, back to back.
# Catches "Fair. Honest. Since 1961." and "Straight answers. Clean books. Since 1983."
_FRAG = r"[\w'’-]+(?:\s+[\w'’-]+){0,3}\."
TRIAD = re.compile(rf"{_FRAG}\s*{_FRAG}\s*{_FRAG}")
PLACEHOLDER = re.compile(r"\[[^\]]{3,80}\]|AI-IMAGE", re.I)
PROPER = re.compile(r"(?<![.!?]\s)(?<!^)\b[A-Z][a-z]{2,}\b")


def load_banlist():
    """Words that should never carry a trade site's copy. See references/banlist.md.

    Returns (motif_words, cutesy_words). Motif words are capped at 2 per page; cutesy
    words (Tier 1B) are capped at ZERO -- anthropomorphised plants and winking at the
    reader are never right on a contractor's site, not even once.
    """
    here = Path(__file__).resolve().parent.parent / "references" / "banlist.md"
    motif, cutesy = [], []
    in_cutesy = False
    if here.exists():
        for line in here.read_text().splitlines():
            if line.startswith("## "):
                in_cutesy = "1B" in line or "cutesy" in line.lower()
            m = re.match(r"^\s*[-*]\s+`([^`]+)`", line)
            if m:
                (cutesy if in_cutesy else motif).append(m.group(1).strip().lower())
    return motif, cutesy


VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
             "meta", "param", "source", "track", "wbr"}


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
            # a loose run of text ended where a sibling element began
            self._flush()

    def handle_startendtag(self, tag, attrs):
        return

    def handle_endtag(self, tag):
        if tag in VOID_TAGS:
            return
        if tag in BLOCK_TAGS or (self._cur and self._cur not in BLOCK_TAGS):
            self._flush()
        # unwind to the matching open tag; tolerate unclosed inline elements
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
            # Visible copy that isn't inside a <p> or heading -- stat strips, gallery
            # captions, badges. Customers read these, so the sweep has to show them.
            if not data.strip() or not self._stack:
                return
            self._cur = self._stack[-1][0]
            self._line = self.getpos()[0]
        self._buf.append(data)

    def _flush(self):
        if self._cur and self._buf:
            # join on a space: adjacent text nodes are separated by inline tags,
            # and "Honest.<span>Since" must not become "Honest.Since"
            text = re.sub(r"\s+", " ", " ".join(self._buf)).strip()
            text = re.sub(r"\s+([,.;:!?])", r"\1", text)
            if text:
                self.blocks.append((self._cur, text, self._line))
        self._buf, self._cur = [], None


def words(s):
    return re.findall(r"[A-Za-z][A-Za-z'’-]*", s)


STOP = set("""about after again against also always analyze and another any are around because
been before being below between both but call can come could crew day days each even every
first free from full get give good great has have here how into its just keep know like
local look made make many more most much must need never new next not now off one only
other our out over own place plan property same say season see service services since some
such take than that the their them then there these they thing this those through time
today too under until use very want was way we well were what when where which while who
why will with without work works would year years you your yours""".split())


def cutesy_hits(blocks, cutesy_list):
    """Tier 1B words, capped at zero. Returns [(line, word, text), ...].

    A word list rather than a grammar heuristic on purpose: "we'll tell you what your
    lawn needs" is approved copy, so any anthropomorphism regex keyed on needs/wants
    fires on good lines. The shapes that can't be word-matched -- puns, winks, jokes
    about the work -- are caught by the say-aloud read, not by this.
    """
    hits = []
    for _, text, line in blocks:
        for w in cutesy_list:
            if re.search(rf"\b{re.escape(w)}\b", text, re.I):
                hits.append((line, w, text))
                break
    return hits


def framing(body):
    """Company-framed ("we do X") vs customer-framed ("you get Y").

    Advisory, and deliberately not a target ratio. A contractor legitimately says "we" --
    "we show up when we said we would" is a promise and belongs in first person. The
    failure is a whole page of it, which reads as a log of the contractor's activities
    rather than what the homeowner ends up with.
    """
    we = len(re.findall(r"\b(?:we|we'll|we're|we've|our|ours|us)\b", body, re.I))
    you = len(re.findall(r"\b(?:you|your|yours|you'll|you're)\b", body, re.I))
    return we, you


def year_drift(body):
    """'20 yrs' on a page that also says 'since 2004' -- in 2026 that's 22.

    Advisory, not a hard fail: both can legitimately be true (an owner with 25 years in
    the trade whose own company started in 2004). But when they drift it is usually a
    stat nobody updated, it contradicts the page, and it undersells the client.
    """
    since = re.search(r"\bsince\s+((?:19|20)\d\d)\b", body, re.I)
    span = re.search(r"\b(\d{1,2})\s*(?:\+\s*)?(?:yrs?|years)\b", body, re.I)
    if not (since and span):
        return None
    started, claimed = int(since.group(1)), int(span.group(1))
    actual = datetime.now().year - started
    if abs(actual - claimed) <= 1:
        return None
    return (claimed, started, actual)


def heading_echoes(blocks):
    """Card bodies that just say their own heading again.

    Advisory: some echo is natural. The failure is a body whose only new information is
    a trailing prepositional phrase -- heading "Seat walls & fire pits" over body
    "Built-in seat walls and fire pits, laid in matching stone."
    """
    out, pending = [], None
    for tag, text, line in blocks:
        if tag.startswith("h"):
            pending = (text, line)
        elif tag == "p" and pending:
            hw = {w.lower() for w in words(pending[0]) if len(w) > 3}
            bw = {w.lower() for w in words(text) if len(w) > 3}
            if hw and len(hw & bw) / len(hw) >= 0.6:
                out.append((line, pending[0], text))
            pending = None
    return out


def duplicate_blocks(results, min_pages=3):
    """Paragraphs appearing verbatim on N+ pages.

    Shared boilerplate is usually fine (a repeated three-step explainer). The bug this
    catches is shared copy carrying a page-specific noun -- "what your beds need" on the
    masonry page -- which reads as careless to the one person who notices: the owner.
    """
    seen = {}
    for r in results:
        for _, text, _ in r["blocks"]:
            if len(words(text)) >= 5:
                seen.setdefault(text, set()).add(Path(r["file"]).name)
    return sorted(((t, sorted(f)) for t, f in seen.items() if len(f) >= min_pages),
                  key=lambda kv: -len(kv[1]))


def repeated_words(body, top=8, floor=3):
    """Distinctive words used 3+ times -- a motif detector that doesn't need a banlist.

    Advisory only: a landscaper's page SHOULD repeat "patio". The judgment call is
    whether the repeated word carries information or mood. "grounds" x4 is a mood word.
    """
    freq = {}
    for w in words(body.lower()):
        w = w.strip("'’-")
        if len(w) >= 5 and w not in STOP:
            freq[w] = freq.get(w, 0) + 1
    hits = sorted(((w, c) for w, c in freq.items() if c >= floor), key=lambda kv: -kv[1])
    return hits[:top]


def analyze(path, banlist, watch=(), cutesy_list=()):
    raw = Path(path).read_text(errors="replace")
    p = Extract()
    p.feed(raw)
    p._flush()
    blocks = p.blocks

    paras = [t for tag, t, _ in blocks if tag in {"p", "li", "dd"} and len(words(t)) > 2]
    heads = [t for tag, t, _ in blocks if tag.startswith("h")]
    h1 = next((t for tag, t, _ in blocks if tag == "h1"), "")
    body = " ".join(t for _, t, _ in blocks)
    wc = len(words(body))
    if wc == 0:
        return None

    para_lens = [len(words(t)) for t in paras] or [0]
    emdash = body.count("—")
    dash_paras = sum(1 for t in paras if "—" in t)
    motifs = {w: len(re.findall(rf"\b{re.escape(w)}\w*\b", body, re.I))
              for w in list(banlist) + list(watch)}
    motifs = {w: c for w, c in motifs.items() if c > 0}
    noanchor = [t for t in paras if not re.search(r"\d", t) and not PROPER.search(t)]

    r = {
        "file": str(path),
        "words": wc,
        "paragraphs": len(paras),
        "emdash": emdash,
        "emdash_per_100w": round(emdash / wc * 100, 2),
        "dash_paragraph_pct": round(dash_paras / len(paras) * 100, 1) if paras else 0,
        "median_para_words": statistics.median(para_lens),
        "max_para_words": max(para_lens),
        "h1_words": len(words(h1)),
        "h1": h1,
        "formal_openers": len(FORMAL_OPENER.findall(body)),
        "contractions": len(CONTRACTIONS.findall(body)),
        "spelled_numerals": len(SPELLED_NUM.findall(body)),
        "triads": sum(1 for t in heads + paras if TRIAD.search(t.strip() + " ")),
        "motifs": dict(sorted(motifs.items(), key=lambda kv: -kv[1])),
        "motif_max": max(motifs.values(), default=0),
        "motif_worst": max(motifs, key=motifs.get) if motifs else "",
        "noanchor_para_pct": round(len(noanchor) / len(paras) * 100, 1) if paras else 0,
        "placeholders": len(PLACEHOLDER.findall(body)),
        "dash_sample": [t for t in paras if "—" in t][:3],
        "repeated": repeated_words(body),
        "blocks": blocks,
        "cutesy": cutesy_hits(blocks, cutesy_list),
        "echoes": heading_echoes(blocks),
        "year_drift": year_drift(body),
        "framing": framing(body),
    }
    return r


def verdict(r):
    """Return list of (check, ok, detail) for the hard gates only."""
    v = []
    v.append(("em-dash rate", r["emdash_per_100w"] <= T["emdash_per_100w"],
              f"{r['emdash_per_100w']}/100w (max {T['emdash_per_100w']})"))
    v.append(("dash-restatement shape", r["dash_paragraph_pct"] <= T["dash_paragraph_pct"],
              f"{r['dash_paragraph_pct']}% of paragraphs (max {T['dash_paragraph_pct']}%)"))
    v.append(("longest paragraph", r["max_para_words"] <= T["max_para_words"],
              f"{r['max_para_words']} words (max {T['max_para_words']})"))
    lo, hi = T["h1_words"]
    v.append(("hero headline length", lo <= r["h1_words"] <= hi,
              f"{r['h1_words']} words (want {lo}-{hi})"))
    v.append(("formal openers", r["formal_openers"] <= T["formal_openers"],
              f"{r['formal_openers']} 'It is/There is' openers (max {T['formal_openers']})"))
    v.append(("contraction floor", r["contractions"] >= T["min_contractions"],
              f"{r['contractions']} contractions (min {T['min_contractions']})"))
    v.append(("spelled numerals", r["spelled_numerals"] <= T["spelled_numerals"],
              f"{r['spelled_numerals']} (max {T['spelled_numerals']})"))
    v.append(("triad constructions", r["triads"] <= T["triads"],
              f"{r['triads']} (max {T['triads']})"))
    v.append(("motif cap", r["motif_max"] <= T["motif_max"],
              f"'{r['motif_worst']}' x{r['motif_max']} (max {T['motif_max']})" if r["motif_worst"] else "none"))
    v.append(("no placeholders", r["placeholders"] == 0,
              f"{r['placeholders']} placeholder/AI-IMAGE strings in visible copy"))
    v.append(("no cutesy language", not r["cutesy"],
              f"{len(r['cutesy'])} hit(s): " + ", ".join(
                  f"'{w}' line {ln}" for ln, w, _ in r["cutesy"][:4]) if r["cutesy"] else "none"))
    return v


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    watch = []
    for f in list(flags):
        if f.startswith("--watch="):
            watch = [w.strip().lower() for w in f.split("=", 1)[1].split(",") if w.strip()]
            flags.discard(f)
    banlist, cutesy_list = load_banlist()
    if not args:
        print(__doc__)
        return 2

    results = [r for r in (analyze(a, banlist, watch, cutesy_list) for a in args) if r]

    if "--list" in flags:
        # Every visible string, for the say-aloud sweep. Put a verdict on each line
        # BEFORE editing anything: fine / too poetic / too cute / too vague / overwritten.
        for r in results:
            print(f"\n=== {r['file']}  ({len(r['blocks'])} visible strings)")
            for tag, text, line in r["blocks"]:
                print(f"  {line:>5}  {tag:<4}  {text}")
        print("\nRead every line above. The checks cannot hear register; you can.")
        return 0

    if "--json" in flags:
        for r in results:
            r.pop("blocks", None)
        print(json.dumps(results, indent=2))
        return 0

    failed = False
    if "--compare" in flags:
        cols = ["words", "emdash_per_100w", "dash_paragraph_pct", "median_para_words",
                "triads", "motif_max", "noanchor_para_pct"]
        print(f"{'file':44} " + " ".join(f"{c[:11]:>12}" for c in cols))
        for r in results:
            name = "/".join(Path(r["file"]).parts[-3:])
            print(f"{name:44} " + " ".join(f"{str(r[c]):>12}" for c in cols))
        return 0

    for r in results:
        print(f"\n=== {r['file']}  ({r['words']} words, {r['paragraphs']} paragraphs)")
        print(f"    hero: {r['h1'][:90]}")
        for name, ok, detail in verdict(r):
            print(f"    [{'PASS' if ok else 'FAIL'}] {name:24} {detail}")
            failed |= not ok
        print(f"    [ -- ] median paragraph       {r['median_para_words']} words   "
              f"(advisory; the crew's tightest reference pages sit at 8-12)")
        print(f"    [ -- ] paragraphs with no number or proper noun   "
              f"{r['noanchor_para_pct']}%   (advisory; read them, cut the ones saying nothing)")
        if r["repeated"]:
            top = ", ".join(f"{w} x{c}" for w, c in r["repeated"])
            print(f"    [ -- ] used 3+ times: {top}")
            print("           (advisory; fine for a service noun, a motif if it's a mood word)")
        if r["motifs"]:
            top = ", ".join(f"{w} x{c}" for w, c in list(r["motifs"].items())[:6])
            print(f"    flagged vocabulary: {top}")
        we, you = r["framing"]
        if we > you * 1.5:
            print(f"    [ -- ] framing: {we} we/our vs {you} you/your   (advisory; the page may")
            print("           describe your activities more than their outcome -- read rule 6.")
            print("           A process section legitimately runs on 'we'; check the rest.)")
        if r["year_drift"]:
            claimed, started, actual = r["year_drift"]
            print(f"    [ !! ] year drift: page says '{claimed} yrs' and 'since {started}'"
                  f" -- that's {actual}. Check which is right; a stat that contradicts")
            print("           the page reads careless, and usually undersells the client.")
        if r["echoes"]:
            print("    [ -- ] body repeats its own heading (advisory):")
            for line, head, body in r["echoes"][:5]:
                print(f"      line {line}  '{head}' -> {body[:90]}")
        if r["cutesy"]:
            print("    cutesy language (fix all of these):")
            for ln, w, text in r["cutesy"]:
                print(f"      line {ln} ['{w}']: {text[:130]}")
        if r["dash_sample"]:
            print("    fix these first (dash-restatement shape):")
            for s in r["dash_sample"]:
                print(f"      - {s[:150]}")

    dupes = duplicate_blocks(results) if len(results) > 2 else []
    if dupes:
        print(f"\n=== shared across pages ({len(dupes)} blocks) — advisory")
        print("    Fine for genuine boilerplate. A bug when the shared line names something")
        print("    page-specific (\"what your beds need\" on the masonry page).")
        for text, files in dupes[:8]:
            print(f"    [{len(files)} pages] {text[:110]}")

    if failed:
        print("\nChecks failed. Fix them -- then read every line with --list, because")
        print("the checks cannot hear register and half the problems never trip one.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
