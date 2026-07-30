# Principles — why the human-sounding lines work

Distilled from Harry Dry's copywriting guides (marketingexamples.com/copywriting/tips and
/conversational), Mailchimp's voice-and-tone guide, and the exemplars in
`exemplars.md`. Sources are free and worth reading in full.

These are the reasons behind the fixes in `tells.md`. When a fix feels arbitrary, the
principle behind it is here.

---

## The three tests

Run these on any line before it ships. They are faster than any checklist.

1. **Can I visualize it?** "A low-maintenance outdoor living space" has no picture in it.
   "A bluestone patio you hose off" does.
2. **Can I falsify it?** If nothing in the line could be proven wrong, it also can't be
   proven right, so it persuades nobody. Numbers, dates, place names, license numbers.
3. **Could nobody else say this?** Paste the line onto a competitor's site. If it still
   works, cut it or make it specific.

## The one gate that outranks the tests

**Read it aloud, in the owner's voice, standing at their truck or their front desk.** If it
would sound strange coming out of their mouth, it is wrong for their site, even if it is
good writing. Harry Dry's version is the kitchen table: read it to your partner, and if
they cringe, rewrite it.

---

## Writing

1. **Write with your eraser.** Cut until the line can't lose another word. Most fixes in
   `tells.md` are deletions.
2. **Nobody cares what you can do. They care what you can do for them.** "We use
   commercial-grade equipment" is about you. "Your lot gets cut in one visit" is about them.
3. **Don't exaggerate.** An honest line reads warmer than an inflated one. "Most jobs, same
   week" beats "always fast".
4. **Kill the passive voice.** Name who does what. Passive construction is how a page
   avoids committing to anything.
5. **Kill adverbs and adjectives.** They are vague and they try too hard. A noun and a
   number do the work.
6. **More periods, fewer commas.** Short sentences read as speech. Long ones read as prose.
7. **Use contractions.** Only academics say "you are". (copycheck.py enforces a floor of
   three per page.)
8. **Ignore grammar rules that make you sound like a document.** Start a sentence with And.
   Use a fragment. That is what talking looks like on a page.
9. **Ditch the thesaurus.** The plain word is the right word. Synonym-cycling across a page
   is a tell in itself.
10. **Don't kill the personality — and don't manufacture one.** The best sites feel real,
    which is a different thing from feeling clever. On this crew's trade sites, personality
    comes from what the owner actually said in the questionnaire, never from the writer.

## Structure

11. **Slippery slide.** Every line's only job is to get the next line read. A headline that
    closes its own loop has failed at its job.
12. **Find the tension.** Pleasant copy gets forgotten. The problem the customer walked in
    with is the tension, and stating it plainly is the strongest opening on a trade site.
13. **Don't persuade — let the reader persuade themselves.** Lay out the facts in the order
    a customer thinks about them and stop.
14. **Fence-sitters don't buy.** Take a position. "We don't do sealcoating" is stronger
    than a list of everything.
15. **Stories beat facts for memory, facts beat adjectives for trust.** Use both; skip the
    adjectives.
16. **Respect the competition.** Naming what a competitor does well signals confidence.
    Nobody who is winning needs to sneer.

## Voice

17. **Use the customer's own words.** The fastest way to sound human is to quote the
    people you serve. For this crew that means the questionnaire answers, which are the
    voice source of record. The old website is a *fact* source and its wording carries no
    authority.
18. **Load up on personal pronouns,** weighted toward you/your. copycheck.py reports the
    we/you ratio as an advisory for exactly this reason.
19. **Empathize, don't impress.** The reader has a problem. Impressing them is a detour.
20. **Don't imitate.** Clichés are inversely correlated with sounding alive. If a phrase
    arrived pre-assembled, it came from somewhere else.
21. **Don't try too hard.** Customers see through forced voice faster than they see through
    dull voice. Mailchimp's rule: dry humor, never jokes, and forced humor is worse than
    none.
22. **Clear beats entertaining.** Always. On every page, in every register.

---

## Where these stop

All of it is subordinate to the client's `voice-spec.md`. Where a principle here and the
spec disagree, the spec wins — it was built from what the owner actually said, and this
file was built from consumer brands with different permissions. In particular:

- "Don't kill your personality" does **not** license charm, puns, winks, or
  anthropomorphism on a trade site. `banlist.md` Tier 1B bans those outright and it is
  correct.
- "Ignore grammar rules" does not extend to legal text, license numbers, hours, or NAP.
- No principle here justifies adding a fact the client did not give you.
