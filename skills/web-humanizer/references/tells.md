# The 20 website AI tells

Not the article tells. A generated *page* fails differently from a generated *essay*: the
sentences can be individually fine and the page still reads like it came out of a machine,
because the shapes are the shapes of a template.

Each tell below: what it looks like, why it reads generated, and the fix as a recipe. The
fix is always **more concrete**, never more clever. `[script]` means `aitells.py` catches
it; `[read]` means only a person can.

---

## Hero and headline

### 1. Interchangeable hero verbs `[script]`
Any hero opening with Empower, Unlock, Unleash, Transform, Elevate, Supercharge,
Revolutionize, Reimagine, Maximize, Optimize, Streamline, Amplify, Accelerate. Also
Discover / Experience / Introducing as an imperative headline.

Why it reads generated: the verb carries no information about the business. "Transform
your outdoor space" works for every landscaper in New Jersey, which means it works for
none of them.

**Fix:** name what the customer ends up with, in the words they would use.
- "Elevate Your Outdoor Living Experience" → "Patios, walls, and walkways in West Essex"
- "Unlock Your Home's Potential" → "Kitchen remodels, start to punch list, in 6 weeks"
- "Transform Your Smile Today" → "Same-day crowns, most in one visit"

### 2. Outcome with no mechanism `[script advisory]` `[read]`
"The intelligent way to manage your property." "We help you save time and money."
A result is promised; nothing on the page says how it happens.

**Fix:** replace the outcome with the mechanism that produces it, or cut the line. If the
client never told you the mechanism, the line does not get filled in — it gets deleted.
- "We save you money on your taxes" → "We file your return and your quarterly estimates"

### 3. Audience vagueness `[script]`
"For modern homeowners." "For today's busy families." "Businesses of all sizes."

Why it reads generated: it is an audience with no address. A real local business names the
towns it drives to.

**Fix:** name the place, the property type, or the situation.
- "For today's busy homeowners" → "For Nutley, Belleville, and Bloomfield"
- "Businesses of all sizes" → "Sole proprietors and shops under 20 employees"

### 4. The benefit triad headline `[script advisory]`
"Faster. Simpler. Better." "Fast, Fair, and Local." Three parallel abstractions with no
referent. copycheck.py already caps three-fragment triads at one per page; this is the
comma-list variant.

**Fix:** one of the three, made specific. Three real services in a heading is fine
("Mowing, cleanups, and mulch") — three qualities is not.

### 5. Contained headline `[read]`
A headline that closes its own loop, so there is no reason to read the next line.
"We Offer Quality Plumbing Services in Essex County."

**Fix:** make the headline owe the reader something. State the problem, or a fact odd
enough to need explaining. "Most of our calls are a fixture nobody has touched in 20 years."

---

## Cards and sections

### 6. Two-abstract-noun card titles `[script]`
"Seamless Integration." "Professional Service." "Quality Workmanship." "Expert Care."

Why it reads generated: it names a category of goodness instead of a thing you do.

**Fix:** title the card with the service, the noun a customer would search for.
- "Quality Workmanship" → "Transmission rebuilds"
- "Comprehensive Solutions" → "Bookkeeping and payroll"
- "Expert Care" → "Root canals and extractions"

### 7. Suspicious symmetry `[script]`
Four cards at exactly 27 words each. Every section the same length. A pros/cons list
balanced to the item.

Why it reads generated: hand-written cards come out uneven, because the facts are uneven.
Even lengths mean the length was the specification and the facts got padded to reach it.

**Fix:** let the card with more to say be longer, and let the thin one be one sentence.
A card with nothing behind it gets cut, not filled.

### 8. Body restating its own heading `[script in copycheck]`
Heading "Seat walls & fire pits" over body "Built-in seat walls and fire pits, laid in
matching stone." (copycheck.py reports this as `heading_echoes`.)

**Fix:** the body carries only what the heading does not. "Laid in matching stone."

### 9. Fragmented headers `[read]`
Section headings that are sentence fragments doing mood work: "Beneath the beauty."
"Where craft meets care."

**Fix:** the heading labels the section. "Drainage." "How we work."

### 10. The everything-page `[read]`
Every service listed, none explained; the page covers the whole trade so nothing on it is
specific to this business.

**Fix:** the three services that actually pay the bills get a section. The rest get a list.

---

## Vocabulary and sentence texture

