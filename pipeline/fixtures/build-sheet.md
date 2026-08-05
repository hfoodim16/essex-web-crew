# Build Sheet — Smoke Test Plumbing (FIRE-DRILL FIXTURE, not a client)

> SYNTHETIC FIXTURE — written to pass plan-lint's build-sheet checks exactly.
> See README.md before editing.

## Global block (paste-ready)

### Tokens

```css
:root{
  --ink:#1b1f23;
  --paper:#ffffff;
  --steel:#41505c;
  --signal:#0b5c3f;
  --signal-dark:#084430;
  --hair:#d5dade;
}
```

### Fonts

Display: "Zilla Slab", Georgia, serif. Body: "Public Sans", system-ui, sans-serif.

### Motion

entrance = rise-in; hover = underline-draw; set-piece = none; tempo 420ms, 60ms stagger; GSAP tier 0

### Composition device

Dominant column — services runs 7/5 with copy carrying the weight. Carried by `services`.

### Head / SEO

Title "Smoke Test Plumbing — synthetic fixture". No JSON-LD (fixture; not a business).

## Sections (build in this order)

### 1. id: hero

- format: hero , opener: none
- copy: "Burst pipe at 2am? We answer the phone." + lede inline in mockup
- palette: bg var(--paper), text var(--ink), cta var(--signal)
- assets: none
- motion: entrance
- done-when: one h1, tap-to-call visible without scrolling

### 2. id: facts

- format: stat-strip , opener: bare-h2
- copy: founded 1994 / under 90 minutes / six towns
- palette: bg var(--paper), tiles #f2f4f6, text var(--ink)
- assets: none
- motion: none
- done-when: three fact tiles render with dt/dd pairs

### 3. id: services

- format: split , opener: kicker+h2
- copy: services list inline in mockup (4 items)
- palette: bg var(--paper), kicker var(--signal)
- assets: none
- motion: none
- done-when: 7/5 grid on desktop, single column under 760px

### 4. id: process

- format: steps , opener: bare-h2
- copy: call → quote → fix, one bold lead-in each
- palette: numerals var(--signal), text var(--ink)
- assets: none
- motion: none
- done-when: ordered steps with oversized numerals

### 5. id: area

- format: editorial-column , opener: numeral
- copy: six town names inline
- palette: label var(--steel), text var(--ink)
- assets: none
- motion: none
- done-when: town list readable at 62ch measure

### 6. id: contact

- format: cta-band , opener: side-label
- copy: "Water where it shouldn't be? Call now."
- palette: bg var(--signal), text var(--paper), button var(--paper) on var(--signal-dark)
- assets: none
- motion: none
- done-when: band contrast >= 4.5:1 including button hover
