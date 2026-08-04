# STATE — <prospect-slug>

> The run's durable ledger. Append-only. On pause or kill, THIS FILE is the handoff —
> no improvised RESUME-HERE notes. On resume, every teammate reads it before anything
> else. Keep entries short; this is a ledger, not a journal.

## Current stage

<!-- One line, updated in place (the only non-append field):
     e.g. "Stage 7 — builder mid-build" / "Stage 8 round 2 — awaiting critic" / "PAUSED by Harry 14:02" -->

## Fix ledger (append one row per fix, per round — never overwrite)

<!-- DONE requires PAGE-LEVEL EVIDENCE: the file/page plus what was observed rendering,
     never a bare grep count. The canonical failure: a fix was logged "DONE — 3 occurrences"
     where the 3 were a CSS base rule plus its two responsive steps, not three pages;
     a full round was wasted rediscovering it was never fixed. -->

| Round | Fix | Status | Evidence (page-level, or it isn't DONE) |
|---|---|---|---|

## Open questions (append; strike through when answered)

<!-- Anything blocked on Harry or the lead. One line each, with who owes the answer. -->

## Voided gates (append when a mid-run change invalidates earlier passes)

<!-- e.g. "Palette changed to azul+gold — round-1 distinctiveness PASS void; re-run at next audit."
     A gate listed here is NOT passed, whatever audit.md says. -->

## Sheet review (B1b)

<!-- One line per round: "Round 1 — SHEET GO" or "Round 1 — 4 fixes to planner (listed
     in critic message <time>)". The Builder starts only after a SHEET GO line exists. -->

## Evidence block (written by the Builder at handoff — REQUIRED)

<!-- Paste real outputs, never summaries. A handoff without this block gets bounced
     unreviewed; a claim that fails the Critic's random spot-check triggers a full
     re-run and is itself a fail item.
     - detector exit code per page (with per-page finding counts)
     - copycheck.py exit code · aitells.py exit code
     - composition counts: sections / distinct families / max consecutive / kickers vs
       budget / opener dupes
     - screenshot filenames saved -->

## Stood-down teammates

<!-- Name + timestamp when a teammate is stood down. A teammate on this list who receives
     a message replies "Stood down — forward to the lead" and takes no other action. -->
