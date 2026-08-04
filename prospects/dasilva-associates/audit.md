# Audit — `dasilva-associates` · DaSilva & Associates, LLC

**Review round: 2** (incremental re-review of the round-1 fix list + full re-measure of everything
the azul+gold repaint and the lead's NAP dedup invalidated)
**+ Amendment A — real office photograph swapped in** (lead-directed asset swap on Harry's explicit
instruction, **not** a finding against the build; see the amendment section at the end). Sign-off
stands: re-verification turned up nothing.
**Verdict: PASS — $10K 8/8, rubric boldness 8, no dimension below 8.**
**Paid calls this prospect: 2 (~$0.10)** — hero `nano-banana-2` @2K (~$0.06) + Newark street @1K
(~$0.04). **No regenerations ordered this round; no new generations. The image cap is spent and
untouched.** ⚠ **Per Amendment A, only ONE generated image now ships** — the courtroom hero. The
generated streetscape was deleted and replaced by the client's real photograph of his real office.
The spend stands at 2 calls (the money was spent); the shipped count is 1. `og-image.webp` verified programmatically as a crop of the hero (best mean absolute
difference **2.50/255** against a scaled hero band at y=20 — compression noise, not a second
exposure), **not** a third paid call. No video, none requested by the plan.

**Detector: 0 errors, 0 advisory** across all four pages, exit 0, no `DETECTOR DEGRADED` banner.
**Waived in-file: none — zero `impeccable-disable` comments in the build.** The `cream-palette`
waiver died with the beige, as required, and did not reappear.

> ### ⚠ Independence caveat — read this first
> No builder existed this round. The lead granted write access and instructed me to implement the
> disclaimer. I therefore **both applied and judged** four code fixes (listed under "Fixes applied
> this round"). That is a departure from the normal critic contract, where the critic never edits
> the build. Every fix is small, named, and re-verified by measurement after the fact, and all
> gates were re-run post-edit — but Harry should know the gate and the hand were the same party on
> those four changes.
>
> **Also not run: the independent cold read.** The copy gate normally ends with a fresh subagent
> reading the page blind. Agent spawning is restricted in this session, so I performed the
> say-aloud read myself over **every visible string on all four pages** (not a spot check) and
> recorded it below. The mechanical halves (`copycheck.py`, `aitells.py`) both exit 0. Treat the
> cold read as outstanding rather than passed.

---

## Gate A — mechanical (all run before any screenshot)

| Gate | Result |
|---|---|
| Step 0 detector, 4/4 pages | **PASS** — 0 errors, 0 advisory, exit 0, 0 waivers |
| Detector engine liveness control | **PASS** — deliberately-bad control file → **6 findings, exit 2** (`gradient-text`, `overused-font`, `repeated-section-kickers`, `ai-color-palette`, `marketing-buzzword`). The clean result is a real pass, not a silent no-op |
| `copycheck.py`, 4/4 pages + voice-spec watch list | **PASS** — exit 0 |
| `aitells.py`, 4/4 pages | **PASS** — exit 0 |
| Exactly one `<h1>` per page | **PASS** — 1/1/1/1 |
| Horizontal overflow @375 (coarse) | **PASS** — `scrollWidth == innerWidth` on all four |
| Contrast sweep, computed, every text node | **PASS** — **0 failures across 56 distinct fg/bg pairs** |
| Tap targets @375 (coarse pointer emulated) | **PASS** — **0 elements under 44px** on all four pages |
| Console errors | **PASS** — clean on all four |
| Offline / no CDN | **PASS** — only external strings are canonical/OG URLs (metadata, not fetched). Fonts self-hosted WOFF2. **613 KB total** (was 652 KB before Amendment A) |

### Fail-visible — measured with the skill's own `impeccableMeasureHiddenText()`, six paths

Measured **before** any force-reveal, using the bundled browser build the gate names.

| Path | index | practice-areas | attorney-bio | contact |
|---|---|---|---|---|
| `main.js` **404** (never arrives) | **0%** | **0%** | **0%** | **0%** |
| `main.js` loads then **throws on line 1** | **0%** | **0%** | **0%** | **0%** |
| `main.js` throws **after** `motionOK()` (late throw) | **0%** | **0%** | **0%** | **0%** |
| **IntersectionObserver present but never fires** | **0%** | **0%** | **0%** | **0%** |
| `prefers-reduced-motion: reduce` | **0%** | **0%** | **0%** | **0%** |
| After riding the full page (every IO target given its chance) | **0%** | **0%** | **0%** | **0%** |
| **At rest, 1440×900, no scroll** | 72% | 46% | 47% | 23% |
| **At rest, 375×812, no scroll** | 71% | 50% | 48% | 22% |

**Round 1's 71%-on-throw hole is closed** (builder's fix), and a **second, previously undetected
hole was found and closed this round** — see fix 2 below.

**Documented exception — the at-rest number.** Read literally, 23–72% with body copy in the samples
exceeds the ~15% threshold. It is recorded as an exception, not a silent pass, for three reasons:

1. **Every degraded path measures 0%.** The gate's own text says the rename test and this
   measurement "are one gate, not two", and its subject — *content permanently hidden* — is met on
   all six non-at-rest paths.
2. **The threshold's calibration assumes non-opacity reveals.** The reference figure it cites (0% of
   3,035 chars) is a site whose vocabulary is mask-curtain and clip-wipe — `clip-path`, which the
   function does not read. This build's entrance is **opacity**-based, so it registers below-fold
   IO state as "hidden" by construction. Confirmed by reading the function's source: it counts any
   ancestor at `opacity <= 0.02`, with no viewport test.
