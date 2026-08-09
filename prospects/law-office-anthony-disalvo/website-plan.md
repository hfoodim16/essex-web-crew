# Website plan — Law Office of Anthony DiSalvo, Esq. · `law-office-anthony-disalvo`

## Source authority — dossier-only build

**There is no `client-answers.md` for this prospect and there will not be one.** Harry
authorized a dossier-only build. Every decision a client answer would normally control
was decided from `dossier.md` + `site-content.md` and is **flagged** in §9 (the
"Dossier → decisions" table, standing in for "Client answers → decisions") and in the
Confirm-with-client list (§16). His old site is 16 years old and archived — it is a
fact source, not a voice source, and content parity binds loosely here (no live visitor
loses anything; provenance per `site-content.md`). Anything the dossier does not
support ships as a visible `[placeholder]` or is written around.

Voice contract: **`voice-spec.md`** (written before this hero direction; every copy
direction below conforms to it).

Builder: **5 pages, static, opens by double-click.** `mockup/index.html`,
`real-estate.html`, `wills-probate.html`, `zoning.html`, `about.html` + `style.css`,
`main.js`, assets local in `mockup/assets/`. **GSAP tier 0 — no vendor folder.**

---

## 1. Art direction — **"Porta Aperta" (The Open Door)**

A neighborhood professional's office with the door open — warm plaster, Bloomfield
brick, slate composure, and a chunky humanist serif that feels like a hand-painted
shingle done well. Everything the category default is not: no navy, no gold, no
columns, no gavel, no skyline. His whole differentiator is being the opposite of
intimidating — plain English, fair fees, weekend appointments, Italian at the kitchen
table — so the site reads *domestic and welcome*, structured around a literal
**arched-doorway motif**: the four practice areas are four doors, the hero image sits
in an arch, light falls through arch-shaped washes. A homeowner should read it in two
seconds: *a real person, near me, who will pick up the phone and not talk down to me.*

### The color-convention call — explicit

- **The convention:** legal = **navy + gold + serif** (engine result for "Legal
  Services": authority navy `#1E3A8A` + trust gold `#B45309` on near-white; psychology:
  authority, tradition, trust, gravitas).
- **The call: BREAK it, deliberately.** Two reasons. (1) The dossier's own evidence:
  his brand is anti-corporate warmth — reviews sell reachability and fairness, not
  gravitas; the dossier explicitly warns off the dark-navy authority palette. (2)
  Anti-repetition: the crew's most recent signed prospect (`paul-da-silva-law`, also a
  solo Essex County law office) already honors blue+gold; two lawyer sites in a row in
  the same family is the sameness the ban list exists to kill.
- **Trust cues kept from the category** (breaking ≠ forfeiting): a composed serif
  voice, a restrained 5-token system, generous whitespace, an espresso near-black that
  carries gravitas where it's needed (footer, CTA band), credentials doing the
  persuading (since 2000, former prosecutor, 4.8★).
- **Stated exception for the detector (`cream-palette` / premium-consumer trap):** the
  ground is a warm plaster off-white and the accent is a brick terracotta — territory
  the Step 0 detector and `color-conventions.md`'s trap table flag as the AI-default
  premium palette. **This is a decided exception, not a default:** the warmth IS the
  brief (Italian-American neighborhood practice, domestic register, houses and brick),
  the convention deliberately broken is legal navy, and the family is argued distinct
  from the banned rows below. Builder may waive `cream-palette` in-file citing this
  paragraph; Critic should accept it.
- **Collision check vs the ban list:** `fora-digital` (banned row) is warm **paper +
  ink + cobalt + clay** — its identity is the saturated cobalt accent and interactive
  cobalt field; our palette has **no blue anywhere**, the primary accent is brick
  terracotta paired with a cool slate counterweight, and the family reads
  "brick-and-slate domestic," not "paper-and-cobalt editorial." `paul-da-silva-law`
  (banned row) is cool porcelain + iron-gall ink + brass — cool-toned, hairline-ruled,
  brass metal accent; ours is warm-toned, arch-built, no metallics. `happy-trees`
  (banned row) is bark/moss/sky/lime naturals — no green exists in ours.

## 2. Typography

- **Display: `Young Serif`** (Google Fonts; single weight 400 — its heft IS the
  hierarchy, sized not weighted). Chunky, warm, old-style — reads like a well-made
  shingle, not a law-review masthead. Used for: the text wordmark (no logo exists —
  dossier: "No logo found", the CLAUDE.md text-wordmark case), h1–h3, the big phone
  number, practice-card titles.
- **Body: `Alegreya Sans`** (Google Fonts; 400/500/700/800). Humanist, calligraphic
  warmth, excellent at text sizes for an older audience. Used for: body, nav, lists,
  forms, buttons, captions.
- Never the banned set (Inter, Roboto, Arial, Helvetica, Fraunces, Instrument Serif,
  Geist, Plus Jakarta Sans, Space Grotesk). Not in any `design-memory.md` row; distinct
  from the engine's conventional EB Garamond/Lato and from every sibling pairing.
