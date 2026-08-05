# Before / after

Every "before" here is real copy this crew shipped. Every "after" keeps all the same
facts — nothing is lost, the words just stop performing.

**Read this file before you draft, not after you fail a check.** The scripts tell you a
threshold broke; this file tells you what the fix sounds like. The "before" column is
what a first draft will sound like if you write on instinct — that is the point of
keeping it. None of these pages were rewritten to make this file; they shipped, and they
stay as they are ("Lessons flow forward", `CLAUDE.md`). The afters are teaching text.

## How cases get added

A case file that stops growing stops teaching. The crew already paid for that once: the
third-person "the team built…" construction was found and fixed in FORA's round 3a, was
never written down anywhere, **and came back** — §12 below is the second catch of the
same tell.

- **Who:** the Critic, at sign-off, in the same pass that appends the `design-memory.md`
  and `copy-memory.md` rows. Also the lead, any time Harry reads a page and calls a line
  fake.
- **When:** whenever a **human read caught what both scripts passed**. That is the whole
  trigger. A line that failed `copycheck.py` is already taught by the threshold; a line
  that sailed through every check and still read wrong is the only kind worth a case.
- **What:** the before **verbatim** (paraphrase makes it useless), an after that keeps
  every fact, and one line saying what the words were doing instead of informing.
- **Where:** register problems here; page-shape problems in
  `web-humanizer/references/tells.md`. If it looks like a new *class* of failure rather
  than an instance, tell the lead — it may be worth a script check.

---

### 1. The dash-restatement template

> **Before:** Weekly and seasonal lawn care paired with steady, general upkeep of the
> whole property. It is the routine, unglamorous work that quietly keeps a yard looking
> cared-for from spring through fall — mowing, edging, and the season-to-season
> attention that a well-kept Verona lawn asks for.

> **After:** Mowing, edging, and cleanups, weekly from spring through fall. We handle
> the whole property, not just the lawn.

52 words to 21. The facts kept: weekly, spring-through-fall, mowing, edging, cleanups,
whole property. The words dropped: "routine", "unglamorous", "quietly", "cared-for",
"season-to-season attention", "asks for". None of them were information.

---

### 2. Elaboration after the dash

> **Before:** Design and installation of walkways, patios, and the stonework that gives
> a property its structure — plus upgrades to existing hardscape that has seen better
> seasons.

> **After:** Walkways, patios, and stonework — new installs and repairs to hardscape
> that's worn out.

The dash survives here because it separates two different facts (new work, repair work)
instead of restating one. That's the legitimate use, and one per section is the ceiling.

---

### 3. Client boilerplate carried over from the old site

> **Before:** Design, construction, hardscape and full-property care — with outstanding
> professional service and complete satisfaction, from start to finish.

> **After:** Design, construction, hardscape, and full-property care. Thirty years in
> Montclair, same crew.

"Outstanding professional service and complete satisfaction, from start to finish" is
their own 2003 copy. It is a fact source, not a voice source — keep the services, drop
the agency-speak, and put a real fact where it was.

---

### 4. Essayist framing of ordinary work

> **Before:** A stone fire pit at the center of the evening.

> **After:** Stone fire pits, built on site.

> **Before:** Paver, Blue Stone and Concrete walkways that lead the eye.

> **After:** Walkways in paver, bluestone, or concrete.

A landscaper does not say "at the center of the evening." The materials were always the
interesting part.

---

### 5. Section headers

| Before | After |
|---|---|
| Three Lines of Craft | What we do |
| Thirty Years, Gallery-Hung | Recent work |
| Beneath the beauty | Drainage and grading |
| Our oasis promise | What we promise |
| Verona natives, meticulous by habit. | Verona since 1981 |
| In their words. | Reviews |

---

### 6. Motif-hammering

`duran-and-son-landscaping/mockup/index.html` uses **oasis seven times** in visible copy
— the h1, the section eyebrow, the story quote, two h2s, and two body paragraphs — plus
twice more in the meta tags. Any word repeated like that reads as machine-written, no
matter how good the word is. Use it once or not at all.

Same page, same problem: "tailored" five times.

All seven, and what each one should have been:

| # | Before | After |
|---|---|---|
| 1 | *(h1)* Your dream outdoor oasis, 25 years in the making. | Landscape design and build in Northern New Jersey. 25 years, same family. |
| 2 | *(eyebrow)* Our oasis promise | What we promise |
| 3 | For over 25 years, Duran & Son Landscaping has been the go-to choice for homeowners in Northern New Jersey looking to create their dream outdoor oasis. | Duran & Son has designed and built landscapes for Northern New Jersey homeowners for 25 years. |
| 4 | *(h2)* Let's plan your outdoor oasis | Let's plan your project |
| 5 | *(h2)* Protect the oasis you built | Keep it looking the way it did on day one |
| 6 | …so your yard stays the oasis you wanted year after year. | …so the planting and stonework hold up year after year. |
| 7 | Landscape lighting extends your outdoor oasis into the evening — highlighting trees, walls and walkways with a warm, welcoming glow that's as much about safety as it is about beauty. | Landscape lighting puts light on trees, walls, and walkways after dark — safer to walk, and the yard still reads at night. |

