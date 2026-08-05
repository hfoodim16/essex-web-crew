# Essex Web Crew

**Setting this up on a new machine? Start with [SETUP-COREY.md](SETUP-COREY.md).**

> **`CLAUDE.md` is canonical.** Rules, checklists, and role/skill assignments are defined
> there. If this file disagrees with `CLAUDE.md`, `CLAUDE.md` wins — fix this file.

A Claude Code **agent team** that runs like a mini web agency on an **ask-first** model:
find a business that could use a website → **ask what they want** → build from their
answers → keep refining it with them. We never build a site speculatively and pitch it.

The work is split into **two independent teams** that never run together (both prompts in
[KICKOFF.md](KICKOFF.md)):

- **Team 1 — Prospecting run.** `scout` + `analyst` only. Scouts Essex County, NJ
  businesses whose websites are naturally static/low-maintenance (leading with trades, but
  any industry that fits), scores them, then researches the top 3 and writes each one a
  research dossier plus a full capture of their existing site. The run's final output is
  **the shortlist with contact info** — then it ends. **Nothing is built, and there's no
  approval pause.**
- **Between the teams — Harry, no agents.** He contacts the prospects himself, call or
  email, in his own words. Anyone who says yes gets
  [`templates/Website-Questionnaire.docx`](templates/Website-Questionnaire.docx) — a standing,
  client-ready 17-question questionnaire that needs no run to produce. Harry collects
  their answers.
- **Team 2 — Build run.** `planner` + `builder` + `critic` (plus a capture-only `analyst`
  if the client has no dossier yet). Input is the client's answers, saved to
  `client-answers.md`. The planner plans FROM the answers (they outrank the old site and
  the dossier), one builder builds it the "DaSilva workflow" way, the critic gates it,
  and the site goes back to the client for feedback and iteration.

Each built site ships with **real AI-generated images in every slot the plan marked `GENERATE`** (hero first) and
labeled placeholders for the rest, run through the `web-design-ultra` design pipeline.

**The team never contacts anyone.** Everything lands on disk for Harry to review; all
client contact is Harry personally, and he relays the client's answers back.

## Layout

```
SETUP-COREY.md            First-time setup on a new machine (start here)
install.sh                One-shot installer used by SETUP-COREY
CLAUDE.md                 Shared playbook (all teammates read this)
design-memory.md          Anti-repetition log — planner reads, critic appends per sign-off
HOW-TO-RUN.md             Quick start (terminal steps + paste prompts)
run.sh                    Launcher (sets the agent-teams flag)
KICKOFF.md                How to run — dry run + Prospecting + Build run prompts
PLAYBOOK.md               Harry's pitch-phase scripts — whole-run walkthrough + review decision tree
FULL-PROCESS.md           The whole journey (Steps 1–15): pitch phase + client phase — real content/photos, production build, domain, go-live, maintenance
COREY-DEPLOY.md           Deploying a signed-off site
.claude/
  settings.local.json     Enables agent teams (experimental flag)
  agents/                 Teammate roles: scout, analyst (team 1) · planner, builder,
                          critic (team 2) · caretaker (post-launch) ·
                          fora-benchmark, fora-site-auditor (FORA-internal)
  launch.json             Dev-server configs for the browser pane (if present)
design-gates.md           One-page map of where every quality gate lives
docs/
  mockup-recipe.md        The full DaSilva build recipe (read on demand)
  media-policy.md         Image + video policy and the all-in site budget
  delivery.md             Handoff and go-live steps
skills/                   Vendored Claude Code skills, installed by install.sh
                          (web-design-ultra is the design engine; trade-copy and
                          web-humanizer are the copy gates)
lab/                      Technique test builds referenced by the skills
Inspiration/              Reference photography + site mockups (never shipped as-is;
                          see Inspiration/hero-plates.md)
audit/                    FORA's own site audits (not client work)
github/                   Moving work between Harry's Mac and Corey's — see github/README.md
  scripts/preflight.sh    Shared sync checks (finds the repo, verifies login, reports the gap)
  skills/github-push/     "push this" — pull first, safety-check the diff, commit, push
  skills/github-pull/     "pull" — show what's incoming, protect local work, pull, re-install skills
pipeline/
  rubric.md               Candidate scoring rubric
  candidates.md           Scout output → Analyst scoring (regenerated each run)
  package-site.sh         Packages a signed-off site for delivery
  fire-drill.sh           Verifies every gate still accepts good / rejects bad —
                          run after ANY gate, rule, or agent change
  speculation-log.md      What we guessed vs what the client actually said
  _smoke-test/            The fire drill's fixtures (never delete to go green)
templates/
  Website-Questionnaire.docx
                          Standing client questionnaire — sent as-is to anyone who says yes
  release-form.html       Release & publication approval, filled per client by the Builder
  package-checklist.md    Critic's sign-off gate + the $10K Checklist's full text
  build-sheet-template.md The Builder's spec contract — shape the Planner fills in
  client-intake-template.md
                          Scratchpad for facts a client still owes; answers graduate
                          into client-answers.md
  STATE-template.md       Per-run ledger; the handoff on any pause (never a RESUME note)
prospects/
  <slug>/                 One folder per prospect:
    from the Prospecting run:  dossier.md · site-content.md
    from the Build run:        client-answers.md · build-sheet.md (the Builder's spec) ·
                               website-plan.md (the reasoning) · voice-spec.md ·
                               mockup/ (incl. assets/) · screenshots/ · audit.md ·
                               release-form.pdf · STATE.md
```

