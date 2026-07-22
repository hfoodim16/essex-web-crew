# Website Plan — Happy Trees by MGM Tree Service LLC (`happy-trees-by-mgm`)

**Planner:** Essex Web Crew planner (Fable) · **Date:** 2026-07-22
**Pipeline:** web-design-ultra Stages 1–5 complete. This plan is the design contract — the Builder implements it exactly and re-decides nothing.

---

## 1. Art direction — "Canopy Height"

A working-at-height direction for an ISA-accredited arborist: the story is told from up in the tree, where Marvin actually works. Bark-dark grounding, warm daylight cream, a pale sky blue — and the accent is **hi-vis chartreuse**, the literal color of an arborist's helmet and saw chaps. The homepage reads as a descent: hero at canopy height, scrolling down through the services to the ground and the contact form, stitched together by a climbing-rope motif. Certified, physical, unmistakably the real trade — not clip-art landscaping green.

**Personality words:** certified, dependable, local.

## 2. Typography

- **Display:** **Zilla Slab** (SemiBold 600 / Bold 700) — a sturdy, engineered slab serif with timber weight; headlines, section titles, big stats. Italic Bold for the occasional emphasis word.
- **Body:** **Work Sans** (400/500) — clean, warm, hard-working grotesque; paragraphs, nav, forms, captions.

Google Fonts both. Never Inter/Roboto/Arial/Helvetica (and no Roboto Slab).

## 3. Color system (`:root` tokens)

| Token | Hex | Role |
|---|---|---|
| `--bark` | `#251E16` | Deep bark brown-black — headline text, footer/hero-scrim base, dark bands |
| `--daylight` | `#F5F0E5` | Warm daylight cream — page background |
| `--sky` | `#9CC0DE` | Pale sky blue — secondary surfaces, canopy-gradient tops, info chips |
| `--moss` | `#55663F` | Muted moss — secondary text, hairlines, icon strokes |
| `--hivis` | `#C9E23F` | Hi-vis chartreuse — CTAs, rope motif, active states, focus ring |

Palette family: **bark + sky + hi-vis chartreuse (working-at-height natural)** — explicitly NOT dark-luxury evergreen, NOT light meadow-green daybreak, NOT parchment+pine (all banned families). CTA buttons: hivis fill, bark text (high contrast).

**Color-convention call:** the tree/eco convention is green + earth + sky (nature, growth, responsibility) — and Stage 3 shows the genre saturated with the same bright landscaping green. This direction **breaks the generic-green convention on purpose**: the greens here are safety-gear chartreuse and muted moss, anchored by bark and sky — differentiated in a samey category while staying unmistakably arboreal. Trust cues kept from the category: natural bark/sky tones, and the ISA/license credential strip front and center (the credibility work the color no longer has to do alone).

## 4. Page map (4 pages: `index.html`, `services.html`, `about.html`, `contact.html`)

Every page: header with the **real Happy Trees logo top-left** (download `https://happytreesnow.com/wp-content/themes/happytrees/images/logo.png` — dossier Logo line; fetch with a browser User-Agent + referer, the server 406s bare hotlinks; fallback copy at `https://happytreesnow.com/wp-content/uploads/2019/04/logo-happy-trees.png`; never redraw), nav, main `tel:` call button; mobile adds a persistent bottom-of-header call bar with BOTH numbers labeled: Main (973) 338-0506 · 24-hr Emergency (973) 641-3396.

