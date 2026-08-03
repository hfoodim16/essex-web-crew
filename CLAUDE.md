# Essex Web Crew — Project Playbook

> This file is read automatically by every teammate. It is the shared source of
> truth. If a spawn prompt and this file disagree, this file wins unless the
> lead says otherwise.

## Mission — the ask-first model, two separate teams

We are a mini web agency run as Claude Code **agent teams**. Our business model is
**NOT** "build a site, show it to them, sell it." It is:

> **Find a client who may need a website → Harry reaches out → ASK what they want (the
> master questionnaire) → build FROM their answers → keep working with them until it's
> perfect.**

We never build speculative mockups and pitch them. The client's answers come first; the
build serves the answers. Because Harry's outreach and the client's reply happen on
human time (days), the work is split into **two independent teams** that never run
together:

- **Team 1 — Prospecting.** `scout` + `analyst` ONLY. The scout finds qualifying
  businesses; the analyst researches the top 3 and writes their dossiers. The run's
  final deliverable is **the shortlist with contact info** — then it ends. Nothing is
  built.
- **Harry, between the teams (no agents involved).** He contacts the prospects himself
  — call or email, his own words. Whoever says yes gets
  **`templates/Website-Questionnaire.docx`**, the standing client questionnaire that needs
  no run to produce. He collects their answers.
- **Team 2 — Build.** `planner` + `builder` + `critic`. Input is the client's answers.
  The planner plans FROM them, one builder builds, the critic gates it, and the
  finished site goes back to the client — then we iterate with them until it's right.

**We never contact a business.** All client contact is Harry personally; the teams only
produce research and websites.

## Territory & target

- **Where:** Essex County, NJ (Newark, Montclair, Bloomfield, Nutley, Belleville,
  West Orange, Livingston, Cedar Grove, Verona, Caldwell, the Oranges, etc.).
- **The real filter — a naturally static website, NOT an industry.** We target businesses
  whose site is **low-maintenance / static**: a brochure, not an app. "Build once, barely
  touch it" — no weekly menus, no e-commerce catalog, no booking engine, no
  constantly-changing content. **We are not limited to blue-collar trades.**
- **Lead niche (proven):** tree service, lawn care, and small landscapers — a real
  scouting run showed these are full of owner-operators on a Facebook page, a dead
  domain, or a 2000s-era site (exactly our target). **Largely skip masonry, paving, and
  fencing** unless a specific listing shows a weak/absent site — those trades here have
  mostly bought modern template sites and filter out fast.
- **Equally fair game beyond the trades:** accountants/CPAs, law offices, insurance
  agents, auto repair, cleaning services, pest control, movers, home inspectors,
  chiropractors/dentists, tutors/music teachers, photographers, funeral homes, vets.
  Professional offices often sit on a neglected 2000s-era site — prime targets.
- **Skip industries needing constant updates** (the opposite of what we sell):
  restaurants/cafés (menus), e-commerce/boutiques (inventory), event venues and gyms
  (schedules), news/blog-driven businesses.
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

### Team 1 — Prospecting run (`scout` + `analyst` only — nothing is built)

| Stage | Owner | Model | Output |
|---|---|---|---|
| P1. Scout candidates (10–12) | `scout` | Sonnet | `pipeline/candidates.md` |
| P2. Score, research the top 3, capture their sites | `analyst` | Opus | `prospects/<slug>/dossier.md` + `site-content.md` |
| P3. **Deliver the shortlist** (final output) | `analyst` → lead | Opus | Top 3 with winnability pitches **and contact info** |

**The run ends at the shortlist.** Never spawn a planner, builder, or critic in a
prospecting run — there is nothing to build yet.

### Between the teams — Harry (no agents)

Harry contacts the prospects himself, in his own words. Anyone who says yes gets
**`templates/Website-Questionnaire.docx`** — a standing, client-ready questionnaire
covering everything a build needs. It requires **no run to produce**: it's already
written and sits in the repo. Harry collects the answers and pastes them into the
Build run.

### Team 2 — Build run (`planner` + `builder` + `critic`)

| Stage | Owner | Model | Output |
|---|---|---|---|
| B0. Save the client's answers | lead | — | `prospects/<slug>/client-answers.md` |
| B0b. *(only if no dossier exists)* capture-only research | `analyst` | Opus | `dossier.md` + `site-content.md` for this ONE business |
| B1. Plan FROM the answers | `planner` | Fable | `prospects/<slug>/website-plan.md` incl. "Client answers → decisions" |
| B2. Build | `builder` ×1 | Opus | `prospects/<slug>/mockup/` + `screenshots/` |
| B3. Critique loop | `critic` | Opus | `prospects/<slug>/audit.md` (every round) + fix messages, sign-off |
| B3b. **Publish to Claude Design** | lead | — | A card-per-section design-system project at claude.ai/design (`/design-push`) |
| B3c. *(only if the site was edited in the Design pane)* **Pull those edits back** | lead | — | `/design-pull` → the edits land in `mockup/`, round-trip verified |
| B4. **Iterate with the client** | Harry ↔ client | — | Feedback → Harry reopens → builder revises → **re-run `/design-push`** |

**Client answers are the top authority.** The hierarchy, highest first:

1. **The client's questionnaire answers** (`client-answers.md`) — controlling.
2. The business's own current statements (their website, a Google Business post).
3. Directories and aggregators (Yelp, Manta, LinkedIn, YellowPages).

When the answers conflict with the old site's content or anything the Analyst inferred,
**the answers win** — it's their site and they just told us what they want. This binds
the Analyst too: in a Build run's capture-only mode it reads `client-answers.md` first, and its
dossier **supplements the answers rather than correcting them** — any difference between
an answer and a public source goes into a **"Confirm with client (optional)"** note for
Harry, never a `[verify]` blocker and never resolved in the old site's favor. Content
parity still applies to real content the answers didn't override (the questionnaire asks
what they want kept, changed, or dropped).

`<slug>` = kebab-case business name, e.g. `montclair-stone-masonry`.

**Division of design labor:** the `planner` (Fable) makes ALL the design decisions —
art direction, fonts, palette, page map, per-section layout — and writes them to
`website-plan.md`. The `builder` (Opus) IMPLEMENTS that plan and does not re-decide the
design.

