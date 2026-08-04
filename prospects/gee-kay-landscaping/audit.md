# Audit — Gee-Kay Landscaping, Inc. (Rev 2 — full rebuild)

**Slug:** `gee-kay-landscaping` · **Date:** 2026-08-02 · **Review round: 1**
**Art direction:** "Property Line" · **Build:** rebuilt from scratch — new direction, new
three-file page structure, no line carried over from the Rev 1 HTML.
**Supersedes** the Rev 1 audit of 2026-07-19 in full.
**Paid calls this prospect: 0.** No images, no video, no Firecrawl, no Perplexity. Nothing
in this run cost money.

> **Why the Rev 1 "PASS — 8/8" was wrong.** That audit was scored by eye before the
> deterministic detector existed in this pipeline. Run against the Rev 1 file today the
> detector reports **27 contrast failures**, worst `#31502f` on `#a8763e` at **2.3:1**. The
> round-3 fix introduced a darker `--brass-text` for small accent *text* but left
> `--brass-clay` in service as a *background* with pine text on top of it, so the worst pair
> on the page was never touched. Rev 1 also shipped two bracketed placeholders as visible
> page copy — an owner's note attributed to George Reinhardt, and an `[Insured — confirm]`
> chip — which the same audit signed off as "honesty flag respected". Both are gone here.

---

## Mechanical gates

| Gate | Command | Result |
|---|---|---|
| Plan lint | `plan-lint.mjs website-plan.md` | **exit 0** — clean, 18 sections, 10 families |
| Step 0 detector | `detect.mjs mockup/{index,services,contact}.html` | **exit 0 — 0 errors, 0 advisory**, no rules waived |
| Detector health | parser deps present | no `DETECTOR DEGRADED` warning; the engine parses real CSS — the same invocation reports 27 findings on the Rev 1 file |
| Copy register | `copycheck.py` | contact **exit 0**; index and services fail **one** check only — documented exception below |
| Page shape | `aitells.py` | **exit 0** on all three pages |
| Fail-visible measurement | `impeccableMeasureHiddenText()` at rest, **before** any force-reveal | **0%** on all three pages (index 0 of 3115 chars, services 0 of 1705, contact 0 of 1620). Gate is ≤15%. |
| JS-off test | renamed `main.js`, reloaded, captured | page renders complete; every word readable, both CTAs and the phone number tappable; hidden text still 0% |
| Horizontal overflow | `scrollWidth` vs `clientWidth` at 375 and 1440 | equal on all six page/width combinations; zero elements extend past the viewport |
| Console | CDP `Log` + `Runtime.exceptionThrown`, all three pages | **no errors** |

**Detector: 0 errors, 0 advisory. No rules waived.**

Findings fixed during the build rather than waived: 27 low-contrast pairs (palette
redesigned so `--flag` and `--spruce` never meet as a text pair), `hero-eyebrow-chip` (the
tracked micro-kicker became a reading-size dateline on a datum rule), three `all-caps-body`
hits, four `cramped-padding` hits, `wide-tracking`, `tight-leading`, and
`clipped-overflow-container`.

### The one documented exception — `copycheck.py` "no placeholders"

`copycheck.py` fails index (5 hits) and services (3 hits) on `no placeholders`, which
matches the literal string `AI-IMAGE` in visible copy. Those eight hits are exactly the
eight image slots this run was instructed to keep as labeled placeholders, in the label
format CLAUDE.md's Image policy mandates verbatim (`<span>AI-IMAGE — …</span>`).

The two rules are mutually exclusive: the check cannot pass while the house placeholder
convention is followed. **The label was kept and the check was not gamed** — renaming the
token to slip past the gate would defeat its purpose while leaving identical content on the
page. Every other copycheck line passes on all three pages, including the em-dash rate,
which failed mid-build and was fixed by setting the labels with a middot instead.

The exception clears itself the moment real photography lands in the slots.

---

## Composition counts (blocking — counted, not eyeballed)

18 sections across the three pages, in document order.

| # | Quota | Count | Verdict |
|---|---|---|---|
| 1 | ≥ 4 distinct families per 8 sections | **10 distinct** across 18 (hero, stat-strip, card-grid, full-bleed-band, steps, editorial-column, quote-monolith, cta-band, split, bento) | **PASS** |
| 2 | No family twice consecutively | 0 back-to-back repeats | **PASS** |
| 3 | Kicker budget ≤ ceil(18÷3) = 6 | **4** — §1 `kicker+h2`, §8/§10/§15 `side-label` | **PASS** |
| 4 | No two adjacent sections share an opener | 0 matches across all 17 boundaries | **PASS** |
| 5 | No opener signature on > 50% | most-used is `bare-h2` at **6/18 = 33%** | **PASS** |

Opener sequence as built — `kicker+h2 · none · bare-h2 · in-media · numeral · bare-h2 ·
none · side-label ‖ bare-h2 · side-label · in-media · bare-h2 · none ‖ bare-h2 ·
side-label · none · bare-h2 · in-media`.

