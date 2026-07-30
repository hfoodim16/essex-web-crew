---
name: github-pull
description: |
  Use when getting the other person's latest crew work down onto this Mac.
  Triggers: "pull", "pull from GitHub", "get Corey's changes", "get Harry's
  latest", "grab the newest files", "sync down", "did anything change?", or
  being told the other person just pushed. Also use at the start of a work
  session, before building anything, so you don't edit a stale copy.
  The sending side runs github-push.
---

# github-pull

Brings down everything the other person pushed to `hfoodim16/essex-web-crew`. Harry and Corey both
run this from their own clone.

**Run this before starting work, not after.** Editing a stale copy is what creates the conflicts
this repo is bad at — two versions of the same mockup can't be merged, only chosen between.

## 1. Preflight

```bash
bash github/scripts/preflight.sh
```

Works from any directory. `RESULT: FAIL` → do what the `FIX:` line says and stop.

If the shell says **`No such file or directory`**, this clone predates the sync tooling. Bootstrap it
once by hand — this is also the whole job the first time, since the pull is what delivers the tooling:

```bash
git -C ~/Projects/essex-web-crew pull --rebase && ~/Projects/essex-web-crew/install.sh --force
```

Then restart Claude Code and the skills are live.

Read the report:

- `behind: 0` and `uncommitted: 0` → already up to date. Say so and stop; there is nothing to do.
- `behind: 0` but `uncommitted` > 0 → nothing incoming, but this Mac has unsent work. Point the user
  at `/github-push` instead.
- `behind` > 0 → there's work to collect, continue.

## 2. Protect uncommitted work

If `uncommitted` is 0, skip to step 3.

Otherwise this Mac has changes that a pull could collide with. Show the user
`git status --short` and ask which they want:

| Choice | When | What you run |
|---|---|---|
| **Push mine first** (usually right) | The local changes are finished work | Hand off to the `github-push` skill, which pulls and pushes in one pass. Done — don't continue here. |
| **Stash, pull, restore** | The local changes are half-finished | `git stash push -u -m "pre-pull"` → continue to step 3 → `git stash pop` at the end |
| **Throw mine away** | The local changes are junk | Only on an explicit yes from the user. `git checkout -- .` — this is not recoverable. |

## 3. Show what's coming before taking it

```bash
git fetch origin
git log --oneline HEAD..@{u}
git diff --stat HEAD..@{u}
```

Summarize for the user in plain terms — which prospects changed, whether skills or docs moved — so
they know what landed and why their files look different afterward.

## 4. Pull

```bash
git pull --rebase
```

If it conflicts, stop and resolve with the user:

| File | Resolution |
|---|---|
| `design-memory.md` | **Keep both sides' rows.** Append-only ban-list, never a genuine conflict. |
| `prospects/<slug>/**` | Ask whose version is current. Do not hand-merge two mockups. |

`git add <files>` then `git rebase --continue`. To back out: `git rebase --abort`, then explain why.

If you stashed in step 2: `git stash pop` now, and resolve any conflicts the same way.

## 5. Re-install skills if they changed

The crew's skills are **copied** into `~/.claude/skills/` — a pull updates the repo but not the
installed copies. If preflight reported skills drift, or the pull touched `skills/` or `github/`:

```bash
./install.sh --force
```

`--force` is required; a plain run skips anything already installed. `.env` files are preserved. Then
tell the user to restart Claude Code so the new versions load.

## 6. Verify, then report

```bash
git rev-list --left-right --count HEAD...origin/main
```

`behind` (the second number) must be `0`. Then report:

- how many commits came in and what they changed
- whether `./install.sh --force` was needed and whether it ran
- anything still uncommitted on this Mac that should go up with `/github-push`
