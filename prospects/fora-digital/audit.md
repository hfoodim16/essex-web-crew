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

---
---

**Review round: 2**
**Auditor:** Critic (Essex Web Crew)
**Date:** 2026-07-23
**Artifact:** `prospects/fora-digital/mockup/` after the round-1 fix pass
**Method:** re-check of the five round-1 fixes only, plus the no-JS render, 375 px tap targets
and the plate hover state, as promised in round 1 §7.

## VERDICT — **FAIL** (round 2)

The round-1 blocker was genuinely fixed. Round 2 fails on a **new regression introduced by the
fix pass itself** — a reminder that a fix round needs the same capture discipline as a build round.

### Round-1 fixes — all five verified fixed

| # | Round-1 finding | Status |
|---|---|---|
| 1 | Page renders as solid cobalt blocks with JS disabled | **FIXED** — `main.js` now sets `document.documentElement.classList.add('js')` as its first executable statement, and every curtain rule is scoped `.js .reveal::after`. With JS off the page renders as plain, readable content. |
| 2 | Sub-44 px tap targets at 375 px | **FIXED** — `@media (pointer:coarse)` block added covering `.link-draw`, `.link-arrow`, `.foot-cols a`, `.nav-links a`, plus `.contact-card .c-email`. |
| 3 | False affordance — plates look clickable but aren't | **FIXED (by removal)** at this point in time: the cobalt hover cue was stripped so the plates no longer promised a click. *(Superseded in round 3 — see below.)* |
| 4 | Dead `transition:object-position` declaration | **FIXED** — declaration removed; the caption-title underline-draw implemented in its place. |
| 5 | Anchor targets have no `scroll-margin-top` | **FIXED** — `#work,#founders,#contact,#top{scroll-margin-top:calc(var(--nav-h) + 12px)}`. |

### 1. [BLOCKER] Regression — the honesty badge and the project title collapsed onto one line

**What fails:** while implementing fix #4, `.plate-caption h3` was given `display:inline` so the
underline-draw gradient would track the text rather than the full block width. An inline `h3` shares
a line box with the preceding inline-block `.badge`, so both plates now read as a single run —
`REAL CLIENT WORK Cecere Brothers Landscaping` — instead of a badge sitting above its title.

