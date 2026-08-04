# `_smoke-test` — synthetic fixture, not a real prospect

**Smoke Test Plumbing is not a business.** Nothing here is a client, nothing here
ships, and nothing here costs money. This folder exists so `pipeline/fire-drill.sh`
has a known-good build to check the gates against.

The underscore prefix keeps it visually separate in `ls prospects/`.

## What's in here

| File | Role in the drill |
|---|---|
| `client-answers.md` | Minimal answers so the folder looks like a real Build run |
| `website-plan.md` | **Written to pass `plan-lint.mjs` exactly.** Every required field present, all four section-format quotas satisfied |
| `mockup/index.html` + `style.css` | **Written to pass `detect.mjs` exactly.** One `<h1>`, four format families, AA contrast, no banned fonts, no placeholder text |

## Rules for editing

These fixtures are calibration references — the drill's whole value is that a
failure means *the gates changed*, not that the fixture rotted. So:

- If you change a gate's thresholds, update these fixtures deliberately and say
  so in the commit.
- Never "fix" a drill failure by loosening the fixture until it passes. Work out
  which gate changed and whether that change was intended.
- Keep them small. They're read by humans debugging a gate, not by clients.