- **Wordmark lockup:** "Law Office of **Anthony DiSalvo**, Esq." in Young Serif,
  two-line stack in the header (top-left, where a logo belongs), with the tagline as a
  small Alegreya Sans line beneath it in the footer lockup only. Spelling **DiSalvo**
  (his own site's usage — see §9).

## 3. Color system (CSS `:root` tokens)

| Token | Hex | Role |
|---|---|---|
| `--intonaco` | `#F5EEE2` | Warm plaster — page ground, light sections |
| `--mattone` | `#B05A38` | Bloomfield brick terracotta — arches, rules, large display accents, active states |
| `--mattone-scuro` | `#7E3A20` | Darkened brick (a shade, not a 6th hue) — CTA fills, any brick-toned text on plaster |
| `--ardesia` | `#47535B` | Slate — secondary text, captions, card meta, form labels |
| `--ink` | `#2A211B` | Espresso near-black — headings/body on plaster; ground of the footer (the single dark section) |
| `--linea` | `#DDD2C2` | Warm hairline — borders, rules, dividers |

(Italian token names: intonaco = plaster, mattone = brick, ardesia = slate, linea =
line.) Light text on `--ink` is `--intonaco`. All components reference tokens; no
hardcoded hex.

**Contrast rules (Builder verifies at final values):**
- Body: `--ink` on `--intonaco` (~12:1 ✓).
- `--mattone` on `--intonaco` ≈ 3.4:1 — **large display text, arch strokes, and rules
  only.** Any normal-size brick-toned text uses `--mattone-scuro` (~6.5:1 ✓).
- CTA buttons: `--mattone-scuro` fill + `--intonaco` label (~6.5:1 ✓). Never
  `--mattone` fill with light label.
- `--ardesia` on `--intonaco` ≈ 6.3:1 ✓ for secondary text.
- The full-bleed band ships with no overlay text (§6.5); if any text is ever placed
  over a photo, it sits on an `--ink`-based scrim, AA re-checked against the actual
  image.

## 4. Anti-repetition (Stage 4 — crew log, last 3 rows banned)

Read `~/Projects/essex-web-crew/design-memory.md` 2026-08-02. Banned and avoided:

| Banned row | Fonts avoided | Palette family avoided | Archetype avoided | Motion avoided |
|---|---|---|---|---|
| happy-trees-by-mgm | Zilla Slab / Work Sans | bark + moss + sky + hi-vis lime | canopy-descent full-bleed | dapple light + photo scrim |
| fora-digital | Instrument Serif / Hanken Grotesk | warm paper + ink + cobalt + clay | gallery-wall portfolio (framed plates) | mask-curtain entrance, underline-draw/fill-sweep hovers, `view()` gallery-hang, pointer vector field |
| paul-da-silva-law (Rev 3) | Libre Caslon Text / Albert Sans | porcelain-and-ink with brass | modular ruled ledger (Swiss hairline compartments) | rules-draw-in entrance, weight-shift hover, sticky progress rail |

Also avoided although outside the 3-row window (crew-repeat hygiene, and because the
legal sibling makes echoes louder): Besley/Schibsted (da-silva Rev 2), split-screen
advocacy + clip-wipe (da-silva Rev 2), ink bands as mid-page punctuation (da-silva Rev
3), sidebar letterhead + dot grid (john-sessa), Marcellus (anthonys), Fraunces
(banned globally anyway). Flagged defaults (fade-up / staggered text delay / count-up):
not used.

**Soft-sameness screen vs the legal sibling (Critic advance flag, 2026-08-02) — designed
around, by name:**
1. *Hero shot collision:* the dossier's "warm streetscape at golden hour" hint is NOT
   followed — da-silva's image A is exactly that shot (street-level NJ street, warm
   late-afternoon, phone register). Our two generated images are a **house portrait in
   soft morning sun** and a **domestic closing-table still life (house keys, kitchen
   table, morning window light)** (§13) — no streetscape exists anywhere in this
   build, and neither image shares genre with either da-silva image (streetscape +
   office interior). The still life also carries the transactional-domestic
   differentiator: DiSalvo's work is closings, deeds, variances, and wills — keys in
   your hand, not a courtroom.
2. *Closing rhythm:* da-silva closes every page with a dark band carrying a huge
   display-serif phone number. Ours closes with a **light arch-framed "open door"
   invitation block** with a button-sized call CTA; the only dark section is the
   footer. (The about-page contact block is phone-dominant because no email exists —
   a functional necessity, one page, not a sitewide closing rhythm.)
3. *No ruled compartments, no italic-serif index numerals (01–04), no
   "legal-record/document" organizing idea anywhere* — the organizing idea is domestic
   (doors, arches, plaster).
4. *Value structure:* warm plaster + non-metallic brick/slate — not light-porcelain +
   single-metallic-accent.

**What makes DiSalvo diverge from Da Silva at the structural level, not just hue:**
Da Silva is a *courtroom* story — dark-first gravitas, ruled compartments, ink bands, a
defense attorney for frightened families. DiSalvo is a *keys-in-your-hand* story — 26
years at one Broad Street address, closings and variances and wills, fluent Italian,
talks people out of paying him. So: warm light-first vs cool light-on-dark-structure;
arches vs hairline rules; domestic photography vs civic streetscape; settle-in motion
vs drawn rules; a recovered personal tagline vs a composed positioning line.

## 5. The three directions (Stage 5) + the pick

**Direction 1 — "Counselor's Standard" (HONORS convention).**
Concept: the navy+gold solo-attorney site executed cleanly — trust by recognition for
a risk-averse audience. Layout: centered-classic + credential strip · Type: Petrona /
Source Sans 3 · Palette: authority navy + muted gold on near-white (honors) ·
Background: flat + grain · Motion: minimal, blur-focus entrance · Hero: office-interior
photo. **Why not:** it is the exact register the dossier warns against for *this* man,
it cannot clear boldness ≥ 8, and it walks straight into the legal sibling's
blue+gold territory — the one collision this build must not have.

