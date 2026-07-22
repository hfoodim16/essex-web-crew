# Kickoff — Running the Essex Web Crew

## Before you start

1. Agent teams are **experimental** and **token-heavy** (each teammate is a full Claude
   instance, ~7× a solo session). A full run spins up several teammates plus subagents.
   Do the **dry run** first.
2. Agent teams must be enabled. This project ships `.claude/settings.local.json` with
   `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS: "1"`. Start Claude Code from THIS folder
   (`~/Projects/essex-web-crew`) so it's picked up. Split-pane view needs tmux or
   iTerm2; otherwise the default in-process agent panel works fine.
3. Recommend setting the default teammate model to **Sonnet** in `/config` (or it's
   requested in the prompts below).

---

## Dry run (cheap — do this first)

Paste this to the lead:

```
Read CLAUDE.md and .claude/agents/scout.md. Spawn ONE teammate named 'scout'
using the scout agent type. Task it to find just 5 qualifying Essex County, NJ
trade businesses (per the qualification rules in CLAUDE.md) and write them to
pipeline/candidates.md with evidence and sources. Use Sonnet. Free tools only —
no Firecrawl/Perplexity. When scout is done, review pipeline/candidates.md with
me. Do not proceed past the scout.
```

Check: `pipeline/candidates.md` has 5 real, verified, qualifying businesses with
evidence and source links, and the agent panel showed the scout working. If the output
is weak, refine `.claude/agents/scout.md` before the full run.

---

## Full run

Paste this to the lead:

```
Read CLAUDE.md and all files in .claude/agents/. Run the full Essex Web Crew
pipeline. Each teammate uses the model in its agent definition's frontmatter —
do NOT force a single model. The intended lineup is: scout=Sonnet,
analyst=Opus, planner=Fable (claude-fable-5), builder=Opus, copywriter=Sonnet,
critic=Opus. Free tools only — no Firecrawl/Perplexity. The one pre-approved
paid step is each builder generating its 2 AI images (~$0.17/prospect);
anything beyond that asks me first. Teammates must invoke their skills themselves via
the Skill tool (see the "Skills each agent uses" table in CLAUDE.md) — skills are
not auto-loaded for teammates.

Run stages OVERLAPPED, not strictly sequentially — teammates stream work to
each other as described in their agent files. Never weaken a quality gate to
save time.

1. Spawn 'scout' and 'analyst' (scout + analyst agent types) TOGETHER. The scout
   streams candidates to pipeline/candidates.md in batches of 5–6 and messages
   the analyst as each batch lands; the analyst scores incrementally instead of
   waiting for the full list.
2. The analyst researches the top 3 finalists IN PARALLEL (one research subagent
   each), writes prospects/<slug>/dossier.md for each, then sends me the
   shortlist with a winnability pitch per business.
3. STOP and wait for my approval of the 3 finalists. Do NOT spawn the planner or
   builders until I confirm or swap them.
4. After I approve, spawn the whole next wave AT ONCE: 'planner', all three
   'builder' teammates (one per prospect, each owning ONLY its own
   prospects/<slug>/mockup/ and prospects/<slug>/screenshots/ folders),
   'copywriter', and 'critic'.
   - The planner batches its shared research once per trade, then finishes and
     hands off ONE complete plan at a time (prospect #1 first) so builders start
     staggered rather than all waiting for all three plans.
   - Builders do their pre-work while waiting for their plan (read dossier,
     download the real logo, scaffold folders, start their static server) and
     build the moment their plan arrives. They do NOT guess at the design.
   - The copywriter starts from the dossiers immediately.
   - The critic audits the outreach drafts FIRST, then each mockup the moment
     its builder submits — never batching all three together.
5. Builders and copywriter loop directly with the critic until every package
   passes the $10K Checklist (8/8), the web-design-ultra rubric (no dimension
   below 7, boldness >= 8), and the package checklist. Before the FINAL sign-off
   the critic runs the run-level distinctiveness check across all three mockups.
   All gates stay fully enforced.
6. When all three packages are signed off, give me a summary. Do not contact any
   business — everything is a draft on disk for me to review.
```

If a teammate can't be spawned on Fable by the `planner` frontmatter alone, spawn it
explicitly with the model id `claude-fable-5`.

## After the run

Follow **`PLAYBOOK.md`**. It has two scripts: **Script 1** is a plain-English
walkthrough of the whole run (summon the team → send → follow-up), and **Script 2**
is a detailed review decision tree where every decision point branches to a labeled
next step with a paste-able prompt — so there's a defined path for every outcome
(bad client, wrong-vibe mockup, off-voice email, no reply, all three flopped, etc.).
