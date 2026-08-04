# Website Plan — Gee-Kay Landscaping, Inc. (Rev 2 — full rebuild)

**Slug:** `gee-kay-landscaping` · **Date:** 2026-08-02 · **Supersedes:** Rev 1 ("Heritage Ledger", 2026-07-19)

**Input of record.** There is no `client-answers.md` for this prospect. The lead approved
building from `dossier.md` plus Rev 1 of this plan as the client's requirements. Every
factual claim below traces to `dossier.md`. Anything not in it is a **labeled visible
placeholder**, never a plausible-looking value.

**Zero-spend run.** No images and no video are generated. All eight AI-IMAGE slots carry
over from Rev 1 as labeled placeholder blocks with their original subjects and labels.
**No slot is marked GENERATE.** The imagery **register** is declared anyway (below) so the
placeholders are art-directed and so whoever fills them later has the brief.

**Why Rev 1 is being replaced rather than patched.** Three defects, all structural:

1. **27 WCAG contrast failures**, worst `#31502f` on `#a8763e` at 2.3:1 — the palette
   itself was the bug, so a repaint of components wouldn't have fixed it.
2. **Two fabricated-adjacent placeholders shipped as visible page text** — a bracketed
   owner's note attributed to George Reinhardt (we have no statement from him) and an
   `[Insured — confirm]` chip (we have no insurance confirmation). Both are removed
   outright, not restyled.
3. A display face that is now on the banned list, so its `overused-font` finding blocks.

---

## 1. Design Read (taste-skill §0)

**Reading this as:** a 45-year Livingston landscape *construction* firm that has no
website at all, so this page is the first impression it has ever controlled — the job is
to make measured, permanent-feeling work legible to a homeowner on a phone in about eight
seconds, and to get them to tap the phone number.

Unpacked, the three things that read out of that:

- **The differentiator is that they build, not just mow.** "Design and installation of
  new, and upgrading of existing Landscapes and Hardscapes" is construction work. Every
  landscaper site in Essex County looks like a mowing service. This one should look like
  a firm that draws a plan before it digs.
- **45 years is the whole pitch, and it needs no nostalgia to land.** 1981 stated plainly
  beats any amount of heritage styling. Rev 1 spent its entire art direction on the
  heritage feeling and had nothing left for the construction claim.
- **The visitor is skeptical and in a hurry.** Every visible sentence competes with a
  Google results page. Specification, not atmosphere.

### Anti-Default Discipline (taste §0.D)

Defaults refused, with what replaced them:

| Default for this brief | Refused because | Instead |
|---|---|---|
| Warm earth tones + big serif = "landscaper" | Four of the crew's last builds are in that lane; it's the category default, not a decision | Cool plan-paper ground; the green is a *spruce* used as ink, not as a mood |
| Golden-hour photo hero with a scrim | Not available at zero spend, and it's the shape every trade site takes | Type-led hero; the image plate is a supporting column, not the ground |
| Heritage/ledger dressing to sell "since 1981" | Rev 1 did exactly this and the date still didn't read | The date is set as a measurement, at scale, in the trust strip |
| Three icon-heading-paragraph cards for the services | The card wall | Card grid for the overview only; each service gets a *different* format on the Services page |

### AI Tells checked (taste §9)

Purple/indigo gradient: absent. Glassmorphism: absent. Icon-tile stack: absent. Eyebrow
over every section: budgeted at 4 of 18 (see §5). Section numbering: used once, on the
`steps` family only, where the order carries information. Gradient text: absent. Card
wall: one card grid on one page.

---

## 2. Three divergent directions (Stage 5)

Forced apart on ground, type register, and layout archetype — not three colorways of one idea.

### Direction A — "Property Line" ✅ CHOSEN

The site as a **site plan**. Cool plan-paper ground carrying a faint surveyor's tick
field; spruce green used as drafting ink rather than as scenery; a single surveyor's-flag
orange for the one thing you're meant to do. Layout is a **measured register**: a visible
7/5 dominant column, hairline datum rules that run to the page edge, and headings that sit
on the rule like a callout. Big numerals (1981, 45, 5.0, 3) are set as *measurements* — the
scale jump between them and body copy is the page's loudest move.

