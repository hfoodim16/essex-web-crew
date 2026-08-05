# Essex Web Crew — Project Playbook

> This file is read automatically by every teammate. It is the shared source of
> truth. If a spawn prompt and this file disagree, this file wins unless the
> lead says otherwise.

## Mission — the ask-first model, two separate teams

We are a mini web agency run as Claude Code **agent teams**. Our business model is
**NOT** "build a site, show it to them, sell it." It is:

> **Find a client who may need a website → Harry reaches out → ASK what they want (the
> master questionnaire) → build FROM their answers → keep working with them until it's
> perfect.**

We never build speculative mockups and pitch them. The client's answers come first; the
build serves the answers. Because Harry's outreach and the client's reply happen on
human time (days), the work is split into **two independent teams** that never run
together:

- **Team 1 — Prospecting.** `scout` + `analyst` ONLY. The scout finds qualifying
  businesses; the analyst researches the top 3 and writes their dossiers. The run's
  final deliverable is **the shortlist with contact info** — then it ends. Nothing is
  built.
- **Harry, between the teams (no agents involved).** He contacts the prospects himself
  — call or email, his own words. Whoever says yes gets
  **`templates/Website-Questionnaire.docx`**, the standing client questionnaire that needs
  no run to produce. He collects their answers.
- **Team 2 — Build.** `planner` + `builder` + `critic`. Input is the client's answers.
  The planner plans FROM them, one builder builds, the critic gates it, and the
  finished site goes back to the client — then we iterate with them until it's right.

**We never contact a business.** All client contact is Harry personally; the teams only
produce research and websites.

**Outside both teams — the caretaker and the FORA pair.** These are never spawned in a
Prospecting or Build run:

- **`caretaker`** — post-launch only, for sites already live on a real domain. Registry
  keeping + incident diagnosis. Its beat starts where the two teams' ends.
- **`fora-benchmark` + `fora-site-auditor`** — FORA-internal tooling for auditing **our own
  agency site** (foradigital.com), not client work. `fora-benchmark` researches
  well-executed sites and produces a "copy bar"; `fora-site-auditor` grades FORA's site
  against it plus its own seven categories. Neither writes files — the benchmark's output
  is pasted into the auditor's task context by hand. The boundary is **whose site it is**,
  not which folder: FORA's own site sits at `prospects/fora-digital/` for historical
  reasons and is theirs to read, but **every other `prospects/<slug>/` is a client build
  belonging to the `critic`** — two auditors grading one build by different rubrics is how
  a crew ships contradictions.

## Territory & target

- **Where:** Essex County, NJ (Newark, Montclair, Bloomfield, Nutley, Belleville,
  West Orange, Livingston, Cedar Grove, Verona, Caldwell, the Oranges, etc.).
- **The real filter — a naturally static website, NOT an industry.** We target businesses
  whose site is **low-maintenance / static**: a brochure, not an app. "Build once, barely
  touch it" — no weekly menus, no e-commerce catalog, no booking engine, no
  constantly-changing content. **We are not limited to blue-collar trades.**
- **Lead niche (proven):** tree service, lawn care, and small landscapers — a real
  scouting run showed these are full of owner-operators on a Facebook page, a dead
  domain, or a 2000s-era site (exactly our target). **Largely skip masonry, paving, and
  fencing** unless a specific listing shows a weak/absent site — those trades here have
  mostly bought modern template sites and filter out fast.
- **Equally fair game beyond the trades:** accountants/CPAs, law offices, insurance
  agents, auto repair, cleaning services, pest control, movers, home inspectors,
  chiropractors/dentists, tutors/music teachers, photographers, funeral homes, vets.
  Professional offices often sit on a neglected 2000s-era site — prime targets.
- **Skip industries needing constant updates** (the opposite of what we sell):
  restaurants/cafés (menus), e-commerce/boutiques (inventory), event venues and gyms
  (schedules), news/blog-driven businesses.