**Composition device (named):** the **dominant column** — a 7/5 split (58fr / 42fr, never
50/50) **carried by the Home hero (§1)**, type column wide, image plate breaking the
content column's right edge rather than aligning to it. Supporting move inside the first
two sections: an **8.6× scale jump** between the trust strip's `1981` numeral (7rem at
desktop) and its `0.8125rem` caption — clear of the ≥3× bar on its own.

**Other countable checks**

- **Hero:** 4 text elements (dateline, h1, subhead, CTA row) — cap is 4. Headline 2 lines
  at 1440. Subhead 25 words. Both CTAs above the fold. Top padding 4.5rem desktop, under
  the ~6rem ceiling. No trust strip inside the hero; it is the section below.
- **CTAs:** "Get an estimate" (3 words), "Our services" (2). Neither wraps at desktop. One
  primary intent site-wide; the repeated tap-to-call is `local-trade.md`'s sanctioned
  exception.
- **Nav:** one line at desktop, header 74px (≤80px).
- **Grid cell count == item count:** services 3/3, steps 4/4, bento fills a 4×2 mosaic with
  no orphan tile — it *had* one on the first pass, and the cell order was changed so the
  mosaic packs.
- **Bento visual weight:** 2 of 4 cells carry it (the 2×2 image plate, the spruce `45`
  cell). Requirement is ≥2.
- **Zigzag:** §10 image-left, §12 image-right. Mirrored, not repeated.
- **Falsifiable facts visible:** 1981 · 45 years · 5.0 on Angi · Livingston · 73 N
  Livingston Ave · three service lines · NJ Home Improvement Contractor license.
  `aitells.py` counts ≥1 mechanically and passes.
- **Consistency locks:** one theme (light, with two deliberate spruce bands and a graphite
  footer — no alternation); one accent, used identically; one radius system (2px,
  all-sharp).
- **Present or unfinished:** skip-to-content is the first focusable element on every page;
  privacy and terms links in the footer.

---

## The 10-dimension rubric

Scored off the six screenshots in `screenshots/`, not from memory of the code.

| # | Dimension | Score | Note |
|---|---|---|---|
| 1 | **Boldness / distinctiveness** | **8** | The site-plan read is a position, not a colourway: tick-field ground, drafting-ink green, one flag orange, facts set as measurements at 7rem. Unmistakably not the warm-earth landscaper template, and unlike the four landscapers already in `design-memory.md`. Held at 8 rather than 9 because with every image slot empty the boldest surface is typography alone — the direction has more range than this build can currently show. |
| 2 | Visual hierarchy | 9 | Eye lands on the h1, then 1981/45/5.0, then the orange CTA. Three clear tiers on every page. |
| 3 | Typography craft | 9 | Newsreader roman against Familjen Grotesk; every scale step ≥1.27×; measure capped at 68ch; −0.018em tracking on display only. Neither face is banned or in the last three memory rows. |
| 4 | Color & contrast | 9 | Five tokens plus two documented tints, every pair computed before building. Detector reports **zero** contrast findings including `:hover` states — against 27 in Rev 1. The rule that makes it hold: `--flag` and `--spruce` never meet as a text pair, which was Rev 1's 2.3:1 bug. |
| 5 | Spacing rhythm | 8 | Three deliberate density steps (tight / base / breathe) alternating dense↔breathe. The gap between the steps section and the editorial column is the largest on the page; it reads as a beat rather than a hole, but it is the first thing I would tighten next. |
| 6 | Background / depth | 8 | Three layers — tiling surveyor tick-field SVG, feTurbulence grain at 0.045, one spruce radial wash behind the hero column. Not a flat rectangle, and the tick field *is* the direction rather than decoration. Not higher because it is deliberately quiet: a plan sheet, not atmosphere. |
| 7 | Imagery quality | **n/a — not scored** | Zero images by instruction. All eight slots are labeled placeholders in the direction's colours (chalk ground, spruce hairline, flag corner tick). The register is declared in the plan as `proud-contractor` for whoever fills them. Scoring this would be scoring an absence the brief required. |
| 8 | Responsiveness | 9 | Real phone decisions, not a shrink: hero plate moves above the copy, CTAs go full-width and stack, nav collapses to a drawer while the **tap-to-call button stays visible**, trust cells gain hairline separators, split order flattens. Zero horizontal overflow at 375px; every tap target ≥24px after one fix, the primary call button 44px+. |
| 9 | Motion polish | 8 | Nameable from the screenshots: slide-alternate rows, a hairline tracing each card's edge on hover, the hero lifting away as the header compacts. One entrance, one hover, one set-piece, zero ambient — inside budget. None of the flagged default trio; no overlap with the last three memory rows. Transform-only, so nothing on the page is ever hidden. Not 9 because the entrance is the quietest of the three moves and carries most of the work. |
| 10 | Cohesion | 9 | Corner tick, datum rule and hairline trace are one mark at three scales. One art director throughout. |

**Lowest scored dimension: 8. Boldness: 8.**

### Gate result

| Condition | Status |
|---|---|
| Step 0 exits 0 | ✅ |
| No dimension below 7 | ✅ (lowest 8) |
| Boldness ≥ 8 | ✅ (8) |
| Every composition check passes | ✅ (all five quotas counted above) |
| No console errors, no horizontal overflow at 375px | ✅ |
| JS-off test passes | ✅ (0% hidden, page complete) |
| Bold test vs Rev 1 | ✅ — different palette family, type pairing, layout archetype and page structure. Not a subtle pass. |

