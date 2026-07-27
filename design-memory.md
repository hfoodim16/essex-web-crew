# Design Memory — Essex Web Crew

Project-local anti-repetition log for crew pitch mockups. `web-design-ultra` Stage 4 reads the **last 3 entries** here (not the global skill log) and bans reusing their font pairing, palette family, or layout archetype on the next prospect — so consecutive prospects look like different studios made them. Stage 8 / the critic appends one row per signed-off mockup.

Columns:
- **Date** — `YYYY-MM-DD`
- **Project** — prospect `<slug>`
- **Font pairing** — heading / body
- **Palette family** — e.g. earthy, dark-moody, warm-editorial, muted-luxury
- **Layout archetype** — e.g. editorial-asymmetric, bento, brutalist-stack, immersive-scroll, service-index
- **Background system** — e.g. gradient-mesh, grain, imagery-driven, contours
- **Signature motion** — entrance family + hero move, e.g. clip-wipe + underline-draw, scale-settle + magnetic (see the skill's `references/motion.md`). ⚠default = the fade-up/text-delay/count-up trio.

| Date | Project | Font pairing | Palette family | Layout archetype | Background system | Signature motion |
|------|---------|--------------|----------------|------------------|-------------------|------------------|
| 2026-07-21 | Cecere Brothers Landscaping | Fraunces / Figtree | forest-editorial | editorial-gallery / service-index | imagery-driven (AI photos) + topographic-contours + grain | fade-up ⚠default + row-expand hover + headline glint |
| 2026-07-21 | anthonys-landscaping — "Evening Estate" | Marcellus / Mulish | dark-evergreen + ivory + brass (dark-luxury) | dark editorial / service-index SPA | flat dark tokens + diagonal texture (built pre-imagery) | not recorded (pre-motion-schema) |
| 2026-07-21 | duran-and-son-landscaping — "Sunday Morning Oasis" | Bricolage Grotesque / Nunito Sans | light daybreak + meadow-green + river-blue + cedar | bright family-friendly stack | light paper tokens (built pre-imagery) | not recorded (pre-motion-schema) |
| 2026-07-21 | gee-kay-landscaping — "Heritage Ledger" | Fraunces / Karla | parchment + pine + brass-clay + sage (warm heritage) | ledger / archival editorial | parchment tokens + rule-work (built pre-imagery) | not recorded (pre-motion-schema) |
| 2026-07-22 | john-sessa-cpa — "Balanced Books" | Spectral / Public Sans (+ IBM Plex Mono numerals) | precision-professional (porcelain + ink-navy + manila + verdigris) | sidebar-anchored letterhead | dot-grid graph-paper + teal radial wash + grain | not recorded (pre-motion-schema) |
| 2026-07-22 | cedar-grove-transmission — "Signal & Steel" | Archivo / Barlow | industrial graphite + steel + trans-fluid red | industrial spec-sheet + bento | schematic gear linework + grain + steel glow-orb | not recorded (pre-motion-schema) |
| 2026-07-22 | happy-trees-by-mgm — "Canopy Descent" | Zilla Slab / Work Sans | natural bark + moss + sky + hi-vis lime | canopy-descent full-bleed + rope-stitch scroll | dapple light + photo scrim | not recorded (pre-motion-schema) |
| 2026-07-23 | fora-digital — "Main Street Modern" (our own agency site) | Instrument Serif / Hanken Grotesk | warm-editorial paper + ink + cobalt + clay (BREAK from the dark/tech-slick agency convention; cobalt kept as the trust cue) | gallery-wall portfolio — alternating framed plates + registration-mark hero mat | linen grain + hero radial wash + cool contact wash + **interactive cobalt "compass field" canvas in the hero** | mask-curtain wipe (cobalt panel scaleX, 90 ms `--i` stagger) + ink-sweep hovers (underline-draw / fill-sweep) + gallery-hang `animation-timeline: view()` + **pointer-reactive hero vector field (segments rotate toward the cursor; idle auto-orbit)** — deliberately NOT fade-up, NOT count-up |
| 2026-07-25 | paul-da-silva-law — "Ironbound Counsel" (Rev 2, client-directed palette) | Besley / Schibsted Grotesk | dark-first iron-gall ink-blue + aged brass + cool porcelain (HONORS legal blue+gold by client instruction, executed in non-default dark-first registers — near-black #131D33 ground, aged brass #B3873E not yellow-gold) | split-screen advocacy (dark identity panel / light content panel) + document-discipline interior stack | ink grounds + azulejo monoline lattice + grain + warm lamp-glow radial | clip-wipe reveal (clip-path inset, "unredacting", 70ms `--i` stagger) + card lift/tilt ≤2° + subtle hero parallax — deliberately NOT fade-up/count-up |
<!-- newest at the bottom; append one row per signed-off prospect -->
