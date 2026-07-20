# Audit — Anthony's Landscaping

**Reviewed:** 2026-07-19 · **Critic:** critic · **Art direction:** "Evening Estate"
**Overall: PASS — 8/8.**

## $10K Checklist

1. **Point of view** — PASS. "Evening Estate" dark design-build direction (forest-charcoal ground, ivory inscription caps, bluestone gray, restrained brass) — the mood of a finished SOMA backyard at dusk with the lighting on. Rationale at top of style.css. Distinctly not a template; deliberately the opposite of their .gif-era site.
2. **Typography** — PASS. Marcellus (Roman-caps display) + Mulish (crisp body) via Google Fonts; not Inter/Roboto. Uppercase serif headings carry real hierarchy against low-contrast body.
3. **Restrained color** — PASS. 5 tokens in :root (evergreen, moss-panel, ivory, bluestone, brass); all other values are token-derived alpha tints. No stray hex in components.
4. **Hierarchy breathes** — PASS. Generous dark negative space, oversized ghost page-numbers, clear eyebrow→h1→lede rhythm, section-heads with capped measure. The eye is led.
5. **Imagery with intent** — PASS. Every image slot is a labeled AI-IMAGE placeholder styled in the direction (moss panel + diagonal hatch + brass keyline + descriptive prompt). No stock/hotlinked images.
6. **Motion whispers** — PASS. Reveal-on-scroll with clip-path image wipe, 3D card tilt, lerped custom cursor with contextual labels — all gated behind prefers-reduced-motion; cursor also gated on coarse pointer.
7. **Mobile designed, not shrunk** — PASS. Proven by mobile-home.png and mobile-hardscape.png (the two densest pages): single-column service index, reflowed stat column, collapsed 6-card signature grid, full-width stacked CTAs, working hamburger. Real phone decisions, not a shrink. (Recommend capturing the other 3 pages too for a complete set, but the mobile system is proven.)
8. **Invisible expensive stuff** — PASS. Semantic header/nav/main/footer, role=region + aria-labels per SPA page, skip-link, focus-visible ring. Full meta+OG+Twitter+inline SVG favicon. Contrast is strong on the dark ground (brass ~6.6:1, bluestone ~5.6:1 on cards, ivory ~14:1 — all clear AA). Placeholder-only assets → sub-2s.

## Hard rules
- Images: PASS — placeholders only.
- Fabricated facts: PASS. CRITICAL honesty flag respected — NO current owner asserted anywhere; only the well-sourced historical "founded by Anthony Molinaro over thirty years ago" appears; no "Chike Achebe." 30+ years, SOMA, complimentary estimates, phone/address all trace to dossier.
- Client real content: PASS — their live-site copy reused near-verbatim (philosophy line, "quality, experience, workmanship, professional integrity," "cut above the rest," design/maintenance blurbs) and their actual service list drives the pages. Genuine gaps (hours, exact towns) are bracketed placeholders.
- No outbound contact: PASS.

## Result
Mockup PASSES 8/8. Email previously passed. Package ready for sign-off.
