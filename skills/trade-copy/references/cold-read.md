# The cold read

The last step before any copy ships. **Dispatch a fresh agent that has not seen the
drafting or the fixes, and have it judge the page cold.**

## Why this exists and not more rules

Every previous version of this skill tried to solve bad copy with better rules. The
record says rules are not the binding constraint:

| Reader | Result |
|---|---|
| `copycheck.py` alone | Passed a page the owner called fake. Twice. |
| The agent that wrote the fixes, reading carefully | Missed 28 offenders, then 20 more. |
| A fresh agent reading cold | Found all of them, both times. |

The writer cannot hear the page. Having just chosen a sentence, you read your intention
instead of your words, and a line you edited around becomes a line you believe you read.
That is not carelessness and more diligence will not fix it. A second pair of eyes will.

## The protocol

1. **Finish your own pass first.** The cold read is verification, not a substitute for
   doing the work — don't ship a draft to it and ask what to fix.
2. **Dispatch a subagent with no context from your session.** It must not be told what you
   changed, what you were worried about, or that the copy has already been through a pass.
   Anything you tell it, it will agree with.
3. **Give it the owner's own standard**, in the owner's words. "It's a landscaper, not a
   dessert" is worth more than a paragraph of criteria.
4. **List the settled decisions** so it doesn't re-litigate approved choices. Pull these
   from the voice spec's *Settled* section.
5. **Demand an honest null.** Without this, agents invent marginal findings to look
   thorough, and real findings get lost in the noise.
6. **Fix what it finds, then run it again** if the round was large. The second cold read
   on the first site still found 20 offenders after the first round's 28 were fixed.

## Prompt template

> Final copy audit for a [TRADE] business website. The owner is a working [TRADE] in
> [TOWN] who has rejected drafts as [THE OWNER'S ACTUAL COMPLAINT] — his standard:
> "[HIS OWN WORDS]."
>
> Read ALL visible copy in these files (headings, paragraphs, card text, stat labels,
> gallery captions, button text, meta descriptions). Exclude nav, footer, and real
> customer review quotes: [PATHS]
>
> One test per line: would a licensed contractor say this out loud to a homeowner standing
> in their driveway?
>
> Flag only genuine problems, in these categories:
> - CUTESY (puns, winks, jokes, anthropomorphized plants/weather, coy "actually")
> - POETIC (literary, atmospheric, metaphor)
> - VAGUE (claim with no content, self-announced virtue, adjectives doing a fact's job,
>   absolute overclaims)
> - OVERWRITTEN (trailing clause or restatement adding no fact)
> - CADENCE (lines landing like quotable closers; fragments used for drama; every
>   paragraph ending on a punchline; a rhythm so even it reads as designed)
> - UNSUPPORTED (a number, price, turnaround, guarantee, or spec not established anywhere
>   else on the site, and reading as invented)
> - INACCURATE (a claim the rest of the page contradicts)
>
> Quote verbatim with file:line and category.
>
> Do NOT report these, they are settled: [SETTLED DECISIONS FROM THE VOICE SPEC]
>
> Do NOT invent marginal findings to seem thorough. If a page is clean, say "CLEAN" and
> move on. I need to know whether this is actually finished, so an honest "nothing left"
> is more useful than padding. Final verdict: SHIP or NOT READY, with a count of real
> remaining offenders.

## Reading the result

- **Point it at what you just changed.** If the pass added a particular kind of line, say
  so and ask it to be strict there. Naming the suspicion — "this pass added 'so…'
  consequence clauses; tell me if any assert something the business never claimed" —
  turned up three invented promises (a pricing structure, a ten-year lifespan, a storm
  response time) that a generic audit of the same page would likely have read past.
- **CADENCE is the category this project learned the hard way.** FORA's round-3a audit
  found the page's real problem was that *"every lead landed like a quotable closer —
  that cadence is the tell, more than any single word."* No individual line looked
  wrong. Ask the reader for the pattern, not just the offenders.
- **Findings in the UNSUPPORTED and INACCURATE buckets outrank every tone finding.** The last two the cold
  read caught were a "20 yrs" stat on a page that said "since 2004" (it was 2026), and a
  heading promising "what every visit includes" over a list of twice-a-year work. Wrong
  is worse than ugly, and both were the kind of thing that becomes an argument in a
  driveway.
- **A finding you disagree with is still data.** If a fresh reader misread the line, a
  homeowner can too.
- **"SHIP" from an agent told it may say SHIP is meaningful.** That's the point of the
  honest-null instruction.

## Banking the result

The fix list is for this build. **The case file is for every build after it.**

Any finding the cold read produced that both scripts passed goes into
`references/examples.md` — before verbatim, after with every fact intact, one line on
what the words were doing. The Critic does this at sign-off (`.claude/agents/critic.md`).

Why this step exists: the cold read is the most productive slop-detector this crew has —
by the record at the top of this file, it found what the script missed twice and what a
careful self-read missed 48 times. All of that value evaporates if the finding ships with
the build and is never written down. It has already cost us once: a third-person
construction fixed in FORA's round 3a reverted onto the live site, because the lesson
existed in a fix list and nowhere else.

If the finding is a *shape* rather than a register problem, it belongs in
`web-humanizer/references/tells.md`. If it looks like a whole class nobody has named yet,
tell the lead — new classes are where the next script check comes from.
