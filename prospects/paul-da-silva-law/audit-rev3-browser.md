# Audit — `paul-da-silva-law` Rev 3 · BROWSER-DEPENDENT HALF

**Review round: 1** (Rev 3) · Critic: `critic-rev3-browser` · 2026-07-30
Scope: the six browser gates the lead assigned (live JS-off reload, composition checks,
10-dimension rubric, $10K items 1–7, measured contrast, distinctiveness) + the interactive
click-test. Static/content/copy gates are NOT re-scored here — see
`audit-rev3-lead-static.md` and `audit-rev3-content.md`.

Pre-gates taken on trust (not re-run): Step 0 detector exit 0 / 0 errors / 0 advisory ×4,
0 waivers; `copycheck.py` exit 0 ×4; `aitells.py` exit 0; fail-visible 0.0% hidden at rest
×4; 0 console errors; 0 horizontal overflow at 1440/375.

---

## Gate 1 — LIVE JS-off reload · **PASS**

Method: `main.js` physically renamed out of the mockup directory (verified `http://localhost:8747/main.js`
→ **404**), then all four pages loaded in headless Chrome at 1440×900, waited **2600 ms** (past the
1200 ms dead-man timer), scrolled top-to-bottom and back, then measured every text node's real
computed visibility up its whole ancestor chain (`display`, `visibility`, `opacity`, zero-size,
and `clip-path: inset()` ≥ 90%). `main.js` restored immediately after and verified present
(6423 bytes, md5 `35f9e2fa6a172b5f12a6362f58d321a4`).

| Page | `documentElement.className` | Text chars | Hidden | Visible `tel:` links | Buttons hidden |
|---|---|---|---|---|---|
| index | **`""`** | 3177 | 0.54% | 4 of 5 | 0 of 2 |
| practice-areas | **`""`** | 2526 | 0.67% | 5 of 6 | 0 of 2 |
| attorney-bio | **`""`** | 2610 | 0.65% | 3 of 4 | 0 of 1 |
| contact | **`""`** | 1167 | 1.46% | 4 of 5 | 0 of 2 |

The `.js` class is **gone from `<html>` on every page** — the dead-man timer fired exactly as
designed, so the architecture the lead verified statically works live.

**The sub-2% residue is not hidden content.** On all four pages the *only* hidden string is a
single `Call 973-344-0808`, and it is the sticky mobile call bar: `style.css:575`
`.mobile-call{display:none}`, promoted to `display:block; position:fixed; bottom:0` only inside
the 375px media block (`style.css:740`). A mobile-only element correctly absent at 1440 is not
JS-hidden content. **Real hidden-at-rest with JS off: 0.00%.** Four other `tel:` links per page
remain visible and full-size (206×49, 216×56, 488×76, 103×26 on index), and every `.btn` /
`.btn-call` / submit button renders at full size. Full-page JS-off capture:
`scratchpad/live-nojs-index.png` (4618 px tall, complete).

Item 8's JS-off clause therefore holds live, not just in principle.

---

## Gate 5 — Measured WCAG AA contrast · **PASS, with one 0.1-short decorative numeral**

All ratios computed from the actual token hex values (WCAG 2.x relative-luminance formula),
then each pairing traced to the CSS rule that actually uses it.

**Body / UI text — all comfortably AA:**

| Foreground | Ground | Ratio | Threshold | Verdict |
|---|---|---|---|---|
| `--ink #161A24` | `--pedra #F0F2F5` | **15.51:1** | 4.5 | PASS |
| `--ink` | `#fff` (compartment fill) | **17.39:1** | 4.5 | PASS |
| `--muted #566072` | `--pedra` | **5.65:1** | 4.5 | PASS |
| `--muted` | `#fff` | **6.34:1** | 4.5 | PASS |
| `--ouro-escuro #806026` | `--pedra` | **5.17:1** | 4.5 | PASS |
| `--ouro-escuro` | `#fff` | **5.80:1** | 4.5 | PASS |
| `--pedra` | `--tinta #131D33` | **14.96:1** | 4.5 | PASS |
| `--pedra` | `--tinta-2 #0D1526` | **16.25:1** | 4.5 | PASS |
| `--linha #C8CDD6` | `--tinta` | **10.52:1** | 4.5 | PASS |
| `--linha` | `--tinta-2` | **11.42:1** | 4.5 | PASS |
| `--lamp #EAD9AE` | `--tinta` | **12.02:1** | 4.5 | PASS |
| `--lamp` | `--tinta-2` | **13.05:1** | 4.5 | PASS |
| `--ouro #B3873E` | `--tinta` | **5.16:1** | 4.5 | PASS |
| `--ink` on `--ouro` (call button label) | — | **5.34:1** | 4.5 | PASS |
| `--ink` on `--lamp` (button hover fill) | — | **12.45:1** | 4.5 | PASS |

