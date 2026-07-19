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
pipeline. Use Sonnet for all teammates. Free tools only.

1. Spawn 'scout' (scout agent type): find 10–15 qualifying Essex County, NJ
   businesses → pipeline/candidates.md.
2. Spawn 'analyst' (analyst agent type): score them against pipeline/rubric.md,
   research the top 3, write prospects/<slug>/dossier.md for each, then send me
   the shortlist with a winnability pitch per business.
3. STOP and wait for my approval of the 3 finalists. Do NOT spawn builders until
   I confirm or swap them.
4. After I approve: spawn three 'builder' teammates (builder agent type), one per
   approved prospect, each owning only its own prospects/<slug>/mockup/ folder.
   Spawn 'copywriter' (copywriter agent type) for the outreach emails, and
   'critic' (critic agent type) as the quality gate. Builders and copywriter loop
   directly with the critic until every package passes the $10K Checklist and the
   package checklist.
5. When all three packages are signed off, give me a summary. Do not contact any
   business — everything is a draft on disk for me to review.
```

## After the run

For each `prospects/<slug>/`: review the dossier, open `mockup/index.html` in the
browser, read the email, then generate the real images from the `AI-IMAGE:` prompts and
send the outreach yourself.
