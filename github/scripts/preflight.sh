#!/usr/bin/env bash
# Mechanical checks both sync skills run before touching git.
# Locates the crew repo, proves GitHub is reachable, and reports the exact
# state of local vs remote so the skill knows what it is about to do.
#
# Usage: bash github/scripts/preflight.sh
# Exit:  0 = safe to sync, 1 = something needs fixing (a FIX line says what)
#
# Works from any directory on any machine — it finds the repo itself.
set -uo pipefail

fail() { echo "RESULT: FAIL"; echo "FIX: $1"; exit 1; }

# ---------- 1. locate the repo ----------
# In order: an explicit CREW_ROOT, the repo the current directory is inside,
# then the conventional clone path both machines use.
ROOT=""
if [ -n "${CREW_ROOT:-}" ] && [ -d "$CREW_ROOT/.git" ]; then
  ROOT="$CREW_ROOT"
else
  top="$(git rev-parse --show-toplevel 2>/dev/null || true)"
  if [ -n "$top" ] && [ -f "$top/CLAUDE.md" ] && [ -d "$top/prospects" ]; then
    ROOT="$top"
  elif [ -d "$HOME/Projects/essex-web-crew/.git" ]; then
    ROOT="$HOME/Projects/essex-web-crew"
  fi
fi
[ -n "$ROOT" ] || fail "Can't find the crew repo. Clone it with:
       git clone https://github.com/hfoodim16/essex-web-crew.git ~/Projects/essex-web-crew
     Or set CREW_ROOT=/path/to/your/clone and run this again."

cd "$ROOT"

echo "=== Essex Web Crew sync preflight ==="
echo "repo         : $ROOT"

# ---------- 2. the remote is the crew repo ----------
REMOTE="$(git remote get-url origin 2>/dev/null || true)"
[ -n "$REMOTE" ] || fail "This clone has no 'origin' remote. Add it:
       git -C $ROOT remote add origin https://github.com/hfoodim16/essex-web-crew.git"
case "$REMOTE" in
  *essex-web-crew*) ;;
  *) fail "origin points at '$REMOTE', which is not the crew repo. Expected …/essex-web-crew.git" ;;
esac
echo "remote       : $REMOTE"

# ---------- 3. GitHub is reachable and we're authenticated ----------
if ! git ls-remote --heads origin >/dev/null 2>&1; then
  fail "GitHub rejected the connection — you're probably not logged in on this Mac. Fix:
       gh auth login          (choose GitHub.com > HTTPS > authenticate in browser)
       gh auth setup-git      (lets plain git commands use that login)
     No gh? Install it with: brew install gh
     Then run this again. If it still fails, ask Harry to confirm you're a
     collaborator on hfoodim16/essex-web-crew — it's a private repo."
fi
echo "auth         : OK"

# Refresh our view of the remote so the counts below are true.
git fetch --quiet origin 2>/dev/null || true

# ---------- 4. branch and upstream ----------
# Harry's clone is on 'master', a fresh clone lands on 'main'. Never hardcode.
BRANCH="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo '?')"
UPSTREAM="$(git rev-parse --abbrev-ref --symbolic-full-name '@{u}' 2>/dev/null || true)"
if [ -z "$UPSTREAM" ]; then
  UPSTREAM="origin/main"
  echo "branch       : $BRANCH"
  echo "upstream     : $UPSTREAM  (not tracked — set it with: git branch -u origin/main)"
else
  echo "branch       : $BRANCH"
  echo "upstream     : $UPSTREAM"
fi

git rev-parse --verify --quiet "$UPSTREAM" >/dev/null \
  || fail "Can't resolve '$UPSTREAM'. Run: git fetch origin"

# A clone made before a force-push shares no ancestor with the remote. git can't
# merge that — it errors with "refusing to merge unrelated histories" — so catch it
# here with the actual fix instead of letting the pull fail cryptically.
if ! git merge-base HEAD "$UPSTREAM" >/dev/null 2>&1; then
  DIRTY_NOW="$(git status --porcelain | wc -l | tr -d ' ')"
  fail "This clone's history has nothing in common with GitHub's — it was made before
     the history was replaced. A plain 'git pull' refuses outright, and a rebase would
     try to replay the whole stale snapshot as a patch. Reset the clone instead.

     This clone currently has $DIRTY_NOW uncommitted file(s).
     ** The reset below DELETES them permanently. ** Copy anything you want to keep
     out of the folder first, then:

       git -C $ROOT fetch origin
       git -C $ROOT reset --hard $UPSTREAM
       $ROOT/install.sh --force

     Then restart Claude Code and run this again."
fi

# ---------- 5. what's out of sync ----------
COUNTS="$(git rev-list --left-right --count "HEAD...$UPSTREAM" 2>/dev/null || echo '0	0')"
AHEAD="$(echo "$COUNTS" | cut -f1)"
BEHIND="$(echo "$COUNTS" | cut -f2)"
DIRTY="$(git status --porcelain | wc -l | tr -d ' ')"

echo "ahead        : $AHEAD  (local commit(s) GitHub doesn't have)"
echo "behind       : $BEHIND  (commit(s) on GitHub this clone doesn't have)"
echo "uncommitted  : $DIRTY  file(s) changed in the working tree"

# Do the incoming commits change the skills? If so the local installed copies
# in ~/.claude/skills/ are stale until install.sh runs again.
DRIFT="$(git diff --name-only "HEAD..$UPSTREAM" -- skills github 2>/dev/null | wc -l | tr -d ' ')"
if [ "$DRIFT" -gt 0 ]; then
  echo "skills drift : $DRIFT file(s) — after pulling, run ./install.sh --force"
else
  echo "skills drift : none"
fi

echo "RESULT: PASS"
