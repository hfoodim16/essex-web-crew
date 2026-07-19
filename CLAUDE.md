# Essex Web Crew — Project Playbook

> This file is read automatically by every teammate. It is the shared source of
> truth. If a spawn prompt and this file disagree, this file wins unless the
> lead says otherwise.

## Mission

We are a mini web agency run as a Claude Code **agent team**. Each run we:

1. **Scout** Essex County, NJ trade businesses that need a website.
2. **Score** them and pick a top 3.
3. **Pause** and let Harry approve the shortlist.
4. **Build** a full, review-ready pitch package for each approved prospect:
   a research dossier, a working website mockup, and a personalized outreach email.

Everything lands on disk for Harry to review. **We never contact a business.**
Harry generates the real images and sends the outreach himself.

## Territory & target

- **Where:** Essex County, NJ (Newark, Montclair, Bloomfield, Nutley, Belleville,
  West Orange, Livingston, Cedar Grove, Verona, Caldwell, the Oranges, etc.).
- **Niches:** **lead with tree service, lawn care, and small landscapers** — a real
  scouting run showed these are full of owner-operators on a Facebook page, a dead
  domain, or a 2000s-era site (exactly our target). **Largely skip masonry, paving, and
  fencing** unless a specific listing shows a weak/absent site — those trades here have
  mostly bought modern template sites and filter out fast. Also fair game: any local
  service business whose website is naturally **low-maintenance / static** — no weekly
  menus, no e-commerce, no booking engine required. "Build once, barely touch it" sites
  are the kind we want to sell.