3. **The blur-focus entrance is the Planner's locked Stage 5 signature move.** Per the playbook, a
   gate never overrules a direction the Planner locked for a real reason.

The residual risk is real and worth stating: an opacity entrance is the most fragile family, which
is why this build needs four independent un-hide guards where a transform-only entrance would need
none. `gee-kay` Rev 2 avoided this by going transform-only and measured 0% at rest.

## Composition counts (blocking — counted, not eyeballed)

| Page | Sections | Distinct families | Need | Family twice in a row | Kickers | Budget | Adjacent opener match | Max opener share |
|---|---|---|---|---|---|---|---|---|
| `index` | 7 | **7** (hero, stat-strip, card-grid, quote-monolith, split, editorial-column, cta-band) | ≥4 | none | **1** | ≤3 | none | 2/7 = 29% |
| `practice-areas` | 6 | **6** (hero, split, card-grid, steps, editorial-column, cta-band) | ≥3 | none | **1** | ≤2 | none | 3/6 = 50% |
| `attorney-bio` | 4 | **4** (split, steps, card-grid, cta-band) | ≥2 | none | **0** | ≤2 | none | 2/4 = 50% |
| `contact` | 3 | **3** (split, table, full-bleed-band) | ≥2 | none | **1** | ≤1 | none | 1/3 = 33% |

All five quotas **PASS** on all four pages. `practice-areas` and `attorney-bio` sit exactly at the
50% opener line (the rule fails *above* 50%); `contact` spends exactly its budget of 1.

