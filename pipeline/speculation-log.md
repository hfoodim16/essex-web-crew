# Speculation log — how good are our guesses?

Several builds start before the client has said a word: the Analyst reads their old
site and Google listing, and the Planner builds from inference. When the real
questionnaire eventually arrives, we find out how much of that was right.

**Nothing else in the crew captures that.** Without this log every speculative build
is a fresh guess, and we never learn which inferences hold and which ones we should
stop making. A few filled rows here is the difference between "the crew builds sites"
and "the crew gets better at building sites."

## When to append

The **Planner**, at the start of any Build run where a prior `client-answers.md`
carried the `SPECULATIVE PITCH` banner. Before planning from the real answers, diff
them against what the speculative build assumed and log one row per material
difference. Cosmetic wording differences don't count — log things that would have
changed the build.

`Verdict` is one of:

- **confirmed** — we guessed it and the client agrees
- **wrong** — the client says otherwise; the speculative build would have been off
- **unasked** — the questionnaire doesn't cover it, so it stays an assumption

## The log

| Date | Prospect | Source of the guess | What we assumed | What the client actually said | Verdict | Rule of thumb |
|---|---|---|---|---|---|---|
| _(first entries come from the DaSilva & Associates run — its build ran fully speculative, so it's the first real measurement)_ | | | | | | |

## Rules of thumb (promote here once a pattern repeats)

Once the same verdict shows up across two or three prospects, write the lesson here
and the Analyst/Planner should apply it by default.

- _(none yet — needs data)_
