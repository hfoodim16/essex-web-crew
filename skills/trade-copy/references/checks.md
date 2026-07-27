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
`~/Claude Code/corey-blakes-steakhouse/index.html` and
`prospects/fora-digital/mockup/index.html`. Both pass every hard check. Every other
mockup in `prospects/` fails at least two.

| Check | Threshold | Reference site | What a failure means |
|---|---|---|---|
| **em-dash rate** | ≤ 1.0 per 100 words | 0.5 | You're using the dash as a rhythm device. Current mockups run 1.1–3.4. |
| **dash-restatement shape** | ≤ 15% of paragraphs contain an em dash | 7.3% | The `[clause] — [prettier restatement]` template has become the house style. The script prints the first three offenders — fix those and the rate usually follows. |
| **longest paragraph** | ≤ 60 words | 41 | Someone wrote an essay paragraph. Split it or cut it. |
| **hero headline length** | 3–9 words | 4 | Under 3 is a fragment with no information; over 9 stops being a headline. |
| **formal openers** | ≤ 2 "It is / There is / That is" | 0 | Period-piece register. Contract them. |
| **contraction floor** | ≥ 3 contractions | 12 | Zero contractions is the clearest sign nobody spoke these sentences aloud. |
| **spelled numerals** | ≤ 3 above ten | 1 | "Forty-five years" belongs in a novel; the site says "45 years". |
| **triad constructions** | ≤ 1 per page | 0 | "X. Y. Z." heroes. One is a choice; two is a tic. Check other prospects before using your one. |
| **motif cap** | ≤ 2 uses of any banned or watched word | 2 | Motif-hammering — the loudest tell in this project's output. `oasis` appeared 6× on one page. |
| **no placeholders** | 0 | 0 | `[Hours — placeholder]` or `AI-IMAGE` strings are visible in the copy. This alone makes a deploy-ready build look fake. |
| **no cutesy language** | 0 | 0 | A Tier 1B word — anthropomorphised plants, winking, whimsy. Zero tolerance: unlike a motif, one is already wrong. |

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
