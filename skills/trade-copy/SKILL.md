---
name: trade-copy
description: Use when writing or reviewing any visible text for a local-business website — headlines, hero subheads, section copy, service descriptions, about text, CTAs, meta and alt text — or when copy reads fake, stiff, over-written, AI-generated, too poetic, or unlike how the owner actually talks. Also use when planning a site's voice from a client questionnaire, auditing a built mockup's wording, or drafting outreach email and call scripts.
---

# Trade copy

## Overview

Websites for local businesses fail on wording in a specific way: the copy is *good
writing* about a landscaper instead of *a landscaper's website*. The owner reads it and
finds sentences he would never say out loud, and the whole site reads fake to him even
though no individual line is bad.

**The voice is a licensed contractor talking to a homeowner in their driveway** —
competent, direct, unembarrassed. Not charming, not lyrical, not folksy. He is quoting
work he'll be held to.

**Copy is specification, not prose.** Concrete nouns, numbers, town names, service names,
hours, materials. The best-reading site in this project reads like a menu and a spec
sheet, not like an essay.

**Three ways to miss the target.** Only the first was obvious; the others sink just as
many pages:

| Miss | Sounds like | Real example |
|---|---|---|
| **Too poetic** | essayist, atmospheric, magazine profile | "A stone fire pit at the center of the evening." |
| **Too cute** | whimsy, puns, winking, jokes | "won't need babying to survive the winter" |
| **Too vague** | claims with no content | "When the weather turns, we show up." |

"Plain" is not the target and won't save you — *"won't need babying"* is plain, and the
owner still called it unprofessional. **Professional** is the target.

**The shape that works:** `[what you get] + [the concrete thing that delivers it] + [so,
the consequence]`.

> Paver patios laid on compacted gravel and screed sand, with joints locked **so they
> don't shift**.

