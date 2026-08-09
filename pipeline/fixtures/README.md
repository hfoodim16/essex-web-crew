# Fire-drill fixtures — test data, not a client

**Nothing in this folder is a business.** "Smoke Test Plumbing" is invented. Nothing
here ships, nothing here costs money, and no client will ever see it. These files
exist so `pipeline/fire-drill.sh` has something to test the quality gates against.

They lived in `prospects/` until 2026-08-05, where they looked like a stray client
folder and got deleted twice. They are drill infrastructure, so they now live beside
the drill that owns them.

## Why the drill needs them

Every gate can fail in two directions, and only one of them is visible:

- **It becomes impossible to satisfy** — nothing passes. You notice immediately,
  because your work stops.
- **It silently stops firing** — everything passes. You never notice, because a broken
  gate and clean work look identical from the outside.

The second one is the reason this folder exists. The drill keeps a deliberately
**good** page and a deliberately **bad** page, and after any rule change it checks that
each gate still *accepts* the good one and still *rejects* the bad one.

Not hypothetical here. `banlist.md` sat unread for a month — its loader only parsed
single backticked words, so an entire section of banned phrases was decoration — while
every check reported green. The first run after the fix found 19 hits on one built page.

## What's in here

| File | What it proves |
|---|---|
| `website-plan.md` | **Written to pass `plan-lint.mjs` exactly.** Every required field present, all four section-format quotas satisfied |
| `build-sheet.md` | **Written to pass the sheet half of `plan-lint.mjs`** — every `var(--x)` defined, unique section ids, no rename instructions |
| `mockup/index.html` + `style.css` | **Written to pass `detect.mjs` exactly.** One `<h1>`, four format families, AA contrast, no banned fonts, no placeholder text |
| `copy-good.html` | Passes **both** copy gates — `copycheck.py` and `aitells.py` — clean |
| `copy-bad.html` | Plants one instance of each tell the copy gates catch. **Deliberately terrible. Do not fix it.** |

The drill writes its known-bad plan, sheet, and mockup into a temp dir at runtime, so
only the good fixtures plus `copy-bad.html` live on disk.

## Rules for editing

The drill's whole value is that a failure means *the gates changed*, not that a
fixture rotted. So:

- If you change a gate's thresholds, update these fixtures deliberately and say so in
  the commit.
- **Never "fix" a drill failure by loosening a fixture until it passes.** Work out
  which gate changed and whether that change was intended.
- Keep them small. They're read by a human debugging a gate, not by a client.

## If you deleted them

```bash
git restore pipeline/fixtures/
```

The drill aborts red and prints that command rather than reporting a false PASS —
which is what it used to do, since a missing file matched none of its grep patterns.
