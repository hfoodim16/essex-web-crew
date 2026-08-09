# Website plan — Smoke Test Plumbing (FIRE-DRILL FIXTURE, not a client)

> **SYNTHETIC FIXTURE — not a real prospect.** Written to pass `plan-lint.mjs`
> exactly. See `README.md` before editing.

## 1. Design Read

Reading this as: a local trade site for homeowners with an urgent problem, with a
plainspoken utilitarian language, leaning toward a sturdy slab + humanist sans
pairing and near-zero ornament.

## 2. Art direction — "Service Entrance"

Working-trade direction: the site reads like a well-kept van — everything labeled,
nothing decorative. Imagery **register: proud-contractor**.

## 3. Typography

- **Display:** Zilla Slab
- **Body:** Public Sans

## 4. Color system (`:root`)

| Token | Hex | Role |
|---|---|---|
| `--ink` | `#1b1f23` | Body and headline text |
| `--paper` | `#ffffff` | Page background |
| `--steel` | `#4a5560` | Secondary surfaces |
| `--signal` | `#0b5c3f` | CTAs and links |

## 5. Composition device

**Dominant column** — the services section runs a 7/5 split rather than 6/6, with
the copy column carrying the weight. Carried by section 3.

## 6. Motion

entrance = rise-in; hover = underline-draw; set-piece = none; tempo 420ms
`cubic-bezier(.２,.8,.2,1)`, 60ms stagger. GSAP tier 0.

## 7. Page map — one page

Each section carries its format and opener tokens.

1. Hero — format: hero, opener: none
2. Trust strip — format: stat-strip, opener: bare-h2
3. Services — format: split, opener: kicker+h2
4. Process — format: steps, opener: bare-h2
5. Service area — format: editorial-column, opener: numeral
6. Contact — format: cta-band, opener: side-label

Six sections, five distinct families (need ≥3), no family repeats back to back,
two kicker-style openers against a budget of 2, and no two adjacent sections share
an opener.

## 8. Images

No `GENERATE` slots — this fixture must never cost money. All image slots stay
labeled placeholders.
