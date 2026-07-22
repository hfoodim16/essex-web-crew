# Website Plan — Cedar Grove Transmission & Auto Repair Inc (`cedar-grove-transmission`)

**Planner:** Essex Web Crew planner (Fable) · **Date:** 2026-07-22
**Pipeline:** web-design-ultra Stages 1–5 complete. This plan is the design contract — the Builder implements it exactly and re-decides nothing.

---

## 1. Art direction — "Signal & Steel (the honest garage)"

An industrial spec-sheet direction for a shop whose entire brand equity is *"Mike is fair and honest"* + 60 years under the hood. Dark graphite like a clean shop floor, bone-white type like stenciled part numbers, steel-blue secondary, and one accent: **trans-fluid red** — the exact red of fresh transmission fluid, the shop's flagship trade. Oversized condensed numerals carry the story (1961 · 60+ · 5★). It reads like a beautifully printed work order: nothing hidden, nothing dressed up, everything competent.

**Personality words:** honest, seasoned, dependable.

## 2. Typography

- **Display:** **Archivo** (Black 900, plus Expanded width at hero scale) — industrial, stenciled confidence for headlines, the giant numerals, and section titles. All-caps for eyebrows/labels with wide tracking.
- **Body:** **Barlow** (400/500/600) — utilitarian grotesque drawn from public-signage DNA; paragraphs, nav, cards, forms.

Google Fonts both. Never Inter/Roboto/Arial/Helvetica. (No mono third face here — that's the CPA site's voice; keep the two mockups distinct.)

## 3. Color system (`:root` tokens)

| Token | Hex | Role |
|---|---|---|
| `--graphite` | `#16181B` | Page background — dark shop-floor base |
| `--panel` | `#22262B` | Raised surface — cards, bento cells, form panel |
| `--bone` | `#EDEAE4` | Primary text + headline color |
| `--steel` | `#97A6B4` | Secondary text, hairlines, schematic linework |
| `--transred` | `#D8342C` | Single accent — CTAs, tel: buttons, active states, numeral highlights |

Palette family: **industrial graphite + steel + trans-fluid red**. NOT dark-luxury (no evergreen, no ivory, no brass — that family is banned); this is workshop-industrial, matte and utilitarian. CTA buttons: transred fill, bone text.