Why it wins: it is the only one of the three that says *construction* rather than
*grounds-keeping*, which is the actual differentiator in the dossier. It is also the
furthest from every landscaper the crew has already built (all four sit in warm-earth or
dark-evergreen). And it degrades well at zero spend — a type-and-rule system does not need
photographs to look finished, which is exactly the constraint this run is under.

### Direction B — "Route Book" ❌

The maintenance calendar as the spine: a twelve-month scroll, warm cream, terracotta
accents, month cards as the primary navigation. Rejected — warm cream + a serif +
month-cards is one degree from Rev 1's retired parchment ledger, and it foregrounds
recurring maintenance, which is the *commodity* half of the business.

### Direction C — "Night Yard" ❌

Dark ground, landscape-uplighting palette, full-bleed imagery, minimal type. Rejected on
two counts: `anthonys-landscaping` already occupies dark-evergreen in `design-memory.md`,
and a dark imagery-led direction is the worst possible fit for a build with **zero real
images** — it would ship as eight dark rectangles.

---

## 3. Typography

Google Fonts, two families, `display=swap`. Neither is on the banned set, and neither
appears in the last three `design-memory.md` rows (Zilla Slab/Work Sans · a serif
display/Hanken Grotesk · Libre Caslon Text/Albert Sans).

- **Display — Newsreader** (variable `wght` 400–700, `opsz` axis). An editorial
  news-serif with a small optical-size axis, so headlines set tight and dense rather than
  decorative. Used **roman only, never italic at display size** — an oversized italic
  serif hero is its own detector rule and is not the register here.
- **Body / UI — Familjen Grotesk** (variable `wght` 400–700). A Swedish grotesque with
  enough quirk in the `a`, `g` and `y` to not read as system sans, and a real variable
  weight axis for the hover personality.

Scale (Builder implements as tokens — every step ≥ 1.25× its neighbour, so
`flat-type-hierarchy` cannot fire):

| Step | Size |
|---|---|
| `--fs-mega` (measurement numerals) | `clamp(3.5rem, 8vw, 7rem)` |
| `--fs-h1` | `clamp(2.6rem, 6.2vw, 4.6rem)` |
| `--fs-h2` | `clamp(1.85rem, 3.6vw, 2.6rem)` |
| `--fs-h3` | `1.35rem` |
| `--fs-body` | `1.0625rem` / 1.62 |
| `--fs-label` | `0.8125rem`, tracking `0.1em`, uppercase |

Body measure capped at 68ch. Tracking floor `-0.02em` on display, never below.

---

## 4. Color system — "plan paper"

Five tokens plus two documented tints. Every pair below was computed before a line was
written; **nothing on this site sits under 4.5:1**, hover states included.

| Token | Hex | Role |
|---|---|---|
| `--paper` | `#E9EBE4` | Page ground — a cool grey-green plan paper, deliberately *not* cream |
| `--chalk` | `#FBFCF9` | Raised surfaces, form fields, card grounds |
| `--graphite` | `#1E241F` | All body text, footer ground |
| `--spruce` | `#234A33` | Headings, primary CTA fill, inverted bands |
| `--flag` | `#A83F1E` | The single accent: rule marks, the one primary action, link underlines |

Documented tints (derived, not new hues): `--graphite-dim #4A5449` (secondary text on
light) and `--paper-dim #B9C6B4` (secondary text on spruce/graphite).

Verified contrast ratios:

| Pair | Ratio | Use |
|---|---|---|
| `--graphite` on `--paper` | 13.2:1 | body |
| `--graphite` on `--chalk` | 15.6:1 | body on cards |
| `--spruce` on `--paper` | 8.3:1 | headings |
| `--flag` on `--paper` | 5.2:1 | accent text, links |
| `--flag` on `--chalk` | 6.0:1 | accent text on cards |
| `--chalk` on `--flag` | 6.0:1 | primary CTA at rest |
| `--chalk` on `--spruce` | 9.7:1 | CTA hover, inverted bands |
| `--paper` on `--graphite` | 13.2:1 | footer |
| `--graphite-dim` on `--paper` | 6.6:1 | secondary text |
| `--paper-dim` on `--spruce` | 5.6:1 | secondary text, inverted |

