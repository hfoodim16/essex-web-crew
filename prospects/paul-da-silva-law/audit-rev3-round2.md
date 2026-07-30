# Audit — `paul-da-silva-law` Rev 3 · ROUND 2 (incremental re-verification)

**Review round: 2** (Rev 3) · Critic: `critic-rev3-round2` · 2026-07-30
Scope: verify the eight fixes the builder applied after round 1, re-check only what those
fixes could have broken, and give the round-2 verdict on the one gate that was failing
(the countable composition checks). Everything else in round 1 stands as recorded in
`audit-rev3-browser.md` and `audit-rev3-lead-static.md`.

Method: headless Chrome over CDP against `http://localhost:8912` (the mockup served over
http, not `file://`). Every number below is measured in the live DOM or off a capture — no
number is inferred from CSS source.

---

## FIX 1 — home h1 must render exactly 2 lines · **VERIFIED PASS**

`--fs-h1` is now `clamp(2.75rem, 6.5vw, 4.25rem)`. Line count measured with a `Range` over
the h1's text nodes (distinct line-box tops), not just box-height ÷ line-height, so the two
methods cross-check each other.

| Viewport | font-size | line-height | box height | line-box tops | lines (box ÷ lh) | lines (real boxes) | measure |
|---|---|---|---|---|---|---|---|
| **1280** | 68px | 70.72px | 141px | 184, 255 | **2.00** | **2** | 1075px |
| **1440** | 68px | 70.72px | 141px | 187, 258 | **2.00** | **2** | 1066px |
| **1600** | 68px | 70.72px | 141px | 187, 258 | **2.00** | **2** | 1056px |

Round 1 measured 80px / 83px lh / 250px box / **3 lines**. Now **141px / 2 lines at all three
widths** — the clamp fix holds either side of 1440, not just at it. The 6.5vw middle term only
takes over below ~1046px (6.5vw = 68px at 1046), so 1280/1440/1600 all sit on the 4.25rem
ceiling and are identical by construction; the measured identity confirms that.

**Still display scale.** 68px home h1 vs the interior h1 measured at **56px** on
`practice-areas.html` (`--fs-h1i` ceiling `clamp(2.4rem,5vw,3.5rem)` = 56px). The home
headline is 21% larger than the interior scale, so it did not collapse into it. Copy
untouched: *"A Newark defense attorney who speaks your language."*

**Composition check "headline ≤ 2 lines": now PASSES.**

---

## FIX 2 — card CTAs bottom-align across a row · **VERIFIED PASS**

Measured `.cmp` compartments on `index.html` @1440 after forcing reveals.

| # | Compartment | display / flex-dir | box top → bottom | height | **`goTop`** | gap below go |
|---|---|---|---|---|---|---|
| 0 | Criminal Defense | `flex` / `column` | 1570 → 1816 | 246 | **1742** | 31 |
| 1 | Traffic | `flex` / `column` | 1570 → 1816 | 246 | **1742** | 31 |
| 2 | Family Law | `flex` / `column` | 1816 → 2061 | 246 | **1988** | 31 |
| 3 | Real Estate | `flex` / `column` | 1816 → 2061 | 246 | **1988** | 31 |

Round 1: row 1 **1842 vs 1870**, row 2 **2118 vs 2090** — 28px out in both rows. Now
**row 1 = 1742 / 1742 (0px apart)** and **row 2 = 1988 / 1988 (0px apart)**, with an
identical 31px gap below every go-link. `margin-top:auto` is resolving to 28.05px on the
short cell and 0px on the tall one, which is exactly the intended behaviour.

**Composition check "Card CTAs bottom-align across a row": now PASSES.**

---

## FIX 3 — Family Law's 7 items as two columns · **VERIFIED PASS**

`practice-areas.html` `#family` now carries `<ul class="lineitems lineitems-2col settle">`.
Measured @1440:

- **`display: grid`, `grid-template-columns: 399.203px 399.219px`** — two real equal columns.
- **7 items, split 4 + 3** across two distinct x origins (**354** and **753**).
- The list now spans **354 → 1152px**, which is the section's full width (`secLeft` 354,
  `secRight` 1152, `secW` 798). Round 1's empty right half is gone — the list occupies it.
- **Collapsed hairlines kept:** every `<li>` has `border-top: 0px` / `border-bottom: 1px`, so
  the ledger rule grammar is unchanged from the single-column groups.
- Still inside the same ruled group (`#family` `.grp-head` header + the same `.lineitems` base
  class), not broken out into cards.

**All 7 strings verbatim, none lost** — checked against `site-content.md` lines 57–63:
Divorce · Alimony · Child support · Child custody · Domestic violence ·
Pre- and post-nuptial agreements · Juvenile delinquency and dependency proceedings.
Layout-only change; no copy touched, so no parity or voice re-gate is needed.

