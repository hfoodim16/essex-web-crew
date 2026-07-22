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

| Stage | Owner | Model | Output |
|---|---|---|---|
| 1. Scout candidates (10–15) | `scout` | Sonnet | `pipeline/candidates.md` |
| 2. Score + research finalists | `analyst` | Opus | `prospects/<slug>/dossier.md` + shortlist message to lead |
| 3. **Approval pause** | lead ↔ Harry | — | Harry confirms/swaps the 3 |
| 4. Website plan (1 per prospect) | `planner` | Fable | `prospects/<slug>/website-plan.md` |
| 5. Build mockups (1 per prospect) | `builder` ×3 | Opus | `prospects/<slug>/mockup/` |
| 6. Outreach (email or call script) | `copywriter` | Sonnet | `prospects/<slug>/outreach-email.md` (email found) or `outreach-call.md` (no email) |
| 7. Critique loop | `critic` | Opus | `prospects/<slug>/audit.md` (written every round) + fix messages, sign-off to lead |

`<slug>` = kebab-case business name, e.g. `montclair-stone-masonry`.

**Division of design labor:** the `planner` (Fable) makes ALL the design decisions —
art direction, fonts, palette, page map, per-section layout — and writes them to
`website-plan.md`. The `builder` (Opus) IMPLEMENTS that plan and does not re-decide the
design. Copywriter can run in parallel with planner/builders once prospects are approved.

## Per-prospect output contract

Each approved prospect gets a folder `prospects/<slug>/` containing:

- `dossier.md` — research + a page map + a "why this client is winnable" pitch.
- `website-plan.md` — the Planner's design brief the Builder implements.
- `mockup/` — `index.html`, `style.css`, `main.js` (+ extra `.html` pages if the
  page map calls for them). Static only. Opens by double-click, no build step.
- `screenshots/` — desktop + mobile captures proving the QA passes ran.
- `outreach-email.md` — the personalized email draft (with `To:`/`mailto:` link) + a
  short pitch one-pager. Written **only when the dossier has a real email address**.
- `outreach-call.md` — written **instead** when no email was found: the phone number
  (`tel:` link) + a spoken call script + prepared responses so Harry is ready to call.
- `audit.md` — the Critic's scored $10K Checklist result (8/8 or documented exceptions).

## The Mockup Recipe (the "Corey Blake workflow")

This is our house method, distilled from a real build
(`~/Claude Code/corey-blakes-steakhouse/`). Builders MUST follow it.

### PRIMARY design skill: `web-design-ultra`

The **`web-design-ultra`** skill (`~/.claude/skills/web-design-ultra/SKILL.md`) is the
team's primary design skill — every mockup runs through its 8-stage art-direction
pipeline. The recipe steps below execute *inside* that pipeline. How the stages map to
the team:

