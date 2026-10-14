# Build Sheet — Atlas-Law

> **The Builder's ONLY required input.** Self-contained, ordered top-to-bottom in build
> order. If you must open `website-plan.md` to build a section, this sheet is defective:
> report it to the Planner via the lead; never bridge the gap by interpreting.
>
> Single authority (this sheet outranks the plan) · no renames · present tense only ·
> every section block is buildable from itself plus the global block · palette by token
> name only.

## Global block (paste-ready)

**Direction:** "Kentucky Field". White-first business-law site where Kentucky blue
(`var(--kentucky)`) is used as a full-strength color FIELD, never as a timid accent: the
home and about heroes are solid blue fields with white type, the attorney's real studio
portrait overlaps out of the blue into the white page below, and solid blue bands
punctuate the long pages. Type is a modern grotesk (Mona Sans) for the wordmark, headings and UI,
set against a crisp text serif (Source Serif 4) for reading. Square corners everywhere, no
gold, no metal accents, no rule-work. Put these three sentences at the top of
`style.css` as the rationale comment.

**Visual target:** `prospects/Atlas-Law/directions/a.png`. Match its mood, palette weight
(roughly one third blue field, two thirds white), type scale and the portrait overlap.
Its text is placeholder, never copy. It shows a split-header (big heading left, paragraph
right) under the strip: do NOT build that; section 3 below stacks its heading. Where the
comp disagrees with this sheet, the sheet wins.

