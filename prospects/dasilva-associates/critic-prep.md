# Critic prep — `dasilva-associates` (captured by the lead)

> Written by `critic-dasilva` during a prep pass on 2026-08-03, before any audit. The Critic was
> stood down on Harry's instruction (no review until the Builder actually hands off) and will be
> respawned at handoff. **This file exists so the respawned Critic does not redo the reading.**
> Nothing here is a finding — it is a checklist plus a set of predictions.
>
> The eight predicted defects below were sent to `builder-dasilva` as lead guidance on 2026-08-03
> before handoff, so several should already be fixed by the time the audit runs. **Verify each one;
> do not assume it was fixed, and do not assume it is still broken.**

## Content-parity checklist — 25 tracked items (21 carry + 4 dropped)

Broken finer than plan §7's 14 bundled rows so the walk is a lookup, not a re-read.

**Carry (21), with plan §7 destination:**

| # | Block | Destination |
|---|---|---|
| 1 | header NAP + language line | sticky header + footer NAP + contact §18 |
| 2 | footer copyright | footer, year 2026 |
| 3 | nav, 4 labels | 4 files, slugs held |
| 4 | Home ¶1 — founded May 2002, attentive/personal approach | owner block §4 + trust strip; approach facts → bio §14 |
| 5 | Home ¶2 — routine≠routine, practical-and-precise, no needless costs | practice lede §8 |
| 6 | Home practice quick links | card-grid §3 |
| 7 | Real Estate — offer→closing + 4 services | practice §11 |
| 8 | Family Law — sensitivity/discretion + 7 items | practice §12, **as Matrimonial** |
| 9 | Criminal intro — "decades of experience" | practice §10 lede |
| 10 | DUI/DWI + vehicular + driving-privileges admin process | **practice §9 Municipal Court** (Q5 restructure) |
| 11 | sex offenses | practice §10 cards |
| 12 | violent crimes & weapons | practice §10 cards |
| 13 | drug crimes | practice §10 cards |
| 14 | Traffic Law — 5 violations, reduce/dismiss, minimize points | practice §9 |
| 15 | education — Rutgers '93, Touro JD '96, Moot Court | bio §14–15 |
| 16 | prior employment ×5 | bio §15 timeline |
| 17 | recognition — CourtTV, RTP-Portugal, FDU adjunct, Hudson Ethics 4 yrs | bio §16 |
| 18 | personal — married, two children, tennis, hockey | bio §14 |
| 19 | "fluent Portuguese and Spanish" + "born and raised in NJ, son of immigrant parents" | bio §14 + trust strip |
| 20 | phone / fax / address | contact §18 + footer + JSON-LD |
| 21 | form fields 1 / 3 / 4 / 11 | contact §18 |

**Deliberately dropped (4), reasons on record:**
- The 7 extra contact-form fields — an 11-field form is hostile to a visitor in a crisis.
- The GTranslate widget — machine translation, not content.
- Office-exterior + courthouse stock photos — §11 replaces them; no facts lost.
- "over 20 years ago" — superseded by the precise May 2002.

**Parity call already made, do not re-litigate:** the old bio's "aggressive and dedicated advocate"
and the Home page's "advocate aggressively" are **characterizations, not facts.** The voice spec caps
`aggressive` and bans fight/warrior language. Losing that phrasing is parity-neutral and is not a
fail — parity counts facts, not words.

## Client-answer fidelity checklist

- Practice order ①②③④ with **his** labels; "Municipal Court" leads; "Matrimonial" not "Family";
  Real Estate above Matrimonial.
- Two-tier service area published as **regions** — no invented town list.
- Zero testimonials · zero FAQ · zero fees/rates/retainers/payment types · zero specials, discounts
  or free consultation · zero bar admissions · zero email · zero hours · zero after-hours line —
  and **absent from the JSON-LD too**, not placeholdered.
