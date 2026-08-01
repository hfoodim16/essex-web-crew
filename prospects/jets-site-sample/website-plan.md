# Website plan — New York Jets (jets-site-sample)

SAMPLE build (internal demonstration). Planned from `client-answers.md` (top authority)
via web-design-ultra Stages 1–5. No dossier, no site-content.md — the client reported no
current website, so **the content-parity chain does not apply**; every fact on the site
comes from the answers, everything else is a labeled placeholder. Copy contract:
`voice-spec.md` (read it before writing any visible string).

---

## 1. Art direction — "Gameday Broadcast"

Dark stadium-night green as the ground, chalk white as the voice, poster-scale condensed
type doing the work photography can't (most slots ship as placeholders). The register is
a franchise's own broadcast package — floodlights, turf, yard-line chalk — which answers
the client's three words directly: *professional* (composed, restrained, organizational),
*athletic* (velocity in the type and motion), *large* (display type at poster scale,
full-bleed bands). It is also the first dark-first build since anthonys-landscaping and
shares nothing with the last three design-memory rows.

## 2. Typography

- **Display: Big Shoulders** (Google Fonts, variable) — uppercase, weights 600–800,
  tight tracking, used for all headlines, the giant "1969" numerals, and
  ticket-package titles. (No text wordmark — the real logo is on disk; see §5.1.) Condensed and athletic without being the Barlow-Condensed
  sports default the Stage 2 engine suggested (deliberately diverged).
- **Body: Chivo** (Google Fonts) — 400/700, sentence case, all body copy, captions, nav.
- Not banned (no Inter/Roboto/Arial/Helvetica/Fraunces/Instrument Serif/Geist/Plus
  Jakarta/Space Grotesk) and distinct from the last 3 rows (Zilla Slab/Work Sans,
  Instrument Serif/Hanken Grotesk, Libre Caslon Text/Albert Sans, and the superseded
  Besley/Schibsted Grotesk).

## 3. Color system (CSS `:root` tokens)

**Client-locked constraint (Q18): "Our team colors are green and white."** The whole
system is built inside that instruction — this outranks any detector palette rule.

| Token | Hex | Role |
|---|---|---|
| `--night` | `#0A1F14` | page ground (deep stadium-night green-black) |
| `--pine` | `#14472F` | panel/card ground, footer |
| `--turf` | `#1F7A4D` | the ONE accent — hover states, live details, hairline moments |
| `--chalk` | `#F4F7F3` | text, primary CTA ground (white button, `--night` label) |
| `--hairline` | `rgba(244,247,243,.16)` | rules and borders |

One theme: dark-first on every section (no light/dark alternation — composition lock).
Text is always `--chalk` on `--night`/`--pine` (AA passes); `--turf` is never body-text
color, only large type, fills, and interactive states. Primary CTA: `--chalk` ground +
`--night` label — the loudest thing on a dark page.

**Color-convention call:** the convention for a sports franchise is "team colors, loud."
All three directions honor it — the client locked green/white, so the honor/break axis
here is *deployment* (dark-first vs light-first), not hue. This direction deploys dark.
The Stage 2 engine's category palette (team red + championship gold) was discarded —
overridden by the client's locked colors.

## 4. The three divergent directions (Stage 5) and the pick

**A — "Gameday Broadcast" (PICKED).** Dark stadium-night ground · Big Shoulders/Chivo ·
poster-scale type-led stack · skew-slide entrances + in-frame zoom-crop hovers + one
"1969" scroll scrub · full-bleed cinematic stadium imagery · floodlight-wash atmosphere.
Honors team colors, dark deployment.

**B — "The Gameday Program."** Light-first: chalk ground, green ink — a printed
game-day program as archetype (numbered sections, heavy rules, heritage-forward).
DM Serif Display / Archivo. Line-draw underlines + slide-alternate entrances. Contained
plates instead of full-bleed. Honors team colors, white deployment. Rejected: reads
adjacent to the crew's recent editorial/ledger builds (gee-kay, paul-da-silva) even with
different tokens — weakest divergence.

**C — "Turf Signal."** Split Swiss-poster blocking: hard-edged alternating white/green
panels, diagonal cut lines, variable-width type (Anybody / Red Hat Text), scale-settle
entrances + icon-nudge hovers, typographic-first (almost no photography). Honors team
colors, 50/50 deployment. Rejected: strong, but "large" without the imagery register the
client's Q5 asks for ("showcase our players"), and the diagonal-energy look undercuts
"professional."

