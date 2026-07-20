# Website Plan — Anthony's Landscaping

**Slug:** `anthonys-landscaping` · **Planner:** Fable · **Date:** 2026-07-19
**Source of truth:** `prospects/anthonys-landscaping/dossier.md` — reuse the site's REAL
captured copy (verbatim lines below); do not rewrite the business.

---

## 1. Art direction — "Evening Estate"

A dark, refined design-build direction: deep forest-charcoal ground, ivory type, bluestone
gray, and a restrained brass accent — the mood of a finished SOMA backyard at dusk with
the landscape lighting just switched on. Anthony's is a 30-year firm whose `.gif`-era site
looks cheaper than its patios; the fix is quiet luxury that lets big project imagery and
generous dark space do the talking. This is the upscale pole of our three prospects —
noticeably more formal than Gee-Kay's warm parchment or Duran's daylight friendliness.

Signature moves:
- Dark theme throughout (the only dark site of the three) with ivory serif-caps headings.
- A thin brass keyline frame around hero and section images — "gallery-hung" projects.
- Full-bleed image bands between text sections so the portfolio carries the pitch.
- Numbered service-line index (01 Design & Build / 02 Hardscape & Masonry / 03 Lawn
  Maintenance) used in nav-adjacent contexts and page headers — architectural-studio feel.

## 2. Typography

Google Fonts, display=swap:

- **Display: Marcellus** (single weight 400 — that's the design: inscription-style Roman
  caps). All h1–h3, page numbers ("02"), nav wordmark "ANTHONY'S LANDSCAPING", stat
  figures. Set h1/h2 in all-caps with letter-spacing 0.04em; never bold-faked.
- **Body: Mulish** (weights 300, 400, 600, 700). Body copy, nav links, buttons, captions,
  form labels. A precise, low-contrast sans that reads crisp on dark backgrounds; 600 for
  buttons/labels, 300 for large intro paragraphs.

Scale: body 17px/1.7 (Mulish 400 at 300-weight for lede paragraphs); h1
clamp(2.4rem, 5.5vw, 4rem) caps; h2 clamp(1.8rem, 3vw, 2.5rem) caps; eyebrow labels
Mulish 700 uppercase 0.75rem letter-spacing 0.18em in brass.

## 3. Color system

`:root` tokens (5):

| Token | Hex | Role |
|---|---|---|
| `--evergreen` | `#101B14` | Page background |
| `--moss-panel` | `#1A2A1F` | Cards, alternate section bands, form fields |
| `--ivory` | `#F1EDE2` | Headings + body text |
| `--bluestone` | `#8DA1A6` | Secondary text, captions, hairlines (nod to their bluestone walks) |
| `--brass` | `#C1985C` | Accent: eyebrows, keylines, button fill (with `--evergreen` text), link hover |

Usage rules: ivory-on-evergreen for all reading text (AA-safe); bluestone only for
captions/metadata ≥14px; brass never for paragraph text; buttons are brass fill with
evergreen text (primary) or ivory outline (secondary). Placeholders (`.img-placeholder`)
fill `--moss-panel` with a 1px brass keyline. No other hex anywhere.

## 4. Page map — 5 pages (single-file SPA, `data-page` nav per house recipe)

Sections: `page-home`, `page-design-build`, `page-hardscape`, `page-maintenance`,
`page-about`. Nav: Home · Design & Build · Hardscape & Masonry · Lawn Maintenance ·
About & Contact + brass button "Free Estimate" → About & Contact. (Complimentary
estimates are dossier-verbatim.)

### Page 1 — Home (`page-home`)
1. **Hero** — see §5.
2. **Philosophy line** — their verbatim sentence set large in Marcellus, centered, brass
   rules above/below: "Our philosophy is to provide all of our customers with outstanding
   professional service and complete satisfaction."
3. **Service-line index** — three numbered panels (01/02/03) with AI-IMAGE, caps title,
   one-line summary, "Explore →" to each service page.
