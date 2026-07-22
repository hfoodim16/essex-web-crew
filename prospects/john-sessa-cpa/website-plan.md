# Website Plan — John Sessa Jr, CPA (`john-sessa-cpa`)

**Planner:** Essex Web Crew planner (Fable) · **Date:** 2026-07-22
**Pipeline:** web-design-ultra Stages 1–5 complete. This plan is the design contract — the Builder implements it exactly and re-decides nothing.

---

## 1. Art direction — "Balanced Books"

A precision-professional direction built on the client's own best review: *"straight and to the point, and very good at what he does."* Cool porcelain white, deep ink-navy, a manila-folder warm surface, and a single verdigris-teal accent — the visual language of a perfectly kept ledger: ordered, calm, quietly confident, zero franchise gloss. It says "43 years of clean books" without a single stock handshake.

**Personality words:** precise, established, personable.

## 2. Typography

- **Display:** **Spectral** (SemiBold 600 / Medium 500) — a bookish, precise serif with real authority; headings, hero, section titles. Use tight tracking at large sizes.
- **Body:** **Public Sans** (400/500) — civic-grade clarity; paragraphs, nav, forms, footer.
- **Accent (numerals/labels only):** **IBM Plex Mono** (400/500) — tabular figures for the phone number, "SINCE 1983," section eyebrows, and the trust-strip stats. This is the "ledger" voice; never body text.

Google Fonts all three. Never Inter/Roboto/Arial/Helvetica anywhere.

## 3. Color system (`:root` tokens)

| Token | Hex | Role |
|---|---|---|
| `--ink` | `#17293D` | Deep ink-navy — headings, body text, footer background |
| `--porcelain` | `#F7F9F8` | Cool porcelain white — page background |
| `--manila` | `#EFE7D6` | Manila-folder warm surface — alternating sections, cards, form panel |
| `--verdigris` | `#0F6E62` | Single accent — CTAs, links, active states, focus ring, rule accents |
| `--slate` | `#5B6B7A` | Muted — secondary text, captions, hairlines |

Palette family: **precision-professional (porcelain + ink + manila + verdigris)**. Backgrounds porcelain/manila; text ink; one accent only. CTA buttons: verdigris fill, porcelain text.

