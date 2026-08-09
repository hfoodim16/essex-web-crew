#!/bin/bash
# Package a prospect's finished site into a rename-proof zip for handoff.
# Usage: pipeline/package-site.sh <prospect-name> [--force]
# Output: prospects/<prospect-name>/<prospect-name>-site.zip
#
# GATED. The zip refuses to build unless the site passes the detector, carries no
# placeholder leakage, and has a design-memory row. This exists because gee-kay's
# deploy-ready/ folder shipped with "[placeholder: a short note from owner…]" and
# 27 contrast failures in it — packaging ran after critique and checked nothing.
set -euo pipefail

CREW_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PROSPECT=""
FORCE=0
for arg in "$@"; do
  case "$arg" in
    --force) FORCE=1 ;;
    *) [ -z "$PROSPECT" ] && PROSPECT="$arg" ;;
  esac
done

if [ -z "$PROSPECT" ]; then
  echo "Usage: $0 <prospect-name> [--force]" >&2
  echo "Prospects:" >&2
  ls "$CREW_ROOT/prospects" >&2
  exit 1
fi

PROSPECT_DIR="$CREW_ROOT/prospects/$PROSPECT"
if [ ! -d "$PROSPECT_DIR" ]; then
  echo "No such prospect: $PROSPECT_DIR" >&2
  exit 1
fi

# Best available version of the site, in priority order
SITE_DIR=""
for candidate in deploy-ready deliverable mockup; do
  if [ -f "$PROSPECT_DIR/$candidate/index.html" ]; then
    SITE_DIR="$PROSPECT_DIR/$candidate"
    break
  fi
done

if [ -z "$SITE_DIR" ]; then
  echo "No index.html found in deploy-ready/, deliverable/, or mockup/ for $PROSPECT" >&2
  exit 1
fi

STAGING="$(mktemp -d)/${PROSPECT}-site"
mkdir -p "$STAGING"
# Copy site files only. `_*.html` are dev scratch harnesses that point at localhost;
# Netlify's own `_redirects`/`_headers` have no extension, so they still ship.
rsync -a --exclude '.DS_Store' --exclude '*.zip' --exclude '__MACOSX' --exclude '_*.html' "$SITE_DIR/" "$STAGING/"

# ---------------------------------------------------------------------------
# GATE — everything below runs against the staged copy, i.e. exactly what would
# ship. Nothing is deleted on failure; the staging dir is cleaned up either way.
# ---------------------------------------------------------------------------
# bash 3.2 (macOS default) errors on ${#arr[@]} for an empty array under `set -u`,
# so track failures as a newline-delimited string instead.
GATE_FAILURES=""
add_failure() { GATE_FAILURES="${GATE_FAILURES}${GATE_FAILURES:+$'\n'}• $1"; }

# 1. Detector must exit 0 AND must not have silently degraded. A degraded run
#    uses the regex fallback, catches almost nothing, and still exits 0 — so a
#    clean result under that warning is worthless.
# NOTE: detect.mjs writes its report to STDERR, not stdout, so both the findings
# and the DEGRADED banner land in the same capture.
DETECT_OUT="$(mktemp)"
if node "$CREW_ROOT/skills/web-design-ultra/scripts/detect.mjs" "$STAGING"/*.html \
      >/dev/null 2>"$DETECT_OUT"; then
  DETECT_RC=0
else
  DETECT_RC=$?
fi
if grep -q "DETECTOR DEGRADED" "$DETECT_OUT" 2>/dev/null; then
  add_failure "detector ran DEGRADED (missing parser deps) — result is meaningless.
      Fix: cd skills/web-design-ultra/scripts/detector && npm install"
elif [ "$DETECT_RC" -ne 0 ]; then
  # Summarise by rule id + count rather than dumping 50+ near-identical lines.
  DETAIL="$(grep -oE '^[[:space:]]+\[[a-z0-9-]+\]' "$DETECT_OUT" 2>/dev/null \
            | tr -d ' []' | sort | uniq -c | sort -rn | head -8 \
            | awk '{printf "      %s x%s\n", $2, $1}' || true)"
  TOTAL="$(grep -cE '^[[:space:]]+\[' "$DETECT_OUT" 2>/dev/null || echo '?')"
  add_failure "detector found $TOTAL anti-patterns:
${DETAIL:-      (run detect.mjs on the site dir for detail)}"
fi

# 2. No placeholder leakage in shipped files. Labeled `<!-- AI-IMAGE: … -->`
#    comments are the crew's intended convention and are NOT matched here; this
#    targets visible bracketed notes and unresolved PLACEHOLDER_ tokens.
LEAKS="$(grep -rnE '\[[Pp]laceholder|\[[^]]*— confirm\]|\[Hours —|PLACEHOLDER_[A-Z]' \
          "$STAGING" 2>/dev/null | grep -v 'AI-IMAGE' | head -12 || true)"
if [ -n "$LEAKS" ]; then
  add_failure "placeholder text would ship to the client:
$(echo "$LEAKS" | sed "s|$STAGING/||" | sed 's/^/      /')"
fi

# 3. The build must be logged for anti-repetition, or the next build can't
#    diverge from it.
if ! grep -qi "$PROSPECT" "$CREW_ROOT/design-memory.md" 2>/dev/null; then
  add_failure "no design-memory.md row for '$PROSPECT' — log the build (font pairing, palette, archetype, signature motion) before shipping"
fi

rm -f "$DETECT_OUT"

ZIP_PATH="$PROSPECT_DIR/${PROSPECT}-site.zip"

if [ -n "$GATE_FAILURES" ]; then
  echo "" >&2
  echo "✖ PACKAGING REFUSED — $PROSPECT ($(basename "$SITE_DIR")/)" >&2
  echo "$GATE_FAILURES" | sed 's/^/  /' >&2
  echo "" >&2
  if [ "$FORCE" -ne 1 ]; then
    echo "  Nothing was written. Fix the above, or re-run with --force to package anyway." >&2
    rm -rf "$(dirname "$STAGING")"
    exit 2
  fi
  echo "  --force given: packaging anyway, marked UNGATED in the filename." >&2
  echo "" >&2
  ZIP_PATH="$PROSPECT_DIR/${PROSPECT}-site-UNGATED.zip"
fi

rm -f "$ZIP_PATH"
(cd "$STAGING" && zip -r -X -q "$ZIP_PATH" .)
rm -rf "$(dirname "$STAGING")"

if [ -z "$GATE_FAILURES" ]; then
  echo "✔ Gate passed — detector clean, no placeholder leakage, design-memory logged."
fi
echo "Packaged $(basename "$SITE_DIR")/ → $ZIP_PATH"
unzip -l "$ZIP_PATH"