**Site shape:** classic multi-page, three real HTML files sharing one `style.css` and one
`main.js`: `index.html`, `practice-areas.html`, `about.html`. No contact page and no
"Contact" nav item (the client said he doesn't want one); contact lives in the header,
a closing band on every page, and the footer. No form anywhere.

### Tokens

```css
:root{
  /* palette: five colors */
  --kentucky:#0033A0;   /* University of Kentucky royal blue (PMS 286). Fields, buttons, links, numerals */
  --white:#FFFFFF;      /* page ground; text on blue */
  --ink:#0B1530;        /* body + heading text on white; never pure black */
  --mist:#E8EEF8;       /* tinted tiles, alternate surfaces */
  --slate:#4B5873;      /* secondary text on white/mist (7.1:1 on white) */

  /* derived shades: computed from the five, not new colors */
  --kentucky-deep:color-mix(in oklch, var(--kentucky) 70%, var(--ink));
  --kentucky-lift:color-mix(in oklch, var(--kentucky) 84%, var(--white));
  --on-blue-muted:color-mix(in oklch, var(--white) 82%, var(--kentucky));
  --rule:color-mix(in oklch, var(--kentucky) 16%, var(--white));

  /* type */
  --font-display:"Mona Sans",system-ui,-apple-system,"Segoe UI",sans-serif;
  --font-body:"Source Serif 4","Iowan Old Style","Georgia",serif;
  --fs-wordmark:clamp(4.5rem, 15vw, 14rem);
  --fs-h1:clamp(2.6rem, 1.5rem + 3.7vw, 4.75rem);        /* short interior h1s: "Practice areas", "Matthew Atlas" */
  --fs-h1-hero:clamp(2.1rem, 1.1rem + 2.8vw, 3.25rem);  /* the long home h1 only: 52px max so it sets on 2 lines */
  --fs-h2:clamp(1.95rem, 1.35rem + 2vw, 3rem);
  --fs-stat:clamp(2.25rem, 1.6rem + 2.2vw, 3.5rem);
  --fs-h3:1.5rem;
  --fs-lead:1.3125rem;
  --fs-body:1.125rem;
  --fs-small:0.875rem;
  --lh-tight:1.04;
  --lh-body:1.6;

  /* space + layout */
  --container:1240px;
  --measure:62ch;
  --gutter:clamp(1.25rem, 4vw, 3rem);
  --space-section:clamp(4.5rem, 2.75rem + 6vw, 8.5rem);
  --space-block:clamp(2rem, 1.5rem + 2vw, 3.25rem);
  --nav-h:76px;
  --radius:0px;
  --overlap:clamp(48px, 8vw, 128px);
  --focus:3px solid var(--kentucky);

  /* motion */
  --ease:cubic-bezier(.77,0,.18,1);
  --dur-in:780ms;
  --dur-hover:220ms;
  --stagger:80ms;
  --i:0;               /* per-element stagger index; set inline as style="--i:n" */

  /* depth */
  --grain:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/></filter><rect width='100%' height='100%' filter='url(%23n)' opacity='.55'/></svg>");
  --field:radial-gradient(120% 90% at 85% 0%, var(--kentucky-lift) 0%, transparent 55%),
          radial-gradient(90% 80% at 0% 100%, var(--kentucky-deep) 0%, transparent 60%),
          var(--kentucky);
}
```

**Blue field recipe** (`.field`, used by `home-hero`, `home-fees`, `pa-disputes`, `about-hero`,
the blue tiles): `background:var(--field)` plus a `::before` overlay with
`background-image:var(--grain); opacity:.05; mix-blend-mode:overlay; pointer-events:none`.
Text on a field is `var(--white)`; secondary text on a field is `var(--on-blue-muted)`.
White and mist sections are flat. No dot grids, no hairline rule systems, no gradient
meshes on white.

**Corners:** `var(--radius)` (0) on every button, tile, image and card. No pill buttons,
no arch-top images, no rounded cards.

### Fonts

Self-host both as WOFF2 in `mockup/fonts/` (the site must work offline; no Google Fonts
`<link>` in the shipped HTML). Download from:
`https://fonts.googleapis.com/css2?family=Mona+Sans:wdth,wght@75..125,200..900&family=Source+Serif+4:ital,opsz,wght@0,8..60,200..900;1,8..60,400&display=swap`
(latin subset only). Declare with `font-display:swap`, `font-stretch:75% 125%` on Mona Sans.

| Use | Family | Settings |
|---|---|---|
| Wordmark "ATLAS LAW" (header + footer) | `var(--font-display)` | `font-stretch:125%; font-weight:800; letter-spacing:-0.01em; text-transform:none` (type it in capitals) |
| h1 | `var(--font-display)` | interior h1s: `font-size:var(--fs-h1); font-stretch:110%`; home h1: `font-size:var(--fs-h1-hero); font-stretch:100%; text-wrap:balance`; both `font-weight:700; line-height:var(--lh-tight); letter-spacing:-0.02em` |
| h2 | `var(--font-display)` | `font-stretch:105%; font-weight:650; line-height:1.08; letter-spacing:-0.015em` |
| h3, stat figures | `var(--font-display)` | h3 `font-weight:600`; figures `font-size:var(--fs-stat); font-stretch:105%; font-weight:750; white-space:nowrap` |
| Eyebrows, side-labels, nav, buttons, table labels, footer labels | `var(--font-display)` | `font-weight:560; font-size:var(--fs-small); letter-spacing:.06em`; eyebrows + side-labels uppercase, everything else sentence case |
| Body, lead, lists, quote | `var(--font-body)` | `font-optical-sizing:auto; font-weight:400`; lead `var(--fs-lead)`; pull quote `font-size:clamp(1.6rem,1.2rem+1.5vw,2.25rem); font-style:italic; line-height:1.3` |

All headings sentence case (only proper nouns and "ATLAS LAW" capitalized).

### Motion

- **entrance = clip-wipe.** Media (portraits, generated plates): `clip-path:inset(0 0 100% 0)` → `inset(0 0 0 0)`, a top-down unveil. Tiles and cards: `clip-path:inset(0 100% 0 0)` → `inset(0 0 0 0)`, left to right. Duration `var(--dur-in)`, ease `var(--ease)`, siblings staggered `calc(var(--i) * var(--stagger))`. Trigger once with IntersectionObserver (threshold .12, unobserve after). Applies ONLY to: `home-hero` portrait, `home-practice` tiles, `home-matt` photo, `pa-employment` cards, `pa-real-estate` image frame, `pa-fractional` tiles, `about-hero` portrait. Headings and paragraphs get no entrance.
- **hover = fill-sweep.** Every button and every linked tile: a `::before` layer `transform:scaleX(0)` → `scaleX(1)` from `transform-origin:left`, duration `var(--dur-hover)`, ease `var(--ease)`, label color swaps. Fills: solid blue button → `var(--kentucky-deep)`; white button on a field → `var(--mist)`; outline button → `var(--kentucky)` fill with `var(--white)` label (on a field: `var(--white)` fill with `var(--kentucky)` label); linked tile on white/mist → `var(--mist)`/`var(--rule)`; blue tile → `var(--kentucky-deep)`. Inline text links: underline color shifts from `var(--rule)` to `var(--kentucky)`, no animation. `:active{transform:scale(.98)}` on buttons. Hover styles only inside `@media (hover:hover) and (pointer:fine)`. Non-interactive cards (the `pa-employment` cards, the `pa-fractional` fee tiles) get NO hover.
- **set-piece = scroll-scrub, one, on the `pa-real-estate` image only.** Pure CSS, zero JS: the `<img>` sits in an `overflow:hidden` 4:5 frame; inside `@supports (animation-timeline: view())`, the image runs `@keyframes settle{from{transform:scale(1.14) translateY(-3%)}to{transform:scale(1) translateY(0)}}` with `animation:settle linear both; animation-timeline:view(); animation-range:entry 0% cover 60%`. No support → static image.
- **tempo:** entrances `var(--dur-in)` (780ms), hovers `var(--dur-hover)` (220ms), one ease `var(--ease)`, stagger `var(--stagger)` (80ms), total stagger span ≤ 0.6s. Never the bare `ease` keyword, never `linear` except the scrub.
- **GSAP tier 0.** No libraries, no `vendor/` folder.
- **Rule 0 (content never hidden by JS):** every hidden state is scoped to `html.js` inside `@media (prefers-reduced-motion: no-preference)`. Put the motion.md head snippet in `<head>` before the stylesheet (adds `js`, removes it on a script `error` event or after a 2s timer, `window.motionOK()` cancels the timer) and call `window.motionOK()` on the first line of `main.js`. Rename `main.js`, reload: every word and image visible.
- Reduced motion: no clip-wipes, no scrub, hovers become instant color changes.
- Header gains `box-shadow:0 1px 0 var(--rule)` once `scrollY > 8` (state, not a set-piece).

### Composition device

**Overlap, carried by `home-hero`:** the real formal portrait sits in the right 4 of 12
columns of the blue hero field and extends `var(--overlap)` (48–128px) below the field's
bottom edge into the white `home-credentials` strip, so the photo visibly crosses the
blue/white boundary. The strip runs full width with `padding-top:calc(var(--overlap) + 2.5rem)`,
so its items always start below the photo's bottom edge. `about-hero` repeats the same
overlap mirrored (portrait left), and `about-bio` starts below it the same way.
Every other section stays on the grid.

### Media budget

`2 GENERATE slots, $0` (bin/gen-image, ChatGPT Image; generate one at a time, hero-first
order: `pa-hero` plate, then `pa-real-estate` plate). Register: **editorial** for both
(documentary architectural photography, no people). Plus two REAL client headshots
(supplied, not generated). The OG image is built from the real formal portrait (crop only)
plus the wordmark (no generation). **Video: none.** Site budget $0.

Real client photos, copy into `mockup/assets/`:
- `headshot-2.jpeg` (formal, navy suit, red tie, grey studio seamless, 800×1000) → `assets/matt-formal.webp`, quality 85, same pixel size. Used in `home-hero` and `about-hero`.
- `headshot-1.png` (casual, dark jacket, blurred office, 800×800, soft detail) → `assets/matt-casual.webp`, quality 85, same pixel size. Display no larger than 360 CSS px wide anywhere. Used ONLY in `home-matt`. The file has a white feathered edge, so it sits on a `var(--white)` ground only, never on mist or blue.
- Source: `prospects/Atlas-Law/assets/headshots/`. **Crop and resize only.** No retouching, no background removal, no filters, no duotone, no grayscale, never regenerated.

Generated stills go to `mockup/assets/` as WebP (quality 82), with `width`/`height` set and
`loading="lazy"` below the fold. Realism QA after each: reject warped racking, window frames or ductwork,
garbled text, people, logos; one regeneration max, then report.

### Global components (every page, identical)

**Head snippet order:** charset, viewport, title, description, canonical, OG/Twitter,
inline SVG favicon (a `var(--kentucky)` square with a white bold "A" in Mona Sans; the
client has no logo, so this is a typographic placeholder favicon, not a mark), the
motion.md `js` snippet, `style.css`, JSON-LD. `<html lang="en">`.

**Skip link** (first focusable): "Skip to content" → `#main`.

**Header** (sticky, `var(--nav-h)` tall, `background:var(--white)`, one line at desktop):
- Left: wordmark text "ATLAS LAW" (link to `index.html`, `aria-label="ATLAS LAW, home"`), `var(--kentucky)`, `font-size:1.75rem`.
- Right, ≥ 820px: nav links "Practice areas" (`practice-areas.html`) and "About" (`about.html`), `var(--ink)`, `aria-current="page"` on the active page shown by a 2px `var(--kentucky)` bar under the label; then two buttons: solid "Email Matt" (`mailto:matt@matlas-law.com`; `background:var(--kentucky)`, label `var(--white)`) and outline "Text 917-213-4979" (`sms:+19172134979`; 1.5px `var(--kentucky)` border, label `var(--kentucky)`).
- < 820px: header padding `0 1rem`, items `gap:.375rem`. Wordmark at `font-size:1.125rem; font-stretch:112%` (about 130px wide). Then a compact solid "Email" button (mailto) and a compact outline "Text" button (sms), each `min-height:44px; min-width:44px; padding:0 .625rem; font-size:.8125rem; letter-spacing:.02em`. Then a 44×44px icon-only menu button: a three-line SVG icon (2px strokes, `var(--ink)`), `aria-label="Menu"`, `aria-expanded`, `aria-controls="menu"`, no visible text. Budget at 360px: 16 + 130 + 6 + 58 + 6 + 50 + 6 + 44 + 16 = 332px. The panel (`id="menu"`, full width under the header, `var(--white)`) lists "Practice areas", "About", "matt@matlas-law.com", "Text 917-213-4979". Email and Text stay visible in the header without opening the menu. All tap targets ≥ 44px.
- Header done-when: at 360px and 375px there is no horizontal scroll, the wordmark doesn't wrap, and Email, Text and the menu icon all show on one line.

**Closing contact band** is a per-page section (below), not a global component.

**Footer** (`background:var(--white)`, top border `1px solid var(--rule)`):
- Row 1: three columns.
  - "Contact" (label) — "matt@matlas-law.com" (mailto) · "Text 917-213-4979" (sms) · "New Jersey and New York".
  - "Pages" — "Home" · "Practice areas" · "About".
  - "Admissions" — "Admitted in New Jersey and New York" · "Matthew Atlas, Attorney at Law".
- Row 2, `id="legal"`: label "Disclaimer", then: "This website is general information, not legal advice. Emailing or texting ATLAS LAW doesn't create an attorney–client relationship, so please don't send confidential details until we've agreed to work together." Label "Privacy", then: "This site has no forms and sets no tracking cookies. Emails and texts you send go directly to Matt." (Use an en dash in "attorney–client".) Add an HTML comment above this row: `<!-- Proposed legal text: the attorney must approve or replace it before launch. -->`
- Row 3: the wordmark "ATLAS LAW" at `var(--fs-wordmark)`, `var(--kentucky)`, `font-stretch:125%; font-weight:800; line-height:.82`, full container width, as a `<p aria-hidden="true">` (the brand line; the name is already in text above).
- Row 4: "© 2026 ATLAS LAW" left; "Disclaimer" and "Privacy" links (both to `#legal`) right; `var(--slate)`, `var(--fs-small)`.

### Head / SEO

Domain (client's, Q30): `https://www.matlas-law.com/`.

| Page | `<title>` | meta description | canonical |
|---|---|---|---|
| `index.html` | Business Lawyer in New Jersey & New York \| ATLAS LAW | AI-assisted business law from Matthew Atlas, over 15 years as in-house counsel. Fixed fee and subscription arrangements. Commercial, employment, disputes, real estate. NJ and NY. | `https://www.matlas-law.com/` |
| `practice-areas.html` | Practice Areas: Commercial, Employment, Real Estate \| ATLAS LAW | Commercial contracts and M&A, employment claims and handbooks, dispute resolution, real estate leases and financings, and fractional general counsel. NJ and NY. | `https://www.matlas-law.com/practice-areas.html` |
| `about.html` | About Matthew Atlas \| ATLAS LAW | Over 15 years as in-house counsel at JPMorgan Chase, Colgate-Palmolive, Saks Fifth Avenue and Related. Admitted in New Jersey and New York. | `https://www.matlas-law.com/about.html` |

OG + Twitter (`summary_large_image`) on every page: `og:title` = the page title,
`og:description` = the meta description, `og:image` =
`https://www.matlas-law.com/assets/og.jpg`, `og:type` = website. Build `og.jpg` with
ImageMagick, 1200×630: left 696px is flat `#0033A0` (the `var(--kentucky)` value) with
"ATLAS LAW" in white Mona Sans (125% width, weight 800, about 96px) and under it "AI-assisted business law · New Jersey & New York" in white Mona Sans 500 at about 30px; right 504px is the real
formal portrait `headshot-2.jpeg` scaled to 630px tall (504×630, the full 4:5 frame, crop
and resize only, no filter or retouch). No generated image in the OG card.

JSON-LD (identical on all three pages; no address, by the client's choice; no `geo`, no
`sameAs`, no hours, no price range: none were given):

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LegalService",
  "name": "ATLAS LAW",
  "url": "https://www.matlas-law.com/",
  "email": "matt@matlas-law.com",
  "telephone": "+1-917-213-4979",
  "image": "https://www.matlas-law.com/assets/og.jpg",
  "foundingDate": "2026-09",
  "areaServed": [
    { "@type": "State", "name": "New Jersey" },
    { "@type": "State", "name": "New York" }
  ],
  "knowsAbout": ["Commercial law", "Employment law", "Dispute resolution and litigation", "Real estate law", "Fractional general counsel"],
  "founder": { "@type": "Person", "name": "Matthew Atlas", "jobTitle": "Attorney" }
}
</script>
```

Footer NAP and JSON-LD must match: "ATLAS LAW", "matt@matlas-law.com", "917-213-4979".
One `<h1>` per page.

**Release form:** pages built = Home, Practice areas, About. Client = ATLAS LAW, Matthew
Atlas, matt@matlas-law.com. Domain line: www.matlas-law.com (client-supplied, Q30).

## Claims ledger (the Builder states nothing outside it)

| Claim (as worded on the page) | Source | Type | Evidence on page | Missing before publish |
|---|---|---|---|---|
| "over 15 years" / "15+ years as in-house counsel" | client-answers Q3 | factual | named employers beside it | none |
| In-house at "JPMorgan Chase, Colgate-Palmolive, Saks Fifth Avenue and Related" (text only, no logos) | Q3 | factual | names in text | titles + dates per company (confirm, optional) |
| "Admitted in New Jersey and New York" | Q23; NY confirmed by NY OCA reg. 4252565 | factual | footer + about table | NJ admission year (optional) |
| "Law school: University of Virginia" | NY OCA registration record (dossier) | factual | about table | client confirms wording/degree |
| "Private practice since September 2025" / "ATLAS LAW since September 2026" / `foundingDate 2026-09` | Q2 | factual | home-matt, about | none |
| "for companies with around $50 million to $200 million in annual revenue …" | Q6 | positioning | home-approach | client OK to publish the revenue band |
| "don't need, or can't fund, a full-time lawyer on staff" | Q6 ("don't have the need or the funds") | positioning | home-approach | none |
| "I'm open to alternative fee arrangements, including fixed fees and subscriptions, so you know the rate and can budget for it." + the two one-line fee definitions in `pa-fractional` (no "monthly", no prices, no terms) | Q11 + client update 2026-10-13 (point 2) | conditional | home-fees, pa-fractional, about-background | client confirms the one-line definitions match how he'd scope them |
| "AI-assisted business law" (eyebrow) / "An AI-based firm with flexible fees" (h2) / "I run ATLAS LAW as an AI-based firm." / "AI-assisted. I do the legal work." | client update 2026-10-13 (point 1: "AI Based Law Firm") | positioning | home-hero, home-fees, about-bio, about-background | none; always shown beside the line that he does the legal work |
| "AI tools make the work more efficient." / "AI tools help me work efficiently" | client update 2026-10-13 ("Using AI tools to provide legal services more efficiently") | factual (process, no outcome) | home-fees, about-bio | none |
| "What you're paying for is my experience and my legal and business judgment, not my time." | client update 2026-10-13, near-verbatim | positioning | home-fees | client confirms it holds on every engagement (if any matter is billed hourly, reword) |
| "The tools assist. I do the legal work, check what they produce and stand behind the advice." / "the legal work and the judgment calls stay with me" | Harry's compliance instruction (2026-10-13) + the lawyer's own duty of competence and supervision | factual (about his practice) | home-fees, about-bio | client confirms the wording describes how he works |
| Practice areas + every sub-item | Q9 | factual | practice-areas page | none |
| "Alternative fee arrangements, including fixed fees and subscriptions, are available for the other practice areas too." | Q11 + client update 2026-10-13 | conditional | pa-fractional | none |
| "Employment claims and real estate disputes, from early resolution through litigation." | Q9 (the disputes heading + his listed "Employment Claims" and "Real estate disputes") | conditional | pa-disputes | client confirms the line and anything to add |
| "I'm based in New Jersey and New York and take clients from anywhere." | Q4 | factual | home-approach | none |
| "Messages go straight to me." | solo practice, his own email/number (Q24) | factual | contact bands | none |
| Pull quote "This is what I'm doing now, and I'm available if you're looking for legal services." | Q2, lightly edited (person/tense) | his words | home-matt | client approves the edit |
| Footer disclaimer + privacy text | none (standard protective text) | assurance | footer `#legal` | attorney approves or replaces (launch blocker) |
| "sets no tracking cookies" | the build itself | factual | footer | stays true only if no analytics are added at go-live |
| NOT CLAIMED anywhere: specialist / specializes / certified / expert / best / top / leading; any comparison with other lawyers or "outside counsel"; prices; "lower rates"; "fewer billable hours"; any saving, percentage or "value" promise; "insights traditional firms don't give" or any comparison with traditional firms; names of specific AI tools; "free consultation"; response times; case results; reviews; awards; "20+ years"; "General Counsel at [company]" | NJ RPC 7.1(a), 7.1(a)(3), 7.4(a); NY Rule 7.1; dossier; Harry 2026-10-13 | — | — | — |

## Interaction cards

None. No custom interactions: the mobile menu, linked tiles and the CSS scrub are
standard patterns. No slider, no configurator, no form.

## Sections (build in this order)

### 1. id: home-hero

- page: `index.html` (first section inside `<main id="main">`)
- format: hero, opener: kicker+h2
- layout: full-width `.field` (blue field recipe), content in the container on a 12-col grid. Text in cols 1–8 (about 800px at a 1240px container), vertically centred, top padding ≤ 6rem. Portrait in cols 9–12, aspect 4:5 (about 390×490px), bottom edge extends `var(--overlap)` below the field (the composition device). Field min-height removed (lead ruling 2026-10-13, audit R1 fix 1): the field's height comes from its content + padding. The portrait is top-aligned to the text block (the portrait's top edge sits within 40px of the eyebrow's top at 1440×900) and still crosses the field's bottom edge by `var(--overlap)` — match the About hero. Text column stays cols 1–8; never widen it.
- copy:
  - eyebrow (`<p>`, uppercase small label): "AI-assisted business law · New Jersey & New York"
  - h1: "A business lawyer who spent over 15 years in-house." (`font-size:var(--fs-h1-hero)` = 52px at 1440, `font-stretch:100%`, `text-wrap:balance`, no forced `<br>`; 51 characters balance to two lines of about 740px each inside the ~800px column)
  - subtext (`var(--fs-lead)`, `var(--font-body)`): "Contracts, employment, disputes, real estate and fractional general counsel work for companies without their own legal department."
  - CTAs: solid white "Email Matt" (`mailto:matt@matlas-law.com`) and outline-white "Text 917-213-4979" (`sms:+19172134979`)
  - That is the whole hero: 4 text elements. No caption, no trust strip, no tagline inside it.
- palette: bg the field (`var(--kentucky)`, `var(--kentucky-lift)`, `var(--kentucky-deep)` via `var(--field)`), h1 `var(--white)`, eyebrow + subtext `var(--on-blue-muted)`, solid CTA bg `var(--white)` label `var(--kentucky)`, outline CTA border + label `var(--white)`, focus ring `3px solid var(--white)` on the field.
- assets: `assets/matt-formal.webp` (real client photo, from `headshot-2.jpeg`), `alt="Matthew Atlas, founder of ATLAS LAW"`, `width="800" height="1000"`, `fetchpriority="high"`, not lazy. Crop/resize only.
- motion: clip-wipe (media, top-down) on the portrait only.
- mobile (< 820px): text first, then the portrait at 78% of the container width, right-aligned, overlapping the strip by 48px; h1 ≤ 4 lines at 375px (it sets at about 34px there); both CTAs full width, stacked.
- done-when: at 1440px and at 1280px the h1 sits on exactly 2 lines at no more than 52px, both CTAs are visible without scrolling, and the portrait visibly crosses the blue/white edge into the strip below. If Mona Sans sets wider than estimated and the h1 makes 3 lines, step `--fs-h1-hero`'s max down by 0.125rem at a time until it makes 2; never widen the text column into the portrait.

### 2. id: home-credentials

- page: `index.html`
- format: stat-strip, opener: none
- layout: white ground, full container width (cols 1–12), three equal items in a row (each about 390px at 1440), separated by 1px `var(--rule)` vertical dividers. `padding-top:calc(var(--overlap) + 2.5rem)` so every item starts below the hero portrait's bottom edge; `padding-bottom:var(--space-block)`. Each item: figure on top (`var(--fs-stat)` = 56px max, `white-space:nowrap`; "Fixed fee" is the widest at about 290px), label under it. Between 820px and 1100px the figure size follows the clamp down (about 40px at 900px) and the three items stay in one row. No heading.
- copy:
  - "15+" / "years as in-house counsel"
  - "NJ & NY" / "admitted to both bars"
  - "Fixed fee" / "and subscription arrangements"
- palette: bg `var(--white)`, figures `var(--kentucky)` at `var(--fs-stat)`, labels `var(--ink)` in `var(--font-body)`, dividers `var(--rule)`.
- assets: none
- motion: none (static figures; no count-up).
- mobile (< 820px): one column, items separated by horizontal `var(--rule)` lines; `padding-top:calc(48px + 2rem)` so it starts below the portrait's 48px overlap.
- done-when: at 1440px, 1024px and 375px all three figures sit on one line each inside their own item with no overflow, and no part of the strip's text is covered by the portrait.

### 3. id: home-approach

- page: `index.html`
- format: editorial-column, opener: bare-h2
- layout: white ground, one column at `var(--measure)` starting at col 2 (offset, not centred). Heading STACKED above the paragraphs (no split header).
- copy:
  - h2: "A legal and business advisor for your company"
  - p: "I worked as counsel at JPMorgan Chase, Colgate-Palmolive, Saks Fifth Avenue and Related, so I understand the client side well. I've helped companies solve their problems with practical answers and kept legal from being the obstacle to getting things done."
  - p: "ATLAS LAW is set up for companies with around $50 million to $200 million in annual revenue that have legal issues but don't need, or can't fund, a full-time lawyer on staff."
  - p: "I'm based in New Jersey and New York and take clients from anywhere."
- palette: bg `var(--white)`, h2 `var(--ink)`, body `var(--ink)`, last paragraph `var(--slate)`.
- assets: none
- motion: none
- done-when: the heading sits above three paragraphs in a single left-offset column no wider than 62ch.

### 4. id: home-fees

- page: `index.html` (directly after `home-approach`, before `home-practice`)
- format: full-bleed-band, opener: in-media
- layout: full viewport width `.field` band (blue field recipe: radial field + 0.05 grain), padding `var(--space-section)` top and bottom. h2 across cols 1–10 inside the band. Under it, two text blocks side by side: block A in cols 1–6, block B in cols 7–12, top-aligned, `gap:var(--space-block)`. The CTA sits under both blocks, left-aligned. No photo, no icons, no divider rule between the blocks.
- copy:
  - h2: "An AI-based firm with flexible fees"
  - block A: h3 "How I work" / p "AI tools make the work more efficient. What you're paying for is my experience and my legal and business judgment, not my time." / p "The tools assist. I do the legal work, check what they produce and stand behind the advice."
  - block B: h3 "Fixed fee or subscription" / p "I'm open to alternative fee arrangements, including fixed fees and subscriptions, so you know the rate and can budget for it."
  - CTA: solid white "Email Matt" (`mailto:matt@matlas-law.com`)
- palette: bg `var(--field)`, h2 + h3 `var(--white)`, p `var(--on-blue-muted)`, CTA bg `var(--white)` label `var(--kentucky)`.
- assets: none
- motion: hover fill-sweep on the CTA.
- mobile (< 820px): h2, then block A, then block B, stacked full width; CTA full width.
- done-when: one full-width blue band directly under `home-approach` carrying the heading, the two blocks with the copy exactly as above, and a working Email button; no photo, no price, no percentage, no "monthly", and the word "AI" appears at most 3 times on the whole home page (eyebrow, this h2, block A's first sentence).

### 5. id: home-practice

- page: `index.html`
- format: bento, opener: side-label
- layout: `var(--mist)` ground. The h2 is a side-label: rotated -90deg in a narrow left margin column (desktop), reading bottom-to-top. The bento uses a 6-column grid with these areas (DOM order stays Q9 order: commercial, employment, disputes, real estate, fractional):
  `"com com com com fgc fgc" / "emp emp emp emp fgc fgc" / "dr dr dr re re re"`. Reading order left-to-right, top-to-bottom never puts Real estate before Disputes. Five tiles, five cells, no empty cell. Each tile is one `<a>` to `practice-areas.html#<section id>`, with an `→` glyph (aria-hidden) bottom-right.
- copy:
  - h2 (side-label): "Practice areas"
  - tile `com` → `practice-areas.html#pa-commercial`: h3 "Commercial law" / p "Vendor and services agreements, NDAs, supply agreements and licenses. Purchase and sale agreements and M&A."
  - tile `emp` → `practice-areas.html#pa-employment`: h3 "Employment law" / p "EEOC charges, discrimination and wage and hour claims, internal investigations, offer letters, separations, handbooks and RIF analysis."
  - tile `dr` → `practice-areas.html#pa-disputes`: h3 "Dispute resolution and litigation" (no paragraph; the client gave no sub-items)
  - tile `re` → `practice-areas.html#pa-real-estate`: h3 "Real estate" / p "Leases and guaranties, LOIs, construction agreements, financings, ADA claims and real estate disputes."
  - tile `fgc` → `practice-areas.html#pa-fractional`: h3 "Fractional general counsel" / p "Ongoing legal help as your company's part-time general counsel."
- palette: section bg `var(--mist)`; tiles `com`, `emp`, `re`, `dr` bg `var(--white)` with text `var(--ink)` and p `var(--slate)`; tile `fgc` is a blue field (`var(--field)`) with text `var(--white)` and p `var(--on-blue-muted)`; side-label `var(--kentucky)`; arrows `var(--kentucky)` (white on `fgc`).
- assets: none
- motion: clip-wipe (tiles, left to right), `--i` 0–4 in DOM order; hover fill-sweep on every tile.
- mobile: side-label becomes a normal horizontal small uppercase label above the tiles; tiles stack in Q9 order, one column.
- done-when: five tiles of unequal size fill the grid with no gap cell, the fractional tile is blue, and each tile click lands on its anchor on the practice-areas page.

### 6. id: home-matt

- page: `index.html`
- format: split, opener: none
- layout: white ground, 12-col: photo in cols 2–5 (1:1, max 360px wide), quote block in cols 6–11, vertically centred. No heading element; the pull quote opens the section.
- copy:
  - blockquote (pull quote style): "This is what I'm doing now, and I'm available if you're looking for legal services."
  - cite under it: "Matt Atlas, founder"
  - p (small, `var(--font-display)`): "Private practice since September 2025. ATLAS LAW since September 2026."
  - link: "More about Matt" → `about.html` (with `→` glyph, aria-hidden)
- palette: bg `var(--white)`, quote `var(--ink)`, cite + facts `var(--slate)`, link `var(--kentucky)` with underline `var(--rule)`.
- assets: `assets/matt-casual.webp` (real client photo, from `headshot-1.png`), `alt="Matt Atlas"`, `width="800" height="800"`, displayed ≤ 360px, `loading="lazy"`. Crop/resize only.
- motion: clip-wipe (media, top-down) on the photo.
- mobile: photo 200px wide, left-aligned, above the quote.
- done-when: the casual photo renders no wider than 360px beside the quote, and the link opens `about.html`.

### 7. id: home-contact

- page: `index.html` (last section before the footer)
- format: cta-band, opener: bare-h2
- layout: `var(--mist)` band, container with h2 + line on the left (cols 1–7) and the two buttons plus the email link on the right (cols 8–12).
- copy:
  - h2: "Email or text me directly"
  - p: "Messages go straight to me."
  - detail (plain text link): "matt@matlas-law.com" (mailto)
  - buttons: solid "Email Matt" (mailto) and outline "Text 917-213-4979" (sms)
- palette: bg `var(--mist)`, h2 `var(--ink)`, p `var(--slate)`, solid button bg `var(--kentucky)` label `var(--white)`, outline border + label `var(--kentucky)`, email link `var(--kentucky)`.
- assets: none
- motion: hover fill-sweep on buttons.
- mobile: one column, buttons full width.
- done-when: both buttons and the email link open mailto/sms with the correct address and number, and the Text button shows the number at every width.

### 8. id: pa-hero

- page: `practice-areas.html` (first section inside `<main id="main">`)
- format: hero, opener: in-media
- layout: full-width band, min-height `clamp(420px, 60vh, 620px)`, the generated plate behind with scrim `linear-gradient(90deg, color-mix(in oklch, var(--kentucky) 92%, transparent) 0%, color-mix(in oklch, var(--kentucky) 70%, transparent) 55%, color-mix(in oklch, var(--kentucky) 30%, transparent) 100%)`. Text inside the image band, cols 1–7, top padding ≤ 6rem.
- copy:
  - h1: "Practice areas"
  - subtext: "5 areas of business law. If your issue isn't listed, email or text me and ask."
  - on-page links (`<nav aria-label="On this page">`, a row of plain outlined-white links): "Commercial" → `#pa-commercial`, "Employment" → `#pa-employment`, "Disputes" → `#pa-disputes`, "Real estate" → `#pa-real-estate`, "Fractional general counsel" → `#pa-fractional`
- palette: scrim from `var(--kentucky)`, h1 `var(--white)`, subtext `var(--on-blue-muted)`, link borders + labels `var(--white)`.
- assets: GENERATE `assets/plate-warehouse.webp`, aspect **16:9**, register **editorial**, full-width page hero, `fetchpriority="high"`. Prompt, verbatim:
  > A photograph of the interior of a clean, well-run mid-sized distribution warehouse, tall blue steel pallet racking receding down a wide central aisle, neatly stacked pallets of plain unmarked cardboard cartons, a sealed polished concrete floor, soft daylight from high clerestory windows mixing with overhead LED light. Documentary editorial photography, 35mm lens at eye level, calm, orderly and quiet, slight film grain, honest colors with cool blue tones, the left third of the frame darker and less busy for a headline. Empty of people. No readable labels, no barcodes, no branding, no logos, no signage, no text on boxes, no forklifts, no illustration, no 3D render, no CGI, no painting, no oversaturation, no plastic textures, no perfect symmetry, no watermark.
- motion: none on the hero (it is above the fold).
- mobile: band min-height 360px; on-page links wrap into rows of full-width-friendly 44px-tall targets.
- done-when: the h1 reads white over the plate at AA contrast and all five on-page links jump to their sections.

### 9. id: pa-commercial

- page: `practice-areas.html`
- format: editorial-column, opener: bare-h2
- layout: white ground, one column at `var(--measure)` starting at col 2. h2, then two groups, each an h3 with an unordered list (no bullets; each item on its own line with a 1px `var(--rule)` top border).
- copy:
  - h2: "Commercial law"
  - h3: "Contracts" / list: "Vendor and services agreements" · "Non-disclosure agreements (NDAs)" · "Supply agreements" · "Licenses"
  - h3: "Transactional documents" / list: "Purchase and sale agreements" · "Mergers and acquisitions (M&A)"
- palette: bg `var(--white)`, h2 `var(--ink)`, h3 `var(--kentucky)`, list text `var(--ink)`, item borders `var(--rule)`.
- assets: none
- motion: none
- done-when: all six Q9 commercial items appear under their two group headings.

### 10. id: pa-employment

- page: `practice-areas.html`
- format: card-grid, opener: side-label
- layout: `var(--mist)` ground. h2 as a side-label rotated -90deg in a narrow left margin column (desktop). Six cards in a **2-column** grid (three rows), equal width, heights follow content, all square-cornered. Cards are NOT links and get no hover.
- copy:
  - h2 (side-label): "Employment law"
  - card: h3 "Employment claims" / list "Discrimination and EEOC charges" · "Wage and hour claims"
  - card: h3 "Internal investigations" / list "Employee complaints"
  - card: h3 "Employment agreements" / list "Offer letters and employment agreements" · "Terminations and separations"
  - card: h3 "Employee handbooks"
  - card: h3 "Reduction in force (RIF) analysis"
  - card: h3 "General employment counseling"
- palette: section bg `var(--mist)`; cards 1 and 3 (the two Q9 groups that carry nested sub-items, so they're the heaviest cards; this is the reason they're blue) bg `var(--kentucky)` with h3 `var(--white)` and list `var(--on-blue-muted)`; cards 2, 4, 5, 6 bg `var(--white)` with h3 `var(--ink)` and list `var(--slate)`; side-label `var(--kentucky)`.
- assets: none
- motion: clip-wipe (cards, left to right), `--i` 0–5.
- mobile: side-label becomes a horizontal small uppercase label; one column.
- done-when: six cards, all nine Q9 employment entries (including the nested ones) present, two cards blue.

### 11. id: pa-disputes

- page: `practice-areas.html`
- format: full-bleed-band, opener: in-media
- layout: full-width `.field` band (blue field recipe), container cols 1–8, generous vertical padding `var(--space-section)`.
- copy:
  - h2: "Dispute resolution and litigation"
  - p: "Employment claims and real estate disputes, from early resolution through litigation."
  - CTA: outline-white "Email Matt" (mailto)
- palette: bg `var(--field)`, h2 `var(--white)`, p `var(--on-blue-muted)`, CTA border + label `var(--white)`.
- assets: none
- motion: hover fill-sweep on the CTA.
- done-when: a solid blue band with the heading, one line, and a working Email button; nothing else added.

### 12. id: pa-real-estate

- page: `practice-areas.html`
- format: split, opener: bare-h2
- layout: white ground, image cols 1–5 (aspect 4:5), text cols 7–12. h2 then a single list (no bullets, `var(--rule)` top borders).
- copy:
  - h2: "Real estate"
  - list: "Lease negotiation, guaranties and lease interpretation" · "Letters of intent (LOIs)" · "Construction agreements" · "Real estate disputes" · "ADA claims" · "Financings and loans"
- palette: bg `var(--white)`, h2 `var(--ink)`, list `var(--ink)`, borders `var(--rule)`.
- assets: GENERATE `assets/plate-space.webp`, aspect **4:5**, register **editorial**, contained split image, `loading="lazy"`. Prompt, verbatim:
  > A photograph of an empty, newly finished ground-floor commercial space ready for a new tenant: tall storefront windows looking out onto a quiet tree-lined suburban street, a sealed polished concrete floor, clean white walls, an open ceiling with neatly run ductwork painted white, soft morning daylight falling across the floor in long window-shaped patches. Documentary architectural photography, 24mm lens at eye level, natural light only, honest proportions, slight film grain, neutral whites with cool blue shadows. No furniture, no people, no signage, no lettering on the windows, no "for lease" signs, no logos, no text, no illustration, no 3D render, no CGI, no painting, no oversaturation, no plastic textures, no perfect symmetry, no watermark.
- motion: clip-wipe (media, top-down) on the 4:5 frame, plus the site's one set-piece: the CSS scroll-scrub (`settle`) on the `<img>` inside that `overflow:hidden` frame.
- mobile: image first at full width (aspect 4:3 crop via `object-fit:cover`), list below.
- done-when: the six Q9 real-estate items appear beside a believable empty commercial space with no readable signage, and with `animation-timeline` support the image visibly settles inside its frame as the section scrolls through.

### 13. id: pa-fractional

- page: `practice-areas.html`
- format: bento, opener: in-media
- layout: white ground, a 3-tile bento: tile A (blue field) spans cols 1–7 and both rows; tiles B and C stack in cols 8–12. The h2 sits INSIDE tile A (in-media opener). Tiles are not links.
- copy:
  - tile A: h2 "Fractional general counsel" / p "Your company's general counsel, part-time, for businesses that don't have their own legal department."
  - tile B: h3 "Fixed fee" / p "One price for a defined piece of work, agreed before it starts."
  - tile C: h3 "Subscription" / p "For ongoing legal work rather than a single matter."
  - line under the bento (`<p>`, full width, `var(--slate)`, `var(--font-body)`): "Alternative fee arrangements, including fixed fees and subscriptions, are available for the other practice areas too."
- palette: tile A `var(--field)` with h2 `var(--white)` and p `var(--on-blue-muted)`; tile B bg `var(--mist)` with h3 `var(--kentucky)` and p `var(--ink)`; tile C bg `var(--white)` with 1.5px `var(--rule)` border, h3 `var(--kentucky)`, p `var(--ink)`.
- assets: none
- motion: clip-wipe (tiles, left to right), `--i` 0–2. No hover (tiles are not interactive).
- mobile: one column, A then B then C.
- done-when: three unequal tiles, heading inside the blue tile, fee tiles carry only the two one-line definitions (no "monthly", no prices), and the one line under the bento reads exactly "Alternative fee arrangements, including fixed fees and subscriptions, are available for the other practice areas too."

### 14. id: pa-contact

- page: `practice-areas.html` (last section before the footer)
- format: cta-band, opener: bare-h2
- layout: `var(--mist)` band, h2 + line cols 1–7, buttons + email link cols 8–12.
- copy:
  - h2: "Not sure which area fits? Email or text me."
  - p: "Messages go straight to me."
  - detail (plain text link): "matt@matlas-law.com" (mailto)
  - buttons: solid "Email Matt" (mailto) and outline "Text 917-213-4979" (sms)
- palette: bg `var(--mist)`, h2 `var(--ink)`, p `var(--slate)`, solid button bg `var(--kentucky)` label `var(--white)`, outline border + label `var(--kentucky)`, email link `var(--kentucky)`.
- assets: none
- motion: hover fill-sweep on buttons.
- mobile: one column, buttons full width.
- done-when: both buttons and the email link work, the Text button shows the number, and the heading fits on ≤ 2 lines at 1440px.

### 15. id: about-hero

- page: `about.html` (first section inside `<main id="main">`)
- format: hero, opener: kicker+h2
- layout: full-width `.field`, mirrored from `home-hero`: portrait in cols 1–5 (4:5) extending `var(--overlap)` below the field into the white section under it; text in cols 7–12, vertically centred, top padding ≤ 6rem. Field min-height `min(70vh, 680px)`.
- copy:
  - eyebrow: "Founder, ATLAS LAW"
  - h1: "Matthew Atlas"
  - subtext: "Admitted in New Jersey and New York. Over 15 years as in-house counsel."
  - CTAs: solid white "Email Matt" (mailto) and outline-white "Text 917-213-4979" (sms)
- palette: bg `var(--field)`, h1 `var(--white)`, eyebrow + subtext `var(--on-blue-muted)`, solid CTA bg `var(--white)` label `var(--kentucky)`, outline border + label `var(--white)`.
- assets: `assets/matt-formal.webp` (real client photo), `alt="Matthew Atlas"`, `width="800" height="1000"`, `fetchpriority="high"`. Crop/resize only.
- motion: clip-wipe (media, top-down) on the portrait.
- mobile: text first, then the portrait at 78% width, left-aligned, overlapping 48px into the next section.
- done-when: name, admissions line and both CTAs show without scrolling at 1440px, and the portrait crosses the field edge.

### 16. id: about-bio

- page: `about.html`
- format: editorial-column, opener: bare-h2
- layout: white ground, `padding-top:calc(var(--overlap) + var(--space-block))` so nothing starts under the hero portrait's overhang; one text column `var(--measure)` in cols 6–12. No photo in this section (the casual photo lives on Home only).
- copy:
  - h2: "From the client side to my own firm"
  - p: "I've spent over 15 years as in-house counsel at JPMorgan Chase, Colgate-Palmolive, Saks Fifth Avenue and Related. That experience lets me understand the client side well."
  - p: "I've been back in private practice since September 2025 and opened ATLAS LAW in September 2026. I advise companies on contracts, employment, disputes and real estate, and work as fractional general counsel for businesses without a legal department."
  - p: "I run ATLAS LAW as an AI-based firm. AI tools help me work efficiently, and the legal work and the judgment calls stay with me."
- palette: bg `var(--white)`, h2 + body `var(--ink)`.
- assets: none
- motion: none
- mobile: text full width, `padding-top:calc(48px + var(--space-block))`.
- done-when: three paragraphs under the heading (the third is the AI paragraph), no photo, and no text sits under the hero portrait's overhang at 1440px or 375px.

### 17. id: about-background

- page: `about.html`
- format: table, opener: side-label
- layout: `var(--mist)` ground; h2 as a rotated side-label in the left margin (desktop); a two-column definition list (`<dl>`) in cols 3–11: label column 30%, value column 70%, each row separated by a 1px `var(--rule)` line.
- copy:
  - h2 (side-label): "Background"
  - rows (`<dt>` / `<dd>`):
    - "Admitted" / "New Jersey · New York"
    - "Law school" / "University of Virginia"
    - "Companies" / "JPMorgan Chase · Colgate-Palmolive · Saks Fifth Avenue · Related"
    - "Private practice" / "Since September 2025"
    - "ATLAS LAW" / "Founded September 2026"
    - "Based in" / "New Jersey and New York"
    - "Clients" / "Businesses, wherever they're based"
    - "How I work" / "AI-assisted. I do the legal work."
    - "Fees" / "Alternative fee arrangements, including fixed fee and subscription"
    - "Contact" / "matt@matlas-law.com · Text 917-213-4979" (both linked: mailto, sms)
- palette: bg `var(--mist)`, side-label `var(--kentucky)`, `<dt>` `var(--slate)` in `var(--font-display)` small caps-style label, `<dd>` `var(--ink)` in `var(--font-body)`, row lines `var(--rule)`, links `var(--kentucky)`.
- assets: none
- motion: none
- mobile: side-label becomes a horizontal label; each row stacks label over value.
- done-when: ten rows render as a real `<dl>`, values exactly as written above.

### 18. id: about-contact

- page: `about.html` (last section before the footer)
- format: cta-band, opener: bare-h2
- layout: `var(--white)` band with a 1px `var(--rule)` top border (it follows a mist section), h2 + line cols 1–7, buttons + email link cols 8–12.
- copy:
  - h2: "Email or text me directly"
  - p: "Messages go straight to me."
  - detail (plain text link): "matt@matlas-law.com" (mailto)
  - buttons: solid "Email Matt" (mailto) and outline "Text 917-213-4979" (sms)
- palette: bg `var(--white)`, h2 `var(--ink)`, p `var(--slate)`, solid button bg `var(--kentucky)` label `var(--white)`, outline border + label `var(--kentucky)`, email link `var(--kentucky)`.
- assets: none
- motion: hover fill-sweep on buttons.
- mobile: one column, buttons full width.
- done-when: both buttons and the email link work, and the Text button shows the number.

## Build checks the sheet already expects to pass

- Text buttons: every Text button except the compact < 820px header button reads "Text 917-213-4979", at every width, because `sms:` links do nothing on most desktops.
- Per page section counts: Home 7 sections / 7 families / kickers 2 (budget 3); Practice areas 7 / 7 / kickers 1 (budget 3); About 4 / 4 / kickers 2 (budget 2). No family or opener repeats back to back on any page.
- `copycheck.py` + `aitells.py` on all three pages; watch list caps from `voice-spec.md` (`in-house` ≤ 2 per page; `AI` ≤ 3 per page).
- Detector on all three pages; JS-off test; no Google Fonts or CDN requests.
