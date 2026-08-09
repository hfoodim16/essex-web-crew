# Website plan — DaSilva & Associates, LLC · slug `dasilva-associates`

> Build contract for the Builder. Produced by the Planner from `client-answers.md` (top
> authority), `site-content.md` (content-parity contract), and `dossier.md` (support).
> Companion artifact: `voice-spec.md` — every visible string is written against it.
> This is a REBUILD for a real client from his real questionnaire answers. It replaces
> nothing in `prospects/paul-da-silva-law/` (that build is frozen and untouched).
> **Standing instruction (Harry, verbatim): "always listen to the questionnaire."** The
> client's answers are controlling on every collision — old site, dossier, the frozen
> build, any convention or gate. Where a gate and an answer disagree, the answer wins and
> the exception is stated here.

**Design Read (taste §0):** Reading this as: a local professional-services site (solo
law office) for Essex County people facing a charge, a closing, or a divorce, with a
professional-and-friendly plain-language voice, leaning toward a dark civic-editorial
aesthetic family with courtroom gravity.

**Taste dials:** trust-first/regulated read → DESIGN_VARIANCE 5 · MOTION_INTENSITY 3 ·
VISUAL_DENSITY 4. Redesign mode: **overhaul** (Q7 "TOO VANILLA", Q10 "OPEN TO EITHER")
with content and IA preserved (taste §11: keep the 4-page nav, keep slugs, keep the real
logo, rewrite the voice per the client's own instruction).

---

## 1 · Art direction — "The Quiet Verdict" (deep azul + gold, dark-first civic poster)

> **⚑ AMENDED BY THE LEAD, 2026-08-03, on Harry's direct instruction:** *"Do azul and gold
> colors rather than the green and beige."* The original courtroom-green-and-bone palette
> is retired; §1 and §3 below are rewritten to match what is actually built. Everything
> else in this plan — typography, page map, section formats, content map, motion,
> composition device, imagery, SEO — is unchanged and was never in question. The direction
> NAME is kept deliberately: it names the empty-counsel-table concept, not the green.

A deep azul ground with cool paper type and gold as the accent that carries the dark
bands: the gravity of a paneled courtroom, rendered in the firm's own blue rather than the
generic template navy Paul called "too vanilla." Oversized
serif headlines and giant real numerals (May 2002, 90%, 4 practice areas) do the talking
in his own plain language — bold in structure, type, and color, never in the writing,
which is exactly the tension his Q7/Q8 answers set up. Friendliness comes from cool paper
surfaces, a humanist body face, and copy that reads like Paul explaining, not a firm
performing.

*(Builder: paste the paragraph above at the top of `style.css`.)*

### Redesign audit (taste §11 — the site being replaced)
- **Current state:** dated WordPress template; generic legal-directory look; stock
  office-exterior + courthouse-columns photos; 11-field contact form; the differentiators
  (languages, CourtTV, community roots) buried in interior body text; no dominant phone
  CTA; thin body copy. Current dials read roughly 2/1/3.
- **Preserve:** IA (4 pages, same nav labels), page slugs, the real logo, every fact
  block (content map, §7). **Retire:** template look, stock photography, the 11-field
  form, GTranslate widget, brochure phrasing.

## 2 · Typography

- **Display: Frank Ruhl Libre** (Google Fonts; weights 500/700/900) — headlines, page
  titles, the giant numerals, the owner block. A sturdy, high-shouldered serif with real
  gravitas that no recent crew build or AI default uses.
- **Body: Red Hat Text** (Google Fonts; 400/500/700) — all body copy, nav, buttons,
  forms, captions. Humanist, warm, plainly legible: the "friendly" half of Q8.
- Not Inter/Roboto/Arial/Helvetica, not Fraunces/Instrument Serif/Geist/Plus Jakarta
  Sans/Space Grotesk, and not any pairing from the last 3 design-memory rows.
- Scale: fluid `clamp()` display sizes; **h1 ≈ 3.4–4.5rem desktop vs 1rem/16px body — a
  ≥3× jump is the deliberate hierarchy engine** (see composition device). Stat numerals
  larger still (~5–6rem).

## 3 · Color system (`:root` tokens)

| Token | Hex | Role |
|---|---|---|
| `--azul-950` | `#041E30` | darkest step — footer base |
| `--azul-deep` | `#062B44` | primary dark ground — hero, CTA bands |
| `--azul-900` | `#0A3A58` | elevated panels/cards on dark |
| `--azul-lift` | `#0A3D5E` | ceiling of the dark band's radial gradient (derived; capped so gold clears AA across every blend) |
| `--azul` | `#00588A` | accent **on light grounds only** — sampled from his logo roundel |
| `--azul-hov` | `#00426B` | azul hover |
| `--gold` | `#C8A24A` | accent **on dark grounds only** — CTAs, band numerals, focus ring on dark |
| `--gold-hov` | `#D9B75F` | gold hover |
| `--gold-deep` | `#7E5F16` | gold-as-text on light, used sparingly |
| `--paper` | `#F4F6F7` | light ground — cool near-white, deliberately NOT beige; also text on dark |
| `--paper-2` | `#E4EAEE` | cards on light |
| `--paper-dim` | `#AFC0CC` | muted text on dark |
| `--ink` | `#0D1B24` | text on light |
| `--ink-dim` | `#44586A` | muted text on light |

**The one rule that governs this palette: the accent flips with the ground.** Gold cannot
appear on paper (2.17:1) and azul cannot appear on any dark ground (1.78:1). This is
enforced **structurally, not by convention** — `:root` sets `--accent: var(--azul)` and the
dark surfaces (`.band-dark, .hero, .site-footer, .topstrip`) redefine `--accent: var(--gold)`
with matching `--on-accent` and `--focus`. Every accent element and every button reads
`var(--accent)`, so the failure mode cannot be reintroduced by forgetting a rule; adding a
new dark surface to that selector list makes it inherit correctly.

Gold is the first accent in this build that can live on a dark band at all — garnet was
1.49:1 there and azul 1.78:1, which is why earlier drafts kept forcing the hero CTA to a
light fill. **The hero CTA is gold-filled with `--ink` text (7.27:1).** The logo's secondary
gray `#747679` gets no token: it lives inside the mark and fails as text (3.99:1).

**Verified contrast** (lead-computed, then re-measured from the render by the Builder — 48
pairs, 0 failures): gold/azul-deep 6.07 · gold/azul-900 4.96 · gold/azul-950 7.07 ·
gold/azul-lift 4.74 · ink/gold 7.27 · paper/azul-deep 13.48 · paper-dim/azul-deep 7.82 ·
ink/paper 16.15 · ink-dim/paper 6.80 · azul/paper 7.01 · azul-hov/paper 9.73 · paper on the
scrimmed hero 10.33 · gold button boundary vs scrim 4.51 (needs 3.0).

**Color-convention call — restated, because the ruling changed it.** The legal category
convention is navy/burgundy/deep-green + gold ("authority navy + trust gold"). This palette
now **takes the convention head-on rather than sidestepping it**, at Harry's instruction.
The risk is explicit and on the record: blue-and-gold is the category default, and *"too
vanilla"* was Paul's own complaint about his current site (Q7). **The distinctiveness must
therefore be carried entirely by structure, type and composition** — the civic poster-stack,
the dark-first inversion, the 900-weight Frank Ruhl at a ≥3× jump, and the oversized real
numerals — not by the palette. The blue is his own logo blue rather than a template navy,
which is what keeps it his. The Critic is directed to judge boldness harder on this account,
**not** to fail the build for the palette choice, which is settled.

**No `cream-palette` waiver is needed or present.** The rule fired on the retired warm bone;
the cool `--paper #F4F6F7` does not trip it (confirmed with `--no-inline-ignores`). The stale
waiver comments were removed from all four files rather than left naming a token that no
longer exists.
**No stated exception is required.** The earlier `cream-palette` waiver existed for the
retired warm bone and is gone; see the note above.

**Buttons:** the accent-filled button follows the ground via `--accent` — **azul-filled on
light, gold-filled with `--ink` text on dark.** The CTA-band phone number sets in gold,
huge; contrast carries it.

Theme lock: each page is paper-ground with dark azul bands as composition (hero, CTA
bands) — one theme, dark bands as punctuation, never a mid-page theme flip. Footer is
dark azul with the logo on a paper chip so the full-color mark and NAP sit legibly.

> ### Terminology note for anyone reading the rest of this plan
> Sections 4 onward were written against the retired palette and still say **"verde"** and
> **"bone"** in descriptive prose (band descriptions, background system, logo placement,
> the divergence table, the Stage-5 direction write-ups). **Read `verde` → `azul` and
> `bone` → `paper` throughout.** The layouts, formats, openers, content map and composition
> device those sections describe are all current and were never affected by the repaint —
> only the colour words are stale. §3 above is the authoritative palette. Any contrast
> figure appearing later in this file is superseded by the verified table in §3.
> One exception: the **Stage 3 evidence sheets (§16)** describe *other people's* websites —
> colour words there are those sites' palettes and are correct as written.

## 4 · Page map (multi-file — his #1 goal is search ranking; each page indexes separately)

Four files, mirroring the old nav exactly (parity floor + slug stability): `index.html` ·
`practice-areas.html` · `attorney-bio.html` · `contact.html`. Practice areas stay ONE
page with four deep anchor sections (`#municipal-court`, `#criminal-law`, `#real-estate`,
`#matrimonial-law` — successor anchors to the old site's `#criminal/#traffic/#family/#real`).
Rationale: per-practice pages would be the bigger SEO play, but Paul's real per-practice
facts are thin, and padding four pages into existence violates the voice spec. If Harry
wants the growth step, that's a follow-up ask (it pairs with Confirm item 9, the FAQ).
Sticky header on every page: logo top-left (real file, see §10), nav, and an azul
tap-to-call `tel:` button; the language line "Se Habla Espanol / Nos falamos o portugues"
rides the header strip sitewide exactly as his site writes it.

### index.html — Home
1. **Hero** — format: hero, opener: in-media — full-bleed dark verde band, generated
   counsel-table image under a scrim, h1 set inside the band. See §8 hero direction.
2. **Trust strip** — format: stat-strip, opener: none — 4 real numbers/facts, giant Frank
   Ruhl numerals: `Opened May 2002` · `90% of clients come by referral` · `4 practice
   areas` · `Portuguese & Spanish spoken`. All his, all checkable. No invented stats.
3. **Practice areas** — format: card-grid, opener: bare-h2 — four typographic cards in
   HIS numbered order ① Municipal Court ② Criminal Law ③ Real Estate ④ Matrimonial Law,
   azul numerals, ≤30 words each, each linking to its anchor. No images (cards are
   typographic; his numbering is the visual).
4. **The owner block** — format: quote-monolith, opener: none — the ONE lyrical block:
   first-person, attributed "— Paul Da Silva," built strictly from his Q1 sentences
   (opened May 2002 to serve the community where he was born and raised; big-firm-level
   service and advocacy). Set large in Frank Ruhl on bone.
5. **Service area** — format: split, opener: bare-h2 — left: the two-tier split published
   exactly (Northern NJ for real estate & matrimonial; entire state for municipal &
   criminal — regions, NO invented town list). Right: GENERATE slot 2 (Newark streetscape,
   §11). Newark address appears here too (Q14 "BOTH").
6. **Born and raised here** — format: editorial-column, opener: side-label — short about
   preview (≤80 words): son of immigrant parents, born and raised in NJ, the practical
   and precise approach carried from the old site's real copy; link to Attorney Bio.
7. **Call band** — format: cta-band, opener: in-media — dark verde band: "Call
   973-344-0808" as a huge tap-to-call line, language line beneath.

### practice-areas.html
8. **Page hero** — format: hero, opener: bare-h2 — short bone-ground page title band (no
   image): "Practice Areas," lede carrying the old site's real fact: a routine matter for
   an experienced attorney is not routine for the client; practical and precise litigation
   without needless additional costs.
9. **① Municipal Court** — format: split, opener: side-label — DWI/DUI and vehicular
   offenses (first-time and repeat), minor criminal offenses, traffic: driving without a
   license, suspended license, reckless driving, uninsured driving, speeding; the
   administrative process of protecting driving privileges; aim to reduce or dismiss
   charges and minimize points. Image side: PLACEHOLDER (municipal courtroom bench
   detail). Statewide.
10. **② Criminal Law** — format: card-grid, opener: bare-h2 — offense-type cards from
    site-content: violent crimes & weapons (murder, manslaughter, robbery, burglary,
    assault, firearms), drug crimes (possession, distribution, trafficking, prescription),
    sex offenses, aggravated assaults. Plain labels, no war language (voice spec).
11. **③ Real Estate** — format: steps, opener: numeral — the transaction as a numbered
    sequence (offer → contract/purchase & sale agreement → title search → closing), with
    leases/rentals and co-op & condominium transactions carried as list items. This is
    the one place order itself informs — the only numbered section family on the site
    beyond his own ①–④.
12. **④ Matrimonial Law** — format: editorial-column, opener: bare-h2 — divorce, alimony,
    child support, child custody, domestic violence, pre- and post-nuptial agreements,
    juvenile delinquency and dependency proceedings; the old site's real line about
    sensitivity and discretion carried as fact, rewritten to spec register.
13. **Call band** — format: cta-band, opener: in-media — same band as Home (consistency).

### attorney-bio.html
14. **Bio intro** — format: split, opener: bare-h2 — left: PLACEHOLDER portrait frame
    (never generated — labeled frame awaiting Paul's real headshot, Q11); right: who he
    is in ≤3 short paragraphs (born and raised in NJ, son of immigrant parents, fluent
    Portuguese and Spanish, opened the office May 2002; one personal sentence: married,
    two children, tennis and hockey).
15. **Career timeline** — format: steps, opener: numeral — Rutgers BA '93 → Touro JD '96
    (Moot Court Board) → Legal Aid Society of Manhattan → Legal Aid Society of Nassau
    County → NJ Office of the Public Defender (criminal cases including murder trials) →
    boutique litigation firm, Montclair → opened DaSilva & Associates, May 2002.
16. **Recognition** — format: card-grid, opener: bare-h2 — four credential cards, each
    the credential + one plain line: CourtTV guest commentator · RTP-Portugal guest
    commentator · former Adjunct Professor, Fairleigh Dickinson University · 4 years,
    Hudson County Ethics Committee. NO bar admissions (unpublished — Confirm list).
17. **Call band** — format: cta-band, opener: in-media.

### contact.html
18. **Contact** — format: split, opener: bare-h2 — left: phone DOMINANT (azul, huge,
    tap-to-call), fax, full address, language line; right: the 4-field form (Name · Email
    · Phone · What happened / Description of service) as a styled placeholder embed.
    No email address displayed, no hours (none exist — nothing invented).
19. **Where we work** — format: table, opener: side-label — the two-tier service area as
    a 2-row table: Real Estate & Matrimonial → Northern New Jersey · Municipal Court &
    Criminal → the entire state. Address line beneath (Q14 "BOTH").
20. **Map band** — format: full-bleed-band, opener: none — Google Map embed placeholder
    for 385 Lafayette Street, styled block + HTML comment.

**Quota check (lint-verified):** 20 sections · 10 distinct families · no family twice in
a row · 3 kicker-class openers (side-label ×3) vs budget ceil(20/3)=7 · no two adjacent
sections share an opener · numeral only on steps.

## 5 · Composition device

**The ≥3× scale jump, carried by the Home trust strip (section 2):** the four real
numerals set at ~5–6rem Frank Ruhl against 1rem body — a wall of his own checkable
numbers as the page's loudest visual event. The same jump echoes in every page h1 and the
CTA band's phone number. Grids stay calm (variance 5); the scale contrast IS the symmetry
break, verifiable in the desktop screenshot.

## 6 · Client answers → decisions (every load-bearing answer, walked)

| Answer | Decision in this plan |
|---|---|
| Header wrote `PAULDASILVALAW` (his URL) | **RESOLVED by his own brand asset:** the logo reads **DaSilva & Associates, LLC** (no space) — that spelling ships sitewide, in the footer NAP, and in the JSON-LD. The old footer's "Da Silva" was the old site contradicting its own logo; the logo wins. Domain pauldasilvalaw.com stays the domain (canonicals, launch). |
| Q1 opened May 2002; big-firm service & advocacy from the community he was born and raised in | The spine: hero concept (§8), owner quote-monolith (Home §4), trust strip fact, bio intro. |
| Q2 two-tier service area | Published exactly as split: Home split section 5, contact table 19, per-practice "statewide" notes on 9–10. NO town list invented. |
| Q3 goals: SEO first, then calls, then professional look | Multi-file indexable pages, full local-SEO kit (§13); phone dominant everywhere (calls); editorial imagery register + this art direction (professional). |
| Q4 90% referrals | Trust-strip numeral + hero subhead fact. The strongest checkable number on the site. |
| Q5 his four practice areas, his numbering | Card order, page order, anchor names, and the ①–④ numerals as a visual motif. "Municipal Court" leads; "Matrimonial Law" replaces "Family Law"; Real Estate ranks above Matrimonial. |
| Q6 N/A — nothing dropped, no specials | Every old-site service carried (content map §7). No free-consultation offer anywhere. |
| Q7 "TOO VANILLA" | The direction: dark courtroom green + his logo's azul + oversized serif — a deliberate break from both his current template and the navy-gold category default. |
| Q8 "professional & friendly, common language, nothing too fancy" | Voice spec governs every string; boldness lives in structure/type/color only; motion nearly still (tier 0). |
| Q9 no reference sites, no color constraints | Palette freely chosen (§3) with the convention call stated. |
| Q10 logo: "open to either" | His REAL logo ships regardless (§10) — we never invent a mark; colors around it are new. |
| Q11 photos: "I'll try to get you some" (CourtTV era) | Portrait = labeled placeholder frame; NO generated face, NO fabricated broadcast still. CourtTV appears as a text credential only. |
| Q12 "just the ones already on web site" | Site has zero reviews → **no testimonial section exists in this plan.** Lawyer.com quotes not used. Authorized credentials only (bio §16). |
| Q13 contact same as current site | Phone 973-344-0808 primary CTA; fax + address carried; form kept but cut to 4 fields; no email, no hours, nothing invented. |
| Q14 "BOTH" | Address AND service-area block both appear (Home 5, Contact 18–19, footer NAP). |
| Q15 N/A | No FAQ section anywhere. |
| Q16 no fees/payment info | Zero fee/retainer/payment content sitewide — hard exclusion. |
| Q17 GoDaddy domain; cell for Harry | Launch note for Corey (DNS at GoDaddy, real domain — not just Netlify subdomain). Cell number appears NOWHERE in the build. |

**Flag for the lead (no invention, Harry's Confirm list already carries these):** email,
hours, bar admissions, review permission, headshot, service-area wording, language-line
accents, FAQ, DNS. (Firm-name spelling: resolved above.) None block the build; the plan
writes around all of them.

## 7 · Content map (content-parity contract vs `site-content.md`)

| site-content.md block | Destination |
|---|---|
| Site-wide header: firm name, phone, fax, address, language line | Sticky header (phone, language line) + footer NAP on every page + contact 18 |
| Site-wide footer copyright | Footer, updated year, spelling per working name |
| Nav: Home · Practice Areas · Attorney Bio · Contact Us | Same 4 pages, same labels ("Contact Us" → "Contact" in nav is cosmetic; page carries full title) |
| Home ¶1 (founded May 2002; attentive, professional, personal approach) | Home owner block (4) + trust strip fact; "attentive/personal approach" facts fold into bio intro (14) |
| Home ¶2 (routine for the attorney ≠ routine for the client; practical & precise approach; no needless litigation costs) | Practice-areas page lede (8) — carried as his real differentiating fact |
| Home practice-area quick links | Home card-grid (3), new anchors |
| Real Estate block (protecting interests offer→closing + 4 services) | Practice areas 11 — all four services + the offer-through-closing frame as the steps |
| Family Law block (sensitivity/discretion + 7 items) | Practice areas 12, renamed Matrimonial Law per Q5, all 7 items carried |
| Criminal Defense intro ("decades of experience… all types of criminal matters") | Practice areas 10 lede (rewritten to spec register, fact kept) |
| — DUI/DWI & vehicular (incl. driving-privileges administrative process) | **Moves to 9 Municipal Court** (Q5 restructure — his numbering wins) |
| — Sex offenses / violent crimes & weapons / drug crimes | Practice areas 10 cards, every listed offense carried |
| Traffic Law block (5 violations + reduce/dismiss/minimize points) | Practice areas 9 Municipal Court |
| Traffic Law **statutory penalties** for those 5 violations (recovered 2026-08-04 — the original capture summarized them away) | Practice areas 9, `.penalty-list` under the split. Legal text: carried in substance, never reworded for voice, exempt from the copy checks. Closing qualifier added so the page states ranges, not predictions. |
| Attorney Bio: all education, employment, accomplishments, personal | attorney-bio.html 14–16, full fidelity |
| Contact: phone/fax/address | contact 18 + footer + JSON-LD |
| Contact form fields 1,3,4,11 (Name, Email, Phone, Description) | contact 18 — the 4-field form |

**Deliberately dropped (with reasons — no silent drops):**
1. Form fields **Company Name, Address, City, State/Province, ZIP, Website, How Did You
   Hear** (7 fields) — an 11-field form is hostile to someone who was arrested last
   night; the trimmed form keeps every field needed to return a call.
2. **GTranslate EN/PT/ES flag widget** — machine-translation plugin, not real content
   (dossier-confirmed); parity-neutral. The human-written language line is carried
   prominently instead.
3. **Office-exterior + courthouse-columns stock photos** (contact page) — generic stock
   the critique of the old site names as a weakness; replaced by the art-directed image
   plan (§11). No facts lost.
4. **"Established his own law firm over 20 years ago"** (bio phrasing) — superseded by
   the precise fact he gave: opened May 2002; the timeline (15) carries it exactly.

## 8 · Hero direction (obeys voice-spec.md)

- **Concept:** his differentiator, plainly said. Reference headline (Builder confirms
  against voice spec + the hero-uniqueness list): **"Big-firm advocacy, from a Newark
  neighborhood office."** (7 words — no triad, no "Since [year]" h1, no split-contrast
  pair; checked against all prospect heroes 2026-08-03.)
- **Subhead (≤30 words):** Municipal court, criminal, real estate and matrimonial law.
  Serving Northern NJ and the entire state since May 2002. 90% of clients come by
  referral.
- **CTA:** one primary — "Call 973-344-0808" (azul, tap-to-call). No secondary in the
  hero. Hero stack ≤4 text elements (no eyebrow, no trust micro-strip — the trust strip
  is its own section directly below).
- **Image intent:** GENERATE slot 1 (§11) under a verde scrim, h1 set in-media on the
  clear left third.

## 9 · Signature motion (Builder implements exactly; all reduced-motion gated)

- **Entrance family: blur-focus** — elements sharpen into place (opacity + blur→0).
  Small/medium elements only, never the full-bleed hero image. Thematically right:
  things coming into focus.
- **Hover personality: icon-nudge** — arrows/`tel:` glyphs translate 5px, 200ms; plus the
  universal pressed state (`:active` scale .97). Plain and professional; no lift, no
  tilt, no underline-draw, no fill-sweep.
- **Scroll set-piece: NONE.** Deliberate — Q8 "nothing too fancy," and the motion budget
  goes to one ambient system instead.
- **Tempo:** entrances 600ms, ease `cubic-bezier(.16,1,.3,1)`, stagger 70ms (cap ≤12).
- **GSAP tier 0** — pure CSS + IntersectionObserver; no vendor payload.
- **Anti-repetition (vs last 3 design-memory rows):** avoided fade-up + row-expand
  (Cecere), mask-curtain wipe + ink-sweep hovers + pointer vector field (fora-digital),
  rules-draw-in + weight-shift + sticky progress rail (paul-da-silva-law Rev 3). Neither
  token here appears in any of those rows.
- **Background & atmosphere:** layered verde gradient depth on dark bands (near-black
  green vignetting toward `--verde-2` center-light, per backgrounds.md layered-gradient
  recipe) + fine grain at 0.03 + ONE ambient system: slow diagonal **window-light god
  rays** on the Home hero only (atmosphere.md recipe, 30s drift, reduced-motion → static
  beams). Light sections: flat bone with a faint paper-grain, no rules/hairline fields
  (Rev 3's territory). Animated-system budget: entrance + hover + 1 ambient = 3 of ≤4.
  No reactive field — wrong register for a law office.

## 10 · Logo (hard rule)

**Already downloaded by the lead: `mockup/assets/logo.png`** (from the dossier's logo
line at pauldasilvalaw.com) — 1888×706 transparent PNG, ~2.67:1, scales-and-pen roundel
+ two-line wordmark ("DaSilva &" in `#00588A`, "ASSOCIATES, LLC" in `#747679`). Ships
as-is: never redrawn, never replaced with a text lockup, never hotlinked.

- **Header treatment (the mark is WIDE — no square slot):** full-color logo on the bone
  header, rendered at ~48px tall (≈128px wide) desktop / ~40px mobile, left-aligned with
  clear space ≥ the roundel's width on each side. Full color works because the header is
  bone and the site accent IS the logo blue (§3) — no knock-out needed, nothing collides.
- **Footer:** full-color mark again on the bone footer beside the NAP.
- Never place the full-color logo on a verde band (blue-on-dark-green fails contrast);
  the dark bands carry no logo.
- Alt: `DaSilva & Associates, LLC logo`. Optimize a downscaled copy for display width
  (keep the original in assets); no visual edits to the mark itself.

## 11 · Imagery — register + slot list

**Register: `editorial` (ONE register sitewide).** Justification (required): a law
office's proof is professional presence, not job photos — a commissioned-shoot look is
exactly Paul's stated goal #3 ("more professional"), and there is no "finished work" to
photograph in the proud-contractor sense. Prompts follow imagery.md's photorealism kit,
editorial register. **No readable business names, signage, lettering, or documents-with-
legible-text in any generated image. No faces (never Paul's, and no invented stand-in
attorney). No fabricated CourtTV material.**

| # | Slot | Status | Spec |
|---|---|---|---|
| 1 | Home hero (full-bleed background, section 1) | **GENERATE** | `16:9`, `2K`. Prompt: "Editorial interior photograph of an empty counsel table in an older wood-paneled American courtroom, early morning; tall windows off-frame right casting long diagonal shafts of soft daylight across dark walnut wood; a closed leather folio and a single legal pad on the table, no readable text; deep green and warm off-white grade, muted tones, shallow depth of field, quiet and grave mood; shot on a full-frame camera at 35mm, f/2.8, natural light only; no people, no signage, no seals, no readable lettering." Optimize → WebP at display width, under verde scrim. |
| 2 | Home service-area split (section 5, contained) | **GENERATE** | `4:3`, `1K`. Prompt: "Editorial street photograph of a Newark, New Jersey neighborhood block in early morning light: modest brick row buildings with ground-floor storefronts, awnings with no readable lettering, a church spire in the far distance, parked cars with no visible plates; warm low sun raking across brick, long shadows, muted editorial color grade; 50mm, f/5.6, eye level; no people in focus, no readable signage or license plates." Honest alt text: "Newark neighborhood street" — no claim it is Lafayette Street. |
| 3 | Attorney portrait (bio 14) | PLACEHOLDER | Labeled frame, 3:4, styled in direction colors: `[Photo of Paul Da Silva goes here — awaiting client photo]`. NEVER generated. |
| 4 | Municipal Court split image (practice 9) | **GENERATED** (post-plan, Harry-approved 2026-08-04 — takes the cap slot slot 2 freed) | `4:3`, `1K` → `assets/municipal-courtroom.webp` (1120×837, 48 KB). Prompt: "Editorial interior photograph of an empty municipal courtroom bench detail, early morning. Warm oak judge's bench and clerk's desk in an older American municipal courtroom; soft daylight from high windows raking low across the wood grain; empty gallery chairs falling out of focus behind. Deep green and warm off-white grade, muted editorial color, shallow depth of field, quiet and grave mood. Shot on a full-frame camera at 50mm, f/2.8, natural light only. No people, no signage, no seals, no emblems, no readable lettering, no documents with legible text." Illustrative, not a specific courthouse — no caption, no location claimed in alt text. |
| 5 | Google Map (contact 20) | EMBED PLACEHOLDER | Styled block + comment: map embed for 385 Lafayette Street, Newark, NJ 07105. |
| 6 | OG image | derived | Reuse slot 1 WebP crop (1200×630). No extra generation. |

Plan shipped at the hard cap: exactly 2 GENERATE (hero + next most visible), via
`/generate` on `nano-banana-2` (never `-lite`). Everything else placeholder.

**Still inside the cap as built.** Slot 2 never used its generated street shot — the
client supplied a real photograph of the office, so that generation doesn't count against
the cap on the shipped site. Slot 4 was generated on 2026-08-04 (Harry approved directly)
and takes the freed slot. **Live AI images: slots 1 and 4 — two, at cap.** Spend on the
shipped pair: ~$0.10.

**VIDEO: none.** Zero video slots on this build, in either register (mandated; nothing
here passes the filmed-action frame-2 test, and a designed-loop fails occupational fit
for a law office).

## 12 · Local-service conversion patterns (local-trade.md, adapted to a law office)

- Tap-to-call `tel:+19733440808` in the header on every page, visible on mobile; CTA
  repeated top (header/hero), mid (call bands 7/13/17), and footer.
- ONE primary action sitewide: call. Form is the quiet secondary on Contact only.
- Service-area block with his real REGIONS (never an invented town list): Home 5 +
  contact 19.
- Trust strip from real credentials only (Home 2): year, referral rate, practices,
  languages. No license/rating lines — none exist; nothing fabricated, no placeholder
  badges pretending otherwise.
- No before/after gallery (no work product to show; not faked).
- Estimate form → 4-field contact form (18).
- Consistent NAP footer on all 4 pages, matching JSON-LD exactly.

## 13 · Local SEO plan (his #1 goal)

- **JSON-LD `Attorney`** (LocalBusiness subtype) on every page, identical NAP:
  name "DaSilva & Associates, LLC", telephone "+1-973-344-0808", faxNumber
  "+1-973-344-3838", address 385 Lafayette Street, Newark, NJ 07105, foundingDate
  "2002-05", founder Paul Da Silva, knowsLanguage ["en","pt","es"], areaServed "New
  Jersey", url https://pauldasilvalaw.com/. **OMIT `email` and `openingHours` entirely**
  (none published — inventing them is an automatic fail).
- **Titles/descriptions per page, service + place:**
  - index: `Newark NJ Attorney — Municipal Court, Criminal, Real Estate & Matrimonial Law | DaSilva & Associates, LLC`
  - practice-areas: `Practice Areas — DWI & Municipal Court, Criminal Defense, Real Estate, Matrimonial Law | Newark, NJ`
  - attorney-bio: `Paul Da Silva, Attorney — Newark, NJ | DaSilva & Associates, LLC`
  - contact: `Contact DaSilva & Associates — 385 Lafayette Street, Newark, NJ | 973-344-0808`
  Descriptions ≤160 chars each, naming the practice split and the two-tier service area
  where it fits; written to spec register.
- Canonicals to `https://pauldasilvalaw.com/` paths; keep slugs aligned with the old
  site (`/practice-areas/`, `/attorney-bio/`; note for Corey: old `/contact-us/` should
  301 to the new contact page at launch — GoDaddy DNS + real domain, Q17).
- OG + Twitter card tags (OG image = slot 6), inline SVG favicon (azul "D" monogram is
  acceptable as a favicon glyph only — it is not a logo replacement), semantic
  `<header>/<main>/<section>/<footer>`, one h1 per page, descriptive internal anchor
  links between the practice cards and their sections.

## 14 · Embed placeholders

Contact form (18) — styled 4-field placeholder with inline demo confirmation on submit
(no silent click); Google Map (20) — styled placeholder block; both with HTML comments
saying what gets wired later. No real third-party services.

## 15 · Content honesty notes

- "24 years" only as arithmetic from **May 2002** (his number); prefer stating "since
  May 2002."
- No bar admissions, email, hours, awards, results, win rates, staff, or reviews —
  unpublished/unauthorized; write around, never placeholder-fake a credential.
- The old site's "decades of experience" is supportable (JD 1996) but render it
  concretely (e.g., practicing since 1996 / office opened May 2002) rather than as a
  vague boast.
- Generated images carry no claim: hero alt "counsel table in a courtroom," street alt
  "Newark neighborhood street." Neither pretends to be HIS courtroom or HIS block.

## 16 · Stage 3 evidence sheet

**Local `Inspiration/` library (checked first; filenames are hashes):** mostly trade
photography (excavators, meadows, mountain lake — wrong register here, not used) plus
four site mockups. One pattern drawn: **`251d045b…jpg` ("Heritage Architecture" landing)**
— a dusk-graded, two-tone **diagonal-split ground with a serif display headline set
in-media over a full-scene illustration**: the evidence that a dark, atmospheric ground +
restrained serif can carry authority without hairline rule-work. Informs the Home hero's
in-media composition and the dusk-toned grade. The Greenora/Haven/OG-Outdoors mockups
are the light SaaS-template look this build deliberately avoids. No image is shipped or
seeded (no video on this build).

**Live references (patterns, never copies):**
- **Bryan Brown Law (via OnTheMap/AALM roundups)** — crisis-audience restraint: simple,
  uncluttered page, a personal first-person hero instead of credentials-first. Pattern
  taken: personal voice up top (our owner quote-monolith), minimal section count.
- **Parikh Law** — a solo defense attorney carrying a bold two-color scheme (orange/dark
  gray) with confidence; evidence that a strong non-navy palette keeps gravity. Pattern:
  one saturated accent against a dark neutral (our azul-on-verde).
- **The Modern Firm criminal-defense portfolio** — category baseline: navy/gold serif
  templates with courthouse stock — the exact "vanilla" to beat; confirms the convention
  we're bending.
- **Clio criminal-defense design guide** — conversion spec for crisis visitors: sticky
  call bar, "Call"-verb CTAs, plain language over legalese, short forms. Pattern: header
  tap-to-call + 4-field form + phone-dominant contact page.
- **OnTheMap best-law-sites roundup** — recurring elite patterns: attorney-portrait
  anchor (our bio split with a real-photo frame), muted restrained palettes,
  localized photography over stock (our Newark streetscape slot).

## 17 · Stage 4 anti-repetition (crew `design-memory.md`, last 3 rows)

Banned and avoided: **fonts** Zilla Slab/Work Sans, Instrument Serif/Hanken Grotesk,
Libre Caslon Text/Albert Sans (+ the lead's wider list: Spectral/Public Sans,
Archivo/Barlow, Fraunces/anything, and the skill's global bans) → picked Frank Ruhl
Libre/Red Hat Text, used by no row. **Palette families** natural bark/moss/hi-vis,
warm-editorial paper+cobalt+clay, porcelain-and-ink with brass → courtroom-green
dark-first with the logo's own blue; no brass anywhere. (Noted: fora-digital's cobalt
was also a blue accent — different family: warm paper gallery-wall vs dark-green banded
poster, and `#00588A` is the client's fixed brand color, not a chosen accent.) **Archetypes** canopy-descent full-bleed,
gallery-wall plates, modular ruled ledger (+ earlier rows' sidebar letterhead,
spec-sheet+bento) → civic poster-stack: full-width bands, oversized numerals, ZERO
hairline rule-work. **Background systems** dapple+scrim, linen grain+washes+compass
field, porcelain rule-field+ink bands → verde layered gradient + window-light rays.
**Motion** (see §9). Not a returning-client re-plan: `dasilva-associates` has no prior
Claude Design project; the frozen `paul-da-silva-law` build is a different deliverable
Harry keeps, which is exactly why the divergence table below is a hard gate.

## 18 · Divergence table vs `paul-da-silva-law` — "Counsel of Record" (Rev 3)

| Axis | Rev 3 | This build |
|---|---|---|
| Layout archetype | Modular ruled ledger — Swiss compartments, collapsed hairlines, ink bands, 7/5 spans | Civic poster-stack — full-width bands, oversized numerals, no hairline rule-work at all |
| Typography | Libre Caslon Text / Albert Sans (variable) | Frank Ruhl Libre / Red Hat Text |
| Palette | Light-first porcelain + ink + brass (63% porcelain) | **Dark-first deep azul + cool paper + gold.** ⚠ See the honesty note below — this axis narrowed after the repaint |
| Background system | Flat porcelain rule-field + corner washes + grain + ink bands | Layered verde gradient + window-light god rays + bone paper; no rule-field, no washes |
| Motion | rules-draw-in + weight-shift hover + sticky progress rail (tier 0) | blur-focus + icon-nudge + NO set-piece + one ambient ray system (tier 0) |

**4 of 5 axes diverge cleanly (≥3 required) — the palette axis is now PARTIAL, and that is
worth stating plainly rather than scoring generously.**

> **Honesty note, added by the lead with the 2026-08-03 repaint.** As originally planned,
> the palette axis diverged completely: courtroom green against Rev 3's porcelain-and-brass,
> with the plan explicitly claiming "zero brass/gold." Harry's instruction moved this build
> to **azul and gold** — and **gold is the same metal-accent family as Rev 3's brass.** The
> two builds now share an accent family they were specifically designed not to share.
>
> **What still separates them, and it is substantial:** Rev 3 is **light-first** (63%
> porcelain) with brass *demoted to structure* — `--ouro` is text in exactly one CSS rule.
> This build is **dark-first**, with gold as a full working accent that carries the CTAs and
> band numerals on deep azul grounds. Opposite ground, opposite role for the metal. Add the
> four axes that diverge outright — layout archetype, typography, background system, motion
> — and the builds do not read as siblings.
>
> **This does not fail the ≥3 requirement and is not a reason to reopen anything.** It is
> recorded because the anti-repetition log is only useful if it is accurate, and because the
> Critic's round-1 distinctiveness PASS was reached against the *green* build. **The
> distinctiveness check must be re-run against the azul+gold screenshots**, specifically
> comparing gold-on-azul here to brass-on-porcelain there. If it comes back too close, that
> is a direction issue for Harry, not a Builder fix.

Structure differs too: Rev 3 is a compartmented single-flow; this is 4 indexable files with
dark/light banding.

## 19 · Stage 5 — the three directions and the pick

**Direction 1 — "The Quiet Verdict" (PICKED).**
Concept: courtroom gravity in deep green; his numbers set huge; plain words. Layout:
civic poster-stack (dark/light full-width bands). Type: Frank Ruhl Libre / Red Hat Text.
Palette: verde/bone/azul — the accent sampled from his own logo (family: dark courtroom
green). Background: layered verde gradient + window-light rays + grain. Motion:
entrance=blur-focus, hover=icon-nudge, set-piece=none, tempo 600ms
`cubic-bezier(.16,1,.3,1)`/70ms, GSAP tier 0. Composition device: ≥3× numeral scale jump
(trust strip). Hero: counsel-table image, in-media h1. Convention call: **honors** the
legal palette through deep green + the firm's own trust-blue while refusing the
navy-gold default. Why bold: nobody in this category locally runs dark-green poster
typography anchored to the client's actual mark; it is unmistakably serious yet visibly
not the template Paul complained about — and the fixed logo can't collide with a palette
built from it.
Taste check: passes §0.D (no purple gradient, no centered-hero-over-mesh, no 3-equal-card
default — cards exist once, as his numbered four) and §9 (serif justified: heritage/
authority family with an articulated reason; no AI tells in the section plan).

**Direction 2 — "Letter of the Law" (not picked).**
Concept: the composed, light counter-proposal. Layout: centered-classic + editorial
columns. Type: Literata / Source Sans 3. Palette: bone ground, authority-navy ink, warm
gold accent (family: light navy-gold — **honors** the convention outright). Background:
flat bone, generous whitespace, no texture. Motion: entrance=slide-alternate,
hover=zoom-crop, set-piece=none, tempo 700ms/60ms, tier 0. Composition device: dominant
column. Hero: split with portrait frame. Why not: it is the tasteful version of exactly
the navy-gold category default — Q7 ("too vanilla") argues against picking it; diverges
from Rev 3 on only 3 axes.

**Direction 3 — "Headline Docket" (not picked).**
Concept: newsprint-brutalist — the CourtTV commentator as front page. Layout:
magazine/broken-grid, oversized condensed heads. Type: Big Shoulders Display / IBM Plex
Sans. Palette: true off-black + warm tan + one signal red (family: black-and-tan —
**breaks** the convention; trust cue kept via monochrome restraint). Background: flat
duotone blocks, halftone texture. Motion: entrance=skew-slide, hover=crossfade-zoom,
set-piece=CSS scroll-scrub on the timeline, tempo 500ms/50ms, tier 0. Composition
device: off-grid offset columns. Why not picked: visually the loudest of the three, but
a tabloid register is the wrong gravity for a family walking in scared, and it leans on
the media credential he mentioned only in passing — Direction 1 is the boldest that
still carries the gravity the brief demands.

Axes check: 1 vs 2 differ on layout/type/palette/background/motion (5); 1 vs 3 differ on
5; 2 vs 3 differ on 5. None hits a banned combo.

## 20 · Builder notes

- Multi-file build: shared `style.css` + `main.js`; per-page `<title>`/meta/JSON-LD;
  works by double-click, offline, no CDN (fonts via Google Fonts link are the standing
  exception; vendor nothing else — tier 0).
- JS-off test applies: hidden entrance states only under the `html.js` guard from
  motion.md rule 0; rename `main.js`, reload, every word readable.
- Run trade-copy `copycheck.py` + web-humanizer `aitells.py` on all four pages; the
  voice spec's hard exclusions are Critic gates.
- Release form: generate from `templates/release-form.html` with the 4 built pages
  listed; blanks stay blank.
- The Critic walks §7 against the mockup; anything unplaced and unlisted is a fail on
  both of us — message me, not the void, if a block has no home.
