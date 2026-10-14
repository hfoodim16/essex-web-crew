# Website plan — ATLAS LAW (`Atlas-Law`)

> The Planner's reasoning record, for Harry and the Critic. **The Builder never reads
> this file**: everything executable is in `build-sheet.md`, which outranks this plan.
> Voice contract: `voice-spec.md`. Written 2026-10-12, web-design-ultra Stages 1–5.

## Design Read

**Reading this as: a three-page credibility site for owners and executives of $50–200MM companies with no in-house lawyer (and for opposing counsel checking him out), with a plain, first-person, fairly casual professional language, leaning toward a white page with full-strength Kentucky-blue color fields, a modern wide grotesk over a crisp text serif, and his real studio portrait as the proof.**

Mode (taste §11): **Greenfield.** The old domain is an unfinished Squarespace AI draft with nothing the client wrote (Q12–Q14 blank, no logo, no name, no contact). Nothing to preserve but the name as set ("ATLAS LAW") and the domain.

## Stage 1 — Brief

- **Product:** brochure site, static, three pages (Home, Practice areas, About). No contact page, no form.
- **Audience:** owners/CFOs/COOs of companies with ~$50–200MM revenue and no legal department (Q6). Secondary: opposing counsel and referral sources verifying him (Q5); LinkedIn connections after his launch post (Q7). Mostly desktop, often a phone off LinkedIn.
- **Mood words (client's):** Professional; Modern; Helpful (Q15). Fairly casual, texts clients (Q16).
- **Colors (client's):** Kentucky blue and white (Q18). No logo yet (Q19).
- **References (client's):** uristlaw.com, twelvestonegc.com, turleylaw.com, sentiogc.com (Q17). All four are solo or boutique fractional-GC sites.
- **Harry:** "Keep it professional and follow the questionnaire. Feel free to generate images, but be sure to use the headshots."
- **Speculation log (B0a):** not applicable. `client-answers.md` carries no SPECULATIVE banner and no prior build exists for this prospect, so there is no delta to log.
- **Returning client:** no. No Claude Design project exists for Atlas-Law.

## Decision map (decision-readiness §1)

1. **Who arrives, from where?** LinkedIn connections clicking his launch announcement; referrals from word of mouth checking him out before they email; opposing counsel looking him up; anyone searching "ATLAS LAW" / "Matthew Atlas". → named face + admissions above the fold on Home and About.
2. **What problem are they solving?** A mid-size company has a contract, employment, lease or dispute problem, or wants steady legal coverage, and has no lawyer on staff. → full Q9 lists on Practice areas; fractional GC as its own block.
3. **What must they understand in 5 seconds?** A business lawyer, a real named person with a face, admitted in NJ and NY, 15+ years in-house at companies they know, and how to reach him. → `home-hero` + `home-credentials`.
4. **What would make this the wrong provider?** Personal matters (family, criminal, injury); companies outside the revenue band; matters outside NJ/NY admission. → "Business law" eyebrow, "for companies…" subtext, the revenue band in `home-approach`, admissions everywhere.
5. **What evidence would make them believe it?** Exists: real portrait (2), admissions (Q23, NY registry), the four employers (Q3), 15+ years (Q3), UVA law school (registry), launch dates (Q2). Missing: reviews, titles per company, any matter examples. → credentials strip, about table; no review section.
6. **What uncertainty stops them acting?** Cost (→ fixed fee / subscription band and tiles), "does he handle my issue" (→ every sub-item listed + "if it isn't listed, ask"), confidentiality (→ footer disclaimer), "will a real person answer" (→ "Messages go straight to me", his own email and number).
7. **What does the next step commit them to?** An email or a text. Nothing else: no form, no booking, no fee statement (none given, so no "free consultation").
8. **What happens after they act?** Matt replies himself (solo practice). No response time is promised: he gave none.

Every section in the sheet traces to a line above: hero (3), credentials (3, 5), approach (2, 4), practice tiles + practice page (2, 6), fees band + fractional bento (6), home-matt (1, 5), contact bands (7, 8), about hero/bio/background (1, 5), footer legal (6). No question is left without a section.

## Client answers → decisions

| Q | Their answer (short) | What the plan does |
|---|---|---|
| Name field | "Atlas Law" | Superseded by Q1's exact form. |
| Current site field | www.matlas-law.com | Domain for canonical URLs + JSON-LD. Old site content dropped (content map). |
| 1 | "ATLAS LAW" | Set in capitals everywhere: header + giant footer wordmark, body copy, title tags, JSON-LD `name`. |
| 2 | Launching own firm as of September; back in private practice since last September; 15+ yrs in-house; wants momentum and to let people know he's available | Dates on `home-matt` and `about-background` (Sept 2025 / Sept 2026); his "this is what I'm doing now … available" becomes the site's one lyrical block (`home-matt`). LinkedIn-launch framing drives a credibility-first hero. |
| 3 | 15+ yrs in-house at JPMorgan Chase, Colgate-Palmolive, Saks Fifth Avenue, Related; understands the client side; practical solutions; legal not the obstacle | The hero h1 ("…spent over 15 years in-house"), the credentials strip, `home-approach` (his phrases: "client side", "legal and business advisor", "solve problems", "the obstacle to getting things done"), About. Employers as text only, never logos (trademark/endorsement risk). His "different lens than outside counsel" point is NOT published as a comparison (NJ RPC 7.1(a)(3)); it's made through facts about him. |
| 4 | Based in NJ and NY, can service clients anywhere | "I'm based in New Jersey and New York and take clients from anywhere." (`home-approach`), about table "Clients: Businesses, wherever they're based". Worded so it never implies admission elsewhere; admissions stated beside it. JSON-LD `areaServed` = NJ, NY. |
| 5 | Look professional and established, "not a hack", to prospects and opposing counsel | Drives the whole direction: real formal portrait above the fold, admissions on every page, square-cornered restraint, no gimmicks, no stock gavels, no invented praise. |
| 6 | Target: $50–200MM revenue companies without in-house legal; they can't justify a full-time lawyer; outside counsel more expensive/less skilled | Audience line in hero subtext; revenue band + "don't need, or can't fund, a full-time lawyer on staff" in `home-approach`. The "more expensive and possibly less skilled" reasoning stays OFF the site (comparison ban). Question 4 to Harry: OK to publish the revenue band? |
| 7 | Word of mouth only; will link from LinkedIn for a formal announcement | OG/Twitter cards built for a clean LinkedIn preview: OG image = his real formal portrait (crop only) + the wordmark on a Kentucky-blue panel, so the preview shows the person, not a stock building. Footer LinkedIn link wanted but no URL given → question for Harry; not invented. |
| 8 | Four items: mission/value overview, services per Q9, bio, contact info | Page map: Home (mission/value + teasers), Practice areas (Q9 in full), About (bio), contact on every page (header buttons, closing band, footer). |
| 9 | Five areas in order with sub-items | Practice areas page carries every sub-item in Q9 order: `pa-commercial`, `pa-employment`, `pa-disputes`, `pa-real-estate`, `pa-fractional`; home bento tiles keep the same DOM order. Abbreviations expanded once (NDAs, M&A, LOIs, RIF, EEOC kept). |
| 10 | (blank) | No preference: nothing phased out; carry all of Q9. |
| 11 | No discounts; emphasize openness to Fixed Fee/Subscription (strengthened by U2) | Credentials strip item 3, full-width blue `home-fees` band, two fee tiles in `pa-fractional` plus a line saying the options apply to the other areas too, about table row. No prices, no discount language, no "monthly" (he never said how a subscription is billed). |
| 12 | (blank) | No preference; old site dropped (it's a template draft). |
| 13 | (blank) | Same. |
| 14 | (blank) | Nothing protected word-for-word. |
| 15 | Professional; Modern; Helpful | Register = professional office, first person; modern grotesk display; "helpful" carried by plain lists, "if it isn't listed, ask", and visible contact, never by calling himself helpful. |
| 16 | Fairly casual; uses text messages | Sets the register only: contractions, "I", "Email Matt" / "Text 917-213-4979" CTAs. Not written as copy (a "fairly casual" line works against Q5's "not a hack"); the texting fact is carried by the Text buttons. |
| 17 | uristlaw, twelvestonegc, turleylaw, sentiogc | Studied at Stage 3 (evidence below). Took: headshot-in-hero split (Urist), background definition list (Twelvestone → `about-background`), plain business-owner register (Turley), blue color-block confidence (Sentio). Copied no layout, line, or color whole. |
| 18 | Kentucky blue and white | `--kentucky:#0033A0` + `--white:#FFFFFF` are the page. Hex reasoning below; Question 1 to Harry. |
| 19 | Working on a logo | Wordmark only ("ATLAS LAW" in Mona Sans, 125% width, 800 weight); typographic "A" favicon flagged as a placeholder; no invented mark. |
| 20 | (blank) | No job photos exist (a lawyer has none). Generated plates are architecture/interiors only, editorial register, no people. |
| 21 | (blank) | Nothing to photograph requested. |
| 22 | (blank) | **No testimonial section** (real reviews only). No placeholder block either: an empty review frame on a launch-announcement site reads unfinished. |
| 23 | Admitted to the NJ and NY bars | Credentials strip, hero/about subtext, footer, about table. No "certified"/"specialist". |
| 24 | Prefer email (matt@matlas-law.com) or text (917-213-4979) | Primary CTA "Email Matt" (mailto), secondary "Text Matt" (sms:). No form, no booking, no "Call now". Mobile header keeps both visible. |
| 25 | Same email/text; no hours or after-hours line | Same NAP everywhere; no hours shown (none given), none in JSON-LD. |
| 26 | Don't show physical address | No address anywhere, no map, no `address` in JSON-LD. Name + phone satisfies NY Rule 7.1(d) Comment [10] per the dossier. |
| 27 | (blank) | No FAQ section. |
| 28 | (blank) | No policies stated. Footer carries a proposed disclaimer/privacy text the attorney must approve (launch blocker). |
| 29 | Don't need a Contact Me tab | Nav = "Practice areas", "About" only. Contact = header buttons + closing band per page + footer. |
| 30 | www.matlas-law.com | Canonical/OG URLs; release form domain line. |
| U1 (update 2026-10-13) | "AI Based Law Firm": AI tools make the work more efficient; clients pay for his experience and legal/business judgment, not his time; client-side experience informs the advice | Highlighted in three places inside the existing design, no new section: the home hero eyebrow becomes "AI-assisted business law · New Jersey & New York"; the home blue band (`home-fees`) is reframed to "An AI-based firm with flexible fees" and moved up to sit directly under `home-approach`; About gets one bio paragraph and a "How I work" table row. Every AI mention sits beside "I do the legal work … and stand behind the advice." The client-side point is already carried by `home-approach` ("so I understand the client side well"); the "traditional law firms" comparison is not published (list below). |
| U2 (update 2026-10-13) | "Alternative Fee Arrangements and Subscriptions": flexible fees for rate and budgeting predictability; AI + lower rates = value | Extends what Q11 already placed rather than duplicating it: the same `home-fees` band carries "Fixed fee or subscription" as its second block ("…so you know the rate and can budget for it."); the `pa-fractional` page line now names "Alternative fee arrangements"; the About "Fees" row uses his term. "Lower rates" and the value/"bang for their buck" promise are not published (list below). No prices. |

**Conflicts / ambiguity found:** none that blocks. Q8 ("Contact information" as a must-have) and Q29 ("Don't need a Contact Me tab") read together as contact on every page with no contact page, which the plan does. Q4 "can service clients anywhere" needs careful wording against his two admissions (done). Q6's comparative reasoning can't be published (ethics, not a conflict).

## Stage 2 — Design intelligence

- `search.py "fractional general counsel business law firm solo attorney professional modern helpful" --design-system` → pattern "Trust & Authority + Conversion", style "Accessible & Ethical", palette authority navy `#1E3A8A` + trust gold `#B45309` on `#F8FAFC`, fonts EB Garamond / Lato. Taken: the accessibility floor (focus rings, 44px targets, reduced motion), "hidden credentials" as the thing to avoid. Diverged from: the gold accent and the Garamond/Lato pairing (category default).
- `search.py "law firm" --domain color` → **no database match**; retried `"legal services"` → Legal Services: navy `#1E3A8A` + gold `#B45309`, note "Authority navy + trust gold". That is the industry convention for the Stage 5 call.
- Typography query (modern professional) returned Poppins/Open Sans and Outfit/Rubik: both on the watchlist or generic; rejected.

## Stage 3 — Inspiration evidence

Industry pack read first: `Inspiration/industries/law/notes.md` + `teardown.md`. Its rules became ledger rows (no comparisons, no specialist/certified, testimonials only if real, award disclaimers N/A). Its "type already used for law" list is honored (none reused). Its color note ("break it for business boutiques that sell sharpness") supports the saturated-blue call.

The client's four references were captured with `bin/inspo law …` on 2026-10-12 into the law pack and read as images: `Inspiration/industries/law/uristlaw.com-page.jpg`, `twelvestonegc.com-page.jpg`, `turleylaw.com-page.jpg`, `sentiogc.com-page.jpg` (each also has `-desktop`/`-phone`). Craft/conversion references from the pack: `ario.law-desktop.jpg`, `dorsellaw.com-desktop.jpg`.

| Site | Hero | Layout | Type | Color | Proof / CTA | One thing to steal |
|---|---|---|---|---|---|---|
| uristlaw.com (client ref) | split-screen: headline left, cut-out headshot right on dark teal | alternating image+text (zigzag ×3), grouped bullet lists | serif display (Lora-like) + geometric sans | dark teal + chartreuse CTA | "Let's Talk" ×3, testimonial cards, free consult | **The named lawyer's face in the hero, on a saturated field.** (Not stolen: the zigzag, the chartreuse, the stock B/W office photos.) |
| twelvestonegc.com (client ref) | centered statement on navy, gold eyebrow | Swiss/modular grid, numbered card grid, background definition list | Georgia-like serif + sans eyebrows | navy + gold | "Schedule a consultation", inquiry form, LinkedIn | **The "Background" definition list** (role, admission, education, location) → `about-background`. (Not stolen: navy+gold, 01–04 numbering.) |
| turleylaw.com (client ref) | full-bleed image/video with heavy grotesk caps h1 | utility bar, card grid, numbered lists, FAQ, sticky mobile bar | condensed heavy grotesk + serif italic | cream + black + yellow | "Book a Consultation — $125" everywhere, results with disclaimer | **A plain business-owner register** and contact always reachable on mobile. (Not stolen: video hero, prices, yellow.) |
| sentiogc.com (client ref) | asymmetric offset: serif headline left, stacked navy + stat cards right | card canvas | serif display + sans body | warm white + navy + sage | "Schedule a conversation", stat cards (3x, 20–40%) | **Confidence of one big solid blue block** on a light page. (Not stolen: unsourced comparative stats like "20–40% vs in-house GC" — those would fail our ledger.) |
| ario.law (juried, Awwwards HM) | oversized wordmark as graphic + named partner on video | editorial asymmetric | neo-grotesk | black/white | weak CTA on phone | **The firm name set huge as a graphic** → the footer wordmark, which is also the only "logo" he has. |
| dorsellaw.com (conversion) | text-led headline + two hard numbers | stat strip under hero | geometric sans | warm grey + navy + blue CTA | "Call Now" kept beside the menu | **Two verified facts right under the promise** → `home-credentials`. |

**Synthesis.** Carry forward: face-in-hero, a facts strip directly under the hero, a definition-list background, one confident blue block, contact always reachable. Break deliberately: navy + gold, serif-display + sans-body (every law build we've shipped), zigzag image/text, stock office photography, comparative stats, consultation-fee CTAs.

`Inspiration/` photo plates (excavator, meadow, grass) are trade photography; none fits a law practice, none is used, and no image-to-video seed is named.

## Stage 4 — Anti-repetition

Last 3 rows of `design-memory.md`: paul-da-silva-law Rev 3, gee-kay-landscaping Rev 2, dasilva-associates. Banned for this build, and how Atlas avoids each:

| Axis | Banned (last 3) | Atlas |
|---|---|---|
| Fonts | Libre Caslon Text / Albert Sans · Newsreader / Familjen Grotesk · Frank Ruhl Libre / Red Hat Text (also law-pack list: Young Serif, Besley / Schibsted Grotesk) | **Mona Sans / Source Serif 4**, never used by the crew; inverts the law default (sans display, serif body). |
| Palette | porcelain + ink + brass · grey-green plan paper + spruce + flag orange · dark-first azul + gold | **Pure white + saturated royal blue fields + ink, no metal accent at all.** Differs from dasilva on ground (white-first vs dark-first), on the blue (bright PMS 286 royal vs deep azul `#041E30`), and on accent (none vs gold). Differs from Rev 3 on ground (true white `#FFFFFF`, not porcelain) and accent (no brass). |
| Layout | modular ruled ledger · 7/5 measured register · civic poster-stack (h1 over full-bleed photo, alternating light/dark bands) | **Editorial asymmetric with a portrait overlap.** No hairline rule system; the home hero is a solid color field with a real portrait, not an h1 over a photo; blue bands appear twice on long pages, not alternating. |
| Background | flat porcelain rule-field · surveyor tick-field + grain · photographic hero + azul scrim + god rays | Monochrome blue radial "field" + 0.05 grain on blue areas only; white areas flat. No god rays, no ticks, no rules. |
| Entrance | rules-draw-in · slide-alternate · blur-focus | **clip-wipe** |
| Hover | weight-shift · rule-trace edge-lift · icon-nudge | **fill-sweep** (the `→` glyphs do not move) |
| Set-piece | sticky-progress · hero-exit · none | **CSS scroll-scrub** on one plate |

Disclosed overlap outside the window: FORA's own agency site (2026-07-23) also used cobalt and an ink-sweep (fill-sweep/underline-draw) hover. It is not a client build and is outside the last-3 window. I chose clip-wipe over mask-curtain specifically because FORA's signature was a cobalt mask-curtain.

Copy ledger (`copy-memory.md`): hero construction is new (plain noun phrase + relative clause carrying a tenure number). Not a three-fragment + year, not a negated pair, not second-person aspiration, not dasilva's contrast appositive. `grep '<h1' prospects/*/mockup/index.html` shows no sibling shape.

## Stage 5 — Three divergent directions

**Industry color convention:** law = authority navy + trust gold (engine: Legal Services `#1E3A8A` + `#B45309`; psychology: gravity, tradition, trust). The client's "Kentucky blue and white" keeps the blue trust cue and drops the gold, so every direction honors the blue and none uses gold; they differ in how hard the blue is pushed.

**Direction A — "Kentucky Field"** (Planner)
- Concept: Kentucky blue used as a full-strength field, the real portrait stepping out of it; modern, confident, unmistakably "blue and white".
- Layout: editorial asymmetric; hero 7/5 split on a solid blue field with the portrait overlapping into white.
- Type: Mona Sans (wide wordmark, 110% headings, UI) / Source Serif 4 (body).
- Palette: `#FFFFFF` dominant, `#0033A0` fields + accent, `#0B1530` ink, `#E8EEF8` mist, `#4B5873` slate. **Breaks** the navy+gold convention (saturated royal instead of navy, no gold); keeps the blue trust cue and generous whitespace.
- Background: monochrome blue radial field + grain on blue; flat white elsewhere.
- Motion: entrance=clip-wipe hover=fill-sweep set-piece=scroll-scrub (one plate); 780ms `cubic-bezier(.77,0,.18,1)`, 80ms stagger; GSAP tier 0.
- Composition device: overlap (portrait crosses the hero field into the credentials strip).
- Hero + imagery: formal portrait in hero; editorial architecture/interior plates (no people). (Planned as 3; reduced to 2 at the B1b sheet review.)
- Comp: `prospects/Atlas-Law/directions/a.png`.

**Direction B — "Desk Bento"** (Planner)
- Concept: everything a prospect needs in one composed first screen of tiles.
- Layout: bento grid hero (headline tile, portrait tile, blue fee tile, credentials tiles, contact tile).
- Type: Literata (serif display) / Onest (sans body).
- Palette: mist `#EEF3FA` ground, white tiles, navy ink `#0B1F44`, one `#0033A0` tile. **Adapts** the convention (navy authority as ink, blue as one accent tile, gold dropped).
- Background: flat tinted tiles, no texture.
- Motion: entrance=scale-settle hover=zoom-crop set-piece=none; 600ms `cubic-bezier(.2,.7,.2,1)`, 70ms; GSAP tier 0.
- Composition device: ≥3× scale jump between the headline tile and the small fact tiles.
- Comp: `prospects/Atlas-Law/directions/b.png`.

**Direction C — "Open Counsel"** (GPT-6 Astra via `bin/ask-gpt --astra --effort high`; context file `/tmp/atlas-plan/c-context.txt`)
- Concept (Astra, verbatim): "Corporate experience presented with the clarity and accessibility of a direct conversation."
- Layout: centered spacious masthead, text-only hero, open vertical sequence, no tiles.
- Type: Barlow Condensed / Noto Sans.
- Palette: `#0033A0` headings and actions on white `#FFFFFF`, text `#152342`, recesses `#EAF0FC`, slate `#53627A`. **Honors** the blue cue, drops navy+gold ceremony.
- Background: uninterrupted white, pale-blue recessed panels with inner shadow.
- Motion: entrance=none hover=crisp color inversion set-piece=none; 140ms ease-out; GSAP tier 0.
- Composition device: the portrait pushed beyond the right edge of a centered column.
- Planner's hold-to-bans check: no banned font, palette, layout or motion. Barlow (as Barlow, not Condensed) was cedar-grove-transmission's body face, outside the last-3 window; acceptable. Hero headline "Business counsel. Built on in-house experience." is a two-fragment construction; it would need rewriting under our copy rules. No rewrite needed otherwise.
- Comp: `prospects/Atlas-Law/directions/c.png`.

Divergence: A vs B differ on layout, type, color strategy, background and motion (5/5). A vs C differ on layout, type, background and motion (4/5). B vs C differ on layout, type, color strategy, motion (4/5).

**Taste check (§0.D, §9) on all three:** none uses purple, gradient text, glass, three equal cards, custom cursors, pill buttons, arch-top photos, drawn underlines, section-number eyebrows or invented stats. B's bento hero is the closest to a current AI-site trend (Sentio's card stack is the same move), which counts against it. C has no face above the fold, which fails the law pack's evidence #1 (the named lawyer), and its condensed blue caps read as campaign signage on the comp.

**Pick: A, "Kentucky Field".** Comps side by side: A is the only one where "Kentucky blue and white" is the first thing you see, at full strength, and the real portrait does the credibility work Q5 asks for. It's the boldest of the three in color and composition while staying squarely professional; B is pleasant but dilutes the client's color to one tile and leans on a trend; C is the quietest and loses the face. A also sits nearest the reference he likes most structurally (Urist's face-on-a-field hero) without copying its zigzag body. Visual target in the sheet: `directions/a.png`, with one correction: the comp's split-header under the strip is banned (Stage 8), so `home-approach` stacks its heading.

## Art direction

**"Kentucky Field."** White-first business-law site where Kentucky blue is used as a full-strength color field, never as a timid accent. The attorney's real studio portrait overlaps out of the blue into the white page, which carries the "real, established, practicing" message Q5 asks for. A modern wide grotesk for the wordmark and headings over a crisp text serif for reading; square corners, no gold, no ornament.

**Typography reasoning.** Mona Sans (variable width 75–125, weight 200–900) lets one family do the brand job (the wordmark at 125% width, weight 800, is his interim logo until he has one) and the heading job (110%) and UI labels. Source Serif 4 is a transitional text serif with optical sizes, so long Q9 lists and the bio read like well-set documents without a "legal letterhead" costume (the 2026-10-10 letterhead sample was rated 2.5/10). Neither is on the banned list or the FONT_WATCHLIST, and the crew has never used either.

**Kentucky blue: `#0033A0`.** "Kentucky blue and white" is the University of Kentucky's color pair; UK's official blue is PMS 286, `#0033A0`. Other readings considered: Kentucky bluegrass (a blue-green; nobody says "Kentucky blue and white" meaning grass) and the light "Carolina" sky blue (`#7BAFD4`, a different school's color, often confused). `#0033A0` passes 10.6:1 with white, so white type on the blue field and blue text on white both clear AA comfortably. **Confirm with client (Question 1):** show him the swatch next to a lighter alternative.

**Exceptions to house gates, stated so the Builder can waive and the Critic can accept:**
- `local-trade.md` patterns that don't apply to a solo business lawyer: **no estimate form** (Q24 prefers email/text; a form with no verified destination is a launch blocker), **no town list** (Q4: NJ, NY, clients anywhere; JSON-LD uses `State` areas), **no project gallery** (no job photos exist), **no reviews strip** (Q22 blank), **no map or address** (Q26), **no `tel:` "Call" CTA** (he said text; the number is shown and linked with `sms:`; Question 3).
- The header carries two CTAs (Email / Text). They are two channels he named, not one intent in two hats.

## Page map (tokens live in the sheet)

Classic multi-page, three files. Every section's `format:`/`opener:` token is in `build-sheet.md` (plan-lint reads them there).

- `index.html`: `home-hero`, `home-credentials`, `home-approach`, `home-fees`, `home-practice`, `home-matt`, `home-contact` (7 sections, 7 families, kickers 2/3)
- `practice-areas.html`: `pa-hero`, `pa-commercial`, `pa-employment`, `pa-disputes`, `pa-real-estate`, `pa-fractional`, `pa-contact` (7 sections, 7 families, kickers 1/3)
- `about.html`: `about-hero`, `about-bio`, `about-background`, `about-contact` (4 sections, 4 families, kickers 2/2)

Why a separate Practice areas page: Q9's Employment and Real Estate lists are long, real content; folding them into the home page would bury his value proposition. Why not five practice pages: Dispute Resolution and Fractional GC have no sub-items, so their pages would be empty. Why five practice-area sections take five different formats: their content genuinely differs in shape (two grouped lists; six parallel items; one line; a list beside a place; a definition of two fee options).

## Composition device

**Overlap**, carried by `home-hero`: the formal portrait, in the right 4 of 12 columns of the blue field, extends 48–128px below the field into the white credentials strip, crossing the blue/white edge. `about-hero` mirrors it. The Critic should be able to name it from the desktop screenshot.

## Signature motion

- **entrance = clip-wipe** (media top-down, tiles/cards left-to-right), only on photos, plates, bento tiles and employment cards. Text never animates in.
- **hover = fill-sweep** on buttons and linked tiles only.
- **set-piece = scroll-scrub**, one: the `pa-real-estate` image settles (scale 1.14→1) inside its 4:5 frame as it crosses the viewport, pure CSS `animation-timeline: view()`. (Moved from the dropped `home-fees` plate at B1b.)
- **tempo:** 780ms entrances, 220ms hovers, one ease `cubic-bezier(.77,0,.18,1)`, 80ms stagger.
- **GSAP tier 0.** Zero library bytes.
- Avoided (last 3 rows): rules-draw-in, slide-alternate, blur-focus entrances; weight-shift, rule-trace-lift, icon-nudge hovers; sticky-progress and hero-exit set-pieces. Not fade-up, not count-up (the stat figures are static), not a custom cursor, not magnetic.
- Background & atmosphere: blue "field" (two radials from the five tokens + 0.05 grain) on blue areas; no animated atmosphere: fog or god rays would undercut "professional". No reactive field (wrong register for law).

## Imagery

**Register: editorial**, one register for every generated slot. Justification: a business lawyer has no job-site photos, so the proud-contractor "best photo on their Google profile" frame doesn't exist for him; his real formal headshot is itself a commissioned studio portrait, so plates shot as documentary architectural photography sit with it. All plates are places, never people: no fake clients, staff or office.

| Slot | Kind | Aspect | Where | Why it earns its place |
|---|---|---|---|---|
| `home-hero` portrait | REAL (headshot-2, formal) | 4:5 | home hero | The credibility proof Q5 asks for; Harry's instruction. |
| `about-hero` portrait | REAL (headshot-2, formal) | 4:5 | about hero | Opposing counsel lands on About; the formal face belongs there. |
| `home-matt` photo | REAL (headshot-1, casual) | 1:1, ≤360px | home quote split, white ground only | Matches Q16's casual voice; shown small because the source file is soft; white ground because the file has a white feathered edge. Its only placement (dropped from About at B1b: it sat under the hero portrait's overhang). |
| `pa-hero` plate | GENERATE | 16:9 | practice page hero | The client's world (a mid-size distribution business: supply agreements, leases, employees), not the lawyer's. |
| OG card | REAL (headshot-2, crop) + wordmark | 1200×630 | LinkedIn / social preview | Q7: the LinkedIn launch preview should show the lawyer. |
| `pa-real-estate` plate | GENERATE | 4:5 | real estate split | An empty commercial space ready for a tenant, the literal subject of lease and construction work. |

`2 GENERATE slots, $0`. The glass-tower plate for `home-fees` was dropped at B1b (a looking-up office tower is a stock law cliché); that band is now a solid blue field. Not generated on purpose: anything with people, any office interior that could pass as "his office", skylines (would imply an office location he chose not to show), gavels/scales/courthouses (looks like evidence, isn't).

**Video: none.** Free ladder first: the static blue field + grain + one CSS scrub carries the depth. A `filmed-action` clip fails the frame-2 test (there's no work to watch), and a `designed-loop` behind a law practice is the convention error `color-conventions.md` warns about. No VIDEO request.

## Content map (content parity)

`site-content.md` is a Squarespace AI starter draft the client didn't write. Every block is deliberately dropped:

| site-content.md block | Destination |
|---|---|
| Home: "Strategic Legal Counsel / Comprehensive Legal Services and Business Solutions / Solving Legal Problems" | Deliberately dropped: template filler; banned vocabulary (strategic, comprehensive, solutions). |
| Home: "For more than 20 years, Atlas has delivered strategic legal and business counsel…" | Deliberately dropped: template claim; the client's own figure is "over 15 years as an in-house counsel" (Q3), used instead. |
| Home: "Discover Our Approach", "Stay Connected / Follow Us" (icons to Squarespace's own accounts) | Deliberately dropped: dead template links. |
| Home: "Let us know if you have a legal problem that needs a solution." | Deliberately dropped: replaced by the email/text bands (Q24). |
| Services: "Strategic Legal Solutions Tailored to Your Business" + two template paragraphs | Deliberately dropped: template filler. |
| Services: store products Paralegal Research $95, Contract Review $750, Legal Research $399, Trial Representation $350 (+4 product pages, "Add To Cart") | Deliberately dropped: Squarespace sample products, not his services or prices; his services are Q9, his fee position is Q11. |
| Services/About/Contact: "Request a (Confidential) Consultation" + form copy, "our team", "a qualified attorney" | Deliberately dropped: template; false for a solo practice; Q24 replaces the form with email/text; Q29 removes the contact page. |
| About: "About Our Legal Services" + two template paragraphs | Deliberately dropped: template filler; About is rebuilt from Q2, Q3, Q23 and the NY registry. |
| Cart page | Deliberately dropped: commerce artifact. |
| Firm name "ATLAS LAW" (all caps) | Carried: header/footer wordmark, every page. |
| Domain www.matlas-law.com | Carried: canonical, OG, JSON-LD, release form. |

Since parity for this build is the client's answers, here is where each answered fact lands:

| Client fact | Section |
|---|---|
| Q1 name; Q19 wordmark | Global header and footer (every page) |
| Q3 15+ years in-house | → `home-hero` (h1) |
| Q23 admissions; Q11 fees (as a fact) | → `home-credentials` (strip) |
| Q3 employers + client side; Q6 audience + revenue band; Q4 location | → `home-approach` |
| Q9 five areas (summary) | → `home-practice` (tiles) |
| Q11 fixed fee / subscription; U1 AI-based firm + U2 alternative fees | → `home-fees` (band, block A + block B) |
| U1 AI, as the first words on the site | → `home-hero` (eyebrow) |
| U2 alternative fees for every area | → `pa-fractional` (line under the bento) |
| U1 AI paragraph | → `about-bio` |
| U1 "How I work" + U2 "Fees" rows | → `about-background` |
| Q2 quote + dates | → `home-matt` |
| Q24/Q25 email + text | → `home-contact` (and every contact band, header, footer) |
| Q9 Commercial items | → `pa-commercial` |
| Q9 Employment items (all nested) | → `pa-employment` |
| Q9 Dispute resolution/litigation | → `pa-disputes` |
| Q9 Real estate items | → `pa-real-estate` |
| Q9 Fractional GC + Q11 fee options | → `pa-fractional` |
| Q2/Q3 bio prose | → `about-bio` |
| Q23 + registry law school + Q2 dates + Q4 + Q11 | → `about-background` |

## Claims ledger

| Claim (as worded) | Source | Type | Evidence on page | Missing before publish |
|---|---|---|---|---|
| "over 15 years" / "15+ years as in-house counsel" | Q3 | factual | employers named beside it | none |
| JPMorgan Chase, Colgate-Palmolive, Saks Fifth Avenue, Related (text, no logos) | Q3 | factual | names in text | titles + dates (optional, Question 5) |
| "Admitted in New Jersey and New York" | Q23; NY OCA reg. 4252565 (dossier) | factual | strip, heroes, footer, table | NJ year (optional) |
| "Law school: University of Virginia" | NY OCA record (dossier) | factual | about table | client confirms wording (Question 6) |
| Sept 2025 private practice / Sept 2026 ATLAS LAW | Q2 | factual | home-matt, about | none |
| "$50 million to $200 million in annual revenue" | Q6 | positioning | home-approach | client OK to publish (Question 4) |
| "don't need, or can't fund, a full-time lawyer on staff" | Q6 | positioning | home-approach | none |
| "Open to fixed fee and subscription arrangements" + one-line definitions | Q11 | conditional | home-fees, pa-fractional | definitions confirmed (Question 11) |
| Every Q9 practice item | Q9 | factual | practice page | none |
| "Employment claims and real estate disputes, from early resolution through litigation." | Q9 (heading + his listed employment claims and real estate disputes) | conditional | pa-disputes | scope confirmed (Question 12) |
| "based in New Jersey and New York and take clients from anywhere" | Q4 | factual | home-approach | none |
| "Messages go straight to me." | Q24 (his own email/number, solo) | factual | contact bands | none |
| Pull quote (Q2, edited for person/tense) | Q2 | his words | home-matt | edit approved (Question 13) |
| "AI-assisted business law" / "An AI-based firm with flexible fees" / "I run ATLAS LAW as an AI-based firm." / "AI-assisted. I do the legal work." | U1 | positioning | home-hero, home-fees, about-bio, about-background | none; always beside the "I do the legal work" line |
| "AI tools make the work more efficient." / "AI tools help me work efficiently" | U1 | factual (process, no outcome) | home-fees, about-bio | none |
| "What you're paying for is my experience and my legal and business judgment, not my time." | U1, near-verbatim | positioning | home-fees | confirm it holds on every engagement (Question 16) |
| "The tools assist. I do the legal work, check what they produce and stand behind the advice." / "the legal work and the judgment calls stay with me" | Harry's compliance instruction 2026-10-13 + the lawyer's duties of competence and supervision | factual (about his practice) | home-fees, about-bio | client confirms the wording (Question 17) |
| "I'm open to alternative fee arrangements, including fixed fees and subscriptions, so you know the rate and can budget for it." | Q11 + U2 | conditional | home-fees | none |
| "Alternative fee arrangements, including fixed fees and subscriptions, are available for the other practice areas too." | Q11 + U2 | conditional | pa-fractional | none |
| NOT stated: "fewer billable hours", "lower rates", "greater client value", "bang for their buck", "insights … unlikely to get from traditional law firms", any saving, percentage or comparison with traditional firms, named AI tools, AI confidentiality safeguards | NJ RPC 7.1(a), 7.1(a)(3); NY Rule 7.1(a); Harry 2026-10-13 | rule | absent | — |
| Footer disclaimer + privacy text | none | assurance | footer | **attorney approval: launch blocker** (Question 9) |
| "sets no tracking cookies" | the build | factual | footer | stays true only without analytics at go-live |
| Compliance: no "specialist/specializes/certified/expert" | NJ RPC 7.4(a); NY Rule 7.1(c) (dossier) | rule | absent | — |
| Compliance: no comparisons, no "best/top/leading", Q6 reasoning unpublished | NJ RPC 7.1(a)(3) | rule | absent | — |
| Compliance: name + phone shown; no address | NY Rule 7.1(d) Cmt [10] (dossier, eff. June 1 2026) | rule | header/footer | — |
| Compliance: no "Attorney Advertising" label | NY former 7.1(f) eliminated June 1 2026 (dossier) | rule | absent | confirm NJ needs none (no ratings/awards shown, so the NJ approval disclaimer is N/A) |
| Compliance: no results, no reviews, no awards | Q22 blank; Opinion 49 N/A | rule | absent | — |
| NOT stated anywhere: "20+ years", prices, "free consultation", response times, titles, "General Counsel at [company]", OSL Retail Services | dossier confirm list | — | — | — |

## Interaction usefulness test (§3)

No custom interactions are planned (no slider, scroll scene, configurator or form). The scroll-scrub is decorative motion on one image, not an interaction, and the page reads identically without it.

## Questions for Harry (unclear or conflicting answers)

None of these blocks the build; the sheet uses the stated defaults.

1. **Kentucky blue = `#0033A0`** (University of Kentucky royal blue)? If he meant something lighter, it's a one-token change. Worth showing him the swatch.
2. **Name on the site:** we use "Matthew Atlas" for the formal name (heading, footer, schema) and "Matt" in buttons ("Email Matt"). OK, or "Matt Atlas" / "Matthew J. Atlas"?
3. **Text only, or call or text?** He wrote "text me". The site says "Text 917-213-4979" with tap-to-text links and no "Call" button.
4. **OK to publish the revenue band** ("around $50 million to $200 million in annual revenue")? It filters the wrong fit but could put off a $30MM company he'd happily take.
5. **Titles and rough years at each company** (optional). The bio names the four companies without roles until he gives them.
6. **Law school line:** the NY registry lists University of Virginia. Show it as "University of Virginia" (default), or "University of Virginia School of Law, J.D. [year]"? Undergrad?
7. **Admission years:** show "NY 2004" and the NJ year, or just the states (default)?
8. **Legal entity name** for the footer (e.g., "Atlas Law LLC" / "PLLC"), if any. Footer says "© 2026 ATLAS LAW" until then.
9. **Footer disclaimer and privacy text** are proposed, not his. He must approve or replace them before launch (launch blocker).
10. **LinkedIn URL** to link in the footer (Q7). Not linked until he gives it.
11. **Fee definitions:** "Fixed fee: one price for a defined piece of work, agreed before it starts" / "Subscription: for ongoing legal work rather than a single matter." (No billing period is stated; if he bills monthly, the sheet can say so then.) Does that match how he'd scope them?
12. **Disputes line:** "Employment claims and real estate disputes, from early resolution through litigation." Does he also handle contract or other commercial disputes? If so, it's a one-line addition.
13. **Pull quote** on Home is his Q2 sentence lightly edited: "This is what I'm doing now, and I'm available if you're looking for legal services." OK?
14. **Generated photos:** a warehouse aisle and an empty retail space as atmosphere. None is presented as his office or clients. OK with him?
15. **OSL Retail Services** (employer on his NY registration) stays off the site by default.
16. **"Not my time":** is every engagement fixed fee or subscription, or are some matters billed hourly? If any are hourly, the home line "What you're paying for is my experience and my legal and business judgment, not my time." needs the alternative in the softened list (#5).
17. **AI wording:** "The tools assist. I do the legal work, check what they produce and stand behind the advice." Does that describe how he works? Does he want to say anything about how client information is handled with AI tools?
18. **The softened/omitted list** above (10 items) needs his OK, especially "fewer billable hours", "lower rates" and "insights … traditional law firms", which are left off.

## Sheet review revisions (B1b round 1, 2026-10-12)

The critic returned 11 fixes; all applied in `build-sheet.md`, with voice-spec and this plan updated to match:

1. Home h1 gets its own size token (`--fs-h1-hero`, 52px max, normal width, `text-wrap:balance`) and a cols 1–8 column (portrait now cols 9–12), so it sets on 2 lines at 1440, with a step-down rule if it doesn't.
2. Credentials strip runs full width with `padding-top: overlap + 2.5rem`; figures shrink to 56px max, no-wrap.
3. About: the casual photo is removed from `about-bio`, which now starts below the hero portrait's overhang.
4. Mobile header fit specified (smaller wordmark, compact buttons, 44px icon menu with `aria-label`, a 332px budget) with a no-horizontal-scroll check at 360px.
5. Every Text button except the compact mobile header one reads "Text 917-213-4979".
6. "Monthly" removed from the fees band and the Subscription tile.
7. Home bento bottom row is now "dr dr dr re re re" (Q9 order).
8. `home-approach` heading is now "A legal and business advisor for your company" (his Q3 words); the body's "inside" became "at".
9. The "fairly casual … by text" line is cut.
10. The disputes line names only employment claims and real estate disputes.
11. The OG card is built from his real formal portrait plus the wordmark.

Non-blocking notes taken: the glass-tower plate is dropped (the fees band is a blue field; the scroll-scrub moved to the real estate image); the two blue employment cards have a stated reason (they're the two Q9 groups with nested items); a line on the Practice areas page says the fee options apply to every area; the casual headshot sits on white only; no extra wordmark or tracked-caps eyebrow was added.

## Client update 2026-10-13: placement

The update is controlling (same weight as `client-answers.md`). It was folded into the existing plan with no new section, no new family and no nav change, so composition quotas and plan-lint stay as they were (18 sections, 9 families).

- **Why the home band, not a new section:** the band already carried Q11's fee message, and his two points are one argument (AI-assisted work → you pay for judgment → fees you can plan around). One band carrying both, with two blocks side by side, highlights them more clearly than two thin sections, and it doesn't duplicate the fee message. It moves up one slot, from after the practice tiles to directly after `home-approach`, so the order reads: who he is → his background → how he works and bills → what he handles. The opener and family chain still alternate (editorial-column/bare-h2 → full-bleed-band/in-media → bento/side-label → split/none).
- **Why the hero eyebrow:** "clearly highlighted" means visible on the first screen. The eyebrow is the one hero slot that can change without adding a fifth hero text element or touching the h1.
- **Why not the nav:** a three-page site with a new "AI" or "Fees" page would be thin (he gave no tool, process or price detail), and Q29's Contact ban stands. No nav change.
- **Practice areas:** only the page-level fee line changes, to his term "alternative fee arrangements". The fixed-fee and subscription tiles stay as they are.
- **About:** one bio paragraph and one table row ("How I work"); the "Fees" row takes his term.

## Client update 2026-10-13: softened or omitted (for Harry to run by the client)

| # | His phrase | What the site does | Why | Compliant alternative if he wants more |
|---|---|---|---|---|
| 1 | "AI Based Law Firm" | Kept: "An AI-based firm with flexible fees" (home h2), "I run ATLAS LAW as an AI-based firm" (About). The hero eyebrow says "AI-assisted business law". Every mention sits beside "I do the legal work … and stand behind the advice." | Read alone, "AI-based law firm" could suggest that software provides the legal service (NY Rule 7.1(a) / NJ RPC 7.1(a): misleading). Harry's rule: AI assists him, he does the work. | Already compliant as placed. |
| 2 | "Using AI tools to provide legal services more efficiently" | Softened to "AI tools make the work more efficient." | "AI tools … provide legal services" makes the tool the provider. | "I use AI tools to do the work more efficiently." |
| 3 | "Allows for fewer billable hours" | Omitted | A savings claim with no baseline (fewer than what?): a cost expectation the site can't substantiate (NJ RPC 7.1(a); Harry: no promised savings). | "I use AI tools so routine tasks take less of my time." (process only; still confirm he's comfortable) |
| 4 | "and greater client value" | Omitted | Unverifiable comparative ("greater" than whom?). | Let the fee terms speak: "so you know the rate and can budget for it." |
| 5 | "Clients are paying for my experience and legal/business judgment, not my time." | Kept near-verbatim in body copy (not a heading: an "X, not Y" heading trips our copy gate) | Fine as positioning about how he works. **Only accurate if no engagement is billed by the hour.** | If some matters are hourly: "AI tools mean less of what you pay for is time; what you're paying for is my experience and judgment." |
| 6 | "I'm utilizing my experience on the client side to provide them insights that they are unlikely to get from traditional law firms." | Comparison omitted; the client-side point stays in `home-approach` ("so I understand the client side well") | A comparison with other lawyers stated as fact (NJ RPC 7.1(a)(3), NY Rule 7.1). | "My years on the client side shape the advice I give." |
| 7 | "Offering flexible fee arrangements that allow clients greater rate and budgeting predictability" | Softened to "I'm open to alternative fee arrangements, including fixed fees and subscriptions, so you know the rate and can budget for it." and "flexible fees" in the home h2 | "Greater" is comparative; predictability itself is a plain property of a fixed fee or subscription. | Already compliant as placed. |
| 8 | "because of the reliance on AI, and lower rates" | Omitted | "Lower rates" is a price comparison with no prices or baseline (Harry: no prices); tying it to AI implies a saving. | "Ask me about rates." (no figure) |
| 9 | "should provide clients would great value (bang for their buck)" | Omitted | An unverifiable value promise, and the idiom works against Q5's "not a hack". | None needed. |
| 10 | "Alternative Fee Arrangements and Subscriptions" | Kept verbatim as a term (home block B, practice-areas line, About "Fees" row) | Names the arrangement types, no prices. | — |

Context for Harry, not for the site: lawyers' AI use is the subject of ABA Formal Opinion 512 (2024), which covers competence, confidentiality and fees. If prospects ask how client information is protected when he uses AI tools, that's a line only he can write.

## Handoff notes

- Sheet: `build-sheet.md` (18 sections, 9 families, plan-lint exit 0). Voice: `voice-spec.md`. Comps: `directions/a.png` (pick), `b.png`, `c.png`.
- No VIDEO request. 2 GENERATE stills, $0.
