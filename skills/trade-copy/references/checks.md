# Stage B — the checks

```bash
# one page
python3 skills/trade-copy/scripts/copycheck.py prospects/<slug>/mockup/index.html

# add this site's watch-list words from voice-spec.md
python3 skills/trade-copy/scripts/copycheck.py prospects/<slug>/mockup/index.html --watch=oasis,tailored

# compare against the whole portfolio
python3 skills/trade-copy/scripts/copycheck.py prospects/*/mockup/index.html --compare
```

Exit code 0 = every hard check passed. The Builder runs it before handoff; the Critic
runs it as a gate.

The script reads only visible body copy. It drops `<nav>`, `<footer>`, `<form>`,
`<script>`, `<style>`, `<blockquote>`, and anything whose class contains `review`,
`testimonial`, or `quote` — **real customer quotes are never measured and never
edited.** If a check trips on a real review, the markup is wrong, not the review.

## The thresholds, and where they came from

Calibrated against the two pages in this project whose copy already reads right:
`prospects/dasilva-associates/mockup/index.html` and
`prospects/fora-digital/mockup/index.html`. Every other mockup in `prospects/` fails at
least two. The **Reference site** column below is the DaSilva home page, measured.

> **Re-measured 2026-08-04.** Both pages were calibration-clean when these thresholds
> were set (2026-08-02) and have since drifted by exactly one check each: DaSilva was
> rebuilt and now trips **contraction floor** (2, min 3); FORA trips **longest paragraph**
> (83 words, max 60). Both remain the best-reading pages in the project and stay the
> reference — a reference page is not required to be gate-perfect, and neither threshold
> was loosened to accommodate them. Read them for register, run the gate on your own page.

| Check | Threshold | Reference site | What a failure means |
|---|---|---|---|
| **em-dash rate** | ≤ 1.0 per 100 words | 0.62 | You're using the dash as a rhythm device. Current mockups run 1.1–3.4. |
| **dash-restatement shape** | ≤ 15% of paragraphs contain an em dash | 6.2% | The `[clause] — [prettier restatement]` template has become the house style. The script prints the first three offenders — fix those and the rate usually follows. |
| **longest paragraph** | ≤ 60 words | 35 | Someone wrote an essay paragraph. Split it or cut it. |
| **hero headline length** | 2–9 words | 8 | Over 9 stops being a headline. The floor is 2, not 3: interior pages legitimately title themselves "Practice areas" and "Privacy Policy", both on reference builds. The docs said 3 and the script said 2 until 2026-08-05; the script was right and the docs were corrected to match, not the other way round. |
| **formal openers** | ≤ 2 "It is / There is / That is" | 0 | Period-piece register. Contract them. |
| **contraction floor** | ≥ 3 contractions | 6 | Zero contractions is the clearest sign nobody spoke these sentences aloud. |
| **spelled numerals** | ≤ 3 above ten | 0 | "Forty-five years" belongs in a novel; the site says "45 years". |
| **triad constructions** | ≤ 1 per page | 0 | "X. Y. Z." heroes. One is a choice; two is a tic. Check other prospects before using your one. |
| **motif cap** | ≤ 2 uses of any banned or watched word | 0 | Motif-hammering — the loudest tell in this project's output. `oasis` appears **7×** on one page (`duran-and-son`); all seven are quoted with rewrites in `examples.md` §6. |
| **no placeholders** | 0 | 0 | `[Hours — placeholder]` or `AI-IMAGE` strings are visible in the copy. This alone makes a deploy-ready build look fake. |
| **no cutesy language** | 0 | 0 | A Tier 1B word — anthropomorphised plants, winking, whimsy. Zero tolerance: unlike a motif, one is already wrong. |
| **no banned phrases** | 0 | 0 | A phrase from the "Banned phrases" section — "we pride ourselves on", "from start to finish", "no job too big or too small". **New 2026-08-05.** These were in `banlist.md` since July and read by nothing: the loader only picked up single backticked words, so the whole quoted list was decoration. Entries marked "(unless the client said it)" are still exempt. |

## The advisory readouts

Reported, never auto-failed. All three need a human read.

**Words used 3+ times.** The motif cap above only catches words on the banlist or the
spec's watch list. This line catches the rest — a site whose own invented mood word runs
through every section. The judgment: does the repeated word carry *information* or
*mood*? A masonry page repeating "patio" is fine, that's the product. A landscaping page
repeating "grounds" (hero, gallery heading, closing CTA) is a motif, and "grounds" is an
estate word no NJ homeowner uses about their own yard. Mood words go on the voice spec's
watch list, then `--watch=` makes them a hard failure on the next run.