4. **Craft & trust band** — split layout: left, the verbatim about line ("We take pride
   in our reputation for quality, experience, workmanship, and professional integrity.
   From start to finish we are there every step of the way."); right, stat column:
   "Founded over 30 years ago" · "South Orange / Maplewood" · "Complimentary estimates".
5. **Project gallery strip** — horizontal row of 4 keylined AI-IMAGEs (patio+firepit,
   walkway, pool surround, lighting at dusk) with bluestone captions — the proof their
   old site never shows.
6. **CTA band** — "Thirty years of SOMA backyards. See what yours could be." + Free
   Estimate button + phone (973) 763-6566.

### Page 2 — Design & Build (`page-design-build`)
1. **Page header** — "01 — DESIGN & BUILD", lede from their verbatim design blurb: work
   closely with you to "envision and develop a unique landscape design solution that will
   add value, functionality, and beauty to your home."
2. **Capability grid** — real service names from their site, grouped (verbatim items):
   Landscape Design · Grading · Plantings · Drainage · Waterproofing · Mulching · Low
   Voltage Lighting · Fences · Play Areas (RR Tie Borders with Play Chips).
3. **Feature split** — AI-IMAGE (planted landscape) + ~70 words on the design-to-build
   process (write from the blurb; invent no process steps beyond "design → build").
4. **Secondary feature** — drainage/grading credibility block (they explicitly list
   drainage, grading, waterproofing) with AI-IMAGE.
5. **Mini-CTA** — Free Estimate band.

### Page 3 — Hardscape & Masonry (`page-hardscape`)
1. **Page header** — "02 — HARDSCAPE & MASONRY".
2. **Signature projects grid** — 2×3 keylined cards, all verbatim service names:
   Patios · Walkways (Paver, Blue Stone, Concrete) · Retaining Walls · Fire Pits ·
   Custom Built-In BBQ's · Belgium Block Curbing. Each card: AI-IMAGE + caps title +
   one factual line.
3. **Driveways & curbing band** — full-width: Asphalt Driveways · Street Sidewalks &
   Curbing (verbatim), AI-IMAGE background with dark overlay.
4. **Mini-CTA**.

### Page 4 — Lawn Maintenance (`page-maintenance`)
1. **Page header** — "03 — LAWN MAINTENANCE", lede from their verbatim maintenance
   blurb: a "'cut above the rest' by ensuring a completely manicured lawn, meticulously
   pruned plant material, and healthy turf areas."
2. **Program list** — two columns, verbatim items: Weekly Lawn Service · Ornamental
   Pruning · Shrub Pruning · Small Tree Pruning · Spring Clean Up · Fall Clean Up · Turf
   Care Lawn Spraying Program · Fall & Spring Lawn Aeration and Seeding · Gutter Cleaning.
3. **Seasonal rhythm strip** — four small blocks (Spring / Summer / Fall / Year-round)
   mapping the real items above to seasons — organization only, no new services.
4. **Mini-CTA**.

### Page 5 — About & Contact (`page-about`)
1. **Page header** — "THE FIRM".
2. **Story** — ~100 words strictly from dossier: founded over 30 years ago by Anthony
   Molinaro; reputation for quality, experience, workmanship, professional integrity;
   serving South Orange / Maplewood and surrounding Essex County. **Do not name a
   current owner** (see §9).
3. **Values row** — three brass-keylined tiles quoting their own words: Quality ·
   Workmanship · "There every step of the way".
4. **Contact split** — left: phone (973) 763-6566, address 175 Church St, South Orange,
   NJ 07079, "Complimentary estimates", hours `[Hours — placeholder]`; right: form embed
   placeholder (§8).
5. **Map** — embed placeholder.
6. **Footer** (global) — evergreen, wordmark, numbered nav, phone, address; no owner name.

## 5. Hero direction

- **Headline (caps, Marcellus):** "OUTDOOR SPACES BUILT TO OUTLAST TRENDS."
  Sub-eyebrow above it in brass: "SOUTH ORANGE · DESIGN-BUILD LANDSCAPING · EST. 30+ YEARS".
- **Sub-copy:** one line from their real positioning: "Design, construction, hardscape
  and full-property care — with outstanding professional service and complete
  satisfaction, from start to finish."
- **CTAs:** brass "Request a complimentary estimate" + outline "View our work" (anchors
  to gallery strip).
- **Hero image intent:** full-viewport AI-IMAGE of a finished patio + plantings at dusk
  with landscape lighting, dark gradient overlay bottom-up so ivory text sits on the
  darkest zone; thin brass frame inset 24px on desktop.

## 6. Motion notes (ALL reduced-motion-gated; cursor/tilt disabled on pointer:coarse)

- Reveal-on-scroll: images unmask with a clip-path wipe (bottom-up, 700ms); text fades up
  20px, 500ms; stagger 80ms.
- Brass keylines draw in (border via scaleX/scaleY transforms) as frames reveal.
- Subtle 3D tilt (max 3°) on the numbered service-index panels and gallery cards — fits
  the "gallery" concept; disable on touch.
- Magnetic effect on the two hero CTAs and the nav Free Estimate button.
- Custom cursor: ivory dot + brass lerped ring; label "View" over gallery/cards,
  "Estimate" over CTA buttons.
- Nav background fades from transparent to `--evergreen` on scroll.

## 7. AI-IMAGE placeholder list

All placeholders `--moss-panel` fill, 1px brass keyline, bluestone label text.

| # | Slot | Generation prompt for Harry |
|---|---|---|
| 1 | Home hero | "Luxury suburban backyard at dusk: bluestone patio with built-in fire pit, layered plantings, warm low-voltage landscape lighting glowing, deep blue-hour sky, high-end residential New Jersey, no people" |
| 2 | Index 01 — Design & Build | "Landscape architect's completed design come to life: freshly planted layered garden beds with ornamental grasses and boxwood beside a modern colonial home, late afternoon" |
| 3 | Index 02 — Hardscape | "Close low-angle shot of a natural bluestone paver patio with tight joints, sitting wall in matching stone, dusk light" |
| 4 | Index 03 — Maintenance | "Immaculately striped dark-green lawn with meticulously pruned shrubs along a walkway, upscale residential property, morning light" |
| 5 | Gallery — patio + firepit | "Circular stone fire pit at the center of a paver patio, four Adirondack chairs, evening glow, landscaped borders" |
| 6 | Gallery — walkway | "Curved bluestone walkway with Belgium block edging through a manicured front yard, golden hour" |
| 7 | Gallery — pool surround | "Backyard in-ground pool with stone coping and paver surround, landscaped privacy plantings, twilight, pool lights on" |
| 8 | Gallery — lighting | "Warm low-voltage landscape lighting washing up mature trees and a stone retaining wall at night, deep shadows, luxury ambiance" |
| 9 | D&B feature — plantings | "Crew-planted new landscape bed: balled shrubs going into fresh dark mulch beside string lines and a grading rake, work in progress, no faces" |
| 10 | D&B secondary — drainage/grading | "Freshly regraded side yard with new sod meeting a gravel French-drain channel along a foundation, clean and orderly, daylight" |
| 11 | Hardscape band — driveway | "Freshly paved black asphalt driveway with Belgium block granite curbing, colonial home, crisp edges, late afternoon shadows" |
| 12 | Hardscape card — retaining wall | "Tiered natural stone retaining walls holding planted terraces on a sloped suburban yard, golden hour" |
| 13 | Hardscape card — built-in BBQ | "Custom built-in outdoor BBQ island in stone veneer with stainless grill, on a paver patio, dusk" |
| 14 | Maintenance — manicured lawn | "Perfect diagonal mow stripes on a lush lawn, sharply edged beds, hedges squared, upscale home, midday" |

## 8. Embed placeholders

- **Contact form** (About & Contact): moss-panel block with brass keyline, static field
  labels (Name / Phone / Email / Tell us about your project) + brass button; comment:
  `<!-- EMBED: contact form service goes here (replaces old contact.php form) -->`.
- **Google Map**: placeholder block "Map — 175 Church St, South Orange NJ"; comment:
  `<!-- EMBED: Google Maps iframe, 175 Church St, South Orange, NJ 07079 -->`.
- No booking widget.

## 9. Content honesty notes (Builder: write around these)

- **OWNERSHIP — the big one.** The old site's About page referenced a possible 2025
  ownership transition ("Chike Achebe"); every other source shows Anthony Molinaro as
  founder/owner. **Do not name a current owner anywhere.** "Founded by Anthony Molinaro
  over 30 years ago" is the only safe formulation (founder ≠ current-owner claim). No
  owner photo slot, no "meet the owner" section. Footer and About stay owner-neutral.
- **"30+ years"** — dossier-backed phrasing is "over 30 years ago"; never a specific
  founding year (none exists).
- **No reviews/ratings** — no aggregate rating or testimonials were captured. Do NOT
  build a testimonial section; the trust story is longevity + breadth + their own values
  copy. If the Builder wants a quote slot, it must be a labeled
  `[Testimonial — placeholder, collect from client]` block, clearly non-factual.
- **Verbatim copy is the voice** — the philosophy, about, design, and maintenance lines
  quoted in §4 are their real site copy; reuse them exactly (light punctuation cleanup
  ok). New connective copy must add zero new factual claims.
- **Hours, email, town list** — `[placeholder]`; only the phone, address, form, and
  "complimentary estimates" are verified contact facts.
- **Service names** — use their verbatim list; don't add services (no pools-construction
  claim — pools appear only as *project types showcased*, so the pool gallery image is
  fine, but never list "Pools" as a service).