## Speed rules — overlap the work, never lower the bar

Runs are slow because teammates WAIT on each other, not because the work is slow. Every
teammate follows these; none of them touch a quality gate.

1. **Stream your output downstream as soon as a unit is usable.** Don't sit on a finished
   batch waiting for the whole set — the scout messages the analyst every 5–6 verified
   candidates rather than delivering all 10–12 at the end; the planner hands its finished
   plan to the builder the moment it's done instead of polishing it further.
2. **Parallelize independent work.** The analyst researches all three finalists at once
   (one subagent each); the builder launches both image generations concurrently.
   **Delegated research must return verbatim quotes + source URLs (never summaries) and
   surface source contradictions rather than resolving them — and the analyst still
   verifies the load-bearing facts against primary sources itself.** Delegation speeds up
   discovery; it never replaces your own eyes on the source.
3. **Do prep work while blocked.** A builder waiting on its plan still reads the dossier,
   downloads the real logo, scaffolds folders, and starts its server — everything that
   doesn't depend on a design decision it isn't allowed to make.
4. **Review on arrival.** The critic audits the mockup the moment it's submitted, and
   turns each re-submission around as it arrives — the builder is blocked until the fix
   list lands.
5. **Don't gold-plate the search.** Time-box discovery work (the scout stops at ~12 solid
   candidates); depth per item stays the same. **A time-box never justifies
   under-delivering a required count** — the scout's floor is 10 qualifying candidates; a
   dry search means change angle, not stop. If a floor genuinely can't be met, say so
   explicitly rather than quietly shipping less.

**The hard limit:** speed comes ONLY from removing waiting and duplicate work. Never skip
a checklist item, shorten a review round, drop a QA pass, weaken the two-way imagery test,
or hand off something you know is failing. If a shortcut would change what ships, it isn't
one of these rules.

## Per-prospect output contract

Each approved prospect gets a folder `prospects/<slug>/` containing:

**From the Prospecting run:**
- `dossier.md` — research + a page map + a "why this client is winnable" pitch +
  the contact info Harry needs to reach out.
- `site-content.md` — the Analyst's page-by-page FULL-TEXT capture of the existing site
  (required whenever the prospect has one) — the content-parity source of truth.

*(The client questionnaire is NOT a per-prospect artifact — it's the standing
`templates/Website-Questionnaire.docx`, sent as-is to anyone who says yes.)*

**From the Build run (only after the client's answers are in):**
- `client-answers.md` — the client's answers, saved verbatim by the lead from Harry's
  paste. The top authority for everything downstream.
- `website-plan.md` — the Planner's design brief the Builder implements, including the
  **"Client answers → decisions"** section and the **content map** that places every
  site-content.md block (or lists it as deliberately dropped, with a reason).
- `voice-spec.md` — the Planner's copy-voice contract for this client, written via
  `trade-copy` Stage A from their answers, before any hero direction. It governs every
  visible string the Builder writes and is what the Critic's copy gate scores against; a
  missing one is a fail on the Planner.
- `mockup/` — `index.html`, `style.css`, `main.js` (+ extra `.html` pages if the
  page map calls for them, + `vendor/` if the plan's signature move needs the GSAP
  tier). Static only. Opens by double-click, no build step, **works offline** —
  libraries are vendored from the skill's `assets/gsap/`, never loaded from a CDN.
- `screenshots/` — desktop + mobile captures proving the QA passes ran.
- `release-form.pdf` (+ `release-form.html` source) — the Fora Digital **Website Release
  & Publication Approval**, pre-filled with this client's business name, contact, and the
  exact pages built. Harry sends it for signature when the client approves the site for
  launch. Generated by the Builder from `templates/release-form.html`; signature, date
  and checkbox fields stay blank, and unknown fields (domain, preview link) ship as clean
  blank lines rather than invented values.
- `audit.md` — the Critic's scored result for BOTH scoreboards ($10K Checklist 8/8 or
  documented exceptions, plus the 10-dimension rubric), rewritten every review round with
  a `Review round: N` line and a `Paid calls this prospect:` ledger line.

**Not a file in the folder, but part of the contract:** every signed-off prospect also has
a **Claude Design project** — its own card-per-section design system at claude.ai/design,
published by the lead with `/design-push`. That's where the site gets reviewed and precisely
edited before going live, so a signed-off prospect without one is incomplete.

## Delivery to Corey

Corey Rapkin (**crapkin@foradigital.com**) is the one who puts a site live via Netlify
Drop — he needs the packaged zip, not loose files.

**The Critic's sign-off means the BUILD is done. It does not mean "publish it."**
Delivery has its own gate, below.

**Only the lead session does this.** Teammates have no Gmail tools; the Critic signals
sign-off, the lead performs delivery. Harry can also trigger it any time with
"deliver `<slug>`".

Delivery sends a **zip for deploying**. That's separate from keeping the two Macs in sync
— for that, invoke **`github-push`** after a run finishes and **`github-pull`** before
starting one. A signed-off prospect should go up to GitHub as well as out as a zip, so
whoever picks it up next has the source.

**The procedure:**

0. **Check the signed release form FIRST — this is a hard gate.** Confirm with Harry that
   the client has returned a **signed** `release-form.pdf`. The Critic only verifies the
   form exists and is filled correctly; it cannot know whether the client signed it. No
   signature on file → **stop here.** Say what's missing and let the package wait. Nothing
   goes to Corey, because the next thing that happens to that zip is a real business's
   name, phone number, and address appearing on the public internet, and an AI score is
   not the client's permission to publish. A signed-off `audit.md` means the build is
   finished, never that it may go live.