**Color-convention call:** the accounting/legal convention is navy + gold/burgundy/deep-green gravitas (authority, tradition, trust). This direction **honors** the navy trust core (ink-navy dominant) and **adapts** the accent — verdigris teal (trust + calm, per the Stage 2 engine's "trust teal" note) instead of gold, so it reads current, not lodge-hall. Deliberate honor-with-a-twist.

## 4. Page map (3 pages: `index.html`, `services.html`, `about.html`)

### Home (`index.html`)
1. **Left rail / header** (see layout note): text wordmark "John Sessa, CPA" in Spectral (dossier: **no logo exists** — wordmark is correct), nav, `tel:` call button always visible.
2. **Hero** — split: headline + sub + CTA left, contained hero photo right (GENERATE slot 1).
3. **Trust strip** — mono-numeral band: `SINCE 1983` · `43 YEARS IN PRACTICE` · `CPA — LICENSED IN NJ` · `BY THE BLOOMFIELD TRAIN STATION`. (No star rating here — the Chamber 4.8★/13 is `[verify]`; if the Builder includes it, it must be a labeled placeholder: `[4.8★ Chamber of Commerce — verify count]`.)
4. **Services overview** — three cards on manila: Tax · Accounting & Bookkeeping · Advisory (Advisory card copy hedged, see honesty note). Each links to `services.html`.
5. **"What neighbors say"** — ONE real Nextdoor quote, large Spectral pull-quote: *"John is straight and to the point, and very good at what he does."* — T. B., Nutley, NJ · via Nextdoor. (Builder: confirm display name on live Nextdoor page before using more than initials.)
6. **Service-area block** — "Serving Bloomfield, Glen Ridge, Nutley, Montclair, Belleville & surrounding Essex County" (dossier-attested towns; keep this phrasing).
7. **Estimate/booking CTA band** — verdigris band, one plain action: **"Call to book: (973) 748-5710"** (`tel:`) + secondary link to contact form on About page.
8. **Footer** — NAP: John Sessa Jr, CPA · 142 Washington St, Bloomfield, NJ 07003 · (973) 748-5710. Hours: `[Hours — confirm with John]` visible placeholder. NAP must match JSON-LD exactly.

### Services (`services.html`)
1. Page hero (typographic, no photo): "Services — plain and simple."
2. **Tax** — individual & small-business tax preparation and tax planning (the core; lead with it). Image slot 2 (GENERATE).
3. **Accounting & Bookkeeping** — general accounting and bookkeeping for small businesses. Image slot 3 (PLACEHOLDER).
4. **Advisory** — consulting / business planning; copy must hedge: "Ask John whether advisory support fits your situation" — see honesty note. No auditing claims.
5. **"Who John helps"** — individuals, small businesses; second real quote can sit here: *"John Sessa CPA Bloomfield N.J. 973-748-5710 The Best !"* — V. M., Glen Ridge, NJ · via Nextdoor (or omit if it reads awkward; T. B. quote is the priority).
6. CTA band (same as home) + footer.

### About + Contact (`about.html`)
1. **The practitioner story** — solo CPA, practicing since 1983 (43 years), by the Bloomfield train station. Copy written from dossier facts only. Image slot 4 (PLACEHOLDER, office-exterior intent).
2. **Credentials block** — CPA license (number `[CPA license # — placeholder]`), years, locality.
3. **Contact** — phone-first: big `tel:` button; **contact-form embed placeholder** (≤4 fields: name, phone, town, "what do you need help with"); **Google Map embed placeholder** for 142 Washington St.
4. Footer.

## 5. Hero direction

- **Headline concept:** "Straight answers. Clean books. Since 1983." (Direct lift of the review's cadence — the business's own reputation as the headline.)
- **Sub-copy angle:** solo CPA in Bloomfield — tax prep, planning, bookkeeping and accounting for individuals and small businesses, one practitioner who knows your name. One plain CTA: "Call to book."
- **Hero image intent:** the orderly-desk scene (slot 1 below) — calm, credible, human; contained in the split layout, not full-bleed.

## 6. Layout archetype + motion + background

- **Layout archetype: sidebar-anchored "letterhead."** Desktop: a fixed left rail (~300px) carrying the wordmark, nav, mono phone number, and a thin verdigris rule — like the margin rule on engraved letterhead; content scrolls right on a disciplined 12-col grid with generous whitespace. Mobile: rail collapses to a top bar with hamburger + persistent call button.
- **Background system:** porcelain base + a **fine graph-paper dot grid** (CSS `radial-gradient` dots, ~22px, ≤6% ink opacity, masked to fade at section edges) in hero and CTA bands only + one soft teal radial wash behind the hero (light-mode mesh, alpha ≤0.10) + the SVG grain overlay at 0.04. NOT parchment, NOT ruled lines (banned system), NOT dark.
- **Motion character: minimal-restrained — restraint is the flex.** Reveal-on-scroll (short 12px rise + fade, IntersectionObserver), a single **glint sweep** on the mono "SINCE 1983" numeral (7s sparse cycle, from atmosphere.md), verdigris underline draw-in on nav hover, gentle button press states. No cursor replacement, no tilt, no parallax — a CPA site that fidgets loses trust. Everything gated behind `prefers-reduced-motion`.
- **Atmosphere budget:** the glint is the one atmospheric effect. Nothing else.

## 7. Stage 5 — three divergent directions + the pick

Banned combos avoided (design-memory last 3): fonts Marcellus/Mulish, Bricolage Grotesque/Nunito Sans, Fraunces/Karla; palettes dark-luxury-evergreen+brass, light-daybreak-meadow-green, warm-heritage-parchment+pine+brass; layouts dark-editorial/service-index SPA, bright-family-friendly stack, ledger/archival-editorial; backgrounds flat-dark+diagonal, light-paper, parchment+rule-work. None of the three directions below touches any of these; this pick also diverges from the other two prospects this run (auto = dark industrial stack, tree = canopy-descent scroll).

- **Direction A — "Letterhead Classic."** Concept: engraved-stationery gravitas. Layout: centered-classic; Type: Libre Caslon / Source Sans 3; Palette: navy + white + gold (honors convention fully); Background: flat white + hairline rules; Motion: none-but-fades. *Honors the convention.* Rejected: safest of the three; gold + rules drifts toward the banned heritage/rule-work territory and reads like every attorney site.
- **Direction B — "Balanced Books" (PICKED).** Concept: the perfectly kept ledger — Swiss-precision professionalism with a human warm surface. Layout: sidebar-anchored letterhead; Type: Spectral / Public Sans + IBM Plex Mono numerals; Palette: ink + porcelain + manila + verdigris (honors navy core, adapts accent); Background: dot-grid graph paper + teal wash + grain; Motion: minimal + one glint. *Bold because:* no solo-CPA site looks like this — mono-numeral typography and a fixed letterhead rail give it a designed point of view while staying utterly trustworthy.
- **Direction C — "After Hours."** Concept: dark-mode boutique advisory — ink-black, cream serif, brass details, moody desk photography. Layout: immersive scroll. *Breaks convention* (dark luxury for a CPA). Rejected: collides with the banned dark-luxury palette family and over-styles a 43-year solo practitioner into a Manhattan wealth firm — dishonest register for this client.

**Pick: B.** It is the boldest direction that is still honest about who John is — Direction C is flashier but wrong for the client and banned-adjacent; B has a genuine editorial point of view (letterhead rail + ledger mono) no competitor CPA site in the Stage 3 gallery showed.

## 8. Image list (exactly 2 GENERATE; register locked once: **proud-contractor** — here "proud practitioner": real, warm, believable office photography, NOT editorial)

| # | Slot | Status | Spec |
|---|---|---|---|
| 1 | Home hero — orderly desk | **GENERATE** | `3:4`, **1K** (contained split-hero plate ~640–800px wide; not full-bleed, so 1K per sizing rule) |
| 2 | Services — Tax section | **GENERATE** | `4:3`, **1K** (contained section plate) |
| 3 | Services — Bookkeeping | PLACEHOLDER | labeled AI-IMAGE box: "tidy small-business bookkeeping scene — organized receipts, ledger, laptop, warm light" |
| 4 | About — office exterior | PLACEHOLDER | labeled AI-IMAGE box: "Main-Street professional office exterior near a NJ train station, morning light" |
| 5 | OG image | derived | crop of slot 1 to 1200×630 via media_optimizer (no extra generation) |

**Slot 1 generation prompt (hero):**
> A photograph of an orderly accountant's desk in a small professional office, taken with a phone, good consumer-camera quality, straight-on slightly elevated framing, level horizon: a closed manila folder, a stack of neatly squared tax documents, a desktop calculator, reading glasses and a fountain pen on a wooden desk, soft morning sun through a window at left, calm and unhurried, muted navy and warm cream tones, subtle grain, natural imperfections, uneven textures, no phone UI, no on-screen icons, no status bar, no timestamp overlay, no screen chrome, no readable names or numbers on any papers, no illustration, no 3D render, no CGI, no painting, no oversaturation, no plastic or waxy textures, no perfect symmetry, no text, no watermark, no logo, no people

**Slot 2 generation prompt (Tax section):**
> A photograph over the shoulder of an accountant in a light blue shirt reviewing a printed tax return with a client at a small office desk, taken with a phone, good consumer-camera quality, gently angled framing, level horizon, faces soft-focus and turned away, warm natural office light from a window, modest tidy office with a bookshelf behind, muted navy and cream tones, subtle grain, natural imperfections, no phone UI, no on-screen icons, no status bar, no timestamp overlay, no screen chrome, no readable text on the documents, no illustration, no 3D render, no CGI, no painting, no oversaturation, no plastic or waxy textures, no perfect symmetry, no watermark, no logo

Both optimize to WebP, downscaled to real display width. One register across the site; slots 3–4 placeholders styled in `--manila` with `--slate` label text.

## 9. Embed placeholders

- **Contact form** (about.html): styled placeholder panel, 4 fields max (name / phone / town / need), HTML comment `<!-- EMBED: contact form service goes here -->`. Phone > email emphasis.
- **Google Map** (about.html): styled placeholder block, `<!-- EMBED: Google Map — 142 Washington St, Bloomfield, NJ 07003 -->`.
- No booking widget (John books by phone).

## 10. Content honesty notes (Builder must respect)

- **No email exists** — do not print an email address anywhere. Phone is the only contact channel + form placeholder.
- **Advisory services (consulting / business planning / auditing) are cpadirectory-only `[verify]`** — the Advisory card uses hedged copy ("ask John whether…"), never lists "Auditing" as an offered service, and the plan deliberately leads with the consistently-attested core (tax prep, planning, bookkeeping, accounting).
- **Chamber 4.8★/13 is `[verify]`** — omit, or show only as a clearly labeled placeholder.
- **Hours unknown** — visible `[Hours — confirm with John]` placeholder in footer and JSON-LD `PLACEHOLDER_OPEN/CLOSE` tokens.
- **No fabricated tagline/about** — all copy written from dossier facts (1983, Bloomfield, by the train station, solo CPA).
- **Nextdoor reviewer names**: initials as captured (T. B., V. M.); Builder confirms display names on the live page before expanding.

## 11. Real reviews plan

Two real Nextdoor quotes exist (dossier "Real reviews") — use verbatim only:
1. T. B. (Nutley) quote → home pull-quote section (primary).
2. V. M. (Glen Ridge) quote → services page (optional; omit if awkward — it's mostly a phone number).
No review wall, no invented testimonials, no star widget without verification.

## 12. Local-trade conversion patterns (house standard)

- **Tap-to-call** `tel:+19737485710` in the header/rail on every page; call button persists in mobile top bar.
- **One plain CTA:** "Call to book: (973) 748-5710" — repeated hero / mid / footer.
- **Service-area block** with real towns (Bloomfield, Glen Ridge, Nutley, Montclair, Belleville).
- **Trust strip:** 43 years / since 1983 / CPA-licensed (license # as labeled placeholder) — all real or visibly placeholder.
- **No project gallery** (not applicable to a CPA — the services cards + credential block do this work; documented exception for the Critic).
- **Form ≤4 fields** (placeholder embed).
- **NAP footer** identical across pages and to JSON-LD: `John Sessa Jr, CPA · 142 Washington St, Bloomfield, NJ 07003 · (973) 748-5710`.
- **Local SEO:** JSON-LD `@type: "AccountingService"`; `<title>`: "CPA & Tax Preparation in Bloomfield, NJ | John Sessa Jr, CPA"; meta description naming tax prep + Bloomfield/Glen Ridge/Nutley; OG/Twitter cards with hero image; canonical; inline SVG favicon (ledger-tick "JS" mark in ink/verdigris); one `<h1>` per page with service + town. Unknown values stay `PLACEHOLDER_…` — never invented.