### 11. The AI-vocab cluster `[script]`
effortless, hassle-free, leverage, robust, scalable, game-changer, world-class,
best-in-class, industry-leading, next-level, top-notch, one-stop, innovative, synergy,
delve, myriad, plethora, paramount, pivotal, vibrant, nuanced, comprehensive, cornerstone,
turnkey, future-proof, customer-centric, results-driven, second to none, unmatched.

(A second, overlapping list lives in `trade-copy/references/banlist.md` and is capped at
two uses per page by copycheck.py. The two lists are kept disjoint so no word gets two
different fixes from two different scripts.)

Why a cluster and not a word: "comprehensive" alone is a word an accountant would use
about a return. Three of these on one page is a fingerprint.

**Fix:** the plain word, or the number.
- "robust, comprehensive coverage" → "covers the roof, the siding, and the gutters"
- "industry-leading response times" → "on site within 48 hours, most weeks same day"

### 12. Uniform sentence rhythm `[script advisory]`
Every sentence 14 to 18 words. Human copy swings from 3 words to 30.

**Fix:** break one long sentence into two, and let one be four words. Do not add sentences
to vary the rhythm — cut, then split.

### 13. Adjective stacking `[read]`
"A beautiful, functional, low-maintenance outdoor living space."

**Fix:** one adjective at most, or none, and let a noun do the work. "A bluestone patio you
hose off."

### 14. Passive construction and subjectless fragments `[read]`
"Your project will be handled with care." "Committed to excellence in every job."

**Fix:** name who does what. "Rich runs every job himself."

---

## Trust and proof

### 15. Zero falsifiable claims `[script]`
Not one number, date, place name, license number, or proper noun anywhere on the page.
Nothing a customer could check, and nothing a competitor could not also claim.

**Fix:** one checkable fact minimum. A year founded, a count of jobs, a response window, a
service radius, a license number, a price floor. Never invent one — if the questionnaire
does not have it, ask, and until then the page carries fewer claims.

### 16. The competitor-paste test `[read]`
Take any line, paste it onto a competitor's site. If it still works, it was never about
this business. This is the single most useful read on the page and no script can run it.

**Fix:** add the thing only they can say. The 1961 founding date, the two brothers, the
one town they will not drive past.

### 17. Generic testimonials `[script advisory]`
"Great service, highly recommend!" — no name, no town, no detail, and all quotes on the
page in the same voice.

**Fix:** real quotes only, verbatim, with whatever name the customer gave. A page with two
real reviews beats a page with six invented ones. Never edit a real quote to pass a check,
and never write one.

### 18. Missing proof of the work `[read]`
No photos of the actual crew, truck, shop, or finished job. Stock imagery only.

**Fix:** flag the gap as a labeled placeholder and tell the client exactly which photo to
send. A labeled placeholder is honest; a stock photo pretending to be their work is not.

### 19. Self-announced virtue `[script in copycheck]`
"Honest, reliable, no-pressure service." Every contractor claims this, so it persuades
nobody. (banlist.md Tier 1B owns this one.)

**Fix:** state the fact and let it stand. "Free on-site estimate, usually within 48 hours."

### 20. Scarcity and urgency theater `[read]`
"Limited spots available!" on a service with unlimited capacity. Countdown timers on an
evergreen offer.

**Fix:** delete it. If a real constraint exists — a season, a booked calendar — say the
real one: "Fall cleanup books out by mid-October."

---

## Round 2 — the tells added 2026-08-05 `[script hard]`

Sourced from the Wikipedia "Signs of AI writing" categories the general `humanizer` skill
carries. An audit found 28 of its 33 categories with no mechanical check anywhere in this
crew, while `aitells.py`'s original six gates had gone quiet — **zero hits across all 30
built pages**. A gate that never fires is not proof of a clean corpus; it is a gate that
stopped measuring what the crew still does. Each one below swept to zero across those 30
pages before it was made hard, so none of them fires on work already signed off.