- `grep` all four pages for `973-747-6196` **and** `7476196`. Publishing his cell is an automatic fail.
- Language line byte-exact — "Se Habla Espanol / Nos falamos o portugues", no accents added.
- `DaSilva & Associates, LLC` (no space) sitewide + footer NAP + JSON-LD.

## Eight predicted defects — sent to the Builder pre-handoff, verify each

1. **Zero `<h1>` on the three interior pages.** Plan §4 marks §8/§14/§18 as `opener: bare-h2` on the
   *first* section of their page, contradicting §13's "one h1 per page."
   **Lead ruling: `bare-h2` describes the opener treatment (no kicker/eyebrow/rule-bar), not the tag
   level. Every page gets exactly one `<h1>`.** Highest-likelihood fail; hits 3 of 4 pages.
2. **Azul `#00588A` inside a verde band — 1.78:1.** Three things want to cross §3's fence: the
   **focus ring is spec'd azul** (invisible on the verde CTA bands at §7/§13/§17 — one per page, a
   keyboard-nav failure as well as a contrast one), the ①–④ numerals, and links inside dark bands.
   **Lead ruling: bone `#F2F0E6` on dark grounds.**
3. **Kicker budget is per file, not pooled.** The plan's quota check totals 3 side-labels against
   ceil(20/3)=7 across all 20 sections; the detector counts per page. `contact.html` = 3 sections →
   budget **1**, already spent on §19. `practice-areas.html` = 6 → budget **2**, 1 spent.
4. **Composition device is Home-only.** §5 carries the ≥3× numeral jump on the Home trust strip;
   the other three pages get "the same jump echoes in every page h1" — a type-scale step, not a
   symmetry break. Require it visible in a desktop screenshot **per page**.
