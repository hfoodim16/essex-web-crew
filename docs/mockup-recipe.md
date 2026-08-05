# The Mockup Recipe (the "DaSilva workflow") — full text

> Extracted from CLAUDE.md (token diet, 2026-08-03): read ON DEMAND by the role that
> needs it, instead of by every teammate at spawn. CLAUDE.md keeps the binding summary;
> where the two ever disagree, CLAUDE.md wins.

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
- **Stage 6 → runs, budget-bounded.** Builders generate **every slot the Planner marked
  `GENERATE`**, hero first — **no count cap; stop at the site budget** ($1.00 no video /
  $1.50 with one) via the `/generate` skill on `nano-banana-2` + the skill's
  `references/imagery.md` photorealism kit; client-photo slots stay labeled AI-IMAGE
  placeholders (see Image policy). **Optionally one
  video clip — only after Harry approves it** (a marked `VIDEO` slot is a request, not an
  authorization), in its declared register: `filmed-action` or `designed-loop`, ≤8s, never
  both, inside the site's **all-in budget of $1.00 (no video) / $1.50 (with video), images
  included**; zero video is the norm (see Video policy). ALSO layer the skill's free CSS craft:
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
5. **Imagery with intent** — every Planner-marked `GENERATE` slot holds a REAL generated
   image passing the two-way realism test (no count cap — the site budget is the limit);
   every `PLACEHOLDER` slot is a deliberate, labeled AI-IMAGE box matching the art
   direction (see the Image policy below). A placeholder sitting in a `GENERATE` slot is
   never an acceptable exception. No stock defaults.
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

