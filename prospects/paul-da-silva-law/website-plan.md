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