1. Package the site:
   ```bash
   pipeline/package-site.sh <slug>
   ```
   This writes `prospects/<slug>/<slug>-site.zip` — the whole site, correctly named
   `index.html` at the top level, assets included, dev scratch stripped.

   **Then publish it to Claude Design** — invoke the `design-push` skill on
   `prospects/<slug>/mockup/` with the client's name. The finished site lands at
   claude.ai/design as a card-per-section design system you can refine visually.
   One DesignSync permission prompt per push; that's inherent to the tool and can't
   be automated away. **After a revision round, run `/design-push` again** — it writes
   the same paths, so the same project updates in place rather than duplicating.

   **It's a round trip, not a one-way publish.** The repo stays the source of truth and a
   re-push overwrites, so edits made *inside* Claude Design have to come back to the site
   first — that's **`/design-pull`**, which finds them on its own (it re-bundles the source
   and diffs, so nobody has to remember what they changed) and verifies every write-back by
   round-trip. `/design-push` refuses to run while unpulled edits exist, so refining a site
   in the Design pane can't silently cost you the work.

2. Create a Gmail draft with the Gmail MCP `create_draft` tool:
   - **to:** `crapkin@foradigital.com`
   - **subject:** `<Business Name> website — ready to put live on Netlify`
   - **body:** four lines, no fluff — which business this is, drag the attached zip onto
     https://app.netlify.com/drop, claim the site and rename the subdomain to
     `<slug>.netlify.app`, reply with the live URL.
   - **attachment:** if the zip is **≤ 200 KB**, attach it (`base64 -i <zip>`, mimeType
     `application/zip`). If it's larger, create the draft *without* the attachment and
     open the body with a line Harry can't miss:
     `ATTACH BEFORE SENDING: <absolute path to zip>`. Base64-ing a multi-MB file through
     a tool call is not workable — image-heavy sites will always take this path, and a
     mockup carrying a vendored GSAP tier (~45 KB zipped) may tip a borderline one over.

3. **Draft only — never send.** Report the draft ID and the zip path back to Harry, and
   say plainly whether the zip was attached or he has to attach it himself.

4. **When Corey replies with the live URL, register the site for monitoring.** Add it to
   `~/Projects/site-caretaker/sites.json` (the `caretaker` agent owns that file and its
   format — hand it the URL and let it do the write). This is the ONLY thing that puts a
   published site under the hourly uptime/DNS/TLS monitor. Skip it and the site is live,
   carrying a client's phone number, and watched by nobody. A delivery isn't finished at
   the draft — it's finished when the live URL is in the registry.

## The Mockup Recipe (the "DaSilva workflow")

This is our house method. The reference build is
**`prospects/paul-da-silva-law/`** — in-repo, so every teammate on either Mac can open it.
Builders MUST follow the recipe.

### PRIMARY design skill: `web-design-ultra`

The **`web-design-ultra`** skill (`~/.claude/skills/web-design-ultra/SKILL.md`) is the
team's primary design skill — every mockup runs through its 8-stage art-direction
pipeline. The recipe steps below execute *inside* that pipeline. How the stages map to
the team:

> **The mechanical gates are inside the skill now** — the crew gets them by running the
> pipeline, not from a separate tool. `references/critique.md` carries all three: the Step 0
> detector scan (60 deterministic rules, zero tokens, ~1s — Builder before handoff, Critic
> before any screenshot), the fail-visible measurement, and the countable composition checks.
> `references/craft-floor.md` is the build-time quality floor. `design-gates.md` (repo root)
> is now just a one-page map of where each gate lives and what stays crew-specific.
>
> **Both Impeccable and taste are in play, at opposite ends of the pipeline.**
>
> **Impeccable is the frontend audit engine.** It is the source of the detector, the nine
> craft references and the `impeccable-disable` waiver syntax, forked in and stripped of
> its native-platform material. Its job is auditing what got built: the Builder runs the
> scan across **every page** of the mockup before handoff, the Critic runs it first at
> Stage 8, plus the fail-visible measurement and the composition checks.
> `references/craft-floor.md` loads at Stage 7, immediately before UI edits. Impeccable
> never sets direction — a gate checks the build, it does not choose the design.
>
> **`design-taste-frontend` (taste) is a planning input.** The Planner invokes it for four
> sections only — §0 Brief Inference (the one-line **Design Read**, written into the
> plan), §0.D Anti-Default Discipline and §9 AI Tells (run the three directions against
> them at Stage 5), and §11 Redesign Protocol when an existing site is being replaced. Its
> stack picks, install commands, dials and block library are build-time material and are
> **not** used — that is the Builder's territory and `web-design-ultra` governs it.
>
> **The two rulebooks do disagree, so precedence is explicit:** client answers +
> `voice-spec.md` → `web-design-ultra` → taste. Taste's examples suggest **Geist**, which
> our banned-font list forbids, and its em-dash guidance differs from `trade-copy`'s. Take
> its reasoning, never its specific picks, wherever they collide with ours.
>
> Precedence is strict and runs one way:
>
> **client brief + `voice-spec.md` → `web-design-ultra` direction + `local-trade.md` → the gates.**
>
> A gate never overrules a direction the Planner locked for a real reason. This is not
> theoretical: the detector flags `cream-palette` and the skill's own premium-consumer palette
> ban points the same way, but a landscaper in earth tones or a mason in warm stone is
> *correctly* there, because our trades carry their own colour conventions. What's banned is
> *defaulting* there without deciding. Exceptions get stated in `website-plan.md` and waived
> in-file with a reason.

