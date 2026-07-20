# Website Plan — Duran & Son Landscaping

**Slug:** `duran-and-son-landscaping` · **Planner:** Fable · **Date:** 2026-07-19
**Source of truth:** `prospects/duran-and-son-landscaping/dossier.md`. Both of their
domains are dead — there is no site copy to port; copy is rebuilt honestly from the
captured listing/review facts only.

---

## 1. Art direction — "Sunday Morning Oasis"

A bright, warm, daylight direction: soft warm-white ground, meadow green, a clear
river-blue accent (their irrigation/water story), and rounded, organic shapes — the
feeling of stepping into your own finished backyard oasis on a Sunday morning. Duran &
Son's captured positioning is literally "create their dream outdoor oasis," and they're
the family-owned, homeowner-friendly firm of our three — so this site is the warm,
approachable pole: lighter than Anthony's dusk-luxury, more contemporary and sunnier than
Gee-Kay's heritage parchment.

Signature moves:
- Large soft-radius ("pebble") corners on cards and images — one consistent organic
  radius token, echoed everywhere.
- A gentle SVG wave divider between major sections (water/irrigation motif, used
  sparingly — 2–3 times per page max).
- The river-blue accent is reserved for water/light things (irrigation, lighting, links)
  so the palette tells the service story.
- A "family-owned · licensed & insured · work guaranteed" trust chip row styled as
  rounded badges — their captured values copy turned into UI.

## 2. Typography

Google Fonts, display=swap:

- **Display: Bricolage Grotesque** (weights 500, 700; condensed-ish, characterful).
  All h1–h3, stat numbers, nav wordmark, trust-chip labels. Friendly but confident —
  a family firm that builds serious retaining walls.
- **Body: Nunito Sans** (weights 400, 600, 800). Body copy, buttons, captions, forms.
  Rounded, open, extremely legible — matches the approachable-premium tone.

Scale: body 17px/1.65; h1 clamp(2.5rem, 6vw, 4.25rem) Bricolage 700; h2
clamp(1.9rem, 3.2vw, 2.6rem); eyebrows Nunito Sans 800 uppercase 0.78rem
letter-spacing 0.14em in `--river`.

## 3. Color system

`:root` tokens (5):

| Token | Hex | Role |
|---|---|---|
| `--daybreak` | `#F9F7F0` | Page background |
| `--evergreen-ink` | `#243329` | Text, footer background |
| `--meadow` | `#2E7A4B` | Primary: buttons, h1/h2 accents, icons |
| `--river` | `#2C7FA6` | Accent: eyebrows, links, irrigation/lighting UI, wave divider |
| `--cedar` | `#8A5A33` | Warm secondary: trust chips, hairlines, hover states |

Usage rules: evergreen-ink on daybreak for body (AA+); meadow-on-daybreak for headings
and primary buttons (white text on meadow); river only as accent/eyebrow/link color,
never long text; cedar decorative only. Surfaces/tints: Builder derives with
`color-mix(in srgb, var(--meadow) 8%, white)` (and the river equivalent for the
irrigation page band) — no additional raw hex anywhere. `.img-placeholder` = meadow 8%
tint fill, cedar 1px border, evergreen-ink label.

## 4. Page map — 4 pages (single-file SPA, `data-page` nav per house recipe)

Sections: `page-home`, `page-design-build`, `page-maintenance`, `page-irrigation`.
**About + Contact live at the bottom of Home** (planner's call vs. burying contact on
the irrigation page): nav links are Home · Design & Build · Maintenance · Irrigation &
Lighting · Contact — where "Contact" routes to `page-home` and scrolls to the
`#contact` section. Nav also carries a meadow button "Call (862) 252-7030".

### Page 1 — Home (`page-home`)
1. **Hero** — see §5.
2. **Trust chip row** — rounded badges from their captured values copy: "Family-owned" ·
   "Licensed & insured" · "All work guaranteed" · "25+ years". (See §9 — all four are
   dossier-captured listing copy; keep exact phrasing.)
3. **Services overview** — four pebble-corner cards: Landscape Design & Build /
   Grounds Maintenance / Irrigation / Outdoor Lighting — each AI-IMAGE, title,
   one-liner, link to its page (irrigation + lighting cards both link to
   `page-irrigation`).