The light-first inversion is genuinely safer than Rev 2, not just different: the plan's rule
that `--ouro` is **never** body text on light grounds is honored — `grep` for
`color:var(--ouro)` returns exactly **one** text rule in the whole stylesheet (`.num`,
`style.css:122`), plus non-text uses (button fills, `border-bottom-color`, a 2px rule).
Inline practice links on `practice-areas.html` use `--ouro-escuro` on pedra (5.17:1), which is
the fix the plan promised over Rev 2's `--lamp`-on-ink link.

**The one finding — `--ouro` folio numerals:**

| Instance | Ground | Size | Ratio | Large-text threshold | Verdict |
|---|---|---|---|---|---|
| `.cmp .num` (home practice compartments, criminal sub-ledger, recognition blocks) | `#fff` (`style.css:290`) | 2.5rem / 40px | **3.25:1** | 3.0 | PASS |
| `.cmp:hover .num` → `--ouro-escuro` on `--pedra` hover fill | `--pedra` | 40px | **5.17:1** | 3.0 | PASS |
| `.band-ink .num` → `--lamp` | `--tinta` | 40px | **12.02:1** | 3.0 | PASS |
| **`.grp-head .num`** (practice-areas group folios 01–04, `style.css:440`) | **`--pedra` page ground** | **2rem / 32px** | **2.90:1** | 3.0 | **0.10 SHORT** |

`.grp-head` has no fill of its own (`style.css:435–439` — only top/bottom `--linha` rules), so
those four numerals sit `--ouro` directly on `--pedra` at **2.90:1** against a 3:1 large-text
floor. Every *other* numeral in the site is on `#fff` (3.25:1) and clears it.

**Severity — advisory, not an item-8 fail.** These four glyphs are decorative folio indices
that duplicate information already carried in AA-compliant text twice over: the sticky rail
(`01 Criminal Defense` …, `--muted`/`--ink`) and the adjacent h2. WCAG 1.4.3 exempts
incidental text, and nothing is lost if a reader can't resolve them. Item 8 was already scored
by the lead and this doesn't reopen it. **Recommended one-line fix** (not gating):
`.grp-head .num{color:var(--ouro-escuro)}` → 5.17:1, and it matches the plan's own R3-9
practice-areas spec, which asks for the index range in `--ouro-escuro` on pedra.

Non-text `--linha` hairlines on `--pedra` measure **1.42:1** — deliberate and correct. They are
decorative rules, not UI-component boundaries carrying state or meaning, and the 1.4.11 3:1
requirement doesn't reach them. Field boundaries that *do* carry state (form focus) use a 2px
`--tinta` rule (14.96:1 vs pedra).

The form has **no `placeholder` attributes at all** — real visible `<label>`s in `--muted` on
`#fff` (6.34:1). That sidesteps the composition checks' most common miss ("light placeholders on
a near-white form") by not having placeholders.

---

## Gate 2 — Countable composition checks · **4 CHECKS FAIL UNEXCUSED**

Measured in the live DOM, not eyeballed off a scaled screenshot.

### Hero (index @1440) — passes

| Check | Threshold | Measured | Verdict |
|---|---|---|---|
| Headline lines | ≤ 2 | **3** (box 250px ÷ 83px line-height, font 80px, measure 1066px) | **FAIL** |
| Subtext words | ≤ 20 | **18** | PASS |
| Text elements in hero | ≤ 4 | **3** + CTA row = 4 (h1, sub, language lines; no eyebrow — the masthead *is* the identity) | PASS |
| Hero top padding | ≤ ~6rem | **80px (5rem)** | PASS |
| CTA visible without scrolling | — | yes, CTA row at y≈600 of 900 | PASS |
| Trust strip inside hero | must be outside | outside — the record row is its own ink section | PASS |
| Italic display descender clearance | — | h1 is roman; italic is used only at 2.5rem numerals / quotes, no clipping | PASS |

