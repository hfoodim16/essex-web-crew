# How to Run — Simple Steps

**1. Open Terminal** (Cmd+Space → "Terminal" → Enter).

**2. Start it:**
```bash
~/Projects/essex-web-crew/run.sh
```
(If that errors: `cd ~/Projects/essex-web-crew && CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 claude`)

**3. Set fallback model:** type `/config` → Default teammate model → **Sonnet** → Escape.
(Each agent overrides with its own model; this is just a backup.)

**4. Paste this as your message:**
```
Read CLAUDE.md and all files in .claude/agents/. Run the full Essex Web Crew
pipeline per KICKOFF.md. Each teammate uses the model and skills in its own
agent definition. Free tools only — no Firecrawl/Perplexity; the one
pre-approved paid step is each builder's 2 AI images (~$0.17/prospect).
Spawn scout, then analyst, then STOP and
show me the top-3 shortlist for approval before spawning the planner and
builders. After I approve, run planner → builders + copywriter → critic until
every package passes. Don't contact any business.
```

**5. Watch the agent panel** below your prompt (↑/↓ select, Enter to read/message a teammate).
Scout + Analyst run first (a few minutes).

**6. Approve the shortlist** when it shows you 3 businesses:
```
Approved — build all three.
```
(or: `Swap #2 for [name], then build all three.`)

**7. Let it finish.** Planner → Builders + Copywriter → Critic. If it stops early:
```
Continue — not all tasks are complete.
```

**8. Review results:**
```bash
open ~/Projects/essex-web-crew/prospects/
```
Each `prospects/<slug>/` has `dossier.md`, `mockup/index.html`, `outreach-email.md`, `audit.md`.

**9. Shut down** when done: `Ask all teammates to shut down.` — or just `/exit`.

---

## If something goes wrong

| Problem | Fix |
|---|---|
| No agent panel appears | Teams flag didn't load — quit, relaunch with the manual command in step 2. |
| A teammate is on the wrong model | Tell the lead to respawn it (planner needs `claude-fable-5`). |
| A teammate skips its skill | Message it: `use the <skill> skill`. |
| Lead stops too early | `Continue — not all tasks are complete.` |
| Too many permission prompts | Approve them, or pre-approve common ops before running. |

## Reminders

- **Do NOT run this in the desktop/web app** — the teammate panel only works in a real terminal.
- **Token-heavy:** 6 Claude instances + subagents. Keep an eye on the first few minutes.
- **Nothing is sent to any business** — everything is a draft on disk for you to review.
- After review: generate the real images from the `AI-IMAGE:` prompts, then send outreach yourself.
