# Essex Web Crew

**Setting this up on a new machine? Start with [SETUP-COREY.md](SETUP-COREY.md).**

A Claude Code **agent team** that runs like a mini web agency. Each run it scouts
Essex County, NJ businesses whose websites are naturally static/low-maintenance
(leading with trades, but any industry that fits), scores them, pauses for Harry's
approval, then builds a full review-ready pitch package for the top 3: a research
dossier, a working website mockup (built the "Corey Blake workflow" way), and personalized
outreach — an email when a real address was found, otherwise a phone number + call script.

Each mockup ships with **2 real AI-generated images** (hero + one priority slot) and
labeled placeholders for the rest, run through the `web-design-ultra` design pipeline.

**The team never contacts anyone.** Everything lands on disk for Harry to review;
Harry generates the remaining images and sends outreach himself.

## Layout

```
CLAUDE.md                 Shared playbook (all teammates read this)
design-memory.md          Anti-repetition log — planner reads, critic appends per sign-off
HOW-TO-RUN.md             Quick start (terminal steps + paste prompts)
run.sh                    Launcher (sets the agent-teams flag)
KICKOFF.md                How to run — dry run + full run prompts
PLAYBOOK.md               Harry's pitch-phase scripts — whole-run walkthrough + review decision tree
FULL-PROCESS.md           The whole journey (Steps 1–15): pitch phase + client phase — real content/photos, production build, domain, go-live, maintenance
.claude/
  settings.local.json     Enables agent teams (experimental flag)
  agents/                 Teammate roles: scout, analyst, planner, builder, copywriter, critic
pipeline/
  rubric.md               Candidate scoring rubric
  candidates.md           Scout output → Analyst scoring (regenerated each run)
templates/
  email-voice.md          Outreach email voice guide
  package-checklist.md    Critic's sign-off gate (both scoreboards + imagery realism +
                          local-trade + outreach checks)
prospects/
  <slug>/                 One folder per approved prospect:
    dossier.md · website-plan.md · mockup/ (incl. assets/) · screenshots/
    outreach-email.md OR outreach-call.md · audit.md
```

## The team

| Role | Model | Skills | Does |
|------|-------|--------|------|
| **scout** | Sonnet | `research`, `docs-seeker` | Finds 10–12 qualifying businesses — any industry with a naturally static site, leading with trades (free web tools; no Firecrawl/Perplexity). |
| **analyst** | Opus | `research` | Scores them, captures each finalist's real site content + real reviews, writes dossiers, pitches the shortlist. |
| **planner** | Fable | **`web-design-ultra`**, `ui-ux-pro-max`, `frontend-design`, `design-system`, `aesthetic`, `sequential-thinking` | Runs the web-design-ultra pipeline (Stages 1–5) → `website-plan.md`: art direction, fonts, palette, page map, three divergent directions. |
| **builder** ×3 | Opus | **`web-design-ultra`**, `ai-multimodal`, `ui-ux-pro-max`, `frontend-design`, `frontend-development`, `web-frameworks` | Each *implements* one prospect's chosen direction (Stage 7) into a mockup with 2 real AI images (hero + 1) + placeholders beyond; owns its own folder. |
| **copywriter** | Sonnet | `humanizer`, `brand`, `sequential-thinking` | Writes the personalized outreach email + one-pager if the dossier has an email; otherwise a phone number + call script. |
| **critic** | Opus | **`web-design-ultra`**, `ui-ux-pro-max`, `code-review`, `design-system` | Audits every mockup against the Stage 8 rubric + the $10K Checklist; enforces real-reviews-only; loops until sign-off. |

The lead session orchestrates, enforces the approval pause, and assembles results.
Design decisions live with the **planner** (Fable); the **builder** (Opus) implements
them and doesn't re-decide the design.

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