### Navigation, CTAs, sections — pass

| Check | Measured | Verdict |
|---|---|---|
| Nav one line, ≤ 80px | main deck **74px** (masthead total 114px incl. the utility top deck — a named archetype in R3-9) | PASS |
| No CTA label wraps at desktop | none wrap | PASS |
| No two CTAs share an intent | one primary (`Call 973-344-0808`) + one secondary (`Send a message`); repeated tap-to-call is the `local-trade.md` exception | PASS |
| Zigzag cap ≤ 2 consecutive splits | **1** image+text split per page total | PASS |
| Split-header ban | no section uses headline-left / explainer-right as a header | PASS |
| Layout variety ≥ 4 families for 8 sections | **8 distinct**: masthead hero · mounted photo band · ruled record row · asymmetric compartment grid · split compartment · asymmetric ink band · ruled quote columns · asymmetric CTA | PASS |
| ≤ 1 marquee per page | **0** | PASS |
| Grid cell count == item count | practice 4/4 · record 4/4 · criminal sub-ledger 4/4 · recognition 3/3 · reviews 3/3 — **no empty tiles** | PASS |
| One theme (no alternation) | pedra / ink / pedra / ink / pedra / ink — **alternates**, but this is the brief's named device (R3-1, R3-3, R3-8: "ink bands as punctuation"), and the bands share identical grammar | **exception, brief cites it** |
| One accent colour | brass only, identically everywhere | PASS |
| One corner-radius system | `--radius: 0` — all-sharp, no exceptions found | PASS |
| Multi-cell grid carries weight in ≥ 2 cells | every cell is text-on-flat-white **plus** a 2.5rem brass folio numeral and a 2px brass rule per cell | **exception, brief cites it** (R3-5/R3-6 lock "flat bordered containers / service index-ledger"; flatness is the archetype, and the numerals are real non-text marks) |

### Labels, dressing, alignment — two fail

| Check | Measured | Verdict |
|---|---|---|
| Eyebrow count ≤ ceil(sections ÷ 3) | index: **4** `.label` across **7** sections; cap = 3 | **1 over — exception, brief cites it** (R3-6 rotates three structurally different treatments: ruled header row / rotated side label / bare label+rule; no stacked eyebrow-over-h2 appears anywhere) |
| No decorative page furniture | no scroll cues, no locale/time strip, no version stamp, no photo credits, no word strip. `01–04` on the practice header and `1993–2002` on the education header sit right-of-heading | **accepted** — a ledger index range whose numerals are actually carried by the compartments, and a real date span; not tile pagination |
| **Card CTAs bottom-align across a row** | compartments are equal height (248px) but go-links are **not** aligned: row 1 `goTop` 1842 vs 1870 (**28px apart**), row 2 2118 vs 2090 (**28px apart**) | **FAIL** |
| Parallel lists share a Y origin | recognition h3s share a Y origin; their **bodies do not**, because the 3-col cell's h3 wraps to 4 lines | **FAIL (minor, same root cause as fix 5)** |
| Optical centering | phone glyph in the brass button reads centred against its label | PASS |
| **Lists > 5 items need a real component** | practice-areas **Family Law = 7 items** as a single `<ul>` of full-width rows with a hairline under each — the exact anti-pattern the check names ("not a longer `<ul>` with a hairline under every row") | **FAIL** |
| Quotes ≤ 3 lines, name + role | all three reviews render **4 lines** in 3 columns; attribution is name + platform | **not actionable** — verbatim protected reviews cannot be shortened, and platform provenance is required by our own real-reviews rule. The only lawful fix is layout (fewer/wider columns), not copy |
| Contrast: CTAs, inputs, placeholders, focus, helper text | see Gate 5 — all AA; **no placeholders exist** | PASS |
| **Skip-to-content link as first focusable** | **absent.** First focusable is `a.brand` (the logo). `grep -i skip` across all four pages and `style.css` → **0 hits** | **FAIL** |
| Privacy / terms links in footer | absent | **exception** — no such pages exist on a 4-page brochure site, and linking to pages that don't exist would be a dead click. The bar-advertising disclaimer block carries the legal text |

