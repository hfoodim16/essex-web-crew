---
name: web-design-ultra
description: Use when building, designing, or redesigning any website, landing page, marketing site, web app, dashboard, or web UI — or when asked to make a site more beautiful, bolder, more distinctive, higher-end, or less generic/AI-looking. Also the /web-design-ultra command. Runs a full art-direction pipeline: real-site inspiration, forced-divergent directions, AI imagery and rich backgrounds, and a screenshot critique gate.
---

# Web Design Ultra

## Overview

An art-director pipeline for producing **bold, distinctive, verified** websites — stronger than plain style-lookup or taste-prompting alone. It exists to kill four failure modes: same-y output across projects, safe/generic design, inconsistent quality, and designs invented in a vacuum instead of grounded in real references.

**Core principle:** Never build straight from the prompt. Ground in evidence → diverge deliberately → verify with your own eyes (screenshots) → refuse to ship the boring option.

This skill orchestrates existing tools rather than duplicating them:
- **Design intelligence** (styles/palettes/fonts/stack rules) → `ui-ux-pro-max` search engine
- **AI image + video generation** → the `generate` skill (Nano Banana 2 for images, Veo 3.1 for video, via Kie AI)
- **Motion craft** → `references/motion.md` (the named vocabulary) + `references/gsap.md` (the vendored GSAP 3.15 tier)
- **Publishing the finished site** → the `design-push` skill (Stage 8 on-pass), which bundles it via `scripts/design-bundle.py` and pushes it to claude.ai/design as a card-per-section design system

## The Non-Negotiables

**Violating the letter of the pipeline is violating the spirit.** These hold on every run, even under time pressure or "it's just a small site":

1. **Evidence before design.** You must look at real reference sites (Stage 3) before committing to a direction. No skipping to build.
2. **Three genuinely different directions.** Not three shades of the same idea — they must differ on ≥3 of the 5 divergence axes. See `references/directions.md`.
3. **No repeats.** Read `data/design-memory.md` and do not reuse the last 3 projects' font pairing, palette family, or layout archetype.
4. **The bold test.** For a redesign, before/after screenshots must be obviously different at a glance. If a stranger couldn't tell them apart, it failed — start over, don't tweak.
5. **Verify with screenshots.** You must screenshot the built site (desktop + mobile + dark if relevant) and score it against the rubric before claiming done. See `references/critique.md`.
6. **Never generic fonts.** The banned set is **Inter, Roboto, Arial, Helvetica, Fraunces, Instrument Serif, Geist, Plus Jakarta Sans, Space Grotesk** — the first four are the old defaults, the rest are the ones each new wave of AI-generated sites converged on next. Stage 8's detector flags all of them mechanically (`overused-font`). A client's genuine brand font is a documented exception, never a silent pass. Never the purple-gradient-on-white AI-slop look.
7. **Content is never hidden by JavaScript.** Motion hides and reveals at runtime; the stylesheet never ships content at `opacity:0` or under a covering panel. Rename the script, reload — if the page goes blank, it fails, no matter how good it looked animated. See `references/motion.md` rule 0. Stage 8 now **measures** this rather than eyeballing it: `impeccableMeasureHiddenText()` reports the percent of page text invisible at rest (a broken page reads ~86–100%, a healthy one 0%).
8. **Real businesses get real content only.** Never fabricate reviews, testimonials, ratings, stats, credentials, or years-in-business for a real company — a pitch that invents "★★★★★ Sarah M." is a liability, not a flourish. Invented copy is allowed **only** for fictional demos, or as an explicitly labeled placeholder: `[PLACEHOLDER — replace with real review]`. When you lack real content, ship the labeled placeholder, not a plausible lie.

## The Pipeline (run all 8 stages, in order)

Create a todo for each stage so none is silently dropped.

### Stage 1 — Brief
Extract: product type, audience, niche, target stack, mood/personality words, page list, and whether this is a new build or a redesign. Ask the user **only** if something load-bearing is genuinely ambiguous. When running autonomously, infer sensibly and state your assumptions.

### Stage 2 — Design intelligence
Query the reused engine for baseline candidates (run from anywhere; absolute path):
```bash
python3 ~/.claude/skills/ui-ux-pro-max/scripts/search.py "<product type + niche + mood>" --design-system --persist
```
- Add `--stack <stack>` (react, nextjs, vue, svelte, astro, html-tailwind, shadcn, swiftui, flutter … 22 available) for implementation rules.
- Add `--domain <domain>` for deep-dives (e.g. color, typography, landing, charts).
- `--persist` writes `design-system/MASTER.md` into the project for cross-session consistency.
- Requires Python 3. If it errors on missing deps, it is stdlib-only — rerun; if the path is wrong, `ls ~/.claude/skills/ui-ux-pro-max/scripts/`.