**Color-convention call:** the auto-repair convention is red/black/steel — energy, machinery, reliability (Stage 2/3 evidence: the genre leans navy/red trust colors; the engine's literal suggestion was an off-target wellness green, ignored as a bad hit). This direction **honors the convention** deliberately — a 60-year family shop should look like the best version of a garage, not a rebrand — but elevates it: matte graphite instead of black-gloss, one restrained red instead of checkered-flag clutter. Trust cue kept: BBB badge + real review wall.

## 4. Page map (4 pages: `index.html`, `services.html`, `about.html`, `contact.html`)

Every page: sticky header with **real CGT logo top-left** (download `https://static.wixstatic.com/media/ca6033_683b7d949b0f46929e5c0c52d241c97f~mv2.png` into `mockup/assets/` — dossier Logo line; it's a small square "CGT" badge, so pair it with an Archivo "CEDAR GROVE TRANSMISSION" wordmark beside it rather than enlarging or redrawing it), nav, and a transred `tel:` call button always visible (mobile: logo + hamburger + call button).

### Home (`index.html`)
1. **Hero** — full-bleed shop-bay photo (GENERATE slot 1) under a graphite scrim; headline + sub left-aligned over it; giant Archivo Expanded numeral "1961" ghosted at low opacity behind the headline. One plain CTA: **"Call the shop: (973) 239-1072"** + secondary "Get an estimate" → contact.
2. **Trust strip** — odometer-style count-up numerals: `SINCE 1961` · `60+ YEARS FAMILY OWNED` · `BBB ACCREDITED SINCE 2005` · `5★ ON CARFAX (28 REVIEWS)` (each stat platform-labeled, never averaged).
3. **Services bento grid** — 4 cells: Transmission (flagship, largest cell) / General Repair / Maintenance / Towing, each with 1-line honest copy + link.
4. **"Complimentary road test"** band — the site's own verbatim hook: "COMPLIMENTARY road testing to help analyze and diagnose the problems your vehicle may be having." Transred rule + big type.
5. **Review pull-quote** — *"Mike is fair and honest, GREAT SERVICE!!! and he does FANTASTIC WORK!!!"* — John R., Yelp (5★). Link "Read more on the About page."
6. **Service-area block** — "Serving Cedar Grove, Verona, Little Falls, Montclair, West Caldwell, Caldwell & Bloomfield."
7. **Marquee divider strip** — infinite-scroll service words (TRANSMISSIONS · BRAKES · A/C · DIAGNOSTICS · SUSPENSION · ALIGNMENT · TOWING), steel text on graphite.
8. **Estimate CTA band** + **footer** — NAP: Cedar Grove Transmissions & Auto Repair Inc. · 475 Pompton Ave., Cedar Grove, NJ 07009 · (973) 239-1072 · Mon–Fri 8am–5pm, Sat–Sun closed. (Suppress the Verizon email on the mockup design or show as plain contact line — do NOT feature it; part of the pitch is retiring it. Footer NAP matches JSON-LD exactly.)

### Services (`services.html`)
1. Typographic page hero: "For all your car care needs." (their verbatim tagline) with schematic-linework background.
2. **Transmission** — flagship section: repair + rebuilding; image slot 2 (GENERATE — rebuilt transmission on bench). Honest copy from dossier service list.
3. **General auto repair** — foreign & domestic; brakes, suspension, A/C, engine rebuilding, diagnostics, wheel alignment. Image slot 3 (PLACEHOLDER — diagnostics scan tool).
4. **Maintenance** — routine service + the complimentary road-test hook repeated.
5. **Towing** — short section, phone-first ("Broken down? Call…" `tel:`).
6. CTA band + footer.

### About (`about.html`)
1. **The 60-year story** — family owned & operated **since 1961** ("over 60 years" — site-authoritative figure), three generations of Cedar Grove drivers. Copy from dossier facts only; operator referred to as "Mike" exactly as reviews do (surname `[verify]` — never invent one).
2. **Meet the team** — the **real CGT team photo** (`https://static.wixstatic.com/media/ca6033_eedebec847504f94bba1e1c8c97fc803~mv2.jpg` → download to `mockup/assets/`; real beats generated — does not count against image cap).
3. **Review wall** — all 5 real reviews, each with name + platform + stars as captured (John R./Yelp, Cathy L./Yelp, Mark H./Yelp, Jessica Fedo/Google via Birdeye, Tim Gerds/Google via Birdeye). Panel cards on `--panel`.
4. **Accreditation** — BBB accredited since 2005 (badge placeholder block labeled "BBB seal — official asset"; do not fake the seal). No ASE claim (not attested).
5. Footer.

### Contact (`contact.html`)
1. **Phone-first hero** — big `tel:` button + hours (Mon–Fri 8am–5pm | Sat–Sun closed, verbatim).
2. **Estimate form embed placeholder** — ≤4 fields: name / phone / vehicle (year-make-model) / what's it doing. `<!-- EMBED: estimate form service goes here -->`.
3. **Map embed placeholder** — `<!-- EMBED: Google Map — 475 Pompton Ave., Cedar Grove, NJ 07009 -->`.
4. Footer.

## 5. Hero direction

- **Headline concept:** **"Fair. Honest. Since 1961."** — the review language and the founding year doing all the work.
- **Sub-copy angle:** family-owned transmission & full auto repair in Cedar Grove — complimentary road-test diagnosis, straight answers from Mike and the team.
- **Hero image intent:** a clean, competent working bay (slot 1) — real shop, flatteringly lit, never showroom.

## 6. Layout archetype + motion + background

- **Layout archetype: industrial spec-sheet stack + bento service grid.** Multi-page; oversized ghosted numerals as section anchors; asymmetric left-weighted text blocks; bento grid for services; full-width marquee divider. NOT a service-index SPA, NOT dark-editorial (banned archetype) — this is utilitarian-brutalist, print-workshop rhythm.
- **Background system:** graphite base + **exploded-gearbox schematic linework** (a custom inline SVG of gears/shafts in `--steel` at ~7% opacity, placed behind hero and section headers — the signature motif) + SVG grain overlay (0.05) + ONE steel-blue glow orb behind the services grid (blur 90px, opacity ~0.35). Explicitly NOT diagonal texture (banned system), NOT paper/parchment.
- **Motion character: kinetic-but-controlled.** Odometer count-up numerals in the trust strip (IntersectionObserver-triggered), the marquee strip (slow, pausable), snappy 150ms hover states on bento cells (lift + transred edge), reveal-on-scroll with a slightly mechanical stagger. No cursor replacement (wrong audience), no tilt. All gated behind `prefers-reduced-motion` (marquee stops, counters render final values).
- **Atmosphere budget:** grain + the single glow orb. Max 2; no fog/rays — wrong mood for a garage.

## 7. Stage 5 — three divergent directions + the pick

Banned combos avoided (design-memory last 3): fonts Marcellus/Mulish, Bricolage/Nunito Sans, Fraunces/Karla; palettes dark-luxury-evergreen+brass, light-daybreak-meadow, warm-heritage-parchment; layouts dark-editorial/service-index SPA, bright-family stack, ledger/archival; backgrounds flat-dark+diagonal, light-paper, parchment+rules. Also diverges from this run's other prospects (CPA = light sidebar-letterhead serif; tree = sky/canopy immersive scroll).

- **Direction A — "Daylight Bay."** Concept: bright, approachable neighborhood garage. Layout: light bento grid; Type: Work Sans/Karla-adjacent humanist; Palette: concrete grey + safety orange on white (*breaks* the dark-garage convention toward friendliness). Rejected: body face collides with banned Karla territory, and a light friendly stack sits too close to the banned bright-family-friendly archetype; also weakest expression of 60-year heritage.
- **Direction B — "Signal & Steel" (PICKED).** Concept: the honest garage as a beautifully printed work order. Layout: industrial spec-sheet stack + bento; Type: Archivo Black / Barlow; Palette: graphite + bone + steel + trans-fluid red (*honors* the auto convention, elevated); Background: gearbox schematic linework + grain + one orb; Motion: kinetic odometer numerals + marquee. *Bold because:* no local competitor (Stage 3: the genre is dated text-heavy pages or generic template navy) has typographic scale, schematic linework, or a real point of view — this looks like a shop that rebuilds gearboxes with pride.
- **Direction C — "Chrome Americana."** Concept: 1961 nostalgia — cream/turquoise retro-Americana, script accents, badge shapes. *Breaks* convention toward heritage-kitsch. Rejected: nostalgia reads "old-fashioned shop" not "shop that can service my 2024 CR-V"; risks costume over credibility, and warm-cream heritage territory brushes the banned warm-heritage family.

**Pick: B.** Boldest direction that strengthens (rather than costumes) the shop's actual equity: honesty, tenure, mechanical competence.

## 8. Image list (exactly 2 GENERATE; register locked once: **proud-contractor** — real working shop, flatteringly lit, never showroom or editorial)

| # | Slot | Status | Spec |
|---|---|---|---|
| 1 | Home hero — working bay | **GENERATE** | `16:9`, **2K** (full-bleed background hero, dark scrim over) |
| 2 | Services — rebuilt transmission | **GENERATE** | `4:3`, **1K** (contained section plate) |
| 3 | Services — diagnostics | PLACEHOLDER | labeled AI-IMAGE box: "mechanic running a scan tool at the driver's door, clean bay, natural light" |
| 4 | About/trust — shop exterior | PLACEHOLDER | labeled AI-IMAGE box: "tidy independent auto shop exterior on a suburban NJ avenue, morning light, unbranded signage" |
| 5 | About — team | **REAL ASSET** | the CGT team photo (download URL above; not generated, no cap impact) |
| 6 | OG image | derived | crop of slot 1 to 1200×630 (no extra generation) |

**Slot 1 generation prompt (hero, 16:9, 2K):**
> A photograph of the inside of a clean independent auto repair shop bay, taken with a phone, good consumer-camera quality, gently angled framing, level horizon: a silver sedan raised on a two-post lift, a mechanic in a plain dark work shirt inspecting the underside, organized tool chests and neatly hung tools along the wall, clean sealed concrete floor, bright even workshop lighting with some daylight from an open bay door, honest working atmosphere, muted graphite and steel tones with a hint of red from a tool chest, subtle grain, natural imperfections, uneven textures, dead space in the upper left for a headline, no phone UI, no on-screen icons, no status bar, no timestamp overlay, no screen chrome, no branding, no lettering on vehicles, no signage, no logos, no readable text anywhere, plain unmarked uniforms, no illustration, no 3D render, no CGI, no painting, no oversaturation, no plastic or waxy textures, no perfect symmetry, no watermark

**Slot 2 generation prompt (transmission, 4:3, 1K):**
> A photograph of a freshly rebuilt automatic transmission resting on a clean steel workbench in an auto shop, taken with a phone, good consumer-camera quality, straight-on slightly angled framing, level horizon, the aluminum casing clean and precise, a torque wrench and a few sockets neatly beside it, soft even workshop light with mild daylight from the side, honest and competent, muted graphite and steel tones, subtle grain, natural imperfections, uneven textures, no phone UI, no on-screen icons, no status bar, no timestamp overlay, no screen chrome, no branding, no lettering, no signage, no logos, no readable text, no illustration, no 3D render, no CGI, no painting, no oversaturation, no plastic or waxy textures, no perfect symmetry, no watermark, no people

Both optimize to WebP, downscaled to display width (hero full-bleed keeps 2K-derived width; slot 2 ≈ 800–1000px). One register site-wide; placeholders styled on `--panel` with `--steel` labels.

## 9. Embed placeholders

- **Estimate form** (contact.html): 4 fields (name / phone / vehicle / issue), styled placeholder + `<!-- EMBED: estimate form -->`.
- **Google Map** (contact.html): `<!-- EMBED: Google Map — 475 Pompton Ave., Cedar Grove, NJ 07009 -->`.
- **BBB seal** (about.html): labeled placeholder block — the official dynamic seal gets embedded post-sale; never fake the artwork.

## 10. Content honesty notes (Builder must respect)

- **Years:** site-authoritative phrasing only — "family owned & operated since 1961 · over 60 years." Never "65 years," never "over 50."
- **"Mike"** appears only as reviews name him; **no surname, no title** ("owner" unverified — say "Mike and the team").
- **Star ratings are platform-labeled, never averaged** (5★ CARFAX/28 · 4.5★ Yelp/30 · 4.8★ Birdeye — use at most two, always labeled).
- **No ASE certification claim** (not attested). BBB accredited since 2005 is real — use it.
- **Verizon email:** do not showcase `cgtrans316@verizon.net` as a design feature; a plain footer contact line at most.
- **Service-area towns** are dossier-suggested, not shop-published — phrase as "serving Cedar Grove and neighboring towns:" + list (the Critic knows the list is `[placeholder]`-grade; keep phrasing soft).
- Deeper service descriptions don't exist on their site — Builder writes short honest copy strictly from the dossier's service list, no invented specifics (no "certified technicians," no warranty claims).

## 11. Real reviews plan

Five real captured reviews (dossier "Real reviews") — review wall on About + one pull-quote on Home, all verbatim with name + platform as captured. The two Birdeye/Google full names (Jessica Fedo, Tim Gerds) may be shown as captured; Builder may shorten to first name + initial for consistency. Never edit quote text (keep the caps and exclamation points — they read real because they are).

## 12. Local-trade conversion patterns (house standard)

- **Tap-to-call** `tel:+19732391072` button in header on every page, mobile-persistent; repeated hero / mid / footer.
- **One plain CTA:** "Call the shop: (973) 239-1072" (primary) + "Get an estimate" (secondary, form).
- **Service-area block** with real town names (soft phrasing per honesty note).
- **Trust strip:** since 1961 / 60+ years / BBB since 2005 / platform-labeled rating — all real.
- **Gallery:** no before/after gallery page (their photos live on the Wix "Media" page we're not scraping) — the services imagery + team photo carry proof; documented exception for the Critic.
- **Form ≤4 fields.**
- **NAP footer** identical on all pages and to JSON-LD: `Cedar Grove Transmissions & Auto Repair Inc. · 475 Pompton Ave., Cedar Grove, NJ 07009 · (973) 239-1072`.
- **Local SEO:** JSON-LD `@type: "AutoRepair"`; `<title>`: "Transmission Repair & Auto Repair in Cedar Grove, NJ | Cedar Grove Transmission"; meta description naming transmission repair + Cedar Grove/Verona/Montclair; OG/Twitter with hero; canonical; inline SVG favicon (gear glyph in transred on graphite); one `<h1>` per page with service + town; real hours in `openingHoursSpecification` (Mon–Fri 08:00–17:00). Unknown values stay `PLACEHOLDER_…`.
