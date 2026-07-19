#!/usr/bin/env bash
# Launch Claude Code in this project with agent teams enabled.
# Usage: ./run.sh   (from anywhere — it cd's into the project itself)
set -euo pipefail
cd "$(dirname "$0")"
echo "Starting Claude Code with agent teams enabled (CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1)..."
echo "Then paste a prompt from KICKOFF.md — do the dry run first."
CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 exec claude "$@"
