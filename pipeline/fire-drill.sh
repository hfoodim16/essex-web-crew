#!/bin/bash
# Fire drill — prove the crew's gates still work, end to end, for $0.
#
# Run this after changing ANY gate, rule, threshold, or agent instruction.
# It checks two things every gate must do:
#   (a) PASS a known-good build   — the gate hasn't become impossible to satisfy
#   (b) FAIL a known-bad build    — the gate is actually still firing
#
# (b) is the one that matters. A gate that silently stopped firing looks exactly
# like a clean codebase, which is how a page with 5 of 7 identical sections once
# passed a green check.
#
# Fixtures live in prospects/_smoke-test/ (synthetic, never ships, costs nothing).
# Usage: pipeline/fire-drill.sh
set -uo pipefail

CREW_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
FIXTURE="$CREW_ROOT/prospects/_smoke-test"
DETECT="$CREW_ROOT/skills/web-design-ultra/scripts/detect.mjs"
PLANLINT="$CREW_ROOT/skills/web-design-ultra/scripts/plan-lint.mjs"
SCRATCH="$(mktemp -d)"
trap 'rm -rf "$SCRATCH"' EXIT

PASS=0
FAIL=0
step() { printf '  %-58s' "$1"; }
ok()   { echo "PASS"; PASS=$((PASS+1)); }
bad()  { echo "FAIL — $1"; FAIL=$((FAIL+1)); }

echo ""
echo "Fire drill — crew gate verification"
echo "───────────────────────────────────────────────────────────────────"

# ── 0. The detector must not be degraded, or everything below is theatre ────
step "detector has its parser dependencies"
DEG="$(node "$DETECT" "$FIXTURE/mockup/index.html" 2>&1 >/dev/null | grep -c "DETECTOR DEGRADED" || true)"
if [ "$DEG" -eq 0 ]; then ok; else
  bad "running DEGRADED — cd skills/web-design-ultra/scripts/detector && npm install"
  echo ""
  echo "Stopping: every check below would be meaningless." >&2
  exit 1
fi

# ── 1. plan-lint PASSES the good plan ───────────────────────────────────────
step "plan-lint accepts the known-good plan"
if node "$PLANLINT" "$FIXTURE/website-plan.md" >/dev/null 2>&1; then ok
else bad "the good fixture plan no longer passes — a plan rule changed"; fi

# ── 2. plan-lint FAILS a plan that breaks each quota ────────────────────────
# Same plan, section tokens rewritten to violate: only 2 families across 6
# sections, two `split` back to back, 4 kicker openers against a budget of 2,
# and adjacent shared openers.
cat > "$SCRATCH/bad-plan.md" <<'EOF'
# Website plan — Broken Fixture
Reading this as: a deliberately invalid plan.
Composition device: none.
Motion: entrance = rise-in.
Imagery register: proud-contractor.
1. Hero — format: split, opener: kicker+h2
2. Two — format: split, opener: kicker+h2
3. Three — format: card-grid, opener: kicker+h2
4. Four — format: card-grid, opener: kicker+h2
EOF
step "plan-lint rejects a quota-breaking plan"
PL_OUT="$(node "$PLANLINT" "$SCRATCH/bad-plan.md" 2>&1)"; PL_RC=$?
if [ "$PL_RC" -eq 0 ]; then
  bad "accepted an invalid plan — quota checks are not firing"
elif ! echo "$PL_OUT" | grep -q "back to back"; then
  bad "rejected, but the consecutive-family check did not fire"
elif ! echo "$PL_OUT" | grep -q "kicker-style openers"; then
  bad "rejected, but the kicker-budget check did not fire"
else ok; fi

# ── 3. detector PASSES the good mockup ──────────────────────────────────────
step "detector accepts the known-good mockup"
if node "$DETECT" "$FIXTURE/mockup/index.html" >/dev/null 2>&1; then ok
else bad "the good fixture mockup no longer passes — a detector rule changed"; fi

# ── 4. detector FAILS a slop mockup ─────────────────────────────────────────
# Four sections opening with the identical kicker+h2 shape: must trip both
# section-shape-repetition and repeated-section-kickers.
mkdir -p "$SCRATCH/slop"
cat > "$SCRATCH/slop/index.html" <<'EOF'
<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Slop</title><style>
body{font-family:Georgia,serif;color:#1b1f23;background:#fff;margin:0}
.s{padding:60px 24px}.k{font-weight:700;color:#0b5c3f;font-size:1rem}
</style></head><body>
<h1>Slop fixture</h1>
<section class="s"><div class="head"><p class="k">One</p><h2>First</h2></div><p>Body copy for the first section of the fixture.</p></section>
<section class="s"><div class="head"><p class="k">Two</p><h2>Second</h2></div><p>Body copy for the second section of the fixture.</p></section>
<section class="s"><div class="head"><p class="k">Three</p><h2>Third</h2></div><p>Body copy for the third section of the fixture.</p></section>
<section class="s"><div class="head"><p class="k">Four</p><h2>Fourth</h2></div><p>Body copy for the fourth section of the fixture.</p></section>
</body></html>
EOF
step "detector catches repeated section shapes"
SLOP_OUT="$(node "$DETECT" "$SCRATCH/slop/index.html" 2>&1)"; SLOP_RC=$?
if [ "$SLOP_RC" -eq 0 ]; then
  bad "passed an obviously sloppy page — section rules are not firing"
elif ! echo "$SLOP_OUT" | grep -q "section-shape-repetition"; then
  bad "failed, but section-shape-repetition did not fire"
elif ! echo "$SLOP_OUT" | grep -q "repeated-section-kickers"; then
  bad "failed, but repeated-section-kickers did not fire"
else ok; fi

# ── 5. packaging gate REFUSES a build with planted placeholder text ─────────
# Copy the good fixture, plant one placeholder, and confirm the packager
# refuses. Uses a throwaway prospect dir so nothing real is touched.
PLANT="$CREW_ROOT/prospects/_smoke-test-plant"
rm -rf "$PLANT"; mkdir -p "$PLANT/mockup"
cp "$FIXTURE/mockup/"* "$PLANT/mockup/"
printf '<p>[placeholder: owner quote goes here]</p>\n' >> "$PLANT/mockup/index.html"
step "packaging gate refuses planted placeholder text"
PKG_OUT="$(bash "$CREW_ROOT/pipeline/package-site.sh" _smoke-test-plant 2>&1)"; PKG_RC=$?
if [ "$PKG_RC" -eq 0 ]; then
  bad "packaged a build containing placeholder text"
elif ! echo "$PKG_OUT" | grep -q "placeholder text would ship"; then
  bad "refused, but not for the placeholder reason (rc=$PKG_RC)"
elif [ -f "$PLANT/_smoke-test-plant-site.zip" ]; then
  bad "refused but still wrote a zip"
else ok; fi
rm -rf "$PLANT"

# ── report ──────────────────────────────────────────────────────────────────
echo "───────────────────────────────────────────────────────────────────"
if [ "$FAIL" -eq 0 ]; then
  echo "  All $PASS checks passed. Gates are live."
  echo ""
  exit 0
fi
echo "  $PASS passed, $FAIL FAILED."
echo ""
echo "  A failure means a gate changed behaviour. Work out which change caused it —" >&2
echo "  do NOT loosen the fixtures in prospects/_smoke-test/ to make this go green." >&2
echo ""
exit 1
