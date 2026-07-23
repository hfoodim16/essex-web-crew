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

## Run A — Prospect & Ask (find clients + get questionnaires ready)

This run does NOT build any mockups. We ask first, then build from the answers.

Paste this to the lead:

```
Read CLAUDE.md and all files in .claude/agents/. Run the Essex Web Crew
"Run A — Prospect & Ask" pipeline. Each teammate uses the model in its agent
definition's frontmatter — do NOT force a single model. The lineup for this run
is: scout=Sonnet, analyst=Opus, planner=Fable (claude-fable-5),
copywriter=Sonnet, critic=Opus. Free tools only — no Firecrawl/Perplexity, and
no paid image generation in this run (nothing is built). Teammates must invoke
their skills themselves via the Skill tool.

We use the ASK-FIRST model: we do NOT build a speculative site and pitch it. This
run ends with a tailored client questionnaire + first-contact outreach per
prospect, ready for me to send. Do NOT spawn any builders.

Run stages OVERLAPPED, not strictly sequentially. Never weaken a quality gate to
save time.

1. Spawn 'scout' and 'analyst' TOGETHER. The scout streams candidates to
   pipeline/candidates.md in batches of 5–6 and messages the analyst as each
   batch lands; the analyst scores incrementally.
2. The analyst researches the top 3 finalists IN PARALLEL (one research subagent
   each), writes prospects/<slug>/dossier.md and site-content.md for each, then
   sends me the shortlist with a winnability pitch per business.
3. STOP and wait for my approval of the 3 finalists.
4. After I approve, spawn 'planner', 'copywriter', and 'critic'.
   - The planner writes prospects/<slug>/questionnaire.md for each approved
     prospect: a client-facing document I can send as-is, with exactly 10
     questions in plain English, tailored to THAT business (real services, town,
     their current site). No website plans and no design work in this run.
   - The copywriter writes the first-contact outreach that DELIVERS the
     questionnaire — outreach-email.md if the dossier has a real email (10
     questions pasted below the sign-off), else outreach-call.md (the questions
     as a spoken call guide + an offer to text/email them). It must NOT claim a
     mockup exists.
   - The critic reviews both against templates/package-checklist.md (Run A
     section) and loops until they pass.
5. When all three are signed off, give me a summary: per prospect, the contact
   channel, the questionnaire path, and the outreach path. Do not contact any
   business — everything is a draft for me to send.
```

Then: send the questionnaires, collect the client's answers, and start **Run B** below.

## Run B — Build & Perfect (skips scout & analyst)

Use this once a client has answered the questions. It goes straight to the planner.

Paste this to the lead, filling in the two slots:

```
Read CLAUDE.md and all files in .claude/agents/. Run the Essex Web Crew
"Run B — Build & Perfect" pipeline for ONE client. Skip the scout and analyst —
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
   scouting, no scoring, no shortlist, no approval pause.
3. Spawn 'planner' (Run B): plan FROM the client's answers. Their answers are the
   TOP authority — above the dossier, above the old site, above design instinct.
   The plan must include a "Client answers → decisions" section mapping every
   answer to what the plan does about it, and flag any answer that is unclear or
   conflicts with another so I can ask them.
4. Spawn ONE 'builder' for this prospect. It implements the plan and treats the
   client's answers as binding.
5. Spawn 'critic': enforce client-answer fidelity (an ignored answer is a fail),
   content parity, the $10K Checklist (8/8), the web-design-ultra rubric (no
   dimension below 7, boldness >= 8), the interactive click-test, and the
   package checklist. Loop until it passes.
6. No copywriter — this client is already engaged.
7. When signed off, summarize what was built and call out anything I should
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