**Framing (we/you).** Fires only when "we/our" runs more than 1.5× "you/your". A blunt
metric, and knowing its limits matters: a well-written contractor page has a process
section that legitimately runs on "we" — "we show up when we said we would" is a promise
and belongs in first person. On the site this was calibrated against, the ratio barely
moved between a company-framed draft and a fixed one, because the fix was one sentence
("We check sun exposure…" → "You get a site check…"), not a global pronoun swap. Treat a
hit as a prompt to read the non-process sections, not as a quota to hit.

**Year drift.** Fires when a page claims "N yrs" and "since YYYY" that don't agree with
each other and the calendar — "20 yrs" beside "since 2004" in 2026. Advisory because both
can honestly be true (an owner with 25 years in the trade whose own company started in
2004), but usually it is a stat nobody updated. Two reasons it matters more than its
size: a number that contradicts the page reads careless to the one reader who counts, and
the stale figure almost always *undersells* the client. Accuracy findings outrank tone
findings — wrong is worse than ugly.

**Elegant variation** (new 2026-08-05). Fires when four or more different banlist words
each appear exactly once. This is the counterweight to `motif cap`, and the two pull in
opposite directions on purpose: a page that says "oasis" seven times fails the cap, while a
page that says oasis, sanctuary, retreat, haven once each passes every check and is the
*same tell* — humanizer category 11. Until now nothing in this project pushed back on
synonym cycling, which meant the cheapest way to satisfy the motif cap was to commit the
other sin. Advisory, because touching four banlist words once can be honest; a reader
decides whether it is vocabulary or evasion.

**Median paragraph length** (reference: 8 words). A low median is not automatically
good — the wordiest sites in this project score *well* here because they use many tiny
cards, while the plainest site scores 22 because it writes normal sentences. Read it as
context for the other numbers, not as a target.

**Paragraphs with no number or proper noun** (reference: 21.8%). Meant to catch padding,
but plain direct copy trips it honestly: "Broken down? Get it to a shop that will tell
you straight what it needs" contains no fact and is exactly right. So: open the
paragraphs it flags and ask whether each one *says* anything. Cut the ones that don't.
Don't rewrite them — a padding paragraph rewritten is still padding.

## What the script cannot check

Most of it, honestly. The checks are a floor, not a standard.

Nothing mechanical catches "meticulous by habit", "Thirty Years, Gallery-Hung", "we read
the sun", "Three steps, no mystery", or "Rooted in West Essex". All are clean on every
threshold above. The cutesy word list catches the vocabulary of whimsy but not its
*shapes* — puns, winks, jokes, coy tails — because those are register, and register has
no regex.

**So the read is not the last step, it is the gate.** Run:

```bash
python3 skills/trade-copy/scripts/copycheck.py <page.html> --list
```

and go down every string asking one question: *would the owner say this out loud to a
customer standing in his driveway?* Sort each into fine / too poetic / too cute / too
vague / overwritten before editing anything.

> **Baseline re-measured 2026-08-05**, after the banlist loader was fixed and the phrase
> check added. Across all 30 built pages: 2 pages trip **no banned phrases** —
> `anthonys-landscaping` (19 hits: "from start to finish", "every step of the way", "a cut
> above", "outstanding professional service", "complete satisfaction") and
> `duran-and-son-landscaping` ("quality workmanship"). `duran-and-son` also trips **motif
> cap** on `oasis` ×7. **All three are frozen and stay as they are** — the same rule that
> governs the two `overused-font` bounces in `design-gates.md`. They are listed so nobody
> mistakes the failure for a broken check; per **Lessons flow forward** in `CLAUDE.md`, a
> signed build is calibration data, never a fix list. The phrase check earned its place by
> finding 19 instances of exactly what the banlist was written to stop.

A page that passes all eleven checks and fails the read is a failing page. It has happened
on this project already: the script went green while "won't need babying to survive the
winter" sat two lines above a freshly edited line, unread.

## Shared blocks across pages

When you pass several pages at once, the script lists paragraphs appearing verbatim on
three or more of them. Genuine boilerplate is fine — a three-step explainer belongs on
every service page. The bug it catches is **shared copy carrying a page-specific noun**:
"We'll tell you honestly what your beds need" is correct on the planting page and wrong on
the masonry page, where the customer is pricing a patio. The owner notices that instantly.

## Fixing a failure

Rewrite toward fewer words, not different words. The dash failures are the fastest win:
in almost every case the text before the dash is already a complete, honest sentence and
everything after it is the same idea in nicer clothes. Delete the second half.

Before packaging (`pipeline/package-site.sh`) run the checks once more on the final
build — the placeholder check especially, since a `deploy-ready/` folder shipping
`[Insured — confirm]` is worse than a draft doing it.