Rule that makes this hold: **`--flag` and `--spruce` are never set against each other** —
that pair was Rev 1's 2.3:1 failure. `--flag` only ever meets `--paper`, `--chalk`, or
carries `--chalk` on top of it. The CTA's hover swaps flag→spruce, and 6.0:1 → 9.7:1 both pass.

**Background system:** *plan-paper* — a tiling SVG surveyor's tick field (data-URI, 96px
grid, low alpha) + a `feTurbulence` grain overlay + one soft spruce radial wash behind the
hero column. Three layers, no flat rectangle, no mesh, no orb, no dot-grid (reserved to
`john-sessa-cpa`), no contours (reserved to `cecere-brothers`).

---

## 5. Page map — 3 real HTML files, 18 sections

Rev 1 was a single-file SPA with JS page-toggling. Rev 2 ships **three real pages**
(`index.html`, `services.html`, `contact.html`) — each with its own `<title>`, meta
description, canonical, and **exactly one `<h1>`**. Nav is plain `<a href>`; nothing about
navigation depends on JavaScript.

Every section below carries its `format:` and `opener:` tokens from `section-formats.md`.

### `index.html` — Home

1. **Hero** — format: hero, opener: kicker+h2 — 7/5 dominant column. Left: locality
   kicker, h1, one-sentence subhead, two CTAs. Right: the hero image plate, breaking the
   container's right edge. Four text elements exactly.
2. **Trust strip** — format: stat-strip, opener: none — three measurement numerals on
   hairline datum rules: `1981` / `45` / `5.0`.
3. **Services overview** — format: card-grid, opener: bare-h2 — three cards, three cells,
   each with an image plate. The only card grid on the site.
4. **Service area** — format: full-bleed-band, opener: in-media — spruce band, heading set
   inside it, over the tree-lined-street image plate. Confirmed towns + the labeled
   unconfirmed list (§9).
5. **How a job runs** — format: steps, opener: numeral — four numbered steps (walk the
   property → plan and price → build → maintain). The only place numerals label sections.
6. **Who you're hiring** — format: editorial-column, opener: bare-h2 — one narrow measure
   of real prose. **No owner quote, no pull-quote slot.**
7. **What customers say** — format: quote-monolith, opener: none — the two real captured
   quotes, each attributed to its platform.
8. **Estimate CTA** — format: cta-band, opener: side-label — phone + the 4-field estimate form link.

### `services.html` — Services

9. **Page header** — format: hero, opener: bare-h2 — h1 + the client's own one-line
   description of the three lines.
10. **Lawn & grounds maintenance** — format: split, opener: side-label — image plate left,
    copy right.
11. **Landscape design & installation** — format: bento, opener: in-media — a four-cell
    mosaic: the before/after image plate (2 cells wide), a spruce-ground stat cell, a text
    cell, a materials list cell. Two cells carry real visual weight.
12. **Hardscapes** — format: split, opener: bare-h2 — copy left, image plate right
    (mirrored from §10, and not adjacent to it).
13. **Mini CTA** — format: cta-band, opener: none — shorter than Home's.

### `contact.html` — About & Contact

14. **Page header** — format: hero, opener: bare-h2 — h1 "A Livingston family business."
15. **Story** — format: editorial-column, opener: side-label — three short paragraphs,
    every sentence traceable to `dossier.md`.
16. **Credentials** — format: stat-strip, opener: none — three items: family-owned since
    1981 · licensed NJ Home Improvement Contractor · 5.0 on Angi. **Nothing about insurance.**
17. **Contact** — format: split, opener: bare-h2 — left: phone, address, hours placeholder;
    right: the estimate form (4 fields).
18. **Map** — format: full-bleed-band, opener: in-media — labeled embed placeholder.

### Quota check (run `plan-lint.mjs`; counted here too)

- Sections: **18**. Distinct families: **10** (hero, stat-strip, card-grid,
  full-bleed-band, steps, editorial-column, quote-monolith, cta-band, split, bento) — need ≥ 4. ✅
