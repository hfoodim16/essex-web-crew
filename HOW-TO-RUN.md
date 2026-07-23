# How to Run — Simple Steps

**1. Open Terminal** (Cmd+Space → "Terminal" → Enter).

**2. Start it:**
```bash
~/Projects/essex-web-crew/run.sh
```
(If that errors: `cd ~/Projects/essex-web-crew && CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 claude`)

**3. Set fallback model:** type `/config` → Default teammate model → **Sonnet** → Escape.
(Each agent overrides with its own model; this is just a backup.)

There are **two separate runs**, and they never run together: a **Prospecting run** that
finds you clients, and a **Build run** that builds one client's site from their answers.
In between, you do the talking. Both prompts also live in `KICKOFF.md`.

**4. Run 1 — Prospecting. Paste this as your message:**
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

**5. Watch the agent panel** below your prompt (↑/↓ select, Enter to read/message a teammate).
Scout + Analyst run together (a few minutes).

**6. The run ends at the shortlist — now it's on you.** Nothing was built, and there's no
approval pause. Call or email the 3 prospects yourself, in your own words. Anyone who says
yes gets `templates/questionnaire-master.md` as-is — it's already written, no run needed.
Collect their answers, then start a Build run.

**7. Run 2 — Build. Paste this, filling in the two slots:**
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
(If the planner won't spawn on Fable from its frontmatter, tell the lead to spawn it
explicitly with the model id `claude-fable-5`.)

**8. Let it finish.** Planner → Builder → Critic loop. If it stops early:
```
Continue — not all tasks are complete.
```

**9. Review results:**
```bash
open ~/Projects/essex-web-crew/prospects/
```
A prospected business has `dossier.md` and `site-content.md`. Once it's been through a
build run it also has `client-answers.md`, `website-plan.md`, `mockup/` (incl. `assets/`),
`screenshots/`, and `audit.md`.

**10. Shut down** when done: `Ask all teammates to shut down.` — or just `/exit`.

**11. Delivery to Corey — automatic.** When the critic signs a prospect off, the lead
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
- **Token-heavy:** a prospecting run is 2 teammates (scout, analyst) + the lead; a build run
  is 3 (planner, builder, critic) + the lead — plus subagents in both. Keep an eye on the
  first few minutes.
- **Nothing is sent to any business** — everything lands on disk for you to review.
- All client contact is you, personally: reach out to the shortlist in your own words, and
  send `templates/questionnaire-master.md` to anyone who says yes.
- After review: generate the real images from the `AI-IMAGE:` prompts before the site goes
  to the client.
