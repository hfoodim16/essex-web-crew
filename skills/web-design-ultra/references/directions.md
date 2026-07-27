# Directions — forced divergence

Purpose: kill same-y, safe output. Generate **three genuinely different** design directions so the chosen one is a deliberate pick, not the first thing that came to mind. This is the anti-generic engine of the whole skill.

## The rule

The three directions **must differ on ≥3 of the 5 divergence axes** from each other. Two directions that share layout + type + color with a different accent are NOT two directions — they're one. If you can't tell them apart in a sentence, they're too close.

None of the three may use a font pairing, palette family, or layout archetype **banned** by the last 3 entries in `data/design-memory.md` (Stage 4).

## The 5 divergence axes (pick a different option per direction)

### 1. Layout archetype
split-screen · editorial asymmetric · bento grid · brutalist stack · immersive full-bleed scroll · centered-classic (use sparingly) · sidebar-anchored · magazine/broken-grid · dense dashboard grid (apps) · card-canvas

### 2. Typography personality
elegant serif display · geometric sans · grotesque/neo-grotesque · mono-accent techy · expressive/condensed headline · humanist warm · editorial serif+sans mix · oversized brutalist. **Never Inter/Roboto/Arial/Helvetica as primary.**

### 3. Color strategy
dark-first moody · light-airy with one sharp accent · high-contrast duotone · earthy/natural · vibrant maximalist · monochrome + single acid pop · muted premium/luxury · warm-analog · **industry-conventional (honor the category's expected palette for trust/recognition)**

Whatever you pick, make the occupational-convention call **explicit** per `color-conventions.md`: name the industry's expected palette and decide honor-or-break on purpose — at least one of the three directions should honor/adapt it.

### 4. Background / depth system
flat with generous whitespace · layered gradient mesh · noise/grain texture · geometric SVG pattern · imagery-driven (full-bleed photo/render) · animated gradient · glow/orb ambience · **animated atmosphere (drifting fog · parallax clouds · god rays/beams · aurora ribbons · dust motes/fireflies)** · **reactive field (pointer-spotlight · vector/compass field · constellation network · flow ribbons · perspective grid · data stream · starfield parallax · aurora mesh · circuit traces)**. See `backgrounds.md` (static/ambient), `atmosphere.md` (animated weather/light), `reactive-backgrounds.md` (fields that respond to pointer/scroll — tech register; costs the scroll set-piece).

### 5. Motion character
minimal-restrained · smooth-editorial (scroll reveals, parallax) · kinetic/aggressive (marquees, snappy) · playful-springy · cinematic (staged hero sequences) · **atmospheric (god rays, drifting fog, shimmer sweeps — light that moves)**

**Every direction must name its signature move** (see `motion.md`):

- **Entrance family** — clip-wipe · mask-curtain · blur-focus · scale-settle · slide-alternate · tilt-settle · stagger-cascade · line-draw · skew-slide · split-line-mask `[GSAP]` · character-cascade `[GSAP]` · word-tumble `[GSAP]` · iris-open `[GSAP]` · scrub-reveal `[GSAP]` · (fade-up ⚠ flagged default)
- **Hover personality** — underline-draw · fill-sweep · magnetic · lift+tilt · zoom-crop · icon-nudge · weight-shift · rule-trace-lift · crossfade-zoom · cursor-follow-label · glyph-scramble `[GSAP]`
- **At most one scroll set-piece** — parallax · scroll-scrub · sticky-progress · horizontal-strip · pinned-statement `[GSAP]` · sticky-stack `[GSAP]` · hero-exit `[GSAP]` · theme-transition `[GSAP]` · marquee-velocity `[GSAP]`
- **Tempo** — one ease + one stagger, per `motion.md`.

`[GSAP]` moves need the vendored loadout in `gsap.md`; state the tier in the brief so the byte cost is a decision, not a surprise.

⚠ **fade-up reveals, staggered text delay, and number count-up are the defaults every AI site ships.** Using them needs an explicit justification, never all three together, and never if a recent design-memory entry logged them. Directions must differ from each other on motion just as they do on type and palette.

## Direction-brief template (one per direction)

```
Direction <n>: <evocative name>
Concept: <one line — the feeling and who it's for>
Layout archetype: <axis 1>
Typography: <heading font / body font — from Stage 2 candidates or a deliberate pick>
Palette: <dominant + accent, with hex; name the family>
Background system: <axis 4 — specific recipe from backgrounds.md>
Motion: entrance=<family> hover=<personality> set-piece=<one or none>; tempo <duration/ease/stagger>; GSAP tier <0–3>
Hero + imagery: <what the hero is; what images to generate (feeds imagery.md)>
Why it's bold: <what makes it NOT generic for this niche>
```

## Choosing

- **Interactive:** present all three (a short paragraph each, or a visual comparison in the browser) and let the user pick.
- **Autonomous:** pick the **boldest** direction that still fits the brief's constraints. State which you picked and why in one line. When in doubt, bolder wins — Harry rejects safe passes.

## Anti-patterns

- Three variations of "clean modern SaaS" → that's one direction. Diverge harder.
- All three centered-hero + sans-serif + white bg → you've changed nothing. Change the axes.
- Picking the safe middle option by default → the pipeline exists to avoid exactly this.
