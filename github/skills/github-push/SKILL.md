---
name: github-push
description: |
  Use when sending your local crew work up to GitHub so the other person can
  get it. Triggers: "push this", "push to GitHub", "send Corey my changes",
  "send Harry the latest", "save this to the repo", "sync my work up", or
  finishing a build/prospecting run whose output the other machine needs.
  Also use before stopping for the day so nothing lives only on one Mac.
  The receiving side runs github-pull.
---

# github-push

Sends everything on this Mac up to `hfoodim16/essex-web-crew` so the other person can pull it.
Harry and Corey both run this from their own clone.

**Commit first, then pull, then push.** The order matters: `git pull --rebase` refuses to run with
uncommitted changes, so committing has to come first. Pulling before the push (rather than just
letting the push fail) is what keeps the history a straight line instead of a knot of merge commits.

## 1. Preflight

```bash
bash github/scripts/preflight.sh
```

Works from any directory — it finds the repo itself. If it prints `RESULT: FAIL`, do exactly what
the `FIX:` line says and stop. Do not work around it. The two real failures are *not logged in on
this Mac* (`gh auth login`) and *repo not where expected* (set `CREW_ROOT`).

If the shell says **`No such file or directory`**, this clone predates the sync tooling. Bootstrap it
once by hand, then start over:

```bash
git -C ~/Projects/essex-web-crew pull --rebase && ~/Projects/essex-web-crew/install.sh --force
```

Read the counts. `uncommitted: 0` **and** `ahead: 0` means there is nothing to send — say so and
stop. `behind` > 0 means the other person has pushed work you don't have; step 4 folds it in.

## 2. Look at what you're about to send

```bash
git status --short
```

Three checks before staging anything. They take a few seconds and each one has already bitten this
repo:

1. **No secrets.** Nothing named `.env`, no API key in a diff. `ai-multimodal/.env` holds a live
   billing key and lives outside the repo — if it somehow shows up here, stop.
2. **No images the site needs are being ignored.** `.gitignore` blocks `prospects/**/*.{png,jpg,jpeg,webp}`
   with narrow exceptions for `screenshots/`, `mockup/assets/`, and `mockup/work/**`. A mockup that
   loads images from anywhere else will push as a **broken page**. For any new or changed mockup,
   check the referenced files are actually tracked:

   ```bash
   git check-ignore -v prospects/<slug>/mockup/**/*.{png,jpg,jpeg,webp}
   ```

   Anything it reports is invisible to the other person. Add a `!` exception to `.gitignore` first,
   then continue.
3. **Deletions are intentional.** If `git status` shows `D` on files you didn't mean to remove,
   sort that out before committing.

## 3. Commit

```bash
git add -A
```

Write a real commit message describing what changed — a scan of `git log --oneline -10` shows the
house style: a plain summary line, then a short paragraph on what and why. "Update files" is not a
commit message; the other person reads these to know what they're getting.

End every message with:

```
Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

## 4. Take their work first

Only if preflight said `behind` > 0 — otherwise skip straight to step 5.

```bash
git pull --rebase
```

This has to happen **after** the commit: with a dirty working tree it aborts with
*"cannot pull with rebase: You have unstaged changes."*

**If it conflicts, stop and resolve it with the user. Never `--force` past a conflict** — on this
repo that silently deletes the other person's work.

Two conflicts are common and both have a known answer:

| File | What happened | Resolution |
|---|---|---|
| `design-memory.md` | Both of you appended a row to the ban-list | **Keep both rows.** Nothing here is ever a real conflict — it's an append-only log. |
| `prospects/<slug>/**` | You both edited the same prospect | Ask the user whose is newer. Do not merge two mockups by hand. |

After resolving: `git add <files>` then `git rebase --continue`. To bail out entirely:
`git rebase --abort`, then tell the user why.

## 5. Push

```bash
git push origin HEAD:main
```

`HEAD:main` is deliberate — it works whether the local branch is `master` or `main`, and the remote
only ever has `main`.

If it's rejected as non-fast-forward, someone pushed between your step 4 and here. Go back to step 4
and pull again. **Never `--force`** unless the user explicitly asks and understands it discards the
other person's commits.

## 6. Verify, then report

```bash
git fetch origin && git rev-list --left-right --count HEAD...origin/main
```

Must print `0	0`. Anything else means the push didn't fully land — say so plainly rather than
reporting success.

Then tell the user, in a few lines:

- what was pushed (the commit summary, file count)
- anything you deliberately left out and why (ignored source art, zips)
- **"Tell <the other person> to run `/github-pull`"** — and if the push touched `skills/` or
  `github/`, add that they'll need `./install.sh --force` afterward
