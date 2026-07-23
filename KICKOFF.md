# Kickoff — Running the Essex Web Crew

## Before you start

1. Agent teams are **experimental** and **token-heavy** (each teammate is a full Claude
   instance, ~7× a solo session). A run spins up its teammates plus subagents.
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
businesses — any industry with a naturally static site, leading with trades
(per the qualification rules in CLAUDE.md) and write them to
pipeline/candidates.md with evidence and sources. Use Sonnet. Free tools only —
no Firecrawl/Perplexity. When scout is done, review pipeline/candidates.md with
me. Do not proceed past the scout.
```

Check: `pipeline/candidates.md` has 5 real, verified, qualifying businesses with
evidence and source links, and the agent panel showed the scout working. If the output
is weak, refine `.claude/agents/scout.md` before a real Prospecting run.

---

## Team 1 — Prospecting run (find me clients)

**Who runs:** `scout` + `analyst` only. Nothing is built. The run ends when you have a
shortlist of 3 real prospects with their contact info.

Paste this to the lead:

```
Read CLAUDE.md, .claude/agents/scout.md and .claude/agents/analyst.md. Run the
Essex Web Crew PROSPECTING pipeline. Lineup: scout=Sonnet, analyst=Opus — each
teammate uses the model in its own frontmatter. Free tools only — no
Firecrawl/Perplexity, no paid image generation (nothing is built in this run).
Teammates invoke their own skills via the Skill tool.

This is the Prospecting team ONLY. Do NOT spawn a planner, builder, or critic —
there is nothing to build yet. I contact the prospects myself afterwards.

Run it overlapped, not strictly sequentially, and never weaken a quality gate to
save time:

1. Spawn 'scout' and 'analyst' TOGETHER. The scout streams verified candidates
   to pipeline/candidates.md in batches of 5-6 and messages the analyst as each
   batch lands; the analyst scores incrementally instead of waiting for the full
   list. Scout floor: 10 qualifying candidates, stop around 12.
2. The analyst researches the top 3 finalists IN PARALLEL (one research subagent
   each, verbatim quotes + source URLs, and it verifies the load-bearing facts
   itself), then writes prospects/<slug>/dossier.md for each (plus site-content.md
   for any that already has a website).
3. The analyst delivers the shortlist to me as the run's FINAL output. For each
   of the 3 I need: how to reach them (phone, email if found, owner's name), why
   they're winnable, the angle to lead with, and the recommended scope.
4. Then summarize and stop. No approval pause is needed — nothing runs after the
   shortlist.
```

**Then it's on you (no agents involved):** call or email the prospects yourself. Anyone
who says yes gets **`templates/questionnaire-master.md`** — the standing client
questionnaire, already written and ready to send. Collect their answers, then run Team 2
below.

## Team 2 — Build run (build the site from their answers)

**Who runs:** `planner` + `builder` + `critic` (plus a capture-only `analyst` if this
client has no dossier yet). Use it once a client has answered the questionnaire —
answers from `templates/questionnaire-master.md` or just notes from a phone call both
work. Paste whatever you got; skipped questions are fine.

Paste this to the lead, filling in the two slots:

```
Read CLAUDE.md and all files in .claude/agents/. Run the Essex Web Crew
BUILD pipeline for ONE client. Skip the prospecting team —
we already have this client. Lineup: planner=Fable (claude-fable-5),
builder=Opus, critic=Opus. Free tools only — no Firecrawl/Perplexity; the one
pre-approved paid step is the builder's 2 AI images (~$0.17). Teammates invoke
their own skills via the Skill tool.

CLIENT: <slug or business name>

THEIR ANSWERS TO THE QUESTIONNAIRE:
<paste the client's answers here — verbatim, however they gave them>

Do this:
1. Save their answers verbatim to prospects/<slug>/client-answers.md.
2. If prospects/<slug>/dossier.md does NOT exist (a client I found myself):
   spawn 'analyst' in CAPTURE-ONLY mode first — research just this ONE business
   and write dossier.md + site-content.md + the logo URL + real reviews. No
   scouting, no scoring, no shortlist. The analyst reads
   client-answers.md FIRST and treats it as controlling: its research
   SUPPLEMENTS the client's answers and never corrects them. Any difference
   between an answer and their old site/a directory goes in a "Confirm with
   client (optional)" note for me — never a [verify] blocker, and never
   resolved in the old site's favor.
3. Spawn 'planner': plan FROM the client's answers. Their answers are the
   TOP authority — above the dossier, above the old site, above design instinct.
   The plan must include a "Client answers → decisions" section mapping every
   answer to what the plan does about it, and flag any answer that is unclear or
   conflicts with another so I can ask them.
4. Spawn ONE 'builder' for this prospect. It implements the plan and treats the
   client's answers as binding.
5. Spawn 'critic': enforce client-answer fidelity (an ignored answer is a fail),
   content parity, the $10K Checklist (8/8), the web-design-ultra rubric (no
   dimension below 7, boldness >= 8), the imagery two-way realism test,
   real-reviews-only, the interactive click-test, the distinctiveness check
   against our last 3 design-memory.md rows, and the package checklist. Loop
   until it passes.
6. When signed off, summarize what was built and call out anything I should
   confirm with the client. Expect to iterate: I'll bring their feedback back.
```

If a teammate can't be spawned on Fable by the `planner` frontmatter alone, spawn it
explicitly with the model id `claude-fable-5`.

## After the run

Follow **`PLAYBOOK.md`**. It has two scripts: **Script 1** is a plain-English
walkthrough of the whole run (summon the team → send → follow-up), and **Script 2**
is a detailed review decision tree where every decision point branches to a labeled
next step with a paste-able prompt — so there's a defined path for every outcome
(bad client, wrong-vibe mockup, off-voice email, no reply, all three flopped, etc.).