**Evidence:** measured on both plates — `gapBadgeToTitle = -37 px` (the title's top sits *above* the
badge's bottom), `getComputedStyle(h3).display === "inline"`, badge and title tops within 4 px of
each other. The `h3`'s `margin-bottom` is silently discarded because vertical margins do not apply
to inline boxes.

**Why this blocks:** those badges are this site's load-bearing honesty device. "Real client work"
and "Concept build" are the mechanism by which one paying client and one fictional demo are kept
visibly distinct, which is the single hardest requirement in `client-answers.md`. When the badge
merges into the title it stops reading as a label and starts reading as a prefix — degrading the
one element that must never be ambiguous. Content honesty itself re-verified **CLEAN**; the
regression is presentational, but it presents the honesty.

**What "fixed" looks like:** keep the `h3` block-level and move the underline onto an inner
element — `<h3><span class="u">…</span></h3>`, with `.plate-caption h3{font-size:var(--fs-h3);
margin-bottom:var(--space-1)}` and the gradient plus hover target on `.plate-caption h3 .u`.

### 2. [NOTE, non-blocking] `.wordmark` omitted from the coarse-pointer tap-target rule

`.wordmark` measures 95 × 40 px at 375 px — 4 px short on the vertical. It was left out of the
fix-#2 selector list. Add it.

### 3. Process finding — the capture that would have caught this was never taken

Both screenshots delivered with the round-1 fix pass were **hero-only frames**. A hero frame cannot
show a defect in the Work section. Round 1 explicitly asked for the plate hover state to be
re-checked; the regression sat two screens below the delivered evidence. **Any future round that
touches the Work section must ship a Work-section capture.** Logged into the QA field notes.

## Next round

Fix #1 is required to clear the gate; #2 rides along. Both are surgical CSS/HTML edits. Nothing
about the art direction, palette, typography, layout or copy changes.

---
---

**Review round: 3**
**Auditor:** Critic (Essex Web Crew)
**Date:** 2026-07-23
**Artifact:** `prospects/fora-digital/mockup/` (index.html · style.css · main.js · assets/ · **work/**)
**Verified against:** `client-answers.md` (top authority) → `website-plan.md` → `CLAUDE.md`
**Method:** served over `http://localhost:5601` in the browser pane; **Work-section capture taken
this round** (`screenshots/work-section.png`) per the round-2 process finding; both bundled builds
opened over HTTP *and* over `file://`; no-JS and `prefers-reduced-motion` states reproduced in
headless Chrome with pixel-level cobalt-coverage measurement; contrast computed numerically;
coarse-pointer tap targets measured by injecting the shipped `@media (pointer:coarse)` declarations
into a `pointer:fine` viewport.

## VERDICT — **PASS** (round 3)

- **$10K Checklist: 8 / 8** → clears the gate.
- **web-design-ultra rubric: PASSES** — no dimension below 7, boldness 9.
- **Content honesty: CLEAN — full pass, no findings.**

The round-2 regression is gone, the round-1 blocker stays fixed, and the two changes Harry
requested between rounds are implemented correctly and — importantly — make the page *more*
honest than it was, not less. Signed off.

## 0. What changed since round 2

Two client-requested changes, plus the round-2 regression fix.

1. **Browser-chrome bar removed from all four plates.** The faux dots + URL pill are gone from the
   markup and the `.chrome` / `.dots` / `.url-pill` rules are gone from the stylesheet.
2. **The two real portfolio plates are now genuine links** into bundled copies of the actual builds,
   shipped inside the mockup at `mockup/work/`.
3. Round-2 fix: `h3` restored to block-level with the underline moved to an inner `<span class="u">`.
4. Round-2 note: `.wordmark` added to the coarse-pointer 44 px selector list.

### A round-1 finding is deliberately reversed — and that is correct

Round 1 finding #3 flagged the plates as a **false affordance**: they carried a cobalt hover cue but
did nothing. Round 2 recorded it fixed by *removing* the cue. The plates are now real links, so the
cue is no longer a lie — restoring `cursor:pointer` and the cobalt border sweep is the right call and
is **re-scored as correct**, not as a regression. The affordance and the behaviour now agree, which
is what the original finding actually asked for.

The chrome-bar removal also retires round 1's open question about the `cecerebrotherslandscaping.com`
URL pill implying our build was live at that domain. The claim is gone; the question is moot.

## 1. The $10K Checklist

| # | Item | Score | Justification |
|---|---|---|---|
| 1 | Point of view, not a template | **PASS** | "Main Street Modern" unchanged and intact. Removing the chrome bar strengthens it — the plates now read as framed prints on a linen wall rather than as browser screenshots, which is the metaphor the section head ("Hung with pride") was always reaching for. |
| 2 | Typography that does work | **PASS** | Instrument Serif / Hanken Grotesk. Measured at 1440: h1 116 px / lh 121.8, h2 56 px, body 17 px / lh 28.05. No generic fallbacks anywhere. |
| 3 | Restrained color system | **PASS** | Unchanged. Cobalt still confined to interactive + badge + wordmark; clay still appears exactly once. |
| 4 | Hierarchy that breathes | **PASS** | Badge → title → description, in that order, on both plates. Verified in the Work-section capture. |
| 5 | Imagery with intent | **PASS** | Still **zero AI-generated images**, per the ZERO budget in `client-answers.md`. Two real screenshots, both `loading="lazy"`, both with `width`/`height`, both local. |
| 6 | Motion that whispers | **PASS** | Mask-curtain signature intact and `.js`-scoped. Reduced-motion kill switch verified live (below). No fade-up, no count-up. |
| 7 | Mobile designed, not shrunk | **PASS** | `document.documentElement.scrollWidth === 375` at a 375 px viewport — no horizontal overflow. **All 15 interactive elements reach ≥44 px** under the shipped `@media (pointer:coarse)` rule (measured: 0 remaining under 44, down from 8 in round 1 and 1 in round 2). |
| 8 | The invisible expensive stuff | **PASS** | No-JS render safe (0.43 % cobalt). Zero console errors on the mockup and on both bundled builds. Heading order h1→h2→h3 with no skips. Both images have descriptive alt. JSON-LD still omits `telephone`/`address`. WCAG AA passes on every measured pair. |

**Score: 8 / 8.** Gate cleared.

## 2. web-design-ultra 10-dimension rubric

| # | Dimension | Score | Change from round 1 |
|---|---|---|---|
| 1 | **Boldness / distinctiveness** | **9** | — |
| 2 | Visual hierarchy | 8 | — |
| 3 | Typography craft | 9 | — |
| 4 | Color & contrast | 9 | — |
| 5 | Spacing rhythm | 7 | — |
| 6 | Background / depth | 8 | — |
| 7 | Imagery quality | **9** | Held. The plates lost the chrome bar and gained ~24 px of image per plate; the frame identity survives on border + radius + shadow alone. |
| 8 | Responsiveness | **8** | ↑ from 7 — tap-target failure resolved. |
| 9 | Motion polish | **8** | ↑ from 7 — the curtain now has a real non-JS fallback and the dead `object-position` transition is gone. Still short of 9: two specced flourishes were never built. |
| 10 | Cohesion | 9 | — |

**Gate: no dimension below 7 ✓ · boldness 9 ≥ 8 ✓ → rubric PASSES.**

## 3. Verified technical evidence — round 3

**Round-2 regression — resolved.** Measured on both plates:

| Plate | `gapBadgeToTitle` | `h3` display | `h3` margin-bottom | badge & title share a line? |
|---|---|---|---|---|
| Cecere Brothers Landscaping | **+16 px** | `block` | `8px` | **no** |
| Corey Blake's Steakhouse | **+16 px** | `block` | `8px` | **no** |

Round 2 measured `-37 px` and `display:inline` on both. **Work-section screenshot captured and
inspected** (`screenshots/work-section.png`, 1440-wide source) — badge sits on its own line above
the title on both plates, confirmed visually, not just numerically.

**Chrome bar — fully removed.** `grep` count of `chrome` / `dots` / `url-pill` = **0 in
`index.html`** and **0 in `style.css`**. No dead CSS left behind. Visually the plates still read as
deliberate framed objects rather than amputated screenshots.

**Portfolio links — genuine and safe.**

| | Cecere plate | Steakhouse plate |
|---|---|---|
| `href` | `work/cecere-brothers/index.html` | `work/corey-blakes-steakhouse/index.html` |
| `target` / `rel` | `_blank` / `noopener` | `_blank` / `noopener` |
| `aria-label` | "Open the Cecere Brothers Landscaping site in a new tab" | "Open the Corey Blake's Steakhouse concept site in a new tab" |
| `cursor` | `pointer` | `pointer` |

- Explicit `index.html` in the href (not a bare directory) — required for `file://`, where
  directory→index resolution does not happen.
- `.plate-link:focus-visible` ring present in addition to the global `:focus-visible`.
- **Coming-soon plates: 0 anchors, `cursor: auto`** — no affordance, nothing to click. Correct.

**Bundled builds load completely, in both contexts.**
- Over HTTP: Cecere → `index.html` + `logo-real.png` (real client logo, 544 px natural width) +
  `hero.webp`, `patio.webp`, `design.webp`, `masonry.webp`, `lawn.webp` — **all 200**, document
  height 8175 px. Steakhouse → `index.html` + `style.css` + `main.js` + `hero-steak.jpg` — **all 200**.
- Over `file://`: both render correctly (headless capture inspected — Cecere shows the real logo,
  hero photograph and god-ray treatment intact).
- **0 absolute-path references** in either bundled build, which is why `file://` works.
- Every `url()` reference in both builds resolves to a file that exists on disk.
- Bundle size 3.2 MB total (Cecere 1.4 MB, Steakhouse 1.8 MB) — the ~950 KB of unused Cecere
  editorial backups and the unused 11.6 MB `hero-steak.png` were correctly excluded.

**No-JS resilience — holds.** Headless Chrome, `--disable-javascript`, 1440×2400:
**cobalt coverage 0.43 %** (round 1: effectively the entire page). Visual inspection confirms the
hero renders as plain, readable, correctly-styled content — wordmark, nav, headline, lead, both
CTAs, marquee. The round-1 blocker is genuinely gone, not merely repainted.

**Reduced motion — holds.** Headless Chrome, `--force-prefers-reduced-motion`, 1440×1600:
cobalt coverage 0.65 %, all content visible. The `@media(prefers-reduced-motion:reduce)` block kills
`animation`, `transition` and `scroll-behavior` globally, hides the curtain panel, and stops the
marquee and asterisk loops. `main.js` independently calls `openAll()` on the reduce branch.

**Contrast (computed, WCAG 2.x) — every pair passes.**

| Element | Ratio | Size | Verdict |
|---|---|---|---|
| `.btn-primary` (white on cobalt) | **7.62** | 15 px / 600 | AA + AAA |
| `.badge-real` (white on cobalt) | **7.62** | 12 px / 600 | AA + AAA |
| `.badge-concept` (ink on paper) | **15.7** | 12 px / 600 | AAA |
| `.link-draw` / `.c-email` (cobalt on surface) | **7.37** | 17–17.6 px | AA + AAA |
| `.foot-line` | **8.33** | 15 px | AAA |
| founder bio, `.soon-sub`, `.kicker.role` (stone on surface) | **5.40** | 17 / 15 / 13 px | AA |
| `.hero-kicker`, `.hero-lead`, `.plate-caption p` (stone on paper) | **4.96** | 13–21 px | AA |
| `.foot-bottom p` | **4.85** | 15 px | AA |
| `h1 em` (clay on paper) | **4.35** | 54.4 px display | AA-large (needs 3.0) ✓ |

Lowest body-copy ratio is 4.85 against the 4.5 threshold. No failures.

**Structure & accessibility.** 15 interactive elements, all ≥44 px on coarse pointers. Heading
order: h1 → h2 → h3 ×2 → h2 → h3 ×2 → h2, no skips, exactly one h1. 2 images, **0 missing alt**.
Zero console messages on the mockup and on both bundled builds. No horizontal overflow at 375 px
or 1440 px.

## 4. Content-honesty verdict — **CLEAN, no findings**

Re-verified line by line against `client-answers.md`.

- **Two co-owners, named correctly**, both labelled "Co-Owner". No invented division of labour.
- **Harry's bio** carries exactly the four supplied facts (co-owner; sophomore at The Ohio State
  University studying accounting; West Essex High School; sports / gym / family and friends) and
  adds nothing.
- **Corey's bio** carries exactly the two supplied facts and — correctly — is allowed to be shorter
  rather than padded to match Harry's. The layout absorbs the asymmetry instead of inventing a
  third line, which is precisely what the honesty rule demanded.
- **Emails exact**, including the capitalised `CRapkin@`. Present in the founder cards, the contact
  cards, the footer and the JSON-LD.
- **No phone number, no street address** anywhere — including in structured data. `grep` for tel:
  patterns, digit-group phone formats and address tokens in `index.html`: **0 matches**.
- **Portfolio labelling is unambiguous.** "Real client work" on Cecere; "Concept build" on the
  steakhouse, with body copy that says it outright — *"a fictional steakhouse we designed to show
  the range… Not a client; a demonstration."*
- **Coming-soon plates invent nothing** — no fake logo, client name or screenshot. "Next project —
  in progress."
- **No fabricated social proof.** `grep` for `years`, `experience`, `clients served`, `N+`,
  `testimonial`, `award`, `certified`, `licensed`, `insured`, `trusted by`, `rated`, `reviews`,
  `guarantee`: **0 matches**. The section head owns the position instead — *"A young studio's honest
  wall — one real client, one concept build, and room we intend to fill."*
- **Headshots are honest placeholders** — HF / CR monograms with "Photo coming soon". No
  AI-generated faces of real people.

Making the plates clickable *raises* the honesty bar and the build clears it: a prospect can now
verify the claim rather than take the screenshot on trust, and what they land on is the genuine
article — the real Cecere build with the real client logo, and the steakhouse concept that is
labelled a concept before they ever click it.

## 5. Remaining findings

None blocking. One item for Harry's decision, one for the record.

### A. [LOW — Harry's call] The bundled Cecere build has a placeholder `tel:` on its estimate CTA

`work/cecere-brothers/index.html:251` — `<a href="tel:+10000000000" class="btn">Get a free
estimate</a>`. **No fake number is displayed** (the button reads "Get a free estimate"), so nothing
dishonest is on screen, but a prospect who taps it on a phone dials a dead placeholder. It is inside
a bundled copy of a client build, not the Fora site, and we do not have Cecere's real number — so I
have deliberately **not** changed it. Options: supply the real number, or repoint the CTA at the
build's own contact section. Flagging, not fixing.

### B. [NOTE] The mockup folder is now 3.2 MB heavier

`mockup/work/` bundles two full sites so the deliverable stays self-contained and works by
double-click as well as on Netlify. That is the right trade for a portfolio, but it is worth knowing
before this gets treated as a lightweight static folder.

## 6. Sign-off

Round 3 **PASSES**. `design-memory.md` row appended.

---
---

**Review round: 3a — copy revision**
**Auditor:** Critic (Essex Web Crew)
**Date:** 2026-07-23
**Scope:** copy only. No CSS, no layout, no structure, no design decisions touched.

## Why

Round 3 passed the design gate, but Harry's read was that the wording sounded AI-generated. A
`/humanizer` audit of `index.html` confirmed a dense cluster of tells rather than one or two
isolated ones:

- **7 em dashes** in visible copy (the single most reliable AI signature)
- **Four consecutive rule-of-three constructions** in the leads and captions
- **Manufactured punchline fragments** — "Not a client; a demonstration.", "nothing padded"
- **Hyphenated-compound pileup** — design-led / estimate-first / mobile-down / reservation-first,
  four in two sentences
- **"actually" as an intensifier** — "the businesses people actually rely on"
- **Stock bio-speak** — "away from the studio you'll find him…"

Every lead landed like a quotable closer. That cadence is the tell, more than any single word.

## What changed

Ten strings, rewritten in a plain first-person "we" voice: meta description, OG description, hero
lead, Work lead, both plate captions, both coming-soon plates, both founder bios, contact lead.
Two `alt` attributes and the `<title>` lost their em dashes (the title now reads
"Fora Digital: Modern sites for local businesses", matching the client's own positioning line
verbatim instead of title-casing it).

**Deliberately unchanged:** the H1, every section headline ("Hung with pride.", "Two names on the
door.", "Start a project."), all kickers, both badges, the marquee, the footer, the wordmark, the
JSON-LD, and every CTA. Those already read as human copywriting.

## Verification

- **Em/en dashes in rendered copy: 0.** Three remain in HTML source comments, which never render.
- **Layout held.** Desktop `scrollWidth === 1440`, 375 px `scrollWidth === 375`, no horizontal
  overflow at either width. Badge→title gap still **+16 px** on both plates with `sameLine: false`;
  title→body **+8 px**. Founder cards stay equal-height (477 px) despite Harry's bio being three
  lines longer than Corey's, with a 16 px gap to each email link. Work-section and founders-section
  screenshots captured and inspected.
- **All three screenshots re-captured** (`desktop.png`, `mobile.png`, `work-section.png`).

## Content honesty — re-verified **CLEAN**

The rewrite adds no facts and removes no labels. Checked against `client-answers.md`:

- Harry's bio still carries exactly his four supplied facts; Corey's still carries exactly his two,
  and is still allowed to be shorter rather than padded.
- Emails unchanged and exact. Still no phone, no address, no stats, no testimonials.
- **The concept labeling got stronger, not weaker.** "A sample build… Not a client; a
  demonstration." became "This one isn't a client. Corey Blake's is a steakhouse we made up so you
  can see what we'd do with a restaurant." Plainer language, same badge above it, and harder to
  misread at a glance.
- The Work lead now says the quiet part in the first person: "We're a young studio and this wall
  doesn't pretend otherwise."
- One detail was added to the Cecere caption: **"in Essex County."** This is not a new claim; it is
  stated on the bundled Cecere build itself ("West Essex County, NJ") and is the client's own
  service area, not Fora's. Verified against the bundled source.

**Verdict: PASS holds.** No re-score needed on the 10-dimension rubric or the $10K Checklist since
design, layout, motion, imagery and structure are untouched.

---

**Review round: 3b — positioning revision**
**Date:** 2026-07-23
**Scope:** copy only. No CSS, no layout, no design changes. One `<p class="lead">` added to the
founders section head, reusing the existing section-head pattern.

## Harry's direction

Three instructions: stop calling it a studio, stop repeating "two people," and say that we're
client-friendly.

## What changed

- **"Studio" is gone.** 0 occurrences in rendered text. The hero kicker is now "A small web
  agency," which matches the descriptor in `client-answers.md` ("a two-person web agency") without
  leading with the headcount.
- **The headcount drumbeat is gone.** 0 occurrences of "two people" / "two-person." It had been
  hit five times: hero kicker, hero lead, meta description, OG description, contact lead, plus the
  founders headline "Two names on the door." The fact is still visibly true (two founder cards,
  two contact cards, two emails) but the copy no longer keeps announcing it.
- **Client-friendliness is now stated in three places**, each saying something different rather
  than repeating one claim:
  - Hero: "we make it easy: email us directly and get a real answer in plain English."
  - Founders (new head lead): "Whoever you email is the person who builds your site. Nothing gets
    handed off."
  - Contact: "Email either of us directly. Tell us what your business does and what you want the
    site to do for you, and we'll take it from there."
- Founders headline "Two names on the door." became "Who you'll be working with." (also
  client-facing rather than self-describing).
- Work lead "We're a young studio…" became "We're new at this…".

## Honesty check on the new claims

These are manner-of-service statements, not verifiable specifications, and they are all true given
that both owners do the work themselves. **Nothing operational or commercial was promised.** A
draft line offering a free consultation ("no charge to talk it through") was written and then
**removed before shipping** because Harry has not set that term. If he wants concrete promises on
the site (response time, revision policy, free first call, pricing), those need his actual terms
and they are not on the page today.

No new facts about either founder. Bios, emails, badges, portfolio labeling all unchanged.

## Layout verification

- **Hero regression caught and fixed.** The first client-friendly hero lead ran to 5 lines, pushing
  the hero from its 824 px minimum to 860 px and dropping the marquee band 36 px below the fold at
  1440x900. Trimmed back to 3 lines; hero is 827 px, marquee bottom 903 px, matching the pre-change
  baseline.
- **Orphan check on every `.lead`** (measured per-word line positions): hero 3 lines / 10 words on
  the last, work 5 / 5, founders 3 / 4, contact 4 / 7. No single-word orphans. An earlier founders
  lead ended with an orphaned "to." and was rewritten.
- No horizontal overflow at 1440 px or 375 px. Plate badge-to-title gap still +16 px on both plates.
- All three screenshots re-captured; founders section inspected separately.

**Verdict: PASS holds.**

---

**Review round: 3c — trims**
**Date:** 2026-07-23
**Scope:** copy only, two deletions at Harry's direction.

1. **Work section lead removed.** "We're new at this and the wall doesn't pretend otherwise…"
   is gone. The Work head is now kicker + H2 only, the same two-element shape the Founders head
   used before round 3b. Gap from head to first plate measures 104 px at both 1440 and 375, matching
   the Founders section, so the rhythm is consistent rather than a dropout.
2. **Hero kicker is now "Fora Digital"** (was "A small web agency"). It reads as a nameplate above
   the headline. Note it repeats the header wordmark directly above it; that is intentional per
   Harry and reads as an editorial masthead, not an error.

**Honesty note:** the removed Work lead was the sentence that voluntarily disclosed the studio's
youth. The load-bearing honesty devices are untouched and still do the work: the "Real client work"
and "Concept build" badges, the steakhouse caption that says outright "This one isn't a client…
we made up," and the two "Next project, in progress" placeholders that invent nothing. Content
honesty re-verified **CLEAN**.

**Verification:** no horizontal overflow at 1440 or 375. Plate badge-to-title gap +16 px on both.
Hero still 827 px with the marquee at its 903 px baseline. Zero console errors. All three
screenshots re-captured.

**Verdict: PASS holds.**

---

**Review round: 3d — founders lead removed**
**Date:** 2026-07-23
**Scope:** copy only, one deletion at Harry's direction.

Removed the Founders head lead ("Whoever you email is the person who builds your site. Nothing gets
handed off."). The Founders head is now kicker + H2 only, matching the Work head.

Section-head shapes are now: **Work** kicker+H2, **Founders** kicker+H2, **Contact** kicker+H2+lead.
All three measure a **104 px** gap from head to content, so the page reads as one rhythm with the
Contact lead as the single deliberate exception (it tells a prospect what to put in the email).

Client-friendly positioning now lives in two places instead of three: the hero lead ("we make it
easy: email us directly and get a real answer in plain English") and the contact lead. The founders
section makes the same point structurally rather than in prose, since the two named owners with
direct email addresses *are* the answer to "who you'll be working with."

**Verification:** no horizontal overflow at 1440 or 375. Zero console errors. Content honesty
unchanged and CLEAN. All three screenshots re-captured; Founders section inspected separately.

**Verdict: PASS holds.**

---

**Review round: 3e — reviews section added**
**Date:** 2026-07-24
**Scope:** new section + supporting CSS + two nav/footer links. No changes to existing sections.

## What was built

A **Reviews** section between Contact and the footer (literally at the bottom, as asked), plus
"Reviews" added to the primary nav and the footer Pages list, and `#reviews` added to the
scroll-margin-top anchor set.

- **Head:** kicker "Reviews" + H2 "Leave a review." + a one-line lead + a cobalt
  "Email us your review" button (`mailto:hfoodim@foradigital.com?subject=Review for Fora Digital`).
  Email is the same contact mechanism the whole site uses, so no backend is implied.
- **Empty state — the "space to show them when they come in."** A dashed-border panel with a
  cobalt open-quote glyph, "No reviews yet," and "You could be the first…" It mirrors the
  coming-soon portfolio plates and the "Photo coming soon" monograms: an intentional placeholder,
  never a fake.
- **Ready-to-use card system.** `.review-card` (clay stars, serif quote, stone author line) is
  fully styled and shipped, with an HTML-comment template in place. When a real review arrives,
  Harry swaps the empty-state block for one `.review-card` per review.

## Honesty — the load-bearing check for this section

`client-answers.md` says: *"No fabricated testimonials, review counts, client counts, or stats…
If a section needs social proof and we don't have it, cut the section."* The section is compliant
because **it displays zero reviews and claims none.** It is an invitation plus an honest empty
state, not manufactured social proof.

- **0 rendered `.review-card` elements**; the only star/quote markup lives inside an HTML comment.
- The comment template's example quote was changed from a realistic-sounding line ("Their site paid
  for itself in a month.") to an unmistakable placeholder ("PASTE THE CLIENT'S EXACT WORDS HERE"),
  with an inline instruction: *"paste in only words a client actually wrote — never invent a quote."*
  This removes any chance of a plausible fake being shipped by accident.
- A temporary two-card injection was used to confirm the layout, then discarded; verified the DOM
  restored to the empty state with no card left behind.

## Verification (measured)

- Section order: hero → work → founders → contact → reviews → footer. Anchor scroll-margin correct.
- Surface background + top rule separates it from the paper Contact above and the ink footer below.
- Head-to-content gap 104 px, matching every other section's rhythm.
- Card template renders as a real two-column grid (508 px cards), clay stars (#B4552D), serif quotes.
- 375 px: single column, empty panel right edge 356 px inside the 375 viewport, **no horizontal
  overflow**; button is a 55 px tap target.
- Zero console errors. No em/en dashes in the new copy.
- Deliverable capture saved: `screenshots/reviews-section.png`; desktop + mobile re-captured.

**Verdict: PASS holds.**

---

**Review round: 3f — "How it works" section added**
**Date:** 2026-07-24
**Scope:** new section + supporting CSS + one nav/footer link. No changes to existing sections.

## What was built and where the content came from

A **How it works** section (kicker "How it works" + H2 "From hello to live.") with four numbered
steps, placed after Founders and before Contact. Order is now:
hero → work → founders → **process** → contact → reviews → footer. "Process" added to the primary
nav and footer Pages list; `#process` added to the scroll-margin anchor set.

Source of the steps: `FULL-PROCESS.md` (the crew's real operating manual for how the business
takes a client from first contact to a live site). Per Harry's instruction, the section starts
**from step 2 of that process** — the internal Step 1 (finding/prospecting a business and reaching
out) is omitted because it isn't client-facing and the Contact section already owns "get in touch."
Only the **main ideas** are shown, not every sub-step, condensed to four client-facing phases:

| On the site | Maps to FULL-PROCESS |
|---|---|
| 01 Tell us about your business | Step 8A/11 questionnaire; golden rule "build only from real answers, never invent" |
| 02 We design and build it | Steps 5–6 (planner→builder→critic, revision rounds) |
| 03 We put it live on your domain | Step 13 (client owns the domain) + Step 10 (no monthly fees) |
| 04 We hand it off and stick around | Step 14 (plain-English handoff) + Step 15 (light maintenance) |

## Honesty check

Every claim traces to the real process document; nothing invented:
- "starts from your real answers, never guesswork" = the manual's golden rule verbatim in spirit.
- "a real site to look at, not a template" = custom planner→builder builds, true.
- "refine it with you until it feels right" = Steps 6/8C revision rounds (1–2 normal), true.
- "the domain stays yours / no monthly fees" = Step 13 ("the client should own the domain") + Step
  10 ("no monthly fees, unlike Wix/Squarespace"). True and not overstated: domain renewal is annual
  and the client's, and the copy says "no monthly fees," not "free forever."
- "hand it off... plain English / a change later is a quick email" = Steps 14–15, true.
No stats, no client counts, no fabricated claims.

## Design

Editorial ledger: four steps, each under its own hairline top rule with an oversized serif numeral.
Numbers are **stone, not cobalt** — cobalt stays reserved for interactive elements, per the design
system's one-interactive-color rule. Titles are serif h3 (site convention); body is stone `fs-small`.

## Verification (measured)

- Section order corrected: process sits before Contact (an earlier insert had briefly placed it
  after Contact; moved).
- Desktop: 4-up grid (234 px columns), head-to-content gap 104 px matching every other section.
- Tablet ≤900 px: 2×2 grid. Mobile ≤560 px: single column. **No horizontal overflow at 1440 or 375.**
- Header nav holds five links + CTA on one 76 px row without wrapping at 1440; nav-links are
  `display:none` on mobile (unchanged behavior), so the extra link doesn't crowd the phone header.
- Zero console errors. No em/en dashes in visible copy (also cleaned one stray dash inside the
  reviews template comment).
- Deliverable capture saved: `screenshots/process-section.png`; desktop + mobile re-captured.

**Verdict: PASS holds.**

---

**Review round: 3g — process steps 3 & 4 corrected**
**Date:** 2026-07-24
**Scope:** copy only, two step bodies + titles, at Harry's correction of the actual mechanism.

Harry corrected the domain/hosting reality: they host on **Netlify** and handle the domain by
either **buying a new one for the client** or **using the client's existing ("old") domain**.

- **03** "We put it live on your domain / …the domain stays yours…" → **"We set up the domain and
  hosting / We buy you a fresh domain or connect the one you already have, then host the site on
  Netlify. No monthly fees to keep it running."** Now names the real host and the real two-way
  domain handling, matching FULL-PROCESS Step 13 (13A existing domain / 13B buy new) + Step 10
  (no monthly fees).
- **04** "We hand it off and stick around" → **"We launch it and hand it off / Once everything
  checks out, we push the site live and hand it over. Want a change down the road? That's a quick
  email."** Go-live moved here so step 3 is cleanly domain+hosting setup and step 4 is
  launch+handoff+aftercare (Steps 14–15).

Verified: no overflow at 1440/375, two-line titles wrap cleanly in their columns, no em/en dashes,
`process-section.png` + desktop/mobile re-captured. **PASS holds.**

---

**Review round: 3h — interactive cobalt hero field**
**Date:** 2026-07-24
**Scope:** new hero canvas + CSS + a second IIFE in main.js. Additive; no copy/layout changes.

## What was added

Harry felt the front page was plain (the hero's right half was empty). Added an **interactive
cobalt "compass field"**: a `<canvas>` behind the hero content renders a grid of short line
segments that rotate to point at the pointer; segments near it grow longer/brighter, so a soft
radial spotlight follows the mouse. Idle / touch → a slow auto-orbit keeps it alive. It fills the
empty right side and makes the page read as "we build interactive things."

- `index.html`: one `<canvas id="hero-field" aria-hidden="true">` after `.hero-wash`; script tag
  cache-busted to `main.js?v=3`; "Process" + "Reviews" nav already present from earlier rounds.
- `style.css`: `.hero-field{position:absolute;inset:0;width:100%;height:100%;z-index:0;
  pointer-events:none}` — layered above the warm wash, below the registration frame and text;
  `pointer-events:none` so CTAs stay clickable.
- `main.js`: second IIFE. Grid capped ~1400 segments, DPR capped at 2, **no shadowBlur** (the
  documented EMBERS perf smell), IntersectionObserver pauses the rAF loop off-screen, debounced
  resize. Left→right alpha ramp keeps the headline area calm and the right half livelier.

## Brand / honesty
Pure abstract geometry, cobalt only. The field literally *is* interactive, so cobalt-as-the-only-
interactive-color still holds. No images, no fabricated content, no copy change.

## Two verification gotchas worth recording (added to the QA field notes takeaways)
1. **Canvas default size beats `inset:0`.** A `<canvas>` carries presentational width/height
   attributes (300×150); with `left:0` *and* `right:0` the width hint wins and the box stays 300px.
   Fix: explicit `width:100%;height:100%` on the canvas.
2. **A continuous rAF loop starves headless Chrome's `--virtual-time-budget`.** The reveal-curtain
   transitions froze mid-open in every virtual-time screenshot, at any budget (tested to 9s), even
   though real Chrome (the browser pane) rendered it perfectly. Fix: a `?still` capture flag that
   paints ONE static field frame and skips the rAF loop, so virtual-time captures render the real
   look with curtains open. The live site (no flag) runs the animation. All deliverable screenshots
   are now taken with `?still=1`.

## Verified
- Real Chrome (browser pane): field paints, concentrated on the right (~5× the left), headline legible.
- CTAs still clickable through the canvas (`elementFromPoint` over "See the work" returns the button;
  canvas never intercepts).
- Reduced motion (`--force-prefers-reduced-motion`): one static frame, no loop, curtains open.
- No horizontal overflow at 1440 or 375; canvas stays within the viewport on mobile.
- Zero console errors. desktop.png + mobile.png re-captured (still mode).

## Kept in reserve (Harry likes it too): floating work cards
The field is a `z-index:0` background layer, so a later pass can drop the two real portfolio
screenshots as tilted, parallaxing browser cards into the right half of the hero on top of the field
without a rebuild.

**Verdict: PASS holds.**

---

**Review round: 3i — marquee fill/seam fix + hero lead trim**
**Date:** 2026-07-24
**Scope:** hero marquee markup + CSS; one hero lead sentence swap. No other sections touched.

- **Hero lead:** dropped the "Fora Digital is Harry Foodim and Corey Rapkin." opener (names still
  live in Founders + Contact), now leads with "We design and build websites…" and closes with a new
  line: "Take a look at what we've made, then say hello." Still 3 lines; hero height and marquee
  position unchanged; no em dashes.
- **Marquee was 0.7× the viewport** (measured 1011px track vs 1440px viewport) → ~30% empty on the
  right, and the -50% loop exposed the seam as a cut-off word. Rebuilt as **two identical `.mq-set`
  groups**, each repeating the phrase enough to exceed the viewport (2587px per set), with the
  spacing carried on the set (internal gap + trailing `padding-right`) so `translateX(-50%)` lands
  exactly one set over. Track is now 3.59× viewport; loop distance == one set width (seam matches);
  set width (2587px) covers displays up to ~2560px. Duration 60s (~43px/s).
- Verified: two sets identical, each covers the viewport (no empty gap), seamless loop math holds,
  no horizontal overflow at 1440 or 375, marquee still clips (`overflow:hidden`). desktop.png +
  mobile.png re-captured.

**Verdict: PASS holds.**