Page-wide list audit confirms nothing else trips the density check: the three
`main ul` groups are **5 items (1 column)**, **7 items (2 columns)**, **4 items (1 column)** —
no remaining single-column list above 5.

**Composition check "Lists > 5 items need a real component": now PASSES.**

---

## FIX 4 — skip-to-content link · **VERIFIED PASS on all four pages**

Identical on `index`, `practice-areas`, `attorney-bio`, `contact`:

| Property | Measured |
|---|---|
| First focusable element in the document | **`<a class="skip">Skip to content</a>`** |
| First child of `<body>` | **yes** |
| `href` → target | `#main` → `<main id="main">` present |
| At rest | `position:absolute` at **x = −9999**, off-screen, `visible: false` |
| On `.focus()` | **x 0, y 0, 153 × 54px**, `background rgb(179,135,62)` (`--ouro`), `color rgb(22,26,36)` (`--ink`), `z-index 400` |
| Fully on screen when focused | **yes** |
| `elementFromPoint` at its centre when focused | **resolves to the skip link itself** (nothing overlaps it) |
| `document.activeElement` after focus | the skip link |

Brass fill with `--ink` label measures **5.34:1** (round 1's table), so the revealed state is
AA and looks deliberate rather than like a browser default. Round 1: `grep -i skip` → 0 hits.

**Composition check "Skip-to-content link as first focusable": now PASSES.**

---

## FIX 5 — `.grp-head .num` contrast · **VERIFIED PASS**

All four practice-areas group folios measured live (computed colour against the resolved
ancestor background, WCAG 2.x relative luminance):

| Folio | color | font-size | ground | ratio | large-text floor |
|---|---|---|---|---|---|
| 01 | `rgb(128,96,38)` = `--ouro-escuro` | **32px** | `rgb(240,242,245)` = `--pedra` | **5.17:1** | 3.0 |
| 02 | same | 32px | same | **5.17:1** | 3.0 |
| 03 | same | 32px | same | **5.17:1** | 3.0 |
| 04 | same | 32px | same | **5.17:1** | 3.0 |

Round 1 measured **2.90:1** (`--ouro` on `--pedra`), 0.10 short. Now 5.17:1 — clears the
large-text floor by 2.17 and also clears the 4.5:1 body floor. Matches R3-9's own
practice-areas spec. The font-size did not change, so the folio still reads at the same scale.

---

## Palette freeze · **STILL FROZEN**

Computed from `:root` in the live page — all nine tokens at their exact Rev 3 hex:

`--pedra #F0F2F5` · `--ink #161A24` · `--muted #566072` · `--linha #C8CDD6` ·
`--tinta #131D33` · `--tinta-2 #0D1526` · `--ouro #B3873E` · `--ouro-escuro #806026` ·
`--lamp #EAD9AE`

Every hex literal in the whole 34.8 KB `style.css`, counted: those nine, plus `#fff` ×6
(the compartment fill, already on round 1's contrast table). **No tenth hue** — the fixes
introduced no new colour, and fix 5 reused an existing token rather than inventing a
mid-brass.

---

## FIX 6 — mobile hero CTA vs the fixed call bar · **NOT DONE — still overlapping (non-gating)**

Measured at 375×812, `scrollY: 0`, no reveal forcing needed (the collision is at first paint):

| Element | top | bottom | height | fill |
|---|---|---|---|---|
| Hero `Call 973-344-0808` (`a.btn.btn-primary`) | 702 | **758** | 56 | `rgb(179,135,62)` = `--ouro` |
| Fixed `.mobile-call` bar (`position: fixed`) | **755** | 812 | 57 | — |

**Gap = −3px.** Identical to round 1. `body{padding-bottom:56px}` is present and correctly
clears the bar at the page *bottom*, but there is still no hero-specific bottom clearance: the
hero CTA row's `margin-bottom` computes to **0px**. So at first paint the two brass slabs still
touch and read as one doubled button.

The lead's read was right — this fix was not applied. It was **non-gating in round 1 and stays
non-gating**: it is a spacing judgment inside a dimension already scored 8 (spacing rhythm) and
8 (responsiveness), not a composition check and not a $10K item. Reported here so the record is
accurate, not as a blocker.

**Fix, unchanged from round 1:** at the 375 block, give the hero's ruled CTA row a bottom margin
of at least the bar's 57px so the two never coincide at scroll 0.

---

## FIX 7 — standalone `.text-link` tap targets ≥44px · **VERIFIED PASS**

Measured at 375×812 with `(pointer: coarse)` confirmed matching (`matchMedia` → `true`) and
touch emulation on:

| CTA | page | height | width | `min-height` |
|---|---|---|---|---|
| *Send a message →* | index | **44px** | 330 | `44px` |
| *Meet Paul Da Silva →* | index | **44px** | 153 | `44px` |
| *Read the full bio →* | index | **44px** | 137 | `44px` |
| *Send a message instead →* | index / practice-areas / attorney-bio | **44px** | 193 | `44px` |
| `a.brand` (logo link) | all four | **44px** | 101 | `44px` |

Round 1: all four at **28px**, logo at **38px**. All now exactly 44px on every page they appear
on, and the logo miss round 1 called "the same family" is fixed too.

**One thing the fix did not reach, and did not cause.** Sweeping every standalone link/button
under **44px** (round 1's harness used a 40px threshold, so these were never on its list):
`.btn-call` **42.7px**, footer `.phone` **42px**, the footer nav row links **32px**, and the
footer's inline `973-344-0808` **25.9px**. None of these is a regression — nothing in fixes 1–8
touches them, and they measure the same as they did before. Observation for the lead only:
`.btn-call` and `.phone` are 1.3px and 2px short of the 44px line and would close with a single
`min-height` added to the same `(pointer:coarse)` block that fix 7 introduced.

---

## Round-1 item 9 (the lead's "fix 8") — recognition h3 wrap · **APPLIED BUT INEFFECTIVE (non-gating)**

`.cmp h3` now computes `text-wrap: balance` and `margin-right: 56px` on all three recognition
blocks. Measured @1440:

| Cell | cell width | h3 width | h3 height | lines | body top |
|---|---|---|---|---|---|
| Legal commentator | 444 | 323 | 28 | 1 | **2015** |
| Adjunct Professor | 355 | 235 | 28 | 1 | **2015** |
| Hudson County Ethics Committee | 266 | **146** | **110** | **4** | **2098** |

Still **4 lines**, so the bodies still do not share a Y origin (2015 / 2015 / 2098) — unchanged
from round 1. `text-wrap: balance` cannot help here: the constraint is width, not distribution,
and the newly added `margin-right: 56px` actually *narrows* this h3 to 146px of a 266px cell.
The 56px gutter exists to clear the folio numeral, but **these three compartments have no
`.num`** (`hasNum: false` on all three), so on this row it is 56px of reserved space paid for
nothing.

Round 1 counted this as the *minor consequential* item, not one of the four gating composition
failures, and explicitly listed it under "fixes I would ask for but would not gate on." That
classification is unchanged, so **it does not block sign-off.** If it is ever worth a touch, the
cheap version is scoping the 56px gutter to compartments that actually carry a numeral
(`.cmp:has(.num) h3`), which gives this h3 202px and drops it to 3 lines; the alternative round 1
named — spans 5/4/3 → 4/4/4 for that row — also works.

---

## Ripple check — fix 2 (`.cmp` became a flex column) · **NO REGRESSION**

`.cmp` is used on three pages. All 11 instances measured, children walked, internal spacing
compared against the block-flow values:

| Page | `.cmp` count | display / dir | internal spacing |
|---|---|---|---|
| index (practice grid) | 4 | `flex` / `column` | numeral 20→60, brass rule at 30 (out of flow), h3 at 50, body at 88, go at 172 — identical across all four cells |
| practice-areas (criminal sub-ledger) | 4 | `flex` / `column` | h3 at 26, body at 60 (or 83 where the h3 wraps to 2 lines), `margin-top: 10.4px` on the body intact |
| attorney-bio (recognition) | 3 | `flex` / `column` | h3 at 30, body at 68 (151 in the 4-line cell), same 10.4px |
| contact | 0 | — | no compartments |

No margin collapsed away and nothing shifted: the only in-flow margins inside a compartment are
`.lrule { margin-bottom: 17.6px }` and `p { margin-top: 10.4px }`, neither of which was
collapsing against a sibling in block flow, so `display:flex` changed no geometry. `margin-top:
auto` only resolves on the `.go` span, which exists solely in the index grid — the sub-ledger and
recognition compartments have no go-link and are unaffected. Every compartment's padding-bottom
is unchanged (30.4px / 25.6px) and the shortest-cell slack is the same equal-height-row artifact
round 1 already accepted (57px on *Sex Offenses*, 84px on *Adjunct Professor*).

---

## Ripple check — fix 3 (real markup change on `practice-areas.html`) · **NO REGRESSION**

**@375:** `#family` `ul` computes `grid-template-columns: 330px` — a **single column** on phone,
one x origin (23), all 7 items present, hairlines intact, item heights 55px (83px for the
two-line *Juvenile delinquency…*). `document.scrollWidth 375 == innerWidth 375` → **no
horizontal overflow.** The 2-column treatment is desktop-only, which is the right mobile
decision rather than a squeezed two-up.

**Sticky progress rail, desktop @1440:** `position: sticky`, `top: 92px`. Before scroll its top
is 467; after `scrollTo(0, 1800)` it is **92** — it pins exactly at its offset and stays in
place.

**Rail as a scrollable tab row @375:** `display: flex`, `overflow-x: auto`,
**`scrollWidth 568 > clientWidth 375`** → still scrollable. Scrolled to the end
(`scrollLeft 193`), the last tab *04 Real Estate* sits at x 235, **141 × 51px**, and
`document.elementFromPoint` at its centre resolves **inside the link** — so round 1's
false-positive-cleared behaviour still holds after the restructure.

**`main.js` is byte-identical to round 1** (6423 bytes, md5 `35f9e2fa6a172b5f12a6362f58d321a4`),
so the rail's `aria-current` progress logic is untouched code, not re-verified behaviour by
accident.

**Visual confirmation of the restructure** (crop off the 1440 full-page capture): two ruled
columns with a vertical hairline divider, 4 items left / 3 right, a hairline under every row, and
the odd 7th slot leaves a clean ragged bottom — the divider and the row rule both stop at the
last filled row, so there is **no dangling rule and no empty bordered cell**. The group still
reads as one ledger, not as two lists.

---

## Hard gate re-confirmed — fail-visible hidden text · **PASS**

Measured at 1440×900 **after** sweeping the whole page top-to-bottom in 400px steps and
returning to scroll 0 (so every `IntersectionObserver` reveal has fired), and **without** forcing
any `.in` classes. Every text node's real computed visibility checked up its whole ancestor chain
(`display`, `visibility`, `opacity` < 0.05, `clip-path: inset(≥90%)`, zero-size).

| Page | text chars | hidden chars | hidden % | `<html>` class | only hidden string |
|---|---|---|---|---|---|
| index | 3192 | 17 | **0.53%** | `" js"` | `Call 973-344-0808` (mobile bar) |
| practice-areas | 2541 | 17 | **0.67%** | `" js"` | same |
| attorney-bio | 2625 | 17 | **0.65%** | `" js"` | same |
| contact | 1182 | 17 | **1.44%** | `" js"` | same |

The single hidden string on each page is the sticky `.mobile-call` bar, which is `display:none`
above 375 by design — a mobile-only element correctly absent at desktop, not hidden content.
**Real hidden-at-rest: 0.00%**, against a ~15% ceiling. No regression from round 1 (identical
figures).

---

## Hard gate re-confirmed — live JS-off reload · **PASS, `main.js` restored**

`main.js` physically renamed out of `mockup/` (verified `http://localhost:8912/main.js` →
**404**), each page loaded fresh and given 2800–3000 ms — past the 1200 ms dead-man timer —
then measured.

| Page | `<html>` class | text chars | hidden % | visible `tel:` | visible buttons |
|---|---|---|---|---|---|
| index | **`""`** | 3192 | 0.53% | 4 of 5 | 2 of 3 |
| practice-areas | **`""`** | 2541 | 0.67% | 5 of 6 | 2 of 3 |
| attorney-bio | **`""`** | 2625 | 0.65% | 3 of 4 | 1 of 2 |
| contact | **`""`** | 1182 | 1.44% | 4 of 5 | 2 of 3 |

`.js` is stripped from `<html>` on all four pages, so nothing is ever hidden. The one
non-visible `tel:` and the one non-visible button on each page are the same mobile-only
`.mobile-call` bar and its brass link. Every word readable, every desktop CTA full-size.

**`main.js` restored and verified: 6423 bytes, md5 `35f9e2fa6a172b5f12a6362f58d321a4`** —
byte-identical to before the test, and `git status` shows no new modification from this audit.

---

## Frozen things re-confirmed

- **Palette:** nine tokens at exact hex, no tenth hue (measured above).
- **`contact.html` map, Harry's uncommitted hand-edit:** the OpenStreetMap
  `<iframe class="map-embed">` is present with `loading="lazy"`,
  `referrerpolicy="no-referrer-when-downgrade"` and
  `title="Map location: 385 Lafayette Street, Newark, NJ 07105"`, **and** the Google
  `maps/search/?api=1&query=385+Lafayette+Street,+Newark,+NJ+07105` "Get directions" link with
  `target="_blank" rel="noopener"`. Same provider, same URLs, same attributes. Intact.
- **Copy voice, re-run because fix 3 edited real markup:** `copycheck.py` **exit 0** on all four
  pages, `aitells.py` **exit 0** across all pages (11 checkable claims on index, 7 on
  practice-areas, no hero verb openers, no abstract-pair titles, no card symmetry). Copy itself
  was untouched — the 7 family-law strings are verbatim — so this is a confirmation, not a
  re-gate.
- **Step 0 detector, re-run independently:** `exit 0` on all four pages, no output (0 errors,
  0 advisory). `grep impeccable-disable` → **0 waivers** in every HTML file and in `style.css`.

---

## The composition checks — the one gate that was failing

Re-run of the four unexcused failures, plus the one minor consequential item:

| Check | Round 1 | Round 2 measured | Verdict |
|---|---|---|---|
| Headline ≤ 2 lines | **FAIL** — 3 lines (80px / 250px box) | 2 lines at 1280, 1440 **and** 1600 (68px / 141px box) | **PASS** |
| Card CTAs bottom-align across a row | **FAIL** — 28px out in both rows | `goTop` 1742 = 1742 and 1988 = 1988 | **PASS** |
| Lists > 5 items need a real component | **FAIL** — 7 items, one column, hairline per row | 7 items in a **2-column grid** (4 + 3), `399px / 399px` | **PASS** |
| Skip-to-content link as first focusable | **FAIL** — 0 hits | first focusable on all 4 pages, off-screen at rest, 153×54 brass on focus | **PASS** |
| Parallel lists share a Y origin | FAIL (minor, non-gating) | still 2015 / 2015 / **2098** — 4-line h3 unchanged | **still off, non-gating** |

The four exceptions round 1 accepted with the Stage 5 brief cited (alternating ink bands, flat
compartments carrying weight in ≥2 cells, 4 eyebrows against a cap of 3, the ledger index range
as page furniture) are untouched by these fixes and stand as recorded.

**Composition checks: all four unexcused failures now pass.** The remaining Y-origin item was
explicitly non-gating in round 1 and is unchanged in status.

---

## Round-2 scoreboards

Round 1's scoreboards stand, with the specific deductions that referenced the now-fixed items
noted as resolved. Nothing was re-scored from scratch.

### `web-design-ultra` Stage 8

**Gate A — Detector: 0 errors, 0 advisory on all four pages (exit 0), 0 waivers in file.**
**Fail-visible: 0.00% hidden at rest (0.53–1.44% measured, all of it the mobile-only call bar).**
**Composition checks: all pass or brief-excused.**

| # | Dimension | Round 1 | Round 2 | Note |
|---|---|---|---|---|
| 1 | Boldness / distinctiveness | 8 | **8** | carried; h1 now at its spec'd 2 lines |
| 2 | Visual hierarchy | 9 | **9** | carried |
| 3 | Typography craft | 9 | **9** | carried — one of its two deductions (3-line h1) is resolved; the 4-line recognition h3 remains |
| 4 | Color & contrast | 9 | **9** | carried — the 0.10-short folio numeral is resolved (2.90:1 → 5.17:1) |
| 5 | Spacing rhythm | 8 | **8** | carried — go-link alignment resolved; the mobile CTA/bar 3px overlap remains |
| 6 | Background / depth | 8 | **8** | carried, untouched |
| 7 | Imagery quality | 8 | **8** | carried, untouched — no new generation this round, 2-image cap intact |
| 8 | Responsiveness | 8 | **8** | carried — the four 28px tap targets and the 38px logo are resolved; the 3px hero/bar overlap remains |
| 9 | Motion polish | 9 | **9** | carried — `main.js` byte-identical |
| 10 | Cohesion | 9 | **9** | carried — the skip link and the 2-col ledger both read in-direction |

**Boldness 8 ≥ 8 ✓ · lowest 8 ≥ 7 ✓ → rubric PASSES.**

### $10K Checklist — 8 / 8

| # | Item | Verdict | Source |
|---|---|---|---|
| 1 | Point of view, not a template | **PASS** | round 1, carried |
| 2 | Typography that does work | **PASS** | round 1, carried — its noted h1 fix is now applied |
| 3 | Restrained color system | **PASS** | re-verified: 9 tokens, no tenth hue |
| 4 | Hierarchy that breathes | **PASS** | round 1, carried |
| 5 | Imagery with intent | **PASS** | round 1, carried; no image touched |
| 6 | Motion that whispers | **PASS** | round 1, carried; `main.js` unchanged |
| 7 | Mobile that's designed, not shrunk | **PASS** | round 1, carried; tap targets now 44px, mobile screenshots on disk |
| 8 | The invisible expensive stuff | **PASS** | JS-off re-verified live; skip link added; folio contrast now 5.17:1; detector exit 0 |

Also standing from round 1: content parity PASS, palette freeze PASS, real-reviews-only PASS,
click-test PASS (zero dead clicks), distinctiveness PASS (a genuine value-structure flip, not
Rev 2 in a new font), copy voice PASS.

---

## Round-2 verdict

**PASS — recommended for sign-off.** The single gate holding round 1 back, the countable
composition checks, now passes: all four unexcused failures measure correct, at three viewport
widths where relevant, and none of the fixes regressed anything. Both hard gates re-confirmed
live (0.00% hidden at rest; `.js` stripped and every word readable with `main.js` renamed away,
then restored byte-identical). Palette and Harry's map hand-edit intact. Detector still exit 0
with zero waivers.

**Two items remain open and both were non-gating in round 1:**

1. **Fix 6 was not applied.** The mobile hero's brass `Call 973-344-0808` (y 702–758) still
   overlaps the fixed `.mobile-call` bar (top y 755) by **3px** at 375×812, scroll 0 — the hero
   CTA row's `margin-bottom` computes to 0px. It is the most visible remaining flaw: the capture
   shows three identical brass call buttons in the first screen, two of them touching and reading
   as one doubled slab. Not a composition check, not a $10K item, inside dimensions already
   scored 8 — so it does not block, but it is a real cosmetic miss and worth one more builder
   round if the lead wants it closed before delivery.
2. **The recognition h3 still wraps to 4 lines**, so those three bodies still do not share a Y
   origin (2015 / 2015 / 2098). `text-wrap: balance` was applied but cannot help a
   width-constrained h3, and the added `margin-right: 3.5rem` narrows it to 146px of a 266px
   cell for a folio numeral those compartments don't have.

Observation for the lead only, not a fix: `.btn-call` (42.7px) and the footer `.phone` (42px) sit
just under 44px on touch. Round 1's harness used a 40px threshold so they were never on the fix
list; they are not regressions and would close with one `min-height` in the `(pointer:coarse)`
block fix 7 already created.

*Sign-off, the `design-memory.md` row and the `/design-push` are the lead's — not decided here.
No message was sent to the builder.*

---
---

# ROUND 3 — the three polish fixes (`style.css` settled 06:43:28)

`main.js` is still byte-identical (6423 B, md5 `35f9e2fa6a172b5f12a6362f58d321a4`); only
`style.css` changed (34.8 KB → 36.0 KB). Everything below is measured against that build.

## The hero / call-bar collision · **FIXED — real 33px gap**

The builder did not add a bottom margin; it tightened the hero's rhythm at `style.css:721–731`
inside `@media (max-width:719px)` (`.hero{padding-top:1.5rem}`, `.hero-rule-top{margin-top:1.5rem}`,
`.hero-foot .shell{padding-block:.9rem}`) with a comment citing the collision.

**A note on method, because the first run gave a wrong answer.** My first measurement returned the
button at y 838–894 with the header at **336px**. That was contaminated: the mobile nav panel was
momentarily expanded, inflating the header by 172px and pushing the whole hero down. A diagnostic
pass (`aria-expanded="false"`, `#primary-nav` `display:none`, `headerH: 164`, `htmlClass: " js"`,
zero console errors, zero failed requests) established the steady state, so I re-measured with a
**precondition guard** — the numbers below are only accepted from a trial where
`headerH === 164` and the toggle reads collapsed.

Measured at **375×812, `scrollY: 0`**, steady state confirmed:

| Element | top | bottom | height |
|---|---|---|---|
| Hero `a.btn.btn-primary` "Call 973-344-0808" | **667** | **722** | 56 |
| Fixed `.mobile-call` bar | **755** | 812 | 57 |

**Gap = +33px** (round 2: **−3px**). `btnFullyAboveBar: true`, `btnFullyVisible: true`. The hero
button moved up 36px, exactly what the tightening was meant to buy. Confirmed on the capture: a
clear porcelain strip now separates the two brass slabs, so they no longer read as one doubled
button. **This item is resolved.**

### Hero still fits one screen — yes, with one honest caveat

Hero spans y **164 → 798** (height 634) in an 812 viewport, so the whole section fits above the
fold. Order inside it after the tightening: h1 **188–417** (5 lines at 375), sub **441–562**,
hero-rule **586**, hero-foot shell **587–797**. No horizontal overflow on any page
(`scrollWidth 375 == innerWidth 375`, all four pages).

> **Correction.** The first version of this line quoted h1 360–588 / sub 612–734 / rule 758 /
> foot 759–968. Those came from the contaminated trial (expanded nav, 336px header) and were
> ~172px too low throughout. The hero *section* bounds and the +33px gap were always from the
> guarded trial and are unchanged; only these four internal offsets were wrong.

**Nothing new was pushed into the bar, but one thing sits under it:** the secondary
`Send a message →` text-link spans y **738–782**, so its lower ~27px is behind the fixed bar at
scroll 0 (visible in the capture as clipped glyphs above the brass bar). This is **not a
regression** — before the tightening that link sat 36px lower, i.e. entirely behind the bar and
partly below the viewport, so it is strictly better than round 2. It is also not a dead click: the
link is reachable and fully visible after any scroll, and it is the *secondary* action while the
primary brass CTA is fully clear. Inherent to pairing a fixed bottom bar with a hero that ends at
798 of 812. **Non-gating**, same family as the original item; if the lead wants it perfect, ~30px
off the `.hero-foot .shell` bottom gap closes it.

## Recognition h3 — scoped gutter · **FIXED as predicted**

`style.css:322–324` now reads `.cmp h3{text-wrap:balance}` with the gutter split out as
`.cmp:has(.num) h3{margin-right:3.5rem}`. Measured @1440:

| Cell | cell width | h3 width | h3 height | lines | body top |
|---|---|---|---|---|---|
| Legal commentator | 444 | 379 | 28 | 1 | 2015 |
| Adjunct Professor | 355 | 291 | 28 | 1 | 2015 |
| Hudson County Ethics Committee | 266 | **202** (was 146) | **83** (was 110) | **3** (was 4) | **2070** (was 2098) |

`margin-right` computes to **0px** on all three numeral-less compartments — exactly the predicted
202px width and 3 lines. **And the scoping didn't cost the cells that need the gutter:** all four
index practice compartments still compute `margin-right: 56px`, and each h3's right edge still
clears its folio numeral's left edge (620 < 633, 1063 < 1070, 531 < 537, 1063 < 1071), all still
one line. The three recognition bodies still don't share a single Y origin (2015 / 2015 / 2070),
but the deviation shrank from 83px to 55px — and this was the non-gating item throughout.

## Tap targets · **FIXED**

`style.css:266` adds `.brand,.btn-call,.phone{min-height:44px}` to the `(pointer:coarse)` block.
Measured at 375 with `matchMedia('(pointer: coarse)')` → `true`:

| Element | round 2 | round 3 |
|---|---|---|
| `.btn-call` | 42.7px | **44px** |
| footer `.phone` | 42px | **44px** |
| `.brand` (logo) | 44px | **44px** |
| `.text-link` ×4 | 44px | **44px** |
| `.map-caption` "Get directions" | — | **44px** |

Still under 44 and never on any fix list (not regressions, all unchanged): the footer nav row
links at **32px** ×4 per page, the footer's inline `973-344-0808` at **25.9px**, and contact's
`.big` phone at **37.8px**. Observation for the lead only.

## Hard gates re-run against the new `style.css`

**Fail-visible (JS on, full sweep top-to-bottom then back to 0 before measuring, no forced
reveals):**

| Page | text chars | hidden | hidden % | `<html>` | only hidden string |
|---|---|---|---|---|---|
| index | 3192 | 17 | **0.53%** | `" js"` | `Call 973-344-0808` (mobile bar) |
| practice-areas | 2541 | 17 | **0.67%** | `" js"` | same |
| attorney-bio | 2625 | 17 | **0.65%** | `" js"` | same |
| contact | 1182 | 17 | **1.44%** | `" js"` | same |

**Real hidden at rest: 0.00%** — unchanged, against a ~15% ceiling.

**Live JS-off reload** — `main.js` renamed out (`http://localhost:8912/main.js` → **404**), each
page loaded fresh for 3000 ms in its own browser:

| Page | `<html>` | hidden % | visible `tel:` | visible buttons |
|---|---|---|---|---|
| index | **`""`** | 0.53% | 4 of 5 | 2 of 3 |
| practice-areas | **`""`** | 0.67% | 5 of 6 | 2 of 3 |
| attorney-bio | **`""`** | 0.65% | 3 of 4 | 1 of 2 |
| contact | **`""`** | 1.44% | 4 of 5 | 2 of 3 |

`.js` stripped on all four by the dead-man timer; the single non-visible `tel:`/button per page is
the mobile-only bar. **`main.js` restored, 6423 bytes, md5 `35f9e2fa6a172b5f12a6362f58d321a4`** —
byte-identical, no parked leftover, `git status` shows the same six modified files as before this
audit and nothing else.

**Also re-confirmed after the CSS change:** Step 0 detector **exit 0 on all four pages**;
`aitells.py` **exit 0**; palette still exactly the nine tokens plus `#fff` — **no tenth hue**;
`contact.html`'s OSM iframe (`loading="lazy"`, `referrerpolicy="no-referrer-when-downgrade"`,
`title="Map location: 385 Lafayette Street, Newark, NJ 07105"`) and the Google
`maps/search/?api=1&query=385+Lafayette+Street,+Newark,+NJ+07105` "Get directions" link
(`target="_blank" rel="noopener"`) **both intact**.

## Round-3 verdict

**PASS — recommended for sign-off.** All three polish fixes verified by measurement, all gates
re-run green against the changed stylesheet, nothing regressed, `main.js` untouched and restored.

Score movement, stated conservatively: the two dimensions whose round-2 deductions were the CTA
collision and the tap targets (5 spacing rhythm, 8 responsiveness) have each lost their remaining
named deduction, but I am **carrying both at 8** rather than raising them — the contact-form and
bio white space that round 1 also cited under spacing is unchanged, and I have not re-audited the
untouched areas that would justify a 9. Rubric stands at **8/9/9/9/8/8/8/8/9/9**, boldness 8,
lowest 8. $10K stands at **8/8**. Composition checks: all pass or brief-excused.

Nothing gating is open. The one cosmetic item left is the secondary `Send a message →` link's
lower half sitting under the fixed bar at scroll 0 — better than it was, non-gating, and the
lead's call whether to spend another round on it.

---

## ROUND 4 — independent re-verification with a proven-fresh stylesheet

The lead flagged that both numbers might have been read off a stale build (citing a `style.css`
write at 06:44:56). Both were re-measured from scratch on a **new server (port 8913), a new Chrome
profile, and `Network.setCacheDisabled: true`**, with the freshness asserted *inside the page*
before either measurement was accepted.

**The file on disk is a single state, and it is the one measured.** `style.css` =
**36,003 bytes**, md5 `3c5c0c3761d75fafca94524fd19d5fc4`, mtime **2026-07-30 06:43:28** local
(10:43:28Z). There is no 06:44:56 version on disk; that timestamp does not correspond to any state
of this file. Both cited rules are present in it: line **324** `.cmp:has(.num) h3{margin-right:3.5rem}`
and lines **724–726** the hero tightening.

**Freshness assertions, all four green in the accepted trial:**

| Assertion | Result |
|---|---|
| Stylesheet re-fetched in-page with `cache: 'no-store'` | **36,003 bytes** — byte-count matches disk exactly |
| Scoped-gutter rule in the fetched text | **true** |
| Hero-tighten rule in the fetched text | **true** |
| Scoped rule live in the **CSSOM** the page paints from | `.cmp:has(.num) h3 { margin-right: 3.5rem; }` |
| Hero-tighten rule live in the CSSOM (inside the 719px media block) | `.hero-rule-top { margin-top: 1.5rem; }` |
| Loaded sheet href | `http://localhost:8913/style.css` |
| The lead's stale-detector (`margin-right: 56px` on a numeral-less h3) | **false** — not stale |

### 1 · Collision @375×812, scrollY 0 — **gap is ≥ 0: +33px**

Accepted on the first trial with all preconditions green (`headerH 164`, `aria-expanded="false"`,
`#primary-nav display:none`, `htmlClass " js"`, computed `.hero{padding-top:24px}` = 1.5rem,
`.hero-rule-top{margin-top:24px}` = 1.5rem, `.hero-foot .shell{padding-top:14.4px}` = .9rem):

| | round 2 | round 4 (fresh) |
|---|---|---|
| Hero `a.btn.btn-primary` | 702 → **758** | 667 → **722** |
| `.mobile-call` top | 755 | 755 |
| **Gap** | **−3px** | **+33px** |
| `btnFullyAboveBar` | false | **true** |

Identical to round 3, now with the stylesheet's identity proven rather than assumed.

**One screen, nothing new pushed into the bar.** Hero 164 → 798 of an 812 viewport; internals
h1 188–417, sub 441–562, rule 586, foot 587–797; no horizontal overflow. Exactly **one**
non-fixed element reaches into the bar's band: the secondary `Send a message →` text-link at
**738–782**, i.e. **27px under the bar** — better than round 2, where it sat 36px lower and was
entirely behind it. Not a dead click, fully visible after any scroll, and the primary brass CTA is
completely clear.

### 2 · Recognition h3 @1440 — **gutter gone, 3 lines**

| Cell | cell W | computed `margin-right` | h3 W | h3 H | lines | body top |
|---|---|---|---|---|---|---|
| Legal commentator | 444 | **0px** | 379 | 28 | 1 | **2015** |
| Adjunct Professor | 355 | **0px** | 291 | 28 | 1 | **2015** |
| Hudson County Ethics Committee | 266 | **0px** | **202** | **83** | **3** | **2070** |

Round 2 was 146px / 110px / 4 lines / 2098 with `margin-right: 56px`. The lead's prediction was
exact: **202px and 3 lines.**

**Do the three bodies share a Y origin? No — 2015 / 2015 / 2070, spread 55px** (was 83px). The
first two align; the third still starts 55px lower because its h3 is 3 lines against their 1. So
that composition check is *improved but still not satisfied* — it was the non-gating "minor
consequential" item in round 1 and remains non-gating. Closing it properly needs the row spans
changed (5/4/3 → 4/4/4), which is a layout decision, not a one-liner.

**The scoping did not cost the cells that need the gutter:** all four index practice compartments
still compute `margin-right: 56px`, and every h3's right edge still clears its folio numeral's
left edge (620 < 633 · 1063 < 1070 · 531 < 537 · 1063 < 1071).

### Round-4 verdict

**Both contested numbers confirmed against a proven-fresh stylesheet. PASS stands.** No score
changes from round 3: rubric **8/9/9/9/8/8/8/8/9/9** (boldness 8, lowest 8), $10K **8/8**,
composition checks all pass or brief-excused, nothing gating open. Two non-gating cosmetics
remain: the secondary hero link 27px under the fixed bar, and the recognition row's third body
55px off the shared Y origin.