**Falsifiable facts** (`aitells.py` `min_falsifiable`, floor 1): **7 / 5 / 8 / 1**. PASS.
(`index` rose 6 → 7 with Amendment A's address caption.)
⚠ `contact` fell from 4 to **1** — the lead's NAP dedup removed the duplicate address sentence, the
map-label digits and the form-intro digits, which were the checkable facts it was counting. Still
above the floor, but it is now one edit away from failing; worth knowing before anything else is
trimmed from that page.

**Composition device — named and landed: the ≥3× numeral scale jump.** Measured per page from the
desktop renders:

| Page | Device instance | Measured jump |
|---|---|---|
| `index` | trust-strip `May 2002` 84px vs 19.2px body | **4.38×** |
| `practice-areas` | §11 `③` 80px vs 18.4px body | **4.35×** |
| `attorney-bio` | §15 `1996` 80px vs 17px body | **4.71×** |
| `contact` | `.contact-phone` 56px vs 16.3px body | **3.43×** |

Landed on all four. Note the plan (§5) deliberately declares **the scale contrast itself as the
symmetry break** — "Grids stay calm (variance 5); the scale contrast IS the symmetry break" — rather
than an overlap or off-grid offset. That is a Planner-locked call with a stated reason, so the check
passes as specified. It is also the single biggest reason boldness lands at 8 rather than 9 (below).

---

## Scoreboard 1 — the $10K Checklist

| # | Item | Score | Note |
|---|---|---|---|
| 1 | Point of view, not a template | **PASS** | "The Quiet Verdict" — dark-first azul poster-stack, full-bleed photographic courtroom hero with the headline set over the image, gold as the working accent on dark bands, oversized real numerals as the hierarchy engine. Not the category template. |
| 2 | Typography that does work | **PASS** *(was FAIL)* | Frank Ruhl Libre 900 / Red Hat Text — non-banned, self-hosted, real 13→84px range. **Round-1 fix 1 verified fixed at three widths:** `1996` now clears its `<h2>` by **25.6px** at desktop and **stacks** at tablet (834) and phone (375); `practice-areas` §11 `③` unregressed (also 25.6px clear). **Round-1 fix 2 was NOT fixed and is fixed now** — see fix 1 below. |
| 3 | Restrained colour system | **PASS** | 5 core tokens + derived tints, all in `:root`, no hardcoded hex in components. The structural accent flip is intact and verified live, not replaced by per-element overrides: `:root` sets `--accent: var(--azul)`; `.band-dark, .hero, .site-footer, .topstrip` redefine it to `var(--gold)`. Measured: gold `rgb(200,162,74)` appears **only** on `rgb(6,43,68)`; azul `rgb(0,88,138)` **only** on light. Never gold on paper, never azul on dark. |
| 4 | Hierarchy that breathes | **PASS** *(was FAIL)* | h1 now **64 / 56 / 56 / 56px** against a 44px max `<h2>` on every page. Band rhythm generous; scale jump lands on all four. |
| 5 | Imagery with intent | **PASS** | Both `GENERATE` slots hold real photorealistic on-direction images passing the two-way test (detail below). Every other slot is a labeled placeholder. 2 generations, at the cap. |
| 6 | Motion that whispers | **PASS** | Signature nameable from the screenshots: **blur-focus entrance + icon-nudge hover**, one tempo (600ms / 70ms stagger), no scroll set-piece, one ambient system (god rays, hero only). Reduced-motion gated — hidden state lives inside `@media (prefers-reduced-motion: no-preference)`. Distinct from the last 3 `design-memory` rows. |
| 7 | Mobile that's designed, not shrunk | **PASS** *(was FAIL)* | **Round-1 fix 4 verified: 0 elements under 44px** at 375 with a coarse pointer, all four pages (was 22–43px). Zero overflow. Real phone decisions: stacked hero with full-width gold CTA carrying the digits, 1-col stats, `<table>` reflows to blocks, side-label rotates, header address dropped. **One further mobile defect found and fixed this round** — see fix 4. |
| 8 | The invisible expensive stuff | **PASS** *(was FAIL)* | `Attorney` JSON-LD, identical on all 4 pages, carrying **only** authorized keys — no `openingHours`, `email`, `aggregateRating`, `review`, `priceRange` or `award`. Full meta/OG/Twitter, canonical, inline SVG favicon, skip link, semantic landmarks, 3px `:focus-visible` ring that flips with scope (gold on dark, azul on light), self-hosted WOFF2, zero CDN, 652 KB, no console errors. **Round-1 fix 3 verified fixed, and a second JS hole found and closed** — fix 2. |

**8 / 8.**

## Scoreboard 2 — `web-design-ultra` 10-dimension rubric

| # | Dimension | Score | Note |
|---|---|---|---|
| 1 | **Boldness / distinctiveness** | **8** | Clears the bar, and only on structure. See the honest read below. |
| 2 | Visual hierarchy | **8** | h1 inversion fixed; scale jump lands on all four; band rhythm reads. Docked: `contact`'s left column still runs empty below the NAP against a much taller form. |
| 3 | Typography craft | **8** | Strong pairing, real range, both round-1 typographic defects fixed. Docked: the bio timeline substitutes a `·` in the year column for undated entries, which reads as a slightly awkward stand-in next to 1993/1996/2002. |
| 4 | Colour & contrast | **9** | 0 failures across 56 computed pairs including hover and focus. Tightest passing pair 6.07:1 against a 4.5 requirement — real headroom, not a squeaker. |
| 5 | Spacing rhythm | **8** | Consistent band scale, generous. Docked for the `contact` empty column and the two very large placeholder voids (portrait, map) that currently read as holes. |
| 6 | Background / depth | **8** | Triple radial on the dark grounds + feTurbulence grain + three animated god rays anchored to the hero photo's windows. Not a flat rectangle. |
| 7 | Imagery quality | **9** | Both images pass both halves of the two-way test; honest wear, no fabricated branding, one register. |
| 8 | Responsiveness | **8** | All targets ≥44px, zero overflow, genuine phone layout decisions including the new media-first order swap. |
| 9 | Motion polish | **8** | Nameable, restrained, reduced-motion-safe, divergent from recent builds, now with four independent un-hide guards. Docked: an opacity entrance is inherently the most fragile family and is why the at-rest measurement needs an exception at all. |
| 10 | Cohesion | **9** | Reads as one art director across four pages. |

**Gate: boldness ≥ 8 → PASS (8). No dimension below 7 → PASS (lowest is 8).**

### Boldness — the honest read the lead asked for

**It holds, but it is carried entirely by structure and type, and the palette is now working
against it rather than for it.**

Blue-and-gold **is** the legal category default, and "TOO VANILLA" was Paul's own complaint about
his current site (Q7). The plan's own Stage 5 rejected Direction 2 in these words: *"it is the
tasteful version of exactly the navy-gold category default — Q7 ('too vanilla') argues against
picking it."* The build now wears close to that palette while keeping Direction 1's structure.
Harry chose it, that is settled, and it is **not** scored as a deviation — but it means the
palette has stopped contributing distinctiveness and the structure has to carry the whole load.

What actually carries it, verified in the screenshots:
- **The dark-first inversion.** A full-bleed photographic courtroom hero with the headline set
  *over* the image in 900-weight Frank Ruhl. Most firms in this category run a light page with a
  navy header, or a portrait hero. This does neither.
- **Real numerals as the loudest event.** `May 2002` / `90%` / `4` / `3` at 84px, `1996` at 80px,
  and a **973-344-0808 set at 84px in gold on deep azul** as a whole section. Committing a full
  band to the phone number is a genuine and memorable decision.
- **Format variety with real range**, strongest on `practice-areas`: split → card-grid → numbered
  steps → split, alternating dark and light, with a rotated side-label and a gold circled ③.

What keeps it off 9:
- The homepage's middle third — the 2×2 practice card grid, "Where we work", "Born and raised
  here" — is conventional and quiet.
- There is **no true symmetry break**. Every band is full-width with content on the same left
  margin. The plan deliberately elected scale contrast *as* the symmetry break, which is a
  legitimate locked call, but the result is a page that is bold in type and calm in composition.
  An overlap, a dominant column, or an off-grid offset on the homepage would have made this a 9.

Round 1 scored boldness **9** against the green build, where the palette itself was doing
distinctiveness work. That work is gone, so the score moves to 8. It clears the bar; it is no
longer comfortably clear of it.

---

## Fixes applied this round (by me — see the independence caveat)

1. **`<h1>` outranked by its own `<h2>`s on `attorney-bio` and `contact` — round-1 fix 2 had NOT
   landed.** `RESUME-HERE.md` recorded it done on the strength of "`.pagehead h1` … 3 occurrences",
   but those three are the base rule plus its two responsive steps, not three pages. The rule only
   ever applied to `practice-areas`, which was already correct at 56px. On the other two the h1
   sits in a `.split`, matched no rule, and rendered at the **34px** UA default beneath 44px `h2`s.
   *Fix:* a base `h1 { font-size: 3.5rem; font-weight: 900 }` floor plus responsive steps at 1080
   and 860, which `.hero h1` and `.pagehead h1` still override. Verified: 64/56/56/56px vs 44px.

2. **`main.js` — a stalled IntersectionObserver permanently hid 56–85% of every page.** The
   builder's round-1 fix correctly covered *throws*, but not *stalls*. If `IntersectionObserver`
   exists and accepts `observe()` but never delivers a callback (stubbed by an extension, disabled,
   or a browser bug), nothing throws, so the `catch` never runs — and `motionOK()` has already
   stood the dead-man timer down. Measured before the fix, after scrolling the entire page:
   **index 75%, practice-areas 71%, attorney-bio 85%, contact 56%** permanently hidden, with
   `973-344-0808` and `Paul Da Silva` among the hidden samples. Scrolling did not help.
   *Fix:* an `observerDelivered` flag set in the callback, plus a 2s backstop that calls
   `motionOff()` if no callback ever arrives. Verified: **0% on all four pages.**

3. **Attorney-advertising disclaimer — the lead's ruling, implemented.** Added the labeled
   placeholder to the footer on all four pages, the same device the frozen Rev 3 used on this
   client: `[Standard attorney-advertising / no-attorney-client-relationship disclaimer — for
   Paul's review]`, in a dashed frame so nobody mistakes it for shipped legal copy, with an HTML
   comment explaining why the value is Paul's to supply. Verified: renders on all 4 pages at
   **9.11:1**, no overflow at 375. Both copy gates still exit 0 (the placeholder-string check
   does not fire on it).

4. **Mobile bio opened with an empty box instead of its own title.** Stacked, the media-first
   split put the portrait placeholder first, so the entire first phone screen was empty hatched
   frame and "Paul Da Silva" sat below the fold. *Fix:* a `.split-media-first` order swap inside
   the existing stacking breakpoint — the name leads, the frame follows. Desktop (≥1080) unchanged.

**Not changed, and why — with a correction.** My first `grep` returned a
`.btn-header-label { display: none }` rule at ≤420px; minutes later the same grep returned nothing
and the CSSOM confirmed the rule was absent. I initially attributed that to a stale shell-wrapper
result. **The lead's later report gives the real explanation: the builder was still writing during
my audit and removed that rule mid-session**, replacing it with `.site-header .btn-sm { gap: 0.25rem }`.
So the rule was real when I first read it, and the amputated **"the office"** button was a real
defect — it was simply fixed by the builder rather than by me. Recorded here because it means the
early part of this audit ran against a moving target; every measurement in this file was re-taken
after my own edits, which are the newest changes on disk.

**Verified after the fact (the lead's requested widths):** the header CTA renders as one whole
phrase, `"Call the office"`, at **414 / 390 / 375 / 360 / 320px** — a real `tel:+19733440808` link,
44px tall, **no overflow at any width** (at 320 it wraps to two lines at 66.7px, still contained and
still a valid tap target). No amputation anywhere.

**Builder's `.steps-head` fix — independently confirmed at the widths that matter.** The lead asked
for 1024 specifically, since that is where the first attempt still overlapped:

| Width | `attorney-bio` "1996" | `practice-areas` "③" |
|---|---|---|
| 1440 | clear **+25.6px** | clear +25.6px |
| 1280 | clear **+25.6px** | clear +25.6px |
| **1024** | clear **+25.6px** | clear +25.6px |
| 900 | clear **+25.6px** | clear +25.6px |
| 861 | clear **+25.6px** | clear +25.6px |
| 860 and below | stacked (no row conflict) | stacked |

`minmax(6.5rem, max-content)` sizes the column to the glyphs, so the clearance is exactly the 1.6rem
grid gap at every width — it cannot regress with font size. `practice-areas`' single-glyph ③ still
clamps to the 6.5rem floor, so its alignment is unchanged. Confirmed fixed.

---

## Hard gates — detail

**Content parity — PASS, 21/21 carried.** Re-verified against the current build, with particular
attention to the fold the Planner warned about (aggravated assault into "Violent crimes and
weapons"): every offence from `site-content.md` is present — murder, manslaughter, robbery,
burglary, assault **and aggravated assault**, firearms; the four drug categories (possession,
distribution, trafficking, prescription); the four sex-offence items. Also confirmed: all 5 traffic
violations, all 4 real-estate sub-services plus the leases/co-op/condo line, all 7 matrimonial
items, the driving-privileges administrative process, all 5 prior employers, all 4 recognition
credentials, the personal line, the language line. The 4 deliberately-dropped blocks are on the
plan's list with reasons. The lead's NAP dedup removed **repetition**, not facts — the address is
still on every page (footer NAP) and twice on `contact` (NAP list + footer).

**Client-answer fidelity — PASS.** His numbering ①②③④ drives card order, page order and anchor
names. "Municipal Court" leads; "Matrimonial Law" replaces "Family Law"; Real Estate sits above
Matrimonial. Two-tier service area published as regions with no invented town list. Phone is the
sitewide primary CTA. Verified in the **rendered DOM**, not by grep: zero testimonials, zero FAQ,
zero fees/rates/retainers, zero specials or free consultation, zero bar admissions, zero `mailto:`,
zero published hours — **and absent from the JSON-LD too**, not placeholdered. Language line
byte-exact, no accents added, exactly once per page. Firm name `DaSilva & Associates, LLC` sitewide
with **zero** occurrences of the spaced "Da Silva &" form.

**Contact-a-business rules — PASS.** Paul's cell is absent from all four rendered pages. **All 13
`tel:` hrefs are `tel:+19733440808`, and every one digit-matches the number rendered beside it** —
checked by extracting digits from both the `href` and the painted link text and comparing:
**zero mismatches**. No invented licence number, insurance line, award, rating, year or credential.

**Real reviews only — PASS.** No testimonial section exists. The one quoted block is Paul's own Q1
answer, first-person, attributed "— Paul Da Silva", which the voice spec authorises as the single
lyrical block. The three real Lawyer.com reviews are correctly absent (Q12 does not authorise them).
`aitells.py` flags that block as "a review block carrying no name" — that is its heuristic
misreading a first-person owner quote, not a finding.

**Copy voice — PASS.** Both scripts exit 0 on all four pages. I read **every visible string on all
four pages** against the driveway test — 50 strings on `index` alone, one at a time, not a spot
check. Nothing poetic, nothing cute, no puns, no promise without content. It sounds like a lawyer
explaining: *"If you're not sure it's something Paul handles, call and ask."* · *"Final figures,
the deed, and the keys."* · *"The aim is to reduce or dismiss the charge and keep points off the
license."* · *"Name, phone, and a few lines about what happened. If it's urgent, don't use the
form."* Thin-fact sections are short rather than padded, per the voice spec — the personal line is
one sentence, each recognition card is the credential plus one line. Shared blocks are page-agnostic
and name nothing page-specific. No year drift: 2026 copyright, May 2002 founding, 1993/1996/2002
timeline all consistent. **The independent cold read was not dispatched** — see the caveat at the
top.

**Mobile tap-to-call — PASS as a deviation, with a recommendation for Harry.**
The lead's dedup relabelled the sticky header CTA to "Call the office", so **the phone number no
longer appears anywhere in the header**. `local-trade.md` asks for a *visible* tap-to-call in the
mobile header. Harry's "repetition is not acceptable" instruction drives this, so it is **not scored
as a failure**. But the lead asked whether a phone visitor can still reach the number fast enough,
so here is the measurement rather than an opinion — at 375×812, distance to the first `tel:` link
that actually **shows digits**:

| Page | Above the fold | First `tel:` link showing digits |
|---|---|---|
| `index` | "Call the office" + **"Call 973-344-0808"** | y=490px — **above the fold** |
| `contact` | "Call the office" + **"973-344-0808"** | y=223px — **above the fold** |
| `practice-areas` | "Call the office" only | y=**4114px** — **5.1 screens down** |
| `attorney-bio` | "Call the office" only | y=**3635px** — **4.5 screens down** |

**My read: fast enough to act, not fast enough to trust.** The *affordance* is above the fold on all
four pages and it works — tapping "Call the office" opens the dialer with the right number, and for
someone in a hurry that is arguably better than reading digits. Nothing is broken and no one is
stranded. But on the two interior content pages the actual number is invisible for four to five
screens, and digits do work the affordance cannot: writing it down, calling from a different phone,
long-pressing to copy, and simply *seeing a real local 973 number* as a trust cue. On a criminal-
defense site the visitor may be on a borrowed or nearly-dead phone.

**Recommendation to Harry (not a build fix, and I have not made it):** leave the header as "Call the
office" — it is his call, it reads well, and on `index` and `contact` the digits are already above
the fold, so putting them back in the header is exactly the repetition he objected to. Instead add
the number **once, high up, on `practice-areas` and `attorney-bio` only** — the two pages where it
is 4–5 screens away. That closes the real gap without reintroducing repetition anywhere he saw it.

**Logo — PASS.** Real logo, `assets/logo.png` 1888×706, local `src` in header and footer on all four
pages, `alt="DaSilva & Associates, LLC logo"`. Not hotlinked, not redrawn, not substituted.

**Imagery — PASS.** Opened at full size and judged by eye. **After Amendment A only one generated
image ships** (the hero); the second slot now carries the client's own photograph.
- `hero-courtroom.webp` 2000×1116, 94 KB. Empty panelled courtroom, counsel table, leather
  portfolio, blank legal pad, green-cushioned chair. Panel joints, window mullions, bench rails and
  table edges all hold straight; no melted or duplicated detail; no faces. **No readable signage,
  lettering, plate or business name anywhere in frame.** Saved from the "too perfect" tell by honest
  wear — scratched tabletop, scuffed floorboards. Alt "Counsel table in a courtroom" claims nothing
  about which court.
- ~~`newark-street.webp`~~ — **superseded by Amendment A.** It passed the two-way test as shipped
  (blank awnings, no invented business name, honest cracked asphalt), but it has been **deleted** and
  replaced by `office-exterior.webp`, the client's real photograph of his real office. Judgement of a
  real photograph is not the two-way test — that test asks whether a generated image would be
  believed; this one *is* the building. See Amendment A.
- **One register sitewide:** available-light documentary. Neither reads as a stock ad; neither
  reads as shabby. Both pass both halves of the two-way test.
- The bio portrait is a labeled placeholder frame, **never a generated face** (Q11). The
  municipal-court slot and the map are labeled placeholders. `og-image.webp` is a verified crop.

**Streetscape adjacency — MOOT, resolved by Amendment A.** This finding existed only because the
image was a *generated* street that the layout could imply was his building. The slot now holds a
real photograph of the real office, so the concern is void and the address has been restored as a
caption. See Amendment A.

**Video — N/A.** Plan marks no `VIDEO` slot; no `<video>` element on any page. Correct default, no
deduction.

**Release form — PASS.** `release-form.pdf` present, valid PDF, **one page**. `release-form.html`
has **zero** surviving `{{` tokens. Client/Business `DaSilva & Associates, LLC`, Contact Name
`Paul Da Silva`, Pages Included `Home · Practice Areas · Attorney Bio · Contact` — **matches the
four pages actually built**. Domain `pauldasilvalaw.com` traces to his own answers (header +
Q17), so it is not invented. Preview Link ships blank. Signature, date and acknowledgement
checkboxes blank.

**Click test — PASS.** Driven programmatically across all four pages. **60 links total, 0 broken** —
every `href` resolves to a real file, and every cross-page `#fragment` was opened on its target page
and confirmed to match a real `id`. Hamburger opens **and** closes on **every** page with
`aria-expanded` tracking (`false/none → true/flex → false/none`). Form submit reveals the inline
demo confirmation. **Zero dead clicks. Zero misleading affordances** — no non-interactive element
anywhere carries `cursor:pointer`, and the practice cards are wrapped `<a>` so the whole card is the
target. Contact form is **4 fields**, phone-first in the copy.

**JS-off — PASS**, with screenshot proof saved to `screenshots/nojs-index.png` and
`nojs-contact.png`: every word readable, hero intact, gold CTA tappable, nav present.

**Screenshot currency, and a note on the capture hang.** All **14** shots (12 + 2 JS-off proofs)
post-date every source file — verified by mtime: newest source `style.css` **18:06:19**, oldest shot
**18:06:56**. They are current for this audit and were taken after every edit, including the last one.
Separately: the lead warned that `captureBeyondViewport` hangs indefinitely (>9 min) on this build
because of the hero's `filter: blur(14px)` god rays, and supplied a tiling harness. **That did not
reproduce here.** Driving system Chrome through `puppeteer-core` with
`page.screenshot({ fullPage: true })` completed all 12 shots in well under a minute, twice, after
riding the page so every IO reveal fired. Worth recording, because the tiling workaround costs real
time and the hang appears specific to the other harness rather than to the build.

**Distinctiveness — PASS, no escalation.** Re-run against the azul+gold build as instructed, off the
fresh screenshots, comparing the last 3 `design-memory` rows (`fora-digital`, `paul-da-silva-law`
Rev 3, `gee-kay-landscaping` Rev 2).

- **vs frozen Rev 3 (the narrowed axis).** The lead is right that brass and gold are the same
  metal-accent family, so the palette axis is now **PARTIAL**. But the two heroes are structurally
  opposite and unmistakable at a glance: Rev 3 is **light-first** — a porcelain ground, a pure
  *type* hero in ink Libre Caslon with no image behind it, a brass hairline under the header, brass
  demoted to a button and a rule, photography relegated to a band *below* the fold. This is
  **dark-first** — a full-bleed photographic band with the headline set *over* the image in
  900-weight Frank Ruhl, gold working as a live accent across the whole page, zero rule-work.
  Opposite ground, opposite hero archetype, opposite role for the metal. **Not siblings.**
- **vs `gee-kay` Rev 2 (the numerals worry).** Both use oversized numerals as a hierarchy engine,
  but that is one widespread pattern executed differently: `gee-kay` is a light plan-paper
  two-column hero on a surveyor tick-field, thin Newsreader, spruce numerals, framed placeholder
  plate, orange CTA. DaSilva is a dark photographic band, 900-weight serif, gold-and-azul numerals,
  god rays. Section rhythm, imagery register and motion vocabulary all differ. **Not siblings.**
- **Motion vocabulary** compared concretely against the logged tokens: blur-focus + icon-nudge here
  vs mask-curtain + ink-sweep (`fora`), rules-draw-in + weight-shift (Rev 3), slide-alternate +
  rule-trace edge-lift (`gee-kay`). No overlap.

**Bold test (redesign) — PASS.** Against Paul's live WordPress site and separately against our own
frozen Rev 3: unmistakably different at a glance.

---

## Documented exceptions (recorded, not failed)

1. **At-rest fail-visible 23–72%** — opacity-based blur-focus entrance, the Planner's locked Stage 5
   signature move. All six degraded/complete paths measure 0%. Full reasoning above.
2. **Placeholder labels read `Photo slot: …`** rather than the playbook's literal `AI-IMAGE — …`,
   because `copycheck.py`'s placeholder gate flags that string in visible copy. The machine-readable
   `<!-- AI-IMAGE: … -->` comments are present and accurate on both slots.
3. **The practice-areas lede carries Paul's own published outcome claim** — *"…which often gets a
   good result without the expense of needless additional litigation costs."* His sentence, mapped
   there by plan §7, and the tightening actually weakens it. Ships as-is; **Harry asks Paul before
   launch**, because NJ attorney-advertising rules are strict about outcome language. Not a build
   fix. This is exactly why exception-and-fix 3 (the disclaimer placeholder) matters.
4. **Independent cold read not dispatched**; say-aloud read done in full instead. See the caveat.
5. **Four fixes applied and judged by the same party.** See the caveat.

---

## Still open for Harry — not build defects

- **A real photo of the office.** Still not on disk. When it arrives, the standing recommendation is
  to replace the generated `newark-street.webp` in the Home service-area section — that retires a
  compromise rather than filling a gap, and lets the address line move back beside it. Real signage
  in a real photo is an asset; the no-signage rule applies only to generated images.
- **A real headshot.** The bio portrait is a labeled placeholder and currently reads as a large void
  on both desktop and mobile. It is honest and correct (never generate his face) but it is the
  single biggest visual improvement available on this site.
- **The phone number on the two interior pages.** Consequence of the header dedup: on
  `practice-areas` and `attorney-bio` the digits are 4–5 screens down. Measurement, reasoning and
  the minimal fix are under "Mobile tap-to-call" above. Harry's call, not a build defect.
- **The outcome-claim question**, paired with the disclaimer wording, as one ask to Paul.
- The 10 items already on the `client-answers.md` Confirm list (email, hours, bar admissions,
  reviews, service-area wording, the language-line spelling, FAQ, domain/DNS).

---

**Round 2 verdict: PASS.** $10K **8/8**; rubric **boldness 8**, no dimension below 8; detector
0/0 exit 0 with zero waivers; both copy gates exit 0; contrast 0 failures across 56 pairs; all
composition checks pass; distinctiveness clears against all three recent rows.

**Signed off — the mockup is FROZEN.** `design-memory.md` row appended, recording the accent as it
actually ships (azul + gold). The lead still owes `/design-push` on
`prospects/dasilva-associates/mockup/`.

**Not yet due:** delivery to Corey. That needs a *signed* `release-form.pdf` back from Paul — a hard
gate, and an AI sign-off is not the client's permission to publish.

---

# Amendment A — the real office photograph (2026-08-03, post-sign-off)

**Lead-directed asset swap on Harry's explicit instruction** ("I also added the image of the office
to assets, use it on the site"). Not a finding against the build, and it does not open a round 3.
**Re-verification turned up nothing; the sign-off stands.**

## What changed

| | Before | After |
|---|---|---|
| Home service-area image | `newark-street.webp` — **generated**, 1100×821, 186 KB | `office-exterior.webp` — **real photograph of the real building**, 1098×787, 179 KB |
| Alt text | "Newark neighborhood street in early morning light" | "DaSilva & Associates law office at 385 Lafayette Street, Newark" |
| Address in this section | removed (a generated street must not imply it was his building) | **restored as a caption** — "The office at 385 Lafayette Street in Newark." |

Source: `prospects/paul-da-silva-law/mockup/assets/5A-DASILVA-EXTERIOR-8IN-MR-ADJ-SH_8824-1536x1024.jpg`,
1536×1024. **Copied out read-only; the original was not modified, moved or deleted, and nothing else
in that frozen folder was touched.** `newark-street.webp` deleted after confirming zero remaining
references anywhere in the build.

**This retires a compromise rather than filling a gap.** The generated streetscape was an invented
block that needed careful captioning *precisely because* it was not his building. That objection is
now void, which is why the address could come back.

## Two judgment calls I made — flag either if you disagree

1. **I cropped the photograph.** Uncropped at the slot's real 549px width, roughly 40% of the frame
   was the neighbour's siding and a tree, and **his sign was too small to read** — which defeats the
   point of using it. I cropped to `(340, 30) → (1470, 840)` of the original: drops most of the left
   neighbour and the far-right house, **keeps** the roof peak, the portico, the front steps, the "3"
   street number and the birch as a framing element. Ratio 1.40 (the previous slot image was 1.34, so
   section proportions barely move). **Nothing was retouched** — no content altered, no cloning, and
   the sign is untouched. If you'd rather ship the photographer's full frame, say so and I'll swap it
   back in one step.
2. **I added the caption rather than putting the address in the body copy.** The photograph carried
   no visible label, so a visitor could not tell whose building it was. A caption labels the image
   without introducing a third competing fact into a section whose heading is "Where we work" and
   whose job is the two-tier service area. Set quiet, in `--ink-dim` at 14px, as a proper
   `<figure>` / `<figcaption>`.

**Address dedup ceiling respected.** Visible (non-meta, non-comment) "385 Lafayette" occurrences per
page: **index 2** (caption + footer NAP — at the ceiling, not over), practice-areas 1,
attorney-bio 1, contact 2. All within Harry's limit of 2.

## The things specific to this photo

- **The sign reads "Da Silva & Associates" — with a space.** We build as **DaSilva** (his logo wins).
  I did **not** retouch the photo and did **not** change our spelling. His own branding is now known
  to be inconsistent in three places: the logo says *DaSilva*, the building sign and the old site's
  footer say *Da Silva*. **Confirm item 1 in `client-answers.md` has been strengthened accordingly**
  — this is a real question worth asking, not a formality, because the sign is the most permanent of
  the three.
- **The no-readable-signage rule does NOT apply here, and a future reader should not flag it.** That
  rule exists to stop *generated* images inventing fake or competitor branding. This is a real
  photograph of his own real sign, so legible real signage is an **asset**. An HTML comment saying so
  sits next to the `<img>` in `index.html`.
- **The sign carries `973-344-0808`.** It is pixels, not text, so it does not affect the visible-count
  dedup, and it creates no *visual* impression of repetition where it sits: the nearest other phone
  number on the page is the CTA band, a full section away, and the sign's number is small enough at
  549px to read as part of the building rather than as a second callout.
- **Register — one honest widening, and it holds.** The hero is a dim, warm, available-light interior;
  this is a bright exterior under a blue sky, so the register is wider than the generated
  golden-hour street it replaced. Judged on the assembled page it reads as one body of work: both are
  documentary, available-light, un-styled, and they sit a full section apart. The blue sky also
  happens to sit naturally with the azul palette. **A real photograph of the real business outranks
  register purity** — this is the client's own content, which is the whole pitch.

## Re-verification (run in full, not a rubber stamp)

| Gate | Result |
|---|---|
| `detect.mjs`, 4/4 pages | **PASS** — 0 errors, 0 advisory, exit 0, **0 waivers** |
| `copycheck.py`, 4/4 pages | **PASS** — exit 0 |
| `aitells.py`, 4/4 pages | **PASS** — exit 0 |
| Contrast, computed, all 4 pages | **PASS** — **0 failures / 56 pairs**. New `figcaption` is `--ink-dim` on `--paper` = **6.80:1** |
| Falsifiable facts, `index` | **6 → 7** (the caption adds a checkable address) |
| Horizontal overflow @375 | **PASS** — none on any page |
| Tap targets @375 coarse | **PASS** — 0 under 44px |
| Fail-visible, `main.js` 404 | **PASS** — 0% on all 4 |
| Fail-visible, throws line 1 | **PASS** — 0% on all 4 |
| Fail-visible, IO never fires | **PASS** — 0% on all 4 |
| Ripple check — `.split-media` CSS | **PASS** — the class exists only on `index`. `attorney-bio`'s `split-media-first` is a **different class token** and does not match `.split-media`; verified no layout change on the other three pages |
| Page weight | **613 KB** total (was 652 KB) — the real photo is *smaller* than the generated one it replaced |
| Screenshots | **All 14 re-shot**, `revealsNotIn: 0` on every capture. Newest source 18:28:55 vs oldest shot 19:18:54 — **all post-date all source** |

**Scores unchanged. $10K 8/8; rubric boldness 8, no dimension below 8.** If anything, imagery (dim 7)
is now stronger in kind rather than degree — one of the two image slots is no longer generated at all,
it is the client's own photograph of his own building, which is the most honest asset on the site.

**Paid calls this prospect: still 2 (~$0.10), and now only ONE generated image ships** — the
courtroom hero. `og-image.webp` remains a crop of it. The generated streetscape has been deleted.
No new generations; the cap is spent and untouched.