**Direction 2 — "Porta Aperta" ← PICKED.**
Concept: the open door — a warm, domestic, Italian-American neighborhood office; the
opposite of intimidating, structured on an arched-doorway motif.
Layout: **arched-entry editorial** (asymmetric type-led hero with arch-framed image;
practice areas as four arched "doors"; light sections with one dark close) · Type:
Young Serif / Alegreya Sans · Palette: plaster + brick + slate + espresso
(brick-and-slate domestic warm — BREAKS legal navy+gold, argued in §1) · Background:
plaster + stucco grain + arch-shaped doorway-light washes · Motion: scale-settle
entrance + zoom-crop hover, no set-piece, one ambient doorway-light drift; tempo 650ms
/ `cubic-bezier(.2,.7,.2,1)` / 80ms; GSAP tier 0 · Hero: his own tagline + arched
golden-hour brick-home photograph.
**Why bold:** no law site looks like this, yet every cue reads *neighborhood
professional you can call on a Saturday* — the differentiator (warmth, houses, Italian
domesticity) carried by structure, palette, and type rather than by claims.

**Direction 3 — "The Broad Street Shingle" (BREAKS, vernacular-loud).**
Concept: Italian-American storefront vernacular — hand-painted-sign energy, oversized
condensed display, awning-scallop dividers, kinetic type.
Layout: brutalist stack / oversized masthead · Type: a condensed display (e.g.
Bricolage Grotesque at heavy weights) / Asap · Palette: espresso + awning red + cream ·
Background: flat + scallop pattern · Motion: kinetic, skew-slide entrances.
**Why not:** visually the boldest, tonally wrong — storefront-sign playfulness reads
cute on a man whose clients bring him wills and probate; the cuteness ban in
`voice-spec.md` applies to the design register too. Bricolage is also a crew repeat
(duran-and-son).

**Pick: Direction 2** — the boldest that fits the brief. Axes check: the three differ
on layout archetype, typography, color strategy, background system, AND motion
character (5/5).

## 6. Page map (5 pages — the dossier's recommended map, adopted)

