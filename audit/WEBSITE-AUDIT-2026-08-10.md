# FORA Digital Website Audit — 2026-08-10 (Round 2)

**Scope:** repo source at `prospects/fora-digital/mockup/` plus the live site at `https://foradigital.com`, run fresh after a major merge from a parallel session (new "Sunday Lawn" and "DaSilva" portfolio pieces, real founder headshots, a two-tier "Builds" catalog replacing the old single-tier "Pricing" section). Two agents ran: `fora-benchmark` (external research on well-executed small-agency and Fortune 500 sites) and `fora-site-auditor` (full audit graded against the benchmark's Copy bar). **Read-only run — no site files were touched; this report is the only new file.** Several of this round's headline findings were independently re-verified by the lead (grep against repo source + a live WebFetch) before inclusion, since the auditor had no Bash or browser tools this session and flagged several claims as unverified — see "Needs a human" for what's still open.

---

## Executive summary

**The live site is not the site in the repo.** Independently confirmed: `foradigital.com` right now shows the OLD single-tier "Pricing" section, the old nav, and both Cecere Brothers Landscaping *and* Corey Blake's Steakhouse in the portfolio — while the repo has a two-tier "Builds" catalog, a "Builds" nav item, and Cecere + Sunday Lawn + DaSilva. Nothing built in this session's earlier round, and nothing from Harry's parallel-session rework, has actually gone live. That's the top priority, full stop — every other fix is invisible to a prospect until a redeploy ships. Beyond that, the two CRITICAL items from Round 1 are both still open and unchanged: the founder bio superlative ("one of the premier AI architects," which also has a subject-verb grammar error) and the collapsed single-font system. A new, real discrepancy surfaced too: the merge that added the "Builds" nav item never swept the four subpages (Privacy, Terms, Thanks, 404), so all of them still link to a `#pricing` anchor that no longer exists — 12 dead links. Copy quality is more mixed than Round 1: the hero, the DaSilva caption, and the process steps are genuinely above the bar the new benchmark set, but the two new tier descriptions, three portfolio captions, and both founder bios all grade SUBPAR, each with a full rewrite below. Three items are correctly flagged for a lawyer, not a template fix: undefined warranty language sold in a priced table, review-publishing consent, and hosting a full copy of a client's site with no noindex.

---

## CRITICAL findings — fix before any more outreach

| ID | Issue | Location | Fix |
|---|---|---|---|
| **A1** | **Confirmed live via WebFetch:** `foradigital.com` shows the old single-tier "Pricing" section, old nav, and Corey Blake's Steakhouse — none of which exist in the current repo. Every prospect Harry has emailed recently, and every one he emails until this ships, sees a stale site missing the new Builds catalog and the second $4,000 tier. | live site vs. `mockup/index.html` | CHANGE — redeploy the current `mockup/` to Netlify before any more outreach |
| **A2** | **Confirmed still present, verbatim, in the repo:** Harry's bio still claims his AI certifications "has skyrocketed him to become one of the premier AI architects" — an unsupported superlative with no source in `client-answers.md`, on the page whose entire job is trust. | `index.html:422–423` | DELETE the clause; replace with a checkable fact (full rewrite below) |

---

## Full findings table (sorted by severity)

| ID | Category | Severity | Location | Issue | Fix | Effort |
|---|---|---|---|---|---|---|
| A1 | Discrepancy | CRITICAL | live vs. `mockup/index.html` | Live deploy is stale — old Pricing, old nav, both old + new portfolio pieces missing | CHANGE — redeploy | S |
| A2 | Unprofessionalism | CRITICAL | `index.html:422–423` | Unverifiable "premier AI architects" superlative in Harry's bio | DELETE clause, replace with checkable fact | S |
| A3 | Unprofessionalism | HIGH | `index.html:422` | Subject-verb error: "certifications… which **has** skyrocketed" → "have" | CHANGE (moot if A2's rewrite lands) | S |
| A4 | Discrepancy | HIGH | `privacy-policy.html`, `terms-of-service.html`, `thanks.html`, `404.html` | 12 dead `#pricing` links across 4 subpages — the anchor was deleted when the merge added "Builds"; nav also differs page to page | CHANGE all `#pricing` hrefs to `#builds`, relabel "Pricing" → "Builds" on all four | S |
| A5 | Discrepancy | HIGH | `client-answers.md:24–45` vs `index.html:420–444` | Top-authority file lists 4 facts for Harry, 2 for Corey, and says headshots are placeholder slots — live bios assert Fisher College, AI certifications, a CPA internship, a PE fund internship, and ship real photos. Not claimed false — claimed undocumented. | CHANGE — have Harry amend `client-answers.md` with the new facts and photo decision | S |
| A6 | Legal gap | HIGH | `index.html:469–516` | Inquiry form collects name/business/email/phone with no privacy notice at point of collection | ADD one line + Privacy Policy link under the submit button | S |
| A7 | Legal gap | HIGH | `index.html:544–588` | Review form collects and intends to publish a first name + business name with no consent language | ADD a consent line above the submit button |  S |
| A8 | Conversion gap | HIGH | `index.html` whole page; JSON-LD `646–662` | Zero geographic signal — no "New Jersey," no "Essex County," no `areaServed` in JSON-LD. A local agency selling to local trades reads as from-nowhere. | ADD "New Jersey"/"Essex County" to hero or footer + `areaServed` to JSON-LD | S |
| A9 | Discrepancy | HIGH | `index.html:166–168` vs `:257` | Cecere caption credits "our detailed design templates" while the process section promises sites "built for your business rather than pulled off a template" — self-contradiction two screens apart | CHANGE the Cecere caption (rewrite below) | S |
| A10 | Discrepancy | MEDIUM | `index.html:250` | Step 01 offers to "get on the phone with us" — no phone number exists anywhere on the site | CHANGE to remove the phone clause, or ADD a real number | S |
| A11 | Conversion gap | MEDIUM | `style.css:559` | `.th-lead{display:none}` hides BOTH tier descriptions below 760px — phone visitors see tier names with zero explanation of what they're buying | CHANGE — shrink instead of hide | S |
| A12 | Backend gap | MEDIUM | `style.css:38–40` | `--serif`/`--sans` tokens both resolve to `'General Sans'` with diverging fallback stacks (Georgia serif vs. Segoe UI sans) — if the Fontshare CDN fails, the page renders a mixed-font page nobody designed | CHANGE — rename tokens, align fallback stacks | S |
| A13 | Discrepancy | MEDIUM | `style.css:38–40` vs CLAUDE.md $10K item 2 | Single font doing display+body+wordmark is a deliberate but undocumented exception to the house font-pairing rule | ADD a one-line waiver in `website-plan.md`, or CHANGE to a real pairing | S |
| A14 | Content gap | MEDIUM | `index.html` | No FAQ; domain cost ("NOT included in either price") exists only in an HTML comment — visitors are never told, while a hero bullet says "Your domain connected" | ADD a 5-question FAQ stating the domain cost plainly | M |
| A15 | Discrepancy | MEDIUM | `audit.md` | Entire file describes a prior design (different fonts, different palette, Corey Blake's Steakhouse, "zero forms on the page") that no longer exists — void as a QA record | ADD a new review round against the current build; mark old rounds historical | M |
| A16 | Discrepancy | MEDIUM | `screenshots/desktop.png`, `mobile.png` | Depict a version of the site that no longer exists (old hero copy, old nav, text wordmark) — the QA proof proves nothing about the current build | CHANGE — recapture after redeploy | S |
| A17 | Unprofessionalism | MEDIUM | `index.html:231–232` | Phone-video caption says "what you see **on the left**" — the video stacks ABOVE the caption on mobile, so the direction is wrong on every phone | CHANGE to "what you're reading now" / similar | S |
| A18 | Discrepancy | MEDIUM | `index.html:513` vs `thanks.html:57–58` | Form promises "as soon as possible"; thanks page promises "usually the same day" — two different commitments, weaker one shown first | CHANGE form note to match the stronger, real commitment | S |
| A19 | Conversion gap | MEDIUM | `index.html:469–510` | 7-field inquiry form vs. the crew's own ≤4-field standard for a local-trade estimate form | CHANGE — keep 4 essentials, move the rest post-reply | S |
| A20 | Conversion gap | MEDIUM | `index.html:525–606` | Reviews section's first visible content is "Nobody has sent one in yet" — the honesty is right, but running an empty social-proof section undercuts itself | CHANGE — hide the section until a real review exists | S |
| A21 | Legal gap | MEDIUM | `index.html:363` | "60 day warranty" sold in a priced table with no defined scope, exclusions, or claim process | ADD a one-sentence scope line — **needs a lawyer**, see below | S |
| A22 | Backend gap | MEDIUM | `mockup/work/cecere-brothers/` | Full copy of a client's site hosted at `foradigital.com/work/cecere-brothers/`, no `noindex`, no canonical, `robots.txt` allows it — confirmed via grep | ADD `noindex` or a canonical to the client's real domain — **needs a permission question too** | S |
| A23 | Backend gap | MEDIUM | `sitemap.xml` | Confirmed: omits `/work/cecere-brothers/` (live, crawlable), no `lastmod` on any entry | ADD the work URL (once A22 is decided) + `lastmod` dates | S |
| A24 | Discrepancy | MEDIUM | `index.html:22,664` vs subpages | Cache-buster skew — homepage loads `style.css?v=5`, subpages load `?v=4` — a returning visitor can get two different stylesheets in one session | CHANGE all five pages to the same version string | S |
| A25 | Backend gap | MEDIUM | `index.html:646–662` | JSON-LD missing `logo`, `image`, `areaServed`, `sameAs` | ADD those four fields | S |
| A26 | Conversion gap | LOW | `index.html:12` | `og:image` is a screenshot of a client's homepage (Cecere) — every social share of foradigital.com shows the client's site, not FORA's | CHANGE to a FORA-branded OG card | S |
| A27 | Unprofessionalism | LOW | `assets/dasilva-2026.webp` | DaSilva screenshot showcased on FORA's own site has typos: missing accents ("Espanol" → "Español") and awkward Portuguese | CHANGE on the DaSilva build, recapture screenshot | S |
| A28 | Backend gap | LOW | `style.css:436,599,603` | `.compare-wrap{overflow-x:auto}` has no `tabindex="0"` (WCAG 2.1.1); two dead CSS rules from the old initials-placeholder era | ADD tabindex; DELETE dead rules | S |
| A29 | Backend gap | LOW | live, unverified | Cannot confirm Netlify actually serves the custom `404.html` (server returned bare 404) | ADD a human check after redeploy | S |
| A30 | Backend gap | LOW | live, unverified | www → non-www redirect not confirmed this round (tool limitation) | ADD a human check for the 301 | S |

---

## Copy report card

Graded against the fresh Copy bar (Patterns A–D, defined below). Verdict: 4.0+ = ABOVE BAR, 3.0–3.9 = AVERAGE, below 3.0 = SUBPAR.

| Copy block | Location | Clar | Spec | Benefit | Cred | Voice | Avg | Verdict | Pattern failed |
|---|---|---|---|---|---|---|---|---|---|
| Hero H1 | `69–73` | 5 | 4 | 5 | 3 | 5 | 4.4 | ABOVE BAR | — |
| Hero lead | `74–78` | 5 | 4 | 4 | 3 | 4 | 4.0 | ABOVE BAR | — |
| DaSilva caption | `187–190` | 4 | 5 | 3 | 5 | 4 | 4.2 | ABOVE BAR | — |
| Process steps 01–04 | `246–271` | 5 | 4 | 3 | 4 | 5 | 4.2 | ABOVE BAR | — |
| Reviews empty state | `600–605` | 5 | 3 | 1 | 4 | 4 | 3.4 | AVERAGE | — |
| Cinematic tier desc. | `311–313` | 4 | 3 | 3 | 2 | 2 | 2.8 | SUBPAR | D |
| Classic tier desc. | `303–304` | 4 | 2 | 3 | 2 | 3 | 2.8 | SUBPAR | D |
| Phone-video caption | `231–232` | 3 | 3 | 1 | 3 | 3 | 2.6 | SUBPAR | — |
| Form note | `513` | 5 | 1 | 2 | 2 | 2 | 2.4 | SUBPAR | — |
| Sunday Lawn caption | `209–213` | 3 | 2 | 2 | 3 | 2 | 2.4 | SUBPAR | — |
| Corey bio | `437–444` | 2 | 4 | 1 | 3 | 2 | 2.4 | SUBPAR | A, B |
| Harry bio | `420–426` | 3 | 3 | 1 | 1 | 2 | 2.0 | SUBPAR | A, B |
| Cecere caption | `166–170` | 3 | 1 | 1 | 2 | 1 | 1.6 | SUBPAR | D |

**Copy Bar patterns, for reference (full detail from fora-benchmark):**
- **A — Warm first-person greeting bio** (jcwebstudio.com): opens "Hi, I'm [Name]…", credentials woven into narrative not bullets, ~300–400 words, ends with exactly one personal detail.
- **B — Client-problem-first bio** (twofold-studios.com): states the visitor's problem before the founder, 1–2 checkable external credentials, ~100–150 words, solution-focused.
- **C — Blunt one-liner founder presence** (pocketknife.design): one flat opinionated sentence, no proof attached, layered on top of A or B — never a substitute.
- **D — Service descriptions by client vertical** (twofold-studios.com): named client type + 3–5 outcome-first bullets, never one generic paragraph.

### Rewrites for every SUBPAR block

**Harry Foodim bio — 2.0, fails A and B**
> Current: "Harry is an Accounting student at The Ohio State University's Fisher College of Business. He has several certifications in artificial intelligence, which has skyrocketed him to become one of the premier AI architects. He also interns at a CPA practice, where he supports and works directly with clients, performs tax preparation, as well as financial planning. At Fora Digital, he is heavily involved in the AI-driven production side. On top of that, he contributes to the Accounting and Operations functions of the business."

Why: "one of the premier AI architects" is an unverifiable superlative that damages the rest of the paragraph; opens with a third-person title, which both benchmark patterns reject; four of five sentences are about accounting, none about why he can build a website.

> Rewrite: Hi, I'm Harry. I'm the one who'll answer your email, and I do the production side of every build — turning what you tell us into the actual pages.
>
> I'm a sophomore studying accounting at Ohio State, and I grew up in West Essex. I also intern at a CPA practice, where I work directly with small business owners on their taxes and planning. That's most of what I do here too: sit with an owner, figure out what the business actually needs said, and build that. No account manager, no handoff — you get me and Corey.
>
> Outside of this I'm at the gym, playing sports, or with family.

*(Uses only facts already in `client-answers.md`. If the AI certifications are real and Harry wants them in, name them specifically — "certified in X and Y" is checkable; "premier AI architect" is not.)*

**Corey Rapkin bio — 2.4, fails A and B**
> Current: "Corey is an Accounting student at the University of Georgia. He gained hands-on experience in fund accounting through an internship focused on private equity fund structures, including net asset value calculations, capital call and distribution processing, and investor reporting. At Fora Digital, he combines that financial background with a passion for design, overseeing the company's finances and design direction. In addition, he works on the AI side to develop tools that further enhance the designing capabilities of the business."

Why: finance jargon aimed at a recruiter, not a coffee-shop owner, is 40% of the bio; "a passion for design" is resume filler; "further enhance the designing capabilities" is padding that says nothing.

> Rewrite: I'm Corey. I make the design calls — what your site looks like, how it's laid out, how it reads on a phone.
>
> I'm a sophomore studying accounting at the University of Georgia, and I spent a summer doing fund accounting for a private equity firm, which mostly taught me that most business software is ugly and confusing for no reason. I'd rather your customers find your phone number in two seconds than be impressed by anything.
>
> Harry and I split every build between us. Whichever of us you email is one of the two people who'll actually make the site.

**Cecere Brothers caption — 1.6, fails D**
> Current: "The team built a striking website for a local landscaping business. Through the use of our detailed design templates, quality images, and a descriptive questionnaire response, the team was able to put together a site that will certainly capture the eye of a client. All the information a customer would need is clearly portrayed, and the result is exactly what our client asked for."

Why: the lowest-scoring block on the site — third person, passive voice, praises FORA instead of describing the work, and names "our detailed design templates" as the method, directly contradicting the process section's promise of no templates (A9).

> Rewrite: A family landscaping outfit in West Essex County. One page carries lawn care, hardscape and design, a gallery of finished jobs, real customer reviews, and a quote form. Dark green and cream, big photos of their own work, and the estimate button follows you down the page on a phone.

**Sunday Lawn Co. caption — 2.4**
> Current: "The team built a cinematic website using a made up landscaping business. The homepage is a continuous film being shown as the viewer scrolls. The film tells the story of the business and the services they provide. Behind the film is an organized, descriptive site that makes it simple for the client to understand."

Why: third-person again, three consecutive sentences opening with "the film," and a closing clause ("makes it simple for the client to understand") vague enough to describe any website ever built — never says what a visitor actually sees.

> Rewrite: A demo, not a client — we invented Sunday Lawn Co. to show what the Cinematic build does. Scroll the homepage and it plays as one continuous film: a lawn at dawn, the crew working, the finished yard at golden hour. Underneath it is an ordinary site — services, service area, reviews, an estimate form — so the film sells and the page still works.

**Classic tier description — 2.8, fails D**
> Current: "A standard, straightforward site that tells people what you do, shows your work, and where customers can easily contact you."

Why: broken parallelism ("tells… shows… where customers can contact you" doesn't scan); "standard, straightforward" undersells a $2,750 product.

> Rewrite: Everything a customer needs to hire you: what you do, photos of your work, your service area, and a phone number and form they can reach in one tap. Three to five pages, fast on a phone.

**Cinematic tier description — 2.8, fails D**
> Current: "A fancy site where your homepage opens on a film that plays as the visitor scrolls — the kind of site people remember."

Why: "fancy" undersells a $4,000 product; "the kind of site people remember" is an unsupported claim in the same breath; the em dash is the crew's own flagged AI tell.

> Rewrite: Your homepage is a film. It plays as the visitor scrolls — your crew, your trucks, your finished work — and everything a Classic site does sits underneath it. This is the one people screenshot and send to a friend.

**Phone-video caption — 2.6**
> Current: "A video our team built, starting from a still of a plain iPhone home screen and ending at what you see on the left."

Why: a sentence fragment with no main verb; "on the left" is wrong on every phone layout (A17); explains how the video was made instead of why a prospect should care.

> Rewrite: This site, on a phone. We started from a blank iPhone home screen and animated it out to what you're reading now — the same scroll and motion work that goes into a Cinematic build.

**Form note — 2.4**
> Current: "We'll get back to you as soon as possible."

Why: commits to nothing; the thanks page already promises something stronger and more specific ("usually the same day"), so the site quietly offers the weaker version at the exact moment a prospect decides whether to hit send.

> Rewrite: Both of us get this. You'll hear back the same day, with what we'd build and what it costs.

**Reviews empty state — 3.4, AVERAGE (not flagged HIGH, but worth tightening)**
> Current: "No reviews yet / Nobody has sent one in yet. When a client does, we post it here."

Why: the honesty is right and should stay — but "Nobody has sent one in yet" is the last thing on the page before the footer, and volunteers the emptiest possible reading. See A20: the stronger move is not running the section yet, not softening this line.

> Rewrite (if the section stays): We've got two client sites live and neither owner has written us a review yet. When one does, it goes here in their words — we don't write them.

---

## Benchmark patterns table

Full pattern table from `fora-benchmark` (Tier 1: Apple/Stripe/Microsoft; Tier 2: JC Web Studio, Pocketknife, Agave Studio, TwoFold Studios — weighted heaviest; Tier 3: Scenic Landscaping, TLC Landscaping, Ganek PC). Every "Fits FORA: Yes" pattern cross-referenced to the gap it would fix.

| ID | Pattern | Seen at | Fits FORA? | Gap(s) it fixes |
|---|---|---|---|---|
| B1 | 5-item flat nav, no dropdowns | stripe.com | Yes | Nav is already the right size (6 items) — **B1 confirms A4's fix should be a relabel/sync, not a redesign**: propagate "Builds" everywhere rather than adding items. |
| B2 | One-sentence hero value prop | stripe.com | Yes | Already achieved — hero scores ABOVE BAR (4.4). No gap; confirms current direction. |
| B3 | Massive mega-nav (9–19 items) | apple.com, microsoft.com | No | — (anti-pattern, correctly not present) |
| B4 | Tiered pricing cards, never fully hidden | pocketknife.design, jcwebstudio.com | **Yes** | **Fixes A11 directly** — B4's "never fully hidden" is the exact rule `.th-lead{display:none}` breaks on mobile. Shrink the tier descriptions instead of hiding them. |
| B5 | Warm first-person bio opening | jcwebstudio.com | **Yes** | **Fixes both bio SUBPAR entries** — this is Copy Bar Pattern A directly; both rewrites above open "Hi, I'm ___" instead of a third-person title. |
| B6 | Bio blends credentials + personal detail | jcwebstudio.com | **Yes** | **Fixes both bio SUBPAR entries** alongside B5 — both rewrites end with exactly one grounding personal detail (gym/sports/family; nothing more). |
| B7 | Client-problem-first section intros | twofold-studios.com | Adapted | Useful for future section intros (e.g. Builds catalog framing), not a direct fix to a current finding. |
| B8 | Small curated portfolio, one specific line each | jcwebstudio.com, pocketknife.design, agave.studio | **Yes** | **Fixes A9, and the Cecere + Sunday Lawn caption SUBPAR entries** — each rewrite compresses to one concrete, specific description instead of a vague self-congratulatory paragraph. |
| B9 | 3-step plain-verb process explainer | pocketknife.design | Yes | Already achieved — process steps score ABOVE BAR (4.2). No gap. |
| B10 | Services segmented by client vertical | twofold-studios.com | Yes | Not a current gap (FORA has one undifferentiated service set) — informs A14's FAQ as a future structural option once FORA has more verticals (trades + law) to segment. |
| B11 | Quirky in-voice CTAs | agave.studio | No | — (anti-pattern; conflicts with FORA's own copy-voice rule) |
| B12 | Founder only in bylines, no dedicated bio page | agave.studio | No | — (anti-pattern; FORA correctly keeps a dedicated Founders section — don't erode it) |
| B13 | Phone-in-header CTA, owner tied to the work | sceniclandscaping.com, tarleton-landscaping.com | **Yes** | **Fixes A10 and A8 together** — B13 validates that FORA's own trade clients expect a working phone number; A10 currently offers one that doesn't exist, and A8's missing geographic signal is the same "are these real local people" trust gap. |
| B14 | One short checkable external credential near founders | ganekpc.com | Adapted | **Fixes A2/A3/A5 directly** — the fix for "premier AI architect" isn't removing all credentials, it's replacing an unverifiable one with something checkable, which is exactly what B14 rewards. |
| B15 | Small, restrained footer | tarleton-landscaping.com, jcwebstudio.com | Yes | Not a current gap — footer isn't flagged. Confirms FORA should resist a mega-footer as the site grows (see B3 anti-pattern). |

**Anti-patterns confirmed correctly avoided on the live site:** B3 (no mega-nav), B11 (no quirky CTAs), B12 (dedicated Founders section still present) — worth noting since the site already gets these right and shouldn't drift.

---

## Quick wins (top 5, severity-to-effort ratio)

1. **A1 — redeploy.** One drag-and-drop to Netlify. Nothing else on this list matters to a live prospect until this ships — right now every visitor sees a portfolio missing both new builds and a price list missing the $4,000 tier.
2. **A2 + A3 — cut "premier AI architects."** One clause, carrying a grammar error and already flagged once. Removing it alone lifts Harry's bio out of SUBPAR; the full rewrite above is ~20 minutes.
3. **A4 — fix the 12 dead `#pricing` links.** Find-and-replace `#pricing` → `#builds` and "Pricing" → "Builds" across four files. Broken nav on every legal page is the cheapest possible credibility loss.
4. **A6 + A7 — two sentences of form notice.** Closes two of the three genuinely legal-risky findings with one line each under a submit button.
5. **A9 + A11 — the template contradiction and the hidden mobile tier copy.** One caption rewrite kills a self-contradiction two screens apart; one CSS change (`display:none` → smaller font-size) stops hiding the one thing phone visitors need to understand what they're buying.

All five are same-day fixes; together they close the top CRITICAL, a live-vs-repo gap affecting every current outreach, a 12-link nav break, two legal-risk items, and the two places the site actively undercuts its own pitch.

---

## Needs a human

**Visual review (Corey) — the auditor had no browser tools this round, so none of this was checked:**
- The Builds comparison table at 375px and 320px — a 3-column, 13-row feature matrix is exactly where "designed, not shrunk" tends to fail.
- The same table between 561–760px, where tier leads are hidden but the table's `min-width:560px` still applies — likely spot for horizontal scroll on a small tablet.
- The animated `background-clip:text` gradient fills (`style.css:341–357, 480–492`) — measure contrast at the lightest frame of the sweep, not just the declared fallback color.
- Founder photos in the arched `.monogram` frame — confirm neither headshot is cropped badly.
- The hero canvas "compass field" on a mid-range Android (a per-frame rAF loop over up to 1,400 segments).
- Full JS-off pass on the current build — the curtain mechanism should be safe by design, but this exact build has never been audited end-to-end (previous JS-off/reduced-motion verification in Round 1 was against the pre-merge file).

**Needs a real lawyer, not a template fix:**
- **A21** — "60 day warranty" sold in a priced table with no defined scope.
- **A7** — whether disclosed consent at submission is sufficient to republish an identifiable person's name and business.
- **A22** — hosting a full copy of a client's live site on foradigital.com — both the SEO harm to the client and the permission question.
- Both legal pages still carry a self-aware footnote recommending attorney review (`privacy-policy.html:153`, `terms-of-service.html:161`) — confirm with the lawyer whether these can come out once real review happens.

**Needs Harry specifically, not a builder:**
- **A5** — amend `client-answers.md` with the real bio facts and the headshot decision.
- **A14** — the real domain cost, so it can be stated on the page instead of living in an HTML comment.
- **A10** — is there a real phone number or not? Step 01 currently offers one that doesn't exist.
- **A6/A7** — confirm the Netlify Forms email notifications were actually set up (the manual step noted in the source). **This is the single highest-consequence unverified item in the audit** — if it wasn't done, every form submission is sitting unread in a dashboard nobody opens.

---

## Proposed fix order

Grouped so each file is touched once, redeploy-blockers first.

**Round 1 — Ships the current build + closes the CRITICALs**
1. **Redeploy first (A1)** — get the current repo state live before anything else, so every subsequent fix actually reaches a visitor.
2. `index.html` — A2/A3 (bio rewrite), A9 (Cecere caption), A11 (unhide mobile tier text), A17 (caption direction fix), A18 (form-note commitment), A10 (phone clause), A6/A7 (form notices)
3. `privacy-policy.html`, `terms-of-service.html`, `thanks.html`, `404.html` — A4 (nav sync, 12 links)
4. `client-answers.md` — A5 (Harry amends with real facts)

**Round 2 — Design-system + legal (needs a decision, not just a fix)**
5. `style.css` — A12 (token rename/fallback fix), A13 (waiver or real pairing decision)
6. Lawyer pass — A21, A7 consent language, A22 permission question

**Round 3 — Backend/SEO + housekeeping (independent, can run anytime)**
7. `sitemap.xml`, `robots.txt`, JSON-LD — A22, A23, A25
8. `og:image`, DaSilva screenshot typos — A26, A27
9. `audit.md`, `screenshots/` — A15, A16 (recapture only makes sense AFTER Round 1 ships)
10. `style.css` cleanup — A28; cache-buster sync — A24

Round 1 clears both CRITICALs and the live/repo gap that makes everything else invisible. Round 2 is separated because it's a direction decision plus real legal work, not a mechanical fix. Round 3 is pure cleanup with no risk to what's already shipped.
