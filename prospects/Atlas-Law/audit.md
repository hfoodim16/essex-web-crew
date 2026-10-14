VERDICT: PASS — round 2 (signed off 2026-10-13; concept, not launch-ready)

# Audit — Atlas-Law (ATLAS LAW, Matthew Atlas)

**Gate A (Step 0):** Detector: 0 errors, 0 advisory on all 3 pages (builder evidence 15:57). Critic spot-check: `practice-areas.html` re-run → exit 0, matches the claim, so the rest of the evidence block is trusted and no further mechanical gates were re-run. In-file waivers accepted: `overused-font` (Mona Sans, sheet-locked; not on the banned set) · `all-caps-body` (the sheet's uppercase hero eyebrow is a label, not body) · `flat-type-hierarchy` / `cramped-padding` / `tight-leading` (static engine can't resolve clamp(); browser-rendered checks at 1440/375 don't flag them).

## Round 1 — 2026-10-13 (first full audit, includes the 2026-10-13 client-update delta)

Review round: 1
Paid calls this prospect: 0 ($0.00) · images: 2 (bin/gen-image) · video: none

### Measured (headless Chrome over http://localhost:8765, title confirmed "… | ATLAS LAW" before any measurement)

- Fail-visible (`impeccableMeasureHiddenText`, at rest, before any reveal forced): index 0% of 2,720 chars · practice 0% of 2,024 · about 0% of 1,846, at 1440 and 375. PASS.
- JS-off (main.js blocked): 0% hidden on all 3 pages. Reduced motion: 0% hidden. After a full scroll every clip-wipe element ends revealed (index 7/7, practice 10/10, about 1/1). PASS.
- Horizontal scroll at 1440/375: none on any page.
- Click-test: menu on practice-areas.html at 375 opens (aria-expanded true, 4 links) and closes. Every same-origin link and `#fragment` on all 3 pages resolves (0 bad). The 5 home tiles are whole-tile `<a>` links to existing anchors. No pointer cursor on any non-link. mailto/sms hrefs: every `sms:+19172134979` sits next to a visible 917-213-4979 (digits match Q24/Q25); every mailto is matt@matlas-law.com.
- Focus ring: 3px solid, white on blue fields, Kentucky blue on white/mist. Tab order at 375: skip link → wordmark → Email → Text → menu → hero CTA.
- **Tap targets under 44px:** header wordmark link 178×28 (desktop) / 109×18 (375) on all pages; "More about Matt →" 151×26; contact-band "matt@matlas-law.com" detail link 179×26 on all pages. FAIL (fix 2).
- Hero geometry at 1440×900: field 67→769px, eyebrow top 231px, portrait 388→884px, so 320px of empty blue above the portrait. About hero for comparison: field 76→706, portrait 193→821. (fix 1)
- Weight: matt-formal.webp 51 KB (LCP), plates 142/166 KB, og.jpg 62 KB. Fonts self-hosted, no CDN.
- Headshots unaltered: RMSE vs source 0.86% (formal) / 0.71% (casual), WebP compression only. Same pixel size.

### Client-answer fidelity (answers + 2026-10-13 update) — PASS
Q1 name in capitals everywhere · Q2 dates + availability quote · Q3 four employers on Home and About · Q4 "take clients from anywhere" next to the admissions · Q6 revenue band · Q8 all four items · Q9 every sub-item in order (home tile row 3 = Disputes then Real estate) · Q11 fees in 4 places · Q18 #0033A0 + white · Q19 wordmark only · Q22/Q27 no reviews/FAQ · Q23 admissions · Q24–26 email first, text second, no address · Q29 no Contact nav. **Update:** AI is on the first screen (eyebrow), the meta/OG descriptions, a dedicated home band, an About paragraph and an About table row; alternative fees/subscriptions in the same band, the practice-page line and the About "Fees" row. Every AI mention sits beside "I do the legal work". One gap: the OG card subtitle still reads "Business law · …" (fix 3).

### Attorney-advertising check on the AI/fee delta (NY 7.1 / NJ RPC 7.1)
- Comparisons with other firms: none ("insights … traditional law firms" omitted). PASS
- Promised savings or percentages: none ("fewer billable hours", "lower rates", "bang for their buck" omitted). PASS
- Guarantees: none. "stand behind the advice" reads as accountability (Sol and Astra agree). PASS
- Prices: none. PASS
- AI assisting him: "The tools assist. I do the legal work, check what they produce and stand behind the advice." / "the legal work and the judgment calls stay with me" / "AI-assisted. I do the legal work." PASS
- **Open, launch blocker (not a build fix):** "What you're paying for is my experience and my legal and business judgment, not my time." is his own sentence. It's accurate only if no matter is billed hourly; Sol and Astra both call it absolute. Planner question 16 already asks. If any work is hourly, use the plan's alternative #5.
- **Open, launch blocker:** the footer disclaimer/privacy text is proposed, not his. Now that the site says "AI-based firm", he should decide whether it needs a line on how client information is handled with AI tools (ABA Formal Op. 512; planner Q17). Only he can write it.
- packcheck law: PASS on comparisons and honors. `tap-to-call` FAIL is a documented exception: Q24 says email or text, the number is printed and tap-to-text everywhere, and NY 7.1(d) needs name + phone shown, which it is. Planner question 3 (call or text?) stays open for Harry.

### Content parity — PASS
`site-content.md` is the Squarespace AI starter draft; every block is on the plan's "Deliberately dropped" list with a reason (template filler, sample products, false "our team"). Parity source = the client's answers, all placed (see above).

### Real reviews / facts / logo — PASS
No reviews exist → no testimonial section, no placeholder. No logo exists (Q19) → the typographic wordmark is correct, not a substitute. No invented facts. UVA law school traces to the dossier's primary NY OCA record (claims-ledger row; confirm wording with client). Sol flagged it as unsupported by the client documents. Ruling: sourced, stays, on the confirm list.

### Imagery — two-way test — PASS
- `plate-warehouse.webp` (pa-hero, 1672×941): straight racking, consistent perspective, no readable labels or branding, no people, believable mid-size distribution floor. Editorial, not too perfect (some wrap, uneven cartons). Under a strong blue scrim. PASS.
- `plate-space.webp` (pa-real-estate, 1000×1250): mullions straight, door hardware plausible, no lettering on the glass, believable empty commercial unit, natural light. PASS.
- One register (editorial) beside the real studio headshot. No fake people or office.
- Real headshots: formal in both heroes + OG, casual on Home only, crop/resize only (measured above).

### Distinctiveness vs the last 3 design-memory rows — PASS
paul-da-silva-law Rev 3 (porcelain + brass, ruled ledger, Libre Caslon) · gee-kay Rev 2 (plan paper, surveyor ticks, Newsreader) · dasilva-associates (dark azul + gold, photo hero, Frank Ruhl). Atlas is white-first with full-strength royal-blue fields, a sans-display/serif-body inversion, a portrait overlap rather than an h1 on a photo, and clip-wipe + fill-sweep + a CSS scrub against rules-draw-in/slide-alternate/blur-focus. Section rhythm and hero framing don't mirror dasilva. Soft overlap only with FORA's own cobalt + sweep (not a client build, disclosed by the planner).

### Composition counts — PASS
| Page | Sections | Families | Max consecutive | Kickers / budget | Opener dupes (adjacent) |
|---|---|---|---|---|---|
| index | 7 | 7 | 1 | 1 / 3 | 0 |
| practice-areas | 7 | 7 | 1 | 0 / 3 | 0 |
| about | 4 | 4 | 1 | 1 / 2 | 0 |
- No opener shape on more than half the sections (index: kicker+h2 ×1, none ×2, bare-h2 ×2, in-media ×1, side-label ×1).
- Composition device: overlap. Visible on About (portrait crosses the field edge, top-aligned). On Home it's visible but the portrait is detached from the text (fix 1).
- Falsifiable facts ≥ 1: "over 15 years", four named employers, "$50 million to $200 million", "September 2025/2026", NJ and NY admissions. PASS.

### Copy voice — PASS (with launch-blocker confirm items)
copycheck 0 / aitells 0 (builder evidence, trusted after the spot-check). Say-aloud read of every string on all 3 pages (`--list`): no line he wouldn't say. Watched: "The tools assist." (Astra calls it scripted; Sol calls it a useful clarification; my ruling: keep, it's the AI-assists rule in his voice). "From the client side to my own firm" is plain enough. Advisory: "AI-assisted" (eyebrow, About row) vs "AI-based" (home h2, About p3). Both accurate, and "AI-based" is his term. Not a fix.
**Cold read (GPT-6.1 Sol, bin/ask-gpt, exit 0):** NOT READY, 2 offenders. (1) "…not my time." ETHICS/VAGUE → ruled a launch blocker for the client to confirm (above), not a builder edit, because the fix depends on a billing fact only he knows. (2) UVA unsupported → disagree, dossier-sourced. Every other AI/fee line is rated compliant and faithful. Neither update theme is missing or weak. Practice page CLEAN.