Every fact survives: 25 years, family-owned, Northern New Jersey, design/build/maintain,
what the lighting lights and why. What goes is one word, seven times.

Note what the rewrites do *not* do — they don't swap in "sanctuary", "retreat", or
"haven". Cycling synonyms to beat the motif cap is a different tell with the same cause
(`checks.md` → elegant variation), and the fix for a mood word is a real noun, not
another mood word.

---

### 7. Spelled-out numerals and formal register

> **Before:** The Reinhardt family started Gee-Kay in 1981 and never left town.
> Forty-five years later, the work is still done the same way neighbors describe it —
> meticulous, family-run, and fairly priced.

> **After:** The Reinhardt family started Gee-Kay in 1981 and never left town. 45 years
> later, neighbors still describe the work the same way: family-run and fairly priced.

"Meticulous" is banned in composed copy — but if it appears in a **real review**, it
stays exactly as the customer wrote it. That's the difference between quoting and
performing.

---

---

### 8. Cutesy — the axis that passes every check

These are all *plain* and *conversational*. Not one trips a threshold. The owner still
called them unprofessional.

| Before | After | Why |
|---|---|---|
| We read the sun, drainage, and soil on your lot before choosing a single plant. | We check sun exposure, drainage, and soil before we pick plants. | Nobody reads the sun. The underlying fact — they assess the site first — is a real selling point and survives. |
| Species that belong in North Jersey and won't need babying to survive the winter. | Species native to North Jersey that survive the winter without extra care. | Plants aren't children. |
| …beds cut back and the lawn woken up for the season. | …beds cut back and the lawn prepped for the season. | The lawn wasn't asleep. |
| Three steps, no mystery. | How it works. | Nothing about an estimate was ever mysterious. The wink invents a problem to be clever about. |
| A lawn that looks handled, because it is. | Weekly service on a set schedule. | The coy tail is the whole sentence's reason for existing. |
| Rooted in West Essex | In West Essex since 2004 | Trade pun. Also a wasted stat line — the date is the fact. |
| From the neighbors | Customer reviews | They're customers, not neighbors. |
| …so it never piles up past the point of no return. | …so leaves don't pile up. | A joke about the work. |
| We come out, look at the space with you, and talk through what you want it to feel like. | We come out, walk the property with you, and go over what you want done. | A contractor asks what you want *done*. |

The tell they share: **the writing is visible.** A homeowner reading these notices a
copywriter. A homeowner reading "Mowing, edging, and cleanups, weekly from spring through
fall" just learns what they get.

---

### 9. Phrase-stuffing — the same five phrases, nineteen times

`anthonys-landscaping/mockup/index.html` carries **19 banned-phrase hits**. Not
nineteen different mistakes — five phrases, reused until they became the site's
structure. Every one of them is in `banlist.md`, and none of them tripped anything until
the loader was fixed, because the checker had never read that section of the list.

The hero subhead lands three of them in twenty-one words:

> **Before:** Design, construction, hardscape and full-property care — with outstanding
> professional service and complete satisfaction, from start to finish.

> **After:** Design, construction, hardscape, and full-property care.

The after is the before with the second half deleted. That is usually the whole edit:
the services were the sentence, and the rest was throat-clearing.

