---
name: web-humanizer
description: |
  Use when reviewing or rewriting the visible copy of a website so it reads as
  written by a person. Triggers: a hero that opens with Empower / Unlock /
  Transform / Elevate, card titles built from two abstract nouns ("Seamless
  Integration", "Professional Service"), benefit-triad headlines, "for today's
  busy homeowners" audience lines, a page with no number or place name anywhere
  on it, cards stamped to identical lengths, or copy the client called generic,
  templated, or AI-written. Also use before handing off any built page whose
  copy has to pass review with zero human edits. Runs on built HTML, after
  trade-copy.
---

# web-humanizer

The website-specific counterpart to the general `humanizer` skill. `humanizer` fixes
generated *prose*; this fixes generated *pages* — the shapes that make a site read like a
template even when every sentence is grammatical.

Division of labour on this crew:

| Owns | Skill |
|---|---|
| Register — how the owner talks, word budgets, banned vocabulary, em dashes, contractions, cutesiness | `trade-copy` |
| Page shape — interchangeable heroes, abstract card titles, no checkable facts, stamped card lengths | **this skill** |
| Long-form prose outside a mockup (articles, outreach drafts) | `humanizer` |

## Precedence, before anything else

1. **The client's `prospects/<slug>/voice-spec.md` outranks this skill.** It was built from
   what the owner actually said. Where the spec and a rule here disagree, the spec wins,
   and you note the conflict in your handoff rather than silently overriding either one.
2. **Never touch:** real review quotes (verbatim, including their em dashes), Q14
   keep-word-for-word content from `client-answers.md`, legal text, license and insurance
   numbers, NAP, hours.
3. **Never add words.** Terseness is not a parity failure. Every fix here is a swap or a
   deletion; if a section has nothing behind it, it shrinks or goes, it does not get filled.
4. **Never invent a fact.** No year, price, response time, or job count that is not in the
   questionnaire. A page with fewer claims is fine; a page with a made-up one is not.
5. **The fix for an AI tell is more concrete, never more clever.** No charm, no puns, no
   winks, no anthropomorphism. `banlist.md` Tier 1B bans those and it is right.

## Process

Four steps, and step 2 is the one that does the work.

**1. Sweep.** Run `--list` and read every visible string against `references/tells.md`. Put
a verdict on each line before editing anything: *fine / could be any company / no fact in
it / stamped to length / abstract heading*. Editing as you read is how half a page gets
missed.

```bash
python3 skills/web-humanizer/scripts/aitells.py prospects/<slug>/mockup/index.html --list
```

**2. Self-critique in writing.** Answer this in full before you touch the page:

> If I saw this page cold, with no idea who built it, what would make me say a machine
> wrote it?

Name the specific lines. Vague answers ("the tone is a bit generic") mean you have not
looked yet. This step is inherited from `humanizer` and it is the reason the loop converges
without a human editing words afterwards.

**3. Rewrite.** Use the fix recipes in `references/tells.md` (every tell now carries a
before → after), the real shipped cases in **`trade-copy/references/examples.md`** — §10
is the cadence failure this skill's step 2 is looking for — the structures in
`references/exemplars.md`, and the three tests in `references/principles.md`:

- Can I visualize it?
- Can I falsify it?
- Could nobody else say this?

**4. Measure, then read again.** Run the script until it exits 0, then re-read the page
aloud in the owner's voice. On a trade site the order is: copycheck first, aitells second,
voice-spec above both.

```bash
python3 skills/trade-copy/scripts/copycheck.py prospects/<slug>/mockup/*.html
python3 skills/web-humanizer/scripts/aitells.py prospects/<slug>/mockup/*.html
```

## Ship gate

The page is done when all of these are true:

- Every hard check in `aitells.py` passes, on every page of the site.
- The hero names what the customer gets, in words the customer would use.
- Every card title names a service, not a category of goodness.
- At least one claim on the page carries a number a customer could check.
- At least one sentence on the page is a sentence the owner would actually say out loud.
- No line on the page would still work if a competitor pasted it onto theirs.

The last two are the real gate. The script is a floor.

## The script

`scripts/aitells.py` — stdlib Python, no dependencies. Exit 0 = all hard checks pass, 1 =
at least one FAIL.

```bash
python3 skills/web-humanizer/scripts/aitells.py <page.html> [more pages] [--list|--json]
```

**Eighteen hard checks.** The original six — hero verb openers · abstract-pair card
titles · AI-vocab cluster · vague audience · falsifiable-claim floor · card symmetry —
plus twelve added 2026-08-05: chat-register openers · signposting · filler phrases ·
authority tropes · negative parallelism · negation runs · `-ing` trailer clause ·
punchline cadence · copula avoidance · weasel attribution · emoji · hyphen-compound
pileup. See `references/tells.md` for what each one is and why.

Those twelve came from the Wikipedia "Signs of AI writing" set the general `humanizer`
skill carries: 28 of its 33 categories had no mechanical check anywhere in this crew,
while the original six had gone quiet — zero hits across all 30 built pages. Every new
check swept to zero across those same 30 pages before it was made hard, so none of them
fires on work already signed off.

Advisories, printed and never auto-failed, because each needs a human read: comma-triad
headings, sentence-rhythm uniformity, near-identical card lengths, outcome-with-no-mechanism
sentences, review blocks carrying no name, vocab hits under the cluster threshold, false
ranges, Title Case headings, `Label: sentence` card stacks, boldface density, and the
overall hyphen-compound rate.

**It does not re-check anything copycheck owns** — em-dash rate, three-fragment triads,
contractions, paragraph length, motif caps, cutesy language, placeholders. The two word
lists are kept disjoint on purpose so no single word ever gets two different fixes from two
different scripts. If you add a word to one, check the other.

Both scripts push the same direction: more concrete. They do not conflict; if a fix seems
to satisfy one and break the other, the fix is wrong.

## Files

| File | What's in it |
|---|---|
| `references/tells.md` | The 32 website AI tells, each with a before → after fix, plus the what-NOT-to-flag list and the signs-of-human-writing preserve list |
| `references/exemplars.md` | Real attributed copy from sites that read human, with what transfers to a trade site and what doesn't |
| `references/principles.md` | Why those lines work — Harry Dry and Mailchimp, distilled, with the three tests |
| `scripts/aitells.py` | The hard gate |
