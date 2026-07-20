# Website Plan — Gee-Kay Landscaping, Inc.

**Slug:** `gee-kay-landscaping` · **Planner:** Fable · **Date:** 2026-07-19
**Source of truth:** `prospects/gee-kay-landscaping/dossier.md` — every factual claim in the
mockup must trace back to it or be an obvious `[placeholder]`.

---

## 1. Art direction — "Heritage Ledger"

An earthy-editorial direction built around the idea of a 45-year family ledger: warm
parchment ground, deep pine green, hairline rules, and a large heritage serif — like a
well-kept record book of Livingston lawns since 1981. Gee-Kay has zero web presence, so
this site IS the brand; it must feel established on arrival, not startup-slick. The look
signals "we were here before the internet, and we're still meticulous" — heritage without
a single dated design move.

Signature moves the Builder should lean on:
- A thin double-rule ("ledger line") motif under section headings and above the footer.
- An oversized "EST. 1981" typographic badge (pure CSS/SVG text, no image) in the hero
  and footer — the one thing a visitor remembers.
- Generous parchment whitespace; content column narrower than usual (~1080px max) so the
  serif headlines feel printed, not web-templated.

## 2. Typography

Google Fonts — load only these two families, display=swap:

- **Display: Fraunces** (weights 400, 600; optical-size axis if using the variable font;
  italic 400 for pull-quotes). All h1–h3, the EST. 1981 badge, review pull-quotes, big
  stat numbers. Fraunces is a warm "wonky" old-style serif — heritage with a
  contemporary edge; it does the "since 1981" work on its own.
- **Body: Karla** (weights 400, 500, 700). Body copy, nav, buttons, labels, form text.
  Humanist grotesque with warmth — friendly like a family business, clean like a pro one.

Scale (Builder implements as tokens): body 17px/1.65; h1 clamp(2.6rem, 6vw, 4.5rem);
h2 clamp(1.9rem, 3.5vw, 2.75rem); h3 1.35rem; small-caps label style (Karla 700,
letter-spacing 0.12em, uppercase, 0.8rem) for section eyebrows like "OUR SERVICES".

## 3. Color system

`:root` tokens (5 colors, restraint over decoration):

| Token | Hex | Role |
|---|---|---|
| `--parchment` | `#F6F1E6` | Page background |
| `--ink` | `#26251E` | Primary text, footer background |
| `--pine` | `#31502F` | Headings, primary buttons, nav accents |
| `--brass-clay` | `#A8763E` | Accent only: eyebrow labels, rules, link hover, badge stroke |
| `--sage-mist` | `#E4E7D6` | Card/surface fill, img-placeholder base, alt-section bands |

Usage rules: pine-on-parchment for all headings (passes AA); ink-on-parchment for body;
`--brass-clay` never used for body text (decorative/large elements only — it's borderline
at small sizes); footer inverts to ink background with parchment text. No other hex values
anywhere in components.

## 4. Page map — 3 pages (single-file SPA per house recipe)

`index.html` with `<main class="page">` sections `page-home`, `page-services`,
`page-about`; nav via `data-page` links. Nav labels: Home · Services · About & Contact,
plus a pine "Call (973) 992-6687" button (real number, from dossier).

### Page 1 — Home (`page-home`)
1. **Hero** — see §5.
2. **Trust strip** — three ledger-style stats separated by hairlines: "Family-run since
   1981" · "5.0 on Angi" · "Licensed NJ Home Improvement Contractor". (All three are
   dossier-sourced.)
3. **Services overview** — three cards (Lawn & Grounds Maintenance / Landscape Design &
   Installation / Hardscapes), each: AI-IMAGE, Fraunces title, 2-sentence description
   written from dossier facts, "See services →" link to page-services.
4. **Why Gee-Kay** — two-column: left, "Livingston natives, meticulous by habit" heading
   + short copy built from review language (meticulous, family-run, fair prices); right,
   About-family AI-IMAGE.
5. **Review strip** — 2–3 real quotes as Fraunces italic pull-quotes with attribution
   ("Yelp review", "Yahoo Local review"): "family business that performs like a well
   oiled machine" · "meticulous with their work… extremely friendly staff". No star
   graphics except the cited Angi 5.0.
6. **CTA band** — pine background band: "Four decades of Livingston lawns. Yours next."
   + phone button + "Request an estimate" button → About & Contact page.

