# github/ — moving files between Harry's Mac and Corey's

Harry and Corey each keep a full clone of `hfoodim16/essex-web-crew` at `~/Projects/essex-web-crew`.
GitHub is the middle. This folder holds the two skills that move work across it, so neither of us
has to remember git commands.

| Skill | Say | What it does |
|---|---|---|
| `github-push` | "push this", "send Corey my changes" | Pulls their work first, checks the diff for secrets and broken image links, commits, pushes. |
| `github-pull` | "pull", "get Harry's latest" | Shows what's incoming, protects anything uncommitted, pulls, re-installs skills if they changed. |

The loop: **one person pushes, tells the other, the other pulls.** Always pull before you start
working — editing a stale copy is what makes conflicts.

```
github/
  README.md              this file
  scripts/preflight.sh   shared checks — finds the repo, proves you're logged in, reports the gap
  skills/
    github-push/SKILL.md
    github-pull/SKILL.md
```

`scripts/preflight.sh` is deliberately the only copy. Both skills call it from the repo rather than
carrying a duplicate, so there is one place to fix when something about the setup changes.

## First time on a new Mac

1. Clone to the exact path (the docs reference it by name):

   ```bash
   git clone https://github.com/hfoodim16/essex-web-crew.git ~/Projects/essex-web-crew
   ```

2. Log in to GitHub for pushing. Cloning a private repo may already have done this, but pushing
   needs it properly wired into git:

   ```bash
   gh auth login && gh auth setup-git
   ```

   No `gh`? `brew install gh` first.

3. Install the skills (this is the same `install.sh` that installs the rest of the crew):

   ```bash
   cd ~/Projects/essex-web-crew && ./install.sh
   ```

4. Check it:

   ```bash
   bash ~/Projects/essex-web-crew/github/scripts/preflight.sh
   ```

   `RESULT: PASS` means you're set.

## Troubleshooting

| What you see | What it means | Fix |
|---|---|---|
| `FIX: GitHub rejected the connection` | Not logged in on this Mac | `gh auth login && gh auth setup-git` |
| Still rejected after logging in | Not a collaborator yet | Harry adds you at Settings → Collaborators on the repo |
| `FIX: Can't find the crew repo` | Clone is somewhere else | `export CREW_ROOT=/path/to/your/clone`, or re-clone to `~/Projects/essex-web-crew` |
| `upstream : origin/main (not tracked…)` | Branch isn't following the remote | `git branch -u origin/main` |
| Push rejected, non-fast-forward | They pushed while you were working | Run `/github-pull`, then push again. Never `--force`. |
| Skills behave like the old version | The installed copies are stale | `./install.sh --force`, then restart Claude Code |
| Conflict in `design-memory.md` | You both appended a row | Keep both. It's an append-only log, never a real conflict. |
| Conflict in `prospects/<slug>/**` | You both edited one prospect | Pick whichever is current — don't hand-merge two mockups. |

## What does not get synced

Some things are gitignored on purpose and stay on the machine that made them:

- `~/.claude/skills/ai-multimodal/.env` — holds a live billing key, lives outside the repo entirely
- `prospects/**/*.zip` — delivery zips, rebuilt on demand by `pipeline/package-site.sh`
- Loose source art (`assets-src/`, stray `.png`/`.jpg` in a prospect folder)
- `.claude/settings.local.json` — per-machine settings

Images a mockup **actually loads** are tracked (`mockup/assets/`, `mockup/work/**`, `screenshots/`).
If you add images anywhere else in a mockup, `github-push` will catch it — that check exists because
a portfolio page once shipped with seven missing images.
