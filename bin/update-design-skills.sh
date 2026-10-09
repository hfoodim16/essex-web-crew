#!/usr/bin/env bash
# update-design-skills.sh — pull the crew's third-party design skills from upstream,
# back up what's installed, and sync them into ~/.claude/skills AND this repo's skills/
# bundle (which install.sh ships to Corey). Re-run any time to refresh.
#
#   bin/update-design-skills.sh            # update + install
#   bin/update-design-skills.sh --dry-run  # show what would change, touch nothing
#
# Harry's own skills (web-design-ultra, trade-copy, web-humanizer, generate, design-*)
# are never touched here — they have no upstream.
set -euo pipefail

dry=0; [ "${1:-}" = "--dry-run" ] && dry=1
repo="$(cd "$(dirname "$0")/.." && pwd)"
global="$HOME/.claude/skills"
work="$(mktemp -d -t design-skills)"
backup="$HOME/.claude/skill-backups/$(date +%Y-%m-%d-%H%M%S)"

# name | upstream repo | path inside the repo
skills=(
  "impeccable|pbakaus/impeccable|plugin/skills/impeccable"
  "frontend-design|anthropics/claude-code|plugins/frontend-design/skills/frontend-design"
  "taste-skill|Leonxlnx/taste-skill|skills/taste-skill"
  "redesign-skill|Leonxlnx/taste-skill|skills/redesign-skill"
  "ui-ux-pro-max|nextlevelbuilder/ui-ux-pro-max-skill|.claude/skills/ui-ux-pro-max"
  "design|nextlevelbuilder/ui-ux-pro-max-skill|.claude/skills/design"
  "design-system|nextlevelbuilder/ui-ux-pro-max-skill|.claude/skills/design-system"
  "ui-styling|nextlevelbuilder/ui-ux-pro-max-skill|.claude/skills/ui-styling"
  "brand|nextlevelbuilder/ui-ux-pro-max-skill|.claude/skills/brand"
  "banner-design|nextlevelbuilder/ui-ux-pro-max-skill|.claude/skills/banner-design"
  "design-motion-principles|kylezantos/design-motion-principles|skills/design-motion-principles"
  "web-quality-audit|addyosmani/web-quality-skills|skills/web-quality-audit"
  "core-web-vitals|addyosmani/web-quality-skills|skills/core-web-vitals"
  "performance|addyosmani/web-quality-skills|skills/performance"
  "seo|addyosmani/web-quality-skills|skills/seo"
  "accessibility|addyosmani/web-quality-skills|skills/accessibility"
  "best-practices|addyosmani/web-quality-skills|skills/best-practices"
)

# Skills the crew's agents invoke. Only these (plus any already bundled) go into the
# repo's skills/ folder that install.sh ships to Corey.
crew_uses=" frontend-design design-motion-principles web-quality-audit core-web-vitals performance seo accessibility best-practices "

for entry in "${skills[@]}"; do
  IFS='|' read -r name upstream sub <<<"$entry"
  clone="$work/${upstream//\//__}"
  [ -d "$clone" ] || git clone -q --depth 1 "https://github.com/$upstream" "$clone"
  src="$clone/$sub"
  [ -f "$src/SKILL.md" ] || { echo "SKIP $name: no SKILL.md at $upstream/$sub"; continue; }

  dests=("$global/$name")
  if [ -d "$repo/skills/$name" ] || [[ "$crew_uses" == *" $name "* ]]; then dests+=("$repo/skills/$name"); fi
  for dest in "${dests[@]}"; do
    if [ -d "$dest" ]; then
      changes=$(rsync -ainc --delete --exclude .env --exclude .venv --exclude __pycache__ "$src/" "$dest/" | grep -cE "^(>|\*deleting|c)" || true)
    else
      changes="new"
    fi
    if [ "$changes" = "0" ]; then echo "ok      $name  ($dest)"; continue; fi
    echo "update  $name  ($changes)  -> $dest"
    [ $dry = 1 ] && continue
    if [ -d "$dest" ]; then mkdir -p "$backup/$(basename "$(dirname "$dest")")"; cp -R "$dest" "$backup/$(basename "$(dirname "$dest")")/"; fi
    mkdir -p "$dest"
    rsync -ac --delete --exclude .env --exclude .venv --exclude __pycache__ "$src/" "$dest/"
  done
done

rm -rf "$work"
[ $dry = 1 ] && echo "dry run — nothing changed" || echo "done. backups: $backup"