### Page 2 — Services (`page-services`)
1. **Page header** — eyebrow "WHAT WE DO", h1 "Services", one intro line from the
   aggregator description ("lawn maintenance, design and installation of new, and
   upgrading of existing landscapes and hardscapes").
2. **Service block ×3** (alternating image left/right):
   - *Lawn & Grounds Maintenance* — weekly/seasonal care, property upkeep.
   - *Landscape Design & Installation* — new landscape design, planting installation,
     upgrades to existing landscapes.
   - *Hardscapes* — design/installation of walkways, patios; upgrades to existing
     hardscape.
   Each: AI-IMAGE, h2, ~60-word description (from dossier service groups; no invented
   sub-services), small "Call for an estimate" text link.
3. **Service area note** — "Serving Livingston and surrounding Essex County towns"
   (dossier wording); the specific town list stays out unless confirmed — Builder may add
   `[town list to confirm]` as an HTML comment only, not visible copy.
4. **Mini-CTA** — repeat phone CTA band (shorter than Home's).

### Page 3 — About & Contact (`page-about`)
1. **Page header** — eyebrow "SINCE 1981", h1 "A Livingston family business".
2. **Story block** — ~120 words written strictly from dossier facts: founded 1981 by the
   Reinhardt family, Livingston natives, family-run construction + maintenance company.
   Where texture is missing use `[placeholder: owner's note]` styled as an italic
   pull-quote slot.
3. **Credentials row** — Licensed NJ Home Improvement Contractor · Family-owned ·
   `[Insured — confirm]` shown as a clearly-marked placeholder chip (do NOT assert
   insurance; dossier only confirms the license).
4. **Contact split** — left: phone (973) 992-6687, address 73 N Livingston Ave,
   Livingston, NJ 07039, hours `[Hours — placeholder]`; right: contact-form embed
   placeholder (§8).
5. **Map** — Google Map embed placeholder, full-width, sage-mist fill.
6. **Footer** (global) — ink background, EST. 1981 badge, nav links, phone, address,
   "Serving Livingston & surrounding areas".

## 5. Hero direction

- **Headline:** "Livingston's lawns, kept in the family since 1981." (Every word
  dossier-true.)
- **Sub-copy angle:** one sentence naming the three service lines + the family promise:
  "Lawn maintenance, landscape design, and hardscapes — built and cared for by the
  Reinhardt family for 45 years." (45 = 2026−1981; consistent with D&B founding year.)
- **CTAs:** primary pine button "Call (973) 992-6687"; secondary outline "Our services".
- **Hero image intent:** full-bleed AI-IMAGE placeholder behind a parchment content
  panel (or side-by-side split on desktop — Builder's layout call within this direction):
  a pristine suburban front lawn at golden hour. The EST. 1981 badge overlaps the image
  edge.

## 6. Motion notes (Builder gates ALL behind prefers-reduced-motion; cursor/tilt off on pointer:coarse)

Whisper-level, heritage-appropriate — no flash:
- Reveal-on-scroll: sections fade-up 18px, 500ms ease-out, staggered 60ms per card.
- Ledger rules "draw" in (scaleX 0→1, 600ms) when their section reveals.
- Stat numbers in the trust strip count up once on first reveal.
- Magnetic effect on the two hero buttons only (subtle, ≤6px translation).
- Custom cursor: small pine dot + lerped brass ring; ring label "View" over service
  cards, "Call" over phone CTAs.
- NO card tilt on this site — too playful for the heritage direction.

## 7. AI-IMAGE placeholder list (exact slots + generation prompts)

Style all placeholders in `--sage-mist` with a pine hairline border and centered label.

| # | Slot | Generation prompt for Harry |
|---|---|---|
| 1 | Home hero | "Wide golden-hour photo of a pristine, freshly striped suburban front lawn with mature oak trees and neat foundation plantings, upscale New Jersey colonial home softly out of focus behind, warm late-afternoon light" |
| 2 | Home card — maintenance | "Landscaping crew member edging a crisp lawn border along a slate walkway, green residential yard, midday, shallow depth of field" |
| 3 | Home card — design/install | "Freshly planted landscape bed with layered shrubs, perennials and dark brown mulch, curved stone edging, suburban front yard, soft morning light" |
| 4 | Home card — hardscape | "Newly laid bluestone paver walkway curving to a front porch through a green lawn, warm evening light, no people" |
| 5 | Home why-us / About family | "Weathered green pickup truck with landscaping trailer parked on a quiet tree-lined suburban New Jersey street, early morning light, nostalgic family-business feel, no readable logos or faces" |
| 6 | Services — maintenance block | "Overhead shot of a perfectly mowed lawn with clean diagonal mowing stripes and trimmed hedge line, residential property" |
| 7 | Services — design/install block | "Before-and-after style composition: one side bare soil garden bed, other side the same bed fully planted with shrubs, ornamental grasses and mulch, suburban yard" |
| 8 | Services — hardscape block | "Finished paver patio with low sitting wall beside a manicured lawn, dusk, warm landscape uplighting, no people" |

## 8. Embed placeholders

- **Contact form** (About & Contact): styled sage-mist block, fields listed as static
  labels (Name / Phone / Email / What do you need done?) + disabled-styled pine submit
  button; HTML comment: `<!-- EMBED: contact form service (e.g. Formspree) goes here -->`.
- **Google Map** (About & Contact): full-width placeholder block labeled "Map — 73 N
  Livingston Ave, Livingston NJ"; comment: `<!-- EMBED: Google Maps iframe, 73 N
  Livingston Ave, Livingston, NJ 07039 -->`.
- No booking widget — phone-first business.

## 9. Content honesty notes (Builder: write around these)

- **"Since 1981" / "45 years"** — from the D&B profile; aggregators say "over 35 years."
  Safe to use as designed, but keep it consistent (1981 everywhere) and flag in the
  outreach that Harry should confirm on first call.
- **Angi 5.0** — cite as "5.0 on Angi", nothing more (no review counts; none captured).
- **License** — "Licensed NJ Home Improvement Contractor" is dossier-backed; "insured"
  is NOT — use the `[Insured — confirm]` placeholder chip or omit.
- **Hours, email, tagline, about copy, exact town list** — none exist anywhere; all must
  be visible `[placeholder]`s or written around. Do not invent an email address.
- **Review quotes** — use only the exact quotes in the dossier, always attributed to
  their platform. A minority of reviews mention service concerns — do not reference
  reviews beyond the captured positive quotes.
- **No staff names** beyond "the Reinhardt family" and owner George Reinhardt (dossier-
  backed); no crew size, no photos implying specific real people.