---

## $10K Checklist — 8/8

1. **Point of view, not a template** — "Property Line": the site as a site plan, committed
   in the ground, the type, the marks and the numerals.
2. **Typography that does work** — Newsreader / Familjen Grotesk, neither defaulted, no
   banned face, scale steps ≥1.27×.
3. **Restrained color system** — 5 tokens + 2 documented tints; `--flag` reserved to one job.
4. **Hierarchy that breathes** — three density steps, 8.6× scale jump, 68ch measure.
5. **Imagery with intent** — *documented, instructed exception*: zero images this run. All
   eight slots are deliberate, labeled, art-directed placeholders carrying their Rev 1
   subjects. No stock, no hotlinks, no invented photography. This is the one checklist item
   not fully satisfied, and it is satisfied as far as a zero-spend run permits.
6. **Motion that whispers** — signature move named in the plan and built; distinct from the
   last 3 prospects; reduced-motion killswitch; nothing hidden by JS.
7. **Mobile that's designed** — see dimension 8.
8. **The invisible expensive stuff** — no build step, no CDN library, no image bytes: three
   HTML files plus ~30 KB CSS and 3 KB JS. WCAG AA throughout (detector: 0 contrast
   findings), visible focus ring, semantic landmarks, skip link, `LandscapingBusiness`
   JSON-LD on all three pages, per-page title/description/canonical/OG/Twitter, inline SVG
   favicon, **exactly one `<h1>` per page** (verified in the DOM, not by eye). Footer NAP
   matches the JSON-LD character for character. Unknown values ship as visible
   `PLACEHOLDER_…` tokens.

---

## Content honesty — the Rev 1 defects specifically

| Rev 1 defect | Status in Rev 2 |
|---|---|
| Visible `[placeholder: owner's note]` attributed to George Reinhardt | **Gone.** §6 has no quote slot at all, so there is nothing to fill in wrong. No sentence anywhere is attributed to him. |
| Visible `[Insured — confirm]` chip | **Gone.** The credentials strip carries three items and insurance is not one of them. The strings "insured" and "bonded" appear nowhere in the three files. |
| Unsourced town list | §4 states the confirmed line as page copy ("Livingston, New Jersey, and the surrounding Essex County towns") and puts the four *likely* towns in a visibly labeled **CONFIRM BEFORE LAUNCH** block styled as a placeholder. JSON-LD `areaServed` carries Livingston plus `PLACEHOLDER_TOWN_…` tokens. |

Everything asserted traces to `dossier.md`. Reviews are the two captured quotes, verbatim,
each attributed to its platform — the dossier holds no reviewer names, so none are
invented. Hours ship as `PLACEHOLDER_HOURS` with a visible note.

---

## Local-trade conversion checklist

| Requirement | Status |
|---|---|
| Tap-to-call in the mobile header | ✅ `tel:+19739926687`, always visible at ≤820px beside the burger; 44px+ target |
| One primary action | ✅ "Get an estimate" — same label in the hero, both CTA bands, and the form submit |
| Service-area block with real towns | ✅ §4, with the honesty split above |
| Trust strip | ✅ §2 (1981 / 45 / 5.0) and §16 (1981 / NJ license / 5.0) |
| Project gallery | ⚠️ the slots are built and art-directed; the photographs are the client's to supply |
| Estimate form ≤ 4 fields | ✅ Name · Phone · Town · What do you need done? Submit reveals an inline demo confirmation — verified by clicking it, not by reading the code |
| Consistent NAP footer | ✅ identical across all three pages and to the JSON-LD |

## Interactive QA (clicked, not assumed)

Driven through CDP at 375×812 across all three pages: **0 dead fragments**, every `*.html`
link resolves to a file that exists, **0 undersized tap targets** (after one fix to footer
and NAP links), burger opens and closes with `aria-expanded` tracking correctly, estimate
form reveals its confirmation on submit, **0 console errors**.

---

## Verdict

**PASS — signed off.** Both scoreboards clear: $10K Checklist 8/8 with one documented,
instructed exception (item 5, imagery), and the 10-dimension rubric with no dimension below
8 and boldness at 8.

**Not cleared for delivery.** Sign-off means the build is finished, never that it may go
live. Outstanding before anything reaches Corey: a **signed `release-form.pdf`** (none
exists for this prospect), the hours, the confirmed town list, real photography for the
eight slots, and a real domain for the `PLACEHOLDER_DOMAIN` tokens.

**Stale artifacts:** `deliverable/` and `deploy-ready/`, plus `mockup.zip` and
`gee-kay-landscaping-site.zip`, all still contain the Rev 1 single-file build. They
contradict this mockup and must be regenerated (`pipeline/package-site.sh gee-kay-landscaping`)
before any of them is used for anything.

**Lead's on-pass duties:** the `design-memory.md` row is appended. `/design-push` remains
the lead's to run — DesignSync auth lives in the lead session.