Shared on every page:
- **Header (plaster, hairline bottom rule):** Young Serif wordmark top-left ("Law
  Office of **Anthony DiSalvo**, Esq.", two-line stack) · nav: Home / Real Estate /
  Wills & Estates / Zoning / About & Contact · **`--mattone-scuro` tap-to-call button
  "Call (973) 233-4778"** (`tel:+19732334778`), visible at every size — on mobile the
  header keeps a compact call button beside the hamburger.
- **Footer (espresso `--ink`):** wordmark small + tagline beneath it ("No client too
  small. No problem too big.") · NAP: Law Office of Anthony DiSalvo, Esq. · 1083 Broad
  Street, Bloomfield, NJ 07003 · (973) 233-4778 · Fax (973) 338-0065 · "Si parla
  italiano · Se habla español" line · nav links · `[Attorney-advertising disclaimer —
  for client review]` clearly bracket-flagged · © 2026 Law Office of Anthony DiSalvo.
  **No email anywhere — none exists.** Footer NAP must match JSON-LD exactly.

### index.html — Home
1. **Hero (plaster, asymmetric split — type left ~55%, arch right):** h1 = the tagline
   **"No client too small. No problem too big."** verbatim (see §10 for the
   typographic treatment) · subhead ≤30 words naming the four practice lines +
   Bloomfield + since 2000 · CTA pair: "Call (973) 233-4778" primary +
   "Send a message" secondary → about.html#contact. Right: **GENERATE image A** in a
   full-height arch frame (§13). Exactly 4 text elements; no eyebrow; trust content
   lives below, never inside.
2. **Trust strip (under hero, hairline-ruled row, 4 items):** *Practicing since 2000* ·
   *Free 30-minute consultation* · *Si parla italiano* · *4.8★ on Google*. All four
   dossier-verified. No count-up.
3. **Four doors (arched practice cards, 4 cells = 4 items):** Real Estate & Closings →
   real-estate.html · Wills, Trusts & Probate → wills-probate.html · Land Use & Zoning
   → zoning.html · Traffic & Municipal Court → about.html#contact (the dossier's
   fold-into-home call: card copy IS the content — speeding, suspended/revoked
   license, DWI, former prosecutor, goal phrasing, ≤30 words). Cards carry arch-top
   frames with tinted grounds (real visual weight in ≥2 cells; the two lead cards get
   AI-IMAGE placeholder art, §13 slots 3–4).
4. **Review band (centered quote, plaster on a warm wash):** the ONE attributed real
   review, large: "Best advice I EVER got from an attorney, and I've sadly seen
   plenty. Good man." — S c., Lawyers.com, 5/5 (2021), verbatim · beside it the 4.8★
   Google line · plus two clearly-labeled placeholder blocks: `[Real Google review
   goes here — text captured, awaiting reviewer first names]`. **No unattributed quote
   ships** (dossier attribution blocker).
5. **Full-bleed photo band:** **GENERATE image B** (§13) — the closing-table still
   life: house keys on a worn kitchen table in morning window light, edge-to-edge,
   **no overlay text, no scrim.** The transaction-artifact image — what his work
   actually hands you. (Deliberately not a streetscape; see §4 item 1.)
6. **Service area (two-column town list on plaster):** intro line from his own
   orientation copy — "1083 Broad Street, Bloomfield — eight miles from New York
   City, just off the Garden State Parkway." — then heading + the 2010 footer's real
   town list: Bloomfield, Montclair, Clifton, Wayne, Sparta, Nutley, Passaic,
   Paterson, Little Falls, Verona, Cedar Grove, Fairfield, Belleville — and Essex,
   Bergen, Passaic, Union, Middlesex, Sussex and Warren counties. Flagged in-comment
   `[16-year-old list — confirm with client]` but shown (it's his own published list).
7. **Closing CTA — the "open door" block (plaster, NOT a dark band):** an arch-framed
   invitation — a `--mattone`-stroked doorway arch with the warm wash inside,
   containing: heading "Free 30-minute consultation." · one line "Weekend appointments
   available upon request." · the tap-to-call **button** "Call (973) 233-4778"
   (button-sized, Alegreya Sans — never a display-serif numeral) + "Send a message"
   secondary link. This is the motif closing every page. **Deliberately not
   da-silva's dark big-serif-phone closing band (§4 soft-sameness item 2).**
8. Footer (espresso `--ink` — the page's single dark section).

Layout families used: asymmetric split hero · ruled strip · arched card grid ·
centered quote band · full-bleed image band · columned list · arch-invitation block —
6+ families across 7 sections ✓. One image+text split on the page (the hero) ✓. Eyebrows:
≤2 total (cards section + service area at most).

### real-estate.html — Real Estate & Closings
1. **Page header (compact, arch-wash background):** h1 "Real estate closings in Essex
   County" + intro ≤40 words (buyers and sellers, residential closings, commercial
   leasing — dossier-proven services only).
2. **For buyers / For sellers / Commercial leasing (3 blocks, ruled columns):**
   buyers: first-time-buyer angle (several reviews are first-time buyers — reachable
   by text with every "silly question"); sellers: including out-of-state estate sales
   (a review documents him guiding one from another state); leasing: short, ≤30 words.
   Facts only; no process invention.
3. **Landlord–tenant matters (compact block, `[confirm]`-flagged):** carried from his
   2010 page at factual fidelity — landlords and tenants, non-payment of rent, lease
   violations, evictions, Section 8 matters, judgment enforcement, security-deposit
   disputes, habitability, Landlord-Tenant Court, keeping fees reasonable. HTML
   comment: `[From his 2010 site — confirm still current before launch]`.
4. **Arch image slot:** AI-IMAGE placeholder (§13 slot 5).
5. Open-door CTA block + footer (shared components).

### wills-probate.html — Wills, Trusts & Probate
His best surviving prose lives here — carry it at full factual fidelity, tightened
per the voice spec (parity counts facts, not words).
1. **Page header:** h1 "Wills, trusts & probate" + the "people put off drafting a
   will" passage carried as the intro (his most human surviving copy — keep the
   comfort-not-jargon substance, trim FindLaw padding).
2. **Wills & trusts (list block):** the real 2010 service list, complete — last will
   and testament after thorough discussion · powers of attorney + advance directives
   (incl. DNR if chosen) · proper witnessing · affidavits that lessen will challenges
   · trusts (sprinkle, special-needs, revocable, spendthrift, others) · guardians for
   minor children · can serve as executor/administrator · **will visit clients at home
   or in the hospital** · keeps copies of estate documents · litigates disputes if
   they arise.
3. **Probate & estate administration (list block):** the real 2010 checklist, complete
   — submitting the will to the Surrogate's Court · letters of administration ·
   locating documents · paying bills and taxes incl. final medical/funeral bills and
   NJ Inheritance Tax · life-insurance claims · distributing assets · dissolving the
   estate · litigating disputes. Plus the "why you should not wait" facts
   (court-mandated deadlines, assets disappearing) as a short plain paragraph.
4. **Arch image slot:** AI-IMAGE placeholder (§13 slot 6).
5. Open-door CTA block + footer.

### zoning.html — Land Use & Zoning
Thin by design (voice spec) — a real niche with one proven win; do not pad.
1. **Page header:** h1 "Zoning variances & land use" + intro ≤40 words: variances for
   homeowners (additions, extensions) and small projects; a client's kitchen-extension
   **Type C variance** is review-documented. Goal phrasing only.
2. **Who this is for (2 short blocks):** homeowners adding on · small
   developers/owners before the zoning board. `[Confirm scope with client]` comment.
3. **Review placeholder block:** `[Real Google review — the Type C variance story is
   captured verbatim, awaiting the reviewer's first name]` — labeled, unfilled.
4. **Arch image slot:** AI-IMAGE placeholder (§13 slot 7).
5. Open-door CTA block + footer.

### about.html — About & Contact
For a solo attorney this page does the selling.
1. **Page header:** h1 "Anthony DiSalvo, Esq."
2. **Portrait: labeled PLACEHOLDER** in the arch frame — `[Photo of Anthony DiSalvo —
   real headshot to come from client]`. **NEVER generated** (hard rule; highest-value
   client ask per the dossier).
3. **Bio (≤150 words + credential list):** former prosecutor; former litigator for a
   national business law firm; New York Law School J.D. 1998; Seton Hall University
   B.S. 1991; admitted to the NJ bar 2000; fluent Italian — welcomes Italian- and
   Spanish-speaking clients; will arrange to visit clients who can't come to the
   office (his 2010 contact-page fact); Vice President of U.N.I.C.O. since 2011.
   `NJ bar number: [placeholder]`. **No founding year** (voice spec). The Avvo 6.5
   rating is NOT featured (unclaimed-profile artifact, per dossier).
4. **Contact block (`#contact`):** phone-dominant — the number huge in Young Serif,
   tap-to-call; fax beneath; full address; hours line: "Weekend appointments available
   upon request. `[Office hours — confirm with client]`" · **form ≤4 fields:** Name ·
   Phone · What do you need help with? (textarea) · "Send" — static demo with inline
   confirmation on submit ("Thanks — Anthony will call you back at the number you
   gave." — Builder finalizes per voice spec), never a dead click; HTML comment
   marking where a real form service goes. **No email field, no email address.**
5. **Map embed placeholder:** labeled block ("Google Map — 1083 Broad Street,
   Bloomfield") + HTML comment for the real embed. The 26-years-one-address fact makes
   the map earn its place.
6. Footer.

## 7. Content map (every `site-content.md` block placed or dropped)

Provenance note: no live site exists; all blocks are from the 2010 Wayback capture.
Parity here protects *facts recovered*, not a live visitor's content.

| site-content.md block | Destination |
|---|---|
| Sidebar NAP (name, address, phone 973-233-4778, fax) | Header CTA + footer + about.html contact block + JSON-LD |
| Tagline ("No client too small. No problem too big.") | Home hero h1, verbatim + footer lockup |
| Flash CTA ("free initial consultation / Call 973-233-4778") | Trust strip item + closing CTA band on every page |
| Home: "Diverse Practice" ¶ (worked in every type of firm, large-firm to two-person) | about.html bio (facts: national-firm litigator, breadth) |
| Home: "Approachable – Caring" ¶ | **Facts carried, phrasing dropped** (voice spec: never self-claim traits). The substance — easy to speak with him — is carried by the reviews band + reachability facts |
| Home: "Clients" ¶ (all walks of life, small family businesses, fluent Italian, welcomes Italian-American clients, wills/trusts/landlord-tenant/small-business) | about.html bio (languages) + home trust strip (Si parla italiano) + footer language line; "no client too small…" is the hero |
| Home: "Philosophy" ¶ (tries cases when needed; keeps costs down, avoids needless litigation) | Kept as ONE plain sentence on about.html bio ("keeps costs down… without going to court when it can be avoided" — fact, review-corroborated) |
| Home: contact ¶ (free initial consultation, 8 miles from NYC / GSP, Mon–Fri 8:30–5, weekend appointments) | Free consult → trust strip; orientation line → home full-bleed band caption; weekend appointments → CTA band + about hours line; **exact hours → `[placeholder]`** (4 conflicting versions) |
| Footer service-area town list (13 towns + 7 counties) | Home §6 service-area block, complete, `[confirm]`-flagged |
| Attorney Profile page (corporate-litigator background, ordinary people's matters, fluent Italian) | about.html bio |
| Practice Areas: Wills & trusts summary + full Wills & Trusts page (all lists) | wills-probate.html §2, complete |
| Practice Areas: Probate summary + full Probate page (all lists, why-not-wait) | wills-probate.html §3, complete |
| Practice Areas: Landlord/Tenant summary + full page (all case types, cost-sensitivity) | real-estate.html §3 compact block, `[confirm]`-flagged |
| Practice Areas: Traffic ¶ (former prosecutor; speeding, revoked/suspended license, DWI, all municipal matters) | Home traffic card (≤30 words, all facts) |
| Practice Areas: routes line (Route 3/21/80/46, off GSP) | ONE orientation line used (home band caption uses the 8-miles/GSP version; routes version dropped as duplicate orientation copy) |
| Contact page ¶ (welcomes Italian/Spanish speakers, will visit clients unable to come to office, form + phone) | about.html bio + contact block |
| Contact form fields (Name, E-mail Address, State, message) | about.html form, cut to 4: Name / Phone / message ("State" dropped — single-county practice; email field dropped — phone-first, no email exists to reply from) |

**Deliberately dropped (no silent drops):**
- **Immigration, Employment Law, Family Law, Bankruptcy, Litigation, International
  Business practice blurbs (+ the bankruptcy debt-relief-agency notice)** — 16-year-old
  advertised areas with NO current evidence (dossier: reviews cluster on four areas;
  "do not build a page for any of these without his confirmation"). Advertising a
  practice area a lawyer no longer takes is a liability, not parity. The breadth they
  represented is carried honestly by his own Yelp line territory ("small office that
  can handle most areas of the law") in the home subhead/about, and each area is on
  the Confirm list (§16) for reinstatement if he confirms.
- **2010 page titles / SEO strings ("Trial Lawyer", "Business Litigation Attorney")** —
  stale positioning nothing current supports; replaced by §15 meta named to the four
  live areas.
- **"Approachable/personable/caring" self-descriptions** — phrasing only (voice spec);
  every underlying fact is carried.
- **FindLaw template art references (pen photos, stock attorney graphic)** — FindLaw
  stock, 404'd anyway; stock is banned regardless.
- **Mon–Fri 8:30–5 exact hours** — one of four conflicting versions; `[placeholder]`
  until he confirms (weekend-appointments phrase IS carried — 3 of 4 sources).

## 8. Real reviews (hard rule compliance)

- **Ships attributed:** the S c. quote (Lawyers.com/FindLaw, 5/5, May 23 2021),
  verbatim, home review band.
- **Ships as labeled placeholders only:** the 4 strong Google quotes — captured
  verbatim in the dossier but name-stripped by the mirror. Blocks read `[Real Google
  review goes here — text captured, awaiting reviewer first names]`. **The Builder
  must NOT paste the unattributed texts into the page.**
- The Superpages "anonymous" review: not used (platform-anonymous, weak; dossier notes
  it for completeness only).
- The 4.8★ Google rating ships as a fact; **no review count** (sources disagree
  24–29), just "4.8★ on Google."

## 9. Dossier → decisions (stands in for "Client answers → decisions")

Every load-bearing decision a questionnaire answer would normally control, with what
the plan does and its dossier basis:

| Decision | Plan | Basis / flag |
|---|---|---|
| Business name & spelling | "Law Office of Anthony DiSalvo, Esq." — **DiSalvo** | His own site + Yelp + Avvo. D&B's "Desalvo…PC" ignored. Confirm #1 |
| Phone | **(973) 233-4778** everywhere | His own site + Yelp (updated May 2026) + Avvo, per dossier recommendation. Confirm #2 — **most important confirm; wrong number is fatal** |
| Email | **None on the site, anywhere** | No email exists in any source; never invent. Confirm #3 (does he have one now?) |
| Practice areas | The four review-proven lines + traffic card; landlord-tenant carried compact + flagged; six 2010 areas dropped to Confirm list | Dossier "build the site around these" + its stale-areas warning |
| Page map | 5 pages (dossier's recommended map, adopted 1:1) | Four real areas = four search intents; About/Contact sells the solo attorney |
| Hero | His recovered tagline, verbatim | His own line; matches what reviews independently say. §10 |
| Logo | Text wordmark in Young Serif | Dossier: "No logo found" → CLAUDE.md wordmark case |
| Headshot | Labeled placeholder, never generated | None exists; dossier's highest-value client ask |
| Founding year | **Never stated**; "practicing since 2000" only | Three conflicting published years; only bar admission is hard-sourced |
| Hours | Weekend-appointments phrase + `[placeholder]` exact hours | Four conflicting versions; weekend availability in 3 of 4 incl. his own site |
| Free consultation | "Free 30-minute consultation" in trust strip + CTA band | Avvo "$0 first 30 minutes" + his own 2010 "free initial consultation" |
| Languages | "Si parla italiano" trust-strip item; Italian + Spanish welcome in bio + footer line | His own site (fluent Italian, welcomes Italian- and Spanish-speaking clients) |
| Towns | 2010 footer list shown, flagged | His own published list; 16 years old. Confirm #6 |
| Reviews | §8 exactly | Attribution blocker in dossier |
| Avvo 6.5 rating | Not featured | Dossier: unclaimed-profile artifact |
| U.N.I.C.O. | Bio line ("Vice President of U.N.I.C.O. since 2011") | Avvo, 2011–Present |
| Palette/direction | Warm break from legal navy | Dossier art-direction hints + anti-repetition vs the legal sibling. Confirm #9 (he may want "lawyer colors" — see da-silva precedent) |
| Domain | None registered; meta uses `PLACEHOLDER_DOMAIN` | `adisalvolaw.com` lapsed and available — Harry's opening gift, not a plan decision |

## 10. Hero direction

- **h1 (verbatim, protected):** "No client too small. No problem too big."
  **Typographic treatment carries the differentiation** (voice-spec hero-uniqueness
  note): two stacked Young Serif lines; in line 1 the word "small" set a step smaller,
  in line 2 the word "big" set a step larger — a quiet scale gesture, both words in
  `--mattone`. No year fragment, no third fragment, no restructuring.
- **Subhead (≤30 words, spec-shaped):** concept — *"Real estate closings, wills and
  estates, zoning, and traffic matters. Plain English and fair fees — practicing on
  Broad Street in Bloomfield since 2000."* (Builder finalizes against voice spec; one
  em dash max.)
- **CTAs:** primary "Call (973) 233-4778" (`tel:`, `--mattone-scuro` fill); secondary
  text link "Send a message" → about.html#contact.
- **Hero media:** GENERATE image A in a full-height arch (§13). The arch is the
  signature frame — used again for practice cards, portrait, and page-header washes.
- Composition: ≤4 text elements; headline ≤2 lines; top padding ≤6rem; trust strip
  below the hero, never inside.

## 11. Signature motion — "Settle In" (Planner-owned; Builder does not re-decide)

- **Entrance family: scale-settle** — `opacity 0, scale(.97)` → settled, 650ms,
  applied consistently to all reveals. (Not in any of the last-3 rows.)
- **Hover personality: zoom-crop** — images scale 1.06 inside their arch/overflow
  frames, caption/label slides up 4px; applies to practice-card arches and image
  plates. Buttons/links use color-step + universal pressed state (`:active
  scale(.97)`) — pressed state is hygiene, not a second personality. Guarded by
  `(hover:hover) and (pointer:fine)`.
- **Scroll set-piece: NONE** (deliberate — the audience is older homeowners; calm is
  the register).
- **Tempo:** 650ms entrances / `cubic-bezier(.2,.7,.2,1)` / 80ms stagger (cards, list
  rows, ≤12 items).
- **GSAP tier: 0** — pure CSS + a ~20-line IntersectionObserver. No vendor folder.
- **Avoided (named):** rules-draw-in, weight-shift, sticky progress rail (da-silva);
  mask-curtain, underline-draw/fill-sweep, `view()` gallery-hang, pointer field
  (fora); dapple/photo-scrim (happy-trees); fade-up/text-delay/count-up (flagged
  defaults).
- **Rule 0 compliance:** all hidden states scoped to `html.js` inside
  `prefers-reduced-motion: no-preference`, with the head opt-in snippet + error/timer
  nets from `motion.md`. JS-off page renders complete.

**Background & atmosphere direction:** plaster ground + fine stucco grain (~0.04
opacity SVG turbulence) sitewide · **arch-shaped warm radial washes** ("light through
a doorway": a soft `--mattone`-tinted radial gradient clipped to an arch, anchored at
each page header and behind the hero arch) · thin `--linea` hairlines and occasional
`--mattone` rules · the full-bleed band's `--ink` scrim. **One ambient system:** a slow
warm glow drift inside the hero arch (atmosphere.md shimmer/god-ray family at very low
alpha, 18s+ cycle, reduced-motion gated, paused offscreen). Budget: 1 entrance + 1
hover + 1 ambient = 3 animated systems ≤4 ✓. **No reactive field** (wrong register for
legal — hard no per `reactive-backgrounds.md`).

## 12. Composition pre-flight (Stage 8 checks planned around)

Hero ≤4 text elements ✓ · trust strip under hero ✓ · one theme (light pages; the
footer is the single dark section — no dark bands anywhere else) ✓ · ≤1 image+text
split per page ✓ (zigzag never reaches 2) · ≥4 layout families on Home ✓ · zero
marquees ✓ · grid cells == items (4 doors) ✓ · eyebrows ≤2 per page ✓ · one accent
used identically everywhere ✓ · one radius system: **arch-top frames + otherwise
near-square (4px) corners** — the arch is a frame shape, not a border-radius mix;
Builder documents the rule in style.css ✓ · CTA labels: primary is the phone number
(the sanctioned local-trade exception to label length); no two CTAs share an intent
(Call vs Send a message) ✓ · skip-to-content link + footer privacy/terms placeholder
links ✓.

## 13. Image list — 2 GENERATE, rest placeholders

**Register (ONE for the whole site): proud-contractor**, adapted to the
neighborhood-real-estate subject — "the best photo on his Google Business profile":
attractive, well-kept North Jersey homes and streets, casual-but-flattering phone-photo
framing, pleasant natural light. NOT editorial (no commissioned-shoot look — this is a
man whose brand is small-firm pricing). **No readable business names, signage,
lettering, house numbers, or branded vehicles in ANY generated image.** No people.

| # | Slot | Status | Spec |
|---|---|---|---|
| 1 | **Home hero (arch frame, contained ~600px wide)** | **GENERATE** | `3:4` · `1K` · proud-contractor. **Morning light, house portrait — deliberately NOT a golden-hour streetscape (§4 soft-sameness item 1).** Prompt: *"A photograph of a handsome brick two-family home with a tidy front porch on a quiet tree-lined northern New Jersey residential street, soft morning sun, taken with a phone, good consumer-camera quality, honest straight-on framing from the sidewalk, level horizon, well-kept small front yard, mature street trees, subtle grain, natural imperfections, uneven textures, no phone UI, no on-screen icons, no status bar, no timestamp overlay, no screen chrome, no illustration, no 3D render, no CGI, no painting, no oversaturation, no plastic or waxy textures, no perfect symmetry, no text, no watermark, no logo, no people, no signage, no lettering, no house numbers, no vehicles"* |
| 2 | **Home full-bleed band (§6.5, edge-to-edge)** | **GENERATE** | `16:9` · `2K` (full-bleed rule) · same register as #1 but a **different photographic genre entirely: a domestic transaction still life, not any street or exterior shot** (collision flag, §4 item 1 — and a second exterior would dilute the doorway motif). The artifact his work actually hands you: keys. Renders edge-to-edge with **no overlay text and no scrim**; also cropped to 1200×630 for the OG image (no extra generation). Prompt: *"A photograph of a set of house keys on a plain steel key ring resting on a worn wooden kitchen table, warm morning window light falling across the wood grain, taken with a phone from above the table at a slight casual angle, good consumer-camera quality, honest framing, subtle grain, natural imperfections, uneven textures, no phone UI, no on-screen icons, no status bar, no timestamp overlay, no screen chrome, no illustration, no 3D render, no CGI, no painting, no oversaturation, no plastic or waxy textures, no perfect symmetry, no text, no lettering, no engraved writing, no documents, no paper, no watermark, no logo, no people, no hands"* |
| 3 | Practice card — Real Estate | PLACEHOLDER | `<!-- AI-IMAGE: a welcoming front porch with the front door standing open, seen from the front walk, morning light, phone-photo register, no signage, no house numbers, no lettering, no people -->` (changed from keys-on-table — that concept now IS generated slot 2) |
| 4 | Practice card — Wills & Estates | PLACEHOLDER | `<!-- AI-IMAGE: a fountain pen resting on plain folded documents beside reading glasses on a dining table, warm domestic light, no readable text -->` |
| 5 | real-estate.html arch slot | PLACEHOLDER | `<!-- AI-IMAGE: modest New Jersey colonial home exterior with a SOLD-style sign deliberately absent, front walk and porch, late morning light, different property from the hero, no signage or lettering -->` |
| 6 | wills-probate.html arch slot | PLACEHOLDER | `<!-- AI-IMAGE: document-and-pen still life, warm and domestic, kitchen-table register, not corporate, no readable text -->` |
| 7 | zoning.html arch slot | PLACEHOLDER | `<!-- AI-IMAGE: a residential rear addition under construction on an attractive suburban home, clean tidy site, framing lumber, bright clear day, no signage, no lettering, no workers -->` |
| 8 | about.html portrait | **PLACEHOLDER — client-supplied only** | `[Photo of Anthony DiSalvo — real headshot to come]`. NEVER generated (real person). |
| 9 | about.html office slot (optional, below contact) | PLACEHOLDER | `<!-- AI-IMAGE slot reserved for a REAL photo of 1083 Broad Street from the client — do not generate a fake office -->` |

Builder: `/generate` on **`nano-banana-2`** (never `-lite`), one at a time, realism QA
per `imagery.md` (two-way test; ≤1 retry each), WebP + downscale to real display width,
store in `mockup/assets/`. Cost ≈ $0.10 (one 1K + one 2K) — within the pre-approved cap.

## 14. Video — ZERO slots (deliberate, despite pre-approval)

Harry pre-approved one `filmed-action` clip (≤$1, ≤8s) for this build. **I am marking
zero video, and here is the honest frame-2 answer:** a solo attorney's work is advice,
paperwork, and phone calls — nothing this business does is physically visible motion.
Frame 2 of any candidate clip (a streetscape with drifting leaves, hands over
documents, a door opening) shows nothing about *his work* that frame 1 cannot; every
candidate is atmosphere, and rung 2 of the free ladder (the doorway-light ambient
drift in §11) already sells the same warmth at $0. A designed loop is a hard no behind
a legal prospect. A still is never a deduction; an unjustified clip is a Critic
hard-fail. The poster-still question is therefore moot — the two GENERATE images carry
the site.

## 15. Local-SEO & meta spec

- **JSON-LD:** `@type: "Attorney"` (schema.org subtype of LegalService) on every page.
  `name` "Law Office of Anthony DiSalvo, Esq." · `telephone` "+19732334778" ·
  `address` 1083 Broad Street, Bloomfield, NJ 07003 · `areaServed` the §6.6 towns ·
  `knowsLanguage` ["en","it","es"] · `url` `https://PLACEHOLDER_DOMAIN` · **no
  `openingHoursSpecification`** (4 conflicting versions — omit rather than guess) ·
  **no `email`** · no `geo`/`sameAs` (don't guess). Footer NAP matches character for
  character.
- **Meta:** title `Real Estate & Estate Attorney in Bloomfield, NJ | Law Office of
  Anthony DiSalvo` (per-page variants naming that page's service + Bloomfield/Essex
  County) · description names services + 2–3 real towns · OG/Twitter cards using the
  image-2 crop · canonical with `PLACEHOLDER_DOMAIN` · inline SVG favicon (Young Serif
  "D" on `--mattone`) · `<html lang="en">` · one h1 per page.

## 16. Confirm with client (for Harry — flags, not blockers)

1. Name styling: "Law Office of Anthony DiSalvo, Esq." OK?
2. **Primary phone: 233-4778 vs 338-0036 — the critical one.**
3. Does an email address exist now? (None published anywhere.)
4. Headshot (highest-value ask) + a real photo of 1083 Broad Street.
5. Practice areas: are landlord–tenant, and any of immigration / employment / family /
   bankruptcy / litigation / international business, still taken? (Currently: L/T
   carried flagged; the rest dropped.)
6. Town/county list still accurate? (16 years old.)
7. Exact office hours; do weekend appointments still stand?
8. NJ bar number + courts admitted (for the bio).
9. Palette check: this plan deliberately breaks "lawyer navy+gold" for warm
   brick-and-plaster — if he wants conventional lawyer colors (as Da Silva's client
   did), that's a revision, not a defect.
10. Google review first names (unlocks 4 strong captured quotes).
11. Free wins to mention: `adisalvolaw.com` is unregistered and cheap to reclaim;
    Avvo/Martindale profiles unclaimed.

## 17. Stage 3 evidence (references studied)

**Local `Inspiration/` library (all 10 files reviewed; filenames are hashes):** the
library is landscaping/trade-weighted this cycle — two landscaping site mockups
(Greenora-style template: the icon-card/eyebrow patterns we deliberately refuse; OG
Outdoors dark photo-hero), one heritage-architecture illustrated landing (cream +
slate + rust, layered scene — the closest tonal cousin to this direction's warmth; its
centered serif masthead informed the wordmark-first header), one SaaS landing, and six
photography references (machinery, garden, landscape — none in the legal/domestic
register). **No file is used as a seed or shipped asset for this build**; the
heritage-architecture mockup is named as tonal evidence only.

**Live/dossier references (named patterns per `inspiration.md` vocabulary):**
- **Lee & Garasia (`njimmigrationattorney.com`, real NJ firm — dossier evidence
  sheet):** sticky condensing bar · full-bleed photo hero · 2-col card grid with
  hover image swap · attributed-testimonial carousel. **Stolen as pattern:** phone
  number present five ways (we do header button + hero CTA + CTA band + footer NAP +
  contact block). **Cliché noted:** stock courthouse/handshake imagery — refused.
- **Cary Estate Planning (`caryestateplanning.com`, solo-adjacent, matches his actual
  practice — dossier evidence sheet):** long conversion scroll · proof directly under
  hero · 4-step process timeline · life-stage segmentation. **Stolen as pattern:**
  review proof immediately below the hero (our trust strip + review band) and the
  anti-category headline move ("Planning Not Paperwork") — ours is his own tagline
  doing the same anti-jargon work. **Refused:** their process timeline (we have no
  confirmed process facts — voice spec cuts it).
- **LegalPeel solo-lawyer gallery (2026 roundup, fetched):** cross-cutting solo
  patterns — 2–5 page structure · one CTA repeated 2–3× (never competing intents) ·
  headshot-forward about pages · micro-niche positioning ("service + town" titles).
  All adopted. **Cliché noted across the set:** navy-suit sameness, "compassionate &
  aggressive" copy — both refused.

**Synthesis:** the category's trust mechanics (phone everywhere, proof early,
credentials concrete) are non-negotiable and adopted; the category's *look* (navy,
columns, courthouse) is the cliché this direction exists to beat; warmth is carried
structurally (arches, plaster, domestic photography) so no copy ever has to claim it.

## 18. Handoff notes for the Builder

- Read `voice-spec.md` before writing ANY visible string; run `copycheck.py` +
  `aitells.py`; the S c. quote and the tagline are protected verbatim.
- Detector waivers expected: `cream-palette` (waive citing §1's stated exception).
  Nothing else should need one.
- Interactive QA: every practice card is one big click target (whole arch clickable,
  not just the title); form shows the inline demo confirmation; no dead clicks.
- JS-off: full page must read (motion rule 0 nets in place).
- Screenshots: desktop + 375px mobile to `screenshots/`, per contract.
- Release form: generate from `templates/release-form.html` with this client's name,
  contact, and the exact 5 pages; unknown fields stay blank lines.