| # | Tell | Before → After | Why it is a tell |
|---|---|---|---|
| 21 | **Chat-register opener** | "Here's the thing: your lawn is your first impression." → "A mown, edged lawn is the first thing anyone sees." | An assistant's voice, not a business's. Nobody writes this on their own site. |
| 22 | **Signposting** | "Let's break down what we do." → "What we do" | Essay scaffolding on a page that is not an essay. The heading was already the signpost. |
| 23 | **Filler phrase** | "At the end of the day, when it comes to drainage, grading matters." → "Grading is what fixes drainage." | Cut the phrase and the sentence survives — which is the test. Here two phrases hid one fact. |
| 24 | **Authority trope** | "The real question is whether your contractor shows up." → "We show up when we say we will." | Asserts weight instead of earning it. The after makes the claim in the crew's own name, where it can be held against them. |
| 25 | **Negative parallelism** | "It's not just a lawn, it's a first impression." → "Weekly mowing and edging, spring through fall." | Builds a strawman version of the service to knock it down. The after says what you actually get. |
| 26 | **Negation run** | "No guessing. No surprises. No hidden fees." → "You get the price before we start, and it doesn't change." | Two is a plain trade site being direct. Three is the rule of three in a costume — and the after is the only one of the four that states the actual promise. |
| 27 | **`-ing` trailer clause** | "We mow twice a month, keeping the property looking its best." → "We mow twice a month." | The tail restates instead of adding. `banlist.md` banned this shape by name and nothing read it until now. Exempt when the tail carries a number or a name — then it is the fact, not a restatement. |
| 28 | **Punchline cadence** | "A sample build… Not a client; a demonstration." → "This one isn't a client. Corey Blake's is a steakhouse we made up so you can see what we'd do with a restaurant." | From the FORA round-3a audit: *"Every lead landed like a quotable closer. That cadence is the tell, more than any single word."* Full case: `trade-copy/references/examples.md` §10. |
| 29 | **Copula avoidance** | "Our shop serves as a partner, not a parts counter." → "We explain the repair before we do it." | Reaching around the word "is". The shorter verb is almost always right, and here the honest version is a different sentence entirely. |
| 30 | **Weasel attribution** | "Experts agree that annual service extends transmission life." → "A fluid change every 30,000 miles is what the manufacturer calls for." | An authority nobody names. On a client site this is also an honesty problem — the after names one that can be checked. |
| 31 | **Emoji** | "Work smarter this summer ☀️" → "Book spring cleanups now — the calendar fills by mid-April." | Never on a contractor's site. Note `★` and `✓` are typography, not emoji, and are not flagged. |
| 32 | **Hyphen-compound pileup** | "A design-led, estimate-first, mobile-down, reservation-first approach." → "We design it, price it before you commit, and build it to work on a phone." | Four coined compounds in two sentences, caught by a human read on FORA's own site and by nothing mechanical. Dictionary hyphenates (family-owned, year-round) are exempt. |

Advisory in the same pass: **false ranges** ("from patios to retaining walls"), **Title
Case Headings**, **`Label: sentence` card stacks**, **boldface density**, and the overall
hyphen-compound rate.

---

## Signs of HUMAN writing — preserve these

Every other section here is about what to remove. This one is about what a rewrite must
not sand off, and it is the reason a humanizing pass can make a page worse. If an edit
deletes one of these, the edit is wrong:

- **A specific number nobody would invent** — "47 years on Pompton Avenue", "$95, and it
  comes off the bill".
- **An admission** — "we don't do irrigation", "that repair isn't worth it on this car".
  A model does not volunteer limits; a business does.
- **A named, checkable particular** — a street, a brand of equipment, a town, a person.
- **Uneven rhythm.** A three-word sentence next to a thirty-word one is a human writing.
  Evening it out is the single most common way a "cleanup" pass adds slop.
- **Mild, unpolished phrasing** — "we'll tell you straight", "give us a call". Plain is
  the target, not a symptom.
- **The owner's own words** from the questionnaire, even when they are clumsy. Especially
  when they are clumsy. `voice-spec.md`'s "Sounds like them" block outranks every rule
  in this file.
- **Repetition that carries information** — a landscaper's page should say "patio" six
  times.

---

## What NOT to flag

The false-positive list matters as much as the tells. Do not flag:

- **Plain, unadorned sentences.** Plain is the target, not a symptom.
- **Perfect grammar.** Real businesses hire real proofreaders.
- **A single word from the vocab list.** One is a coincidence; three is a fingerprint.
- **Repeated service nouns.** A landscaper's page should say "patio" six times.
- **Short pages.** A one-page site with four facts on it is not thin; it is a small
  business.
- **Formal register on a law or medical site.** Register comes from `voice-spec.md`, and
  it outranks everything here.
- **Real review quotes,** including their em dashes, their exclamation points, and their
  word "meticulous".
- **Q14 keep-word-for-word content, legal text, license numbers, NAP, hours.**
- **Numbers everywhere.** A stat strip is not padding.

Look for clusters, not single hits. One abstract heading on an otherwise concrete page is
a heading to rewrite. Three abstract headings, no numbers, four cards of identical length,
and a hero that opens with "Elevate" is a generated page.