4. **Oasis story band** — meadow-tint band, wave divider top: their near-verbatim
   positioning as the centerpiece: "For over 25 years, Duran & Son Landscaping has been
   the go-to choice for homeowners in Northern New Jersey looking to create their dream
   outdoor oasis." Supporting line: "design, build and maintain any type of landscape,
   from grounds maintenance to retaining walls."
5. **Testimonial spotlight** — single large quote card (this is their reputational
   crown jewel): "In a sea of vendors… Duran & Son stands out as world class." —
   attributed "Yelp review". One quote, given room; no invented others.
6. **Service area strip** — "Serving Northern New Jersey — Essex, Morris and Union
   counties" (verbatim), home base West Orange.
7. **About the family** (`#about`) — ~90 words from facts: family-owned, 25+ years,
   full design-build-maintain; `[placeholder: family story — collect from owner]`
   italic slot for texture. AI-IMAGE alongside.
8. **Contact** (`#contact`) — split: phone (862) 252-7030, address 118 S Valley Rd,
   West Orange, NJ 07052, hours `[Hours — placeholder]` + form embed placeholder (§8);
   map placeholder below, full width.
9. **Footer** (global) — evergreen-ink, wordmark, nav, phone, address, counties line.

### Page 2 — Design & Build (`page-design-build`)
1. **Page header** — eyebrow "DESIGN · BUILD", h1 "Built from the ground up", lede from
   captured copy: they "design, build and maintain any type of landscape."
2. **Design-build feature** — split: AI-IMAGE (finished transformation) + ~70 words on
   full design-build capability (no invented process methodology).
3. **Retaining walls & hardscape** — feature block (walls are explicitly named in their
   copy): AI-IMAGE + short copy; keep scope to "retaining walls and hardscape" — no
   patio/paver menu is claimed in the dossier, so don't enumerate one.
4. **Guarantee band** — cedar-accented band: "All of our work is guaranteed." + CTA.
5. **Mini-CTA** — phone + "Get in touch" → Home `#contact`.

### Page 3 — Maintenance (`page-maintenance`)
1. **Page header** — eyebrow "PROPERTY CARE", h1 "Kept beautiful, season after season",
   lede: professional grounds maintenance "tailored to your needs" (captured phrase).
2. **What ongoing care covers** — 3 pebble cards: Grounds maintenance · Seasonal upkeep ·
   Property care programs — descriptions stay generic-but-true to the captured
   "grounds maintenance" service tag; no invented weekly-service menu.
3. **Why maintenance matters** — split with AI-IMAGE (manicured property) + copy
   connecting maintenance to protecting the built oasis.
4. **Mini-CTA**.

### Page 4 — Irrigation & Lighting (`page-irrigation`)
1. **Page header** — eyebrow "WATER & LIGHT" in `--river`, h1 "The systems behind a
   healthy, glowing yard".
2. **Irrigation feature** — river-tint band, wave divider: AI-IMAGE (sprinklers) +
   ~60 words on irrigation/sprinkler solutions (captured service tag; no brand names,
   no smart-system claims).
3. **Outdoor lighting feature** — split, mirrored: AI-IMAGE (dusk lighting) + ~60 words
   on landscape lighting.
4. **Pairing note** — short centered line on design-build + systems under one roof
   ("one company to design, build and maintain" — from captured copy).
5. **Mini-CTA** — phone + Home `#contact` link.

## 5. Hero direction

- **Headline:** "Your dream outdoor oasis, 25 years in the making." (Directly from
  their captured positioning language.)
- **Sub-copy:** "A family-owned Northern New Jersey landscaping company that designs,
  builds and maintains any type of landscape — from grounds maintenance to retaining
  walls. Licensed, insured, and guaranteed."
- **CTAs:** meadow "Call (862) 252-7030" + outline "See our services" (→ services
  overview). Note under CTAs, small: "Serving Essex, Morris & Union counties".
- **Hero image intent:** big pebble-cornered AI-IMAGE right-of-text on desktop (not
  full-bleed — the daylight direction keeps generous warm-white margins): a lush
  finished backyard oasis in morning light. Wave divider closes the hero.

## 6. Motion notes (ALL reduced-motion-gated; cursor effects off on pointer:coarse)

