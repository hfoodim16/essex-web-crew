# Website plan — DaSilva & Associates, LLC · `paul-da-silva-law`

> **Speculative pitch.** `client-answers.md` is derived from the old site, not from Paul —
> treated as controlling per its own header. Every judgment call routes to the
> Confirm-with-Paul list; nothing is invented. Voice contract: `voice-spec.md` (written
> before this plan's hero direction; every copy direction below conforms to it).
>
> Builder: 4 English pages, static, opens by double-click. `mockup/index.html`,
> `practice-areas.html`, `attorney-bio.html`, `contact.html` + `style.css`, `main.js`,
> assets local in `mockup/assets/`.
>
> **REVISION 2 (2026-07-25) — client-directed palette change.** Harry reviewed the
> signed-off mockup and asked for "typical lawyer colors like blue and gold"; the lead
> offered the trade-off and Harry chose blue + gold with distinctiveness preserved through
> layout/typography/motion. This revision swaps the color system (§1 convention call, §3
> tokens, and the palette ripple in §4–§6, §9–§12, §14–§15). Everything else — page map,
> content map, typography, motion vocabulary, voice spec — is unchanged. The two generated
> images are KEPT (see §11 note).

---

## 1. Art direction — **"Ironbound Counsel"**

A Newark Portuguese-district law office rendered with old-world gravity: deep iron-gall
ink-blue grounds like the midnight ink of a ledger, an aged-brass accent like the fittings
of a banker's lamp, cool porcelain-stone body sections, and a Clarendon-serif voice. The
Ironbound identity is **structural, not decorative** — and under the blue palette the
azulejo-derived lattice motif becomes *genuinely* azulejo (blue is the tiles' true,
traditional color), so the Portuguese reference is now carried by an authentic material
language rather than a borrowed one. The two real language lines sit in the header of every
page as a first-class element, not a footnote; the split-screen advocacy layout, the
language/place hero construction, and the RTP-Portugal band carry the rest of the identity.
A scared family should read this in two seconds: *established, serious, local, speaks our
language, call this number.*

### The color-convention call — explicit (REVISED per client instruction)

- **The convention:** legal = **navy + gold + serif** (engine + `color-conventions.md`:
  "navy, burgundy, deep green, gold — authority, tradition, trust, gravitas"; the engine's
  conventional legal pairing is EB Garamond / Lato).
- **The call: HONOR the blue+gold convention — by client instruction — executed in its
  least-default registers.** Revision 1 broke to green+port; Harry reviewed and asked for
  typical lawyer blue and gold, so the honor/break decision is now settled by the client
  (the top authority). The design job becomes: honor the convention *without the template
  read*. So: not corporate navy (#1B2A4A-family) and never bright yellow-gold — instead a
  near-black **iron-gall ink blue** (`#131D33`, the color of a ledger's ink, darker and far
  less saturated than any firm-site navy) and an **aged brass** (`#B3873E`, the metal of a
  banker's-lamp fitting, nothing like #FFD700). The value structure stays dark-first and
  quiet; the hues are conventional, the registers are not.
- **What survives of the Ironbound identity:** the palette signal is gone, but the identity
  was never only the palette — and one piece actually *strengthens*: blue is the true,
  traditional color of Portuguese azulejo tile, so the §12 lattice motif (tile-geometry
  monolines on the dark ground) is now an authentic reference instead of a green
  abstraction. Kept structurally: the language lines as a first-class header element, the
  language/place hero construction, the split-screen advocacy layout, the RTP-Portugal
  commentary band, and the place-true Ironbound imagery.
- **Why it still avoids the generic template:** every generic firm site is *light-first*
  (white ground, navy headings, gold garnish). Ours is dark-first — ink ground with brass
  and porcelain — with a Clarendon display face, a split-screen archetype, clip-wipe
  motion, and an azulejo lattice no template ships. The convention is honored at the level
  of hue; the execution shares nothing else with the category default.
- **Collision check (re-run for the blue family):** fora-digital (banned row) uses **cobalt
  as a bright, saturated mid-tone accent** on warm paper, plus an interactive cobalt canvas.
  Our blue is the opposite role and value: a near-black, low-saturation **ground**, with the
  accent being brass — no bright blue accent exists anywhere in this palette. Light sections
  are a **cool porcelain** (`#F0F2F5`), not fora's warm cream. Nearest non-banned neighbor is
  john-sessa-cpa (porcelain + ink-navy, 4 rows back, outside the ban window): that site is
  light-first porcelain letterhead with a verdigris accent; ours is dark-first midnight with
  brass — different value structure, different accent family, different archetype.

## 2. Typography

- **Display: `Besley`** (Google Fonts; weights 700/800, + 400 italic for the rare pull-line).
  A Clarendon revival named for the typeface's 19th-century originator — sturdy, slab-
  bracketed serifs with genuine legal-ledger gravity. Used for: h1–h3, nav wordmark fallback,
  big phone number, section headings.
- **Body: `Schibsted Grotesk`** (Google Fonts; 400/500/700). Warm, contemporary, highly
  readable grotesk for body, lists, forms, captions, buttons.
- Never Inter/Roboto/Arial/Helvetica. Distinct from every design-memory row (no Besley or
  Schibsted anywhere in the log) and from the engine's conventional EB Garamond/Lato.

## 3. Color system (CSS `:root` tokens) — REVISION 2

| Token | Hex | Role | Replaces (Rev 1) |
|---|---|---|---|
| `--tinta` | `#131D33` | Deep iron-gall ink blue — header, hero ground, footer, dark bands | `--verde #14352A` |
| `--pedra` | `#F0F2F5` | Cool porcelain off-white — body/section background | `--stone #F1F3EE` |
| `--ink` | `#161A24` | Near-black blue-cast text on light grounds | `--ink #1B211D` |
| `--ouro` | `#B3873E` | Aged brass gold — primary CTA, accents, active states | `--porto #6E2B33` |
| `--linha` | `#C8CDD6` | Cool hairlines, borders, rules | `--linha #C7CEC6` |

(Portuguese token names kept — tinta = ink, pedra = stone, ouro = gold.) Light text on
`--tinta` is `--pedra`. All components reference tokens; no hardcoded hex.

**Contrast rules (builder verifies every pairing at final values):**
- CTA buttons: `--ouro` fill with `--tinta` (or `--ink`) label — ≈5:1, passes AA.
- `--ouro` on `--tinta`: large display text, rules, and accents only (≈4.9:1 — AA-large).
- `--ouro` on `--pedra` **fails AA for text** (≈2.9:1) — on light grounds brass is for
  rules/ornament only; any brass-toned *text* on light grounds uses the darkened shade
  `--ouro-escuro #806026` (a shade of ouro, not a sixth hue; ≈5:1 on pedra).
- Body text: `--ink` on `--pedra`; on-image text always over a `--tinta`-based scrim, AA
  re-checked against the actual images.

## 4. Anti-repetition (Stage 4 — crew log, last 3 rows banned)

Read `~/Projects/essex-web-crew/design-memory.md` 2026-07-25. Banned and avoided:

| Banned row | Fonts avoided | Palette family avoided | Archetype avoided | Motion avoided |
|---|---|---|---|---|
| cedar-grove-transmission | Archivo / Barlow | industrial graphite + steel + red | spec-sheet + bento | (triad hero also owned here) |
| happy-trees-by-mgm | Zilla Slab / Work Sans | bark + moss + sky + hi-vis lime | canopy-descent full-bleed | dapple/photo-scrim system |
| fora-digital | Instrument Serif / Hanken Grotesk | warm paper + ink + **cobalt** + clay | gallery-wall plates | mask-curtain entrance, underline-draw/fill-sweep hovers, `view()` gallery-hang, pointer field |

Specifically avoided combos (Rev 2): any **bright/saturated blue accent** (fora's cobalt —
our blue is a near-black, low-saturation *ground* and the accent is brass, so the palette
family reads "midnight + brass," not "blue-on-paper"), warm cream/parchment ground
(paper-and-ink collision — light sections are cool porcelain), bento/spec-sheet grids,
full-bleed photo-scrim scroll, gallery plates, mask-curtain + ink-sweep motion,
fade-up/count-up defaults. Steel-graphite-with-red (cedar-grove) untouched — brass ≠ red,
ink-blue ≠ graphite.

## 5. The three directions (Stage 5) + the pick

**Direction 1 — "Quiet Authority" (HONORS convention).**
Concept: the navy+gold firm site done unusually well — for trust-by-recognition.
Layout: centered-classic + credential strip · Type: EB Garamond / Lato · Palette: navy
`#1B2A4A` + gold `#B08D3E` + white (honors) · Background: flat + grain · Motion:
minimal-restrained, blur-focus entrance · Hero: Newark skyline dusk photo.
Why not: exactly the template the brief orders us to escape; cannot clear boldness ≥ 8.

**Direction 2 — "Ironbound Counsel" ← PICKED** *(Rev 1 shipped it as a green+port break;
Rev 2 re-grounds it in client-directed blue+gold — same direction, same structure, palette
re-registered per §1's revised convention call.)*
Concept: Portuguese-district law office as old-world institution — ledger ink, banker's
brass, porcelain; the language lines as identity.
Layout: **split-screen advocacy** (strong vertical division; dark identity panel / light
content panel) · Type: Besley / Schibsted Grotesk · Palette: tinta + pedra + ink + ouro
(honors convention in non-default registers, argued above) · Background: tinta ground +
azulejo-geometry monoline lattice + grain + warm lamp-glow · Motion: clip-wipe entrances +
lift hover · Hero: place-true Ironbound streetscape, warm late-afternoon light.
Why bold: no other firm in the category looks like this, yet every cue reads *established
law office*; the differentiator (language/place) is carried by structure, palette, and
header — not by a banner.

**Direction 3 — "Docket Broadsheet" (BREAKS hard).**
Concept: legal-notice brutalism — newsprint white, iron black, one signal red, oversized
condensed headlines, ruled columns like a court docket.
Layout: brutalist stack / magazine broken-grid · Type: condensed display (e.g. Archivo
Expanded family adjacent — problematic; would need a non-banned condensed face) · Palette:
monochrome + red pop (break) · Motion: kinetic marquee + snappy reveals.
Why not: visually the boldest, tonally wrong — alarmist energy aimed at a reader who is
already frightened, and its red/graphite family grazes cedar-grove's banned palette. Fails
the brief's "steady, unfrightening" constraint.

**Pick: Direction 2** — the boldest that fits the brief's constraints (Direction 3 is louder
but violates the emotional brief and grazes a ban). Axes check: the three differ on layout
archetype, typography, color strategy, background system, AND motion character (5/5).

## 6. Page map (4 pages — mirrors the old nav exactly, per dossier)

Shared on every page:
- **Header (tinta band):** real logo top-left (see §10) · nav: Home / Practice Areas /
  Attorney Bio / Contact · **language line "Se Habla Espanol · Nos falamos o portugues"**
  (verbatim, unaccented, protected) rendered as a first-class header element — a thin
  identity strip directly above or below the nav, NOT footnote-sized · **ouro tap-to-call
  button "Call 973-344-0808"** (tinta label on brass) visible in header at all sizes
  (becomes sticky bottom bar or prominent header button on mobile).
- **Footer (tinta):** logo (small) · NAP: DaSilva & Associates, LLC · 385 Lafayette Street,
  Newark, NJ 07105 · 973-344-0808 · Fax 973-344-3838 · language line · nav links ·
  `[Standard attorney-advertising / no-attorney-client-relationship disclaimer — for Paul's
  review]` clearly bracket-flagged · © 2026 DaSilva & Associates, LLC. Footer NAP must match
  JSON-LD exactly.

### index.html — Home
1. **Hero (split-screen):** left panel on tinta — h1 (language/place construction per
   voice-spec "Hero uniqueness": concept *"A Newark defense attorney who speaks your
   language."*), the two protected language lines directly beneath as proof, subhead ≤30
   words naming the four practice lines + "385 Lafayette Street, in Newark's Ironbound,
   since 2002," ouro call CTA + secondary "Send a message" link. Right panel: **GENERATE
   image A** (Ironbound streetscape, §11) with tinta-based scrim.
2. **Trust strip (pedra, hairline-ruled):** 4 real facts — *Founded May 2002* · *Former NJ
   Office of the Public Defender* · *Fluent in Portuguese and Spanish* · *Legal commentator,
   CourtTV & RTP-Portugal*. No invented stats, no count-up.
3. **Practice areas (4 cards → practice-areas.html anchors):** Criminal Defense · Traffic ·
   Family Law · Real Estate, in that order (client-answers Q9). Card ≤25 words each, drawn
   from the real service lists.
4. **About band (split, pedra):** ≤90 words carrying the home page's real facts (founded May
   2002; personal approach to every case; practical, precise approach that avoids needless
   litigation costs) + **GENERATE image B** (office interior, §11).
5. **Commentary band (tinta):** the buried best proof point, surfaced: "Frequent guest
   commentator on CourtTV and RTP-Portugal" — RTP given equal-or-greater visual weight (a
   Portuguese national broadcaster puts him on air as a legal expert). Plain statement +
   link to Attorney Bio. No fake logos of the networks (text names only).
6. **Client reviews (pedra):** heading "Client reviews · Lawyer.com" + the 3 real quotes,
   verbatim, attributed (Ted DeCagna · Beli Pacheco · Moses Apsan, Lawyer.com). Nothing else.
7. **Contact CTA band (tinta):** big Besley phone number (tap-to-call), address line, one
   ≤20-word line, "Send a message" secondary → contact.html.

### practice-areas.html
1. Page header (tinta, compact): h1 "Practice Areas" + one-line intro.
2. **#criminal — Criminal Defense** (leads; deepest section): intro ≤40 words ("decades of
   experience" old claim carried as: criminal work since the Public Defender years — keep
   factual), then 4 sub-blocks ≤35 words each: DUI/DWI & Vehicular Crimes (first-time and
   repeat offenses; administrative process of protecting driving privileges) · Sex Offenses
   (rape, statutory rape, child pornography, sexual assault) · Violent Crimes & Weapon
   Offenses (murder, manslaughter, robbery, burglary, assault, firearms) · Drug Crimes
   (possession, distribution, trafficking, prescription drugs).
3. **#traffic — Traffic Law** (thin by design, per voice-spec): violations list (driving
   without a license, suspended license, reckless driving, uninsured driving, speeding) +
   one sentence stating the *goal* — reduce or dismiss charges and minimize license points
   (goal phrasing, never a promise).
