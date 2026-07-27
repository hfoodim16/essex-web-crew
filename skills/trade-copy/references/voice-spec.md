# Stage A — building the voice spec

Written by the Planner, before the plan's hero direction. Output:
`prospects/<slug>/voice-spec.md`, one page. Everything the Builder needs to know about
how this client sounds, so it never has to be improvised while writing HTML.

Read `client-answers.md` twice. The first read is for what they said. **The second read
is for how they said it** — that's the part that becomes the voice.

## What to mine

| Signal | Where | What it decides |
|---|---|---|
| Three words for how it should come across | Q15 | The register keywords. Top authority — if they said "no-nonsense", every poetic line is wrong by their own instruction. |
| How they talk with customers | Q15b (optional) | The formality ceiling, and anything they've told you never to say. |
| Their story, their differentiator, the questions customers ask | Q2, Q3, Q26 | The **sounds-like bank** — 3 to 6 phrases in their own words, quoted verbatim into the spec. Q26 gives you FAQ headings in the customer's actual language. |
| The way the answers are written | whole document | Fragments or full sentences? Contractions? All lowercase? Trade slang? Match it. A client who writes "yeah we do mostly repairs, some new installs" should not get a site that says "We specialize in comprehensive installation services." |
| Must-keep-word-for-word content | Q14 | The protected list. Exempt from every check; never edited. |
| Preferred contact method | Q23 | The CTA verb. They said call → "Call Mike." They said form → "Send a message." Don't offer four ways when they named one. |
| What they don't want on the site | Q28 | Site-specific bans. |
| Services, phasing-out, specials | Q8, Q9, Q10, Q11 | The fact inventory — what body copy is allowed to be *about*. |
| Licenses, certifications, awards | Q22 | Facts that replace adjectives. "Licensed and insured, NJ HIC #13VH…" does the work "quality workmanship" pretends to do. |
| Trade type | dossier | The register preset below. |
| Old site's overused words | `site-content.md` | The motif watch-list. If their old copy leans on a word, the new copy must not inherit it. |

**Thin answers are normal.** The questionnaire tells clients to skip freely. If Q15 is
blank, take the register from the trade preset and the way they wrote whatever they did
answer. **The spec still gets written** — a sparse spec beats no spec, because the
Builder's fallback without one is literary filler.

## Register presets

Pick by trade, then bend it toward the Q15 words.

| Preset | Who | How it sounds |
|---|---|---|
| **Trade / blue collar** | landscaper, mason, tree service, transmission shop, HVAC, roofer, plumber | Short declaratives. Spec-style labels over sentences. Contractions everywhere. Prices, towns, and materials do the persuading. Banlist Tier 1 in full. |
| **Professional office** | CPA, attorney, dentist, insurance, medical | Plain but composed. Still contracted, still concrete. Credentials, years, and process do the persuading. Banlist Tier 2. |
| **Hospitality / premium** | restaurant, spa, salon, venue | The only preset allowing sensory language, and only in item descriptions and the one quarantined owner block. Everything else is Tier 1. Banlist Tier 3. |

## The artifact

Write `prospects/<slug>/voice-spec.md` in this shape. Keep it to one page — the Builder
reads this every time it writes a line.

```markdown
# Voice spec — <Business>

**Register:** <preset> | Q15 words: "<their three words>"
**Say-aloud persona:** Would <owner first name> say this to a customer at the counter?

## Sounds like them (verbatim from their answers)
- "<phrase from Q2/Q3/Q26>"
- "<phrase>"
- "<phrase>"
Use these. Getting one of their own sentences onto their homepage beats anything
composed for them.

## How they write
<One line: fragments vs sentences, contractions, formality ceiling, any slang.>

## Word budgets
| Slot | Words |
|---|---|
| Hero headline | 3–9 |
| Hero subhead | ≤ 30 |
| Service card | ≤ 30 |
| Service detail | ≤ 45 |
| About | ≤ 120, across 2–3 short paragraphs |
| FAQ answer | ≤ 40 |
<Adjust only where the content map demands it — a carried long-form article keeps
its length, because parity wins.>

## CTA
Primary: "<verb from Q23>" — plain, no wordplay.

## Watch list (on top of banlist Tier <n>)
- `<word their old site overuses>`
- `<word from Q28 they don't want>`
Cap: twice per page, each.

## Protected — never edited, exempt from checks
- Q14 word-for-word: <what>
- Real review quotes, license numbers, NAP, hours

## Lyrical block
<"Yes — first person, attributed to <owner>, built from their Q2 answer" OR
"None — they gave no material worth quoting. Every section stays plain.">

## Thin-fact sections (pre-authorized to be short)
- <section>: only <fact, fact>. Two lines maximum. Do not pad this.
- <section>: no material at all — cut it from the page.

## Hero uniqueness
Checked against other prospects' heroes: `grep -h -A2 '<h1' prospects/*/mockup/index.html`
Do not use: <constructions already in use — e.g. three-fragment "X. Y. Since <year>.">

## Settled — do not re-flag
- <line> — <who approved it, when, and why>
```

Keep the **Settled** list current and hand it to every reviewer and every cold read.
Without it each round re-argues lines the client already approved, and the client sees
churn instead of progress. Only a human decision belongs there — "I like it" from the
agent that wrote the line is not a settled decision.

## The thin-fact section is the important part

This is where bad copy actually comes from. If the Planner writes down *at plan time*
that the "Our Process" section has two real facts behind it, the Builder writes two
lines and moves on. If nobody writes it down, the Builder meets an empty section at
build time and fills it with atmosphere, because that is what an empty section asks for.

Deciding a section is thin is a valid plan outcome. Cutting it is better than shrinking
it. A page with six honest sections beats one with nine, three of which say nothing.
