# Audit — Fora Digital (our own agency site)

**Review round: 1**
**Auditor:** Critic (Essex Web Crew)
**Date:** 2026-07-23
**Artifact:** `prospects/fora-digital/mockup/` (index.html · style.css · main.js · assets/)
**Verified against:** `client-answers.md` (top authority) → `website-plan.md` (design contract) → `CLAUDE.md`
**Method:** code read + served over `http://localhost:5610` in the browser pane; desktop (1440 / 1280) and
375×812 inspected section-by-section using the hide-sections capture technique; contrast computed
numerically; every link enumerated and resolved; no-JS state reproduced by stripping `.in`.

## VERDICT — **NEEDS-WORK** (round 1)

- **$10K Checklist: 6 / 8** (items 7 and 8 fail) → below the 8/8 gate.
- **web-design-ultra rubric: PASSES the gate** — no dimension below 7, boldness 9.
- **Content honesty: CLEAN — full pass, no findings.**

This is a genuinely strong piece of design and the honesty audit — the part that mattered most on
this build — is spotless. It fails round 1 on three concrete, surgical defects, none of which
requires touching the art direction. Fix list in §4.

---

## 1. The $10K Checklist

| # | Item | Score | Justification |
|---|---|---|---|
| 1 | Point of view, not a template | **PASS** | "Main Street Modern" is committed to end-to-end: warm linen wall, poster-scale serif, portfolio hung as framed browser plates, registration cross-marks in the hero mat. Deliberately breaks the dark/tech-slick agency uniform, with cobalt kept as the category trust cue — the honor/break call is made explicitly in the plan and executed faithfully. |
| 2 | Typography that does work | **PASS** | Instrument Serif (display) / Hanken Grotesk (body), loaded with `display=swap` + preconnect. Verified computed: `"Instrument Serif", Georgia…` on h1, `"Hanken Grotesk", "Segoe UI"…` on body. No Inter/Roboto/Arial/Helvetica anywhere, including fallback stacks. Real scale contrast (116px H1 vs 17px body), tight display leading, tracked uppercase kickers, italic + clay emphasis on "local". |
| 3 | Restrained color system | **PASS** | Four working colors (paper / ink / cobalt / clay) + two support tokens (surface, line, stone) — all in `:root`, no hardcoded hex in components. Cobalt is disciplined to interactive + badge + wordmark mark; clay appears exactly once (hero `em`). |
| 4 | Hierarchy that breathes | **PASS** | Unambiguous eye path in every section: kicker → H2 → lead → content. Portfolio badge reads before the title, which is the right priority for the honesty story. Generous `--space-section` rhythm. (Minor spacing criticism under rubric dim 5 — not a checklist failure.) |
| 5 | Imagery with intent | **PASS — documented exception** | Client answers set the image budget to **ZERO**; the plan carries **0 `GENERATE` slots**. The two priority slots hold **real screenshots** of actual work (`cecere-brothers.webp` 72 KB, `corey-blakes-steakhouse.webp` 132 KB), full-frame, no crop, `width`/`height` set, `loading="lazy"`, WebP, local. **Zero AI-generated images on the page — confirmed.** This is a stronger outcome than generated imagery would have been: real work is the whole pitch. Remaining slots are honest CSS plates. No stock, no hotlinks (only external refs are Google Fonts + the canonical/OG absolute URLs). |
| 6 | Motion that whispers | **PASS** | Signature is real and non-default: **mask-curtain** entrance (cobalt panel scaleX off, 90 ms `--i` stagger), **ink-sweep** hover family (underline-draw on links, fill-sweep on buttons, 150 ms icon-nudge), one scroll set-piece — **gallery-hang** via `@supports (animation-timeline: view())` with clean static fallback. Two capped continuous loops (marquee 32 s, asterisk 40 s). **No fade-up, no count-up** — grepped and confirmed. All hover behind `(hover:hover) and (pointer:fine)`; `prefers-reduced-motion` kill switch present and correct. *(The curtain's no-JS behaviour is charged to item 8, not here.)* |
| 7 | Mobile designed, not shrunk | **FAIL** | The mobile *design* is genuinely done — verified myself at 375×812: nav collapses to wordmark + compact CTA, hero min-height released so nothing crops, headline holds 3 lines at 54.4 px, CTA goes full-width, plates stack with captions below the frames, coming-soon plates go 1-up under 560 px, monogram frames shrink 150→120 px, section padding drops. `document.body.scrollWidth === 375` — **no horizontal overflow**. It fails on one measured requirement: **8 tap targets under 44 px** (see fix #2). The plan's §11 explicitly demanded "≥44px tap targets"; the build didn't implement it. |
| 8 | The invisible expensive stuff | **FAIL** | Almost all green: 240 KB total, sub-2s ✓ · `lang="en"` ✓ · exactly one `<h1>` ✓ · clean heading order (h1→h2→h3, no skips) ✓ · `header`/`nav`/`main`/`section`×4/`footer` ✓ · both images have descriptive alt ✓ · 7 decorative elements `aria-hidden` ✓ · global `:focus-visible` cobalt ring ✓ · title, description, canonical, OG ×5, Twitter card, inline-SVG favicon ✓ · **JSON-LD parses valid** and correctly **omits `telephone`, `address`, `geo`, `areaServed`** — omitting is right, faking would have been an automatic fail ✓ · **WCAG AA: every pair passes** (measured — table in §3). It fails on one thing: **with JavaScript unavailable the entire page renders as solid cobalt blocks** (see fix #1). |

**Score: 6 / 8.** Gate requires 8/8.

## 2. web-design-ultra 10-dimension rubric

| # | Dimension | Score | Note |
|---|---|---|---|
| 1 | **Boldness / distinctiveness** | **9** | 116 px Instrument Serif poster headline on warm linen, in a category that is uniformly near-black — the break itself is the bold move. Gallery-wall framing, registration marks, marquee band. Would not be mistaken for a template or for any of the last 3 crew builds. |
| 2 | Visual hierarchy | 8 | Eye lands exactly where intended in every section. Half a point off for the 32ch section heads leaving a wide empty right column three times running. |
| 3 | Typography craft | 9 | Distinctive pairing, strong size/weight contrast, tight display rhythm, purposeful italic. |
| 4 | Color & contrast | 9 | Confident, restrained, and *measured* — see §3. Clay correctly quarantined to display size only. |
| 5 | Spacing rhythm | 7 | Token scale is consistent and generous. Deduction: a ~230 px void between the Work section head and plate 1 reads as a dropout rather than a decision, and the repeated empty right-hand column at each section head verges on unintentional. |
| 6 | Background / depth | 8 | Linen grain (3% multiply), hero mat + cobalt registration crosses, warm radial wash behind the headline, cool wash behind Contact, surface/paper/ink section shifts, plate shadows. Not a flat rectangle. The "no fog/god-rays" call is argued in the plan and correct for a paper-and-daylight direction. |
| 7 | Imagery quality | 9 | Two real, well-optimised WebP screenshots in browser-chrome frames. Both are dark heroes and they pop hard against the linen exactly as the plan predicted. No AI imagery, no stock feel. |
| 8 | Responsiveness | 7 | Real phone-layout decisions, zero overflow at 375. Held to 7 by the sub-44 px tap targets. |
| 9 | Motion polish | 7 | The signature is genuine and correctly gated, and it avoids the flagged default trio. Held to 7 by: the curtain having no non-JS fallback (a motion system that can leave content invisible is a motion-system defect), plus two specced flourishes missing and a dead `transition:object-position` left in the CSS. |
| 10 | Cohesion | 9 | One art director throughout — the framing motif recurs in plates, monogram arches and the hero mat; cobalt never leaks off interactive elements; serif/sans roles never break. |

**Gate: no dimension below 7 ✓ · boldness 9 ≥ 8 ✓ → the rubric gate PASSES.**
(Bold test N/A — new build, not a redesign.)

## 3. Verified technical evidence

**Contrast (computed, WCAG 2.x):**

| Pair | Ratio | Verdict |
|---|---|---|
| ink `#1B1813` on paper `#F5F1E8` | 15.7 : 1 | AAA |
| ink on surface `#FDFBF5` | 17.1 : 1 | AAA |
| stone `#6E675C` on paper | 4.96 : 1 | AA ✓ |
| stone on surface | 5.40 : 1 | AA ✓ |
| cobalt `#2447C2` on paper | 6.76 : 1 | AA ✓ |
| white on cobalt (buttons/badge) | 7.62 : 1 | AAA |
| white on cobalt-deep (hover) | 10.09 : 1 | AAA |
| footer `#B9B1A4` on ink | 8.33 : 1 | AAA |
| footer link `#A9BAF5` on ink | 9.29 : 1 | AAA |
| footer kicker `#8C857A` on ink | 4.85 : 1 | AA ✓ |
| clay `#B4552D` on paper | 4.35 : 1 | **AA-large only — correctly used only at 54–116 px** ✓ |

**Click-test — all 16 links enumerated and resolved. Zero dead clicks.**
`#top` `#work` ×3 `#founders` ×3 `#contact` ×3 all resolve to existing IDs; 6 × `mailto:` correct and
case-exact to the client answers (`hfoodim@` / `CRapkin@`). Contact cards are whole-card `<a>` elements —
the entire card works, not an inner link. Zero `<form>`/`<button>`/`<input>` on the page, so there is no
dead-submit placeholder to fail on (correct — the client asked for emails only). Zero console messages.
One misleading affordance found — fix #3.

**Local-trade adaptation — all deviations documented and defensible:** no `tel:` / service-area /
trust strip / estimate form / NAP because **the client stated none exist and said not to invent them**.
One plain primary action ("email us") is repeated in header, hero, contact and footer. Footer contact
block matches the JSON-LD exactly.

**Anti-repetition:** clean against the last 3 crew rows. Instrument Serif / Hanken Grotesk unused
before; warm-linen + cobalt + clay is a different palette family from porcelain/ink-navy
(john-sessa-cpa), graphite/steel/red (cedar-grove-transmission) and bark/moss/lime (happy-trees);
gallery-wall one-pager differs from sidebar-letterhead, spec-sheet bento and canopy full-bleed;
grain + frame-linework differs from dot-grid, schematic linework and dapple. Motion is mask-curtain,
not the fade-up that Cecere used. Also avoids the older Fraunces/Marcellus/Bricolage rows.
*(Run-level three-way distinctiveness check: N/A — single-prospect run.)*

## 4. Content-honesty verdict — **CLEAN, no findings**

This was the load-bearing audit and the build passes it without a single exception.

- **Bios contain only client-supplied facts.** Harry: co-owner · sophomore at The Ohio State
  University studying accounting · West Essex High School graduate · sports, gym, family and friends.
  Corey: co-owner · sophomore at the University of Georgia studying accounting. Word-for-word
  traceable to `client-answers.md`. **No invented experience, no credentials, no specialties, and
  critically no role division** — the site never claims "Harry designs, Corey handles clients."
- **Corey's shorter bio was not padded.** The layout absorbs the asymmetry exactly as the plan
  instructed. A short honest bio was left short. This is the right call and the build made it.
- **Portfolio labels present and unsoftened.** Cecere = **"Real client work"** (cobalt fill chip) —
  verified on screen. Steakhouse = **"Concept build"** (outline chip, deliberately different weight)
  **plus** the explicit caption sentence *"Not a client; a demonstration."* — verified on screen.
  Neither is hedged, shrunk, or buried.
- **Zero fabrications.** Grepped and eyeballed: no testimonials, no reviews, no star ratings, no
  client counts, no "50+ projects", no years-in-business, no awards, no logo wall, no stats row, no
  count-up. The honesty line *"one real client, one concept build, and room we intend to fill"* does
  the trust work instead — and it is the strongest sentence on the page.
- **No location claim anywhere.** No town, county, or state for the agency — correct, none was
  supplied. (The only "Essex" on the page is *West Essex High School*, a client-supplied fact.)
- **Coming-soon plates invent nothing** — no fake client name, no fake logo, no fake screenshot.
  Pure CSS, labelled "Next project — in progress".
- **Headshots are monogram frames** with a "Photo coming soon" caption. **No AI-generated faces of
  real people.** No AI-generated images of any kind on the page.
- **JSON-LD omits phone and address entirely** rather than faking or placeholder-ing them — the
  correct choice, and the one that would have been an automatic fail if done the other way.

## 5. Fix list — ranked by severity

### 1. [HIGH] The page renders as solid cobalt blocks if JavaScript doesn't run
**What fails:** item 8 (invisible expensive stuff), rubric dim 9.
**Evidence:** `.reveal::after` defaults to `transform:scaleX(1)` — an opaque cobalt panel covering the
element — and *only* `main.js` adding `.in` removes it. I reproduced the no-JS state by stripping the
`.in` classes: the hero kicker, all three headline lines, the lead, the CTA row, every section head,
all four plates, both founder cards and both contact cards render as solid blue rectangles. The entire
page content disappears. The `setTimeout(openAll, 2000)` safety net does not help, because it is
itself JavaScript. This matters concretely: this site ships as a zip that Corey drags onto Netlify
Drop — if `main.js` is missing from the package, 404s, or throws, the homepage is blue boxes.
**What "fixed" looks like:** invert the default so the curtain is opt-in, not opt-out. Either
add to `<head>`:
```html
<noscript><style>.reveal::after{display:none}</style></noscript>
```
or (preferred, also covers a JS *error*) have `main.js` set `document.documentElement.classList.add('js')`
as its first statement and scope the curtain to `.js .reveal::after`. Re-verify by loading the page
with JS disabled — all copy must be readable.

### 2. [MED] Eight tap targets are below the 44 px the plan required
**What fails:** item 7 (mobile designed, not shrunk), rubric dim 8.
**Evidence (measured at 375×812):** footer anchors Work / Founders / Contact `63×27`; footer emails
`170×27` ×2; founder-card emails `191×30` and `193×30`; "Meet the founders →" `164×28`. Plan §11
states *"email links keep ≥44px tap targets."* The footer anchors additionally sit only 4 px apart
vertically, which is tight for a thumb.
**What "fixed" looks like:** give `.link-draw` and `.link-arrow` a touch-safe box on coarse pointers —
e.g. `@media (pointer:coarse){.link-draw,.link-arrow{min-height:44px;display:inline-flex;align-items:center}}`
and raise `.foot-cols a` spacing so adjacent targets don't collide. Keep the underline-draw sitting on
the text, not on the padded box. Re-measure all eight at 375 px.

### 3. [MED] Portfolio plates look clickable and aren't
**What fails:** the click-test hard gate (misleading affordance).
**Evidence:** `.plate-row:hover .plate{border-color:var(--cobalt)}` — but the plate is not inside a
link (`closest('a') === null`) and `getComputedStyle(.plate).cursor === "auto"`. The problem is that
**cobalt is declared in the art direction as "the ONLY interactive color"**, and on this very page a
cobalt border on hover is exactly the clickable cue used by `.contact-card` (which *is* an `<a>`).
So the same signal means "click me" in one section and nothing in another. On a portfolio site whose
stated #1 job is the portfolio, a visitor mousing over the Cecere plate and clicking nothing is a
credibility ding.
**What "fixed" looks like:** pick one — (a) drop the cobalt border sweep on `.plate` and let the
caption's title carry the hover (see fix #4), or (b) make the whole plate a real link where an honest
destination exists. Do **not** add `cursor:pointer` without a destination.

### 4. [LOW] Two specced hover flourishes are missing, and one left dead CSS behind
**What fails:** plan fidelity (§10), rubric dim 9.
**Evidence:** the plan's plate hover is *"the caption's title underline draws + the frame border color
sweeps to cobalt"* — only the border half is implemented; there is no rule targeting
`.plate-caption h3` on hover. And the documented pan flourish left `transition:object-position 6s`
on `.shot img` (style.css:193) with **no rule that ever changes `object-position`** — and it could not
work regardless, since the image is `height:auto` with no `object-fit`.
**What "fixed" looks like:** implement the caption-title underline-draw (it also solves fix #3 by
moving the hover cue onto something that genuinely is text), and delete the dead
`transition:object-position` declaration. Dropping the pan itself is fine — the plan explicitly made
it the first thing to cut.

### 5. [LOW] Anchor targets have no `scroll-margin-top`
**What fails:** nothing today; flagged as brittleness.
**Evidence:** jumping to `#founders` lands the section top at `getBoundingClientRect().top === 0`,
i.e. underneath the 76 px sticky header. It is currently invisible only because each section carries
`clamp(6rem,11vw,10rem)` of top padding. Any future padding reduction silently tucks the section
kicker under the header.
**What "fixed" looks like:** `.section, #top{scroll-margin-top:calc(var(--nav-h) + 1rem)}`.

## 6. Optional — for Harry, not the builder

- The Cecere plate's URL pill reads `cecerebrotherslandscaping.com`, presented in browser chrome as
  though that is where the site lives. Worth confirming that is the real live domain. If the Cecere
  build isn't public at that address yet, swap the pill for a neutral label — the rest of the page is
  scrupulously honest and this is the one string I couldn't verify from the client answers.
- A location line for the agency was deliberately omitted (no address or service area was supplied).
  If Harry wants "Essex County, NJ" on the site, he needs to say the words and they get added verbatim.

## 7. Next round

Fixes 1–3 are required to clear the gate; 4–5 are cheap and should ride along. All five are
surgical CSS/HTML edits — **no redesign, no re-planning, and nothing about the art direction,
palette, typography, layout or content should change.** On re-submission I will re-check only the
changed rules plus the no-JS render, the 375 px tap targets, and the plate hover state.

`design-memory.md` row will be appended on sign-off, not before.
