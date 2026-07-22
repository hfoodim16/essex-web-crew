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
flat with generous whitespace · layered gradient mesh · noise/grain texture · geometric SVG pattern · imagery-driven (full-bleed photo/render) · animated gradient · glow/orb ambience · **animated atmosphere (drifting fog · parallax clouds · god rays/beams · aurora ribbons · dust motes/fireflies)** · WebGL/3D (cost-aware). See `backgrounds.md` (static/ambient) and `atmosphere.md` (animated weather/light).

### 5. Motion character
minimal-restrained · smooth-editorial (scroll reveals, parallax) · kinetic/aggressive (marquees, snappy) · playful-springy · cinematic (staged hero sequences) · **atmospheric (god rays, drifting fog, shimmer sweeps — light that moves)**

## Direction-brief template (one per direction)

```
Direction <n>: <evocative name>
Concept: <one line — the feeling and who it's for>
Layout archetype: <axis 1>
Typography: <heading font / body font — from Stage 2 candidates or a deliberate pick>
Palette: <dominant + accent, with hex; name the family>
Background system: <axis 4 — specific recipe from backgrounds.md>
Motion: <axis 5 — what animates>
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
