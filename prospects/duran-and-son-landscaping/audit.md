# Audit — Duran & Son Landscaping

**Reviewed:** 2026-07-19 · **Critic:** critic · **Art direction:** "Sunday Morning Oasis"
**Review round 2 (re-review 2026-07-19):** contrast fix landed — see item 8. **Overall: PASS — 8/8.**

_Round 1 was NEEDS-WORK for one marginal contrast fix on item 8; now resolved._

## $10K Checklist

1. **Point of view** — PASS. "Sunday Morning Oasis" warm-daylight direction (soft warm-white ground, meadow green, river-blue reserved for the water/light story, organic 26px pebble radius, drifting SVG wave dividers). Rationale at top of style.css. The deliberately warm, homeowner-friendly pole of the three sites — distinct, not a template.
2. **Typography** — PASS. Bricolage Grotesque (display) + Nunito Sans (body) via Google Fonts; not Inter/Roboto. Clear scale via clamp; weight contrast does hierarchy work.
3. **Restrained color** — PASS. 5 base tokens in :root (daybreak, evergreen-ink, meadow, river, cedar); all tints/hairlines are color-mix-derived, no stray hex. Three hue families are used with discipline (river reserved for water/light, cedar for hairlines/trust chips).
4. **Hierarchy breathes** — PASS. Generous section padding (clamp), capped measures, clear eyebrow→h2→body rhythm, section-heads and story bands give the eye rest.
5. **Imagery with intent** — PASS. Every image slot is a labeled AI-IMAGE placeholder styled in the art direction (meadow/river tint, hatch texture, contextual leaf/water icons, descriptive prompt). No stock/hotlinked images.
6. **Motion whispers** — PASS. Reveal-on-scroll with stagger, pop-in chips, drifting wave dividers, lerped custom cursor, magnetic buttons — all gated behind prefers-reduced-motion; cursor + magnets also gated on coarse pointer (CSS and JS).
7. **Mobile designed, not shrunk** — PASS. Proven by multiple mobile captures incl. a full-page 375 shot: stacked hero with repositioned 25+ badge, wrapping trust chips, single-column service cards, stacked splits, single-column contact form, hamburger nav, nav-call hidden on mobile. Real phone decisions.
8. **Invisible expensive stuff** — PASS. Semantic HTML, full meta+OG+Twitter+inline SVG favicon, focus-visible ring, sr-only, placeholder-only assets → sub-2s. FIXED: a new --river-ink token (river 76% + evergreen-ink) now drives all river accent TEXT — eyebrows, inline links, county chips, water card-links, and the previously-inline irrigation-page eyebrows. Measures ~5.4:1 on daybreak, ~5.8:1 on white cards, ~5.1:1 on river-tint (county chips) — all clear WCAG AA. The lighter --river is retained only for non-text uses (focus ring, icons, tints). Body ink ~12:1, ink-soft ~5.2:1.

## Hard rules
- Images: PASS — placeholders only.
- Fabricated facts: PASS. All three honesty flags respected — "25+ years" everywhere with NO specific founding year; the About story is an explicit bracketed placeholder that deliberately omits founding year AND names; NO "Alberto" anywhere (the Yelp quote is trimmed before that line); NO ponds in the service set. "Licensed & insured / guaranteed" is legitimate — it's near-verbatim from their own cached copy per the dossier.
- Client real content: PASS — positioning ("dream outdoor oasis," "design, build and maintain any type of landscape… from grounds maintenance to retaining walls"), values, service area (Essex/Morris/Union) and the world-class Yelp quote all reused from the dossier. Genuine gaps (hours, founding year, owner) are bracketed placeholders.
- No outbound contact: PASS.

## Result
Mockup PASSES 8/8 (contrast resolved in round 2). Email previously passed. Package signed off.
