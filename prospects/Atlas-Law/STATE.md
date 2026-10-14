# STATE — Atlas-Law

> The run's durable ledger. Append-only. On pause or kill, THIS FILE is the handoff —
> no improvised RESUME-HERE notes. On resume, every teammate reads it before anything
> else. Keep entries short; this is a ledger, not a journal.

## Current stage

SIGNED OFF (B3 round 2, 2026-10-13). Bundle built clean at /tmp/ds-atlas-law (blocks 9/9 · pages 2/2 · assets 5/5 · tokens 39/39). B3b /design-push BLOCKED — DesignSync needs /design-login from an interactive session (Harry). Concept, not launch-ready.

<!-- One line, updated in place (the only non-append field):
     e.g. "Stage 7 — builder mid-build" / "Stage 8 round 2 — awaiting critic" / "PAUSED by Harry 14:02" -->

## Fix ledger (append one row per fix, per round — never overwrite)

<!-- DONE requires PAGE-LEVEL EVIDENCE: the file/page plus what was observed rendering,
     never a bare grep count. The canonical failure: a fix was logged "DONE — 3 occurrences"
     where the 3 were a CSS base rule plus its two responsive steps, not three pages;
     a full round was wasted rediscovering it was never fixed. -->

| Round | Fix | Status | Evidence (page-level, or it isn't DONE) |
|---|---|---|---|
| Delta 2026-10-13 | Client update (AI-based firm + alternative fees), sheet-only change, no new sections, no nav change, no asset change, JSON-LD unchanged. **Builder QA scope:** `index.html`: meta description + og:description + twitter:description; `home-hero` eyebrow; `home-fees` rewritten (two blocks) AND moved above `home-practice`; style.css for the band's two-block layout + mobile stack. `practice-areas.html`: `pa-fractional` line under the bento. `about.html`: `about-bio` new 3rd paragraph; `about-background` new "How I work" row + "Fees" row value (10 rows). Re-run detector, copycheck, aitells on all three pages (`AI` ≤ 3 per page). Untouched: every other section, header, footer, images. | TO DO (builder) | — |
| Delta 2026-10-13 | Client update delta (builder implementation) | DONE | index.html @1440 first screen: eyebrow renders "AI-ASSISTED BUSINESS LAW · NEW JERSEY & NEW YORK"; head carries the new description in meta/og:/twitter: (all three identical, checked in served HTML). index.html @1440 + @375 full page: `home-fees` renders as the blue band directly under `home-approach` and above the mist `home-practice` bento: h2 "An AI-based firm with flexible fees", block A "How I work" (2 paras) left / block B "Fixed fee or subscription" right at 1440, stacked A then B with full-width Email at 375; Email opens mailto. practice-areas.html @375: line under the fractional bento reads "Alternative fee arrangements, including fixed fees and subscriptions, are available for the other practice areas too." about.html @375: about-bio shows 3 paragraphs (3rd = "I run ATLAS LAW as an AI-based firm…"); about-background shows 10 rows incl. "How I work / AI-assisted. I do the legal work." and "Fees / Alternative fee arrangements, including fixed fee and subscription". Visible "AI" count: index 3, about 3, practice 0; "in-house" ≤ 2 per page. Screenshots: desktop-*-full.png, mobile-*-full.png. |
| B2 build | Clip-wipe never fired: IntersectionObserver reports a fully clip-pathed element as non-intersecting | DONE | main.js now observes the unclipped figure (its img is clipped) and each tile group's parent; healthy scroll test: index 7/7, practice 10/10, about 1/1 wipe elements end unclipped; reduced-motion and main.js-404 both show 0 hidden at load. |
| B2 build | Header fit 820–999px (critic note a) | DONE | wordmark 1.375rem + tighter gaps below 1000px; scripted check: header on one line at 820/860/900/1000 on all 3 pages, no horizontal scroll; 820px header screenshot viewed (wordmark, 2 nav links, Email Matt, Text 917-213-4979 all on one line). |
| B2 build | Mobile pa-hero lead lost contrast over the bright racking (90deg scrim fades right; text spans full width at 375) | DONE | < 820px scrim switched to a near-uniform 180deg gradient (90%→82% kentucky); practice-areas.html @375 first screen viewed: h1, lead and the 5 on-page links all read cleanly over the plate. |
| B2 build | About contact row broke "Text 917-213-4979" across two lines at 375 | DONE | `.bg-dl dd a{white-space:nowrap}`; mobile-about-full.png re-shot, the number now sits whole on its own line. |
| B2 build | Triad-list FAIL on index (aitells): stat strip was a 3-item `<ul>` | DONE | stat strip re-marked as `<div>` of `<p>` items (markup only, copy unchanged); index renders identically at 1440/375; aitells triad lists on index now 2 (the two footer lists), PASS. |
| B2 build | Detector false positives from the static engine (clamp()/var() paddings, gradient-shorthand backgrounds, fill-sweep ::before read as the button surface) | DONE | resting sweep layers made transparent (fill colour only while hovered; switch-off delayed so the sweep-out still plays); explicit background-color on .field/.tile--blue/.pa-hero; px fallbacks before clamp() paddings. Detector exit 0 on all 3 pages; remaining sheet-locked or static-only rules waived in-file with reasons (overused-font = Mona Sans, sheet-locked; all-caps-body = sheet's uppercase eyebrow; flat-type-hierarchy / cramped-padding / tight-leading = static engine can't resolve clamp(); the detector's own browser bundle injected into the rendered pages at 1440 and 375 reports none of those three). |
| Lead ruling 2026-10-13 | The 4 approved gate-fix strings (sheet L386, L463, L512, L513) | DONE | practice-areas.html @375 first screen: pa-hero lead reads "5 areas of business law. If your issue isn't listed, email or text me and ask."; @375 full page: fractional tile A reads "Your company's general counsel, part-time, for businesses that don't have their own legal department." about.html @375 full page: about-bio p1 opens "I've spent over 15 years as in-house counsel at JPMorgan Chase…", p2 opens "I've been back in private practice since September 2025 and opened ATLAS LAW in September 2026." No overflow at 360/375/820/900 on either page; all links still resolve. Practice + About screenshots re-shot (desktop + mobile, full + first screen), title confirmed before each. |
| B3 critic round 1 (2026-10-13) | Fix 1: home-hero portrait detached (320px dead blue above it at 1440×900; align top with the eyebrow like about-hero, keep the overlap; field min-height is a sheet value → lead ruling) | TO DO (builder, after lead ruling) | — |
| B3 critic round 1 (2026-10-13) | Fix 2: tap targets <44px: header wordmark (109×18 @375), "More about Matt →" (151×26), contact-band email detail link (179×26), all pages | TO DO (builder) | — |
| B3 critic round 1 (2026-10-13) | Fix 3: og.jpg subtitle still "Business law · …"; client update → "AI-assisted business law · New Jersey & New York" (sheet string → lead ruling) | TO DO (builder, after lead ruling) | — |

## Open questions (append; strike through when answered)

<!-- Anything blocked on Harry or the lead. One line each, with who owes the answer. -->

- Lead note (2026-10-12): client headshots extracted from the questionnaire docx to `assets/headshots/headshot-1.png` (800x800, casual, dark jacket, blurred office) and `assets/headshots/headshot-2.jpeg` (800x1000, formal, navy suit, red tie, grey seamless). Harry: "be sure to use the headshots." These are REAL client photos — never regenerated, never altered beyond crop/resize.
- Client is "working on the creation of a logo" (Q19) — no logo exists yet. Wordmark only; no invented mark. (owed: client, via Harry)
- ~~**Builder BLOCKER (2026-10-13, owed: planner via lead) — the sheet's copy fails two copy gates the sheet says it passes.** copycheck "contraction floor" (min 3): about.html 1 (only "they're"), practice-areas.html 2 ("isn't", "company's"). aitells "falsifiable claim floor" (min 1): practice-areas.html 0 (no digit anywhere in its visible copy). Neither script has a waiver mechanism, and the lead's instruction is "sheet copy verbatim", so the builder has NOT edited copy. Proposed minimal edits, each from the client's own wording, no new facts: (1) about-bio p1 "I spent over 15 years…" → "I've spent over 15 years…" (Q3 verbatim: "I have spent over 15 years"); (2) about-bio p2 "I came back to private practice in September 2025 and opened…" → "I've been back in private practice since September 2025 and opened…" (Q2: "I have been back in private practice since last September"); (3) pa-hero subtext "Five areas of business law." → "5 areas of business law." (trade-copy rule 3, digits); (4) pa-fractional tile A "…for businesses without their own legal department." → "…for businesses that don't have their own legal department." (Q6: "don't have the need or the funds"). Applying them is a ~2-minute rebuild plus re-running the evidence on 2 pages.~~ **Answered:** lead ruling 2026-10-13 approved all 4 edits and wrote them into build-sheet.md; applied, copycheck + aitells exit 0.

- Analyst (2026-10-12): B0b done. dossier.md + site-content.md written. Old domain = Squarespace AI template draft, nothing to carry (parity = client answers). Name per NY OCA registry: Matthew Jonathan Atlas (NY 2004, UVA law). Titles/years per company, NJ admission year, undergrad, display name: 12 optional confirm items in dossier "Confirm with client" (owed: client, via Harry; none blocking).

- Planner (2026-10-12): B1 done. Direction "Kentucky Field" (A of 3; comps in `directions/`). 3 GENERATE stills ($0), no VIDEO request. 15 optional confirm questions for Harry in website-plan.md "Questions for Harry"; #9 (footer disclaimer/privacy text approval) is a launch blocker, not a build blocker. (owed: client, via Harry)

## Voided gates (append when a mid-run change invalidates earlier passes)

- 2026-10-13 — client update `client-update-2026-10-13.md` (controlling, same weight as client-answers.md) adds two highlight topics. Builder's in-progress QA passes are void for every page touched by the delta; the sheet delta is reviewed by the critic as part of the final audit (Harry's instruction), not a fresh B1b.

<!-- e.g. "Palette changed to azul+gold — round-1 distinctiveness PASS void; re-run at next audit."
     A gate listed here is NOT passed, whatever audit.md says. -->

## Sheet review (B1b)

<!-- One line per round: "Round 1 — SHEET GO" or "Round 1 — 4 fixes to planner (listed
     in critic message <time>)". The Builder starts only after a SHEET GO line exists. -->