## The team

| Role | Team | Model | Does |
|------|------|-------|------|
| **scout** | 1 — Prospecting | Sonnet | Finds 10–12 qualifying businesses — any industry with a naturally static site, leading with trades (free web tools; no Firecrawl/Perplexity). |
| **analyst** | 1 — Prospecting (capture-only in 2) | Opus | Scores them, captures each finalist's real site content + real reviews, writes dossiers, delivers the shortlist with contact info. In a build run it only runs if the client has no dossier yet — research this ONE business, nothing else. |
| **planner** | 2 — Build | Fable | Runs the web-design-ultra pipeline (Stages 1–5) → **`build-sheet.md`** (the Builder's entire spec) + `website-plan.md` (the reasoning, for Harry and the critic): art direction, fonts, palette, page map, three divergent directions — planned FROM the client's answers. |
| **builder** | 2 — Build | Opus | One per build run, starting only on the critic's **SHEET GO**. *Implements* the **build sheet** (never the plan) into a mockup with real AI images in its `GENERATE` slots + labeled placeholders for the client's own photos. |
| **critic** | 2 — Build | Opus | Audits the mockup against the Stage 8 rubric + the $10K Checklist; enforces client-answer fidelity, content parity, real-reviews-only. Loops with the builder, capped at 3 fix rounds, then escalates a stalemate to the lead. |
| **caretaker** | Post-launch | Sonnet | Watches sites already live on a real domain: keeps the site registry current and diagnoses uptime/DNS/TLS/content failures flagged by the hourly monitor. Never edits a live site on its own. |
| **fora-benchmark** | FORA-internal | Sonnet | Researches well-executed sites and returns a pattern table + "copy bar" for **our own** agency site. Never spawned in a client run. |
| **fora-site-auditor** | FORA-internal | Opus | Audits foradigital.com — repo source + the live site — across seven categories, grading copy against the benchmark bar and the crew's copy gates. Read-only. Client mockups belong to the **critic**, never to this. |

**Per-role skills: see the role table in [CLAUDE.md](CLAUDE.md) — that table is
canonical.** Skills change often; keeping a second copy here is how the two drift apart.

The lead session orchestrates and assembles results — in a build run it also saves the
client's answers to `client-answers.md` before spawning anyone. Design decisions live with
the **planner** (Fable); the **builder** (Opus) implements them and doesn't re-decide the
design.

## Run it

Agent teams only work in a **terminal session started with the experimental flag on**.
Easiest way — the launcher handles the flag for you:

```bash
~/Projects/essex-web-crew/run.sh
```

(Or manually: `cd ~/Projects/essex-web-crew && CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 claude`.)

Then paste a prompt from `KICKOFF.md` — **do the dry run first** (agent teams are
experimental and token-heavy, ~7× a solo session). Note: this needs a real terminal
(Terminal.app / iTerm2); the desktop/web app surfaces don't render the teammate panel.