**Also capture the industry-conventional palette.** Run `python3 ~/.claude/skills/ui-ux-pro-max/scripts/search.py "<bare industry term>" --domain color` (e.g. just "dental practice", "law firm", "restaurant") to pull the palette people subconsciously expect for this sector plus its psychology `Notes`. Note it — you'll decide in Stage 5 whether to honor or break it. See `references/color-conventions.md`.

Treat the output as **candidates to diverge from**, not gospel. The engine gives a solid baseline; your job is to push past it — but for the palette specifically, diverge *deliberately*, not by accident (see below).

### Stage 3 — Inspiration (mandatory)
Open the browser pane and study **3–5 real reference sites**, then build an evidence sheet. Full playbook: `references/inspiration.md`. Rule: extract *patterns*, never copy a specific site. **Crew builds: check the local `Inspiration/` library first** — it carries both site mockups (design references) and photography (art-direction and image-to-video source), under that file's transformation rule.

### Stage 4 — Anti-repetition check
Read the design-memory log and list the banned font pairings, palette families, layout archetypes, and **signature motion** (entrance family + hero moves) from its **last 3 entries**. Carry these bans into Stage 5 — motion repeats as easily as fonts do, and the default trio (fade-up + text delay + count-up) is exactly what makes builds feel same-y.

**Which log:** if `<project-root>/design-memory.md` exists, use it (a project keeps its own ban list — e.g. the crew's `~/Projects/essex-web-crew/design-memory.md`, so prospects diverge from each other, not from Harry's unrelated test builds). Otherwise fall back to the global `data/design-memory.md`. Read from and, in Stage 8, append to the **same** file.

### Stage 5 — Three divergent directions
Produce three direction briefs per `references/directions.md`. Each is a mini-spec: name, one-line concept, layout archetype, type pairing, palette, background system, motion character, hero/imagery plan. They must differ on ≥3 of the 5 axes and none may hit a banned combo. Present them for the user to pick when interactive; when autonomous, **pick the boldest** and state which and why.

**Make the color-convention call explicit** (per `references/color-conventions.md`). Name the industry's conventional palette and its psychology (from Stage 2). At least **one** direction must **honor/adapt** that convention; others may break it. For every direction, say whether its palette **honors or breaks** the convention and why that serves this brief — never diverge from the industry norm silently. If breaking, keep at least one trust cue from the category.

### Stage 6 — Assets (imagery + backgrounds + atmosphere)
Generate the imagery the chosen direction needs (hero, textures, OG image) via `references/imagery.md`, construct backgrounds from `references/backgrounds.md`, and layer in animated atmosphere (fog, god rays, clouds, shimmer, motes) from `references/atmosphere.md` where the mood calls for it. Optimize to WebP at correct sizes. A great site is rarely flat color — depth, real imagery, and moving light are how it stops looking like a template. **Imagery must follow `imagery.md`'s photorealism kit, cost rules, and "Fit the slot" sizing** — choose each image's aspect ratio AND resolution tier for where it renders (`--image-size 2K` for full-bleed/background heroes, `1K` for contained cards/plates/OG). Generate exactly ONE image on a skill test/demo; for real builds, announce the image count and per-tier cost (~$0.04 at 1K / ~$0.13 at 2K) before generating a set.

**Video comes in two registers, and picking the register is the decision that matters.** `references/video.md` carries the full system. **Filmed action** is documentary proof — it must pass the frame-2 test (what does frame 2 show that frame 1 cannot?) and suits businesses whose work is physically visible. **Designed loop** is a motion-design object — abstract rendered animation in the site's palette whose job is brand register, not proof; it suits studio/tech/premium brands only, inverts the photorealism kit, and takes the scroll-set-piece slot. Work the cost-ascending ladder first: static depth → atmosphere → reactive field (all free) → designed loop → filmed action. **One clip per site total, either register, never both**; most sites ship zero, and that is never a deduction. **Video always requires an explicit yes before it is generated, in every mode** — propose the register and concept, state clip count × duration × rate, wait. In **crew mode** the planner may mark one `VIDEO` slot, but that is a *request*: the lead takes it to Harry and the builder generates only once he approves that specific clip. Ceilings on the ask are filmed ≤$1 and designed loop ≤$2.50, ≤8s either way; images remain the pre-approved exception.

### Stage 7 — Build