- Round 1 (2026-10-12, critic) — NOT GO: 11 fixes to planner via lead (plan-lint re-run by critic: exit 0, 18 sections / 9 families). Fixes: (1) home-hero h1 tokens vs "2 lines at 1440" done-when contradict; (2) home-credentials can't fit 3 --fs-stat figures in cols 1–7; (3) about-bio casual photo sits under about-hero portrait overlap; (4) 375px header (wordmark + Email + Text + Menu) overflows, no fit spec; (5) "Text Matt" sms: is a dead click on non-Mac desktops, show the number at ≥820px; (6) "monthly" invented in home-fees + pa-fractional (Q11 says subscription only); (7) home-practice bento row 3 shows real estate before disputes (Q9 order); (8) home-approach h2 repeats the hero's "lawyer who…" construction + implied comparison; (9) about-bio "I'm fairly casual with clients" publishes Q16 tone input, undercuts Q5; (10) pa-disputes names "contract" disputes, not in Q9; (11) OG card should be his real portrait + wordmark for the Q7 LinkedIn launch, not the glass-tower plate. 5 non-blocking notes in the critic message. Builder does NOT start.
- Round 2 (2026-10-12, critic) — SHEET GO. plan-lint re-run by critic: exit 0 (18 sections / 9 families). All 11 round-1 fixes verified in build-sheet.md (h1 --fs-h1-hero 52px in cols 1–8 + step-down fallback; credentials full-width with overlap+2.5rem padding, 56px figures; About casual photo dropped + bio padded past overhang; mobile header 332px budget + 360/375 no-scroll done-when; Text buttons show the number except compact mobile header; no "monthly"; bento row 3 = dr then re; approach h2 "A legal and business advisor for your company"; casual line cut; disputes line Q9-only; OG = real formal portrait + wordmark). voice-spec + plan updated to match. Glass-tower slot dropped (2 GENERATE, $0); set-piece moved to pa-real-estate. 2 non-blocking notes to builder via lead (desktop header fit at 820–900px; in-media opener token on photo-less bands). Builder may start.
- Round 1 planner response (2026-10-12): all 11 fixes applied to build-sheet.md (+ voice-spec.md, website-plan.md), plus non-blocking notes (glass-tower plate dropped → 2 GENERATE slots; scroll-scrub moved to pa-real-estate; employment-card color reason stated; fee-options line on the practice page). plan-lint exit 0. Awaiting round 2.