### Home (`index.html`) — the "descent" page
1. **Hero — canopy height** — full-bleed photo of an arborist roped high in a hardwood (GENERATE slot 1), sky-to-bark gradient scrim; headline + sub + CTA "Get a free estimate" + `tel:` button. ISA badge-line under the headline: "ISA-Accredited Arborist · NJTC Registration # NJTC 768421 · Licensed & Insured."
2. **Trust strip** — `SINCE 2003` · `ISA-ACCREDITED` · `NJTC # 768421` · `FULLY LICENSED & INSURED` · `FREE ESTIMATES` (all real, from their site).
3. **Rope descent begins** — a vertical hi-vis rope line (SVG) runs down the left gutter connecting sections 3–6.
4. **Services overview** — four cards: Tree Removal & Stumps / Tree Care & Pruning / 24-Hr Emergency Storm / Extras (holiday lighting · free wood chips · permits). Each links to `services.html`.
5. **"We handle your permit" band** — the real differentiator, sold plainly: many Essex County towns require a permit to remove a tree — Happy Trees files it for you. (Bark band, hivis rule.)
6. **Service-area block** — "Serving Bloomfield, Montclair, Nutley and surrounding Essex County" (site-authoritative phrasing per dossier).
7. **Neighbor quote** — *"I had very pleasant & reliable service from Happy Trees and he lives in Bloomfield."* — R. U., Bloomfield, NJ · via Nextdoor.
8. **Estimate CTA band** — "Get a free estimate" + both phone numbers; note the real promo verbatim: "5% off Any Tree Service over $500.00 — first-time customers; senior discounts available."
9. **Footer** — NAP: Happy Trees by MGM Tree Service LLC · 57 Morley Ln, Bloomfield, NJ 07003 · (973) 338-0506 · marvin@happytreesbymgm.com. Hours: `[Hours — confirm with Marvin]` visible placeholder (loc8nearme's hours are `[verify]`). NAP matches JSON-LD exactly.

### Services (`services.html`)
1. Typographic hero: "High Quality Service at Reasonable Prices." (their verbatim tagline).
2. **Tree Removal & Stumps** — full removal, stump removal/grinding. Image slot 3 (PLACEHOLDER — stump grinding).
3. **Tree Care & Pruning** — trimming, thinning, shaping, elevation, cabling, maintenance (verbatim service list). Image slot 2 (GENERATE — finished shaped tree over a nice home).
4. **Emergency & Storm** — 24-hour response, emergency line huge and tappable: (973) 641-3396.
5. **Extras** — holiday lighting · free wood chip delivery to residents and businesses · municipal permit handling. Image slot 4 (PLACEHOLDER — chipper crew).
6. CTA band + footer. (No crane/bucket-truck claims — `[verify]`, directories only.)

### About (`about.html`)
1. **Marvin's story** — founded 2003 by Marvin Monge, "a 20-year veteran of the tree service industry" (verbatim), ISA-accredited arborist. Image slot 5 (PLACEHOLDER — crew by unbranded truck).
2. **Credentials block** — ISA accreditation · NJTC Registration # NJTC 768421 · fully licensed & insured · workers' compensation included (all verbatim site facts). Angie's List Super Service Award 2016 badge (labeled placeholder block for the real badge asset).
3. **Reviews** — both named Nextdoor quotes (R. U. above + *"Happy Trees in Bloomfield....have used them several times"* — L. T., Cedar Grove, NJ · via Nextdoor). Optional third slot: a labeled placeholder `[Named review from live Yelp/Angi page — Builder confirms name or omits]`.
4. **Service-area map-style town list.**
5. Footer.

### Contact / Get a Quote (`contact.html`)
1. **Quote-first hero** — "Get a free estimate." Both numbers as big `tel:` buttons (Main / 24-hr Emergency) + email link (real: marvin@happytreesbymgm.com).
2. **Estimate form embed placeholder** — ≤4 fields: name / phone / town / what does the tree need. `<!-- EMBED: estimate form service goes here -->`. Promo line repeated beneath (verbatim 5%-off note).
3. **Map embed placeholder** — `<!-- EMBED: Google Map — 57 Morley Ln, Bloomfield, NJ 07003 -->`.
4. Footer.

## 5. Hero direction

- **Headline concept:** **"Certified up here. Trusted down there."** — the ISA credential + neighbor reputation in one line. (Fallback if the Critic finds it too clever: "The ISA-accredited arborist your neighbors call." — keep ONE, plain.)
- **Sub-copy angle:** tree removal, pruning and 24-hour storm response in Bloomfield, Montclair & Nutley — since 2003, licensed NJTC # 768421, free estimates.
- **Hero image intent:** the roped arborist aloft (slot 1) — skilled, real, casually flattering; sky at top for the headline.

## 6. Layout archetype + motion + background

- **Layout archetype: immersive canopy-descent scroll.** Home is a vertical narrative (sky → canopy → work → ground → contact) stitched by the hi-vis rope line in the left gutter; interior pages use the same grid without the full narrative. Asymmetric text blocks, big slab stats, cards that overlap section seams (negative-margin straddle). NOT a service-index SPA, NOT a family-friendly bright stack, NOT ledger/archival (all banned or used this run).
- **Background system:** layered **sky-gradient tops** on sections (daylight cream → pale sky radial at low alpha) + a **drifting dappled canopy-light overlay** (2 blurred radial-gradient "leaf-shadow" layers, `mix-blend-mode: multiply` at low opacity, drifting on 26s/38s alternate transforms — the fog recipe re-tinted as light-through-leaves) + SVG grain (0.04) + the hi-vis rope SVG motif. NOT flat-dark+diagonal, NOT light-paper tokens, NOT parchment rules (banned systems).
- **Motion character: smooth-editorial atmospheric.** Scroll reveals that stagger downward (the descent), the rope line draws in with scroll progress (stroke-dashoffset), dapple layers drift slowly, service cards lift softly on hover. No cursor replacement, no counters (auto shop owns that vocabulary this run). All gated behind `prefers-reduced-motion` (dapple freezes to a static frame; rope renders fully drawn).
- **Atmosphere budget:** dapple drift (counts as the one atmospheric effect; ≤2 layers, blur ≤18px, `will-change: transform`) + grain. Nothing else.

## 7. Stage 5 — three divergent directions + the pick

Banned combos avoided (design-memory last 3): fonts Marcellus/Mulish, Bricolage/Nunito Sans, Fraunces/Karla; palettes dark-luxury-evergreen+brass, light-daybreak-meadow-green, warm-heritage-parchment+pine; layouts dark-editorial/service-index SPA, bright-family stack, ledger/archival; backgrounds flat-dark+diagonal, light-paper, parchment+rules. Extra care taken because all three banned palettes contain greens — this palette's greens (hi-vis chartreuse, muted moss) belong to none of those families. Also diverges from this run's other two prospects (CPA = light serif letterhead; auto = graphite industrial stack).

- **Direction A — "Arbor Green Classic."** Concept: the trustworthy tree company done cleanly. Layout: hero + card stack; Type: Poppins/Open Sans (engine suggestion); Palette: forest green + white + amber (*honors* the eco-green convention). Rejected: it's the saturated genre default Stage 3 documented on every competitor, the engine fonts are generic, and forest-green risks reading as the banned evergreen/pine families.
- **Direction B — "Canopy Height" (PICKED).** Concept: the trade seen from where the arborist actually works — height, rope, safety gear, sky. Layout: immersive canopy-descent scroll + rope motif; Type: Zilla Slab / Work Sans; Palette: bark + daylight + sky + moss + hi-vis chartreuse (*breaks* generic green deliberately, keeps natural trust cues + credential strip); Background: sky gradients + drifting canopy dapple + grain; Motion: smooth-editorial descent. *Bold because:* nothing in the Stage 3 tree-service genre looks at the work from height, and hi-vis chartreuse as brand accent is both striking and literally true to the trade.
- **Direction C — "Storm Watch."** Concept: dark dramatic emergency-first — near-black, storm slate, warning amber, lightning imagery. *Breaks* convention hard toward urgency. Rejected: leads with fear when the dossier says the reputation is warmth/reliability; a dark moody treatment also brushes the banned dark-luxury family and collides with the auto shop's dark direction this run.

**Pick: B.** The boldest option that stays true to a friendly, ISA-certified owner-operator — differentiated in a same-y category without costume or fear.

## 8. Image list (exactly 2 GENERATE; register locked once: **proud-contractor** — flawless finished work / skilled real crew, attractive properties, casual flattering natural light, never editorial)

| # | Slot | Status | Spec |
|---|---|---|---|
| 1 | Home hero — arborist aloft | **GENERATE** | `16:9`, **2K** (full-bleed background hero, gradient scrim) |
| 2 | Services — finished shaped tree | **GENERATE** | `4:3`, **1K** (contained section plate; DIFFERENT property style from any house visible in slot 1) |
| 3 | Services — stump grinding | PLACEHOLDER | labeled AI-IMAGE box: "freshly ground stump with tidy cleanup, raked lawn, residential yard" |
| 4 | Services — chipper crew | PLACEHOLDER | labeled AI-IMAGE box: "ground crew feeding brush into a chipper on a tidy residential street, clean site" |
| 5 | About — crew by truck | PLACEHOLDER | labeled AI-IMAGE box: "crew beside an unbranded bucket truck on a leafy Bloomfield street" |
| 6 | OG image | derived | crop of slot 1 to 1200×630 (no extra generation) |

**Slot 1 generation prompt (hero, 16:9, 2K):**
> A photograph of a professional arborist secured with climbing ropes and harness high in the crown of a large mature oak tree, mid-prune with a small handsaw, wearing a hi-vis helmet and chaps, taken with a phone from the ground looking up at a gentle angle, good consumer-camera quality, level honest framing, bright clear day with soft morning sun through the leaves, leafy suburban New Jersey backyard below with a well-kept lawn, open sky in the upper portion of the frame for a headline, skilled and confident body position, clean professional gear, subtle grain, natural imperfections, uneven foliage textures, no phone UI, no on-screen icons, no status bar, no timestamp overlay, no screen chrome, no branding, no lettering on gear or vehicles, no signage, no logos, no readable text, no illustration, no 3D render, no CGI, no painting, no oversaturation, no plastic or waxy textures, no perfect symmetry, no watermark

**Slot 2 generation prompt (finished job, 4:3, 1K — distinct property):**
> A photograph of a beautifully shaped mature maple tree with a freshly pruned, balanced crown standing over the front yard of an attractive white farmhouse-style home with black shutters and a stone walkway, taken with a phone from the sidewalk, good consumer-camera quality, straight-on level framing, warm late-afternoon light, healthy green lawn with clean bed edges, no branches or debris anywhere, quiet suburban street with a mailbox and driveway visible, subtle grain, natural imperfections, uneven textures, no phone UI, no on-screen icons, no status bar, no timestamp overlay, no screen chrome, no branding, no signage, no lettering, no logos, no readable text, no illustration, no 3D render, no CGI, no painting, no oversaturation, no plastic or waxy textures, no perfect symmetry, no watermark, no people

Both optimize to WebP, downscaled to display width. One register site-wide; placeholders styled on `--daylight` with `--moss` labels and a hivis corner tick.

## 9. Embed placeholders

- **Estimate form** (contact.html): 4 fields (name / phone / town / what the tree needs) + `<!-- EMBED: estimate form -->`.
- **Google Map** (contact.html): `<!-- EMBED: Google Map — 57 Morley Ln, Bloomfield, NJ 07003 -->`.
- **Award badge** (about.html): labeled placeholder for the real Angie's List Super Service Award 2016 badge asset — never redraw or fake it.

## 10. Content honesty notes (Builder must respect)

- **Service area:** lead with the site's own three towns ("Bloomfield, Montclair and Nutley") + "and surrounding Essex County." Don't promote Clifton/Cedar Grove to named service towns.
- **Hours:** `[verify]` — loc8nearme lists Mon–Fri 9–4, Sat 9–2, but the site doesn't; ship a visible `[Hours — confirm with Marvin]` placeholder and `PLACEHOLDER_…` JSON-LD tokens.
- **Crane / bucket-truck services:** directories only — `[verify]`; do NOT list them (the slot-5 placeholder's "bucket truck" is scenery, not a service claim — if the Critic objects, swap to "chip truck").
- **Nextdoor Neighborhood Favorite 2021/2023:** `[verify]` — omit from the mockup.
- **Business name:** brand as **"Happy Trees by MGM"** (the site's own form), full LLC name in footer/JSON-LD; never the "& Landscaping" variant.
- **Promo:** use the 5%-off copy verbatim including its conditions (over $500, first-time customers).
- **Ratings:** if shown, platform-labeled only (e.g. "4.9★ on Angi") — never averaged.

## 11. Real reviews plan

Two named Nextdoor quotes are the safe testimonials (R. U. — Bloomfield; L. T. — Cedar Grove): home gets one, About gets both. The two anonymous loc8nearme quotes are NOT used unless the Builder confirms a named source on the live Yelp/Angi page; otherwise the About third slot ships as the labeled placeholder specified above. Never invent a reviewer.

## 12. Local-trade conversion patterns (house standard)

- **Tap-to-call:** `tel:+19733380506` (main) in the header everywhere; emergency `tel:+19736413396` prominent in header sub-bar, Emergency section, and footer.
- **One plain CTA:** "Get a free estimate" (primary) with call buttons alongside — repeated hero / mid / footer.
- **Service-area block** with the three real towns + Essex County phrasing.
- **Trust strip:** since 2003 / ISA-accredited / NJTC # 768421 / licensed & insured / free estimates — all real site facts.
- **Work gallery:** slots 2–4 form the project imagery (1 real generated + 2 labeled placeholders for Marvin's real job photos) — satisfies the gallery pattern honestly.
- **Form ≤4 fields.**
- **NAP footer** identical on all pages and to JSON-LD: `Happy Trees by MGM Tree Service LLC · 57 Morley Ln, Bloomfield, NJ 07003 · (973) 338-0506`.
- **Local SEO:** JSON-LD `@type: "HomeAndConstructionBusiness"` (no tree-service subtype exists; do not misuse another subtype); `<title>`: "Tree Removal & Tree Service in Bloomfield, NJ | Happy Trees by MGM"; meta description naming tree removal/pruning + Bloomfield/Montclair/Nutley; OG/Twitter with hero; canonical; inline SVG favicon (rope-loop tree glyph in hivis on bark); one `<h1>` per page with service + town. Unknown values stay `PLACEHOLDER_…`.