**Assign a section format to every section before building.** `references/section-formats.md` carries the format families, the opener vocabulary beyond the eyebrow, and the variety quotas (≥4 distinct families per 8 sections, no family twice consecutively, kicker budget ≤ ceil(sections÷3), no two adjacent sections sharing an opener). 79% of visitors scan by riding section openers for landmarks, so a page of identically shaped sections offers one landmark stamped repeatedly. Two blocking detector rules — `section-shape-repetition` and `repeated-section-kickers` — enforce this mechanically.

**Load `references/craft-floor.md` first** — once the direction is settled and immediately before you edit UI. It is the mechanical quality floor (contrast, shadow depth, spacing rhythm, type measure, real states) plus the category defaults to refuse (icon+heading+text card grids, eyebrow over every section, gradient text, nested cards, decorative glass). It never picks the direction; it stops the build from quietly regressing to the mean.

Then implement the chosen direction using Stage 2's stack rules and craft discipline: distinctive type (never the banned set), CSS variables for the whole palette, deliberate spatial composition (asymmetry, overlap, scale contrast), and motion from `references/motion.md` — commit to the direction's **signature move** (one entrance family + one hover personality + at most one scroll set-piece), never the default fade-up/text-delay/count-up trio.

**Decide motion before you pick a technique.** `references/motion-thesis.md` is the *whether and why* layer — name the one focal moment that deserves authorship, what each supporting animation explains (feedback, state, continuity, attention), and the budget. `motion.md` is the *which* layer: the named entrance families, hover personalities, and set-pieces you choose from once the thesis says a moment has earned motion. Running the catalog without the thesis is how a page ends up animating every section identically.