The three differ on ≥3 of the 5 axes (ground, type, layout archetype, motion, imagery
deployment). **A is the boldest**: full commitment to "large" (poster type, full-bleed
bands), the only dark-first option, and the furthest from the last three logged builds.

**Stage 4 — combos avoided** (last 3 rows of `design-memory.md`): fonts as listed in §2;
palette families warm-editorial-paper+cobalt, porcelain-ink-brass, natural-bark/moss/
hi-vis-lime (this build's dark franchise-green monochrome matches none — anthonys'
dark-evergreen+brass is 4 rows back and outside the ban window, and this system carries
no brass/ivory, no luxury register); layout archetypes gallery-wall, modular ruled
ledger, canopy-descent, split-screen advocacy (this is a poster-scale type-led stack);
motion mask-curtain + ink-sweep + pointer field (fora), rules-draw-in + weight-shift +
sticky rail (PDS R3), clip-wipe + lift/tilt + parallax (PDS R2) — none reused.

**Stage 3 evidence sheet** (patterns extracted, nothing copied):
- **Awwwards sports collection** (Williams GP Tech, Audi F1, King James): oversized
  display type as the structural element; full-screen hero + vertical scroll narrative;
  team-color high contrast on dark grounds. → validates poster-scale type-led stack.
- **Juventus.com**: heritage as *structural* content ("Since 1897" as a section, not a
  footnote); tickets as a dedicated module with plain CTAs; restrained two-color
  franchise palette with photography carrying the richness. → validates the heritage
  band + tickets-as-services section.
- **landonorris.com** (Awwwards SOTY): one accent color punctuating a dark neutral
  ground; oversized headlines as section anchors; strategic line breaks fragmenting
  display type. → validates the single-accent discipline (`--turf`) and headline scale.

## 5. Page map