### Independent review (GPT-6 Astra, blind, 6 images, exit 0)
Scores: hierarchy 7 · typography 7 · color 8 · composition 5 · imagery 7 · motion-readiness 6 · copy 7 · conversion 9 · distinctiveness 5 · boldness 6.
Customer (COO, $80M): would email. Hesitates on disputes depth, AI confidentiality, "open to" sounding tentative. Owner: would share after a focused polish; asks for portrait placement, experience forward, clearer AI/fee paragraph; "does not justify a wholesale redesign".
AI-tell hunt: arbitrary tile geometry · repeated gradient fields · rotated side-labels · floating portrait · geometric headline character · slogan-like rhythms.
**Rulings:**
- Home hero proportions (defect 1, composition 5): **agree → fix 1.**
- Distinctiveness 5 / boldness 6 vs mine 8/8 (gap ≥ 2): **disagree.** Against the law category it's judged by (navy + gold + serif display), a white page with full-strength royal-blue fields, a wide grotesk and a giant footer wordmark is clearly its own. The client chose the colour. Astra scored the detached home hero, which fix 1 addresses.
- Tiles overstate sparse content / arbitrary emphasis: **disagree for this round.** These are the SHEET GO'd bento and card-grid formats, and the blue cards have a stated rule (the Q9 groups with nested items). Restructuring would be a redesign on a model's say. Noted for Harry.
- Rotated side-labels as template chrome: **disagree.** It's the sheet's opener device, it's an h2, and it becomes horizontal on mobile. Noted as a soft template tell.
- Bring employer credentials onto Home: **already there** (home-approach p1 names all four; Astra's crops skipped that section).
- About bio far from the portrait: **disagree.** The gap is the portrait overhang the sheet requires text to clear.
- "Not my time" absolute: **agree** → launch blocker above. "You know the rate" imprecise: **disagree**, it's his word ("rate … predictability").
- AI confidentiality: **agree** → launch-blocker note on the footer legal text.
- Disputes depth: thin facts, pre-authorized short in the voice spec → a content request to the client, not a fix.

### Scoreboard 1 — $10K Checklist (6/8)
1. Point of view — PASS. "Kentucky Field", nameable from the screenshots.
2. Typography — PASS. Mona Sans / Source Serif 4, self-hosted, clear scale (52px h1 → 13px labels, 216px wordmark).
3. Restrained color — PASS. 5 tokens + derived shades, used consistently, blue ≈ ⅓.
4. Hierarchy breathes — **FAIL.** The home first screen has 320px of dead blue above a portrait that starts below the h1; the hero reads stretched and the face is detached from the promise (fix 1).
5. Imagery with intent — PASS. 2/2 GENERATE slots real and passing; real headshots unaltered.
6. Motion whispers — PASS. clip-wipe + fill-sweep + one CSS scrub, reduced-motion gated, distinct from the last 3 rows.
7. Mobile designed — PASS. Proven by 6 mobile screenshots; Email + Text in the 375 header; no overflow at 360/375.
8. Invisible expensive stuff — **FAIL.** Tap targets under 44px (fix 2). Everything else passes: AA contrast, focus, semantic HTML, meta/OG/favicon, JS-off, LCP 51 KB.

### Scoreboard 2 — web-design-ultra rubric
| Dimension | Score | Note |
|---|---|---|
| Boldness / distinctiveness | 8 | committed full-field royal blue, wordmark as graphic |
| Visual hierarchy | 8 | h1 → strip → approach reads in order |
| Typography craft | 8 | clean inversion, good measure |
| Color & contrast | 9 | AA everywhere measured |
| Spacing rhythm | **6** | home hero void (fix 1) |
| Background / depth | 7 | field + grain; bands repeat |
| Imagery quality | 8 | real portrait + 2 honest plates |
| Responsiveness | 8 | mobile edited, not shrunk |
| Motion polish | 7 | quiet, working, single set-piece |
| Cohesion | 8 | one system across 3 pages |
Gate: one dimension below 7 → NEEDS-WORK.

### Three verdicts
- **Presentation:** FAIL this round ($10K 6/8; spacing rhythm 6).
- **Decision support:** PASS. Every decision-map line is answered on the page or a confirm item; no unsourced claim; fees and AI stated without savings, prices or comparisons. Open confirm items: "not my time", fee definitions, disputes scope, revenue band, UVA wording, quote edit, name form.
- **Operational readiness:** concept, not launch-ready. No form (by design); email/text links verified. Launch blockers: attorney approval of the footer disclaimer/privacy text (incl. an AI/confidentiality decision), the "not my time" billing fact, the call-or-text question.

### Fix list sent to the lead, round 1
1. **Home hero, portrait detached (index.html, `home-hero`; $10K #4, spacing rhythm).** At 1440×900 the portrait starts at 388px, 157px below the eyebrow, with 320px of empty blue above it. Match About's alignment: the portrait top sits within ~40px of the eyebrow top and still crosses the field edge by `var(--overlap)`. Get there by shortening the field (the sheet's `min(78vh,760px)` min-height is a sheet value, so it needs a lead ruling like the 4 strings) and/or top-aligning the portrait. Never widen the text column. Optional: a closer crop of the real photo (crop only). Done when: at 1440×900 and 1280×800 no blue taller than ~160px sits above the portrait, both CTAs and his full face are above the fold, and the overlap still crosses into the strip.
2. **Tap targets under 44px ($10K #8).** Header wordmark link (all 3 pages; 109×18 at 375), "More about Matt →" (index), contact-band "matt@matlas-law.com" detail link (all 3 pages). Give each a 44px minimum hit area (e.g. `display:inline-flex; align-items:center; min-height:44px`) with no visual size change. Done when every standalone link/button measures ≥ 44px tall at 375 and 1440.
3. **OG card misses the client update (assets/og.jpg; sheet integrity → planner/lead).** The subtitle reads "Business law · New Jersey & New York", while the update made AI-assisted the first-screen message and the meta already says "AI-assisted business law". Rebuild with "AI-assisted business law · New Jersey & New York" (same layout, real portrait, crop only). This is a sheet string (sheet ~L195), so it needs a lead ruling.

## Round 2 — 2026-10-13 (delta re-check of the 3 R1 fixes; sign-off)

Review round: 2
Paid calls this prospect: 0 ($0.00) · images: 2 (bin/gen-image) · video: none. Ledger closed at sign-off.

### Gate A
Detector: 0 errors, 0 advisory (builder evidence 19:56, all 3 pages exit 0; copycheck 0; aitells 0). Spot-check: fix 2 re-measured myself in headless Chrome over http://localhost:8741 (title "Business Lawyer in New Jersey & New York | ATLAS LAW" confirmed): wordmark 109×44 @375 / 178×44 @1440, "More about Matt →" 151×44, contact-band email 179×44, all 3 pages. Matches the claim exactly, so I trust the rest of the evidence and ran no other mechanical checks.

### Fix verification
1. Home hero (desktop-index-first-screen.png, 1440×900): eyebrow top ~133px, portrait top ~152px (≈20px, ≤40 ✓). Portrait crosses the field bottom into the stats strip (overlap kept). h1 on 2 lines. Both CTAs and his whole face above the fold. No blue void above the portrait. PASS.
2. 44px hit areas: PASS (measured above).
3. og.jpg: subline reads "AI-assisted business law · New Jersey & New York", same layout, real headshot crop only. PASS.

### Re-scored (others carried forward from Round 1)
- $10K #4 Hierarchy breathes: **PASS.** Eyebrow → h1 → subline → CTAs → portrait now reads as one unit.
- $10K #8 Invisible expensive stuff: **PASS.** Tap targets fixed; the rest carried from R1.
- Rubric, spacing rhythm: **8** (was 6). The void is gone, and the white gap under the field on the left is the overlap doing its job.

**$10K Checklist: 8/8**, with one documented exception: call or text only, no `tel:` link (client answer, Text 917-213-4979 in header and hero).
**Rubric:** boldness 8 · hierarchy 8 · typography 8 · color 9 · spacing 8 · background 7 · imagery 8 · responsiveness 8 · motion 7 · cohesion 8. No dimension below 7, boldness ≥ 8. PASS.

### Three verdicts
- **Presentation:** PASS.
- **Decision support:** PASS (carried from R1, nothing in the delta touches it).
- **Operational readiness:** concept, not launch-ready. Launch blockers: (1) Matt approves the footer disclaimer and privacy text, including how client information is handled with AI tools; (2) Matt confirms "…not my time" (does he bill any work hourly?); (3) call or text only with no `tel:` link, a documented exception he should confirm.

### Sign-off appends
design-memory.md row · copy-memory.md row · `skills/trade-copy/references/examples.md` §15 ("not my time": a contrast tail that states an unsourced billing fact; caught by the Sol cold read, passed both scripts). No tells.md append (no page-shape miss this build).