**Composition-check result: 4 unexcused failures** (3-line headline, card-CTA bottom-alignment,
the 7-item list, the missing skip link) + 1 minor consequential (recognition Y origin).
Everything else passes or is explained by the locked Stage 5 brief.

---

## Gate 3 — `web-design-ultra` 10-dimension rubric · **PASS (boldness 8, nothing below 7)**

Scored from the builder's desktop + mobile captures for all four pages, native-scale mobile
section crops, a mid-animation frame, and a Rev 2 / Rev 3 first-viewport pair captured
side by side.

| # | Dimension | Score | Reasoning |
|---|---|---|---|
| 1 | **Boldness / distinctiveness** | **8** | A light-first, hairline-ruled ledger is genuinely uncommon in this category, where the default is dark navy + gold or a stock-photo hero. 80px Caslon flush-left across a porcelain masthead, the photograph demoted to a mounted band, collapsed-hairline compartments instead of floating cards — a real point of view, held. Not 9–10 because the boldness is deliberately *grave* rather than spectacular: a stranger says "an unusually well-made law-firm site," not "who made this." For a criminal-defence office that is the right ambition, and it clears the bar. |
| 2 | Visual hierarchy | **9** | Eye lands h1 → CTA row → photograph. The practice grid is deliberately unequal (Criminal 7-col reads senior — the practice's own emphasis); recognition spans 5/4/3 encode importance; folio numerals give a second structural layer without competing with the h3s. Only softness: practice-areas flattens across its three consecutive list groups. |
| 3 | Typography craft | **9** | Genus contrast, not just weight contrast — inky old-style serif against humanist sans, brass caps label as the middle voice. Full scale implemented with real numbers (`--fs-num` etc.). No all-caps Caslon, no letterspaced display serif, no gradient text. Deductions: the h1 runs 3 lines against its own 2-line spec, and the 3-col recognition h3 wraps to 4 lines. |
| 4 | Color & contrast | **9** | Nine frozen tokens, no new hue, alpha-only derivatives; the value inversion is executed with discipline (brass demoted to structure, `--ouro` appears as text in exactly one rule). Measured AA everywhere that carries meaning. One 0.10-short decorative numeral pairing. |
| 5 | Spacing rhythm | **8** | Consistent scale, real breathing, asymmetric content column with the wider right margin as spec'd, compartment padding that scales with `clamp`. Deductions: ~220px of dead white below `Send` in the contact form compartment, ~170px below the bio copy, and the mobile hero CTA overlapping the fixed call bar by 3px. |
| 6 | Background / depth | **8** | Flat porcelain + two low-alpha corner washes + 0.04 grain + real full-bleed structural hairlines + a vertical `--tinta → --tinta-2` gradient on the ink bands. Depth by *rule and value* rather than texture — deliberately pattern-free (the azulejo lattice retired, the dot grid banned to john-sessa). Well judged, but by design the quietest dimension here, so not 9. |
| 7 | Imagery quality | **8** | Two frozen WebP (348 KB hero / 78 KB about), both passing the two-way test, one register (casual natural light, honest level framing), correctly cropped in CSS at 21:9 with `object-position:center 62%` so the storefront line holds. **No readable business name, lettering or signage anywhere in either frame** — awnings blank, no branded vehicle, so the fabricated-branding rule is clean. No rendering tells: brick courses, window frames and awning edges all read straight. Capped at 8 because the site carries only two images and the bio portrait is a labeled placeholder — both correct per the 2-image cap and the never-generate-a-headshot rule, but there is less for this dimension to earn on. |
| 8 | Responsiveness | **8** | Real decisions, not a shrink: 2×2 ruled record grid, single-column compartments with the continuous hairline preserved (reads as one ledger, not four cards), the index rail becoming a genuinely scrollable tab row (`overflow-x:auto`, scrollWidth 568 > clientWidth 375), full-width ruled menu at 53px rows, 44×44 toggle, `body{padding-bottom:56px}` clearing the 57px fixed bar, no overflow. Deductions: four standalone `.text-link` CTAs are **28px** tall on touch (the plan claims ≥44px), the logo link is 38px, and the hero CTA overlaps the fixed bar by 3px at scroll 0. |
| 9 | Motion polish | **9** | Verified live, not inferred. `.rule-bleed.drawx` animates `scaleX 0→1` from `transform-origin:left` over **700ms `cubic-bezier(.16,1,.3,1)`** — sampled at 0 → **0.629** → **0.903** → **0.990** → **1.000**. The 8px `.settle` tail runs 600ms as a subordinate move and never ships alone. Hover transitions `font-variation-settings` over 200ms on a genuinely variable face. One set-piece (sticky index rail, practice page only). One ambient (`.phone::after` brass→lamp glint, 7s with a 72% idle, `mix-blend-mode:screen`) — inside the `prefers-reduced-motion: no-preference` block. Tokens match the spec'd tempo exactly (`--t-draw:700ms --t-settle:600ms --t-hover:200ms --stagger:60ms`). **No GSAP (no `vendor/`), no rAF, no parallax, no count-up, no fade-up-everywhere.** Signature nameable from the artifacts: **rules-draw-in + weight-shift**. Not 10 only because the entrance is one family applied broadly rather than choreographed per section. |
| 10 | Cohesion | **9** | One art director throughout: every page opens label → rule → heading, every section edge is a hairline, brass is only ever structure, radius is 0 everywhere, one ease. The CTA band and footer are genuinely shared components with honest per-page variants (contact drops the address line). |

**Gate: boldness 8 ≥ 8 ✓ · lowest dimension 8 ≥ 7 ✓ → rubric PASSES.**

---

## Gate 4 — $10K Checklist items 1–7 (item 8 already scored by the lead)

| # | Item | Verdict | Reason |
|---|---|---|---|
| 1 | Point of view, not a template | **PASS** | "Counsel of Record" is committed to end to end — light-first ruled ledger, Caslon gravity, brass as fittings. Nothing about it is a template's defaults. |
| 2 | Typography that does work | **PASS** | Libre Caslon Text / Albert Sans. Not the generic four, not on the extended banned set, not in any `design-memory.md` row. Genus + weight + case contrast all doing work. (3-line h1 noted as a fix, not a fail.) |
| 3 | Restrained color system | **PASS** | Nine tokens, frozen verbatim, strictly a subset of Rev 2's (Rev 3 actually *dropped* two off-token hues Rev 2 carried). One accent, used identically. |
| 4 | Hierarchy that breathes | **PASS** | Scale contrast is structural (unequal spans), not decorative. Deliberate whitespace throughout. Two under-filled cells noted as fixes. |
| 5 | Imagery with intent | **PASS** | Both priority slots hold real generated WebP that pass the two-way test; one register; no fabricated branding; remaining slot a labeled placeholder; **2-image cap respected and no new generation this round** (R3-11). |
| 6 | Motion that whispers | **PASS** | Signature move built and verified live; distinct from all of the last 3 `design-memory.md` rows (line-draw ∉ {mask-curtain, clip-wipe, dapple-scrim}; weight-shift ∉ {ink-sweep/underline-draw, lift+tilt}; sticky-progress ∉ {`view()` gallery-hang, hero parallax, pointer field}). Reduced-motion gated; no default trio. |
| 7 | Mobile that's designed, not shrunk | **PASS** | Mobile captures exist on disk for **all four pages** (375×812, 2026-07-29 22:12–22:13), and the layout decisions are real and verified in the DOM, not shrunk. Three tap-target/collision items noted as fixes. |

---

## Gate 6 — Distinctiveness · **VERDICT: genuinely a different site**

**Verified visually with a Rev 2 / Rev 3 first-viewport pair**, both captured at 1440×900 from
live servers (Rev 2 from the snapshot at `scratchpad/rev2-mockup-snapshot/`), plus a Rev 2
mid-page frame covering the same About and Commentary sections.

| | **Rev 2** | **Rev 3** |
|---|---|---|
| First viewport | near-black `--tinta`, 784px dark split-screen hero | porcelain masthead; **the first 1241px of the page is light** |
| Measured dark ground (home) | **50.8%** (784 hero + 551 + 448 bands + 468 footer + 118 header of 4667) | **36.9%** (354 + 476 + 345 bands + 530 footer of 4618) |
| Header | dark `--tinta` bar, logo on a pedra chip, `☎` dingbat | porcelain two-deck masthead, logo directly on porcelain, inline-SVG phone glyph, 2px brass rule closing it |
| Hero archetype | 50/50 vertical split — type left, photo right, equal weight | full-width type masthead; photo demoted to a horizontal mounted band *below* a ruled CTA row |
| Display face | Besley (heavy slab/Clarendon) reversed white | Libre Caslon Text (high-contrast old-style) in near-black |
| Background system | **azulejo monoline lattice visible across every dark ground** | flat porcelain + corner washes + grain; **no pattern at all** — structural hairlines are the only line work |
| Block grammar | bordered, gapped boxes with visible per-card borders | borderless fields sharing one collapsed hairline; white compartments bounded on pedra |
| Section labels | horizontal eyebrow stacked over every h2 | three rotated treatments — ruled header row / rotated vertical side label / bare label+rule |
| Motion vocabulary | clip-wipe + lift/tilt ≤2° + hero parallax | line-draw + weight-shift + sticky-progress; **no lift, no tilt, no parallax** |

**The bold test passes decisively.** A stranger glancing for one second sees a dark site and a
light site. This is a value-structure flip plus a type-genus change plus a retired background
system plus a replaced motion vocabulary — structural change, not a recolor. The specific
"~70% porcelain / ~30% ink" claim in R3-3 measures **63.1% / 36.9%**: directionally correct and a
genuine inversion, but ~7 points heavier on ink than the plan stated. Worth recording, not
worth bouncing.

**Against the last 3 `design-memory.md` rows** (happy-trees-by-mgm, fora-digital,
paul-da-silva-law Rev 2): no shared font pairing, palette family, layout archetype, background
recipe, entrance family or hover personality. Checked for the *softer* sameness too — the
nearest light neighbour is **john-sessa-cpa** (5 rows back: porcelain + ink-navy), and Rev 3
diverges on all four of its recorded columns: Caslon/Albert Sans vs Spectral/Public Sans,
modular ruled ledger vs sidebar-anchored letterhead, no dot grid vs dot-grid graph paper, brass
vs verdigris — plus ink punctuation bands john-sessa never had. Not a sibling of anything
recent.

*(Reading Rev 2's frozen files and screenshots is research, not a reopening. No fix was sent
to any signed prospect.)*

---

## Gate 7 — Interactive click-test · **PASS (both prior automated flags were false positives)**

Four pages × two viewports, driven in a real headless browser.

**Verified working:**
- **Hamburger opens AND closes**, on index and on non-index pages: `display:none` / `aria-expanded="false"` → click → `display:flex` / `"true"` → click → back to `none` / `"false"`. Menu rows **375×53px**, toggle **44×44px**, close icon swaps to ×. Full-width ruled ledger list, not a floating sheet.
- **Form submit shows a real inline demo confirmation.** `.form-result` goes `hidden:true → false`, `display:none → block`, 45px tall, rendering: *"Thanks — this is a demo form. On the live site this reaches Paul Da Silva's office directly. For now, please call 973-344-0808."* Button is **not disabled**, label stays `Send`, text renders `--ink` on white (17.39:1). No silent click, no dead grey button.
- **Nav links, cards, CTAs, footer links, `#fragment` anchors** — 25 / 19 / 13 / 17 elements exercised at 1440 and 23 / 15 / 11 / 15 at 375, **zero dead clicks**.
- Whole practice compartments are the link target (`.cmp` is an `<a>` with `display:block`), so there is no small-inner-link affordance trap.

**Both flags raised by the earlier automated pass are false positives — cleared:**

1. **`practice-areas@375` → `a[href="#real"]` reported "dead, obscured".** It is not. `.rail-list` at mobile is `display:flex; overflow-x:auto` with `scrollWidth 568 > clientWidth 375`, so `04 Real Estate` starts at x=428 — legitimately off-screen in a **deliberately** horizontally-scrollable tab row (plan R3-12). After scrolling the rail to its end the tab sits at x=235, **141×51px**, and `document.elementFromPoint` at its centre resolves **inside the link**. The earlier harness clicked the element's centre coordinate without scrolling the rail first.
2. **`contact` → `.map-frame` reported "misleading affordance".** It is not. Computed: `cursor: auto`, `box-shadow: none`, `transform: none`, no wrapping `<a>`. Nothing about it invites a click; it is a container holding a live OSM iframe (interactive in its own right) plus a captioned "Get directions" link beneath. No hover lift, no pointer cursor, no chevron.

**Non-link compartments that change fill on hover** (the criminal sub-ledger, the recognition blocks) are worth naming but are not a misleading affordance: the change is `#fff → #F0F2F5` — a ~2% value shift — with `cursor` staying `auto`, no lift, no shadow, no chevron, and the rule is `(hover:hover) and (pointer:fine)`-guarded so touch never sees it. Advisory only.

---
## Numbered fixes I would require

The rubric gate and $10K items 1–7 both pass. What holds this half back is the composition-check
clause of the skill's own gate — *"Every composition check above passes, or the Stage 5 brief
explains the exception."* Four fail and the brief does not excuse them. All four are small and
local; none touches palette, copy, content, or the frozen images.

**1. Home h1 renders 3 lines at 1440 — the plan spec'd max 2.**
`index.html` hero h1, `style.css` `--fs-h1` clamp ceiling. Measured: 80px font, 83px line-height,
250px box, 1066px measure. R3-9 index §1 says *"set huge in Caslon across ~10 of 12 columns, max
2 lines"*, and the composition check caps it at 2. **Fixed looks like:** either drop the clamp
ceiling from `5rem` to ≈`4.25rem`, or widen the h1's measure toward the full 10-of-12 columns —
whichever gets *"A Newark defense attorney who speaks your language."* onto two lines at 1440
without shrinking it below the interior-h1 scale. Do not touch the copy; it is frozen.

**2. Practice-compartment go-links don't bottom-align across their row.**
`style.css` `.cmp` / `.cmp .go`. Compartments are already equal height (248px) but the links sit
wherever the copy ends: row 1 `goTop` 1842 vs 1870, row 2 2118 vs 2090 — **28px out in both
rows**. Directly against *"Card CTAs bottom-align across a row, regardless of body length above
them."* **Fixed looks like:** `.cmp{display:flex;flex-direction:column}` +
`.cmp .go{margin-top:auto}`. Two lines, no layout risk.

**3. Family Law's 7 items are a bare `<ul>` with a hairline under every row.**
`practice-areas.html` `#family` `.lineitems`. The density check names this exact shape: *"more
than 5 items needs a real component … not a longer `<ul>` with a hairline under every row."*
**Fixed looks like:** the check's own first suggestion — grouped columns. Two columns of ledger
line items inside the same ruled group (4 + 3), collapsed hairlines kept. Same 7 strings,
verbatim; this is layout only. It also fills the empty right half of that section and breaks up
the page's weakest stretch, where three consecutive groups currently share one grammar. Criminal
already has its 2×2 sub-ledger, so the precedent is in the file.

**4. No skip-to-content link on any page.**
`grep -i skip` across all four pages and `style.css` → 0 hits; the first focusable element is
`a.brand`. This is the composition checks' *"Present or it isn't finished"* item. **Fixed looks
like:** a visually-hidden-until-focused `<a class="skip" href="#main">Skip to content</a>` as the
first child of `<body>`, and `id="main"` on `<main>`, on all four pages. Style it in the direction
(square, `--ouro` fill, `--ink` label) so it looks deliberate when it appears.

### Fixes I would ask for but would not gate on

**5. `.grp-head .num` measures 2.90:1 against a 3:1 large-text floor.** One line:
`.grp-head .num{color:var(--ouro-escuro)}` → 5.17:1. Also matches R3-9's own practice-areas spec.
Consequential benefit: nothing.

**6. Mobile hero CTA overlaps the fixed call bar by 3px at scroll 0.** At 375×812 the hero's brass
`Call 973-344-0808` button spans y 702–758 and the fixed `.mobile-call` bar starts at y 755 — two
identical brass slabs touching at first paint, which reads as one doubled button rather than two
CTAs. `body{padding-bottom:56px}` correctly clears the bar at the page *bottom*; this is the hero
specifically. **Fixed looks like:** add the bar's height to the hero ruled row's bottom margin at
mobile so the two never coincide. (Three tap-to-call affordances in the first screen is planned
and defensible for a criminal-defence office — the issue is the collision, not the repetition.)

**7. Four standalone `.text-link` CTAs are 28px tall on touch.** *Send a message →*, *Meet Paul Da
Silva →*, *Read the full bio →*, *Send a message instead →*. These are standalone calls to action
on their own line, not inline-in-paragraph links, and R3-12 claims *"All tap targets ≥44px"* —
which is true of the buttons, menu rows (53px) and toggle (44×44) but not of these. **Fixed looks
like:** vertical padding to 44px minimum at `(pointer:coarse)`. The logo link at 38px is the same
family of miss, lower stakes.

**8. Two compartments end in a large blank.** ~220px of empty white below `Send` in the contact
form compartment, and ~170px below the bio copy. Both are the ledger grammar equalizing a row's
cell heights, which is internally consistent — a shared-rule table *does* leave the shorter cell
slack — so this is a judgment call, not a rule break. If it's worth a touch, letting the contact
textarea grow into its slack is the cheapest version.

**9. Recognition h3 wraps to 4 lines in the 3-col cell.** *"Hudson County Ethics Committee"* at
the 3-of-12 span reads cramped and pushes that cell's body off the row's shared Y origin.
`text-wrap:balance` on `.cmp h3`, or nudge the spans to 5/4/3 → 4/4/4 for that row only.

### Observations for the lead, not fixes

- **Dev scratch is sitting in `mockup/`:** `_cap.html`, `_frame.html`, `_measure.js` (353 KB),
  `_m_*.html` ×4, `_n_*.html` ×3, `_q.html`, `_r.html`. These are earlier critics' capture
  harnesses, not builder output. `pipeline/package-site.sh` strips dev scratch, so the zip is
  unaffected — but they should be deleted before the repo is committed. I left them alone rather
  than delete files inside a prospect's mockup directory.
- **R3-3's "~70% porcelain / ~30% ink" measures 63.1% / 36.9%.** A real inversion from Rev 2's
  50.8% dark, but ~7 points heavier on ink than the plan claims. Worth correcting in the plan text
  or the `design-memory.md` row rather than changing the build.
- **The three review quotes render 4 lines each** against a ≤3-line check. Not actionable — they
  are verbatim protected reviews and shortening one is forbidden. If it ever matters, the fix is
  two wider columns, not edited quotes.

---

## Summary of this half

| Gate | Result |
|---|---|
| 1. Live JS-off reload | **PASS** — `.js` stripped by the dead-man timer on all 4 pages; 0.00% real hidden text; all CTAs full-size |
| 2. Countable composition checks | **4 FAIL unexcused** (3-line h1, card-CTA alignment, 7-item list, skip link); 4 exceptions accepted with the brief cited |
| 3. 10-dimension rubric | **PASS** — 8 / 9 / 9 / 9 / 8 / 8 / 8 / 8 / 9 / 9. Boldness **8** ≥ 8, lowest **8** ≥ 7 |
| 4. $10K items 1–7 | **7 / 7 PASS** |
| 5. Measured WCAG AA contrast | **PASS** — one 0.10-short decorative numeral, advisory |
| 6. Distinctiveness / bold test | **PASS** — genuinely a different site, not Rev 2 in a new font |
| 7. Interactive click-test | **PASS** — zero dead clicks; both earlier automated flags were false positives |

**Verdict for the browser half: NEEDS-WORK on one gate only — the composition checks.** Four
concrete, local fixes (items 1–4 above), none of which touches the frozen palette, copy, content
or images. Everything else in my scope passes, and the round's sharpest question — whether Rev 3
is a real redesign — resolves clearly in the build's favour.

*Verdict on the package and the `design-memory.md` row are the lead's; not decided here.*