**Single-file SPA** — `index.html` only (thin facts = one page; the content grows the
map, and there isn't content for more). Sections top to bottom:

1. **Header/nav** — the REAL Jets logo, top-left: `assets/ny-jets-logo.svg` (already
   on disk — real file, served local, never hotlinked, never redrawn or restyled),
   `alt="New York Jets logo"`, wrapped in a link to the top of the page.
   **Guaranteed background:** the mark is `#115740` green + white interior, designed
   for a light ground — directly on `--night` it goes muddy. So the logo sits on a
   sharp-cornered `--chalk` plate (its designed ground) inside the otherwise dark
   header chrome, header and footer both; it never sits on `--night`/`--pine` bare.
   Lead-approved exception to the trademark caution (internal sample — Harry's call,
   recorded in client-answers.md note 4). Nav: Tickets · Story · Players · Charity ·
   Contact. Persistent **Get Tickets** button right side, and in the mobile header (the
   tap-to-call slot — see §9 exception). Height ≤ 80px, one line.
2. **Hero** — full-bleed GENERATE image (§8), ≤4 text elements: headline (from the
   voice-spec bank, e.g. "Green and white, wherever the fans are."), subhead ≤25 words,
   one CTA (Get Tickets). No trust strip inside the hero.
3. **Trust strip** (under hero, its own band): `Super Bowl winner, 1969 · 56 years of
   football · Green & White` — real facts only, no invented license/rating analogs.
4. **Tickets** (the services section) — three typographic package tiles on `--pine`:
   **Pre-season** / **3-Game Package** / **Full Season** (grid = 3 cells, 3 items), each
   ≤20 words + Get Tickets CTA (bottom-aligned across the row). One highlight bar
   beneath: free training-camp access for ticket holders (Q8, as given). Support line
   may name Ticketmaster and StubHub (Q7). **No prices, no dates, no seat maps.**
5. **Heritage band — the set-piece** — full-bleed GENERATE turf image (§8) under a
   `--night` scrim; giant "1969" numerals in Big Shoulders 800 (the scroll scrub, §7)
   + "Super Bowl winner" line + the 56-years story lede.
6. **Story / owner block** — `--pine` panel, two short paragraphs (≤90 words total,
   voice-spec budget) + the ONE lyrical block: the owner's verbatim Q2/Q3 quote,
   attributed "— Team Owner, New York Jets" (`<!-- attribution name: Harry to supply —
   client gave none; do not invent -->`).
7. **Players showcase** — intro ≤20 words + three 3:4 placeholder tiles, each labeled
   `[Player photo + name — supplied by the club]`. NO invented names, numbers, or
   positions. Tiles are non-interactive — no hover cue.
8. **Charity** — split section (the page's only image+text split): one 4:3 placeholder +
   intro ≤20 words + `[Charity program details go here — supplied by the club]`.
9. **Inside the club** — two 16:9 placeholders side by side: locker room, training
   facility (Q21 — these photos don't exist yet; captions ≤12 words say so plainly).
10. **Wherever the fans are** — a short full-width typographic band built on the
    client's Q4 phrase. This is the service-area analog; see §9 exception (no towns).
11. **CTA band** — Get Tickets, large, ≤15 words of support copy.
12. **Footer** — the real logo on a small `--chalk` plate (same rule as the header),
    nav repeat, Get Tickets, NAP placeholder block
    (`PLACEHOLDER_TICKET_LINE` · `PLACEHOLDER_TICKET_EMAIL` — NO address, per Q26),
    privacy/terms placeholder links. Matches JSON-LD tokens exactly.

**Cut, deliberately (thin facts — voice-spec authority):** FAQ (Q27 blank), testimonials
(Q22 blank — no invented praise; the layout doesn't need an empty-review block), specials
(Q11 blank), any schedule/roster/news module (churning content, none supplied, and our
static model excludes it).

Composition sanity (planned to pass Stage 8): 1 split section total (zigzag cap ok),
≥4 layout families (full-bleed hero / strip / 3-tile grid / full-bleed band / quote
panel / portrait grid / split / typographic band), 0 marquees, eyebrows ≤ 3 (hero counts
one), grid cells == item counts everywhere, one theme, one accent, one radius system
(all-sharp — athletic), no decorative page furniture (no scroll cues, no word strips,
no tile pagination).

## 6. Hero direction

Headline from the verbatim bank, 3–8 words, obeying `voice-spec.md` — recommended:
**"Green and white, wherever the fans are."** (client's own Q18 + Q4 words; checked
against all existing prospect heroes — no triad, no "Built…", no "Since <year>", no
"Your dream…"). Subhead ≤25 words carrying only real facts (56 years, season-ticket
families). One CTA: **Get Tickets** → `PLACEHOLDER_TICKET_URL`. Image intent: §8 slot 1.

## 7. Signature motion (Builder implements exactly — do not re-decide)

- **Entrance family: skew-slide** — elements enter translated on X with a skew that
  unwinds to zero (reads as velocity; the athletic register's native move). Applied
  consistently to all reveals, `.js`-scoped per motion.md rule 0.
- **Hover personality: in-frame shift (zoom-crop language)** — everything moves *inside*
  its hard frame: images/placeholder plates scale 1.05 within overflow-hidden frames,
  the CTA label + arrow nudge inside the button, nav links get a `--turf` color snap.
  **Nothing lifts, nothing tilts.** Plus the universal pressed state
  (`:active{transform:scale(.97)}`) on all clickables.
- **Scroll set-piece (the one): "1969 resolve"** — the heritage band's giant numerals
  scrub from `scale(1.12)` + widened letter-spacing to set position via CSS
  `animation-timeline: view()` inside `@supports` (no support → renders static). Note:
  same *mechanism* as fora-digital's gallery-hang but a different move on a different
  element; the moves themselves (entrance + hover) are what the ban list keys on, and
  neither is reused.
- **Tempo:** entrances 600ms `cubic-bezier(.16,1,.3,1)`, stagger 70ms (cap ≤12 items),
  hovers 200ms. One ease everywhere.
- **GSAP tier: 0 — pure CSS + IO.** No vendored library; bytes go to the two photographs.
- **Avoided (last 3 rows):** mask-curtain, ink-sweep/underline-draw/fill-sweep, pointer
  vector field (fora); rules-draw-in, weight-shift, sticky progress rail (PDS R3);
  clip-wipe, lift/tilt, parallax (PDS R2); and the fade-up/count-up defaults.
- **Background & atmosphere:** "floodlight" treatment from the skill's free recipes —
  layered radial gradients (two cool-white floodlight washes bleeding from the top
  corners over `--night`), fine grain overlay, soft vertical vignette grounding each
  band. ONE ambient effect: a very slow floodlight shimmer (opacity breathe on the
  washes, 14s sine), reduced-motion gated. No reactive field — wrong register for a
  fan-facing club site, and it would displace the set-piece.
- All motion `prefers-reduced-motion` gated; hover moves behind
  `(hover:hover) and (pointer:fine)`; budget: 1 entrance + 1 hover + 1 set-piece +
  1 ambient ✓.

## 8. Image list — register: EDITORIAL (one register, every slot)

Justification (required for editorial): an NFL franchise is exactly a brand that
commissions photography — the proud-contractor phone-photo register would read as a
fan's snapshot and undercut "professional, athletic, and large."

**Hard rule on every prompt (real trademarked brand):** no readable lettering, signage,
scoreboard text, advertising boards, jersey names/numbers, or logos anywhere in a
generated image. Environments, light, texture, equipment only.

**GENERATE 1 — Hero (full-bleed).** `16:9`, `2K`, editorial. Renders: section 2,
full-viewport background under a `--night` gradient scrim, headline over its negative
space.
> A photograph of an empty professional football stadium at dusk seen from the mouth of
> the players' tunnel, floodlights blazing against a deep blue evening sky, manicured
> green field with crisp white yard lines, rows of green seats in shadow, cinematic wide
> 24mm perspective, one light-source family (cool floodlights against dusk), subtle
> grain, natural imperfections, no illustration, no 3D render, no CGI, no painting, no
> oversaturation, no text, no watermark, no logo, no signage, no lettering, no
> advertising boards, no scoreboard text, no flags, no people

**GENERATE 2 — Heritage band (full-bleed).** `16:9`, `2K`, editorial. Renders: section
5, full-width band background under scrim, "1969" numerals over it. Distinct scene from
the hero (ground level vs tunnel-wide).
> A photograph of a worn leather football resting on stadium turf beside a white chalk
> yard line, low golden-hour sunlight from the west with long soft shadows, shallow
> depth of field, individual grass blades and chalk texture visible, subtle grain,
> natural imperfections, no lettering or brand marks on the ball, no text, no watermark,
> no logo, no signage, no people, no illustration, no 3D render, no CGI, no
> oversaturation

Cost note: two 2K full-bleeds ≈ $0.26 — inside the pre-approved 2-image cap.
Post-process per imagery.md: WebP, downscaled to real display width, stored in
`mockup/assets/`, hero doubles as the OG image (1200×630 crop).

**PLACEHOLDER slots** (labeled `.img-placeholder` blocks styled in the direction's
colors; these are for REAL club photos, not future AI generation, so label them that
way):
- Players ×3 — `3:4` — `[Player photo + name — supplied by the club]`
- Charity — `4:3` — `[Charity photo — supplied by the club]`
- Locker room — `16:9` — `[Locker room — to be photographed (Q21)]`
- Training facility — `16:9` — `[Training facility — to be photographed (Q21)]`

## 9. Contact/CTA plan — documented exceptions (Critic: score these as exceptions, not fails)

The client gave **no phone, no email, no hours, no address** (Q25: "The ticket team";
Q26: "No" to showing an address). Q24 names the one action: "Go to ticketmaster."

1. **Tap-to-call exception:** `local-trade.md`'s tap-to-call rule is satisfied by the
   **Get Tickets CTA in the phone link's place** — mobile header, plus top/mid/footer
   repeats — `href="PLACEHOLDER_TICKET_URL"` styled as the live primary button.
2. **Service-area exception:** no towns were given; Q4's own answer ("Wherever the fans
   are") IS the service-area statement and gets its own band (section 10). No invented
   town list.
3. **Estimate-form exception:** no form at all — the primary action is off-site
   ticketing by the client's instruction. No map (no address, Q26).
4. **NAP:** footer shows `PLACEHOLDER_TICKET_LINE` · `PLACEHOLDER_TICKET_EMAIL`, no
   address line. JSON-LD carries the identical tokens. Fabricating any real Jets contact
   data is an automatic fail.

## 10. Structured data & meta

- **JSON-LD type: `SportsTeam`** (schema.org, under SportsOrganization) — `sport:
  "American Football"`. `LocalBusiness` would be the dishonest subtype for a sports
  franchise; this is the deliberate, documented schema choice. Properties: `name: "New
  York Jets"`, `contactPoint` with the two placeholder tokens, `url:
  PLACEHOLDER_DOMAIN` (Q30 blank). **No `address` property at all** — omitted per Q26,
  not placeholdered.
- Meta title/description name the team + tickets (no towns exist to name — exception
  noted); OG tags with the hero image; canonical placeholder; favicon points at the
  real logo file (`<link rel="icon" href="assets/ny-jets-logo.svg">`) — no redrawn
  monogram, no separate favicon art.

## 11. Content honesty notes (Builder writes around these)

- "56 years" is the client's own figure — used as given; the founding-date discrepancy
  is a "Confirm with client (optional)" note for Harry, never a `[verify]` on the page.
- Owner is unnamed in the answers — the quote block ships with an attribution comment,
  no invented name.
- Nothing about roster, coaches (past coaches are a Q10 hard ban), schedules, stats,
  media coverage, stadium name, or charity program names. The real NFL franchise is NOT
  a research source for this build.
- No testimonials exist; none appear.

## 12. Client answers → decisions

| Q | Answer (gist) | Decision |
|---|---|---|
| 1 | "New York Jets" | Exact name in wordmark, title, JSON-LD, footer. |
| 2 | 56 years; finance → ownership story | Story section (≤90 words) + half the owner quote block. Trust strip "56 years of football". |
| 3 | "willing to eat losses… team to be better" | The difference: the lyrical owner block, verbatim, attributed to the unnamed owner. |
| 4 | "Wherever the fans are" | Section 10 typographic band = the service-area analog; also hero headline material. |
| 5 | Tickets easy, background, players, charity, look like the best | Drives the whole page map: hero CTA → tickets §4, story §6, players §7, charity §8. "Best" shapes the direction (§1), never printed as a claim. |
| 6 | Season-ticket holders, families | Subhead/support copy vocabulary; full-season tile leads the emphasis. |
| 7 | TV, Ticketmaster, StubHub, social | Ticket-section support line may name Ticketmaster/StubHub. No social links invented (none given). |
| 8 | Pre-season, free training camp, 3-game, full season | The three ticket tiles + the training-camp highlight bar — the complete services content. |
| 9 | "Serving the fans what they cheer for…" | Tickets-section intro line, their words. |
| 10 | No negative media, no past coaches | Hard exclusion, site-wide (voice-spec ban list). |
| 11–14 | blank / no current site | No specials section; no parity chain; nothing kept word-for-word. |
| 15 | "Professional, athletic, and large" | The art direction (§1): composed register, velocity motion, poster-scale type. |
| 16 | "Through our support team" | Organizational register site-wide (voice-spec); owner voice only in the quote block. |
| 17 | blank | Inspiration from Stage 3 evidence instead (§4). |
| 18 | "green and white" | Client-locked palette (§3). |
| 19 | "We have a NY Jets logo out there" | REAL logo used (lead-approved for this internal sample): `assets/ny-jets-logo.svg`, header top-left + footer, always on a `--chalk` plate for contrast, never restyled or hotlinked. Still never inside a generated image. |
| 20 | "New York Jets" (photos) | No usable photo inventory → 2 GENERATE environment shots + labeled placeholders for club-supplied photos. |
| 21 | Locker room, training facility not yet shot | "Inside the club" §9 as labeled to-be-photographed placeholders — NOT generated (generating "their" facility would fabricate). |
| 22 | blank | No testimonial section, nothing invented. |
| 23 | "Super bowl winner 1969" | Trust strip + heritage band §5 (the set-piece) — the one credential, made structural. |
| 24 | "Go to ticketmaster" | Primary CTA everywhere: Get Tickets → `PLACEHOLDER_TICKET_URL`. No competing intents. |
| 25 | "The ticket team" | `PLACEHOLDER_TICKET_LINE`/`PLACEHOLDER_TICKET_EMAIL` tokens; "ticket questions go through the ticket team" line. |
| 26 | No address | Address omitted everywhere including JSON-LD. |
| 27–30 | blank | FAQ cut; no policies section; `PLACEHOLDER_DOMAIN` canonical. |

Nothing in the answers was contradictory enough to flag; the only Harry-side note is the
standing "56 years — confirm (optional)" already recorded in `client-answers.md`.

## 13. Cross-references

- Copy contract: `prospects/jets-site-sample/voice-spec.md` — every visible string
  conforms; hero obeys its uniqueness list.
- Placeholders/embeds: no form, no map (§9). All placeholder styling in direction colors.
- Builder: run detect.mjs to exit 0, copycheck + aitells, JS-off test, and the §5
  composition sanity list before handoff.
