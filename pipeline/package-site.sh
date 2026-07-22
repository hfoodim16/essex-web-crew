#!/bin/bash
# Package a prospect's finished site into a rename-proof zip for handoff.
# Usage: pipeline/package-site.sh <prospect-name>
# Output: prospects/<prospect-name>/<prospect-name>-site.zip
set -euo pipefail

CREW_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PROSPECT="${1:-}"

if [ -z "$PROSPECT" ]; then
  echo "Usage: $0 <prospect-name>" >&2
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

ZIP_PATH="$PROSPECT_DIR/${PROSPECT}-site.zip"
rm -f "$ZIP_PATH"
(cd "$STAGING" && zip -r -X -q "$ZIP_PATH" .)
rm -rf "$(dirname "$STAGING")"

echo "Packaged $(basename "$SITE_DIR")/ → $ZIP_PATH"
unzip -l "$ZIP_PATH"