- **Portfolio anchor:** Cecere Brothers Landscaping (Harry's existing client) — use
  it as the credibility reference in pitches.

## Qualification rules (a business must pass ALL of these)

1. **Weak web presence:** EITHER no website at all (just Google Business / Facebook /
   Instagram), OR an outdated / broken / non-mobile-friendly website.
2. **Established:** clear signs it has operated for several years (founding year,
   review history, "since 20XX", established social presence). We are not pitching
   brand-new side hustles.
3. **Reachable:** a findable owner name, phone, email, or contact form.

Good reviews are a **bonus** (higher score), not a requirement.

## Pipeline stages & ownership

### Team 1 — Prospecting run (`scout` + `analyst` only — nothing is built)

| Stage | Owner | Model | Output |
|---|---|---|---|
| P1. Scout candidates (10–12) | `scout` | Sonnet | `pipeline/candidates.md` |
| P2. Score, research the top 3, capture their sites | `analyst` | Opus | `prospects/<slug>/dossier.md` + `site-content.md` |
| P3. **Deliver the shortlist** (final output) | `analyst` → lead | Opus | Top 3 with winnability pitches **and contact info** |

**The run ends at the shortlist.** Never spawn a planner, builder, or critic in a
prospecting run — there is nothing to build yet.

### Between the teams — Harry (no agents)

Harry contacts the prospects himself, in his own words. Anyone who says yes gets
**`templates/Website-Questionnaire.docx`** — a standing, client-ready questionnaire
covering everything a build needs. It requires **no run to produce**: it's already
written and sits in the repo. Harry collects the answers and pastes them into the
Build run.

### Team 2 — Build run (`planner` + `builder` + `critic`)

| Stage | Owner | Model | Output |
|---|---|---|---|
| B0. Save the client's answers | lead | — | `prospects/<slug>/client-answers.md` |
| B0a. *(only if a prior build for this prospect was speculative)* log the delta | `planner` | Fable | rows appended to `pipeline/speculation-log.md` |
| B0b. *(only if no dossier exists)* capture-only research | `analyst` | Opus | `dossier.md` + `site-content.md` for this ONE business |
| B1. Plan FROM the answers | `planner` | Fable | **`build-sheet.md`** (the Builder's only input — self-contained, lint-clean) + `website-plan.md` (the reasoning, for Harry + Critic) |
| B1b. **Sheet review** — judgment pass BEFORE any build | `critic` | Opus | **SHEET GO** message, or a numbered fix list back to the planner (≤2 rounds, then lead) |
| B2. Build (starts only on SHEET GO) | `builder` ×1 | Opus | `prospects/<slug>/mockup/` + `screenshots/` + the **evidence block** in STATE.md |
| B3. Critique loop | `critic` | Opus | `prospects/<slug>/audit.md` (every round) + fix messages, sign-off |
| B3b. **Publish to Claude Design** | lead | — | A card-per-section design-system project at claude.ai/design (`/design-push`) |
| B3c. *(only if the site was edited in the Design pane)* **Pull those edits back** | lead | — | `/design-pull` → the edits land in `mockup/`, round-trip verified |
| B4. **Iterate with the client** | Harry ↔ client | — | Feedback → Harry reopens → builder revises → **re-run `/design-push`** |

**Client answers are the top authority.** The hierarchy, highest first:

1. **The client's questionnaire answers** (`client-answers.md`) — controlling.
2. The business's own current statements (their website, a Google Business post).
3. Directories and aggregators (Yelp, Manta, LinkedIn, YellowPages).

When the answers conflict with the old site's content or anything the Analyst inferred,
**the answers win** — it's their site and they just told us what they want. This binds
the Analyst too: in a Build run's capture-only mode it reads `client-answers.md` first, and its
dossier **supplements the answers rather than correcting them** — any difference between
an answer and a public source goes into a **"Confirm with client (optional)"** note for
Harry, never a `[verify]` blocker and never resolved in the old site's favor. Content
parity still applies to real content the answers didn't override (the questionnaire asks
what they want kept, changed, or dropped).

`<slug>` = kebab-case business name, e.g. `montclair-stone-masonry`.

**Division of design labor:** the `planner` (Fable) makes ALL the design decisions —
art direction, fonts, palette, page map, per-section layout — and writes the executable
result into **`build-sheet.md`** (template: `templates/build-sheet-template.md`), a
self-contained contract the `builder` (Opus) executes top to bottom without re-deciding
anything. **The sheet outranks `website-plan.md`** — the plan carries the Planner's
reasoning for Harry and the Critic, and the Builder never reads it; a sheet that forces
the Builder into the plan is a Planner defect. (A real 588-line plan was half rationale,
and building one hero from it took ~14 lookups across 11 headings — that's the failure
the split prevents.)

## Speed rules — overlap the work, never lower the bar

Runs are slow because teammates WAIT on each other, not because the work is slow. Every
teammate follows these; none of them touch a quality gate.

1. **Stream your output downstream as soon as a unit is usable.** Don't sit on a finished
   batch waiting for the whole set — the scout messages the analyst every 5–6 verified
   candidates rather than delivering all 10–12 at the end; the planner hands its finished
   plan to the builder the moment it's done instead of polishing it further.
2. **Parallelize independent work.** The analyst researches all three finalists at once
   (one subagent each). Image generations are the exception — the builder runs them
   **one at a time**, because Kie rate-limits concurrent jobs.
   **Delegated research must return verbatim quotes + source URLs (never summaries) and
   surface source contradictions rather than resolving them — and the analyst still
   verifies the load-bearing facts against primary sources itself.** Delegation speeds up
   discovery; it never replaces your own eyes on the source.
3. **Do prep work while blocked.** A builder waiting on its plan still reads the dossier,
   downloads the real logo, scaffolds folders, and starts its server — everything that
   doesn't depend on a design decision it isn't allowed to make.
4. **Review on arrival.** The critic audits the mockup the moment it's submitted, and
   turns each re-submission around as it arrives — the builder is blocked until the fix
   list lands.
5. **Don't gold-plate the search.** Time-box discovery work (the scout stops at ~12 solid
   candidates); depth per item stays the same. **A time-box never justifies
   under-delivering a required count** — the scout's floor is 10 qualifying candidates; a
   dry search means change angle, not stop. If a floor genuinely can't be met, say so
   explicitly rather than quietly shipping less.