Terse is not the goal — *true and useful* is. A page of bare fragments ("Laid in matching
stone.") is honest and sells nothing. See rule 5.

**The root cause of bad copy is thin facts.** When a section has nothing real to say, the
instinct is to write around the hole with atmosphere. Don't. **Shrink the section.** A
four-word label that is true beats forty words that are decoration.

## Voice comes from the questionnaire, not from the old website

`prospects/<slug>/client-answers.md` is the voice source. The client's own answers show
how they talk, and the site should sound like that.

The old site (`site-content.md`) is a **fact source only** — services, years, towns,
phone, hours, credentials. Its *wording* carries no authority. If their 2003 site says
"outstanding professional service and complete satisfaction, from start to finish," those
are facts about nothing; take the services and drop the phrasing.

## Two stages

**Stage A — write the voice spec before any copy exists.** Read
`references/voice-spec.md` and produce `prospects/<slug>/voice-spec.md`. This is the
Planner's job, and it happens before the plan's hero direction is written. It fixes
register, word budgets, the client's own phrases, and which sections are allowed to be
short because the facts are thin.

**Stage B — draft against the spec, then measure.** Read the voice spec first, write to
its budgets, then run `references/checks.md`.

## The drafting rules

1. **Say-aloud test.** Every sentence has to be something the owner would say to a
   customer standing at the truck or the counter. "Meticulous by habit" fails. "We show
   up when we say we will" passes. This test outranks every other rule here.
2. **No cuteness.** Lawns, plants, soil, sun, weather, and seasons have no feelings,
   needs, or intentions — they don't get *babied*, they don't *wake up* in spring, and
   nobody *reads the sun*. No puns on the trade ("Rooted in West Essex"). No winking at
   the reader ("Three steps, no mystery"), no jokes about the work ("past the point of no
   return"), no coy tails ("A lawn that looks handled, because it is"). Charm is not
   warmth. It reads as a copywriter performing, and the owner has to send this link to
   paying customers.
3. **Contractions on.** "It's", "we'll", "doesn't". No sentence starts "It is" or "There
   is." Use digits, not spelled-out numerals: "45 years", not "Forty-five years."
4. **Em dashes: at most one per hundred words, and never twice in a section.** The
   failure mode is a template — `[plain clause] — [prettier restatement of the same
   clause]` — repeated down the whole page.
   > "Design and installation of walkways, patios, and the stonework that gives a
   > property its structure — plus upgrades to existing hardscape that has seen better
   > seasons." → "Walkways, patios, and stonework — new installs and repairs."
   That dash survives, because it separates two different facts. A dash that restates
   the clause before it is the one to cut.
5. **Keep the payoff, cut the restatement.** Not every trailing clause is padding, and
   deleting them all leaves a spec sheet that sells nothing. A second half earns its place
   when it names **a consequence the customer can check**: "with joints locked *so they
   don't shift*", "*so water runs away from the house*", "*so there's no separate bill in
   November*". It fails when it says the first half again in nicer clothes: "Clean cut
   edges and a finished mulch layer — *the part that makes the whole yard look
   intentional*." Ask one question: does the second half tell them something new *that
   matters to them*? Keep it. Just prettier? Cut it. If you can't state the consequence
   concretely, write no clause — don't dress a restatement up with "so."
   **The payoff must rest on something the business already claims.** This rule's own
   failure mode: reaching for a consequence and inventing one. "Included in the maintenance
   plan, *so there's no separate bill*" asserts a pricing structure the site never states.
   "*so they still sit level a decade from now*" is a ten-year warranty nobody offered.
   "*usually within 48 hours of the call*" borrowed the estimate turnaround and applied it
   to storm response. All three passed every mechanical check; a cold reader caught them.
   A consequence about *physics or horticulture* is safe — "so they don't shift", "so
   water runs away from the house", "so leaves don't smother the grass". A consequence
   about **price, warranty, lifespan, or response time is a promise**, and you may only
   write it if the client said it.
6. **Write to the customer, not about yourself.** Default to "you/your". Reserve "we" for
   what the contractor owns — showing up, cleaning the site, standing behind the work.
   "We schedule the work, show up when we said we would, and clean the site before we
   leave" is a promise and belongs in "we". A whole page of "we do this, we do that" turns
   a sales page into a log of your activities. Don't overcorrect either: a two-brother
   crew writing "you will receive punctual service" sounds like a phone company.
7. **Numbers are the argument.** Years in business, towns served, crew size, turnaround,
   base depth, visit frequency, warranty length, response time. A real number outsells any
   adjective — "usually within 48 hours" beats "fast, reliable service" every time. Use
   only numbers the client actually gave you; never invent one to fill the shape.
8. **One triad per page, maximum.** "Fair. Honest. Since 1961." is fine once. Before
   using one in a hero, grep the other prospects: two clients with the same
   three-fragment hero looks copy-pasted.
   `grep -h -A2 '<h1' prospects/*/mockup/index.html`
9. **No motifs.** Do not carry an evocative word through the page. "Oasis" in the hero,
   the promise band, three cards and the CTA is the single loudest AI tell in this
   project's output. Any banned or watched word: twice per page, hard ceiling.
10. **Every paragraph carries a fact.** A number, a town, a material, a service name, a
   name, an hour. A paragraph with none of those is padding — delete it, don't rewrite it.
   > "Our philosophy is to provide all of our customers with outstanding professional
   > service and complete satisfaction." → *(cut)*
   Note the after is nothing. There was no fact to save. Rewriting a padding paragraph
   produces a better-written padding paragraph.
11. **One lyrical block per site, or none.** If the owner said something worth quoting,
   give it a first-person attributed block ("— Mike, owner"). It must be built from what
   they actually said in their answers, never invented. Everywhere else on the page is
   plain.
   The reference build spends its one on this, in the office band:
   > "A real estate closing or a traffic ticket may be routine for the office, but it
   > rarely feels that way from where you're sitting."
   322 words of body copy on that page, and exactly one place where a person speaks.
   That ratio is the rule.
12. **Write to the budgets** in the voice spec. Defaults: hero headline 2–9 words (2 only for an interior page title like "Practice areas"; a homepage hero wants a real sentence), hero
   subhead ≤ 30, service card ≤ 30, service detail ≤ 45, about ≤ 120 across 2–3 short
   paragraphs, FAQ answer ≤ 40.
13. **Plain CTA, no wordplay.** "Get a free estimate." "Call Mike." The CTA verb comes
   from how the client said they want to be contacted.
   > "Want a property maintained a cut above?" → "Want us to look at your property?"
14. **Use their words.** The sounds-like bank in the voice spec holds phrases the client
   actually wrote. Getting one of their own sentences onto their homepage is worth more
   than anything you can compose.
   DaSilva's best block is the owner, verbatim from his answers:
   > "I opened the office in May 2002 to serve the community where I was born and raised."
   Nothing composed for that page beats it. Cecere's questionnaire gave "a mess and a
   deadline" — four words no copywriter would have reached for, and the truest thing on
   the site. **Mine the answers for these before you write a line of your own.**

## Content parity means facts, not word count

The Builder must carry every block of real information across (CLAUDE.md — Content
parity). **Parity counts facts, not words.** Tightening a 60-word service description to
25 words that carry the same facts *passes* parity. Dropping one of the facts fails it.
Never pad to survive a parity review — a critic who bounces a mockup for terseness that
kept every fact is misreading the rule.

## Never touch

- **Real review quotes.** Verbatim, always, including their em dashes and their
  adjectives. Never edit a real quote to pass a check.
- **Q14 "keep word-for-word" content** from the client's answers.
- **Legal text, license and insurance numbers, name/address/phone, hours.**

## Measuring

```bash
python3 skills/trade-copy/scripts/copycheck.py prospects/<slug>/mockup/index.html
```

Twelve hard checks, plus advisory readouts that need a human read. Full explanation of
each threshold, what a failure means, and how to fix it: `references/checks.md`.
The Builder runs this before handoff. The Critic runs it as a hard gate.

**`no banned phrases` is new (2026-08-05)** and so is the reason: the loader only ever
read single backticked words, so `banlist.md`'s whole "Banned phrases" section — and six
Tier 2 words wrapped across a line break — were written down and checked by nothing. The
first run of the fixed loader found 19 hits on one built page.

**Outreach drafts have a gate now too:**

```bash
python3 skills/trade-copy/scripts/copycheck.py prospects/<slug>/outreach-email.md --outreach
```

`references/outreach-voice.md` always said "the banlist applies here too" and nothing
could run it — this script read HTML only. Harry sends those drafts himself, which makes
them the copy with the least review and the most consequence. In outreach mode the hero
and placeholder checks are skipped: a draft is *supposed* to carry `[Harry's phone]`.

## Fixing an existing page

**The script tells you where to start. It never tells you where to stop.**

The checks measure eleven mechanical things. They cannot hear register, so a page can go
green while still reading like a brochure written by someone who has never held a shovel.
Every fix pass therefore reads **every visible string on the page**, not the flagged ones.

```bash
python3 skills/trade-copy/scripts/copycheck.py <page.html> --list
```

That prints every heading, paragraph, card, and label with its line number. Work down it
and put a verdict on each line — fine, too poetic, too cute, too vague, overwritten —
*before* you edit anything. Then fix.

This is not optional diligence. On the one page this skill was first used to fix, the
script went green and two of the worst lines on the site survived — sitting two lines
above an edit that had just been made. Adjacent is not the same as read.

## The cold read — required before anything ships

**Dispatch a fresh agent to judge the copy cold, and fix what it finds.** Full protocol
and prompt template: `references/cold-read.md`.

You cannot hear your own page. Having just chosen a sentence, you read your intention
instead of your words. This is not carelessness — on this project the script passed bad
copy twice, the agent that wrote the fixes then missed 28 offenders and, after fixing
those, missed 20 more. A fresh reader caught all of them both times.

So the order is: **read `references/examples.md`** → draft → `--list` sweep → checks green → **cold read** → fix → **bank any case the scripts missed** → ship. The
cold reader must not be told what you changed or what you were worried about; it must be
told the owner's own standard and the settled decisions; and it must be explicitly allowed
to answer "CLEAN", or it will manufacture findings to look useful.

## Red flags — stop and cut

If you catch yourself thinking any of these, the copy is going wrong:

| Thought | What it actually means |
|---|---|
| "This section needs a little more here." | The section has no facts. Shrink it, don't fill it. |
| "The dash makes it flow better." | You wrote the sentence twice. Keep the first half. |
| "It's a nice image — it sets a tone." | The owner has to send this link to his customers. |
| "Their old copy says it this way." | Their old copy is a fact source, not a voice source. |
| "Three short fragments read punchy." | You've used the one triad. Every other prospect has too. |
| "This word ties the page together." | That's motif-hammering, and it's the loudest tell. |
| "Terse copy will fail content parity." | Parity counts facts. Tighten freely; drop nothing. |
| "The script passed, so the copy is fine." | Eleven mechanical checks. None of them can hear register. |
| "I fixed everything it flagged." | Flagged lines are where the read starts, not where it ends. |
| "I was editing right next to it, it looked fine." | You didn't read it. Read it. |
| "I read it all carefully myself, a cold read is overkill." | You wrote it. You read your intention, not your words. Every time this was tested, the cold read found more. |
| "The cold reader is being picky." | Then a homeowner might be too. Argue with the finding, not with having received it. |
| "It's charming — it gives the site personality." | Charm is not warmth. The owner sends this to paying customers. |
| "A little humor makes them seem human." | A contractor quoting work he'll be held to doesn't crack jokes about it. |

## Files

| File | Use |
|---|---|
| `references/voice-spec.md` | Stage A: how to mine the answers, and the artifact template |
| `references/checks.md` | Every check, threshold, and fix |
| `references/banlist.md` | Banned words, phrases, and sentence shapes, by register |
| `references/examples.md` | Before/after pairs from this project's real sites |
| `references/cold-read.md` | The independent second-reader pass; required before shipping |
| `references/outreach-voice.md` | Email and call-script voice (Harry sends; the crew never contacts anyone) |
| `scripts/copycheck.py` | The measurement tool |

**`web-humanizer` runs as the final sweep on every built page** — after this skill's
checks, never instead of them. It owns the website-shaped tells this skill doesn't measure:
heroes that open with a verb any industry could use, card titles built from two
abstractions, a page with no number a customer could check, cards stamped to identical
lengths. Its `scripts/aitells.py` gates alongside `copycheck.py`, and its word lists are
kept disjoint from `banlist.md` so no word ever gets two different fixes. It already
encodes this project's precedence: the voice spec wins, real review quotes are never
touched, and nothing gets added to a page to satisfy it.

The general-text `humanizer` stays available for long-form prose outside a mockup —
articles, outreach drafts. Where it conflicts with the voice spec — it bans em dashes
outright, it is register-agnostic, and it actively coaches "add personality" — **the voice
spec wins**. Never run it over real review quotes.