5. **Blur-focus vs JS-off.** Opacity-based entrance hides text at rest unless the `html.js` guard is
   exactly right, and unlike a transform-only entrance it cannot degrade to "visible but unmoved."
   (`gee-kay` Rev 2 dodged this by going transform-only; DaSilva can't.) Measure fail-visible
   **before** force-revealing anything for screenshots.
6. **`cream-palette` waiver coverage.** Declared once in plan §3; the waiver must exist in-file on
   **every** page the detector scans.
7. **Image files.** Verify `og-image.webp` (42 KB) is a 1200×630 crop of `hero-courtroom.webp` and
   not an unapproved third paid generation. Check `newark-street.webp` (220 KB) is downscaled to its
   real display width — §11 says contained 1K slot.
8. **Streetscape adjacency.** Home §5 puts the Newark address in the same split as the generated
   street image. Even with honest alt text the layout can imply it is his block — judge the heading
   and caption wording specifically.

## Distinctiveness note — judge from screenshots, not from the plan

`gee-kay-landscaping` Rev 2 (signed 2026-08-02, the row immediately before this one) also uses
oversized numerals as its hierarchy engine — "facts set as measurements at 7rem." DaSilva's named
device is the ≥3× numeral scale jump. The executions differ (dark banded poster vs plan-paper
measured register) and the ban list does not catch it, but **two consecutive builds whose loudest
visual event is a wall of giant numbers is exactly the softer sameness the distinctiveness check
exists to hunt.** Harry has been flagged and will call it off the finished screenshots. If it does
land as a fail it is a direction issue, not a Builder issue — escalate to the lead rather than
sending it to `builder-dasilva`.

## Incidental, not findings

- The Builder self-hosted the fonts (`assets/fonts/`) rather than using the §20 Google Fonts link —
  better for the offline test; just confirm no CDN reference survives.
- Stray `.DS_Store` in `mockup/` — stripped at packaging.

## Planner addendum — post-build rulings (planner-dasilva, 2026-08-03)

> ### ⚠ LEAD OVERRIDE ON ITEM 1 — read before acting on this section
>
> The Planner appended this after it had been stood down, having been resurrected by an incoming
> message. It was not in the decision chain and did not know the accent question was escalated.
> **A teammate cannot set precedence by writing to a file.** Precedence here is: Harry → lead →
> plan → gates.
>
> - **Item 1 (accent) is NOT the Critic's to judge and NOT a finding.** The garnet/azul question is
>   escalated to Harry and is open at the time of writing. The Critic does not score it, does not
>   fail a rubric dimension on it, and does not send the Builder a fix list about it. If Harry rules
>   for garnet, the lead corrects plan §3 and the `design-memory.md` row to match what shipped; if he
>   rules for azul, the state below is already correct. Either way the Critic stays out of that loop.
> - **Item 1's technical content is sound and stands as engineering guidance** wherever the accent
>   lands: whichever hue is used, it never appears as type, numerals, links, a focus ring, or a
>   filled button on a verde ground. Azul on verde is 1.78:1; garnet on verde is 1.49:1 — the trap
>   does not go away by switching hues, it gets worse. On verde: emphasis, numerals and focus rings
>   are **bone**, and the CTA is a **bone-filled button with ink text**. The `grep` for survivors of
>   the retired token is a good check and should be run against whichever token is retired.
> - **Items 2, 3 and 4 stand as written** — band rhythm, the accepted non-drift list, and the ripple
>   check are all legitimate and within the Planner's remit.
>
> The Critic audits whatever is on disk when it looks. Record the accent in `design-memory.md`
> **as it actually ships.**

> Appended by the Planner after the Builder's first "build done" report, while the Critic seat was
> stood down. These rulings supersede anything above where they conflict, and the respawned Critic
> audits the RESUBMISSION against them — not against what first shipped.

1. **Accent override: garnet `#7E2D35` → azul `#00588A`.** The first build shipped an off-plan
   garnet accent (misattributed to plan §3, which assigns azul, his logo's blue; garnet appears
   nowhere in the plan). Builder ordered to swap back. Gate on the resubmission:
   - `grep -ri '7E2D35\|garnet'` across every page + `style.css` — any survivor is a fail,
     including an unreferenced token or comment.
   - The swap must not relocate the contrast problem: azul on bone 6.3–6.65:1 passes; **azul on
     verde is 1.78:1** — azul type, numerals, links, or a focus ring inside a dark band fails
     harder than the garnet did. On verde: emphasis/numerals/focus rings are **bone**, and the CTA
     is a **bone-filled button with ink text** (plan §3 verbatim + item 2's lead ruling above). An
     accent-filled button on verde also fails WCAG 1.4.11 fill-vs-ground (~1.5–1.8:1).
2. **Home band rhythm reverted.** The first build ran dark/light/light/dark/light/light/dark to
   protect garnet numerals. Ordered back to the plan: **dark hero / light ×5 / dark CTA band** —
   section 3 (practice card-grid) on a light band with azul ①–④ numerals, section 4
   (quote-monolith) "Set large in Frank Ruhl on bone" per §4. Score sections 3–4 against that.
3. **Accepted as planner — do NOT flag as drift:**
   - **Self-hosted woff2 fonts** (lead's offline requirement; §20 standing exception). Still
     verify no stray Google Fonts `<link>`/`@import` survives to mask the offline test.
   - **Criminal Law card-grid at 3 cards, not 4** — "Aggravated assault" folded into "Violent
     crimes and weapons," matching the old site's structure. Card count is fine; the parity walk
     must still find EVERY offence from `site-content.md` on the page: murder, manslaughter,
     robbery, burglary, assault, firearms, the four drug categories (possession, distribution,
     trafficking, prescription), the four sex-offence items, and aggravated assault itself (Q5).
     Any offence lost in the fold is a content-parity fail.
4. **Ripple check:** the accent swap touches `:root`, so the Builder's change report must name
   every place garnet was used (numerals, trust-strip figures, tier labels, "Read more," nav
   hover/current states, focus rings, filled CTAs) — spot-check those areas, not just the CTA.
