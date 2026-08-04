# Voice spec — DaSilva & Associates, LLC (Paul Da Silva)

**Register:** Professional office (attorney) — banlist Tier 2. | Q8 words: **"PROFESSIONAL & FRIENDLY. COMMON LANGUAGE. NOTHING TOO FANCY."**
**Say-aloud persona:** Would Paul say this to a client sitting across the desk on Lafayette Street? He talks in short, complete, plain sentences — a lawyer explaining, not a brochure selling. Composed but contracted ("it's", "we'll"). Never ornate, never cute, never a pun. A person walking in here may have been arrested last night or be losing their marriage; the copy is calm, direct, and respectful of that.

## Sounds like them (verbatim from the questionnaire)
- "OPENED THE OFFICE WITH THE IDEA OF SERVING THE LOCAL COMMUNITY WHERE I WAS BORN AND RAISED."
- "WANTED TO PROVIDE THE SAME LEVEL OF SERVICE & ADVOCACY TO OUR CLIENTS THAT THE BIG LAW FIRMS PROVIDE THEIRS."
- "90% OF MY CLIENTS ARE REFERRALS FROM OTHER CLIENTS."
- "FOCUS ON NORTHERN NJ FOR REAL ESTATE & MATRIMONIAL CLIENTS. ENTIRE STATE FOR MUNICIPAL & CRIMINAL CLIENTS."
- His practice labels, his numbering: "① MUNICIPAL COURT ② CRIMINAL LAW ③ REAL ESTATE ④ MATRIMONIAL LAW."
Use these. Getting one of his own sentences onto his homepage beats anything composed for him.

## How he writes
Short declaratives, full sentences, no slang, no exclamation points. He uses plain professional vocabulary ("service & advocacy", "front of the line") and ranks things by numbering them. Match that: numbered where order matters, plain everywhere else. Contractions on. Digits for numbers ("24 years", "90%").