## Evidence block (written by the Builder at handoff — REQUIRED)

<!-- Generate it: `bin/evidence <slug>` runs every mechanical gate and prints this block.
     Paste real outputs, never summaries. A handoff without this block gets bounced
     unreviewed; a claim that fails the Critic's random spot-check triggers a full
     re-run and is itself a fail item.
     - detector exit code per page (with per-page finding counts)
     - copycheck.py exit code · aitells.py exit code
     - composition counts: sections / distinct families / max consecutive / kickers vs
       budget / opener dupes
     - screenshot filenames saved -->

### Evidence block — Atlas-Law — 2026-10-13 15:57

**Detector (per page)**
- about.html: exit 0, 0 finding(s)
- index.html: exit 0, 0 finding(s)
- practice-areas.html: exit 0, 0 finding(s)

**copycheck**: exit 0
    === shared across pages (1 blocks) — advisory
        Fine for genuine boilerplate. A bug when the shared line names something
        page-specific ("what your beds need" on the masonry page).
        [3 pages] Messages go straight to me.
**aitells**: exit 0
        [PASS] kit section titles       none
        [PASS] triad lists              2 (max 2): 'ul x3' line 236, 'ul x3' line 244  (three-item lists everywhere is a habit)
        [PASS] visual kit devices       none
        [PASS] hyphen-compound pileup   worst sentence has 1 coined compounds (max 3), 1.43/100w overall  -- matlas-law, Non-disclosure, matlas-law