| Before | After |
|---|---|
| Our philosophy is to provide all of our customers with outstanding professional service and complete satisfaction. | *(cut — it says nothing the services list didn't)* |
| Weekly service, pruning, seasonal clean-ups and a turf-care program that keeps a property a cut above the rest. | Weekly service, pruning, seasonal cleanups, and turf care. |
| We take pride in our reputation for quality, experience, workmanship, and professional integrity. From start to finish we are there every step of the way. | Thirty years in Montclair, same crew. |
| *(h1)* A Cut Above the Rest. | Property maintenance |
| We keep a property a "cut above the rest" by ensuring a completely manicured lawn, meticulously pruned plant material, and healthy turf areas. | Mown, pruned, and fed on a set schedule. |
| Want a property maintained a cut above? | Want us to look at your property? |
| *(h2)* Every Step of the Way — body: From start to finish, we are there every step of the way. | *(h2)* How it works — body: *[the actual steps]* |

That last row is the one to remember. A banned phrase became a **section heading**, and
the body under it restated the heading using the *same five words*. Nothing on that
section tells a homeowner anything. When a heading and its paragraph say the same thing,
one of them is decoration — and it is almost always the paragraph that was supposed to
carry the facts.

**"A cut above" appears four times, including as an `<h1>`.** A phrase used once is a
cliché; used four times it is the site's only idea.

---

### 10. Cadence — when no single line is wrong

The hardest failure in this file, because you cannot find it one sentence at a time.
FORA's own site passed its design gate; Harry read it and said it sounded AI-written. The
audit's diagnosis (`prospects/fora-digital/audit.md`):

> **Every lead landed like a quotable closer. That cadence is the tell, more than any
> single word.**

Nothing there broke a threshold. The page had a rhythm — every paragraph ending on a
short punchy fragment, four rule-of-three constructions in a row, manufactured drama.

| Before | After | What changed |
|---|---|---|
| A sample build… Not a client; a demonstration. | This one isn't a client. Corey Blake's is a steakhouse we made up so you can see what we'd do with a restaurant. | The semicolon fragment was doing the work a plain sentence does better — and the plainer version is *harder to misread*, which matters more than the rhythm. |
| *(headline)* Two names on the door. | Who you'll be working with. | The first is the studio admiring itself; the second answers the reader's question. |
| We're a young studio and this wall doesn't pretend otherwise. | We're new at this. | Six words to four, and the four are the honest ones. |
| We put it live on your domain | We set up the domain and hosting | The before sounds better and says less. |
| We hand it off and stick around | We launch it and hand it off | "Stick around" is a promise with no shape. The after says what happens. |

Other tells the same audit caught, all invisible to a threshold: **seven em dashes**, a
**hyphen pileup** ("design-led / estimate-first / mobile-down / reservation-first" — four
coined compounds in two sentences), and **"actually" as an intensifier** ("the businesses
people actually rely on").

**The test that finds this:** read three consecutive paragraphs aloud. If each one lands
on a beat, you have cadence, not copy. Fix it by making at least one of them end
mid-thought, plainly, on a fact.

---

### 11. Invented quotes, and the template that prevents one

Also from the FORA build. The reviews section shipped as an empty template with an
example quote inside an HTML comment, for a future client to replace:

> **Before:** Their site paid for itself in a month.

> **After:** PASTE THE CLIENT'S EXACT WORDS HERE

The before is a *realistic-sounding* line. That is exactly the danger: a plausible
placeholder is one copy-paste away from becoming a fake testimonial nobody meant to
ship. The after cannot be mistaken for real copy, and the comment now carries its own
instruction — *"paste in only words a client actually wrote — never invent a quote."*

Make placeholders impossible to mistake for content. This is the same rule as the
`[AI-IMAGE: …]` convention, applied to words.

---

### 12. The regression — why cases get written down

On 2026-08-01 an audit of FORA's own site found this caption:

> **Before:** The team built a striking website for a local landscaping business. Through
> the use of our detailed design templates, quality images, and a descriptive
> questionnaire response, the team was able to put together a site that will certainly
> capture the eye of a client.

> **After:** We built this for a family landscaping crew in Essex County — a dark,
> evening-garden look with the estimate front and center, so a homeowner can see what to
> do next without hunting for it. This one's a real client, done and live.

Third-person "the team" about your own work, a "through the use of X, Y, and Z" template,
and an unfalsifiable superlative ("will certainly capture the eye"). The audit's own note
on it is the reason this section exists:

> *the exact AI-tell pattern `audit.md` round 3a already fixed once before it reverted.*

**It was caught, fixed, and came back** — because the lesson lived in one build's fix
list and nowhere else. Three more from the same audit:

| Before | After |
|---|---|
| Through the use of dazzling animations, a high-end black and gold palette, and extreme attention-to-detail… | This one's made up — a steakhouse we invented to show what we'd do with a restaurant: dark, high-end, reservation-first, with the menu and hours exactly where a hungry guest would look. |
| Not only do we have quality image generation, but we even have full video generation. | This clip started as a plain photo of an iPhone home screen — we turned it into video ourselves. Same tools, same process we'd use on your site. |
| He has several certifications in artificial intelligence, which has skyrocketed him to become one of the premier AI architects. | Harry has real certifications in AI and a running internship at a CPA practice doing tax prep and financial planning. |

That last one is the most instructive failure on this page. "Skyrocketed him to become one
of the premier AI architects" is an **unsupported superlative about a college sophomore**
— it does not just read as generated, it costs the reader's trust in everything around
it. The after keeps every real credential and drops the ranking nobody can verify.

**A bio is where invented praise hides best.** Résumé line-items in, adjectives out.

---

### 13. Cecere Brothers — a full pass, before and after

The clearest single-page transformation in the project, because both versions are on
disk. Beyond the cutesy fixes already in §8:

| Before | After | Why |
|---|---|---|
| *(h1)* Grounds worth coming home to. | Yards worth coming home to. | "Grounds" is an estate word. No NJ homeowner calls their yard the grounds — it was the site's own mood word, and the voice spec set a target of zero. |
| Design-led landscaping, lawn care, and stonework for the homes of Caldwell, Cedar Grove, and West Orange. Two brothers, one crew, twenty years of local roots. | Landscaping, lawn care, and stonework in Caldwell, Cedar Grove, and West Orange. | 26 words to 13. "Design-led" is a coined compound, "the homes of" is padding, "local roots" is a pun, and "twenty years" belongs in the stat strip as a numeral where it already lives. |
| *(stat)* 20 yrs · Rooted in West Essex | 22 yrs · In West Essex County | The pun goes, and the number gets *corrected* — it had gone stale. Accuracy outranks tone. |
| *(h2)* What we tend to. | *(cut)* | "Tend" is the same mood-word family as "grounds". |
| *(h2)* Recent grounds. | Recent work. | |
| *(kicker)* From the neighbors | Customer review | They're customers. |

Two lessons past the individual lines. First, **a mood word spreads**: "grounds" was in
the hero, a section header, and the gallery label, so fixing the hero alone would have
left the tell on the page — this is what the watch list in `voice-spec.md` is for. Second,
**the stat was wrong**, and the copy pass is where that surfaced. Read numbers as claims,
not decoration.

---

### 14. What FreshBooks does well — and what doesn't transfer

`freshbooks.com` is accounting software, not a trade site, so copy it selectively. Three
things it does better than anything in this project:

**It writes to the customer.** The homepage is almost all "you/your". Compare the first
pass of a landscaping site, which ran 34 "we/our" against 22 "you/your" — accurate, but a
log of the contractor's activities instead of the homeowner's outcome.

| Company-framed | Customer-framed |
|---|---|
| We check sun exposure, drainage, and soil before we pick plants. | You get a site check — sun, drainage, and soil — before any plant is picked. |

**Numbers do the persuading.** "Save up to 553 hours each year." "$7000 in billable
hours." "4.8/5.0 from 120,000+ reviews." Not *saves time*, not *highly rated*. The trade
equivalents are turnaround, years, towns, crew size, base depth, visit frequency — and
they must be numbers the client actually gave you.

**Promise, then mechanism, then payoff.**

> Get paid faster with automated invoices and billing, secure online payments, and
> built-in reminders **so cash flow stays predictable**.

Outcome first, three concrete mechanisms, then the consequence the reader cares about.
That last clause is the one this skill nearly banned outright — see rule 5.

**What does not transfer.** Don't copy the site wholesale:

- **"Award-winning in-house customer support"** — this is the self-announced-virtue
  pattern in `banlist.md`. A national brand can absorb it; a two-man crew saying
  "award-winning" invites the question *which award?*
- **Promo urgency and emoji** — "90% off for 6 months", "Work smarter this summer ☀️".
  Wrong register for a contractor quoting work.
- **Scale stats** — "30M+ small businesses", "160+ countries". A local business has no
  such numbers, and inventing an equivalent breaks the real-facts-only rule. Their honest
  version is "7 towns" and "400+ properties maintained", which is plenty.

The lesson is the *method* — you-framing, real numbers, promise→mechanism→payoff — not the
voice of a software company.

## What good already looks like in this project

These shipped, and they're right. Match this.

> Broken down? Get it to a shop that will tell you straight what it needs.

> Not sure if you're in the area? Give us a call — if we can help, we'll tell you straight.

> Organized records you can actually use to run the place.

> Fair. Honest. Since 1961.

That last one is a triad, and it works — **once**. Another prospect shipped "Straight
answers. Clean books. Since 1983." on the same portfolio. Two clients with the same
skeleton is how a bespoke site starts looking like a template.

## And what the reference site does

`prospects/dasilva-associates/mockup/index.html` — the best-reading page in this
project — is mostly not sentences at all:

> 385 Lafayette Street · Newark's Ironbound

> Se Habla Espanol · Nos falamos o portugues

> DWI and vehicular charges, drug crimes, weapon and violent offenses, and sex offenses.

> Purchase and sale agreements, title searches, leases, and co-op and condo transactions,
> from offer through closing.

Specification. Nouns, streets, statutes, numbers. Its home page carries 322 words of body
copy with 2 em dashes total, and the one place it stops listing and starts talking is a
single line in the office band — *"A real estate closing or a traffic ticket may be
routine for the office, but it rarely feels that way from where you're sitting."* That's
the pattern: **plain everywhere, with exactly one place where a person speaks.**
