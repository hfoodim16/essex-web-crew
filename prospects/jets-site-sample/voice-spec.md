# Voice spec — New York Jets (jets-site-sample)

**Register:** Professional / organizational (banlist Tier 2) | Q15 words: "Professional, athletic, and large"
**Say-aloud persona:** Would the club's front office put this sentence in a press release —
and would the owner recognize his own words in the difference section? Q16 says customer
communication runs "through our support team" — so the site voice is a buttoned-up
organization, NOT a chatty owner. The ONE exception is the difference/owner block, which
is the owner talking plainly (see Lyrical block).

## Sounds like them (verbatim from their answers)
- "As a kid I always wanted to own an NFL team. After working in finance, I had the money to finally fulfill that goal." (Q2)
- "I am willing to eat losses in order for the team to be better." (Q3)
- "Wherever the fans are" (Q4)
- "My best customers are season-ticket holders. Families that have supported the team for years." (Q6)
- "Serving the fans what they cheer for" (Q9)
- "Super bowl winner 1969" (Q23 — render as "Super Bowl winner, 1969")

Use these. Getting the owner's own sentences onto the page beats anything composed.

## How they write
Short, plain, first-person, confident. Full sentences, no slang, no hype vocabulary.
The organizational sections stay composed and third-person ("the club", "the team");
only the owner block is "I".

## Word budgets
| Slot | Words |
|---|---|
| Hero headline | 3–8 |
| Hero subhead | ≤ 25 |
| Ticket package card | ≤ 20 |
| Section intro (players / charity / inside the club) | ≤ 20–25 |
| Story / about | ≤ 90, 2 short paragraphs |
| Owner quote block | verbatim Q2/Q3 only — no embellishment |
| CTA band | ≤ 15 |

## CTA
Primary, everywhere, one intent: **"Get Tickets"** → `href="PLACEHOLDER_TICKET_URL"`
(Q24: "Go to ticketmaster"). No form, no "contact us" second intent. Ticketmaster and
StubHub may be named in ticket-section support copy (Q7 — the client named them).

## Watch list (on top of banlist Tier 2)
- **Hard bans (Q10 + lead's notes):** negative media of any kind; past coaches; ANY coach
  or player name; stats, scores, schedules, standings; charity program names; invented
  prices, dates, seat maps, phone numbers, addresses, emails, hours.
- **Banned sports-slop vocabulary:** legacy, dynasty, gridiron, glory, faithful, diehard,
  "bleed green", roar, electric, unstoppable, relentless, "gang" anything.
- **"Best team in the NFL"** (Q5) is a directive about how the site should LOOK — never
  print it as a claim.
- **Watch:** "fans" (unavoidable, but cap ~4 uses per page and vary with "season-ticket
  holders", "families"); "green and white" (motif risk — hero + heritage band + footer
  maximum, 3 uses).
- Numbers allowed on the page: **56 years, 1969, 3 games, full season.** Nothing else
  exists — do not invent one to fill a shape.

## Protected — never edited, exempt from checks
- The six verbatim phrases above when quoted as the owner's words.
- All `PLACEHOLDER_…` tokens (must match JSON-LD exactly).
- No Q14 content (blank). No real reviews exist (Q22 blank) — none may be written.

## Lyrical block
**Yes — one.** First person, built ONLY from the Q2 + Q3 verbatim answers, attributed
"— Team Owner, New York Jets" (the client gave no name — do NOT invent one; leave an
HTML comment for Harry to add the attribution name). Everywhere else stays plain.

## Thin-fact sections (pre-authorized to be SHORT — do not pad)
Nearly every section here is thin. That is the plan, not a problem:
- **Tickets:** only 4 facts — pre-season tickets, free training-camp access, 3-game
  package, full-season package. Three cards + one highlight line. No prices, no dates.
- **Story:** only 56 years + the finance-to-ownership story + Super Bowl 1969. ≤ 90 words.
- **Players showcase:** NO material (no names allowed). Intro ≤ 20 words + labeled
  placeholder tiles. Nothing else.
- **Charity:** NO material (no program names given). Intro ≤ 20 words + one labeled
  placeholder block.
- **Inside the club (locker room / training facility):** photos don't exist yet (Q21).
  Two labeled placeholders + captions ≤ 12 words each.
- **Contact:** no phone/email/hours/address. Ticket CTA + "Ticket questions go through
  the ticket team." + placeholder tokens. Two lines maximum.
- **FAQ:** Q27 blank — CUT from the page.
- **Testimonials:** Q22 blank — CUT from the page (no invented praise, no empty-review
  block needed; the layout doesn't require one).

## Hero uniqueness
Checked against `prospects/*/mockup/index.html` heroes. Do NOT use: the three-fragment
triad ("Fair. Honest. Since 1961." — cedar-grove owns it), "Built …" openers (two
exist), "Your dream …, N years in the making" (anthonys owns it), "Since <year>" as the
headline. Recommended construction: build the headline from the client's own Q4/Q18
words — e.g. "Green and white, wherever the fans are." (8 words, verbatim bank, no
triad). Builder may tighten but must stay inside the bank + budgets.

## Settled — do not re-flag
- "56 years" is the client's own figure and is used as given (lead's note 7 — the
  franchise-founding discrepancy is a "Confirm with client (optional)" item for Harry,
  never a `[verify]` blocker on the page).
- "Super bowl winner 1969" is a client-given fact; rendered "Super Bowl winner, 1969".