## The facts inventory (all body copy is ABOUT these — nothing else)
Opened May 2002 (24 years) · born and raised in NJ, son of immigrant parents · 90% of clients are referrals · big-firm-level service and advocacy from a local office · 4 practice areas in HIS order · two-tier service area (Northern NJ for real estate & matrimonial; entire state for municipal & criminal) · phone 973-344-0808 · fax 973-344-3838 · 385 Lafayette Street, Newark, NJ 07105 · "Se Habla Espanol / Nos falamos o portugues" (exactly as his site writes it — no accents; spelling is on Harry's Confirm list) · fluent Portuguese and Spanish · Rutgers BA 1993 · Touro JD 1996, Moot Court Board · Legal Aid Manhattan · Legal Aid Nassau County · NJ Office of the Public Defender (murder trials) · boutique litigation firm, Montclair · former Adjunct Professor, Fairleigh Dickinson · 4 years, Hudson County Ethics Committee · CourtTV and RTP-Portugal guest commentator · married, two children, tennis and hockey · old-site facts: "practical and precise approach... without the expense of needless additional litigation costs", every practice sub-item in site-content.md.

## Word budgets
| Slot | Words |
|---|---|
| Hero headline | 3–9 |
| Hero subhead | ≤ 30 |
| Practice-area card (Home) | ≤ 30 |
| Practice-area detail (Practice Areas page) | ≤ 90 each incl. its service list — the lists ARE the copy |
| Bio | site-content bio facts at full fidelity; prose ≤ 160 across 3 short paragraphs + the timeline |
| Service-area block | ≤ 40 — publish the two-tier split exactly; NO invented town list |
| CTA lines | ≤ 12 |

## CTA
Primary, sitewide, one intent: **"Call 973-344-0808"** (tap-to-call). Q13 said "same as on current web site" and the site leads with the phone. Secondary (contact page only): "Send a message" over the 4-field form. No "free consultation" anywhere — Q6 declined specials, and a free-consult offer he never made is an invented promise.

## Watch list (on top of banlist Tier 2)
- `aggressive` / `aggressively` — old-site word; his questionnaire voice is service-and-advocacy, not combat. Cap: once per page, only in the carried old-site fact about practical litigation, if at all.
- `expertly`, `prides itself`, `best choice` — old-site brochure phrasing; facts only, drop the phrasing.
- `fight`, `fighter`, `warrior`, `relentless` — defense-attorney cliché AND bar-advertising exposure. Zero uses.
- `Ironbound` — real place, but the trilingual-Ironbound identity is NOT the spine of this build. Zero uses in copy unless Paul asks; "Newark" and "the community where he was born and raised" carry it.
- Em dashes: ≤1 per 100 words, never twice in a section (trade-copy rule 4; taste-skill's total ban yields to this spec, but when in doubt use a period).

## Hard exclusions (from his answers — not gaps, refusals)
- NO testimonials/reviews anywhere (Q12: "just the ones already on web site" — his site has zero; the Lawyer.com quotes are NOT authorized).
- NO FAQ (Q15 N/A). NO fees, rates, retainers, payment types (Q16). NO specials/discounts/free consultation (Q6).
- NO bar admissions (never stated). NO email, NO hours, NO after-hours line (none published; omit from JSON-LD too).
- NO cell number (973) 747-6196 — Harry's project contact only.
- Never AI-generate Paul's face; never fabricate a CourtTV still or chyron.
- No case results, win rates, awards, "aggressive fighter" claims — bar-advertising exposure.

## Protected — never edited, exempt from checks
- The language line "Se Habla Espanol / Nos falamos o portugues" — carried exactly as the old site writes it.
- NAP: DaSilva & Associates, LLC · 973-344-0808 · fax 973-344-3838 · 385 Lafayette Street, Newark, NJ 07105.
- His four practice-area names and their order.
- (Q7 named nothing keep-word-for-word — there is no other locked copy.)

## Lyrical block
Yes — ONE first-person attributed block on the homepage, built strictly from his Q1 answer: opened May 2002 to serve the community where he was born and raised, with the same level of service and advocacy the big firms provide theirs. Attributed "— Paul Da Silva". Everywhere else stays plain. Do not compose beyond his sentences.

## Thin-fact sections (pre-authorized to be short — do not pad)
- **Service area:** two tiers, ~2 lines + the regions. He gave regions, not towns. Short is correct.
- **Personal line (bio):** married, two children, tennis and hockey — one sentence. Do not expand.
- **Recognition cards (bio):** each is the credential + one plain line max. The credential is the copy.
- **Contact:** NAP + form + map placeholder. No welcome prose.
- There is NO process section, NO results section, NO FAQ — cut, not shrunk. An empty section idea with no facts behind it does not go on a page.

## Hero uniqueness
Checked `grep -h -A2 '<h1' prospects/*/mockup/index.html` on 2026-08-03. Spent skeletons — do not use:
- Fragment triad ending in a year: "Fair. Honest. Since 1961." / "Straight answers. Clean books. Since 1983."
- "[Service] in [Town] since [year]." (gee-kay)
- Split-contrast pair: "Certified up here. Trusted down there."
- "Your …" possessive opener ("Your dream outdoor oasis…").
DaSilva's hero is a single plain declarative built on HIS differentiator (big-firm advocacy, local Newark office) — no triad, no "since [year]" construction in the h1 (May 2002 lives in the subhead/trust strip).

## Settled — do not re-flag
- "Matrimonial Law" (not "Family Law") — Paul, Q5, his term.
- "Municipal Court" as the lead practice area — Paul, Q5, his numbering.
- No testimonial section — Paul, Q12, 2026-08-03.
- Firm name is **DaSilva & Associates, LLC** ("DaSilva", no space) — resolved by his own logo asset (lead, 2026-08-03); the old footer's "Da Silva" was the old site contradicting its own mark. Use sitewide, in NAP and JSON-LD.