- **Stages 1–5 → Planner.** Brief (from the dossier) → design intelligence
  (`ui-ux-pro-max` search engine + the industry's conventional palette) → real-site
  inspiration (3–5 references, extract patterns never copy) → anti-repetition check
  (read this project's own `~/Projects/essex-web-crew/design-memory.md`, NOT the skill's global
  `data/design-memory.md` — the crew keeps its own ban list so prospects diverge from each
  other) → **three genuinely divergent directions**, pick the boldest. All recorded in
  `website-plan.md`.
- **Stage 6 → runs, capped.** Builders generate **up to 2 real AI images per mockup**
  (hero + the one highest-impact slot the Planner marked `GENERATE`) via the `/generate`
  skill on `nano-banana-2` + the skill's `references/imagery.md` photorealism kit; every
  slot beyond 2 stays a labeled AI-IMAGE placeholder (see Image policy). **Optionally one
  video clip — only after Harry approves it** (a marked `VIDEO` slot is a request, not an
  authorization), in its declared register: `filmed-action` ≤$1 or `designed-loop` ≤$2.50,
  ≤8s, never both; zero video is the norm (see Video policy). ALSO layer the skill's free CSS craft:
  `references/backgrounds.md` (background/texture/depth) and `references/atmosphere.md`
  (animated fog, god rays, shimmer, motes — reduced-motion gated). Real imagery + real
  depth.
- **Stage 7 → Builder.** Implement the chosen direction with the skill's craft
  discipline: distinctive type (never the generic four), whole palette as CSS
  variables, deliberate spatial composition (asymmetry, overlap, scale contrast),
  and the plan's named signature move from the skill's `references/motion.md`
  (GSAP 3.15 vendored to `mockup/vendor/` when the move needs it — `references/gsap.md`).
- **Stage 8 → Builder self-check, then Critic (Critic OWNS this stage).** Run it in the order
  the skill's `references/critique.md` gives. **First, Step 0 — the mechanical scan, before
  anything is served or screenshotted:**
  `node skills/web-design-ultra/scripts/detect.mjs prospects/<slug>/mockup/index.html`
  (60+ deterministic rules, no LLM, ~1s). **One-time setup on a fresh clone:**
  `cd skills/web-design-ultra/scripts/detector && npm install` — its parser packages are
  gitignored, and without them the engine falls back to a regex pass that catches almost
  nothing and still exits 0. It now prints a loud DETECTOR DEGRADED warning when that
  happens; if you ever see it, a clean result is not a passing gate.
  **The gate is the exit code — `exit 2`
  bounces** the build with the findings as the fix list; no review tokens are spent on a
  mockup that fails mechanically. Waivers only as in-file
  `<!-- impeccable-disable <rule> -- reason -->`.
  Then the **fail-visible measurement** in the pane the Critic already opens, **before**
  force-revealing anything for screenshots: above ~15% of page text hidden at rest is a fail.
  Then the countable **composition checks**. **Then** the visual review:
  screenshot desktop + mobile, score the 10-dimension rubric in the skill's
  `references/critique.md`. Gate: **no dimension below 7, boldness ≥ 8** — enforced by the
  Critic alongside the $10K Checklist. **On pass there are two duties, not one:** the Critic appends the
  design-choices row to `design-memory.md`, and the **lead publishes the site to Claude
  Design** with `/design-push` (the Critic can't — the DesignSync auth lives in the lead
  session, so it names it in the sign-off instead).
- **Local-service conversion patterns are house standard.** Our clients are local service
  businesses, so every plan and build applies the skill's `references/local-trade.md`:
  tap-to-call `tel:` link visible in the mobile header (CTA repeated top/mid/footer), one
  plain primary action, a service-area block with real town names, a trust strip
  (years / license / rating — real or clearly labeled placeholder), a project or
  before/after gallery, an estimate form of ≤ 4 fields, and a consistent NAP footer.
  A beautiful hero with no visible phone number is a failed build.
- **Imagery realism is judged, not assumed.** Generated images must pass the two-way test
  in the skill's `references/imagery.md`: *would the business proudly post this — and
  would a visitor believe they took it themselves?* Both the stock-ad "too perfect" look
  and the shabby/messy look FAIL. **No readable business names, lettering, or signage
  inside a generated image** (the model invents fake ones) — the client's real logo is
  composited into the markup instead. One imagery register per site.
- **Distinctiveness check (Critic, before sign-off).** A build run produces ONE site, so
  the risk is that it looks like the last few sites we built. With the mockup still
  unsigned, the Critic compares it against the **last 3 `design-memory.md` rows** (and the
  most recent signed prospect's hero screenshot when it's on disk), hunting the softer
  sameness the ban list misses — section rhythm, imagery register, motion vocabulary, a
  hero that's the same shot in different colors. Reads like a sibling → it goes back.
  Reading a frozen prospect's screenshots or log row is research, never a reopening.
- **Anti-repetition:** consecutive builds must not share a font pairing, palette
  family, or layout archetype. After a prospect's sign-off, **the Critic** appends the
  choices (font pairing, palette, layout archetype, background system) to this project's
  `~/Projects/essex-web-crew/design-memory.md` (the crew's own log, not the skill's global file) so the
  next client's site diverges.

### Step 1 — Design brief before any code (**the PLANNER's step**)
> The Planner makes these calls in `website-plan.md` (web-design-ultra Stages 1–5). The
> Builder implements them and does **not** re-decide them — see "Division of design
> labor" above.

The plan commits to a **named art direction** that fits the business (e.g. "earthy
editorial" for a landscaper, "dark-luxury stone" for a high-end mason, "clean industrial"
for concrete/fencing). The Builder writes those 2–3 sentences of rationale at the top of
`style.css`. The plan locks:
- **Font pairing** — a display face + a body face from Google Fonts.
  **Never Inter, Roboto, Arial, or Helvetica** — and the skill's banned set (`SKILL.md`
  non-negotiable 6) extends that to **Fraunces, Instrument Serif, Geist, Plus Jakarta Sans and
  Space Grotesk**, which are the same saturated-AI-default problem one generation later (we
  shipped Fraunces twice and Instrument Serif once before this was mechanical). The Step 0 scan
  flags all of them. A client's real brand font is a waiver with a reason, never a silent pass.
  (DaSilva used Libre Caslon Text + Albert Sans.)
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
- **Motion (whisper, don't shout):** build the **signature move the plan named** —
  one entrance family + one hover personality + at most one scroll set-piece + one
  tempo, from the skill's `references/motion.md`. Do not default to the old house
  recipe (IO reveal + custom cursor + magnetic + tilt); shipping the same four moves
  on every prospect is the sameness this checklist exists to kill, and it fails
  item 6. **Every motion effect must be gated behind**
  `window.matchMedia('(prefers-reduced-motion: reduce)')` and disabled on
  `(pointer: coarse)` where relevant. **Content is never hidden by JS** — the hidden
  state is applied at runtime, so a missing or broken script leaves a readable page
  (rename `main.js`, reload, read it: that's the test, and it has failed before).
- **Embeds as placeholders** — contact form, Google Map, booking widget: leave a
  clearly styled placeholder block + an HTML comment saying what goes there. Do not
  wire up real third-party services.

### Step 3 — Desktop QA loop
Open in the browser pane. Go section by section: `read_page` / screenshot, fix what
looks wrong, re-check. Don't move on from a broken section.

**Then click every interactive element** (hamburger open+close, every nav/card/CTA/
footer link on every page, every `#fragment`, the form submit). A **dead click** or a
**misleading affordance** — anything that looks clickable where only a small inner link
works — is a QA failure, and placeholder forms must show an inline demo confirmation
rather than a silent click or a disabled button. See "Interactive QA" in
`.claude/agents/builder.md`; the Critic click-tests this independently.

### Step 4 — Mobile pass (this is where cheap sites die)
Resize to iPhone (375×812). Audit **every** section. Make real phone-layout
DECISIONS, not a shrunk desktop: stacked full-width CTAs, tightened hero that fits
one screen, horizontally-scrollable tab rows, reduced section padding, adjusted image
aspect ratios, hamburger menu. Save proof screenshots.

### Step 5 — The $10K Checklist audit (Critic runs this; Builder self-checks first)
Score all 8, fix gaps, re-verify. Source: Metics Media Field Guide No. 01.

The critic writes `prospects/<slug>/audit.md` after **every** review round (NEEDS-WORK
versions included, with a `Review round: N` line), not only at sign-off, recording BOTH
scoreboards — headed by the one-line scan result (`Detector: N errors, M advisory`, plus
any waived rule and its reason). **The gate is both:** below 8/8 on the $10K Checklist
(barring a documented exception) OR any rubric dimension below 7 / boldness below 8 sends it
back to the builder and the loop repeats. A non-zero Step 0 exit short-circuits all of it —
the build goes back before it is ever screenshotted. After
the first full audit, re-reviews are **incremental** — the critic re-checks only the
failed items and the sections the builder's change report says changed (plus a spot-check
if a fix could ripple), not the whole site again.

**The loop is capped at 3 fix rounds.** If round 3 is still NEEDS-WORK, the critic does
not send a fourth fix list — it marks `audit.md` `STALLED — escalated to lead, round 3`
and hands the lead a stalemate report (what still fails, what was already sent, why it
isn't converging, and the options: documented exception, re-scope, or park). Harry
decides from there. The cap moves the decision to a human; it never lowers the bar, and a
capped-out mockup is not signed off and does not go to delivery. Details in
`.claude/agents/critic.md`.

**Sign-off freezes a prospect.** The moment a mockup clears BOTH gates (8/8 $10K **and**
no rubric dimension below 7 with boldness ≥ 8), it is FINAL: its builder
stops and its files never change again, and the critic never reopens it or sends more
fixes. Only prospects that have NOT yet passed stay in the loop. The lead engages a
builder only for a prospect with an open critic fix list; a signed-off mockup is reopened
only if Harry explicitly asks. This keeps already-approved sites from being disturbed
while the others are still being fixed.

1. **Point of view, not a template** — commits to a specific direction with taste.
2. **Typography that does work** — paired display + body, not defaulted, not Inter/Roboto.
3. **Restrained color system** — 3–5 colors, used consistently.
4. **Hierarchy that breathes** — whitespace, scale, contrast guide the eye.
5. **Imagery with intent** — the 2 Planner-marked `GENERATE` slots (hero + one priority
   slot) hold REAL generated images passing the two-way realism test; every other slot is
   a deliberate, labeled AI-IMAGE placeholder matching the art direction (see the Image
   policy below). A placeholder in either priority slot is never an acceptable exception.
   No stock defaults.
6. **Motion that whispers** — art-directed micro-interactions, reduced-motion-safe.
   **Signature move required:** one entrance family + one hover personality picked from
   the skill's `references/motion.md`, and **distinct from the last 3 prospects** in
   `./design-memory.md`. The default trio (fade-up everywhere + staggered text delay +
   number count-up) fails this item unless explicitly justified. GSAP (vendored, per
   `references/gsap.md`) is sanctioned when the move needs it — what's judged here is
   whether the motion was *chosen*, not whether it was typed by hand.
7. **Mobile that's designed, not shrunk** — distinct phone layout decisions.
8. **The invisible expensive stuff** — sub-2s load (compress/omit heavy assets),
   WCAG AA contrast, keyboard navigation, semantic HTML, real meta tags.
   **JS-off test:** rename `main.js` (and `vendor/*.js`), reload — every word readable,
   every CTA tappable. Content hidden by default and revealed only by JS is an
   automatic fail: the site ships as a zip someone else unpacks, so one missing
   script is a blank homepage. (This has happened; see `fora-digital/audit.md`.)
   **Local SEO:** `LocalBusiness` JSON-LD present (correct schema subtype), meta
   title/description naming the service + towns, OG image, canonical, favicon. The
   footer NAP must match the JSON-LD exactly. Unknown values stay as visible
   `PLACEHOLDER_…` tokens — **fabricated NAP/license/hours is an automatic fail.**

### Step 6 — Proof
Save desktop + mobile screenshots to `prospects/<slug>/screenshots/`.

## The anti-slop standard (all three Build agents)

AI slop = the statistical mean: hero, three feature cards, testimonials, CTA, one
section shape repeated, vague copy. It's a **direction failure, not a creativity
failure** — absent constraint, output regresses to the default. Seven levers kill it;
each has an owner and most are mechanically enforced:

| # | Lever | Owner | Enforced by |
|---|-------|-------|-------------|
| 1 | Named art direction before building | Planner | direction brief (Stage 5) + taste §0 **Design Read** |
| 2 | Banned defaults (fonts, purple-gradient, card-wall) | Builder | detector blocking rules |
| 3 | Section-format variety | Planner assigns, Builder obeys | `section-shape-repetition` + `repeated-section-kickers` (blocking) + critic counts |
| 4 | Deliberate symmetry break | Planner names device, Builder lands it | critic composition check (screenshot) |
| 5 | Scale contrast as hierarchy | Builder | `flat-type-hierarchy` (blocking, ≥1.25 step ratio) |
| 6 | Copy specificity — ≥1 falsifiable fact, no abstract-pair labels | Builder (trade-copy + web-humanizer) | `copycheck.py` + `aitells.py` exit 0 |
| 7 | Real assets — real logo, real photos or labeled placeholders, never stock | Builder | critic imagery gate |
| 8 | Plan lint — quotas and required fields checked before a line is built | Planner | `plan-lint.mjs` exit 0 before handoff |

Process levers that keep builds from converging on each other: evidence before design
(Stage 3), three forced-divergent directions (Stage 5), the anti-repetition log
(`design-memory.md`, Stage 4/8), deterministic detection (Step 0 scan), and the
screenshot rubric (Stage 8). **A build that ships with any lever unaddressed is not
done** — the critic's audit records where each one landed.

## The `Inspiration/` library

`~/Projects/essex-web-crew/Inspiration/` is Harry's curated reference folder. The Planner
**checks it first at Stage 3**, before opening the browser — but it supplements live-site
research, it never replaces it. Filenames are content hashes, so identify images by
looking at them. Two kinds, two uses:

- **Site mockups / screenshots** → design references. Dissect them like any live site and
  fill an evidence sheet. Extract patterns, never clone.
- **Photography** (trade work, machinery, landscape) → art-direction reference for the
  register of a shot (lighting, camera height, grit level), and a permitted
  **image-to-video seed frame**.

**Transformation rule (hard).** These are collected references, not licensed stock.
Describing their style in a prompt is always fine. Seeding an image-to-video shot from one
is allowed **only if the plan named the file**, and the output must be a *new shot the
reference informed* — not that photograph with motion added. An image from this folder is
**never shipped as a still**, and never used for a logo or a real person's likeness. The
Critic compares any clip against its named source.

## Image policy (hard rule)

**Tiered: 2 real AI images per mockup, placeholders beyond.**

- **Builders generate up to 2 AI images per mockup — HARD CAP.** Use the **`/generate`
  skill** on **`nano-banana-2`** (Google Gemini 3.1 Flash Image, via Kie AI) — say the
  model explicitly, because `/generate`'s default `-lite` is a draft tier and is not
  acceptable for a client-facing image. Priced by resolution: **~$0.04 at 1K, ~$0.06 at
  2K.** Per-prospect ≈ $0.08 (both 1K) to $0.12 (both 2K); typical one-2K-hero-plus-one-1K
  ≈ $0.10. Pre-approved by Harry at the 2-image cap; NEVER exceed 2 without the lead
  asking Harry first.
- **Priority order: the hero first**, then the one next most visible slot — the
  Planner marks these two as `GENERATE` in the plan's image list.
- **The Planner sizes each GENERATE slot** (see the plan-spec below): aspect ratio +
  resolution tier + where it renders. Rule of thumb: **full-bleed / background hero → `2K`;
  contained cards, plates, split-hero, OG → `1K`** (see the "Fit the slot" section of
  `imagery.md`). The Builder passes `aspect_ratio` and `resolution` accordingly.
- **Quality bar — "proud contractor" register is the DEFAULT for trades.** Follow the
  photorealism kit in `~/.claude/skills/web-design-ultra/references/imagery.md`. The bar is
  the **best photo on the business's Google Business profile**: **flawless finished work**
  (crisp stripes, clean edges, spotless install — nothing sloppy, no clippings/tools left
  out) at an **attractive property** (good curb appeal, nice home), shot **casually but
  flatteringly** in pleasant natural light. Two-way test: *would they proudly post it, AND
  would a visitor believe they took it?* **Both fail modes are rejects** — "too perfect /
  stock-ad" (reads fake) AND "too shabby / mediocre" (believable but not worth showing).
  **One register across the whole mockup** (hero + all slots), set by the Planner — never
  mix. Editorial (pro-shoot look) is opt-in with the Planner's justification.
  **No fabricated branding:** generated images must show no readable business name/logo —
  the model invents fake or competitor names (a truck lettered with the wrong brand). Keep
  vehicles/signs unbranded, angled, or out of frame; composite the prospect's REAL name/logo
  in the build if a branded truck or sign is wanted. Optimize to
  WebP, **downscaling to the real display width** (never ship a 2K file into a small slot),
  store in `prospects/<slug>/mockup/assets/`, reference locally (never hotlink).
- **Every slot beyond the 2 stays a labeled AI-IMAGE placeholder** (this is the norm — most image slots ship as marked placeholders for the client to fill with real job photos)**:**

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

## Video policy (hard rule)

**Default is zero video.** Stills plus the free CSS/GSAP motion tiers carry almost every
mockup, and a clip-free build is never a deduction. **Unlike images, video is NEVER
pre-approved** — the Planner may *request* a clip, but Harry approves each one
individually before the Builder spends anything. Full framework:
`~/.claude/skills/web-design-ultra/references/video.md`.

All generation — images and video alike — runs through the **`/generate` skill**
(`~/.claude/skills/generate/`): Nano Banana 2 for images, Veo 3.1 (`veo3_fast`, Kie AI)
for video. It owns model choice, provider routing, keys, polling and logging; no agent
touches an API key.

**Work the cost-ascending ladder first, stop at the first rung that serves the brief:**
static depth (`backgrounds.md`) → ambient atmosphere (`atmosphere.md`) → reactive canvas
field (`reactive-backgrounds.md`) — all free — then paid video. If a free rung sells the
same feeling, take it.

**Two registers, and a site gets ONE clip TOTAL — either register, never both.**

- **`filmed-action`** — documentary proof. Gate: **the frame-2 test.** What does frame 2
  show that frame 1 cannot? Nothing → ship the still. Real motion that proves or sells
  (water feature, fire, a process/timelapse proof, venue ambience) → justified. For
  businesses whose work is **physically visible**. Photorealism kit applies in full.
  **Ceiling: ≤$1**, ≤8s.
- **`designed-loop`** — an abstract rendered motion object in the site's exact palette; its
  job is **brand register, not proof**, so frame-2 does not apply. Gate: **occupational fit
  — studio / tech / SaaS / premium / creative ONLY** (behind a trade, legal, or medical
  prospect it's the convention error `color-conventions.md` prevents — hard no), the moment
  needs rendered richness no free tier can fake, and it **consumes the scroll-set-piece
  slot** (mutually exclusive with a reactive field). **INVERTS the photorealism kit** — the
  CGI look is the point. **Ceiling: ≤$2.50**, ≤8s.

"It looks premium" and "the hero feels static" are not justifications in either register.

Those dollar figures are **ceilings on what Harry will consider, not budgets the crew may
spend.** Because Kie runs ~4× cheaper than Google direct, an approved clip can afford
1080p and the full 8s inside them — spend the room on quality, never on retries.

- **The Planner marks 0 or 1 `VIDEO` slot** with its **register**, justification, budget,
  duration, aspect, source (text-to-video or an image-to-video seed frame), and poster
  still. **Marking it is a REQUEST.** Unmarked means the Builder ships no clip.
- **The lead takes the request to Harry.** No answer is not a yes — the poster still ships
  alone and the plan is not defective for it.
- **The Builder generates only after Harry approves that specific clip**, to the declared
  register, and never switches it. **No retries** — one approval buys one run; exhaust the
  free `ffmpeg` fixes, then report. A second clip, 4K, >8s, a non-default model
  (Kling/Sora), or any regeneration is a fresh ask.
- **Shipping is part of the rule:** `<video autoplay muted loop playsinline poster="…">`,
  a `prefers-reduced-motion` branch showing the poster still, <~5MB, and a checked loop
  seam. Same content bans in both registers — no readable branding (compose lettering out
  of the shot; negating it does not work), no invented people for a real business.
- **The Critic judges against the declared register** and fails any clip that is
  unauthorized, unjustified, over cap, fallback-less, register-mismatched, or wrong for the
  occupation. The realism test applies to filmed clips only.

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
site's actual services, descriptions, service area, hours, contact info, and testimonials
into the dossier; the Planner structures that real material and the Builder renders it.
We are upgrading the **design and structure**, not rewriting the business. Only use
`[placeholder]` text where information genuinely doesn't exist. This keeps the pitch
honest and makes the site feel like *theirs*, done right.

**Their old site is a fact source, not a voice source** — see Copy voice below. Carry
every fact; don't inherit the phrasing.

## Content parity (hard rule)

**The new site must never know less than the old site. Richer design AND richer
information — that's the pitch.** A beautiful mockup that carries a fraction of the
original's information is a failed mockup: the owner notices their missing content
before they notice our typography. The pipeline summarizes at every hop (site → dossier
→ plan → build), so parity is enforced with an explicit artifact chain:

1. **Analyst** captures the existing site page-by-page, FULL TEXT, into
   `prospects/<slug>/site-content.md` (the dossier summarizes; this file preserves).
2. **Planner** writes a **content map** in `website-plan.md`: every site-content.md
   block gets a destination page/section, or goes on a **"Deliberately dropped"** list
   with a one-line reason. No silent drops. Long-form educational content (pest guides,
   how-it-works explainers, permit directories) is real content — default is CARRY it;
   the page map grows to fit the content, not the other way around.
3. **Builder** transfers mapped blocks at full informational fidelity — their service
   descriptions stay descriptions, their articles stay articles, their town lists stay
   complete. Punchy is for heroes and CTAs, not for the informational body.
4. **Critic** walks site-content.md against the mockup: every block present or
   accounted for on the dropped list, else a numbered fail list. This is a hard gate.

**Parity counts facts, not words.** Tightening a 60-word description to 25 words that
carry the same facts passes; dropping a fact fails. Nobody pads to survive a parity
review, and nobody bounces a mockup for being tighter than the old site.

## Copy voice (hard rule)

A site can be beautifully built and still read fake, and the owner feels it immediately:
sentences he'd never say out loud, one pretty word carried through every section, a dash
in the middle of every line restating what the first half already said. That's the single
most common complaint about our output.

**The client's questionnaire answers are the voice source.** Their old site supplies
facts only. How the copy sounds comes from how *they* talk.

**Copy is specification, not prose** — concrete nouns, numbers, towns, materials, hours.
When a section has no real facts behind it, shrink it or cut it. Never write around the
hole with atmosphere; that is where every bad line in this project has come from.

**The voice is a licensed contractor talking to a homeowner in his driveway.** Three ways
to miss it: **too poetic** ("meticulous by habit"), **too cute** ("we read the sun",
"won't need babying", trade puns, winking), **too vague** ("when the weather turns, we
show up"). "Plain" is not the target — plenty of cutesy copy is plain. Professional is.

Enforced with an artifact chain, same shape as content parity:

1. **Planner** mines `client-answers.md` into `prospects/<slug>/voice-spec.md` — register,
   the client's own phrases, word budgets, banned words, and which sections are
   pre-authorized to be short because the facts are thin. Written BEFORE the hero
   direction.
2. **Builder** writes every visible string against that spec, then runs
   `python3 skills/trade-copy/scripts/copycheck.py prospects/<slug>/mockup/index.html`,
   then sweeps the page with **`web-humanizer`** and runs
   `python3 skills/web-humanizer/scripts/aitells.py prospects/<slug>/mockup/*.html`.
3. **Critic** re-runs both scripts as a hard gate AND reads the page one sentence at a time
   asking whether the owner would say it aloud. The script can't catch "meticulous by
   habit"; a person can.

Two skills, two failure modes, and they do not overlap. **`trade-copy`** owns *register* —
how the owner talks, word budgets, banned vocabulary, em dashes, cutesiness.
**`web-humanizer`** owns *page shape* — the tells that survive a correct register: a hero
opening with a verb any industry could use, card titles built from two abstractions
("Professional Service"), a page carrying no number a customer could check, cards stamped
to identical lengths. Their word lists are deliberately disjoint so no single word gets two
different fixes; both push the same direction, which is more concrete.

Real review quotes, **Q7** keep-word-for-word content, legal text, and NAP are exempt from
every check and are never edited. Nothing is ever *added* to a page to satisfy a check —
terseness passes, invented facts never do. Full rules: the **`trade-copy`** and
**`web-humanizer`** skills.

## Skills each agent uses

Skills are NOT auto-loaded for teammates (the agent-teams runtime doesn't apply the
`skills` frontmatter field) — each agent must invoke them itself via the Skill tool, and
each agent's `tools` list includes `Skill`.

**A required skill that won't load is a stop-and-report, never a proceed-without.** If a
skill marked PRIMARY (or a `references/*.md` file it depends on) is missing or fails to
invoke, say so to the lead and stop that step. Do not improvise the skill's contents from
memory — the whole point of the skill is that it is more current and more specific than
what you'd reconstruct, and a build done from a half-remembered version of the design
pipeline is exactly the generic output the pipeline exists to prevent.

| Agent | Skills to invoke | Why |
|---|---|---|
| `scout` | `research`, `docs-seeker` | Deeper competitor/reputation research when a web search isn't enough; finding directories/docs on unfamiliar trades. |
| `analyst` | `research` | Comprehensive dossier research beyond a plain web search. |
| `planner` | **`web-design-ultra` (PRIMARY)**, **`trade-copy`**, `ui-ux-pro-max`, `frontend-design`, `design-system`, `aesthetic`, `sequential-thinking` | Run the 8-stage art-direction pipeline (Stages 1–5): design intelligence, real-site inspiration, anti-repetition, three divergent directions. `trade-copy` Stage A produces `voice-spec.md` from the client's answers before the hero direction is written. Names each reference site's patterns using the skill's `inspiration.md` vocabulary, and doesn't lock a direction the Stage 8 composition checks will fail — any deliberate exception is stated in `website-plan.md`. |
| `builder` | **`web-design-ultra` (PRIMARY)**, **`trade-copy`**, **`web-humanizer`**, `generate`, `ui-ux-pro-max`, `frontend-design`, `frontend-development`, `web-frameworks` | Execute the chosen direction (Stage 7): generate the 2 real hero/priority images (`/generate` on `nano-banana-2`), plus an approved video clip if there is one, craft discipline + backgrounds/atmosphere recipes; self-score the Stage 8 rubric. `trade-copy` governs every visible string — invoke before writing any text; `web-humanizer` is the sweep after it, catching the page shapes that still read machine-written (interchangeable hero verbs, abstract-pair card titles, no checkable fact, cards stamped to identical lengths) and gating on `aitells.py` exit 0 alongside `copycheck.py`. Reads the skill's `craft-floor.md` before editing UI, works `motion-thesis.md` / `layout-craft.md` / `type-craft.md` / `color-craft.md` when a build needs more than a first pass, and runs the Step 0 scan to `exit 0` before handoff. |
| `critic` | **`web-design-ultra`**, **`trade-copy`**, **`web-humanizer`**, `ui-ux-pro-max`, `code-review`, `design-system` | Audit each mockup against the Stage 8 10-dimension rubric AND the $10K Checklist; enforce real-reviews-only and the COPY VOICE gate (`copycheck.py` + `aitells.py` + a say-aloud read + the cold read); code-quality + design-system rigor. Runs the skill's Step 0 scan as the **first** gate, before any screenshot, then the fail-visible measurement and the composition checks; drives fix rounds with `bolder.md` / `quieter.md` rather than freehand nudges. |
| `caretaker` | `site-caretaker-cycle` (from `~/Projects/site-caretaker/.claude/skills/`) | Post-launch only, and only for sites already live on a real domain. Keeps `~/Projects/site-caretaker/sites.json` — the system of record for published sites — current, and diagnoses the uptime/DNS/TLS/content failures the hourly `com.sitecaretaker.monitor` job flags. Never edits a live site on its own, and never polls in a loop: Layer 1 already watches, for free, every hour. Its standing spec is `~/Projects/site-caretaker/VISION.md`, which lives outside this repo — so the role only works on a machine that has it. |
| **lead** (this session) | **`design-push`**, **`design-pull`**, **`github-push`**, **`github-pull`** | Publish each signed-off site to Claude Design (Stage 8 on-pass step B3b), and re-publish after every revision round. `design-pull` brings edits made in the Design pane back into `mockup/` before a push can overwrite them — and `design-push` refuses to run while any exist. Only the lead can: `DesignSync` is authorized in this session, not in any subagent. `github-pull` / `github-push` move the whole repo between Harry's Mac and Corey's — **pull at the start of a session, push when a run finishes.** Details in `github/README.md`. |

Optional, invoke only if the situation calls for it: `media-processing` (Builder — if
processing real images pulled from an existing client site) and `ai-multimodal`
(Analyst — if extracting content from screenshots of an existing site's design).

## Tooling rules

- **Free tools first.** Use built-in `WebSearch` / `WebFetch` and the browser pane for
  all research and scraping. **Do NOT call Firecrawl or Perplexity** (they cost Harry
  money) — if a page genuinely can't be reached any other way, stop and ask the lead,
  who asks Harry.
- **The only pre-approved paid operation is the builder's 2 AI images per mockup.**
  Generated through the `/generate` skill on **`nano-banana-2`** — the shipping tier, never
  the `-lite` draft model. It costs real money (~$0.04 at 1K / ~$0.06 at 2K ≈ $0.10 per
  prospect) and is **pre-approved at that cap**. A builder generating exactly those 2 is
  following the rules, not breaking them.
- **Video is NOT pre-approved — it is a request.** The Planner may mark ONE justified
  `VIDEO` slot in its declared register (`filmed-action` ≤$1 or `designed-loop` ≤$2.50,
  ≤8s, never both — see the Video policy above), but marking it only *asks*. **The lead
  takes that request to Harry, and the Builder generates nothing until Harry has said yes
  to that specific clip.** No answer yet → the poster still ships in the slot and the site
  is otherwise complete. A clip with no recorded approval is unauthorized spend and the
  Critic hard-fails it.
- Everything beyond — a 3rd image, any video without a confirmed yes, a 2nd clip, 4K, a
  longer clip, any regeneration, or any other paid call — needs the lead to ask Harry
  first.
  "Free tools only" elsewhere in these docs means *no Firecrawl/Perplexity*; it never meant
  skipping the sanctioned assets.
- **Never contact a business.** No emails, no form submissions, no DMs, no calls.
  Drafts only.

## Token reminder

Every teammate is a full Claude instance (~7× cost of a solo session). Keep scope
tight, mark tasks complete promptly, and shut down when your work is signed off.
