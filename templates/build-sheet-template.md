# Build Sheet — <prospect-slug>

> **The Builder's ONLY required input.** Self-contained, ordered top-to-bottom in build
> order. If the Builder must open `website-plan.md` to build a section, this sheet is
> defective — report it to the Planner via the lead; never bridge the gap by
> interpreting.
>
> **Hard rules (Planner writes to these; the lint enforces what it can):**
> - **Single authority.** This sheet outranks `website-plan.md`. A disagreement between
>   them is a Planner defect: the Builder builds the sheet and reports the drift.
> - **No renames, ever.** A direction change means regenerating this sheet with final
>   names everywhere — never a "read X as Y throughout" instruction. (A real plan once
>   shipped a verde→azul terminology map; 28 stale lines survived it, including a CSS
>   var that didn't exist and an image prompt whose meaning changed depending on
>   whether you substituted.)
> - **Present tense only.** No statuses, no history ("never used", "generated
>   post-plan") — run status lives in STATE.md.
> - **Self-containment.** Every section block must be buildable reading ONLY that block
>   plus the global block. Copy is inline or an exact source cite — never "see §8".
> - **Palette by token name only** (`var(--paper)`), never color words.

## Global block (paste-ready)

### Tokens

```css
:root{
  /* EVERY variable referenced anywhere in this sheet must be defined here.
     A var named below but missing here fails plan-lint. */
}
```

### Fonts

<!-- imports + full fallback stacks, paste-ready -->

### Motion

<!-- entrance = <family>; hover = <personality>; set-piece = <one or none>;
     tempo <duration/ease/stagger>; GSAP tier <0-3> -->

### Composition device

<!-- the ONE symmetry break + which section id carries it -->

### Media budget

<!-- No image count cap — the site budget is the only limit: $1.00 all-in if the site
     ships no video, $1.50 if it ships one (images + video + regenerations, everything).
     List every GENERATE slot with its tier and total it here; the builder stops at the
     ceiling. e.g.  1×2K hero ($0.06) + 5×1K ($0.20) = $0.26 of $1.00 — fits.
     If a VIDEO slot is marked, price it here too and show the combined total. -->

### Head / SEO

<!-- title, meta description, canonical, og:*, LocalBusiness JSON-LD.
     Unknown values as PLACEHOLDER_ tokens — never invented. -->

## Sections (build in this order)

<!-- One block per section. Copy the shape exactly. -->

### <n>. id: <kebab-id>

- format: <family> , opener: <opener>
- copy: <final copy inline, or exact cite: client-answers.md Q<n> / site-content.md L<a>-<b>>
- palette: <roles by token name: bg var(--x), text var(--y), accent var(--z)>
- assets: <GENERATE + full prompt + aspect + resolution | placeholder: "<label text>" | none>
- motion: <which global token applies | none>
- done-when: <one observable acceptance line>
