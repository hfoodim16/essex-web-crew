# Voice Spec — Gee-Kay Landscaping, Inc.

**Slug:** `gee-kay-landscaping` · **Written:** 2026-08-02 · **Source:** `dossier.md`

> **Exception on record.** There is no `client-answers.md` for this prospect. The lead
> approved building this rebuild from `dossier.md` + the prior `website-plan.md` as the
> input of record. That makes this spec *inferred*, not client-confirmed — so it is
> deliberately conservative: it tells the Builder what it may NOT say more than what it
> should. Every voice call here gets re-checked with George Reinhardt before launch.

## Register

A licensed landscape contractor with 45 years in one town, talking to a Livingston
homeowner standing in the driveway. He's been doing this since 1981; he doesn't need to
sell hard, and he doesn't perform. Short declarative sentences. Contractions. Names of
things — lawns, beds, mulch, pavers, walkways, Livingston.

**Three ways to miss it, all of which the old build hit:**

- **Too poetic.** "Meticulous by habit." "When the weather turns, we show up."
- **Too cute.** Trade puns, seasonal wordplay, winking at the reader.
- **Too vague.** Any sentence that would read identically on a competitor's site.

## The client's own words (the only phrasings we know are theirs)

From aggregator listings the business itself supplied:

- "A family run landscape construction and maintenance company"
- "lawn maintenance, design and installation of new, and upgrading of existing
  Landscapes and Hardscapes"
- "Servicing Livingston and surrounding areas"

These three phrases are the vocabulary floor. Prefer their nouns ("landscape
construction," "upgrading of existing") over prettier synonyms.

## Word budgets

| Slot | Budget |
|---|---|
| h1 | 4–9 words |
| Hero subhead | ≤ 28 words, one sentence |
| Section h2 | ≤ 7 words |
| Card / service body | 22–45 words |
| Story paragraph | ≤ 55 words each, ≤ 3 paragraphs |
| CTA label | 1–3 words (plus the phone number, which is its own label) |

Hard ceiling: **no paragraph over 60 words** anywhere (`copycheck.py` fails at 61).

## Banned on this site

- **Any owner quote.** We have no captured statement from George Reinhardt. The old
  build shipped `[placeholder: owner's note]` as visible bracketed text. Do not
  reintroduce it in any form — not as a quote, not as a placeholder, not as an italic
  pull-quote slot. The section that wanted one gets cut instead.
- **"Insured" / "bonded" / "fully insured."** The dossier confirms a NJ Home
  Improvement Contractor license and nothing else. No `[Insured — confirm]` chip either;
  the old build shipped that as visible text and it reads as a defect.
- **A license number.** None was captured. "Licensed NJ Home Improvement Contractor" is
  the full permitted claim.
- **Review counts, star graphics, or any rating other than the cited Angi 5.0.**
- **An email address.** None exists. Phone only.
- **Invented hours.** Hours are a visible `PLACEHOLDER` line.
- Marketing filler: *premium, bespoke, curated, elevate, transform, unlock, seamless,
  passion, dedicated, commitment to excellence, attention to detail, peace of mind,
  meticulous* (that last one is a reviewer's word — it may appear inside the real
  quote and nowhere else).

## Pre-authorized short sections

The facts are thin. These sections are **allowed to be short** and must not be padded:

- **Story / About** — three short paragraphs, all four facts (1981, Reinhardt family,
  Livingston natives, construction + maintenance). Nothing about philosophy.
- **Credentials** — three items, no prose.
- **Service area** — the confirmed line plus a visibly-labeled unconfirmed town list.
- **Reviews** — exactly the two captured quotes, attributed to their platform.

Nothing is ever added to a page to satisfy a check.

## Falsifiable facts available (≥1 must be visible; use several)

`1981` · `45 years` · `5.0 on Angi` · `Livingston, NJ` · `73 N Livingston Ave` ·
`three service lines` · `NJ Home Improvement Contractor license`

## Exempt from every check

The two real review quotes, the NAP block, and the JSON-LD. Never edited to pass a script.