- **Stages 1–5 → Planner.** Brief (from the dossier) → design intelligence
  (`ui-ux-pro-max` search engine + the industry's conventional palette) → real-site
  inspiration (3–5 references, extract patterns never copy) → anti-repetition check
  (read the skill's `data/design-memory.md`) → **three genuinely divergent directions**,
  pick the boldest. All recorded in `website-plan.md`.
- **Stage 6 → runs, capped.** Builders generate **up to 3 real AI images per mockup**
  (hero + the two highest-impact slots the Planner marked `GENERATE`) via `ai-multimodal`
  + the skill's `references/imagery.md` photorealism kit; every slot beyond 3 stays a
  labeled AI-IMAGE placeholder (see Image policy). ALSO layer the skill's free CSS craft:
  `references/backgrounds.md` (background/texture/depth) and `references/atmosphere.md`
  (animated fog, god rays, shimmer, motes — reduced-motion gated). Real imagery + real
  depth.
- **Stage 7 → Builder.** Implement the chosen direction with the skill's craft
  discipline: distinctive type (never the generic four), whole palette as CSS
  variables, deliberate spatial composition (asymmetry, overlap, scale contrast),
  motion via CSS/anime.js.
- **Stage 8 → Builder self-check, then Critic.** Screenshot desktop + mobile, score the
  10-dimension rubric in the skill's `references/critique.md`. Gate: **no dimension
  below 7, boldness ≥ 8** — enforced by the Critic alongside the $10K Checklist.
- **Anti-repetition:** consecutive prospects must not share a font pairing, palette
  family, or layout archetype. After a prospect's sign-off, its builder appends the
  choices (font pairing, palette, layout archetype, background system) to the skill's
  `data/design-memory.md` so the next run diverges.

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

The critic writes `prospects/<slug>/audit.md` after **every** review round (NEEDS-WORK
versions included, with a `Review round: N` line), not only at sign-off. Anything below
8/8 (barring a documented exception) goes back to the builder and the loop repeats. After
the first full audit, re-reviews are **incremental** — the critic re-checks only the
failed items and the sections the builder's change report says changed (plus a spot-check
if a fix could ripple), not the whole site again.

**Sign-off freezes a prospect.** The moment a mockup hits 8/8, it is FINAL: its builder
stops and its files never change again, and the critic never reopens it or sends more
fixes. Only prospects that have NOT yet passed stay in the loop. The lead engages a
builder only for a prospect with an open critic fix list; a signed-off mockup is reopened
only if Harry explicitly asks. This keeps already-approved sites from being disturbed
while the others are still being fixed.

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

**Tiered: 3 real AI images per mockup, placeholders beyond.**

- **Builders generate up to 3 AI images per mockup — HARD CAP.** Use the
  `ai-multimodal` skill (Gemini, ~$0.04/image ≈ $0.12/prospect — pre-approved by Harry
  at this cap; NEVER exceed 3 without the lead asking Harry first).
- **Priority order: the hero first**, then the two next most visible slots — the
  Planner marks these three as `GENERATE` in the plan's image list.
- **Quality bar:** follow the photorealism kit in
  `~/.claude/skills/web-design-ultra/references/imagery.md` — maximally photorealistic,
  on-art-direction, no obvious AI tells. Optimize to WebP at correct display size,
  store in `prospects/<slug>/mockup/assets/`, reference locally (never hotlink).
- **Every slot beyond the 3 stays a labeled AI-IMAGE placeholder:**

```html
<!-- AI-IMAGE: wide drone shot of a finished bluestone paver patio at golden hour -->
<div class="img-placeholder" role="img" aria-label="Finished bluestone paver patio">
  <span>AI-IMAGE — paver patio, golden hour</span>
</div>
```

Style `.img-placeholder` as a labeled block in the art direction's colors so the
mockup still reads well. Harry generates the remaining images from these prompts before
anything goes to a client (PLAYBOOK Part 3 Reference A). Still banned always: stock
photos, Unsplash/Google image URLs, hotlinked or copyrighted images.

**The ONE exception — the client's own logo.** If the business's existing site (or
Facebook / Google Business profile) shows a logo, the mockup must use **that exact
logo** — it's their brand, and the whole pitch is "your site, done right." The Analyst
records the logo's direct image URL in the dossier; the Builder downloads the actual
file into `prospects/<slug>/mockup/assets/` and places it in the header/nav (top-left,
where a logo belongs) with proper alt text (`alt="<Business Name> logo"`). Serve it as a
**local file — never hotlink it**, never redraw or "improve" it, and never substitute a
styled text wordmark when a real logo exists. Only if no logo exists anywhere is a
tasteful text wordmark in the display font the right call.

## Content honesty (hard rule)

Do not fabricate facts about a real business — no invented awards, fake years in
business, made-up review counts, or fictional staff. If a detail isn't in the dossier,
write around it or use an obvious placeholder (`[years in business]`). The mockup is a
design demonstration, not a claim of fact.

**Information currency (hard rule).** The mockup must reflect the business **as it is
today**, not as an old source describes it. When sources conflict, the business's own
most recent statement wins — its current website or a Google Business post outranks stale
directory listings, LinkedIn, or aggregators. A change the business itself has announced
(new ownership, a new name, a moved address, a dropped service) is a **current fact**, not
a "discrepancy" to hedge around: put it on the site honestly (e.g. "founded 30+ years ago
by X, now owned by Y"), don't render the outdated version as if nothing changed. Only fall
back to `[verify]` when the business itself hasn't made the current state clear anywhere.

**Real reviews only (hard rule).** A testimonial or review appears on a mockup ONLY if
it is a **real review the Analyst actually found and captured** in the dossier —
verbatim quote + reviewer first name + source platform (Google / Yelp / Facebook /
Angi). **Never write a testimonial for the demo, never paraphrase a review into
something nicer, never invent a reviewer.** If the dossier has no real reviews, the
mockup has **no testimonial section** — or, if the layout needs one, a clearly-labeled
`[Real review goes here — none captured yet]` placeholder block, never fabricated
praise. This is the review-specific case of the broader rule: **do not make up any
information** about the business — reviews, awards, stats, staff, history, or anything
else.

## Use the client's real content (hard rule)

Most prospects already have a website — that's what we're improving on. When they do,
**reuse their real content, don't invent new content.** The Analyst captures the existing
site's actual services, descriptions, service area, hours, contact info, tagline, about
text, and testimonials into the dossier; the Planner structures that real material and
the Builder renders it. We are upgrading the **design and structure**, not rewriting the
business. Only use `[placeholder]` text where information genuinely doesn't exist. This
also keeps the pitch honest and makes the mockup feel like *their* site, done right.

## Skills each agent uses

Skills are NOT auto-loaded for teammates (the agent-teams runtime doesn't apply the
`skills` frontmatter field) — each agent must invoke them itself via the Skill tool, and
each agent's `tools` list includes `Skill`.

| Agent | Skills to invoke | Why |
|---|---|---|
| `scout` | `research`, `docs-seeker` | Deeper competitor/reputation research when a web search isn't enough; finding directories/docs on unfamiliar trades. |
| `analyst` | `research` | Comprehensive dossier research beyond a plain web search. |
| `planner` | **`web-design-ultra` (PRIMARY)**, `ui-ux-pro-max`, `frontend-design`, `design-system`, `aesthetic`, `sequential-thinking` | Run the 8-stage art-direction pipeline (Stages 1–5): design intelligence, real-site inspiration, anti-repetition, three divergent directions. Supporting skills ground palette/type/token choices. |
| `builder` | **`web-design-ultra` (PRIMARY)**, `ai-multimodal`, `ui-ux-pro-max`, `frontend-design`, `frontend-development`, `web-frameworks` | Execute the chosen direction (Stage 7): generate the 3 real hero/priority images (`ai-multimodal`), craft discipline + backgrounds/atmosphere recipes; self-score the Stage 8 rubric. |
| `copywriter` | `humanizer`, `brand`, `sequential-thinking` | Make the email read human, not AI-generated; keep tone-of-voice consistent; structure persuasion flow. |
| `critic` | **`web-design-ultra`**, `ui-ux-pro-max`, `code-review`, `design-system` | Audit each mockup against the Stage 8 10-dimension rubric AND the $10K Checklist; enforce real-reviews-only; code-quality + design-system rigor. |

Optional, invoke only if the situation calls for it: `media-processing` (Builder — if
processing real images pulled from an existing client site) and `ai-multimodal`
(Analyst — if extracting content from screenshots of an existing site's design).

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
