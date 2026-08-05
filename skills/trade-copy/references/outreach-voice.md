# Outreach voice — email and call

**The crew never contacts anyone.** Every outreach artifact is a draft for Harry to
review and send or say himself. No agent in Team 1 or Team 2 produces these on its own
schedule — this file exists so that when Harry asks for outreach help, the voice is
already decided.

## The model this has to match

Ask-first. We do **not** build a site and pitch it. Harry finds a business, reaches out,
asks what they want (`templates/Website-Questionnaire.docx`), and builds from their
answers. So the hook is never "look what I made you" — it's "can I ask you a few
questions." Any draft that offers a finished mockup contradicts the business model.

## Who Harry is, for tone

A young web designer who builds fast, low-maintenance sites for local businesses in
Essex County — trades most often, but equally accountants, law offices, auto shops,
dentists. Real portfolio piece: **Cecere Brothers Landscaping**. Not a faceless agency:
a real person who looked at their business.

**Match the register to the reader.** A landscaper reading on a phone between jobs and a
CPA at a desk want the same honesty but not the same tone. Plain either way — but don't
write to a professional office like it's a job site.

## Principles

1. **Short.** 120–160 words. It's read on a phone, between other things.
2. **Lead with a specific, real observation** about their business — a service they're
   known for, their town, or exactly what's thin about their current web presence.
   Never open with "I hope this email finds you well."
3. **The ask is small.** A few questions about what they'd want, not a meeting, not a
   quote, not a sale. That's the whole conversion event.
4. **Kill the maintenance objection early.** Static site, nothing to break, cheap to
   keep online. This is the objection that stops these businesses, every time.
5. **One soft CTA.** "Worth a few minutes?" No pressure, no fake deadline, no "limited
   spots."
6. **Proof, lightly.** One line about the Cecere Brothers site. No exaggeration.
7. **Accurate.** Only facts from the dossier. No invented compliments or stats.
8. **The banlist applies here too — and now a script enforces it:**

```bash
python3 skills/trade-copy/scripts/copycheck.py prospects/<slug>/outreach-email.md --outreach
```

Run it on every draft before Harry sends it. The hero-length and placeholder checks are
skipped in this mode (a draft is supposed to carry `[Harry's phone]`); everything else —
banned phrases, banned words, em-dash rate, triads, paragraph length, contractions —
applies exactly as it does to a page.
 `references/banlist.md` — no "elevate your online
   presence", no "in today's digital landscape", no triads.

## Shape

```
Subject: <specific — their business name and one concrete thing>

Hi [owner name],

[One or two sentences: the specific real observation about their business or
current web presence.]

[The ask: you build sites for local businesses around here, and before designing
anything you'd rather hear what they'd want than guess. A few questions.]

[One line killing the maintenance objection.]

[Light proof: Cecere Brothers Landscaping.]

[Soft CTA — one question.]

Harry
[phone / link]
```

## Call script (when no email address exists)

Same voice, spoken. What changes:

- **Lines he can actually say.** Short spoken sentences, not paragraphs. He should be
  able to read one without sounding like he's reading.
- **Open with the specific observation**, same as the email: who he is, that he builds
  sites for local businesses, and the one real thing he noticed about theirs.
- **The soft ask is to send the questions**, not to sell on the call: "can I text or
  email you a few quick questions so you can look when you've got a minute?"
- **Prepared responses for the four things they'll say:** they're busy / what does it
  cost / we don't need one / yes, send it. Each gets a short, non-pushy reply.
- **Never:** reading the email aloud, assuming a yes, or pressure of any kind.

## Never

- No hard sell, fake urgency, or "act now."
- No claim the dossier doesn't support.
- No offering a finished site — that's the old model, and it's not what we do.
- No sending. Leave it as a draft with `[placeholders]` where Harry personalizes.

## A model email

Nothing in this file was demonstrated until now, and every draft on disk predates the
ask-first pivot. This is the shape, filled in — invented prospect, real structure.

> **Subject:** Cedar Grove Transmission — quick question about your website
>
> Hi Mike,
>
> I called about a transmission for my sister's Civic last month and ended up finding
> you through a Yelp listing — your own site 404s on the services page.
>
> I build websites for local shops around Essex County. Before I design anything I'd
> rather hear what you'd actually want on it than guess, so I put together a short list
> of questions — what work you want to come in more of, what people always call and ask,
> that kind of thing.
>
> It's a build-once site, not something you'd have to keep feeding. No monthly anything.
>
> I did one recently for Cecere Brothers Landscaping in Caldwell if you want to see the
> kind of thing I mean.
>
> Worth a ten-minute call this week?
>
> Harry
> [phone]

What it does: names a real specific observation (the 404) instead of a compliment, asks
before offering, kills the maintenance objection in one line, offers proof without
pitching, and ends on one question. **No mockup is offered** — see the hazard below.

### Subject lines

| Bad | Why | Good |
|---|---|---|
| Elevating Cedar Grove Transmission's online presence | Banlist verb, agency register, says nothing | Cedar Grove Transmission — quick question about your website |
| Your website — built and ready to see | Offers a speculative build (old model) | Quick question before I'd build anything |
| Transform your business with a modern website | Interchangeable; could be spam to anyone | Noticed your services page is down |

## ⚠ The drafts on disk are the OLD model

All six `prospects/*/outreach-email.md` drafts, and the one call script, **offer a
finished mockup** — "I went ahead and built you a mockup… It's done and ready to look
at." Three carry PASS audits, written before the pivot.

That contradicts the rule at the top of this file and the business model in `CLAUDE.md`:
we ask first and build from the answers. Each of those drafts now carries a SUPERSEDED
banner. **Rewrite to the shape above before sending any of them** — they are drafts
pending a send, not shipped work, so unlike a signed-off mockup they are not frozen.

Two also fail the gate: `anthonys-landscaping` (66-word paragraph, plus "outstanding
professional service" straight out of the banlist) and `gee-kay-landscaping` (63-word
paragraph).