**Work the three craft domains** when a build needs more than a first pass — each pairs a qualitative assessment with a mechanical scan scoped to that domain: `references/layout-craft.md` (squint test, grouping, rhythm, density), `references/type-craft.md` (hierarchy, measure, scale, delivery), `references/color-craft.md` (roles, OKLCH ramps, contrast — the *how to build it* half of `color-conventions.md`'s *which palette*).

**Find one moment that earns personality** via `references/delight.md` — first use, completion, error recovery, or discovery. One is the target; whimsy sprayed across a page costs more than it gives. Ambient light/air effects come from `references/atmosphere.md`; when the signature move needs scrubbing, pinning, staged timelines, split text, or SVG draw/morph, use the vendored GSAP tier in `references/gsap.md` (copy from `assets/gsap/` into the build's `vendor/` — never a CDN). Respect `prefers-reduced-motion` on every animation, and **never hide content behind JavaScript** — rename the script, reload, and the page must still read.

**Opt-in only — technical ambition.** If the user explicitly asks to be blown away ("make it extraordinary", "push what the browser can do", "go all out"), load `references/overdrive.md`: View Transitions, WebGL/WebGPU, scroll-driven animation, spring physics, virtual scrolling. It carries its own mandatory gate — propose 2–3 directions with their trade-offs and get the user's pick **before** writing any code. Never load it on the default path, and never build from it without that confirmation; in Crew mode it also conflicts with the Builder's "implement the plan, don't re-decide it" contract unless the plan itself called for it.

For a **local service business** (landscaper, dentist, plumber, contractor — the crew's bread and butter), also apply the conversion patterns in `references/local-trade.md`: tap-to-call CTA, service-area town list, license/insurance line, before/after gallery, ≤4-field estimate form, consistent NAP footer. **Ship the local-SEO structure too** — `LocalBusiness` JSON-LD + the meta essentials checklist from that file, with `PLACEHOLDER_…` tokens wherever the real NAP data isn't known (never invent it).

### Stage 8 — Critique gate & loop
`preview_start` the site (or, for a static double-click mockup, point the pane at a tiny Bash static server — see `references/critique.md`), then screenshot desktop, mobile (375px), and dark mode if applicable. Score against the 10-dimension rubric in `references/critique.md`. For pitch-mockup deliverables the desktop + mobile screenshots are a **required artifact** saved to `screenshots/`, not just a check — missing mobile screenshots = automatic fail. **Gate:** no dimension below 7, boldness ≥ 8, and (for redesigns) the bold test passes. On failure: fix the specific weak dimensions, re-screenshot, re-score — up to 3 loops, then report honestly with the scores. On pass, two steps: **(a)** append this project's choices (project, date, font pairing, palette, layout archetype, background system, **signature motion**) to the **same log Stage 4 read** — the project-local `design-memory.md` if one exists, else the global `data/design-memory.md`; **(b)** **publish it to Claude Design** by invoking the `design-push` skill, so the finished site lands at claude.ai/design as a browsable card-per-section design system. Re-running a passing build re-pushes and updates the same project in place. Skip only if the user has opted out for this project.

## Crew mode (multi-agent teams, e.g. Essex Web Crew)

When a team runs this skill, the 8 stages split across roles instead of one agent doing all of them. Official mapping (matches the crew's Mockup Recipe):

- **Planner owns Stages 1–5.** Output artifact: a `website-plan.md` that is the design contract. It must carry: the named art direction + direction brief, the **color-convention honor/break call** (Stage 5), the page/section map, the font pairing + `:root` palette, and an **image slot list** marking each slot `GENERATE` (real AI image) or `PLACEHOLDER` (labeled `<!-- AI-IMAGE: … -->`). The planner consulted the anti-repetition log; the plan names the banned combos it avoided. The planner may also mark **at most one `VIDEO` slot** — naming its **register** (`filmed-action` or `designed-loop`) with a written justification, within the crew video tier in `references/video.md`; default is no video.
- **Builder owns Stages 6–7.** Implements the plan exactly — does **not** re-decide direction, fonts, or palette. Generates only the `GENERATE`-marked images within the image cap (see `references/imagery.md` crew tier), plus the `VIDEO` slot if the plan marked one, generated **to its declared register** (`references/video.md` crew tier: filmed ≤$1 Fast/Lite, designed loop ≤$2.50 Standard, ≤6s, one clip per site). Never invents either kind of asset the plan didn't mark.
- **Critic owns Stage 8.** Runs the critique gate + the team's own checklist, loops until sign-off, then appends the passing row to the **project-local** `design-memory.md`. That's on-pass step (a). Step (b) — **publishing to Claude Design** — the critic **hands to the lead**, because `DesignSync` is authorized in the lead session and not in any subagent. It must be named in the sign-off message or it gets dropped.

Any agent that runs Stage 8 (builder self-check or critic) needs the browser/preview tools in its `tools` list (`preview_start`, `navigate`, `computer`, `read_page`, `read_console_messages`, `resize_window`, `javascript_tool`) — Stage 8 cannot be done without them. Solo mode is unchanged: one agent runs all 8 stages.

## Quick Reference

| Need | Go to |
|------|-------|
| Baseline style/palette/font/stack rules | `python3 ~/.claude/skills/ui-ux-pro-max/scripts/search.py …` |
| Occupational color conventions + honor/break | `references/color-conventions.md` |
| Local service-business conversion patterns | `references/local-trade.md` |
| How to research + what to extract from real sites | `references/inspiration.md` |
| The 5 divergence axes + direction-brief template | `references/directions.md` |
| The build quality floor + defaults to refuse (load before editing UI) | `references/craft-floor.md` |
| Whether/why to animate a moment (before picking a technique) | `references/motion-thesis.md` |
| Section format families + opener vocabulary + variety quotas | `references/section-formats.md` |
| Layout / type / color craft passes + domain-scoped mechanical scan | `references/layout-craft.md` · `references/type-craft.md` · `references/color-craft.md` |
| One earned micro-interaction | `references/delight.md` |
| Amplify a flat section / calm an overloud one (Stage 8 fix loop) | `references/bolder.md` · `references/quieter.md` |
| Technically extraordinary effects (OPT-IN, propose-and-confirm first) | `references/overdrive.md` |
| Background/texture/depth recipes | `references/backgrounds.md` |
| Element animations: entrances, reveals, staggers, hovers, scroll set-pieces | `references/motion.md` |
| Animated atmosphere (fog, god rays, clouds, shimmer, motes) | `references/atmosphere.md` |
| Reactive backgrounds (pointer fields, constellation, flow, grids — tech register) | `references/reactive-backgrounds.md` |
| AI image prompt formulas + WebP steps | `references/imagery.md` |
| AI video generation (Veo 3.1, opt-in, cost-gated) | `references/video.md` |
| Scoring rubric + bold test + fix loop | `references/critique.md` |
| Deterministic anti-pattern scan (60 rules, no LLM, ~1s) | `scripts/detect.mjs` |
| Anti-repetition log | `data/design-memory.md` |
| Publish a finished site to Claude Design (Stage 8 on-pass) | `design-push` skill · `scripts/design-bundle.py` |
| GSAP tier: scrub, pin, timelines, split text, SVG draw/morph | `references/gsap.md` (library in `assets/gsap/`) |

## Red Flags — STOP

- "I'll skip the inspiration stage, I know this niche" → No. Evidence before design.
- "Three directions is overkill for a small site" → No. Divergence is the anti-same-y mechanism.
- "The screenshots look fine, no need to score" → No. Score against the rubric.
- "This redesign is subtle but improved" → Fail the bold test. Harry rejects subtle passes.
- Reaching for Inter / a purple gradient / a centered hero with a stock photo → generic. Diverge.