**The hard limit:** speed comes ONLY from removing waiting and duplicate work. Never skip
a checklist item, shorten a review round, drop a QA pass, weaken the two-way imagery test,
or hand off something you know is failing. If a shortcut would change what ships, it isn't
one of these rules.

## Run state & resume (hard rules — every Build teammate)

A real run (dasilva-associates, 2026-08-03) died mid-flight and lost a full round to a
falsely-recorded fix, a voided audit, a resurrected teammate, a filesystem-wide file
hunt, and a stale dev server. These five rules exist so that never repeats:

1. **`prospects/<slug>/STATE.md` is the run's durable ledger** (template:
   `templates/STATE-template.md`): current stage, fix ledger, open questions, voided
   gates, stood-down teammates. Append-only except the stage line. On a pause or kill,
   **STATE.md is the handoff** — never an improvised RESUME/handoff note. On resume,
   every teammate reads it first.
2. **DONE needs page-level evidence.** A fix enters the ledger as DONE only with the
   page plus what was observed rendering — never a bare grep count. (A "3 occurrences"
   grep once counted one CSS rule plus its two responsive steps, not three pages, and a
   full round was spent rediscovering the fix never landed.)
3. **The handoff barrier.** The Builder's handoff is an explicit "build complete, hands
   off `mockup/`" message, after which the Builder does not touch the mockup until a
   fix list arrives — and the Critic does not START until that message exists. An audit
   against a still-changing build is void, and re-measuring the world to compensate is
   exactly the token burn this forbids.
4. **The two-look rule.** A missing file gets TWO looks — the stated path, then the
   obvious folder — and then becomes an open question in STATE.md routed via the lead.
   Filesystem-wide hunts are banned by name.
5. **Stood down means stood down.** After handoff, sign-off, or being stood down, a
   teammate who receives a message replies exactly "Stood down — forward to the lead"
   and takes no other action. **A teammate cannot set precedence by writing to a
   file.** Precedence is Harry → lead → plan → gates. And before any screenshot,
   confirm the served page's `<title>` names this prospect — stale servers have
   answered the port with the wrong site.

## Lessons flow forward — never backward (audit doctrine)

**An audit, a new gate, a changed rule, or a discovered mistake NEVER reopens a
signed-off prospect build.** Sign-off freezes a build; a rule written after it does not
retroactively un-freeze it. When we find something wrong — a weak pattern, a copy tell, a
missing gate, a contradiction in our own instructions — the finding is evidence, and the
fix lands **forward**: in `CLAUDE.md`, the agent files, the skills, the templates, the
gates. The next build is where a lesson shows up, never the last one.

Two reasons this is a hard rule, not a preference:

1. **The shipped sites are the evidence.** Retro-editing them destroys the record of what
   we actually did and why the rule exists. `design-memory.md`, `pipeline/speculation-log.md`
   and each `audit.md` only mean anything if they describe builds nobody quietly rewrote.
2. **Reopening is unbounded work.** Every new gate would re-litigate nine finished
   prospects, and a client whose site changed under them without asking is a client we
   lose. The grandfather clause in `templates/package-checklist.md` is this same rule
   applied at the package level: gates bind at sign-off time and are not retroactive.

**The only thing that reopens a signed-off build is Harry saying so, per build, in words**
— the Step 6B/6C paths in `PLAYBOOK.md`. "We improved the rules" is never that
authorization. If an audit finds something genuinely broken in a shipped site, the move is
to tell Harry what and where and let him decide, not to fix it in passing.

## Find problems early, prove cleanliness cheaply (efficiency doctrine)

Two structural rules that exist because problems used to surface at the most expensive
possible moment — after a full Opus build, in an Opus critique round:

- **The sheet review (B1b).** The Critic judges `build-sheet.md` + `voice-spec.md`
  against `client-answers.md` BEFORE the Builder starts: direction sanity, copy
  quality, content routing, format choices. plan-lint must already be exit 0 — the
  review is judgment, not mechanics. Verdict is one message: **"SHEET GO"** or a
  numbered fix list to the Planner (two rounds max, then the lead). **No build starts
  without SHEET GO.** A ten-minute review that kills a bad sheet saves an entire build
  round — the best token trade in the pipeline.
