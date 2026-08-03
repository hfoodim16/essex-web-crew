# Setup — running the Essex Web Crew on your own Mac

This gets the whole crew running on your machine. About 10 minutes, most of it waiting
on one install.

## Before you start

- **Claude Code** installed and logged in. The crew pins heavy models (the Planner runs
  Fable, the Analyst/Builder/Critic run Opus), so you need a plan that can run them —
  **Max is what this was built and tested on**. On a lighter plan the agents will still
  launch but the quality gates get much weaker.
- **Terminal** (Terminal.app or iTerm). The agent-team panel doesn't render in the
  Claude Code desktop or web app — this is terminal-only.
- **git** and **Python 3.10+**. If `python3 --version` shows 3.9 (the macOS default),
  run `brew install python@3.12` — `install.sh` will find it automatically.

## 1. Clone it

Clone to this exact path — the docs and agent files reference `~/Projects/essex-web-crew`
by name, so a different location means fixing paths later.

```bash
git clone https://github.com/hfoodim16/essex-web-crew.git ~/Projects/essex-web-crew
```

## 1b. Log in to GitHub

Cloning a private repo needs a login; **pushing** needs that login wired into git itself.
Do it now so sending work back later just works:

```bash
gh auth login && gh auth setup-git
```

Pick **GitHub.com → HTTPS → authenticate in browser**. No `gh` on the machine?
`brew install gh` first.

## 2. Install the skills

The crew leans on ~15 Claude Code skills that live in `~/.claude/skills/`. They're
bundled in this repo under `skills/`. This copies them into place and sets up the
image-generation environment:

```bash
cd ~/Projects/essex-web-crew && ./install.sh
```

It **skips any skill you already have** so it won't stomp your own setup. If you want
this repo's versions to win, run `./install.sh --force` (your `.env` files are preserved
either way).

The big one is `web-design-ultra` — that's the design pipeline the Builder and Critic
work from. `ui-ux-pro-max` ships a `search.py` the Planner calls directly.

## 3. Add a Gemini API key

Each site ships with 2 real AI-generated images (the hero + one priority slot),
generated through Google Gemini.
That's the one thing that costs money, and it's billed to whoever's key is in the file.

1. Get a key at https://aistudio.google.com/apikey
2. Open `~/.claude/skills/ai-multimodal/.env`
3. Set `GEMINI_API_KEY=<your key>`

Check it works:

```bash
~/.claude/skills/ai-multimodal/.venv/bin/python -c "import google.genai; print('ok')"
```

Without a key everything else still runs — you'll just get placeholder images instead of
generated ones.

## 4. Run it

```bash
cd ~/Projects/essex-web-crew && ./run.sh
```

That sets `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` and launches Claude Code. Then:

- Set your fallback teammate model to Sonnet (`/config` → Default teammate model). Each
  agent overrides this with its own; it's just a backup.
- Paste a prompt from **`KICKOFF.md`**. Do the dry run first — it's a cheap scout-only
  pass (5 candidates) that proves the scout works before you spend a real Prospecting run.
- `HOW-TO-RUN.md` walks through what happens at each stage. `PLAYBOOK.md` and
  `FULL-PROCESS.md` go deeper.

The crew **never contacts anyone**. Everything lands on disk in `prospects/<name>/` for
you to review. A prospecting run ends at a shortlist with contact info — you reach out to
those businesses yourself, in your own words, and send anyone who says yes
`templates/Website-Questionnaire.docx`. Their answers are what you paste into a build run.

## 5. Optional: rtk

`rtk` is a CLI wrapper that compresses command output to save tokens. `.claude/settings.json`
pre-approves a few `rtk` commands, harmlessly, whether or not you have it. Install with
`brew install rtk` if you want it.

## Make it yours

The playbook in `CLAUDE.md` is written around Harry's market. Four spots you'll probably
want to change — easiest way is to open Claude Code in the project and ask it to localize
`CLAUDE.md` for your territory rather than editing by hand:

| Where | What it says now |
|---|---|
| `CLAUDE.md` line ~11, ~22 | Territory is **Essex County, NJ** (Newark, Montclair, Bloomfield…). Swap in yours. |
| `CLAUDE.md` line ~40 | Portfolio anchor is **Cecere Brothers Landscaping**, Harry's client. Replace with a build of your own, or drop the reference. |
| `CLAUDE.md` "Delivery to Corey" (~line 122) | Tells the crew to package a zip and email it to you for Netlify deploy. On your machine **you're** the deployer — follow `COREY-DEPLOY.md` directly and delete the email step. |
| `CLAUDE.md` "DaSilva workflow" (~line 156) | Names `prospects/paul-da-silva-law/` as the reference build. That folder ships in this repo, so it opens on your machine too — nothing to change. |

`design-memory.md` is shipped on purpose: it's a running ban-list of design choices already
used, so your sites don't come out looking like Harry's. Keep appending to it.

## Trading work back and forth

The repo is how we swap files. Two skills do it, from either Mac — just say what you want:

| Say | Skill | When |
|---|---|---|
| "pull" / "get Harry's latest" | `github-pull` | **Start of every session**, before you build anything |
| "push this" / "send Harry my changes" | `github-push` | When a run finishes, or before you stop for the day |

Pull first, always — editing a stale copy is what creates conflicts. When a pull brings
new or changed skills, re-run `./install.sh --force` and restart Claude Code so the copies
in `~/.claude/skills/` update.

Full details, including a troubleshooting table: **[github/README.md](github/README.md)**.

## What is and isn't committed

`prospects/` **is** tracked — that's the whole point, it's how a build gets from one Mac to
the other. What stays local:

- **any `.env`** — holds a live billing key, never commit one
- `prospects/**/*.zip` — delivery zips, rebuilt on demand by `pipeline/package-site.sh`
- loose source art in a prospect folder (`assets-src/`, stray `.png`/`.jpg`)
- `.claude/settings.local.json` — per-machine settings

Images a mockup actually loads **are** tracked. If you put images somewhere new inside a
mockup, `github-push` checks for that before pushing — a page once shipped with seven
missing images because `.gitignore` swallowed them.