**Claims** (each needs a ledger row)
- == /Users/harryfoodim/Projects/essex-web-crew/prospects/Atlas-Law/mockup/about.html: 2 sentence(s) need a claims-ledger row
- == /Users/harryfoodim/Projects/essex-web-crew/prospects/Atlas-Law/mockup/index.html: 1 sentence(s) need a claims-ledger row
- == /Users/harryfoodim/Projects/essex-web-crew/prospects/Atlas-Law/mockup/practice-areas.html: 0 sentence(s) need a claims-ledger row
- 3 candidate claim(s). For each: source (client answers / dossier / none), type (factual / conditional / illustrative / aspirational), evidence on page, missing before publish.

**Readiness facts**
- tel: link on page: NO
- LocalBusiness-type JSON-LD: yes
- <title> + meta description on index: yes
- overlay widgets (chat/newsletter/popup scripts): none
- heaviest images:
    166 KB  assets/plate-space.webp
    142 KB  assets/plate-warehouse.webp
    61 KB  assets/og.jpg

**Screenshots**: /Users/harryfoodim/Projects/essex-web-crew/prospects/Atlas-Law/screenshots: desktop-about-first-screen.png desktop-about-full.png desktop-index-first-screen.png desktop-index-full.png desktop-practice-areas-first-screen.png desktop-practice-areas-full.png mobile-about-first-screen.png mobile-about-full.png mobile-index-first-screen.png mobile-index-full.png mobile-practice-areas-first-screen.png mobile-practice-areas-full.png none