4. **#family — Family Law:** intro ("understanding and discretion" — their framing) + list:
   divorce · alimony · child support · child custody · domestic violence · pre- and
   post-nuptial agreements · juvenile delinquency and dependency proceedings.
5. **#real — Real Estate:** intro (protecting clients' interests from offer through closing)
   + list: purchase and sale agreements · title searches · leases and rental agreements ·
   co-op and condominium transactions.
6. Contact CTA band (shared component).

Anchor IDs `#criminal #traffic #family #real` preserved from the old site so the home-page
quick links map 1:1 (parity nicety). **Page order Criminal → Traffic → Family → Real Estate
(Q9)** even though the old page ran Real Estate first — log in Client answers → decisions.

### attorney-bio.html
1. Page header: h1 "Paul Da Silva" + one-line role.
2. **Portrait: labeled PLACEHOLDER** (styled frame, "Photo of Paul Da Silva — real headshot
   to come"; NEVER generated — hard rule).
3. Bio narrative ≤160 words: born and raised in New Jersey, son of immigrant parents; fluent
   in both Portuguese and Spanish; founded the firm May 2002. (The old site's "aggressive
   and dedicated advocate" phrasing is NOT carried — banned word; the facts are.)
4. **Timeline (education + career):** Rutgers BA Political Science, Criminology minor, 1993 ·
   Touro Law School (Jacob D. Fuchsberg Law Center) JD 1996, Moot Court Board · Legal Aid
   Society of Manhattan · Legal Aid Society of Nassau County · NJ Office of the Public
   Defender — litigated criminal cases including murder trials · boutique litigation firm,
   Montclair NJ (criminal, family, real-estate matters) · founded DaSilva & Associates, May
   2002.
5. **Recognition block:** CourtTV & RTP-Portugal commentary · former Adjunct Professor,
   Fairleigh Dickinson University · Hudson County Ethics Committee, 4 years.
6. Personal: one sentence (married, two children; tennis and hockey).
7. Contact CTA band.

### contact.html
1. Page header: h1 "Contact."
2. **Phone-dominant block:** the number huge in Besley, tap-to-call; fax beneath; full
   address with "in Newark's Ironbound."
3. **Form placeholder (≤4 fields):** Name · Phone · What happened (textarea) · submit
   ("Send"). Static demo: inline confirmation message on submit ("Thanks — we'll call you
   back at the number you gave." — builder finalizes per voice spec), never a dead click.
   HTML comment marking where a real form service goes.
4. **Map embed placeholder:** labeled block ("Google Map — 385 Lafayette Street") — the
   Ironbound address is the credential, so the map earns its place. HTML comment for the
   real embed.
5. NO email (none exists — never invent), NO hours, NO booking widget.

## 7. Content map (content-parity contract — every `site-content.md` block placed)

| site-content.md block | Destination |
|---|---|
| Site-wide header: firm name, phone, fax, address, language line | Header + footer, every page (fax: footer + contact page) |
| Footer copyright (spelling "Da Silva") | Footer, standardized to **DaSilva** (Q1; Confirm #1) |
| Nav (4 pages) | Same 4-page nav |
| Home ¶1 (founded May 2002, attentive/professional, personal approach) | Home §4 about band (facts carried; ≤90 words) |
| Home ¶2 (routine-for-attorney-not-for-client premise; practical & precise approach; avoiding needless litigation costs) | Home §4 about band + hero subhead territory. The "best choice" superlative phrasing not carried (voice spec); every fact is |
| Home practice-area quick links (4 anchors) | Home §3 cards → same anchors on practice-areas.html |
| Practice: Real Estate intro + 4-item list | practice-areas.html #real, complete list |
| Practice: Family Law intro + 7-item list | practice-areas.html #family, complete list |
| Practice: Criminal intro + 4 sub-blocks (all sub-lists) | practice-areas.html #criminal, all four sub-blocks, every named offense carried |
| Practice: Traffic list + aim | practice-areas.html #traffic (goal phrasing) |
| Bio: fluency, born/raised NJ, son of immigrant parents | attorney-bio.html §3 + home hero/trust strip (fluency) |
| Bio: education (Rutgers '93, Touro JD '96, Moot Court) | attorney-bio.html timeline |
| Bio: prior employment (all 5 entries incl. murder-trial litigation) | attorney-bio.html timeline |
| Bio: accomplishments (CourtTV/RTP, FDU adjunct, Ethics Committee 4 yrs) | attorney-bio.html recognition + home §5 commentary band |
| Bio: personal (married, 2 children, tennis, hockey) | attorney-bio.html §6, one sentence |
| Contact: phone/fax/address repeat | contact.html phone-dominant block |
| Contact form fields Name, Phone, Description of Service | contact.html form (Description → "What happened") |

**Deliberately dropped (no silent drops):**
- **GTranslate EN/PT/ES flag widget** — confirmed machine-translate widget, not real
  translated content (dossier); parity-neutral to drop. Real PT/ES pages = Confirm #8.
- **Form fields: Company Name, Email, Address, City, State/Province/Region, ZIP, Website,
  How Did You Hear** — an 11-field form is a serious mismatch for someone contacting a
  criminal-defense attorney in an emergency (site-content.md builder note); cut to 3 fields,
  phone dominant. (Email *field* on the form is also cut — call-back by phone is the ask; the
  firm publishes no email to receive replies at anyway.)
- **Old stock imagery (office-exterior + courthouse columns)** — generic stock, could be any
  firm anywhere (dossier critique); replaced by place-true generated imagery + labeled
  placeholders. Stock is banned regardless.
- **"the best choice" / "aggressive and dedicated advocate" phrasing** — phrasing only, not
  facts (parity counts facts); banned by voice spec + bar-advertising rules. All underlying
  facts are carried above.

## 8. Client answers → decisions (every numbered item)

| Q | Answer | Plan decision |
|---|---|---|
| 1 | DaSilva & Associates, LLC (spelling inconsistent on old site) | Standardized to "DaSilva & Associates, LLC" sitewide — header, footer, JSON-LD, title. Confirm #1 |
| 2 | Founded May 2002; Legal Aid ×2 → Public Defender → Montclair firm | About band (home) + full timeline (bio page). "Since 2002" used as the era fact |
| 3 | Attentive/professional, personal approach, practical & precise; REAL differentiator = PT/ES fluency + Ironbound address | The differentiator is the art direction itself (§1): language lines in the header sitewide, hero headline construction, palette carrying the Portuguese identity. Their own framing phrases in the sounds-like bank |
| 4 | Towns served UNKNOWN | **No service-area list anywhere.** Address block anchors geography. Confirm #7 |
| 5 | Site's job: found fast → sees his charge → sees his language → calls | Phone CTA in header on every page + hero CTA + contact band on every page; practice-area cards above the fold-adjacent on home; language lines in header |
| 6 | Best customers: defendants + families, drivers, divorcing families, closings; PT/ES-weighted | Copy written to "you/your family" (voice spec); practice order matches; language proof up top |
| 7 | How found today: UNKNOWN | No decision needed on-site. Confirm list |
| 8 | Full service list (verbatim structure) | Carried complete — content map §7; every named offense/item appears |
| 9 | Priority: Criminal → Traffic → Family → Real Estate | Card order (home) + section order (practice page) exactly this. Confirm #5 notes Real Estate may deserve promotion |
| 10 | Nothing being phased out (unknown) | Everything advertised is carried |
| 11 | No specials; no free consult stated | **No free-consultation language anywhere** (voice-spec bar rule). Confirm #6 |
| 12–13 | Likes/bugs about current site: UNKNOWN | Defaults from dossier critique: bury nothing, phone dominant, no stock |
| 14 | Must keep word-for-word: "Se Habla Espanol" / "Nos falamos o portugues", unaccented | Protected strings (voice spec) — header element every page + beneath hero h1. Never "corrected." Confirm #9 (accents) |
| 15 | Three words: steady, plain-spoken, local | Voice-spec register; direction's restraint; no alarmist urgency anywhere |
| 15b | How he talks: UNKNOWN | Tier 2 professional-office preset (voice spec); no salesmanship, no outcome promises, no clichés |
| 16 | Sites he likes: UNKNOWN | Stage 3 evidence sheet (§13) stands in. Confirm list |
| 17 | Colors wanted: UNKNOWN | Planner's call per Q18's own art-direction instruction — §1, break argued explicitly |
| 18 | Logo: keep/fresh UNKNOWN; analyst found the real logo | **Real logo used** — §10 cites the dossier URL; header top-left + footer. Never redrawn |
| 19 | Photos they have: UNKNOWN (stock only) | 2 GENERATE slots + labeled placeholders (§11). No stock |
| 20 | Should be photographed: storefront + Paul | Both are placeholders-by-design: Paul = labeled headshot frame (never generated); real storefront photo = Confirm #10. Generated street image is atmospheric/place-true, explicitly NOT his actual office |
| 21 | Old site has zero reviews; analyst found 3 real ones | Reviews section (home §6) uses exactly the 3 Lawyer.com quotes, verbatim + attributed. Nothing invented. Confirm #11 (courtesy check) |
| 22 | Credentials list (Rutgers, Touro, Legal Aid, PD, FDU, Ethics Cmte, Moot Court, CourtTV/RTP) | Trust strip (home §2), commentary band (home §5), full bio page. **RTP-Portugal given real weight** per the answers' own note. **No bar admissions stated** — Confirm #4 |
| 23 | Ready to hire → call 973-344-0808 | Primary CTA sitewide, tap-to-call `tel:` link; form is secondary |
| 24 | Phone + fax real; NO email, NO hours anywhere | Phone/fax everywhere appropriate; **no email, no hours, no `openingHours` JSON-LD, nothing invented.** Confirm #2, #3 |
| 25 | Show the address | Address in header-adjacent footer, hero subhead, contact page, JSON-LD; "Ironbound" named — the address is the credential |
| 26 | FAQ material: UNKNOWN | **No FAQ anywhere** (voice-spec cut). Confirm #14 |
| 27 | Policies/fees: UNKNOWN | No fee/retainer/payment content. Footer disclaimer ships bracket-flagged for Paul's review, not asserted |
| 28 | Doesn't want on site: UNKNOWN | Nothing speculative added anywhere; conservative defaults |
| 29 | Domain: pauldasilvalaw.com (his) | Canonical + OG URLs reference it; no domain purchase needed |
| 30 | Reach him: Harry's job | No decision on-site |

No contradictions found in the answers; all ambiguity already routes to the Confirm list
(nothing new to flag beyond the list as written — §14 adds none).

## 9. Hero direction

Obeys `voice-spec.md` (headline 3–9 words; no triad — cedar-grove owns it; no "Built…"
construction; checked against all prospect heroes 2026-07-25).
- **Headline concept:** the language/place construction — *"A Newark defense attorney who
  speaks your language."* (8 words). Alternate within spec: *"24 years of defense work in
  the Ironbound."* Builder picks/refines against the spec; no outcome language.
- **Sub-copy angle (≤30 words):** the four practice lines + address + since-2002 — pure
  specification, e.g. criminal defense, traffic, family law, and real estate closings at
  385 Lafayette Street since 2002.
- **Proof row directly under the h1:** the two protected language lines, verbatim, styled as
  a quiet identity strip (small caps or hairline-ruled row) — never a decorative flag.
- **CTA pair:** ouro button "Call 973-344-0808" (`tel:`, tinta label) + text link "Send a
  message."
- **Hero image intent:** place-true Ironbound streetscape (GENERATE A, §11), right panel of
  the split, scrim ensuring AA contrast for anything overlapping.

## 10. Real logo (hard rule)

Dossier Logo line: `https://pauldasilvalaw.com/wp-content/uploads/2022/03/1AAA-DaSilva-LOGO-6IN-CLIP-CLEAR.png`
(transparent PNG wordmark lockup, used in the old site's header and footer). Builder:
`curl -L -o mockup/assets/logo.png "<that URL>"`, place top-left in the header with
`alt="DaSilva & Associates, LLC logo"` and small in the footer. Local file, never hotlinked,
never redrawn, never replaced with a text wordmark. If the PNG is dark-on-transparent and
unreadable on the tinta header, the builder may place it on a small pedra chip/plate behind
it — never recolor the mark itself. (Rev 2 ripple: re-check the logo's legibility against
the new tinta ground.) (Fallback only if the URL is dead: flag the lead;
do NOT substitute a wordmark without the lead's OK.)

## 11. Image list — exactly 2 GENERATE, rest PLACEHOLDER

> **Rev 2 note (amended after critic's in-context review):** the hero (slot A) is KEPT —
> warm brick/neutral streetscape, naturally complementary to midnight+brass, do not
> regenerate. Slot B's first generation rendered distinctly GREEN walls — the one element
> left of the Rev 1 palette, and the thing the client (who reopened specifically over
> color) would notice first. **Slot B is REGENERATED once as a replacement** (within the
> 2-image cap; ~$0.04 at 1K) using the amended prompt below — same room concept and
> register, walls moved to a soft blue-gray, and the brass banker's lamp kept as the
> palette motif. Builder ripple: re-check scrim color (tinta-based) and text-over-image AA
> on both final images.

**Register (ONE for the whole site): proud-contractor, "place-true documentary" calibration.**
Justification for not using editorial: a solo Newark attorney would not plausibly commission
a cinematic shoot; the images must read like excellent real photos of his actual
neighborhood — believable phone/consumer-camera photography, pleasant natural light, level
framing. Both fail modes rejected: stock-ad gloss AND dreary shabbiness. Hard rules for both
slots: **no readable signage, lettering, awnings text, street signs, license plates, seals,
courthouse iconography, diplomas — and never Paul's face or any identifiable person.**

| # | Slot | Status | Spec |
|---|---|---|---|
| A | Home hero, split-screen right panel (also cropped for OG image) | **GENERATE** | `16:9 · 2K` (renders near-full-bleed on desktop). Prompt: *"A photograph of a Newark New Jersey Ironbound neighborhood commercial street in warm late-afternoon light — three-story brick row buildings with ground-floor storefronts, awnings, parked cars, a few street trees, long soft shadows, taken with a phone, good consumer-camera quality, level horizon, honest straight-on framing, subtle grain, natural imperfections, deep green and warm brick tones; no phone UI, no on-screen icons, no status bar, no timestamp overlay, no screen chrome, no readable signage, no lettering, no legible text anywhere, no license plates, no branding, no logos, no people, no illustration, no 3D render, no CGI, no painting, no oversaturation, no plastic or waxy textures, no perfect symmetry, no watermark"* |
| B | Home about band (contained split image) | **GENERATE** (Rev 2 replacement — regenerate once) | `4:3 · 1K` (contained). Different subject/space from A per distinct-property rule. Amended Rev 2 prompt: *"A photograph of a modest, orderly law office consultation room by a large window — soft blue-gray painted walls, dark wood desk, two leather client chairs, a brass banker's lamp with a warm cream glass shade on the desk, neat file folders and legal pads, warm natural daylight from the window, taken with a phone, good consumer-camera quality, level framing, subtle grain, natural imperfections, deep blue and warm wood tones; no green glass, no green objects, no phone UI, no on-screen icons, no status bar, no timestamp overlay, no screen chrome, no readable text, no documents with legible writing, no diplomas, no certificates, no seals, no flags, no signage, no logos, no branding, no people, no illustration, no 3D render, no CGI, no painting, no oversaturation, no plastic or waxy textures, no perfect symmetry, no watermark"* — (Rev 1 prompt superseded; first Rev 2 take passed realism but rendered the lamp's iconic green shade — one shade-fix retry authorized as this prompt's single QA retry, with the passing green-shade take held as the fallback if the retry fails) |
| C | Attorney bio portrait | PLACEHOLDER | Styled frame, `3:4`, label: "Photo of Paul Da Silva — real headshot to come." **Never generate his likeness** |
| D | Contact page map | PLACEHOLDER (embed) | Labeled Google-Map embed block, "385 Lafayette Street, Newark" + HTML comment for the real embed |
| E | Practice-areas page header backdrop (optional texture slot) | PLACEHOLDER | Labeled AI-IMAGE box only if the layout wants it; otherwise use the §12 lattice/gradient treatment — no third generation |

Post-process both GENERATE images to WebP (`media_optimizer.py`, quality ~85), downscaled to
real display width, stored in `mockup/assets/`, referenced locally. OG image = cropped A
(1200×630), brand text composited in the build, never in the generation.

## 12. Motion + background & atmosphere

**Signature moves (distinct from last 3 rows — fora's mask-curtain/ink-sweep, happy-trees'
scrim system, and the flagged fade-up/count-up defaults are all avoided):**
- **Entrance family: clip-wipe** — content revealed by an expanding clip rectangle (crisp,
  document-like; an "unredacting" feel that suits a law office without saying so). Delivered
  via IntersectionObserver `.in`, once, threshold ~.12; stagger-cascade `--i` delays ≤70ms
  on card/list groups (cap 12).
- **Hover personality: lift + tilt (≤2°)** + shadow deepen on cards; pressed state
  `scale(.97)` on everything clickable. Guarded by `(hover:hover) and (pointer:fine)`.
- **Scroll set-piece: none.** At most a subtle hero-image parallax (~0.85×, hero only,
  skipped on `pointer:coarse`) — optional, builder's call, and it is the single allowed
  set-piece if used.
- No count-up anywhere (trust strip is typographic facts, not animated numbers).

**Background & atmosphere (from `backgrounds.md` + `atmosphere.md` free recipes) — Rev 2:**
- Tinta grounds (header/hero/commentary band/footer): deep ink-blue base + **azulejo
  tile-geometry monoline SVG lattice** — the geometric line pattern drawn in a
  barely-lighter ink blue (~6–8% lighter, same low saturation — never cobalt-bright) at low
  opacity, + the standard **grain overlay**. Under blue this is now a genuine azulejo
  reference (blue is the tiles' true color) while staying subliminal — geometry, never
  literal tile clip-art.
- Hero: one **warm lamp-glow radial** (soft brass-tinted `#EAD9AE` radial, alpha ≤ .18)
  breathing very slowly over the tinta panel — brass lamplight on midnight ink; the
  blue/gold complement makes this effect stronger than it was on green. Single atmosphere
  effect, `will-change` promoted, killed under `prefers-reduced-motion`.
- Pedra body sections: flat porcelain + hairline `--linha` rules; generous whitespace does
  the work. Section seams: simple rules, no angled dividers (keep the document discipline).
- Atmosphere budget: 1 effect (the lamp glow). No fog, no god-rays stack, no orbs.

All motion gated behind `prefers-reduced-motion: reduce`; transforms/opacity only.

## 13. Stage 3 evidence sheet (patterns, never copies)

- **Charge-recognition speed** (Andrew Flusche pattern, via Juris Digital roundup): a person
  in trouble must see their exact matter named fast → 4 practice cards immediately after the
  hero; sub-offenses named on the practice page.
- **Bold phone at top + repetition** (Jeff Higgins pattern): number in the header on every
  page, hero CTA, closing band every page.
- **High-contrast non-navy palette can still read serious** (Moses & Rooth's red/white):
  supports the convention break — restraint + type gravity carry the seriousness.
- **Mobile-upfront critical info** (Gounaris Abboud): mobile header keeps tap-to-call +
  language line above everything; §"Mobile" below.
- **"Se Habla" as checkbox vs identity** (Nanato Media's bilingual-design critique): a small
  header badge is the checkbox everyone does; making language capability a hero-level,
  structural element is the differentiator — exactly what this plan does.
- **Solo-attorney restraint** (dossier's reference note): one attorney, one voice, personal
  bio, no fake "team" page, no boardroom stock.

## 14. Content honesty notes (builder writes around these)

- **No email** exists — never render one, not in footer, form copy, or JSON-LD.
- **No hours** — no hours block, no `openingHours`.
- **No bar admissions** — never state NJ/NY licensure (aggregator hint is not sourcing).
- **No case results, win rates, or outcome promises**; traffic "reduce or dismiss" is a goal.
- **No free consultation**, fees, or payment terms.
- **No service-area town list.**
- **"24 years"** derives from the site's own "founded May 2002" — prefer "since 2002" /
  "founded May 2002" phrasing (self-anchoring, ages gracefully).
- **Footer disclaimer** ships bracket-flagged `[…for Paul's review]`.
- **JSON-LD:** `LegalService` (or `Attorney`) — name DaSilva & Associates, LLC, address 385
  Lafayette Street Newark NJ 07105, telephone +1-973-344-0808, faxNumber, url
  pauldasilvalaw.com, founder Paul Da Silva; **omit email and openingHours entirely.** NAP
  identical to footer. Meta title/description name the services + Newark/Ironbound;
  canonical to pauldasilvalaw.com; OG tags + inline SVG favicon (a "DA" ligature or scale-free
  monogram is NOT allowed — no invented marks; favicon should derive from the real logo or be
  a plain typographic "D" in Besley on tinta, which is typography, not a fabricated crest).

## 15. Mobile notes (designed, not shrunk)

375px: hamburger nav; language line stays visible in the compact header (it IS the identity —
may shrink to one line, never disappear); sticky bottom tap-to-call bar in ouro (tinta
label) on all pages; hero stacks (text panel first, image below at 16:9 crop); trust strip wraps to 2×2;
practice cards stack full-width; timeline collapses to a single rail; contact page leads with
the giant number. Screenshots (desktop + 375px) mandatory → `screenshots/`.

## 16. Voice spec cross-reference

`prospects/paul-da-silva-law/voice-spec.md` — written before this plan's hero direction, per
trade-copy Stage A. Every visible string is drafted against it; builder runs
`python3 skills/trade-copy/scripts/copycheck.py` on **all four pages** + the `--list` sweep +
cold read before handoff. Tier 2 banlist + the site-specific watch list (no "aggressive,"
no "results," no "navigate," etc.) apply to every page.

---
---

## Rev 3 (2026-07-29) — type + layout overhaul, Harry-directed

> **Controlling brief: `revision-brief-rev3.md`.** Harry reopened the signed-off Rev 2 site:
> *"Keep the colors, and info. I like how the info is shown in blocks, but I don't love font
> and format as a whole please change with the team."* So: **palette frozen (all nine tokens,
> verbatim), all content frozen, voice-spec frozen, both real images frozen, real logo frozen,
> the live map iframe in contact.html frozen. Typography, layout grammar, ground rhythm,
> background system, and motion are ALL replaced.** The Rev 2 record above stays load-bearing
> for the content map, palette rationale, and honesty notes; wherever Rev 2's layout,
> typography, or motion specs conflict with this section, **Rev 3 wins.**
>
> **Stage 3 note (lead instruction):** this round's inspiration stage ran off the **local
> `ui-ux-pro-max` database** (styles / palettes / 74 font pairings / UX guidelines / motion
> presets) plus the skill's own `references/inspiration.md` pattern vocabulary — **no live-site
> WebSearch/WebFetch**, by lead instruction after a prior attempt stalled on live research.

## R3-1. Art direction — **"Counsel of Record"**

*Counsel of record* is the attorney officially entered on a case's docket — and this design
renders the firm the way a serious legal record reads: a **light-first, hairline-ruled ledger**
set in Caslon, the typeface lawyers have trusted in briefs for two centuries. Porcelain pages
carry the information in **rule-bounded compartments** (Harry's blocks, kept — but composed
like a ledger, not stacked like cards); deep ink bands punctuate rather than dominate; brass
appears as drawn rules, index numerals, and the call button — the fittings on the record, not
the wallpaper. Where Rev 2 was a dark split-screen you looked *into*, Rev 3 is a document you
*hold*: at a glance it is an obviously different site (the bold test), yet every cue still says
*established, serious, local, speaks our language, call this number*.

**The format flip in one line:** dark-first split-screen → **light-first ruled modular ledger**;
floating rounded cards → **flat, square, rule-bounded compartments that share their hairlines
like ledger cells**; centered dark bands → **asymmetric ink punctuation**.

## R3-2. Typography (all-new system — Besley / Schibsted Grotesk retired)

- **Display: `Libre Caslon Text`** (Google Fonts; 400, 400 italic, 700). Caslon is the
  historical setting face of the American legal profession — old-style, inky, unshowy. It reads
  *counsel*, not *studio*. Used for: h1–h3, the big phone numbers, index numerals (italic), the
  protected language lines (400 italic), review quotes (400 italic).
- **Body: `Albert Sans`** (Google Fonts; **variable**, use 400/500/600). Humanist-geometric,
  warm, plain-spoken; the variable axis powers the weight-shift hover (R3-7). Used for: body,
  lists, nav, labels, forms, buttons, captions.
- **Ban check:** neither family appears in any `design-memory.md` row; neither is on the banned
  set (Inter/Roboto/Arial/Helvetica/Fraunces/Instrument Serif/Geist/Plus Jakarta Sans/Space
  Grotesk) nor in the last-3-rows pairings (Zilla Slab/Work Sans · Instrument Serif/Hanken
  Grotesk · Besley/Schibsted Grotesk). Deliberately NOT the engine's conventional legal pairing
  (EB Garamond/Lato): Caslon is sturdier at text sizes than Garamond and Albert Sans is warmer
  than Lato — convention-adjacent gravity without the category default.

**The type system, with numbers (builder implements exactly):**

| Role | Face / weight | Size / leading | Tracking / case |
|---|---|---|---|
| Hero h1 (home) | Libre Caslon Text 700 | `clamp(2.75rem, 6.5vw, 5rem)` / 1.04 | −0.015em |
| Interior h1 | Libre Caslon Text 700 | `clamp(2.4rem, 5vw, 3.5rem)` / 1.08 | −0.012em |
| h2 section | Libre Caslon Text 700 | `clamp(1.75rem, 3vw, 2.5rem)` / 1.12 | −0.01em |
| h3 block heading | Libre Caslon Text 700 | 1.375rem / 1.25 | −0.005em |
| Big phone (CTA band / contact) | Libre Caslon Text 700, `font-variant-numeric: lining-nums` | `clamp(2.5rem, 7vw, 4.5rem)` / 1 | −0.01em |
| Ledger label (replaces the eyebrow) | Albert Sans 600 | 0.8125rem / 1.4 | +0.09em, UPPERCASE |
| Index numeral (01–04) | Libre Caslon Text 400 italic | 2.5rem / 1 | 0 |
| Body | Albert Sans 400 | 1.0625rem / 1.65 | 0 |
| Lead paragraph | Albert Sans 400 | 1.1875rem / 1.6 | 0 |
| Small / captions / footer | Albert Sans 400 | 0.875rem / 1.5 | +0.01em |
| Nav / buttons / go-links | Albert Sans 500 | 0.9375rem / 1.2 | +0.02em |
| Language lines (protected strings) | Libre Caslon Text 400 **italic** | 1.0625rem / 1.4 | +0.01em |
| Review quotes | Libre Caslon Text 400 italic | 1.25rem / 1.5 | 0 |

**How a block's heading relates to its body:** every compartment runs *label → rule → heading →
body*: ledger label (Albert Sans 600 caps, brass `--ouro-escuro` on light / `--lamp` on ink) ·
8px gap · a 1px `--linha` rule the width of the text column · 12px gap · h3 in Caslon 700 at
≈1.3× body size · 8px gap · Albert Sans body. Weight contrast is carried by **genus, not just
weight**: inky serif display against a light humanist sans, with the brass caps label as the
middle voice. No gradient text, no letter-spaced display serif, no all-caps Caslon ever.

## R3-3. Color system — **frozen verbatim** (Rev 2 tokens, zero changes)

```css
:root{
  --tinta:#131D33; --tinta-2:#0D1526; --pedra:#F0F2F5; --ink:#161A24;
  --ouro:#B3873E; --ouro-escuro:#806026; --muted:#566072; --linha:#C8CDD6;
  --lamp:#EAD9AE;
}
```
Same nine names, same nine hex — no new hues, no tints outside these. **What changes is
proportion and placement (allowed by the brief):** Rev 2 was dark-first (~55% ink grounds);
Rev 3 is **light-first — roughly 70% porcelain `--pedra` (with pure `#fff` only as compartment
fill on pedra, already the Rev 2 precedent), ~30% ink** (`--tinta` punctuation bands, `--tinta-2`
footer). Brass moves from "CTA + lamp-glow atmosphere" to **drawn structure**: rules, index
numerals, corner ticks, and the call button. `--lamp` shrinks to small type on ink (labels,
links on dark) and the glint highlight (R3-8). All Rev 2 contrast rules stand: `--ouro` is
never body-text on light grounds (use `--ouro-escuro`, ≈5:1 on pedra); body is `--ink` on
`--pedra`; text on ink grounds is `--pedra`/`--linha`/`--lamp`.

**Detector waiver, pre-stated:** this palette is warm-brass-on-ink and **client-locked** (Harry
chose blue+gold in Rev 2 and froze it in the Rev 3 brief). If any `cream-palette`-family or
premium-consumer-palette rule fires on pedra + brass, the builder waives it in-file:
`<!-- impeccable-disable <rule> -- palette client-locked per revision-brief-rev3.md; carried from signed-off Rev 2 -->`.

## R3-4. Anti-repetition (Stage 4 — read 2026-07-29)

Last 3 rows banned: **happy-trees** (Zilla Slab/Work Sans · bark/moss/lime · canopy-descent
full-bleed · dapple/photo-scrim), **fora-digital** (Instrument Serif/Hanken Grotesk · paper/ink/
cobalt/clay · gallery-wall plates · mask-curtain + ink-sweep/underline-draw hovers + `view()`
gallery-hang + pointer field), **paul-da-silva-law Rev 2 itself** (Besley/Schibsted Grotesk ·
split-screen advocacy + document stack · azulejo lattice + grain + lamp-glow · clip-wipe +
lift/tilt + hero parallax). All avoided — Rev 3 shares no font, archetype, background recipe,
entrance, or hover with any of the three.

**Softer-sameness checks (older rows, for the critic's cold eye):**
- **john-sessa-cpa** (5 rows back) is the nearest light neighbor: porcelain + ink-navy,
  sidebar-anchored letterhead, dot-grid graph paper. Rev 3 deliberately differs: modular ruled
  ledger (not a sidebar letterhead), Caslon/Albert Sans (not Spectral/Public Sans), **no dot
  grid anywhere**, brass accent (not verdigris), and ink punctuation bands john-sessa never had.
- **cedar-grove** bento: our compartments **share collapsed hairline rules and run square to
  full-bleed section rules** — a ledger table, not gap-separated rounded bento tiles.
- **fora** gallery plates: no framed floating plates, no warm paper (pedra is cool), no cobalt.

## R3-5. The three directions (Stage 5, palette-frozen — divergence on composition, type,
ground rhythm, background, motion) + the pick

**Direction A — "Counsel of Record" ← PICKED.**
Concept: the firm as a serious legal record — light-first ruled ledger a frightened family can
actually read. Layout: **Swiss/modular ruled grid + ledger compartments** (named per
`inspiration.md`: editorial masthead hero · Swiss/modular grid · flat bordered containers ·
service index/ledger) · Type: Libre Caslon Text / Albert Sans · Grounds: ~70% pedra, ink as
punctuation · Background: ledger rule-field + corner washes + grain + one brass glint sweep ·
Motion: line-draw entrance, weight-shift hover, sticky-progress index rail (practice page only),
GSAP tier 0. Why bold: a full value-structure flip from Rev 2 — passes the bold test at a
glance — and nobody in this category ships a ruled-ledger law site; the gravity comes from
Caslon and drawn rules instead of dark panels.

**Direction B — "Standing Counsel" (not picked).**
Concept: dark-first monumental civic register — oversized Newsreader display over ink,
porcelain plates overlapping dark grounds, brass frame lines. Type: Newsreader (opsz) / IBM
Plex Sans · Background: duotone-scrim imagery + grain · Motion: split-line mask `[GSAP tier 2]`
+ zoom-crop hover + hero-exit. Why not: it stays **dark-first** — the weakest possible answer
to "I don't love the format as a whole," and it spends a GSAP tier this site doesn't need.

**Direction C — "Primeira Página" (not picked).**
Concept: broadsheet front page — nameplate masthead, column rules, dateline small caps,
all-serif print grammar (Playfair Display / Source Serif 4) · Background: flat newsprint +
rules · Motion: scale-settle + crossfade-zoom. Why not: newspaper grammar reads *coverage of
crime*, not *counsel* — the same alarmist-register failure that killed Rev 2's "Docket
Broadsheet" — and Playfair drifts fashion-editorial.

Axes check: A/B differ on grounds, layout, type, background, motion (5); A/C differ on layout,
type genus mix, background, motion (4); B/C differ on grounds, layout, type, motion (4).
**Pick: A** — the boldest that answers Harry's actual complaint (the format), stated per Stage 5
autonomous rule. The color-convention call is settled and inherited: the palette **honors**
legal blue+gold by client instruction (Rev 2 §1's argument stands verbatim); Rev 3 only
re-proportions it light-first, which moves it *further* from the generic dark-navy firm site.

## R3-6. The block system, re-composed (Harry's keeper, new grammar)

The bounded info block stays the organizing unit. Its Rev 3 grammar:

- **Border/ground:** square corners (`--radius: 0` for compartments), 1px `--linha` borders that
  **collapse between neighbors** (adjacent compartments share one hairline, like ledger cells —
  build as a bordered grid wrapper with `gap:0` and single interior rules, not per-card borders
  that double up). Fill: `#fff` compartments on the `--pedra` page ground; on ink bands,
  compartments are borderless fields divided by `--linha` rules at ~28% opacity.
- **Label:** every compartment opens with the ledger label (Albert Sans 600 caps, brass) over a
  text-column-width rule — see R3-2. This replaces Rev 2's floating eyebrow.
- **Scale contrast:** compartments are sized by the weight of their content, not stamped equal.
  On a 12-column grid the home practice row runs **Criminal 7 / Traffic 5** over
  **Family 6 / Real Estate 6** (Criminal reads visibly senior — it's the practice's own
  emphasis, Q9). Never four identical cards in a row again.
- **Index numerals:** 01–04 set large (2.5rem) in Libre Caslon Text 400 *italic*, `--ouro`
  (on white) / `--lamp` (on ink), top-right of the compartment — the brass folio number.
- **Blocks meet section edges:** section-framing rules run **full-bleed edge to edge** of the
  viewport; the compartment grid hangs from those rules, and the content column is asymmetric
  (offset left, `max-width: 72rem`, with the right margin wider than the left at desktop). One
  overlap moment per page maximum (named per page below).
- **Section headers vary — never the same stacked eyebrow+h2 on every section** (craft-floor
  refuses "eyebrow over every section"). Three treatments, rotated: **(a) ruled header row** —
  label left, h2 beside it, index range right, hairlines above and below, full-bleed; **(b) side
  label** — the label rotated vertical along the section's left rule, h2 in the content column;
  **(c) bare** — label + rule only, no h2, where the content is self-explaining (reviews, CTA).

## R3-7. Signature motion (all-new — clip-wipe / lift-tilt / parallax retired)

- **Entrance family: `line-draw`.** The compartment/section rules **draw themselves in**
  (scaleX 0→1 from `transform-origin:left` on border elements; `pathLength=1` dash trick on the
  few real SVG rules), and each block's content settles 8px upward behind its drawn rule as the
  tail of the same move. The rule IS the reveal — document lines being ruled onto the page.
  Delivered by IntersectionObserver `.in` (threshold ~.12, once, unobserve), stagger
  `--i` × 60ms (editorial lines), cap 12. Justification vs the flagged fade-up default: the
  authored element is the drawn rule; the 8px settle is subordinate and never ships alone.
  **Fail-visible per motion.md rule 0:** hidden states live only under `html.js` +
  `prefers-reduced-motion: no-preference`, with the `<head>` opt-in snippet + `motionOK()`
  cancel — JS off/broken = finished page.
- **Hover personality: `weight-shift`** (Albert Sans is variable): nav links, go-links, and the
  footer links animate `font-variation-settings` 'wght' 400→650 over 200ms (reserve layout with
  a hidden bold duplicate or `text-rendering` care so nothing reflows visibly); compartment
  hover = fill swap `#fff → --pedra` + index numeral deepens `--ouro → --ouro-escuro`; buttons
  get label weight 500→650 + `:active{transform:scale(.97)}`. **No lift, no tilt, no shadow
  motion anywhere** — that was Rev 2's language. Guarded `(hover:hover) and (pointer:fine)`.
- **Scroll set-piece (the one): `sticky-progress` index rail** on `practice-areas.html` only —
  the ledger's tab column (01–04 + phone) sticks and marks the current section (IO toggles
  `aria-current`; a 2px brass rule slides between items). CSS `position:sticky` + the same IO.
  No parallax anywhere (Rev 2 had it), no `view()` scrub (fora owns it).
- **Tempo:** ease `cubic-bezier(.16,1,.3,1)` everywhere (expensive, slow-settling, editorial);
  durations — rule draw 700ms, content settle 600ms, hover 200ms; stagger 60ms. Never `linear`,
  never bare `ease`.
- **GSAP tier: 0** — pure CSS + IntersectionObserver. No vendored library; the bytes stay in
  the photographs.
- Ban check vs last 3 rows: line-draw ∉ {mask-curtain, clip-wipe, dapple-scrim};
  weight-shift ∉ {ink-sweep/underline-draw/fill-sweep, lift+tilt}; sticky-progress ∉
  {`view()` gallery-hang, hero parallax, pointer field}. No fade-up, no count-up.

## R3-8. Background & atmosphere (all-new — azulejo lattice / lamp-glow radial retired)

- **Pedra pages — "ruled paper":** flat `--pedra` base + two barely-there corner washes
  (radial `--linha` at 12–15% alpha, top-left and bottom-right) + the standard **grain overlay**
  at 0.04 — paper-grade depth, no pattern. **No dot grid, no graph paper** (john-sessa owns it),
  no lattice (Rev 2 owns it). Structural hairlines (the full-bleed section rules) are the only
  "pattern" — they are real rules, not a repeating background.
- **Ink bands:** flat vertical gradient `--tinta → --tinta-2` + grain. **No lattice, no
  lamp-glow radial.**
- **Atmosphere (one effect, sitewide): `shimmer/glint sweep`** on the big Caslon phone number
  in each page's ink CTA band — a brass-to-`--lamp` glint crossing the digits every ~7s with the
  long idle (polished-brass-catching-light; the banker's-lamp warmth carried into Rev 3 as a
  moving highlight instead of a radial). Reduced-motion kills it. Budget per page: 1 entrance +
  1 hover + ≤1 set-piece + 1 ambient = within the ≤4-system cap.

## R3-9. Per-section layout spec (all four pages — same filenames, nav labels, URLs)

**Shared header (every page) — porcelain masthead, two decks (replaces the tinta header):**
1. **Top deck:** 13px Albert Sans row between hairlines — language lines left (verbatim,
   protected), address "385 Lafayette Street · Newark's Ironbound" right. On `--pedra`, text
   `--muted`, language lines `--ouro-escuro` italic Caslon.
2. **Main deck:** real `assets/logo.png` top-left **directly on the porcelain** (it lived on a
   pedra chip against Rev 2's dark header; on a light masthead it needs no chip — builder
   verifies legibility, never recolors) · nav right (Albert Sans 500; active page = 2px `--ouro`
   rule under the link, not bold) · **call button**: `--ouro` fill, `--ink` label, **square
   corners**, small inline-SVG phone glyph (stroke, currentColor) — **the ☎ dingbat is retired
   sitewide** (craft checklist: no emoji icons). A 2px `--ouro` rule closes the masthead bottom.
3. Sticky behavior: top deck scrolls away; main deck sticks (`sticky condensing bar`) with a
   hairline + subtle white fill.

**Shared footer — `--tinta-2` ledger:** same strings as Rev 2 (logo on a small pedra chip —
still needed on dark, Rev 2 precedent · one-line services sentence · language lines · Pages
column · Office/NAP column), recomposed as **ruled columns sharing hairlines** (`--linha` at
28% opacity), ledger labels for column heads ("Pages", "Office") in `--lamp` caps. Disclaimer
block (bracket-flagged, verbatim) sits under a full-width rule; bottom row unchanged.
Sticky mobile call bar stays (conversion pattern, not a layout signature).

### index.html
1. **Masthead hero (pedra, header treatment none — it IS the masthead):** the h1
   *"A Newark defense attorney who speaks your language."* (frozen copy) set huge in Caslon
   across ~10 of 12 columns, max 2 lines · hero-sub (frozen 30-word line) in lead size, offset
   to start at column 4 (asymmetry) · then a **full-bleed ruled row**: language lines (Caslon
   italic, `--ouro-escuro`) left | CTA pair right (ouro call button + "Send a message →"
   weight-shift link). 4 text elements + CTA row — under the composition cap.
2. **Photo band + overlap (the page's one overlap):** `assets/hero.webp` full-width at a
   **~21:9 CSS crop** (`aspect-ratio:21/9; object-fit:cover; object-position:center 62%` — the
   file is untouched, brief rule 4), hairline top rule, and its bottom edge **overlaps ~64px
   into the ink band below** (negative margin) so the photograph sits clipped to the ledger
   like a mounted plate. This is the hero re-framed: type-first masthead + mounted photograph,
   nothing like Rev 2's split panel.
3. **The record row (ink band):** the 4 frozen trust facts as a **ruled ledger row** — four
   fields divided by `--linha`-at-28% vertical rules (2×2 on mobile), k in Caslon 700 `--pedra`,
   v in Albert Sans `--linha`. Header treatment (c): none — the row explains itself. No
   count-up (they aren't numbers anyway).
4. **Practice compartments (pedra):** header treatment (a) ruled header row — label "Practice
   areas" + h2 "Find your matter, then call." (frozen) left, index range "01–04" in Caslon
   italic `--ouro-escuro` right. Then the **asymmetric compartment grid**: Criminal 7-col /
   Traffic 5-col / Family 6-col / Real Estate 6-col, collapsed shared rules, each compartment =
   label rule + h3 + frozen ≤25-word p + "See … →" go-link (weight-shift) + folio numeral
   top-right. Whole compartment is the link target (as in Rev 2 — no dead-looking affordances).
5. **About compartment (white on pedra, split):** header treatment (b) — "The office" as a
   **vertical side label** on the compartment's left rule. Inside: `assets/about.webp`
   **reused as-is at its native 4:3** in a ruled frame with brass corner ticks, left 5 cols;
   frozen copy (h2 "Since 2002, one case at a time." + two paragraphs + "Meet Paul Da Silva →")
   right 7 cols.
6. **Commentary band (ink, asymmetric):** left 7 cols — label "On the air", h2 "A legal voice
   the press calls on.", frozen paragraph, "Read the full bio →" link. Right 5 cols — the two
   marks (RTP-Portugal / CourtTV, frozen strings) as **stacked borderless fields sharing one
   rule**, RTP first and set larger (the answers' own weighting). Text names only, no fake
   network logos (unchanged hard rule).
7. **Reviews (pedra):** header treatment (c) — label "Client reviews · Lawyer.com" + rule only
   (drop the h2 "In their words." — **not a content drop: a 3-word section ornament absorbed
   by the new header grammar**; the three quotes carry the section. Logged in R3-10.) Three
   **ruled columns sharing vertical hairlines** (no cards): quote in Caslon italic 1.25rem,
   attribution in Albert Sans small caps. All three quotes verbatim incl. "curtious"/"best"
   (protected).
8. **CTA band (ink, asymmetric — Rev 2's was centered):** left-aligned label "Ready to talk" +
   the giant Caslon phone (tap-to-call, **glint sweep lives here**) + address line; right
   column, divided by a vertical rule: the frozen one-liner "The fastest way to reach the
   office is by phone." + "Send a message instead →". All strings frozen.

### practice-areas.html
1. **Page head (pedra masthead, not ink):** label "DaSilva & Associates, LLC" · h1 "Practice
   Areas" in Caslon · frozen intro line with the inline phone link (`--ouro-escuro` on pedra —
   AA, replacing Rev 2's `--lamp`-on-ink link). Closed by the full-bleed 2px brass rule.
2. **Body = sticky index rail + ledger (the set-piece):** left 2-col sticky rail — 01 Criminal
   Defense / 02 Traffic / 03 Family Law / 04 Real Estate (anchor links `#criminal #traffic
   #family #real`, preserved) + a small call button; 2px brass rule slides to the active item.
   Right 10 cols: the four practice sections as **ruled compartment groups** sharing hairlines,
   each opening with header treatment (a): folio numeral + h2 + frozen intro.
   - **#criminal:** frozen intro; the 4 sub-blocks (DUI/DWI · Sex Offenses · Violent Crimes &
     Weapon Offenses · Drug Crimes, all frozen) as a **2×2 collapsed-rule sub-ledger** inside
     the group — scale contrast: this group is visibly the deepest.
   - **#traffic:** frozen intro + the 5 violations as **ledger line items** (full-width rows
     divided by hairlines, brass tick left — replaces Rev 2's chip pills) + frozen goal
     sentence. Stays thin by design (voice spec).
   - **#family:** frozen intro + 7 ledger line items.
   - **#real:** frozen intro + 4 ledger line items.
3. **CTA band:** shared component (R3-9 index §8).

### attorney-bio.html
1. **Page head (pedra):** label "Attorney" · h1 "Paul Da Silva" · frozen intro line.
2. **Bio compartment (white, split):** portrait placeholder left 4 cols — **3:4 ruled frame
   with brass corner ticks**, frozen label "Photo of Paul Da Silva — real headshot to come."
   (NEVER generated — standing hard rule); frozen two-paragraph bio right 8 cols, first
   paragraph at lead size.
3. **Timeline → ledger table (pedra):** header treatment (a): label "Education & career" + h2
   "The path to the practice." (frozen). The 6 frozen entries as **full-width ledger rows**:
   year column (Caslon 700, `--ouro-escuro`, right-aligned, fixed width) | rule | what (h3
   size) + desc. Hairline between rows; rows draw in via the entrance family. Replaces Rev 2's
   vertical timeline rail.
4. **Recognition (pedra):** header treatment (b) vertical side label "Recognition"; h2 "Beyond
   the courtroom." (frozen) in-column; the 3 frozen recognition blocks as compartments spanned
   **5 / 4 / 3** (commentator widest — the site's best proof). Personal line (frozen) as an
   italic footnote under a short brass rule.
5. **CTA band:** shared component.

### contact.html
1. **Page head (pedra):** label "Get in touch" · h1 "Contact the office." · frozen intro.
2. **Contact ledger (two compartments sharing one rule, 5 / 7):**
   - **Left — call compartment (white):** label "Call the office" · the big Caslon number
     (tap-to-call) · the frozen `<dl>` (Fax / Office / Languages) as ledger rows with hairlines ·
     then the **LIVE map iframe — preserved exactly as it exists in the file today** (Harry's
     hand-edit, currently uncommitted: an **OpenStreetMap embed iframe** + the "Get directions"
     Google Maps link. The brief calls it a Google Maps iframe; the file's actual embed is OSM
     with a Google directions link — **preserve the file's actual live embed byte-for-byte**,
     src untouched, `loading="lazy"` kept, and only restyle the frame). **Frame spec:** square
     corners, 1px `--linha` border, a 2px `--ouro` rule across the top edge, and the "Get
     directions" link restyled as a ledger caption row (Albert Sans small, `--ouro-escuro`,
     weight-shift hover) directly beneath.
   - **Right — form compartment (white):** label "Send a message" · h2 "Tell us what happened."
     (frozen) · the 3 frozen fields (Name / Phone / What happened?) restyled as **ledger
     fields**: no boxes — a 1px `--linha` bottom rule per field, focus = 2px `--tinta` rule +
     label weight-shift 400→600; submit = ouro button (square). Demo behavior unchanged: inline
     confirmation in `.form-result`, never a dead click; the HTML comment marking the real
     handler stays.
3. **CTA band:** shared component minus the address line (as in Rev 2's contact variant —
   "Prefer to call?" label, phone with glint, frozen one-liner).

## R3-10. Rev 3 content map — every current string placed (parity already banked)

Content is frozen, so the map is a **carry-over ledger**: every visible string on the four
Rev 2 pages moves to its Rev 3 home. The critic re-walks this against `site-content.md` + the
Rev 2 pages.

| Current string block (Rev 2) | Rev 3 destination |
|---|---|
| All `<head>` meta: titles, descriptions, OG/Twitter, canonicals, favicon, JSON-LD (×4 pages) | **Unchanged, byte-for-byte** (only the Google Fonts `<link>` swaps to Libre Caslon Text + Albert Sans) |
| Header: language lines + address strip · nav 4 labels · "Call 973-344-0808" | Masthead top deck + main deck (R3-9 shared header) — same strings, same URLs |
| Hero: h1 · language-lines pair · 30-word sub · CTA pair | Masthead hero §1 — same strings, new composition |
| Trust strip: 4 k/v facts | The record row (ink) §3 — all 4 verbatim |
| Practice section: label "Practice areas" + h2 "Find your matter, then call." + 4 cards (num, h3, p, go-link) | Compartment grid §4 — every string carried; spans change, words don't |
| About: label "The office" + h2 + lead + p + "Meet Paul Da Silva →" | About compartment §5 (label becomes the vertical side label — same text) |
| Commentary: label "On the air" + h2 + p + link + 2 marks (name + desc) | Commentary band §6 — all strings, RTP field set larger |
| Reviews: label "Client reviews · Lawyer.com" + 3 verbatim quotes + attributions | Reviews ruled columns §7 — quotes/attributions protected, untouched |
| CTA band strings (label, phone, address, line, link) ×3 page variants | Shared CTA band — all strings, asymmetric composition |
| Footer: services sentence · language lines · Pages · NAP block (incl. fax) · disclaimer (bracket flag + text) · © row | Footer ledger — all strings verbatim; NAP still matches JSON-LD exactly |
| practice-areas.html: page-head strings · 4 section intros · 4 criminal sub-blocks · 5 traffic items + goal · 7 family items · 4 real-estate items | Same page — intros and every list item carried; chips become ledger line items (same text); anchors `#criminal #traffic #family #real` preserved |
| attorney-bio.html: page-head · 2-paragraph bio · portrait placeholder label · 6 timeline entries (yr/what/desc) · recognition h2 + 3 blocks · personal line | Same page — timeline becomes the ledger table, every yr/what/desc string carried |
| contact.html: page-head · "Call the office" + number + dl (Fax/Office/Languages) · **live map iframe + "Get directions" link** · form (label, h2, 3 fields, "Send", comment, `.form-result`) | Same page — **iframe src byte-for-byte** (see R3-9 contact §2); all form strings + demo behavior carried |

**Deliberately dropped (with reasons — nothing else is dropped):**
- **h2 "In their words." (home reviews section)** — a 3-word section ornament, zero
  informational content (parity counts facts); absorbed by the new bare-header grammar where
  the label + quotes carry the section. If the critic reads this as a parity nick, the builder
  reinstates it in the ruled header row — either way it's logged, not silent.
- **The ☎ dingbat glyphs (header button, hero CTA, mobile bar)** — decorative characters, not
  content; replaced by an inline-SVG phone glyph (craft checklist: no text dingbats as icons).
- **The header logo's pedra chip** (visual treatment, not a string) — unnecessary on the light
  masthead; the chip **stays in the footer**, where the logo still sits on dark.

## R3-11. Image list — **NO new generation authorized** (the 2-image cap is spent)

| # | Asset | Rev 3 slot | Treatment |
|---|---|---|---|
| A | `assets/hero.webp` (16:9, 1600×893, frozen) | Home photo band under the masthead | **Reused as-is; ~21:9 crop done in CSS only** (`aspect-ratio:21/9; object-fit:cover; object-position:center 62%` — builder tunes the Y% so the storefront line stays in frame at 375px too, where the band relaxes to 16:9). File untouched, no regeneration, no re-encode |
| B | `assets/about.webp` (4:3, 1000×747, frozen) | Home about compartment, left 5 cols | **Reused as-is at native 4:3** in the ruled frame. No crop needed |
| C | Portrait placeholder | attorney-bio.html §2 | Restyled to the direction: 3:4 ruled frame, brass corner ticks, frozen label text. Never generated |
| D | `assets/og.jpg` | OG/Twitter image, all pages | Unchanged |
| E | Live map iframe | contact.html | Not an image slot — preserved live embed (R3-9 contact §2) |
| F | `assets/logo.png` | Masthead + footer | Frozen, unmodified, local |

No other image slots exist in this direction; the depth budget is carried by R3-8's ruled-paper
system, not imagery. If the builder finds a slot that seems to want an image, the answer is a
rule, a numeral, or nothing — **never a third generation.**

## R3-12. Mobile (375px) — real decisions for the ledger grammar

- **Masthead:** top deck compresses to the language lines only (identity — never disappears;
  address moves into the footer's reach); main deck = logo + hamburger + compact call button.
  Menu = full-width ruled list (ledger rows), not a floating sheet.
- **Hero:** h1 at the clamp floor (2.75rem) · sub full-width · ruled row stacks: language lines,
  then **full-width ouro call button**, then the message link. Photo band relaxes to 16:9 and
  the ink-band overlap shrinks to ~32px (still present — the grammar survives the viewport).
- **Record row:** 2×2 ruled grid (shared hairlines both axes).
- **Practice compartments:** single column, **collapsed rules kept** (one continuous hairline
  between stacked compartments — reads as one ledger, not four cards); folio numerals stay
  top-right at 2rem.
- **Sticky index rail (practice page):** becomes a **horizontally scrollable tab row pinned
  under the sticky masthead** (01–04, brass rule under the active tab); content sections run
  full-width beneath. The criminal 2×2 sub-ledger stacks to 1-col with shared rules.
- **Timeline ledger table (bio):** year column narrows to a 4.5rem left rail; what/desc stack
  right of it — still a table, not a rail of dots.
- **Contact:** call compartment first (number at clamp floor), map iframe full-width ~4:3,
  form below; sticky bottom call bar in ouro on all pages (kept from Rev 2 — conversion
  pattern). All tap targets ≥44px; weight-shift hover is `(hover:hover)`-guarded so touch gets
  the pressed state only.
- Screenshots desktop + 375px, all four pages → `screenshots/` (re-captured, brief rule).

## R3-13. Gate compliance notes (builder + critic)

- **Composition checks, planned around:** hero = 4 text elements + CTA row (under the cap);
  exactly **one** image+text split per page (about / bio); **zero marquees**; section headers
  rotate three treatments (R3-6) instead of eyebrow+h2 everywhere; layout families across the
  home page: masthead hero · mounted photo band · ruled record row · asymmetric compartment
  grid · split compartment · asymmetric ink band · ruled quote columns · asymmetric CTA — no
  two-family monotony.
- **Detector:** expected clean at `exit 0`; the single pre-authorized waiver family is the
  palette one (R3-3) — client-locked colors, waived in-file with the stated reason. Libre
  Caslon Text / Albert Sans are not on the overused-font list.
- **JS-off:** line-draw hidden states scoped `html.js` + reduced-motion wrapper with the
  `motionOK` cancel (R3-7) — rename `main.js`, every word reads.
- **Copy gates:** content is frozen, so `copycheck.py` + `aitells.py` should pass as they did
  at Rev 2 sign-off; the builder re-runs both on all four pages anyway (brief rule 3) since
  even carried strings sit in new markup. The one string-length judgment call (reviews h2) is
  logged in R3-10.
- **Design-memory row (critic, on pass — REPLACES the paul-da-silva-law row):**
  `2026-07-29 · paul-da-silva-law — "Counsel of Record" (Rev 3; palette client-locked, carried
  from Rev 2) · Libre Caslon Text / Albert Sans · dark-first→light-first iron-gall ink +
  aged brass + cool porcelain (client-directed, deliberately carried) · light-first ruled
  modular ledger (Swiss/modular compartments, collapsed hairlines) · porcelain rule-field +
  corner washes + grain; ink punctuation bands; brass glint sweep · line-draw entrance +
  weight-shift hover + sticky-progress index rail — deliberately NOT fade-up/count-up.`
