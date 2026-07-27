# Banlist — words and shapes that make a local-business site read fake

Three tiers. Pick the tier from the register preset in `voice-spec.md`. Tier 1 is the
default; almost every client this crew builds for is a trade or a small office.

`copycheck.py` reads the backticked words out of the **Banned words** lists below and
caps each at 2 uses per page. Words outside those lists are not machine-checked — that
is what the say-aloud test is for.

---

## Tier 1 — Trade / blue collar (landscaper, mason, transmission shop, tree service, HVAC, roofer)

### Banned words

- `meticulous`
- `meticulously`
- `craftsmanship`
- `artistry`
- `artisan`
- `curated`
- `bespoke`
- `elevate`
- `elevated`
- `transform`
- `transformative`
- `oasis`
- `sanctuary`
- `retreat`
- `haven`
- `nestled`
- `tapestry`
- `testament`
- `symphony`
- `seamless`
- `seamlessly`
- `unparalleled`
- `unrivaled`
- `bespoke`
- `timeless`
- `enduring`
- `discerning`
- `refined`
- `exquisite`
- `breathtaking`
- `stunning`
- `unglamorous`
- `understated`
- `deliberate`
- `intentional`
- `philosophy`
- `ethos`
- `journey`
- `passion`
- `passionate`
- `dedicated`
- `commitment`
- `excellence`
- `premier`
- `cutting-edge`
- `state-of-the-art`
- `solutions`
- `holistic`
- `curate`
- `showcase`
- `boasts`
- `renowned`
- `esteemed`

### Banned phrases

- "from start to finish"
- "every step of the way"
- "a cut above"
- "leads the eye" / "draws the eye"
- "attention to detail" (say what the detail *is*)
- "outstanding professional service"
- "complete satisfaction"
- "peace of mind" (unless the client said it)
- "we pride ourselves on"
- "quality workmanship" (empty — name the work)
- "no job too big or too small"
- "your vision, our expertise"

### Banned shapes

| Shape | Example of the failure | Do this instead |
|---|---|---|
| `[plain clause] — [poetic restatement]` | "We grade, drain and waterproof so the work stays put — the invisible groundwork behind a property that holds up season after season." | Stop at the first clause. |
| Three-fragment hero | "Fair. Honest. Since 1961." | One plain sentence, or a fact. Max one triad per page, and never if another prospect's site already uses one. |
| Essayist framing of ordinary work | "It is the routine, unglamorous work that quietly keeps a yard looking cared-for." | "Mowing, edging, and cleanups, weekly through the season." |
| Art-gallery framing of a photo grid | "Thirty Years, Gallery-Hung" | "Recent work" |
| Abstract noun as a section header | "Beneath the beauty" / "Our oasis promise" | "Drainage" / "What we promise" |
| Motif carried through every section | "oasis" in the hero, the promise band, three cards, and the CTA | Use the word once, if at all. |
| `-ing` trailer clause | "...season after season, keeping the property looking its best." | Delete the trailer. |

---

## Tier 1B — Cutesy / whimsical (applies to every tier, including hospitality)

The second failure axis, and the harder one to see: this language is *plain* and
*conversational*, so it slips past every rule aimed at purple prose. It still gets a site
called unprofessional, because a contractor quoting work he'll be held to does not talk
like a children's book.

### Banned words

- `babying`
- `babied`
- `pampering`
- `pampered`
- `coddle`
- `thirsty`
- `hungry`
- `sleepy`
- `woken`
- `snug`
- `cozy`
- `sulk`
- `sulking`
- `cranky`
- `happily`
- `magic`
- `magical`
- `whisper`
- `whispers`
- `honestly`
- `no pressure`
- `no upsell`

### Banned shapes