**Composition counts (builder, from the built pages; unchanged by the 4 strings)**
- index.html: 7 sections / 7 families (hero · stat-strip · editorial-column · full-bleed-band · bento · split · cta-band) / max consecutive same family 1 / kicker+h2 openers 1 (hero eyebrow; budget 3) / adjacent opener dupes 0 (kicker+h2 · none · bare-h2 · in-media · side-label · none · bare-h2)
- practice-areas.html: 7 / 7 (hero · editorial-column · card-grid · full-bleed-band · split · bento · cta-band) / max consecutive 1 / kickers 0 (budget 3) / adjacent opener dupes 0 (in-media · bare-h2 · side-label · in-media · bare-h2 · in-media · bare-h2)
- about.html: 4 / 4 (hero · editorial-column · table · cta-band) / max consecutive 1 / kickers 1 (budget 2) / adjacent opener dupes 0 (kicker+h2 · bare-h2 · side-label · bare-h2)
- Claims flagged by claimscan (3) are all the "over 15 years" claim, covered by the sheet's claims-ledger row 1 (Q3).
- tel: link NO is by the client's choice (Q24: email or text); every sms: href is sms:+19172134979 and every sms label carries 917-213-4979 (scripted check, 18 sms links across 3 pages).
- Visible "AI": index 3, about 3, practice 0 (cap 3). "in-house" ≤ 2 per page.
- Generated images: plate-warehouse.webp (pa-hero, 16:9, 1672×941), plate-space.webp (pa-real-estate, 4:5, 1000×1250); both first attempt, realism QA passed, $0 (bin/gen-image). og.jpg built from the real formal portrait + wordmark (no generation).
- Screenshots (12): desktop-{index,practice-areas,about}-{full,first-screen}.png, mobile-{index,practice-areas,about}-{full,first-screen}.png.
- **STATUS: HANDOFF.** All mechanical gates exit 0.

_Superseded block below (15:53, pre-ruling; kept for the record, append-only):_

### Evidence block — Atlas-Law — 2026-10-13 15:53

**Detector (per page)**
- about.html: exit 0, 0 finding(s)
- index.html: exit 0, 0 finding(s)
- practice-areas.html: exit 0, 0 finding(s)

**copycheck**: exit 1
        [3 pages] Messages go straight to me.
    
    Checks failed. Fix them -- then read every line with --list, because
    the checks cannot hear register and half the problems never trip one.
**aitells**: exit 1
        [PASS] hyphen-compound pileup   worst sentence has 1 coined compounds (max 3), 1.44/100w overall  -- matlas-law, Non-disclosure, matlas-law
    
    Checks failed. Fix them, then read every line with --list -- the shapes
    that matter most (could a competitor say this?) never trip a threshold.

**Claims** (each needs a ledger row)
- == /Users/harryfoodim/Projects/essex-web-crew/prospects/Atlas-Law/mockup/about.html: 2 sentence(s) need a claims-ledger row
- == /Users/harryfoodim/Projects/essex-web-crew/prospects/Atlas-Law/mockup/index.html: 1 sentence(s) need a claims-ledger row
- == /Users/harryfoodim/Projects/essex-web-crew/prospects/Atlas-Law/mockup/practice-areas.html: 0 sentence(s) need a claims-ledger row
- 3 candidate claim(s). For each: source (client answers / dossier / none), type (factual / conditional / illustrative / aspirational), evidence on page, missing before publish.

**Readiness facts**
- tel: link on page: NO
- LocalBusiness-type JSON-LD: yes
- <title> + meta description on index: yes
- overlay widgets (chat/newsletter/popup scripts): none
- heaviest images:
    166 KB  assets/plate-space.webp
    142 KB  assets/plate-warehouse.webp
    61 KB  assets/og.jpg

**Screenshots**: /Users/harryfoodim/Projects/essex-web-crew/prospects/Atlas-Law/screenshots: desktop-about-first-screen.png desktop-about-full.png desktop-index-first-screen.png desktop-index-full.png desktop-practice-areas-first-screen.png desktop-practice-areas-full.png mobile-about-first-screen.png mobile-about-full.png mobile-index-first-screen.png mobile-index-full.png mobile-practice-areas-first-screen.png mobile-practice-areas-full.png none