- No family twice consecutively. ✅
- Kicker-style openers (`kicker+h2` + `side-label`): **4** — §1, §8, §10, §15. Budget
  `ceil(18/3)` = **6**. ✅
- No two adjacent sections share an opener. ✅
- Most-used opener signature: `bare-h2`, **6 of 18 (33%)** — ceiling is 50%. ✅

---

## 6. Composition device

**One device, named: the dominant column — a 7/5 split (58% / 42%), never 50/50 — carried
by the Hero (§1),** where the type column is the wide one and the image plate deliberately
breaks the container's right edge by 4vw rather than aligning to it. It repeats as
structure (not as decoration) in §17's contact split.

Supporting scale jump, in the same first two sections: the trust strip's `1981` numeral at
`clamp(3.5rem, 8vw, 7rem)` against its `0.8125rem` label is an **8.6× jump** at desktop,
well past the ≥3× bar.

---

## 7. Signature motion

Tokens: **entrance = slide-alternate · hover = rule-trace edge-lift · set-piece =
hero-exit · tempo = `cubic-bezier(.2,.75,.25,1)` at 620ms.**

- **Entrance — slide-alternate.** Rows enter from alternating sides (`translateX ∓48px`
  desktop / `∓20px` mobile), 620ms, 70ms `--i` stagger, cap 8 items. **Transform only, no
  opacity** — the slide runs from an already-visible default (`craft-floor.md`), so no
  character on the page is ever invisible at rest. Measured: 0% hidden text on all three
  pages, versus the ≤15% the gate allows.
- **Hover — rule-trace edge-lift.** A hairline travels the perimeter of a card or plate
  while it lifts 4px on a directional shadow. Two scaling pseudo-elements, pure CSS, and
  it is the drafting register the direction is built on. Guarded by
  `(hover:hover) and (pointer:fine)`.
- **Set-piece (one, and only one) — hero-exit.** As the hero scrolls away its content
  lifts and fades and the header collapses to its compact solid state. No parallax, no
  scroll-jacking, no sticky rail.
- **Ambient: zero animated systems.** The tick field and grain are static.
- **Deliberately NOT:** fade-up, count-up, custom cursor, magnetic buttons, card tilt —
  which is the entire Rev 1 motion set, and three of those are the flagged default trio.
- **GSAP tier 0.** A CSS entrance plus a CSS hover needs no library; nothing is vendored.
- **Fail-visible.** Every hidden state is scoped to `html.js` inside
  `@media (prefers-reduced-motion: no-preference)`, with the head-script + error-listener +
  2s-timeout net from `motion.md`. With JS off, nothing is hidden.

Divergence check against the last three `design-memory.md` rows: `happy-trees` (unrecorded),
`fora-digital` (mask-curtain + ink-sweep + gallery-hang + reactive canvas), `paul-da-silva-law`
(rules-draw-in + weight-shift + sticky progress rail). No overlap on entrance, hover, or set-piece.

---

## 8. Imagery — register declared, **nothing generated**

**Register: proud-contractor**, one register across all eight slots. That is the register
whoever fills these later must shoot or generate to — the bar is the best photo on their
Google Business profile: flawless finished work at an attractive property, pleasant natural
light, casual but flattering. No readable business names or signage in any frame.

**This run generates zero images and zero video.** No slot is marked `GENERATE`. All eight
ship as labeled `.img-placeholder` blocks styled in the direction's colors — a chalk ground,
a spruce hairline, a flag corner tick, and the label set in the UI face — so the page reads
as finished at zero cost. Subjects and labels are carried over verbatim from the Rev 1
build.

| # | Slot | Section | Label (verbatim from Rev 1) |
|---|---|---|---|
| 1 | Home hero plate | §1 | AI-IMAGE — Livingston front lawn, golden hour |
| 2 | Services card | §3 | AI-IMAGE — lawn edging |
| 3 | Services card | §3 | AI-IMAGE — new plantings |
| 4 | Services card | §3 | AI-IMAGE — paver walkway |
| 5 | Service-area band | §4 | AI-IMAGE — truck & trailer, tree-lined street |
| 6 | Maintenance split | §10 | AI-IMAGE — striped lawn, overhead |
| 7 | Design & install bento | §11 | AI-IMAGE — design & install, before/after |
| 8 | Hardscape split | §12 | AI-IMAGE — paver patio & sitting wall, dusk |