- Reveal-on-scroll: fade-up 16px, 450ms ease-out, 70ms stagger on card grids.
- Wave dividers drift horizontally a few px in a slow loop (12s, translateX only) —
  the site's one ambient touch; fully disabled under reduced-motion.
- Trust chips pop in with a slight scale (0.94→1) on first reveal.
- Hover on pebble cards: lift 4px + shadow soften (transform/box-shadow only).
- Magnetic hero call button (subtle). Custom cursor: meadow dot + river lerped ring;
  label "Call" over phone CTAs, "View" over service cards.
- No tilt — rounded friendly cards + tilt reads gimmicky; restraint here.

## 7. AI-IMAGE placeholder list

| # | Slot | Generation prompt for Harry |
|---|---|---|
| 1 | Home hero | "Lush finished backyard oasis in soft morning light: curved planting beds, vibrant green lawn, natural stone retaining wall in the background, dew on grass, welcoming family backyard in suburban New Jersey, no people" |
| 2 | Home card — design & build | "Newly completed backyard landscape transformation with fresh sod, curved mulched beds and young plantings, bright daylight" |
| 3 | Home card — maintenance | "Landscaper's clean result: neatly mowed lawn and freshly edged flower beds around a suburban home, midday sun" |
| 4 | Home card — irrigation | "Pop-up lawn sprinkler head spraying a fine arc of water over green grass, backlit by morning sun, water droplets sparkling" |
| 5 | Home card — lighting | "Warm landscape path lights glowing along a garden walkway at dusk, deep blue sky, cozy residential backyard" |
| 6 | Home about-family | "Well-kept landscaping work truck and trailer with mowers parked in a leafy West Orange-style suburban street, early morning, family-business feel, no readable logos or faces" |
| 7 | Design & Build — transformation | "Dramatic finished backyard makeover: new lawn, stone steps and terraced planting beds on a gentle slope, late-morning light" |
| 8 | Design & Build — retaining wall | "Sturdy natural stone retaining wall holding a raised planted bed, crisp construction, suburban yard, afternoon light" |
| 9 | Maintenance — manicured property | "Wide shot of a meticulously maintained residential property: striped lawn, trimmed shrubs, clean walkway edges, golden late-afternoon light" |
| 10 | Irrigation feature | "In-ground irrigation system running across a large green lawn, multiple sprinkler arcs catching sunlight, healthy turf" |
| 11 | Lighting feature | "Professional low-voltage landscape lighting at twilight: uplit trees and a warmly lit stone wall in a family backyard, inviting mood" |

## 8. Embed placeholders

- **Contact form** (Home `#contact`): meadow-tint pebble card, static labels (Name /
  Phone / Email / What's your project?) + meadow button; comment:
  `<!-- EMBED: contact form service goes here -->`.
- **Google Map** (Home, below contact): placeholder "Map — 118 S Valley Rd, West Orange
  NJ"; comment: `<!-- EMBED: Google Maps iframe, 118 S Valley Rd, West Orange, NJ 07052 -->`.
- No booking widget — phone/form business.

## 9. Content honesty notes (Builder: write around these)

- **Years:** use "25+ years" ONLY (listings vary 25–30; exact founding year is a
  `[placeholder]` — never print a year or "since 19XX").
- **"Licensed and insured… all work guaranteed"** — this IS captured listing copy, so
  the trust chips are dossier-backed; keep the exact phrasing and flag in outreach for
  Harry to confirm license details on first call.
- **"Alberto"** appears only inside a customer review — do NOT present him as owner,
  founder, or "the Son." No owner name anywhere; the about block stays "family-owned."
- **Testimonial** — use only the captured (truncated) Yelp quote, attributed to "Yelp
  review"; do not complete the sentence beyond what was captured or add other quotes.
  No star ratings (no aggregate rating captured).
- **Ponds** — directory-tag only, low confidence: excluded from the site entirely.
- **Dead domains** — never reference the old URLs in the mockup.
- **Hours, email, exact towns** — `[placeholder]`; verified contact facts are phone,
  address, and the Essex/Morris/Union counties service area. Do not invent an email.
- **No invented menus** — service sub-items beyond the captured five lines (design-build,
  grounds maintenance, retaining walls, irrigation, outdoor lighting) must not appear.
