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
Run stages OVERLAPPED per the agent files, never strictly sequentially.
Spawn scout and analyst TOGETHER (scout streams candidate batches; analyst
scores incrementally and researches the top 3 in parallel), then STOP and
show me the top-3 shortlist for approval. After I approve, spawn the whole
next wave AT ONCE — planner, all three builders, copywriter, critic — and
loop builders/copywriter with the critic until every package passes both
scoreboards. Don't contact any business.
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
Each `prospects/<slug>/` has `dossier.md`, `website-plan.md`, `mockup/` (incl. `assets/`), `screenshots/`, `outreach-email.md` OR `outreach-call.md`, and `audit.md`.

**9. Shut down** when done: `Ask all teammates to shut down.` — or just `/exit`.

**10. Delivery to Corey — automatic.** When the critic signs a prospect off, the lead
packages the site and drafts the Gmail to Corey (cbrapkin@gmail.com) for you. Check your
Gmail drafts, glance at it, hit send. Nothing is ever sent without you.

Zips over 200 KB can't be attached automatically — those drafts open with an
`ATTACH BEFORE SENDING:` line naming the file, so drag it in before you send.

To package or re-deliver a site by hand:
```bash
pipeline/package-site.sh <prospect-slug>
```
Writes `prospects/<slug>/<slug>-site.zip` from the best available version (`deploy-ready/`,
else `deliverable/`, else `mockup/`), with all assets included and dev scratch files stripped.
Or just say `deliver <slug>` and the lead does both steps. See `COREY-DEPLOY.md` for Corey's side.

Always the zip, never a bare `index.html`: re-downloading an emailed HTML file makes the browser
rename it (`index-4.html`), and hosts only serve an exactly-named `index.html` as the homepage.

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
- **Token-heavy:** 8 teammates (scout, analyst, planner, 3× builder, copywriter, critic) + the lead + subagents. Keep an eye on the first few minutes.
- **Nothing is sent to any business** — everything is a draft on disk for you to review.
- After review: generate the real images from the `AI-IMAGE:` prompts, then send outreach yourself.
