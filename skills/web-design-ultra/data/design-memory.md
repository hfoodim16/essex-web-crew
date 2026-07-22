# Design Memory (global)

Append-only log of finished `web-design-ultra` projects. Stage 4 (anti-repetition) reads the **last 3 entries** and bans reusing their font pairing, palette family, or layout archetype on the next project. Stage 8 appends a new row on every passing build.

**Scope:** this is the **global fallback** log. If a project defines its own `<project-root>/design-memory.md` (same format), that local file wins — read bans from and append to it instead, so a project's prospects diverge from each other, not from unrelated builds. The Essex Web Crew uses `~/Projects/essex-web-crew/design-memory.md`. This global file is for one-off / test / solo builds.

Columns:
- **Date** — `YYYY-MM-DD`
- **Project** — name / brief
- **Font pairing** — heading / body
- **Palette family** — e.g. dark-moody, earthy, duotone, muted-luxury
- **Layout archetype** — e.g. editorial-asymmetric, bento, brutalist-stack, immersive-scroll
- **Background system** — e.g. gradient-mesh, grain, imagery-driven, dot-grid

| Date | Project | Font pairing | Palette family | Layout archetype | Background system |
|------|---------|--------------|----------------|------------------|-------------------|
| 2026-07-21 | EMBERS — Nordic sauna & cold-plunge (test) | Bricolage Grotesque / Hanken Grotesk | fire-ice duotone | split-tension / duotone | gradient-mesh + grain + ember-canvas |
| 2026-07-21 | Cecere Brothers Landscaping (concept) | Fraunces / Figtree | forest-editorial | editorial-gallery / service-index | imagery-driven (AI photos) + topographic-contours + grain + god-rays + drifting-fog + headline-glint |
| 2026-07-21 | Alder Dental Studio (dentist concept) | Instrument Serif / Onest | warm-bone + navy + coral + mint | soft-organic asymmetric + card grid | 1 AI photo (arch-framed) + organic blobs + soft shadows |
<!-- newest at the bottom; append one row per passing build -->
