# FORA Digital Website Audit — 2026-08-01

**Scope:** repo source at `prospects/fora-digital/mockup/` (`index.html`, `style.css`, `main.js`, `thanks.html`, `privacy-policy.html`, `terms-of-service.html`, `work/cecere-brothers/`, `work/corey-blakes-steakhouse/`) plus the live site at `https://foradigital.com` and `https://www.foradigital.com`, cross-checked against `client-answers.md`, `website-plan.md`, and `audit.md` (the crew's own internal sign-off record for this build). Two agents ran: `benchmark-analyst` (external research on well-executed small-agency and Fortune 500 sites) and a site audit against FORA's own repo + live site, using the benchmark's "Copy bar" as the grading standard for copy. **Read-only run — no site files were touched; this report is the only new file.**

---

## Executive summary

The site's structure and page inventory are already right-sized for a 2-person agency — no missing pages, restrained nav, real pricing, real portfolio. The problem is that **what's actually live has drifted from what the crew's own `audit.md` signed off on**: a different color palette, a collapsed single font instead of the audited pairing, embellished founder bios with claims not in `client-answers.md`, and reverted third-person "the team..." portfolio captions that a prior review round had already rewritten and verified fixed. Three findings are CRITICAL and should be fixed before this site is shown to another prospect: unverifiable superlatives in the founder bios ("one of the premier AI architects"), a placeholder `tel:+10000000000` phone number sitting in the live Cecere Brothers portfolio page a prospect can click, and both legal pages publishing text that says on its face they haven't been reviewed by a lawyer yet. A real, provable WCAG contrast failure and a broken `prefers-reduced-motion` selector are also live. Copy quality is split: the hero, "how it works," and reviews section are above the bar the benchmark research set; the three portfolio captions and both founder bios are below it, each with a full rewrite in this report. None of this needs new content invented — every fix either restores what was already signed off, or applies a real fact the crew already has on file.

---

## CRITICAL findings — fix before showing the site to any prospect

| ID | Issue | Location | Fix |
|---|---|---|---|
| **A1** | Live founder bios contain claims absent from `client-answers.md` (top authority) and from `audit.md`'s own "verbatim facts only" sign-off — Harry's bio claims he's "skyrocketed... to become one of the premier AI architects"; Corey's adds an unverified PE fund-accounting internship. An unsupported superlative from a college sophomore actively damages credibility. | `mockup/index.html:304-310, 321-328` | Confirm the underlying facts with Harry/Corey and update `client-answers.md`, or revert to the audited minimal bios. Full rewrite below. |
| **A2** | The "Get a free estimate" button on the bundled Cecere Brothers portfolio page — one click from FORA's own homepage — is `tel:+10000000000`, a placeholder. `audit.md` round 3 flagged this and explicitly chose not to fix it; it's still live and is the first thing a prospect taps to test "real client work." | `prospects/fora-digital/mockup/work/cecere-brothers/index.html:251` (live) | CHANGE to the real Cecere number, or repoint the CTA to that build's own contact section. |
| **A3** | Both the Privacy Policy and Terms of Service are live and published while each ends with "It is recommended that you have it reviewed by a licensed attorney... before publishing." Publishing a document that admits on its face it hasn't been reviewed is the first thing a client's lawyer would flag. | `mockup/privacy-policy.html:151-155`, `mockup/terms-of-service.html:159-163` | Get real attorney review, or at minimum pull the self-incriminating disclaimer before showing the site to any prospect. **Needs a human/lawyer — see below.** |

---

## Full findings table (sorted by severity)

| ID | Category | Severity | Location | Issue | Fix | Effort |
|---|---|---|---|---|---|---|
| A1 | DISCREPANCY / Content honesty | CRITICAL | `index.html:304-310, 321-328` | Bios contain claims not in `client-answers.md`; unsupported superlative ("premier AI architects") | CHANGE: confirm facts or revert to audited minimal bios | M |
| A2 | UNPROFESSIONALISM / Trust | CRITICAL | `work/cecere-brothers/index.html:251` | Placeholder `tel:+10000000000` live in portfolio CTA | CHANGE to real number or repoint CTA | S |
| A3 | LEGAL GAP | CRITICAL | `privacy-policy.html:151-155`, `terms-of-service.html:159-163` | Legal pages admit they're unreviewed, and are live | Get attorney review or pull the disclaimer | L |
| A4 | DISCREPANCY | HIGH | `style.css:8-17` vs `website-plan.md` §4, `audit.md` §3 | Live palette swapped from audited "warm linen" to a cool-blue palette with no critic round; undermines the plan's deliberate rejection of the dark/tech-slick convention | CHANGE: formally re-adopt (update plan + re-critique) or revert | M |
| A5 | DISCREPANCY / Design system | HIGH | `style.css:38-40` | Signed-off Instrument Serif / Hanken Grotesk pairing collapsed into one font (`General Sans` for all three tokens) — violates CLAUDE.md's own display+body pairing rule, on the agency's own flagship site | CHANGE: restore a real pairing, or document the change and rename the misleading `--serif` token | M |
| A6 | DISCREPANCY | HIGH | `index.html:262-287` | Pricing section ($2,750 + 60-day warranty) live with no trace in `client-answers.md` and no critic round | ADD the decision to `client-answers.md`, run one critic pass | S |
| A7 | DISCREPANCY / COPY QUALITY | HIGH | `index.html:166-171, 187-194, 211-213` vs `audit.md` round "3a" | Portfolio captions reverted to the exact third-person, rule-of-three, AI-tell copy round 3a already rewrote and verified gone | CHANGE: re-run `trade-copy`/`web-humanizer`, rewrite (see Copy report card) | S |
| A8 | LEGAL GAP / Accessibility | HIGH | `style.css:15, 247, 586, 621` | `--clay` (#FF5A1F) on `--paper` (#F2F5FF) = 2.86:1, fails WCAG AA at every size used (review stars, hero emphasis word). Old audited clay measured 4.35:1 and passed. | CHANGE clay to a value clearing 3:1 minimum (4.5:1 if used at body size) | S |
| A9 | BACKEND GAP / Accessibility | HIGH | `main.js:25` vs `index.html:200-206` | `main.js` selector `.hero-device .device-video` no longer matches any element (markup renamed to `.plate.device-plate`); `prefers-reduced-motion: reduce` visitors still get an autoplaying, looping video | CHANGE selector to `.plate-device .device-video` | S |
| A10 | DISCREPANCY | MEDIUM | `privacy-policy.html`, `terms-of-service.html` (10 occurrences) | "FORA Digital" (all-caps) used in body text vs "Fora Digital" (title case) in header/footer/title of the same files | CHANGE to one consistent casing sitewide ("Fora Digital") | S |
| A11 | DISCREPANCY | MEDIUM | `thanks.html`, `privacy-policy.html`, `terms-of-service.html` nav | Missing "Pricing" nav link present on `index.html` | ADD Pricing link to all three subpages' nav (desktop + mobile) | S |
| A12 | CONTENT GAP | MEDIUM | `foradigital.com/robots.txt` (404) | No `robots.txt` | ADD minimal `robots.txt` with sitemap reference | S |
| A13 | CONTENT GAP / BACKEND GAP | MEDIUM | `foradigital.com/sitemap.xml` (404) | No `sitemap.xml` — ironic for an SEO-selling agency | ADD sitemap listing all public pages | S |
| A14 | CONTENT GAP | MEDIUM | any unknown path (404) | No custom 404 — visitor drops onto Netlify's stock error page | ADD branded `404.html` matching site's identity | S |
| A15 | CONTENT GAP / CONVERSION GAP | MEDIUM | site-wide | No FAQ (ownership after launch, what happens after the 60-day warranty, cost of later changes) despite `FULL-PROCESS.md` already having real answers | ADD short FAQ sourced from `FULL-PROCESS.md` | M |
| A16 | CONTENT GAP | MEDIUM | repo-wide | No `BRAND.md` / `tokens.css` for FORA's own identity — likely root cause of the palette/font/copy drift (A4, A5, A7) | ADD `BRAND.md` as single source of truth | M |
| A17 | CONVERSION GAP | MEDIUM | `index.html:269-284` | Pricing section never explicitly rejects open-ended hourly billing fear | ADD line: "One flat price, agreed before we start — no hourly clock, no surprise invoice." | S |
| A18 | LEGAL GAP | LOW-MEDIUM | `index.html:353-391, 419-463` | Neither form links to Privacy Policy near its submit button | ADD one-line Privacy Policy link under both submit buttons | S |
| A19 | LEGAL GAP | LOW | `index.html:419-463` | Review form doesn't disclose at submission that it may be published | ADD disclosure line before submit | S |
| A20 | BACKEND GAP | LOW | `style.css:217-225, 235` | Dead CSS targeting a class no longer in the markup (see A9) | DELETE unused rules | S |
| A21 | BACKEND GAP | LOW | `style.css:38` | `--serif` token actually holds a sans-serif font — misleading name | CHANGE variable name once A5 is resolved | S |
| A22 | BACKEND GAP / Performance | LOW-MEDIUM | `index.html:200-206`; `phone-loop.mp4`/`.webm` | Two full video files (849KB + 967KB) for a decorative, below-the-fold loop | CHANGE to a shorter/lower-bitrate clip or CSS-animated static frame | M |
| A23 | BACKEND GAP | LOW | `index.html:379-381` | "Current website" field is `type="text"` not `type="url"` | CHANGE input type to `url` | S |
| A24 | BACKEND GAP | LOW | `style.css:132-137, 163-167` | `.current` nav-link styles defined but never applied by any script | DELETE unused rules (or wire up the active-link JS) | S |
| A25 | CONVERSION GAP | LOW | site-wide | No LinkedIn links on founder cards — no second surface to verify the two people are real | ADD LinkedIn links if profiles exist | S |
| A26 | BACKEND GAP | INFO (passing) | `www.foradigital.com` | Confirmed: 301 redirect to `https://foradigital.com/` — no fix needed | — | — |

---

## Copy report card

Every block graded 1–5 on Clarity / Specificity / Benefit / Credibility / Voice, **and** checked against the benchmark-analyst's Copy Bar (Patterns A–D, defined below the table). Verdict: 4.0+ = ABOVE BAR, 3.0–3.9 = AVERAGE, below 3.0 = SUBPAR.

| Copy block | Location | Clarity | Specificity | Benefit | Credibility | Voice | Avg | Verdict | Copy Bar pattern(s) failed |
|---|---|---|---|---|---|---|---|---|---|
| Hero (H1 + lead) | `index.html:69-78` | 5 | 4 | 4 | 3 | 5 | 4.2 | ABOVE BAR | — |
| "How it works" (4 steps) | `index.html:227-252` | 5 | 4 | 4 | 3 | 5 | 4.2 | ABOVE BAR | — |
| Reviews empty state | `index.html:474-481` | 5 | 4 | 3 | 4 | 5 | 4.2 | ABOVE BAR | — |
| Pricing section | `index.html:262-287` | 5 | 4 | 3 | 3 | 4 | 3.8 | AVERAGE | D (partial — no no-surprise-billing line) |
| Cecere Brothers work caption | `index.html:166-171` | 3 | 2 | 2 | 2 | 2 | 2.2 | SUBPAR | C (structure), voice |
| Corey Blake's Steakhouse caption | `index.html:187-194` | 3 | 2 | 2 | 2 | 2 | 2.2 | SUBPAR | C (structure), voice |
| Phone-loop caption | `index.html:211-213` | 3 | 2 | 1 | 2 | 2 | 2.0 | SUBPAR | C (structure), voice |
| Harry Foodim bio | `index.html:304-310` | 4 | 2 | 1 | 1 | 2 | 2.0 | SUBPAR | A, B |
| Corey Rapkin bio | `index.html:321-328` | 3 | 3 | 1 | 2 | 2 | 2.2 | SUBPAR | A, B |

**Copy Bar patterns, for reference (full detail from benchmark-analyst):**
- **A — Client-first opening** (lukenetti.com): first sentence names the client, not the founder's credentials. Fails if it opens with school/certifications.
- **B — Two-person-studio positioning** (hoodzpahdesign.com): proof and personality interleaved sentence-by-sentence; fails if all résumé (LinkedIn-summary) or all personality (dating-profile).
- **C — Process-quote-as-proof** (maypopcreativestudio.com, structure only — NOT its cutesy tone): testimonials/captions should speak to the experience, not just praise the output.
- **D — Named-package, no-surprises** (icebreaker.agency): price + deliverable + timeline in one line, with an explicit rejection of open-ended billing.

### Rewrites for every AVERAGE / SUBPAR block

**Pricing section — AVERAGE (3.8), fails D partially**
> Current: "Starting at $2,750" + bullets: design/build in 48–72 hours, both owners on the build, 60-day warranty, direct owner access.

Why: clear and mostly concrete, but the single line Pattern D calls for is spread across four bullets, and there's no explicit no-surprise-billing rejection.

Rewrite:
> **$2,750 to start.** One flat price, agreed before we touch a line of code — no hourly clock, no surprise invoice. That covers a full design and build in 48 to 72 hours, both of us on it start to launch, a 60-day warranty after you go live, and direct access to the two people actually building your site.

**Cecere Brothers Landscaping caption — SUBPAR (2.2), fails C/voice**
> Current: "The team built a striking website for a local landscaping business. Through the use of our detailed design templates, quality images, and a descriptive questionnaire response, the team was able to put together a site that will certainly capture the eye of a client. All the information a customer would need is clearly portrayed, and the result is exactly what our client asked for."

Why: third-person "the team" describing FORA's own work, a stiff "through the use of X, Y, and Z" template construction, and an unverifiable superlative ("will certainly capture the eye") — the exact AI-tell pattern `audit.md` round 3a already fixed once before it reverted.

Rewrite:
> We built this for a family landscaping crew in Essex County — a dark, evening-garden look with the estimate front and center, so a homeowner can see what to do next without hunting for it. This one's a real client, done and live.

**Corey Blake's Steakhouse caption — SUBPAR (2.2), fails C/voice**
> Current: "The team built a concept website for a steakhouse, with no client behind it. Through the use of dazzling animations, a high-end black and gold palette, and extreme attention-to-detail, the result was a site that reads like a restaurant worth driving to..."

Why: same third-person/rule-of-three/vague-adjective problems ("dazzling," "extreme attention-to-detail" have nothing concrete behind them).

Rewrite:
> This one's made up — a steakhouse we invented to show what we'd do with a restaurant: dark, high-end, reservation-first, with the menu and hours exactly where a hungry guest would look for them. Not a client. We generated that cover photo with AI, and we're telling you that up front.

**Phone-loop caption — SUBPAR (2.0), fails C/voice**
> Current: "This is a video our team built... Not only do we have quality image generation, but we even have full video generation."

Why: "Not only do we have X, but we even have Y" is a stock hype construction bragging about FORA's own capabilities rather than telling the visitor anything useful.

Rewrite:
> This clip started as a plain photo of an iPhone home screen — we turned it into video ourselves. Same tools, same process we'd use on your site.

**Harry Foodim bio — SUBPAR (2.0), fails A and B**
> Current: "Harry is an Accounting student at The Ohio State University's Fisher College of Business. He has several certifications in artificial intelligence, which has skyrocketed him to become one of the premier AI architects. He also interns at a CPA practice, where he supports and works directly with clients, performs tax preparation, as well as financial planning. At Fora Digital, he is heavily involved in the AI-driven production side. On top of that, he contributes to the Accounting and Operations functions of the business."

Why: opens with school credentials before establishing anything the reader cares about (fails A); it's all résumé line-items, no human specificity (fails B — reads like a LinkedIn summary); "skyrocketed him to become one of the premier AI architects" is an unsupported superlative from a college sophomore that damages credibility. Also flagged as A1 above — no traceable source in `client-answers.md`.

Rewrite (pending confirmation of the underlying facts — flag to Harry):
> Harry's a sophomore at Ohio State studying accounting, with real certifications in AI and a running internship at a CPA practice doing tax prep and financial planning — so when he tells you a number, he's already done the work to back it up. On Fora builds he runs the AI-driven production side and keeps the company's books straight. Off the clock he's usually playing a sport, at the gym, or with family and friends.

**Corey Rapkin bio — SUBPAR (2.2), fails A and B**
> Current: "Corey is an Accounting student at the University of Georgia. He gained hands-on experience in fund accounting through an internship focused on private equity fund structures, including net asset value calculations, capital call and distribution processing, and investor reporting. At Fora Digital, he combines that financial background with a passion for design, overseeing the company's finances and design direction..."

Why: same résumé-first structure, plus finance jargon that means nothing to a landscaper reading it and doesn't connect to why he's good at building websites.

Rewrite (pending confirmation of the underlying facts — flag to Corey):
> Corey's a sophomore at the University of Georgia studying accounting, and interned in private equity fund accounting — NAV calculations, capital calls, investor reporting, the kind of work that has to be exactly right or nothing closes. He brings that same no-slop-allowed habit to design, and he's also the one building the AI tools the two of them use to move faster on every build.

---

## Benchmark patterns table

Full pattern table from benchmark-analyst (Tier 1: Apple/Stripe/Microsoft; Tier 2: Hoodzpah, Maypop, Luke Netti, Icebreaker, Hook Agency — weighted heaviest; Tier 3: CLC Design, Wiesner Bros, Local Coffee). Every pattern marked **Fits FORA: Yes** is cross-referenced below to the specific gap(s) it would fix.

| ID | Pattern | Seen at | Fits FORA? | Gap(s) it fixes |
|---|---|---|---|---|
| B1 | One-sentence hero value prop | apple.com, stripe.com | Adapted (already done) | — |
| B2 | Restrained top nav (5-8 items) | stripe.com | **Yes** | **fixes A11** — the nav is already the right size; A11 is purely a sync bug (3 subpages missing the "Pricing" item `index.html` already has). Applying B2 means keeping nav at 6 items sitewide, not adding a 7th — just propagate the existing item. |
| B3 | Two-tier CTA (low + high commitment) | stripe.com | Adapted | Addresses A25 indirectly — a softer secondary CTA gives a not-ready visitor another way to engage besides "Start a project," partially offsetting the lack of a LinkedIn/social trust surface. |
| B4 | Exhaustive mega-footer | apple.com, microsoft.com | No — does not scale down | — (anti-pattern; explicitly do not copy) |
| B5 | CTA firehose (27+ labels) | stripe.com | No — does not scale down | — (anti-pattern; explicitly do not copy) |
| B6 | Explicit small-team positioning statement | hoodzpahdesign.com | **Yes** | **fixes A1 and the Harry/Corey bio SUBPAR entries** — a standalone "no account managers, the two people who build your site are the two who answer your email" line reframes the two-founder structure as the pitch itself, which the current bios (all résumé, no positioning) don't do at all. |
| B7 | Client-first bio opening | lukenetti.com | Adapted | **fixes A1 and both bio SUBPAR entries** — this is Copy Bar Pattern A directly; the rewrites above apply it by opening each bio with what the client gets before the founder's school. |
| B8 | Founder's own small-business background as trust anchor | maypopcreativestudio.com | Adapted (partial — not available to FORA) | — (neither founder has run a small business; the substitute is concrete numbers, which the rewrites use instead) |
| B9 | Testimonials quote the PROCESS, not just the outcome | maypopcreativestudio.com | **Yes** | **fixes the Reviews empty-state gap** — when Harry collects real reviews (per the real-reviews-only rule), prompting for process language ("was it easy to work with us") sets a bar for what goes in that section once it's populated; also informs A15's FAQ, since process anxiety is exactly what an FAQ should pre-empt. |
| B10 | Transparent fixed-scope pricing, explicit no-hourly-billing framing | icebreaker.agency | **Yes** | **fixes A17 and the Pricing AVERAGE verdict** — FORA already has the flat-fee instinct right (B10 confirms it); what's missing is exactly A17's one sentence rejecting open-ended billing, which the Pricing rewrite above adds. |
| B11 | Diagnostic-first tone ("find the opportunity, fix it in order") | icebreaker.agency | Adapted | Reinforces making the questionnaire-first process explicit on-site — supports A15 (FAQ: "we ask before we pitch"). |
| B12 | "Us vs. DIY vs. big agency" comparison table | hookagency.com | Adapted | Addresses the same underlying need as **A15** (budget-conscious buyers can't tell if this is a good deal) — a small comparison table would give A15's FAQ content a visual, skimmable format instead of prose. |
| B13 | Visual step-by-step process timeline | hookagency.com | **Yes** | Enhances the already-passing "How it works" section (ABOVE BAR at 4.2) — not fixing a defect, but strengthening a section that's currently good text with no visual timeline treatment. |
| B14 | Portfolio shown as name + one-line tag + live link, no long prose | lukenetti.com | **Yes** | **fixes A7 and all three SUBPAR portfolio captions** — the rewrites above compress each caption to exactly this shape (real name, one clause, real/labeled status) instead of the reverted third-person paragraph. |
| B15 | Local-industry vocabulary and specific proof points | clcdesign.com, wiesnerbros.com | **Yes** | **fixes the specificity failures across every SUBPAR copy block** — bios and captions currently score 2/5 on Specificity; B15's discipline (real towns, real numbers, no generic adjectives) is the same fix applied everywhere in the rewrites section. |
| B16 | Founder-origin-story / local-partnership framing | localcoffee.com | Adapted | Mainly a lens for pitching landscaping/coffee-shop prospects, not a direct fix to foradigital.com itself. |
| B17 | Multi-generational/long-tenure narrative | wiesnerbros.com | No — does not apply | — (FORA has no tenure to claim; correctly not attempted anywhere on the site) |
| B18 | Brand-only hero relying on recognition alone | apple.com | No — does not scale down | — (anti-pattern; explicitly do not copy — FORA's benefit-forward hero is correctly not doing this) |

**Anti-patterns confirmed correctly avoided on the live site:** B4 (no mega-footer), B5 (site has exactly two CTA labels, not a firehose), B18 (hero is benefit-forward, not brand-only) — worth noting as things NOT to "fix," since the site already gets these right.

---

## Quick wins (top 5, severity-to-effort ratio)

1. **A9** — Fix the dead `.hero-device .device-video` selector in `main.js:25` → `.plate-device .device-video`. One line, closes a genuine `prefers-reduced-motion` accessibility gate that's silently broken right now.
2. **A2** — Fix or repoint the placeholder `tel:+10000000000` on the bundled Cecere Brothers page. One line, removes a dead-click sitting directly in FORA's own proof-of-work path.
3. **A8** — Darken `--clay` to restore WCAG AA contrast. One CSS value, fixes a mathematically provable accessibility failure.
4. **A11** — Add the missing "Pricing" nav link to `thanks.html` / `privacy-policy.html` / `terms-of-service.html`. Copy-paste from `index.html`'s nav markup.
5. **A10** — Pick one casing for the business name ("Fora Digital") and fix the 10 "FORA Digital" instances across the two legal pages. Find-and-replace inside two files.

All five are same-day fixes, need no design or legal review, and together close a broken accessibility gate, a dead-click credibility hit, a provable contrast failure, and two internal-consistency errors.

---

## Needs a human

**Visual review (Corey) — code can't confirm these:**
- `index.html` desktop ≥1440px: the interactive cobalt "compass field" hero canvas (intentional or noisy?), the mask-curtain reveal timing, the marquee seam (recently re-fixed per `audit.md` round 3i — confirm no visible jump), Work-section plate hover states, and whether the two founder cards still align at equal height now that bios are much longer.
- `index.html` at 375px (iPhone): every section above, plus the Pricing section (added after the last recorded mobile QA round) and the "How it works" 4-step grid at its breakpoints — neither has a post-addition mobile screenshot on file.
- `thanks.html`, `privacy-policy.html`, `terms-of-service.html`: general layout/legibility — no dedicated screenshots exist for these.
- `work/cecere-brothers/index.html`, `work/corey-blakes-steakhouse/index.html`: both render live at `foradigital.com/work/...` — worth a visual pass since they're bundled copies of other builds.
- Contrast in practice: A8 was computed mathematically from hex values; confirm visually how bad the star ratings/hero word actually look before prioritizing.

**Needs a real lawyer, not a template fix:**
- The Privacy Policy and Terms of Service (A3) — both explicitly self-flag as unreviewed, and both are live today.

---

## Proposed fix order

Grouped so each file is touched once, Criticals first.

**Round 1 — Criticals + same-file quick wins**
1. `index.html` — A1 (bio rewrites), A6 (log Pricing decision to `client-answers.md`), A17 (no-surprise-billing line), A7 (portfolio caption rewrites), A18/A19 (form disclosure lines), A23 (input type)
2. `work/cecere-brothers/index.html` — A2 (real phone number or repointed CTA)
3. `privacy-policy.html` + `terms-of-service.html` — A3 (attorney review or pull disclaimer), A10 (name casing)
4. `main.js` — A9 (selector fix)
5. `style.css` — A8 (contrast fix), A20/A24 (dead CSS cleanup — bundle with A9/A8 since it's the same file open)

**Round 2 — Design-system reconciliation (needs a decision, not just a fix)**
6. `website-plan.md` + `style.css` — A4 (palette) and A5 (font pairing): decide whether to formally re-adopt the live drift or revert to audited direction, then update the plan and re-run the critic in one pass.
16. `BRAND.md` (new) — A16, to prevent this drift from recurring.

**Round 3 — Site-wide additions (independent of the above, can run anytime)**
7. `thanks.html`, `privacy-policy.html`, `terms-of-service.html` — A11 (nav sync)
8. New files: `robots.txt` (A12), `sitemap.xml` (A13), `404.html` (A14)
9. `index.html` — A15 (FAQ section), A25 (LinkedIn links, if profiles exist)
10. Asset pass — A22 (video compression)

Round 1 clears every CRITICAL and touches each file exactly once. Round 2 is deliberately separated because it's a direction decision, not a bug fix. Round 3 is pure addition and carries no risk to what's already signed off.
