#!/usr/bin/env bash
# One-time setup for the Essex Web Crew on a new Mac.
# Installs the bundled skills into ~/.claude/skills/ and bootstraps the
# ai-multimodal image-generation environment.
#
# Usage: ./install.sh          skip any skill you already have
#        ./install.sh --force  overwrite your existing copies
set -euo pipefail
cd "$(dirname "$0")"

FORCE=0
[ "${1:-}" = "--force" ] && FORCE=1

SKILLS_SRC="$PWD/skills"
SKILLS_DST="$HOME/.claude/skills"
AIM="$SKILLS_DST/ai-multimodal"

echo "Essex Web Crew setup"
echo "  skills from : $SKILLS_SRC"
echo "  skills to   : $SKILLS_DST"
echo

# ---------- 1. skills ----------
mkdir -p "$SKILLS_DST"
installed=0 skipped=0
for src in "$SKILLS_SRC"/*/; do
  name="$(basename "$src")"
  dst="$SKILLS_DST/$name"
  if [ -e "$dst" ] && [ "$FORCE" -eq 0 ]; then
    echo "  skip     $name (already installed — use --force to overwrite)"
    skipped=$((skipped + 1))
    continue
  fi
  # Never clobber a live .env when overwriting.
  if [ -f "$dst/.env" ]; then
    tmpenv="$(mktemp)"; cp "$dst/.env" "$tmpenv"
  else
    tmpenv=""
  fi
  rm -rf "$dst"
  cp -R "$src" "$dst"
  if [ -n "$tmpenv" ]; then cp "$tmpenv" "$dst/.env"; chmod 600 "$dst/.env"; rm -f "$tmpenv"; fi
  echo "  install  $name"
  installed=$((installed + 1))
done
echo
echo "Skills: $installed installed, $skipped skipped."
echo

# ---------- 2. python for ai-multimodal ----------
# Image generation needs Python 3.10+. macOS ships 3.9, so look for a newer one.
PY=""
for cand in python3.13 python3.12 python3.11 python3; do
  if command -v "$cand" >/dev/null 2>&1; then
    if "$cand" -c 'import sys; sys.exit(0 if sys.version_info >= (3,10) else 1)' 2>/dev/null; then
      PY="$(command -v "$cand")"; break
    fi
  fi
done

if [ -z "$PY" ]; then
  echo "!! No Python 3.10+ found. AI image generation will not work until you install one:"
  echo "     brew install python@3.12"
  echo "   Then re-run ./install.sh"
else
  echo "Python for image generation: $PY ($("$PY" --version 2>&1))"
  if [ -d "$AIM" ]; then
    if [ -x "$AIM/.venv/bin/python" ]; then
      echo "  venv already exists — leaving it alone."
    else
      echo "  creating venv + installing dependencies (this takes a minute)..."
      "$PY" -m venv "$AIM/.venv"
      "$AIM/.venv/bin/pip" install --quiet --upgrade pip
      "$AIM/.venv/bin/pip" install --quiet -r "$AIM/scripts/requirements.txt"
      echo "  done."
    fi
  fi
fi
echo

# ---------- 3. Gemini API key ----------
if [ -d "$AIM" ]; then
  if [ ! -f "$AIM/.env" ]; then
    cp "$AIM/.env.example" "$AIM/.env"
    chmod 600 "$AIM/.env"
    echo "Created $AIM/.env"
  fi
  if grep -q "your_api_key_here" "$AIM/.env" 2>/dev/null; then
    echo "ACTION NEEDED — add your Gemini API key:"
    echo "  1. Get a key at https://aistudio.google.com/apikey"
    echo "  2. Edit  $AIM/.env"
    echo "  3. Set   GEMINI_API_KEY=<your key>"
    echo "  Image generation is billed to that key — the crew makes 2 images per mockup."
  else
    echo "Gemini API key: already set."
  fi
fi
echo

# ---------- 4. optional extras ----------
command -v rtk >/dev/null 2>&1 \
  && echo "rtk: installed (token-saving CLI wrapper)." \
  || echo "rtk: not installed — optional. The crew works fine without it."

echo
echo "Next: read SETUP-COREY.md, then run ./run.sh from Terminal."