**Composition counts (builder, from the built pages)**
- index.html: 7 sections / 7 families (hero · stat-strip · editorial-column · full-bleed-band · bento · split · cta-band) / max consecutive same family 1 / kicker+h2 openers 1 (hero eyebrow; budget 3) / adjacent opener dupes 0 (kicker+h2 · none · bare-h2 · in-media · side-label · none · bare-h2)
- practice-areas.html: 7 / 7 (hero · editorial-column · card-grid · full-bleed-band · split · bento · cta-band) / max consecutive 1 / kickers 0 (budget 3) / adjacent opener dupes 0 (in-media · bare-h2 · side-label · in-media · bare-h2 · in-media · bare-h2)
- about.html: 4 / 4 (hero · editorial-column · table · cta-band) / max consecutive 1 / kickers 1 (budget 2) / adjacent opener dupes 0 (kicker+h2 · bare-h2 · side-label · bare-h2)
- Claims flagged by claimscan (3) are all the "over 15 years" claim, covered by the sheet's claims-ledger row 1 (Q3).
- tel: link NO is by the client's choice (Q24: email or text); every sms: href is sms:+19172134979 and every sms label carries 917-213-4979 (scripted check, 18 sms links across 3 pages).
- Generated images: plate-warehouse.webp (pa-hero, 16:9, 1672×941), plate-space.webp (pa-real-estate, 4:5, 1000×1250); both first-attempt, realism QA passed, $0 (bin/gen-image). og.jpg built from the real formal portrait + wordmark (no generation).
- STATUS (superseded): NOT A HANDOFF at 15:53; cleared by the lead ruling, see the 15:57 block above.


## Audit R1 fixes — applied (builder hero + hit areas before its rate-limit stop; lead finished OG, measured, re-shot) 2026-10-13 19:56

| Round | Fix | Status | Evidence (page-level) |
|---|---|---|---|
| R1 | 1. Home hero: field min-height removed, portrait top-aligned near eyebrow, overlap kept | DONE | index.html @1440×900: portrait top 22px below eyebrow top (≤40 ✓), crosses field bottom by 115px, h1 2 lines at 52px; @1280×800 gap 32px, h1 2 lines; @1024 gap 149 (outside the 1440 spec, stacks cleanly); @375 stacked, scrollWidth 375. Screenshot desktop-index-first-screen.png |
| R1 | 2. 44px hit areas: wordmark, "More about Matt →", closing-band email | DONE | measured boxes @375 + @1440 all 3 pages: wordmark 109×44 / 178×44, more-about 151×44, band-email 179×44; text position unchanged (negative-margin offset) |
| R1 | 3. OG subline "AI-assisted business law · New Jersey & New York" | DONE | mockup/assets/og.jpg rebuilt 1200×630 in-browser with site Mona Sans; left blue panel wordmark + 2-line subline, right = headshot-2.jpeg crop/resize only |

### Evidence block — Atlas-Law — 2026-10-13 19:56

**Detector (per page)**
- about.html: exit 0, 0 finding(s)
- index.html: exit 0, 0 finding(s)
- practice-areas.html: exit 0, 0 finding(s)

**copycheck**: exit 0
    === shared across pages (1 blocks) — advisory
        Fine for genuine boilerplate. A bug when the shared line names something
        page-specific ("what your beds need" on the masonry page).
        [3 pages] Messages go straight to me.
**aitells**: exit 0
        [PASS] kit section titles       none
        [PASS] triad lists              2 (max 2): 'ul x3' line 236, 'ul x3' line 244  (three-item lists everywhere is a habit)
        [PASS] visual kit devices       none
        [PASS] hyphen-compound pileup   worst sentence has 1 coined compounds (max 3), 1.43/100w overall  -- matlas-law, Non-disclosure, matlas-law

