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
