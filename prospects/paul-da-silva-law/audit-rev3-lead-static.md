# Audit — `paul-da-silva-law` Rev 3 · LEAD-VERIFIED STATIC GATES

**Review round: 1** (Rev 3) · verified by the lead session · 2026-07-30

Run in the lead session because an API-side outage killed four consecutive critic agents
(two full critics, then both halves at the same millisecond — 04:57:19.224 / .225 UTC).
These are the gates that don't need a browser. Everything here was executed, not reported.

---

## Step 0 detector · **PASS**

`node skills/web-design-ultra/scripts/detect.mjs` — **exit 0 on all four pages**,
`0 errors, 0 advisory`. `grep impeccable-disable` → **zero waivers in file**; the
`cream-palette` / premium-consumer palette-family rules never fired, so the waiver the plan
pre-wrote in R3-3 was not needed.

## Copy-voice scripts · **PASS**

- `copycheck.py` — exit **0** on all four pages.
- `aitells.py` — exit **0** across all pages. Six hard checks PASS: no hero verb openers,
  no abstract-pair titles, ai-vocab cluster 0 distinct (max 2), no vague audience line,
  **7 checkable claims** (min 1), no card symmetry.

Copy is frozen this round, so advisories are logged, not actioned.

## Font swap complete · **PASS**

`grep -ci "besley\|schibsted"` → **0** in `style.css` and **0** in all four HTML pages,
fallback stacks included. Google Fonts links are `Libre Caslon Text:ital,wght@0,400;0,700;1,400`
and `Albert Sans:ital,wght@0,400..700;1,400`.

## Meta tags · **PASS (all four pages)**

| Page | title | description | OG | Twitter | canonical | favicon |
|---|---|---|---|---|---|---|
| index | 1 | 1 | 5 | 4 | 1 | 1 |
| practice-areas | 1 | 1 | 5 | 2 | 1 | 1 |
| attorney-bio | 1 | 1 | 5 | 2 | 1 | 1 |
| contact | 1 | 1 | 5 | 2 | 1 | 1 |

Meta descriptions name the services **and** the place (`"…in Newark's Ironbound. DWI, drug,
weapon and violent offenses, divorce, closings."`).

## NAP ↔ JSON-LD exact match · **PASS**

`LegalService` JSON-LD: `"telephone": "+1-973-344-0808"`, `"streetAddress": "385 Lafayette
Street"`, `"addressLocality": "Newark"`, `"postalCode": "07105"`.
Footer renders: `385 Lafayette Street` · `Newark, NJ 07105` · `973-344-0808` · fax
`973-344-3838`. Same address, same phone (JSON-LD in E.164 form, footer in display form —
standard). **No fabricated NAP, no invented hours, no invented license number.**

## Semantic HTML · **PASS**

Every page: exactly one `<header>`, one `<main>`, one `<footer>`, **exactly one `<h1>`**, real
`<section>` elements (7 / 3 / 5 / 3). `practice-areas.html` has a second `<nav>` — the sticky
progress index rail, correctly a navigation landmark.

## Keyboard focus ring · **PASS**

`:focus-visible{outline:2px solid var(--ouro-escuro);outline-offset:3px}` — a real visible
ring, and it uses the **AA-safe** brass (`--ouro-escuro #806026`) rather than `--ouro`.

## JS-off architecture · **PASS (static verification; live reload still owed)**

Each page carries, before the JSON-LD:

```html
<script>document.documentElement.className+=" js";window.__revealFail=setTimeout(function(){document.documentElement.classList.remove("js")},1200);</script>
```

`main.js:16` does `if (window.__revealFail) { clearTimeout(window.__revealFail); }`. Every
hidden-at-rest rule in `style.css` is scoped `html.js` **and** wrapped in
`@media (prefers-reduced-motion:no-preference)` — verified across `.drawx`, `.settle`,
`.cells`, `.cells>*`, `.cells>*>*`.

So there are two independent safety nets: no JS at all → `.js` is never added → nothing is
ever hidden; JS present but `main.js` missing or broken → the dead-man timer strips `.js`
after 1200 ms and the page reveals itself. This is the exact failure mode that shipped once
before (`fora-digital/audit.md`), engineered out rather than patched.

## Local-trade conversion patterns · **PASS, with one documented exception**

- **`tel:` links per page:** index 5 · practice-areas 6 · attorney-bio 4 · contact 5. CTA
  repeated top / mid / footer on every page.
- **Contact form: 3 fields** (`≤ 4` required).
- **Bar-advertising disclaimer survived** the rewrite: *"…attorney-client relationship. Prior
  results do not guarantee a similar outcome."*
- **Service-area block — DOCUMENTED EXCEPTION.** The pattern asks for a service-area block
  with real town names. `client-answers.md` **Q4 (Towns / areas served)** is
  `[UNKNOWN] — never stated`. Inventing a town list would violate content honesty, which
  outranks a conversion pattern, so the site is correctly anchored on what is actually
  known: Newark and the Ironbound (91 references, including both meta descriptions), plus
  Hudson County where it is a real biographical fact (the Ethics Committee). **Not a fail.**
  This is a question for Harry to ask the client, not for us to answer — it is already on
  the plan's confirm-with-client list.

## Map embed survived byte-for-byte · **PASS**

`contact.html` retains the OpenStreetMap `<iframe class="map-embed">`
(`openstreetmap.org/export/embed.html?bbox=…&layer=mapnik&marker=…`, `loading="lazy"`,
`referrerpolicy="no-referrer-when-downgrade"`, `title="Map location: 385 Lafayette Street,
Newark, NJ 07105"`) **and** the "Get directions" link to
`google.com/maps/search/?api=1&query=385+Lafayette+Street,+Newark,+NJ+07105`
(`target="_blank" rel="noopener"`). Same provider, same URLs, same attributes. Harry's
hand-edit is intact and, as at Rev 2, is still uncommitted.

---

## STILL OWED — browser-dependent, blocked on the API outage

1. Countable composition checks.
2. 10-dimension rubric (gate: no dimension below 7, boldness ≥ 8).
3. $10K Checklist items 1–7.
4. Measured WCAG AA contrast ratios — the value structure was inverted, so brass-on-porcelain
   and ink-band text are the spots to measure.
5. Interactive click-test, four pages × two viewports, real clicks.
6. Live JS-off reload (architecture above is verified statically; the reload is still owed).
7. Distinctiveness vs the last 3 `design-memory.md` rows and Rev 2's own screenshots —
   **the sharpest question of this round: genuinely a different site, or Rev 2 in a new font?**
8. Mobile-decision review at 375×812.