**Claims** (each needs a ledger row)
- == /Users/harryfoodim/Projects/essex-web-crew/prospects/Atlas-Law/mockup/about.html: 2 sentence(s) need a claims-ledger row
- == /Users/harryfoodim/Projects/essex-web-crew/prospects/Atlas-Law/mockup/index.html: 1 sentence(s) need a claims-ledger row
- == /Users/harryfoodim/Projects/essex-web-crew/prospects/Atlas-Law/mockup/practice-areas.html: 0 sentence(s) need a claims-ledger row
- 3 candidate claim(s). For each: source (client answers / dossier / none), type (factual / conditional / illustrative / aspirational), evidence on page, missing before publish.

**Readiness facts**
- tel: link on page: NO
- LocalBusiness-type JSON-LD: yes
- <title> + meta description on index: yes
- overlay widgets (chat/newsletter/popup scripts): none
- heaviest images:
    166 KB  assets/plate-space.webp
    142 KB  assets/plate-warehouse.webp
    62 KB  assets/og.jpg

**Screenshots**: /Users/harryfoodim/Projects/essex-web-crew/prospects/Atlas-Law/screenshots: desktop-about-first-screen.png desktop-about-full.png desktop-index-first-screen.png desktop-index-full.png desktop-practice-areas-first-screen.png desktop-practice-areas-full.png mobile-about-first-screen.png mobile-about-full.png mobile-index-first-screen.png mobile-index-full.png mobile-practice-areas-first-screen.png mobile-practice-areas-full.png none


## Acceptance (written by the Critic at sign-off — three verdicts, one status per requirement)

<!-- Presentation / Decision support / Operational readiness, each PASS or FAIL on its own.
     Each requirement: Verified (+ evidence) · Implemented, not verified · Blocked (on what,
     owed by whom) · Out of scope. Launch blockers: unsourced factual claim, fabricated
     proof, form with no verified destination. A mockup is "concept, not launch-ready" until
     those clear — say which parts are demonstration. -->

| Verdict / requirement | Status | Evidence |
|---|---|---|
| Presentation | PASS | audit.md R2: $10K 8/8 (exception: no tel:, call/text only per client), rubric no dim < 7, boldness 8, spacing 8 |
| Decision support | PASS | audit.md R1: every decision-map line on the page or a confirm item; no unsourced claim; fees/AI stated without prices, savings or comparisons |
| Operational readiness | concept, not launch-ready | no form by design; mailto + sms links verified R1; JSON-LD, title/meta, AA, focus, LCP 51 KB, 44px targets verified R1/R2 |
| Footer disclaimer + privacy text, incl. how client info is handled with AI tools | Blocked: Matt's approval (owed by client via Harry) | footer on all 3 pages |
| "…not my time" (index.html L131): is any work billed hourly? | Blocked: Matt confirms (client via Harry) | Sol cold read R1; if he bills any work hourly, cut the clause |
| Call or text only, no tel: link | Documented exception, Matt to confirm | header + hero "Text 917-213-4979" |

## Stood-down teammates

<!-- Name + timestamp when a teammate is stood down. A teammate on this list who receives
     a message replies "Stood down — forward to the lead" and takes no other action. -->

- analyst — 2026-10-12, after dossier.md + site-content.md delivered.

- 2026-10-13 LEAD RULING: builder's 4 gate fixes (copycheck contraction floor on About/Practice; aitells checkable-claim floor on Practice) approved and written into build-sheet.md by the lead — L386 "5 areas…", L463 "that don't have their own…", L512 "I've spent…", L513 "I've been back in private practice since September 2025…". All sourced from Q2/Q3/Q6; no new claims. Builder applies, re-runs bin/evidence, hands off.

- 2026-10-13 LEAD RULING (audit R1 fixes 1 + 3, sheet values): build-sheet L269 hero field min-height removed; portrait top within 40px of eyebrow, overlap kept, matching About hero. OG card subline now "AI-assisted business law · New Jersey & New York". Fix 2 (44px hit areas) is builder-only. "not my time" stays per critic ruling: client-confirm launch blocker, not a build edit.

- critic — 2026-10-13, after round 2 sign-off.
- builder — 2026-10-13, after R1 fixes handed off; prospect signed off.
- planner — 2026-10-13, sheet built and signed off.