| Shape | Real example | Do this instead |
|---|---|---|
| **Anthropomorphism** — plants, lawns, soil, sun, weather, or seasons given feelings, needs, or intentions | "Species that … won't need **babying** to survive the winter" · "the lawn **woken up** for the season" | "Species native to North Jersey that survive the winter without extra care" · "the lawn prepped for the season" |
| **Nature given intent, or the crew given mystic perception** | "We **read the sun**, drainage, and soil" | "We check sun exposure, drainage, and soil" |
| **Trade puns** | "**Rooted** in West Essex" (landscaping) · "built to outlast the mortgage" | "In West Essex since 2004" |
| **Winking at the reader** | "Three steps, **no mystery**." | "How it works." |
| **Coy tails** — a clause whose only job is the wink | "A lawn that looks handled, **because it is**." | "Weekly service on a set schedule." |
| **Jokes about the work** | "so it never piles up past the **point of no return**" · "a mess and a deadline" | "so leaves don't pile up" |
| **Folksy labels** | "From the neighbors" (over reviews) | "Customer reviews" |
| **Self-announced virtue** — claiming the trait instead of showing it | "We'll tell you **honestly** what your beds need." · "**No pressure and no upsell.**" | Delete it. Every contractor claims this, so it persuades nobody. State a fact — "Free on-site estimate, usually within 48 hours" — and let it stand alone. |
| **"Actually" as a wink** — implying a rival who gets it wrong | "Designed for the yard you **actually** have." · "the route you **actually** walk to the door" | "Designed for your lot." · "cut and set along the main approach to the door" |
| **Body restating its own heading** | Heading "Seat walls & fire pits" over body "Built-in seat walls and fire pits, laid in matching stone." | The heading already named it. The body carries only what the heading doesn't: "Laid in matching stone." |
| **Absolute overclaims** | "so water pressure **never** pushes them out" | "so water pressure doesn't push them out." No contractor puts *never* in writing about a retaining wall. |

### The line between warm and cute

Warm is fine. Warm is "Give us a call — if we can help, we'll tell you straight." That's a
person talking. Cute is the writer being visible: a pun, a wink, a joke, a plant with
feelings. **If the sentence makes the reader notice the writing, cut it.**

### Register test

Read the sentence out loud in the owner's voice, standing at the truck, talking to a
customer. If it would sound strange coming out of their mouth, it is wrong for their
site — even if it is good writing.

---

## Tier 2 — Professional office (CPA, attorney, dentist, insurance, medical)

Everything in Tier 1 stays banned, with these adjustments:

- Slightly longer sentences are fine; contractions still required.
- Credentials, years, and numbers do the persuading: "CPA since 1983", "IRS
  representation", "same-day crowns". No adjective does work a number can do.
- Additionally banned: `boutique`, `white-glove`, `trusted advisor`, `tailored
  solutions`, `client-centric`, `personalized approach`.
- Still allowed here and nowhere else: "we", "our practice", modest formality in an
  attorney/medical bio.

---

## Tier 3 — Hospitality / premium (restaurant, spa, salon, event venue)

The only tier where sensory language is allowed, and only in two places:

1. **Item descriptions** — concrete and specific, the way a menu reads:
   "Roasted veal marrow, shallot gremolata, toasted sourdough." Nouns, not adjectives.
2. **The one quarantined owner block** — see SKILL.md. First person, attributed, built
   from something the owner actually said.

Everything else on the page still follows Tier 1. `elevate`, `curated`, `bespoke`,
`journey`, and `passion` stay banned in all three tiers — they are agency filler in
every register.

---

## Exempt from every rule on this page

- **Real review quotes.** Verbatim, always. A customer who wrote "meticulous" in a Yelp
  review stays "meticulous". Never edit a real quote to pass a check.
- **Q14 keep-word-for-word content** from `client-answers.md`.
- **Legal text, NAP (name/address/phone), license and insurance numbers, hours.**
- **Words the client used themselves** in their questionnaire answers. If the owner
  says "we take pride in a clean edge", "pride" is theirs to use. Record it in the
  sounds-like bank in `voice-spec.md` so the critic knows it was deliberate.