- **Portfolio anchor:** Cecere Brothers Landscaping (Harry's existing client) — use
  it as the credibility reference in pitches.

## Qualification rules (a business must pass ALL of these)

1. **Weak web presence:** EITHER no website at all (just Google Business / Facebook /
   Instagram), OR an outdated / broken / non-mobile-friendly website.
2. **Established:** clear signs it has operated for several years (founding year,
   review history, "since 20XX", established social presence). We are not pitching
   brand-new side hustles.
3. **Reachable:** a findable owner name, phone, email, or contact form.

Good reviews are a **bonus** (higher score), not a requirement.

## Pipeline stages & ownership

| Stage | Owner | Output |
|---|---|---|
| 1. Scout candidates (10–15) | `scout` | `pipeline/candidates.md` |
| 2. Score + research finalists | `analyst` | `prospects/<slug>/dossier.md` + shortlist message to lead |
| 3. **Approval pause** | lead ↔ Harry | Harry confirms/swaps the 3 |
| 4. Build mockups (1 per prospect) | `builder` ×3 | `prospects/<slug>/mockup/` |
| 5. Outreach email + one-pager | `copywriter` | `prospects/<slug>/outreach-email.md` |
| 6. Critique loop | `critic` | scored audit + fix messages, sign-off to lead |

`<slug>` = kebab-case business name, e.g. `montclair-stone-masonry`.

## Per-prospect output contract

Each approved prospect gets a folder `prospects/<slug>/` containing:

- `dossier.md` — research + a page map + a "why this client is winnable" pitch.
- `mockup/` — `index.html`, `style.css`, `main.js` (+ extra `.html` pages if the
  page map calls for them). Static only. Opens by double-click, no build step.
- `screenshots/` — desktop + mobile captures proving the QA passes ran.
- `outreach-email.md` — the personalized email draft + a short pitch one-pager.
- `audit.md` — the Critic's scored $10K Checklist result (8/8 or documented exceptions).

## The Mockup Recipe (the "Corey Blake workflow")

This is our house method, distilled from a real build
(`~/Claude Code/corey-blakes-steakhouse/`). Builders MUST follow it.

### Step 1 — Design brief before any code
Commit to a **named art direction** that fits the trade (e.g. "earthy editorial"
for a landscaper, "dark-luxury stone" for a high-end mason, "clean industrial" for
concrete/fencing). Write 2–3 sentences of rationale at the top of `style.css`.
Then lock:
- **Font pairing** — a display face + a body face from Google Fonts.
  **Never Inter or Roboto.** (Corey Blake used Cormorant + Montserrat.)
- **Palette** — 3 to 5 colors as CSS custom properties in `:root`. Restraint signals
  premium. (See the token block pattern below.)

### Step 2 — Build
- **Structure:** single-file SPA. `index.html` holds all "pages" as
  `<main class="page" id="page-home">` sections; nav uses `data-page="…"` links and
  `main.js` toggles the `.active` page. (Multi-file only if the page map is large.)
- **Design tokens** in `:root` — colors, fonts, easing curves, `--nav-h`, `--radius`,
  `--container`. Everything references the tokens; no hardcoded hex in components.
- **Semantic HTML** — real `<header> <nav> <main> <section> <footer>`, `aria-label`s,
  `role="list"`, a visible focus ring (`:focus-visible` outline).
- **Meta:** full `<title>`, meta description, Open Graph tags, Twitter card, and an
  inline SVG favicon. (Use the business's real name + town.)
- **Motion (whisper, don't shout):** reveal-on-scroll via IntersectionObserver,
  a custom cursor (dot + lerped ring with contextual labels), magnetic buttons,
  subtle 3D card tilt. **Every motion effect must be gated behind**
  `window.matchMedia('(prefers-reduced-motion: reduce)')` and disabled on
  `(pointer: coarse)` where relevant.
- **Embeds as placeholders** — contact form, Google Map, booking widget: leave a
  clearly styled placeholder block + an HTML comment saying what goes there. Do not
  wire up real third-party services.

### Step 3 — Desktop QA loop
Open in the browser pane. Go section by section: `read_page` / screenshot, fix what
looks wrong, re-check. Don't move on from a broken section.

### Step 4 — Mobile pass (this is where cheap sites die)
Resize to iPhone (375×812). Audit **every** section. Make real phone-layout
DECISIONS, not a shrunk desktop: stacked full-width CTAs, tightened hero that fits
one screen, horizontally-scrollable tab rows, reduced section padding, adjusted image
aspect ratios, hamburger menu. Save proof screenshots.

### Step 5 — The $10K Checklist audit (Critic runs this; Builder self-checks first)
Score all 8, fix gaps, re-verify. Source: Metics Media Field Guide No. 01.

1. **Point of view, not a template** — commits to a specific direction with taste.
2. **Typography that does work** — paired display + body, not defaulted, not Inter/Roboto.
3. **Restrained color system** — 3–5 colors, used consistently.
4. **Hierarchy that breathes** — whitespace, scale, contrast guide the eye.
5. **Imagery with intent** — here: every image slot is a deliberate, labeled
   AI-IMAGE placeholder matching the art direction (see below). No stock defaults.
6. **Motion that whispers** — hand-crafted micro-interactions, reduced-motion-safe.
7. **Mobile that's designed, not shrunk** — distinct phone layout decisions.
8. **The invisible expensive stuff** — sub-2s load (compress/omit heavy assets),
   WCAG AA contrast, keyboard navigation, semantic HTML, real meta tags.

### Step 6 — Proof
Save desktop + mobile screenshots to `prospects/<slug>/screenshots/`.

## Image policy (hard rule)

The team **never generates or hotlinks images**. Every image slot is a placeholder:

```html
<!-- AI-IMAGE: wide drone shot of a finished bluestone paver patio at golden hour -->
<div class="img-placeholder" role="img" aria-label="Finished bluestone paver patio">
  <span>AI-IMAGE — paver patio, golden hour</span>
</div>
```

Style `.img-placeholder` as a labeled block in the art direction's colors so the
mockup still reads well. Harry generates the real images from these prompts before
anything goes to a client. Never use Unsplash/Google image URLs or copyrighted photos.

## Content honesty (hard rule)

Do not fabricate facts about a real business — no invented awards, fake years in
business, made-up review counts, or fictional staff. If a detail isn't in the dossier,
write around it or use an obvious placeholder (`[years in business]`). The mockup is a
design demonstration, not a claim of fact.

## Tooling rules

- **Free tools first.** Use built-in `WebSearch` / `WebFetch` and the browser pane for
  all research and scraping. **Do NOT call Firecrawl or Perplexity** (they cost Harry
  money) — if a page genuinely can't be reached any other way, stop and ask the lead,
  who asks Harry.
- **Never contact a business.** No emails, no form submissions, no DMs, no calls.
  Drafts only.

## Token reminder

Every teammate is a full Claude instance (~7× cost of a solo session). Keep scope
tight, mark tasks complete promptly, and shut down when your work is signed off.