- **The evidence block.** The Builder's handoff must carry proof in STATE.md: detector
  exit codes per page, copycheck + aitells exit codes, composition counts, screenshot
  list. The Critic spot-checks ONE claim at random and — if it holds — **re-runs no
  mechanical checks at all**, spending its round purely on judgment (realism, taste,
  client fidelity). A handoff without the evidence block is bounced unreviewed.

**Model policy — Opus only where judgment lives.** Fable plans. Opus builds, critiques,
and writes dossiers. **Sonnet scouts and runs cold reads** (fresh eyes matter; depth
doesn't). Scripts do everything mechanical for free. Never spend Opus tokens re-deriving
what a script or an attached exit code already proves.

## Per-prospect output contract

Each approved prospect gets a folder `prospects/<slug>/` containing:

**From the Prospecting run:**
- `dossier.md` — research + a page map + a "why this client is winnable" pitch +
  the contact info Harry needs to reach out.
- `site-content.md` — the Analyst's page-by-page FULL-TEXT capture of the existing site
  (required whenever the prospect has one) — the content-parity source of truth.

*(The client questionnaire is NOT a per-prospect artifact — it's the standing
`templates/Website-Questionnaire.docx`, sent as-is to anyone who says yes.)*

**From the Build run (only after the client's answers are in):**
- `client-answers.md` — the client's answers, saved verbatim by the lead from Harry's
  paste. The top authority for everything downstream.
- `build-sheet.md` — **the Builder's entire spec**: self-contained, lint-clean, and it
  outranks the plan. This is the contract.
- `STATE.md` — the run's durable ledger and the handoff on any pause (never a RESUME note).
- `website-plan.md` — the Planner's **reasoning record, for Harry and the Critic — the
  Builder never reads it**, including the
  **"Client answers → decisions"** section and the **content map** that places every
  site-content.md block (or lists it as deliberately dropped, with a reason).
- `voice-spec.md` — the Planner's copy-voice contract for this client, written via
  `trade-copy` Stage A from their answers, before any hero direction. It governs every
  visible string the Builder writes and is what the Critic's copy gate scores against; a
  missing one is a fail on the Planner.
- `mockup/` — **one `.html` per page in the plan's page map** (multi-page is the default;
  a single-file SPA is the exception for a page map small enough that separate files
  would be ceremony), plus one shared `style.css` and one `main.js` (+ `vendor/` if the
  plan's signature move needs the GSAP tier). Static only. Opens by double-click, no build step, **works offline** —
  libraries are vendored from the skill's `assets/gsap/`, never loaded from a CDN.
- `screenshots/` — desktop + mobile captures proving the QA passes ran.
- `release-form.pdf` (+ `release-form.html` source) — the Fora Digital **Website Release
  & Publication Approval**, pre-filled with this client's business name, contact, and the
  exact pages built. Harry sends it for signature when the client approves the site for
  launch. Generated by the Builder from `templates/release-form.html`; signature, date
  and checkbox fields stay blank, and unknown fields (domain, preview link) ship as clean
  blank lines rather than invented values.
- `audit.md` — the Critic's scored result for BOTH scoreboards ($10K Checklist 8/8 or
  documented exceptions, plus the 10-dimension rubric), rewritten every review round with
  a `Review round: N` line and a `Paid calls this prospect:` ledger line.

**Not a file in the folder, but part of the contract:** every signed-off prospect also has
a **Claude Design project** — its own card-per-section design system at claude.ai/design,
published by the lead with `/design-push`. That's where the site gets reviewed and precisely
edited before going live, so a signed-off prospect without one is incomplete.

## Delivery to Corey

Lead-only procedure, run after sign-off: **signed release form gates everything** (none
on file → stop), then the **gated packager** (`pipeline/package-site.sh <slug>` — refuses
on detector failures, placeholder leakage, or a missing design-memory row), then
`/design-push` to Claude Design. **Caretaker registration is NOT part of delivery** — the
caretaker only watches sites already live on a real domain, and at delivery the site is
still a zip. Note it for **go-live** (`FULL-PROCESS.md` Step 14), where the domain exists
and there is a URL to register.
**Full procedure with every step and check: `docs/delivery.md` — the lead reads it at
each delivery; teammates never need it.**
## The Mockup Recipe (the "DaSilva workflow")

Our house method — reference build `prospects/dasilva-associates/`. The `web-design-ultra`
skill is PRIMARY: the Planner runs its Stages 1–5 (Design Read, inspiration, three
divergent directions, per-section `format:`/`opener:` tokens, plan-lint clean), the
Builder executes Stages 6–7 (the plan's `GENERATE` images, budget-capped, + free CSS
craft; implements the plan, never re-decides it), the Critic owns Stage 8 (Step-0 detector scan, both scoreboards,
composition counts, content honesty, sign-off freezes the build). Precedence: client
brief + voice-spec → web-design-ultra direction + local-trade → the gates.
**The full recipe — stage-by-stage duties, token-block patterns, craft rules, gate
wiring — is `docs/mockup-recipe.md`. The Planner and Builder read it at the start of
every Build run; the Critic reads its Stage 8 half.** This summary is binding but not
sufficient to build from.
## The anti-slop standard (all three Build agents)

AI slop = the statistical mean: hero, three feature cards, testimonials, CTA, one
section shape repeated, vague copy. It's a **direction failure, not a creativity
failure** — absent constraint, output regresses to the default. Seven levers kill it;
each has an owner and most are mechanically enforced:

| # | Lever | Owner | Enforced by |
|---|-------|-------|-------------|
| 1 | Named art direction before building | Planner | direction brief (Stage 5) + taste §0 **Design Read** |
| 2 | Banned defaults (fonts, purple-gradient, card-wall) | Builder | detector blocking rules |
| 3 | Section-format variety | Planner assigns, Builder obeys | `section-shape-repetition` + `repeated-section-kickers` (blocking) + critic counts |
| 4 | Deliberate symmetry break | Planner names device, Builder lands it | critic composition check (screenshot) |
| 5 | Scale contrast as hierarchy | Builder | `flat-type-hierarchy` (blocking, ≥1.25 step ratio) |
| 6 | Copy specificity — ≥1 falsifiable fact, no abstract-pair labels | Builder (trade-copy + web-humanizer) | `copycheck.py` + `aitells.py` exit 0 |
| 7 | Real assets — real logo, real photos or labeled placeholders, never stock | Builder | critic imagery gate |
| 8 | Plan lint — quotas and required fields checked before a line is built | Planner | `plan-lint.mjs` exit 0 before handoff |

**After changing any gate, rule, threshold, or agent instruction, run the fire drill:**

```bash
pipeline/fire-drill.sh
```

It costs nothing and takes seconds. Against the synthetic fixtures in
`pipeline/fixtures/` it checks that every gate both **accepts a known-good build**
and **rejects a known-bad one** — the second half being the one that matters, since a
gate that quietly stopped firing is indistinguishable from a clean codebase. If it goes
red, find the change that caused it; never loosen the fixtures to make it green.

Process levers that keep builds from converging on each other: evidence before design
(Stage 3), three forced-divergent directions (Stage 5), the anti-repetition log
(`design-memory.md`, Stage 4/8), **the voice anti-repetition log (`copy-memory.md`) —
every hero this crew has shipped and the constructions now spent, because two clients
already got the same three-fragment-plus-founding-year hero** — deterministic detection
(Step 0 scan), and the screenshot rubric (Stage 8). **A build that ships with any lever unaddressed is not
done** — the critic's audit records where each one landed.

## The `Inspiration/` library

`~/Projects/essex-web-crew/Inspiration/` is Harry's curated reference folder. The Planner
**checks it first at Stage 3**, before opening the browser — but it supplements live-site
research, it never replaces it. Filenames are content hashes, so identify images by
looking at them. Two kinds, two uses:

- **Site mockups / screenshots** → design references. Dissect them like any live site and
  fill an evidence sheet. Extract patterns, never clone.
- **Photography** (trade work, machinery, landscape) → art-direction reference for the
  register of a shot (lighting, camera height, grit level), and a permitted
  **image-to-video seed frame**.

**Transformation rule (hard).** These are collected references, not licensed stock.
Describing their style in a prompt is always fine. Seeding an image-to-video shot from one
is allowed **only if the plan named the file**, and the output must be a *new shot the
reference informed* — not that photograph with motion added. An image from this folder is
**never shipped as a still**, and never used for a logo or a real person's likeness. The
Critic compares any clip against its named source.

## Image policy (hard rule)

**No count cap — the site budget is the only limit.** Generate as many images as the design
genuinely needs through the `/generate` skill on **`nano-banana-2`** (the shipping tier,
never `-lite`; ~$0.04 at 1K / ~$0.06 at 2K), keeping the **projected total inside the
site's all-in budget** ($1.00 no video / $1.50 with one — see Video policy below). At those
rates $1.00 is ~16 images at 2K or ~25 at 1K, so on a still-only site money is not the
binding constraint — **design judgment is.** Generate what makes the page look finished and
specific; don't pad to spend the budget, don't starve a page that needs six plates.
The Planner marks every generated slot `GENERATE` (hero first, then by visibility, each
with register + aspect + resolution) and carries a running cost total. **Slots whose real
answer is the client's own job photography stay labeled AI-IMAGE placeholders** — that is a
content-honesty call, not a cost one. The client's real logo never counts against the
budget and is never regenerated. Anything that would break the budget needs the lead to ask
Harry. **Full policy (registers, sizing, realism QA, spend ledger): `docs/media-policy.md`
— read it before any generation.**
## Video policy (hard rule)

**Default is zero video, and video is NEVER pre-approved** — the Planner may mark ONE
`VIDEO` slot as a REQUEST (register `filmed-action` or `designed-loop`, ≤8s, never both),
the lead takes it to Harry, and **the Builder generates nothing until Harry
says yes to that specific clip.** One approval = one run, no retries without a fresh ask.

**THE SITE BUDGET (hard rule, 2026-08-04): one all-in number per site covering ALL paid
generation — images, video, everything. $1.00 if the site ships no video; $1.50 if it
ships one.** Images spend against it first, so budget the clip before the stills — a
handful of images (~$0.20–0.30) still leaves over $1.10 for it. This replaced the old per-register ceilings (filmed ≤$1, designed ≤$2.50);
register choice no longer buys extra money. A failed clip has already spent the budget —
exhaust the free `ffmpeg` fixes, then ship the poster still. The budget is a **ceiling on
an approved ask, never an authorization to spend.**
Work the free ladder first (backgrounds → atmosphere → reactive field); a clip-free build
is never a deduction. Shipping needs `poster` + `prefers-reduced-motion` + <5MB + checked
loop seam. **Full policy (registers, gates, ladder, occupational fit): `docs/media-policy.md`
— the Planner reads it before marking a slot; the Builder before generating; the Critic
before gating a clip.**
## Content honesty (hard rule)

Do not fabricate facts about a real business — no invented awards, fake years in
business, made-up review counts, or fictional staff. If a detail isn't in the dossier,
write around it or use an obvious placeholder (`[years in business]`). The mockup is a
design demonstration, not a claim of fact.

**Information currency (hard rule).** The mockup must reflect the business **as it is
today**, not as an old source describes it. When sources conflict, the business's own
most recent statement wins — its current website or a Google Business post outranks stale
directory listings, LinkedIn, or aggregators. A change the business itself has announced
(new ownership, a new name, a moved address, a dropped service) is a **current fact**, not
a "discrepancy" to hedge around: put it on the site honestly (e.g. "founded 30+ years ago
by X, now owned by Y"), don't render the outdated version as if nothing changed. Only fall
back to `[verify]` when the business itself hasn't made the current state clear anywhere.

**Real reviews only (hard rule).** A testimonial or review appears on a mockup ONLY if
it is a **real review the Analyst actually found and captured** in the dossier —
verbatim quote + reviewer first name + source platform (Google / Yelp / Facebook /
Angi). **Never write a testimonial for the demo, never paraphrase a review into
something nicer, never invent a reviewer.** If the dossier has no real reviews, the
mockup has **no testimonial section** — or, if the layout needs one, a clearly-labeled
`[Real review goes here — none captured yet]` placeholder block, never fabricated
praise. This is the review-specific case of the broader rule: **do not make up any
information** about the business — reviews, awards, stats, staff, history, or anything
else.

## Use the client's real content (hard rule)

Most prospects already have a website — that's what we're improving on. When they do,
**reuse their real content, don't invent new content.** The Analyst captures the existing
site's actual services, descriptions, service area, hours, contact info, and testimonials
into the dossier; the Planner structures that real material and the Builder renders it.
We are upgrading the **design and structure**, not rewriting the business. Only use
`[placeholder]` text where information genuinely doesn't exist. This keeps the pitch
honest and makes the site feel like *theirs*, done right.

**Their old site is a fact source, not a voice source** — see Copy voice below. Carry
every fact; don't inherit the phrasing.

## Content parity (hard rule)

**The new site must never know less than the old site. Richer design AND richer
information — that's the pitch.** A beautiful mockup that carries a fraction of the
original's information is a failed mockup: the owner notices their missing content
before they notice our typography. The pipeline summarizes at every hop (site → dossier
→ plan → build), so parity is enforced with an explicit artifact chain:

1. **Analyst** captures the existing site page-by-page, FULL TEXT, into
   `prospects/<slug>/site-content.md` (the dossier summarizes; this file preserves).
2. **Planner** writes a **content map** in `website-plan.md`: every site-content.md
   block gets a destination page/section, or goes on a **"Deliberately dropped"** list
   with a one-line reason. No silent drops. Long-form educational content (pest guides,
   how-it-works explainers, permit directories) is real content — default is CARRY it;
   the page map grows to fit the content, not the other way around.
3. **Builder** transfers mapped blocks at full informational fidelity — their service
   descriptions stay descriptions, their articles stay articles, their town lists stay
   complete. Punchy is for heroes and CTAs, not for the informational body.
4. **Critic** walks site-content.md against the mockup: every block present or
   accounted for on the dropped list, else a numbered fail list. This is a hard gate.

**Parity counts facts, not words.** Tightening a 60-word description to 25 words that
carry the same facts passes; dropping a fact fails. Nobody pads to survive a parity
review, and nobody bounces a mockup for being tighter than the old site.

## Copy voice (hard rule)

A site can be beautifully built and still read fake, and the owner feels it immediately:
sentences he'd never say out loud, one pretty word carried through every section, a dash
in the middle of every line restating what the first half already said. That's the single
most common complaint about our output.

**The client's questionnaire answers are the voice source.** Their old site supplies
facts only. How the copy sounds comes from how *they* talk.

**Copy is specification, not prose** — concrete nouns, numbers, towns, materials, hours.
When a section has no real facts behind it, shrink it or cut it. Never write around the
hole with atmosphere; that is where every bad line in this project has come from.

**The voice is a licensed contractor talking to a homeowner in his driveway.** Three ways
to miss it: **too poetic** ("meticulous by habit"), **too cute** ("we read the sun",
"won't need babying", trade puns, winking), **too vague** ("when the weather turns, we
show up"). "Plain" is not the target — plenty of cutesy copy is plain. Professional is.

Enforced with an artifact chain, same shape as content parity:

1. **Planner** mines `client-answers.md` into `prospects/<slug>/voice-spec.md` — register,
   the client's own phrases, word budgets, banned words, and which sections are
   pre-authorized to be short because the facts are thin. Written BEFORE the hero
   direction.
2. **Builder** writes every visible string against that spec, then runs
   `python3 skills/trade-copy/scripts/copycheck.py prospects/<slug>/mockup/index.html`,
   then sweeps the page with **`web-humanizer`** and runs
   `python3 skills/web-humanizer/scripts/aitells.py prospects/<slug>/mockup/*.html`.
3. **Critic** re-runs both scripts as a hard gate AND reads the page one sentence at a time
   asking whether the owner would say it aloud. The script can't catch "meticulous by
   habit"; a person can.

Two skills, two failure modes, and they do not overlap. **`trade-copy`** owns *register* —
how the owner talks, word budgets, banned vocabulary, em dashes, cutesiness.
**`web-humanizer`** owns *page shape* — the tells that survive a correct register: a hero
opening with a verb any industry could use, card titles built from two abstractions
("Professional Service"), a page carrying no number a customer could check, cards stamped
to identical lengths. Their word lists are deliberately disjoint so no single word gets two
different fixes; both push the same direction, which is more concrete.

Real review quotes, **Q7** keep-word-for-word content, legal text, and NAP are exempt from
every check and are never edited. Nothing is ever *added* to a page to satisfy a check —
terseness passes, invented facts never do. Full rules: the **`trade-copy`** and
**`web-humanizer`** skills.

## Skills each agent uses

Skills are NOT auto-loaded for teammates (the agent-teams runtime doesn't apply the
`skills` frontmatter field) — each agent must invoke them itself via the Skill tool, and
each agent's `tools` list includes `Skill`.

**A required skill that won't load is a stop-and-report, never a proceed-without.** If a
skill marked PRIMARY (or a `references/*.md` file it depends on) is missing or fails to
invoke, say so to the lead and stop that step. Do not improvise the skill's contents from
memory — the whole point of the skill is that it is more current and more specific than
what you'd reconstruct, and a build done from a half-remembered version of the design
pipeline is exactly the generic output the pipeline exists to prevent.

| Agent | Skills to invoke | Why |
|---|---|---|
| `scout` | `research`, `docs-seeker` | Deeper competitor/reputation research when a web search isn't enough; finding directories/docs on unfamiliar trades. |
| `analyst` | `research` | Comprehensive dossier research beyond a plain web search. |
| `planner` | **`web-design-ultra` (PRIMARY)**, **`trade-copy`**, **`taste-skill`**, `ui-ux-pro-max`, `frontend-design`, `design-system`, `aesthetic`, `sequential-thinking` | Run the 8-stage art-direction pipeline (Stages 1–5): design intelligence, real-site inspiration, anti-repetition, three divergent directions. `taste-skill` supplies the §0 Design Read, §0.D Anti-Default and §9 AI-Tells passes over the three directions (planning sections only — its stack picks and block library are the Builder's territory). `trade-copy` Stage A produces `voice-spec.md` from the client's answers before the hero direction is written. Names each reference site's patterns using the skill's `inspiration.md` vocabulary, and doesn't lock a direction the Stage 8 composition checks will fail — any deliberate exception is stated in `website-plan.md`. |
| `builder` | **`web-design-ultra` (PRIMARY)**, **`trade-copy`**, **`web-humanizer`**, `generate`, `ui-ux-pro-max`, `frontend-design` | Execute the chosen direction (Stage 7): generate every image the plan marked `GENERATE` (`/generate` on `nano-banana-2`; no count cap — stop at the site budget), plus an approved video clip if there is one, craft discipline + backgrounds/atmosphere recipes; self-score the Stage 8 rubric. `trade-copy` governs every visible string — invoke before writing any text; `web-humanizer` is the sweep after it, catching the page shapes that still read machine-written (interchangeable hero verbs, abstract-pair card titles, no checkable fact, cards stamped to identical lengths) and gating on `aitells.py` exit 0 alongside `copycheck.py`. Reads the skill's `craft-floor.md` before editing UI, works `motion-thesis.md` / `layout-craft.md` / `type-craft.md` / `color-craft.md` when a build needs more than a first pass, and runs the Step 0 scan to `exit 0` before handoff. |
| `critic` | **`web-design-ultra`**, **`trade-copy`**, **`web-humanizer`**, `ui-ux-pro-max`, `code-review`, `design-system` | Audit each mockup against the Stage 8 10-dimension rubric AND the $10K Checklist; enforce real-reviews-only and the COPY VOICE gate (`copycheck.py` + `aitells.py` + a say-aloud read + the cold read); code-quality + design-system rigor. Runs the skill's Step 0 scan as the **first** gate, before any screenshot, then the fail-visible measurement and the composition checks; drives fix rounds with `bolder.md` / `quieter.md` rather than freehand nudges. |
| `caretaker` | `site-caretaker-cycle` (from `~/Projects/site-caretaker/.claude/skills/`) | Post-launch only, and only for sites already live on a real domain. Keeps `~/Projects/site-caretaker/sites.json` — the system of record for published sites — current, and diagnoses the uptime/DNS/TLS/content failures the hourly `com.sitecaretaker.monitor` job flags. Never edits a live site on its own, and never polls in a loop: Layer 1 already watches, for free, every hour. Its standing spec is `~/Projects/site-caretaker/VISION.md`, which lives outside this repo — so the role only works on a machine that has it. |
| `fora-benchmark` | — | **FORA-internal, never a client run.** Researches well-executed sites (Fortune 500, small agencies, local trades) and returns a pattern table plus a "copy bar". Writes no files: its output is pasted by hand into `fora-site-auditor`'s task context. |
| `fora-site-auditor` | `trade-copy`, `web-humanizer` | **FORA-internal, never a client run.** Audits foradigital.com — repo source plus the live site in the browser pane — across seven categories, and grades copy against `fora-benchmark`'s bar plus `copycheck.py` / `aitells.py`. Read-only. Client mockups under `prospects/` are the `critic`'s, never its own. |
| **lead** (this session) | **`design-push`**, **`design-pull`**, **`github-push`**, **`github-pull`** | Publish each signed-off site to Claude Design (Stage 8 on-pass step B3b), and re-publish after every revision round. `design-pull` brings edits made in the Design pane back into `mockup/` before a push can overwrite them — and `design-push` refuses to run while any exist. Only the lead can: `DesignSync` is authorized in this session, not in any subagent. `github-pull` / `github-push` move the whole repo between Harry's Mac and Corey's — **pull at the start of a session, push when a run finishes.** Details in `github/README.md`. |

Optional, invoke only if the situation calls for it: `media-processing` (Builder — if
processing real images pulled from an existing client site) and `ai-multimodal`
(Analyst — if extracting content from screenshots of an existing site's design).

## Tooling rules

- **Free tools first.** Use built-in `WebSearch` / `WebFetch` and the browser pane for
  all research and scraping. **Do NOT call Firecrawl or Perplexity** (they cost Harry
  money) — if a page genuinely can't be reached any other way, stop and ask the lead,
  who asks Harry.
- **The only pre-approved paid operation is image generation, and it is pre-approved up to
  the site budget — not to a count.** Generated through the `/generate` skill on
  **`nano-banana-2`** — the shipping tier, never the `-lite` draft model. It costs real
  money (~$0.04 at 1K / ~$0.06 at 2K), and the builder may spend up to the site's all-in
  budget on it: **$1.00 with no video, $1.50 if a video is approved.** A builder generating
  eight images that total $0.40 is following the rules, not breaking them. Track the
  running total; the moment a plan would break the budget, the lead asks Harry.
- **Video is NOT pre-approved — it is a request.** The Planner may mark ONE justified
  `VIDEO` slot in its declared register (`filmed-action` or `designed-loop`, ≤8s, never
  both — see the Video policy above), priced to fit the site's **$1.50 all-in budget
  alongside its images**, but marking it only *asks*. **The lead
  takes that request to Harry, and the Builder generates nothing until Harry has said yes
  to that specific clip.** No answer yet → the poster still ships in the slot and the site
  is otherwise complete. A clip with no recorded approval is unauthorized spend and the
  Critic hard-fails it.
- Everything beyond — any spend that breaks the site budget, any video without a confirmed
  yes, a 2nd clip, 4K, a longer clip, or any other paid call — needs the lead to ask Harry
  first.
  "Free tools only" elsewhere in these docs means *no Firecrawl/Perplexity*; it never meant
  skipping the sanctioned assets.
- **Never contact a business.** No emails, no form submissions, no DMs, no calls.
  Drafts only.

## Token reminder

Every teammate is a full Claude instance (~7× cost of a solo session). Keep scope
tight, mark tasks complete promptly, and shut down when your work is signed off.
