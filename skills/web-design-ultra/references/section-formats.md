# Section Formats — the vocabulary that kills same-shape pages

Why this file exists: eyetracking says 79% of visitors scan and an average visit reads ≤28% of the words. The scanning mode good sites serve is the **layer-cake**: the eye rides headings and section openers, sampling a layer only when it looks different enough to promise something new. **A page of identically shaped sections gives the scanner no landmarks** — kicker + h2 + short paragraph repeated seven times is one landmark stamped seven times, and the eye stops sampling after the second. That is the "AI slop" shape. Section formats are chosen per section, at plan time, from this vocabulary.

Rhythm is the designed contrast between adjacent sections — dense ↔ breathe, text ↔ visual, contained ↔ full-bleed. The page is a story arc (hero → value → proof → CTA → detail), each beat has a different job, and **a different job earns a different form**.

## The format families

| Family | Job in the arc | Density | Earns its place when |
|--------|----------------|---------|----------------------|
| `card-grid` | compare 3–6 equivalent things (services, plans) | dense | items are genuinely parallel; NEVER the default container |
| `split` | one idea + one image, side by side | medium | the media carries half the argument |
| `full-bleed-band` | visual breather / mood reset | breathe | after 2 dense sections; photo, video poster, or rich gradient |
| `editorial-column` | one narrow measure of real prose | medium | the story matters (about, origin, process narrative) |
| `stat-strip` | 3–4 numbers that prove something | breathe | the numbers are real and verifiable |
| `steps` | sequence with an order (process, timeline) | medium | order itself informs; numbered ONLY here |
| `bento` | one composed mosaic of unequal tiles | dense | mixed content types belong together; ≥2 cells carry visual weight |
| `gallery` | the work itself, imagery-first | dense-visual | portfolio/before-after; captions do the talking |
| `quote-monolith` | ONE testimonial given a whole section | breathe | one voice is strong enough to stand alone |
| `table` | exact comparison (pricing, specs) | dense | reader needs rows and columns, not vibes |
| `faq` | objections answered on the reader's terms | medium | real questions from real prospects |
| `cta-band` | the ask, isolated | breathe | once mid-page at most + once at the end |

## The opener vocabulary (how a section announces itself)

The eyebrow/kicker is ONE opener, not the grammar of the page. Openers, pick per section:
- **bare-h2** — heading alone, scale does the work (the default)
- **kicker+h2** — tracked or accent label above; **budget: ≤ ceil(sections÷3) per page, hero counts**
- **numeral** — oversized index number; ONLY on `steps`
- **side-label** — small rotated/margin label beside content, not above
- **in-media** — heading set inside the image/band itself
- **none** — pure visual band, no heading; caption if needed

A decorative rule-bar, dash, or empty accent block above an h2 **is a kicker** for budget purposes — styling doesn't exempt it.

## Hard quotas (blocking — the detector and critic both count these)

1. **≥4 distinct families per 8 sections**; shorter pages: ≥ ceil(n÷2) distinct families.
2. **No family twice in a row.** (Exception: consecutive `gallery` sections when the content is genuinely serial.)
3. **Kicker budget: ≤ ceil(sections÷3)**, counting the hero's.
4. **No two adjacent sections share the same opener type.**
5. **No opener signature repeated on >50% of sections** — the mechanical form of "the page has one shape."

## How to use it

- **Plan time (planner owns this):** every section in the page map carries `format:` + `opener:` tokens from this file. Check the quotas before handing off — a plan that violates them is defective before a line is built.
- **Build time:** implement the assigned formats exactly; re-deciding them is re-deciding the direction.
- **Critique time:** count sections, distinct families, consecutive repeats, kickers, opener signatures. Write the counts down. Numbers, not vibes.

Dense sections need breathe sections around them — when three dense families stack, the fix is usually inserting a `full-bleed-band` or `quote-monolith`, not restyling the cards. See `layout-craft.md` for the spacing-level rhythm underneath this, and `craft-floor.md` for the per-element quality floor.