Plus one non-AI embed placeholder: the map block in §18.

**No video slot is marked, and none is requested.** The Builder ships no clip; nothing goes
to Harry for approval, and no spend is authorized by this plan.

---

## 9. Local-trade conversion pattern (`local-trade.md`)

| Requirement | Where it lands |
|---|---|
| Tap-to-call in the mobile header | `tel:+19739926687` call button, always visible in the header at ≤ 820px, and in the desktop nav |
| One primary action | **"Get an estimate."** One label, used in the nav button, the hero, both CTA bands and the form submit. The repeated tap-to-call is the sanctioned exception. |
| Service-area block, real towns | §4 — see the honesty note below |
| Trust strip | §2 (1981 / 45 years / 5.0 on Angi) and §16 (family-owned · licensed NJ HIC · 5.0) |
| Project gallery | The image plates in §3, §10, §11, §12 are the gallery slots; the §11 bento cell is the before/after |
| Estimate form ≤ 4 fields | §17 — Name · Phone · Town · What do you need done? Submit is a styled placeholder that shows an inline demo confirmation, never a dead or disabled click. |
| Consistent NAP footer | Footer NAP matches the `LandscapingBusiness` JSON-LD character for character |

**Service-area honesty note (a real judgment call, recorded).** The dossier confirms
exactly one town — Livingston — and lists Roseland, West Orange, Millburn/Short Hills and
Florham Park as *likely, unconfirmed*. Local-trade wants real town names on the page; the
content-honesty rule forbids presenting a guess as fact. Resolution: §4 states the
confirmed line in full-size copy ("Livingston, New Jersey, and the surrounding Essex County
towns"), and the four likely towns appear **below it in a visibly labeled
`CONFIRM BEFORE LAUNCH` block**, styled as a placeholder, not as page copy. The JSON-LD
`areaServed` carries Livingston plus `PLACEHOLDER_TOWN_2…5` tokens. Harry confirms the list
on the first call and the block becomes real copy.

## 10. Content honesty — what this build may and may not say

**May say** (all `dossier.md`-backed): founded 1981 · 45 years · the Reinhardt family ·
Livingston natives · George Reinhardt is the owner · (973) 992-6687 · 73 N Livingston Ave,
Livingston, NJ 07039 · lawn maintenance, landscape design and installation, hardscapes and
upgrades to existing ones · "Servicing Livingston and surrounding areas" · 5.0 on Angi ·
Licensed NJ Home Improvement Contractor · the two verbatim review quotes with their platforms.

**May not say, in any form including a bracketed placeholder:**

- **Any quote or statement attributed to George Reinhardt.** No source exists. Rev 1
  shipped `[placeholder: owner's note]` as visible text; §6 of this plan has no quote slot
  at all, so there is nothing to fill in wrong.
- **Insured / bonded.** No source exists. Rev 1 shipped an `[Insured — confirm]` chip as
  visible text; §16 carries three credentials and insurance is not one of them.
- A license number, an email address, review counts, staff names or crew size, invented
  hours, or a specific founding month.

**Visible placeholders that are correct and intended:** the hours line
(`PLACEHOLDER_HOURS — confirm with George`), the four unconfirmed towns block, the map
embed, and the eight AI-IMAGE plates. These are labeled as placeholders and read as
build-in-progress, which is honest; a plausible invented value would not be.

## 11. SEO / head

`LandscapingBusiness` JSON-LD on every page with the real NAP; `PLACEHOLDER_` tokens for
domain, hours, geo (dropped rather than guessed) and the unconfirmed towns. Per-page
`<title>` in the `<Service> in <Town>, <ST> | <Business>` shape, meta description naming
the service and Livingston, OG + Twitter tags, canonical, `lang="en"`, inline SVG favicon,
and a skip-to-content link as the first focusable element. Footer privacy/terms links present.
