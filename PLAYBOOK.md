# Harry's Playbook

Two scripts live in this file:

- **Script 1 — The Whole Run, In Plain English.** Read this top to bottom. It walks you
  from literally summoning the team to the absolute end — sent email, follow-up, closed
  prospect. No jargon.
- **Script 2 — The Same Run, With the "What If It's Not Perfect" Branches.** Exact same
  nine steps as Script 1, in the same order. The difference: at every step where things
  can go imperfect, it splits into simple lettered branches (Step 6A, 6B…) that tell you
  what to do — including the exact prompt to paste when something needs fixing.

### Quick reference — "something's off, where do I go?"

| Scenario | Go to |
|---|---|
| I don't like one of the top 3 businesses | Script 2, Step 4B |
| Website is close but needs fixes | Script 2, Step 6B |
| Website direction is totally wrong | Script 2, Step 6C |
| An AI image won't come out right | Script 2, Step 7B |
| Email needs small tweaks | Script 2, Step 8B |
| Email is generic / wrong voice / inaccurate | Script 2, Step 8C |
| Client replied — interested | Script 2, Step 9A |
| No reply after a week | Script 2, Step 9B |
| Client said no | Script 2, Step 9C |
| All three pitches flopped | Script 2, Step 9D |
| How do I generate & place the images? | Part 3, Reference A |
| The client gave me info — where do I put it? | Part 3, Reference B |
| How do I make a small edit to a site? | Part 3, Reference C |
| How do I connect the contact form / booking? | Part 3, Reference D |

---

# Script 1 — The Whole Run, In Plain English

Read this once, start to finish, before your first run. It's the map. The detailed
"what if it's not good" branches live in Script 2, which uses these same nine steps.

**Step 1 — Summon the team.**
Open Terminal and run `~/Projects/essex-web-crew/run.sh`. That starts Claude Code inside
the project with agent teams turned on. You'll see a normal Claude prompt — nothing has
started yet. You're just sitting at the controls.

**Step 2 — Give the kickoff order.**
Open `KICKOFF.md`, copy the **Full run** prompt, and paste it in. The lead now starts
building the team: first a scout that searches Essex County for businesses with weak or
missing websites, then an analyst that scores them and researches the best few.

**Step 3 — Wait and watch.**
Press `Ctrl+T` to see the task list, and use the arrow keys to peek at what each
teammate is doing. Scouting plus scoring usually takes 15–30 minutes together. You don't
have to do anything during this stretch — let it cook.

**Step 4 — Approve the shortlist (the team stops here for you).**
The analyst presents 3 businesses, each with a short pitch: why they're winnable, what
the pitch would lead with, and how many pages the site needs. Read them. Reply to
approve all 3, or tell it to swap any you don't like. **Nothing gets built until you
say go.**

**Step 5 — The team builds.**
Once you approve: the planner (Fable) designs each website, three builders each build
one, the copywriter drafts your outreach emails, and the critic audits everything and
keeps sending fixes back until it's genuinely good. This is the longest stage — often
30+ minutes. When every package passes, the lead gives you a summary and the run is done.

**Step 6 — Review the websites.**
Each business now has a folder `prospects/<name>/`. Open its `mockup/index.html`
(double-click) and click through every page. This is where you decide if the site is
good enough to pitch.

**Step 7 — Add the real images.**
The mockups use labeled placeholder boxes instead of real pictures (the team never
generates images). Each box contains a ready-to-use image prompt. Generate the images
with your tool of choice, drop them in, and check the site still looks right.

**Step 8 — Check the emails and send the pitches yourself.**
The team never contacts anyone — the emails are drafts for you. Read each one, fill in
the blanks, attach mockup screenshots (or host the site so they can click a live link),
and send from your own account.

**Step 9 — Follow up and close out.**
Log each email you send, follow up once after about a week of silence, and stop after
two touches. Interested replies turn into real client conversations; everything else
becomes portfolio material for the next pitch.

That's the entire lifecycle. Every "what if" is handled in Script 2 below, step for step.

---

# Script 2 — The Same Run, With the Branches

Same nine steps as Script 1, same order. Steps 1, 2, 3, and 5 can't really go wrong, so
they're single. Steps 4, 6, 7, 8, 9 split into lettered branches — read the one that
matches your situation, do it, and it tells you the next step. No dead ends.

Every paste-able prompt works in a **fresh session**: run
`~/Projects/essex-web-crew/run.sh` and paste it. (If the original team session is still
open, you can paste there instead.)

---

### Step 1 — Summon the team

Open Terminal, run `~/Projects/essex-web-crew/run.sh`. → continue to **Step 2**.

### Step 2 — Give the kickoff order

Copy the **Full run** prompt from `KICKOFF.md`, paste it to the lead. → continue to
**Step 3**.

### Step 3 — Wait and watch

`Ctrl+T` for the task list; arrow keys to peek at each teammate. Scout + analyst take
15–30 min. → continue to **Step 4**.

---

### Step 4 — Approve the shortlist

The analyst gives you 3 businesses with a pitch each. Read them and decide.

- **Step 4A — you like all 3.** Reply to approve them. → continue to **Step 5**.
- **Step 4B — you don't like one (or more).** Paste this to swap the weak one out:

  ```
  Read CLAUDE.md, .claude/agents/analyst.md, and pipeline/candidates.md. I don't
  want the prospect "<slug>" because: <your reason>. Spawn an analyst (Opus) to:
  delete prospects/<slug>/, pick the next-highest-scoring candidate in the
  "## Scoring" section of pipeline/candidates.md that isn't already in prospects/,
  re-verify it qualifies, research it, and write prospects/<new-slug>/dossier.md.
  If my reason is a targeting gap, add one line to pipeline/rubric.md so future
  runs filter it. Then present the replacement with a pitch and STOP for my OK.
  ```

  If the candidate list is empty, add this line to the prompt: *"If no good candidate
  remains, spawn a scout (Sonnet) to find new ones first."* Approve the replacement,
  then → continue to **Step 5**.

---

### Step 5 — The team builds (you trust the plan)

You approved the businesses, so let the team run: planner (Fable) designs, builders
(Opus) build, copywriter (Sonnet) drafts emails, critic (Opus) audits until it passes.
You don't second-guess the design plan here — you listen to Fable. Just wait for the
lead's "all packages signed off" summary. → continue to **Step 6**.

---

### Step 6 — Review the websites (repeat per business)

Open `prospects/<slug>/mockup/index.html`, click every page, narrow the window to phone
width, and skim `audit.md`. Check it uses the client's real content and invents no facts.
Gut check: **would you pay for this site?**

- **Step 6A — you love it.** → continue to **Step 7**.
- **Step 6B — right direction, but has problems** (typos, a broken/ugly section, weak
  page, mobile issue). Write your complaints as a numbered list and paste:

  ```
  Read CLAUDE.md, prospects/<slug>/website-plan.md, and .claude/agents/builder.md.
  Spawn ONE builder (Opus) scoped ONLY to prospects/<slug>/mockup/. Keep the
  existing design — do NOT redesign. Fix exactly this list:
  1. <problem>
  2. <problem>
  Re-run the desktop and mobile QA loops, update prospects/<slug>/screenshots/,
  then a critic (Opus) re-audits and updates prospects/<slug>/audit.md.
  ```

  When it's done, re-review. → then continue to **Step 7**.
- **Step 6C — wrong vibe entirely** (fonts/colors/whole feel miss the business). Design
  belongs to the planner, so fix the plan first. Paste:

  ```
  Read CLAUDE.md, prospects/<slug>/dossier.md, and prospects/<slug>/website-plan.md.
  The design direction is wrong for this business. My notes: <what's wrong + what
  you'd rather see, e.g. "too dark and moody for a friendly family lawn crew;
  should feel bright and trustworthy">. Spawn the planner (Fable, claude-fable-5)
  to REVISE website-plan.md, show me the new plan, and wait for my OK. After my OK:
  spawn a builder (Opus) to rebuild prospects/<slug>/mockup/ from it with full QA
  and fresh screenshots, then a critic (Opus) audits.
  ```

  When it's done, re-review. → then continue to **Step 7**.

---

### Step 7 — Add the real images (repeat per business)

*(Full how-to, including how to generate the images: **Part 3, Reference A**.)*

List every image prompt in the mockup:

```bash
grep -rn "AI-IMAGE" prospects/<slug>/mockup/
```

Generate each image with your tool of choice, save them to
`prospects/<slug>/mockup/images/`, then paste this to swap them in:

```
In prospects/<slug>/mockup/, I've added real images to the images/ folder. Replace
each AI-IMAGE placeholder div with an <img> tag pointing at the matching file (keep
the aria-labels as alt text, add loading="lazy", keep aspect ratios consistent).
Then open it in the browser pane, verify every section still looks right on desktop
and at 375px wide, and update prospects/<slug>/screenshots/.
```

Re-open `index.html` yourself to confirm.

- **Step 7A — all images look good.** → continue to **Step 8**.
- **Step 7B — one or two won't come out right.** Fine for a pitch: leave those as the
  styled placeholders (they're designed to look intentional), or ask a builder to reframe
  that section so it doesn't need the image. → continue to **Step 8**.

---

### Step 8 — Check the email and send (repeat per business)

Read `prospects/<slug>/outreach-email.md`. Does it open with a real, specific observation
about THEIR business? Is every claim true (matches the dossier)? Does it mention the
mockup and the Cecere Brothers reference? Does it sound like you?

- **Step 8A — it's good.** Run the pre-send checklist below, send it, → continue to
  **Step 9**.
- **Step 8B — small tweaks** (a word, a sentence). Just edit the file yourself — faster
  than an agent. Then pre-send checklist, send, → continue to **Step 9**.
- **Step 8C — off** (generic, AI-sounding, or a claim that's not in the dossier). Paste:

  ```
  Read CLAUDE.md, templates/email-voice.md, prospects/<slug>/dossier.md, and the
  current prospects/<slug>/outreach-email.md. Spawn a copywriter (Sonnet) to
  rewrite it. My notes: <what's wrong — e.g. "sounds like AI", "opener is generic,
  use the specific detail about X">. It must invoke the humanizer skill before
  finalizing, then a critic checks it against templates/package-checklist.md.
  ```

  Re-read it, then pre-send checklist, send, → continue to **Step 9**.

**Pre-send checklist** (before any send): contact matches the dossier and is spelled
right · every `[placeholder]` *in the email* filled in · mockup proof attached or linked
(screenshots are the easy default; for a live link, drag the `mockup/` folder onto Netlify
Drop at app.netlify.com/drop — a `file://` path won't work for them) · you read it once
out loud.

*(Leftover `[placeholder]` gaps inside the **website** — hours, exact towns, the owner's
story — are fine to pitch with; you fill those after the client answers. See **Part 3,
Reference B**.)*

Then log the send in `pipeline/outreach-log.md`:

```markdown
| Prospect | Sent | Channel | Status | Next action |
|---|---|---|---|---|
| anthonys-landscaping | 2026-07-20 | email | waiting | follow up 7/27 |
```

---

### Step 9 — Follow up and close out (repeat per business)

- **Step 9A — they're interested.** This is a sales conversation now. Get them on a
  call, walk them through the mockup, anchor credibility on the Cecere Brothers site.
  Selling points: built custom for them, almost zero maintenance (static — no monthly
  fees), fast, looks expensive. On a verbal yes, turn the mockup into the real thing:

  ```
  Read CLAUDE.md. <slug> said yes and is becoming a real client. Help me turn
  prospects/<slug>/mockup/ into a production site: final content pass with their
  confirmed info, real images everywhere, contact details wired in, favicon and
  meta checked, and a deployment plan (static hosting + their domain). List
  everything I still need from the client.
  ```

  Two things that production pass will need their own how-tos: **filling in the client's
  real info** (hours, towns, their story) → **Part 3, Reference B**; and **connecting the
  contact form / booking** → **Part 3, Reference D**.

  Update the log to `won`. **This business is done.**
- **Step 9B — no reply after 5–7 days.** Send ONE short follow-up:

  > Hi <name> — just floating this back up. The mockup I built for <business> is
  > still yours to look at whenever: <link/screenshots>. If now's not the right
  > time, no worries at all. — Harry

  Update the log to `followed up`. If they reply → **Step 9A** or **9C**. Still silent
  after another week → **Step 9C**. Never more than 2 touches.
- **Step 9C — not interested / closed.** Reply politely if they said no, update the log
  to `closed` (note the reason), and keep the mockup — it's portfolio material for the
  next pitch. If the reason is worth learning from ("we just paid for a site"), add a
  line to `pipeline/rubric.md`. **This business is done.**
- **Step 9D — all three flopped** (2 touches each, no bites). Tune the machine before
  the next run. Paste:

  ```
  Read CLAUDE.md, pipeline/rubric.md, templates/email-voice.md, and
  pipeline/outreach-log.md. All 3 pitches got no traction. What I observed: <no
  opens / "we're happy with Facebook" / wrong trade / etc.>. Propose concrete
  edits to the rubric (who we target) and the email voice guide (how we pitch),
  plus 2–3 alternative niches or towns. Wait for my approval, then apply them.
  ```

  Apply the edits, then start a fresh run → back to **Step 1**. **End.**

---

# Part 3 — Reference: The Hands-On Parts

The four things you actually do with your hands after a run. The golden rule for all of
them: **you never edit code — you tell Claude what you want in plain English and it edits
the files.** Every how-to below ends with a prompt you can copy, paste, and fill in.

For a small one-off edit you don't even need the agent team — just open a normal Claude
Code session inside the project (`cd ~/Projects/essex-web-crew && claude`) and talk to it.

---

### Reference A — Adding the real pictures

Every picture slot in a mockup is a labeled placeholder box with a written image prompt
baked in (e.g. "wide drone shot of a finished bluestone paver patio at golden hour").
List them all for a site:

```bash
grep -rn "AI-IMAGE" prospects/<slug>/mockup/
```

**Generate the images** — two ways:

1. **Have Claude make them for you.** In a session, paste:
   ```
   Read prospects/<slug>/mockup/index.html and pull out every AI-IMAGE prompt.
   Use the ai-multimodal skill to generate each image from its prompt, sized for
   where it sits on the page, and save them into prospects/<slug>/mockup/images/
   with clear filenames.
   ```
   (This uses Google's image generation under the hood — it may ask for a Gemini API
   key and can cost a little. If it can't run, use option 2.)
2. **Make them in your own tool** — ChatGPT/DALL·E, Midjourney, whatever you like. Copy
   each AI-IMAGE prompt in, download the result, and drop the files into
   `prospects/<slug>/mockup/images/`.

**Place them** — paste this and Claude swaps every placeholder for a real image:

```
In prospects/<slug>/mockup/, I've added real images to the images/ folder. Replace
each AI-IMAGE placeholder div with an <img> tag pointing at the matching file (keep
the aria-labels as alt text, add loading="lazy", keep aspect ratios consistent),
then open it and confirm every section still looks right on desktop and mobile.
```

(This is the deep version of Script 2, Step 7.)

---

### Reference B — Getting info from the client into the site

When the builders didn't know a real fact, they left a **bracketed gap** right in the
page — like `[Hours — placeholder]`, `[towns — placeholder]`, `[Insured — confirm]`, or
`[the family's story — collect from the owner]`. **Those brackets are your list of
questions to ask the client.** Here's the loop:

**1. Turn the gaps into a question sheet.** Paste:

```
Read prospects/<slug>/mockup/index.html and prospects/<slug>/dossier.md. List every
bracketed placeholder or "confirm" gap as a plain-English question I can ask the
client, and write them to prospects/<slug>/client-intake.md with a blank line under
each one for the answer.
```

**2. Ask the client and type the answers.** Call/text/email them, then open
`prospects/<slug>/client-intake.md` and type each answer under its question. **That file
is "where you type it."** No formatting needed — just plain answers.

**3. Have Claude put the answers into the site.** Paste:

```
Read prospects/<slug>/client-intake.md — I've filled in the client's real answers.
Put them into prospects/<slug>/mockup/index.html, replacing the matching bracketed
placeholders. Don't invent anything: if an answer is still blank, leave the
placeholder as-is. Then open the site and confirm it reads right.
```

Only real answers go in; anything the client didn't give you stays a placeholder. That
keeps the site honest (same rule the team follows).

---

### Reference C — Fixing or changing the site

You describe the change like you'd tell a designer; Claude makes it. Two sizes:

- **Small change** (reword the hero, darken a button, tighten spacing, reorder a
  section) — you don't need the whole team. Open a plain session in the folder and say it:
  ```
  In prospects/<slug>/mockup/, change the hero headline to "<new headline>" and make
  the primary buttons a darker green. Then show me how it looks.
  ```
- **Bigger change**:
  - A section is broken or looks cheap, but the overall design is right → use **Script 2,
    Step 6B** (fix list — keeps the design, builder repairs it).
  - The whole vibe/fonts/colors are wrong for the business → use **Script 2, Step 6C**
    (the planner redesigns first, then a builder rebuilds).

Rule of thumb: if you can describe it in one or two sentences, just ask a normal session
(the small-change path). If it needs real design judgment or a QA pass, use the Step 6
branches so the critic re-checks it.

---

### Reference D — The backend: contact form, quotes, reservations, map

**Do this only after a client says yes (Script 2, Step 9A).** While a site is still a
pitch, the contact form stays a harmless stub — no point paying for services for someone
who hasn't signed. The mockups are already built to plug into these; the form is disabled
on purpose until you wire it.

**Keep everything static + third-party.** These sites have no server of their own — that's
what makes them "build once, barely touch it." You never run a backend; you point the
site at services that handle it for you.

- **Contact form / "request a quote"** (what a landscaper or tree service actually needs):
  sign up for a no-server form service — **Formspree**, **Web3Forms**, or **Netlify
  Forms** (all have free tiers). Each gives you an endpoint; form submissions get emailed
  straight to the client. Then paste:
  ```
  In prospects/<slug>/mockup/, wire the contact form to my Formspree endpoint
  <paste URL>: set the form's action and method=POST, remove the disabled/"return
  false" demo stub, add whatever hidden fields the service needs, and show a
  thank-you message after submit. Then test that it validates required fields.
  ```
- **Simplest option of all:** if the client just wants the phone to ring, skip the form —
  a big "Call or text us" button (`tel:`) plus their number is genuinely zero-maintenance.
- **Reservations / booking:** trades rarely need true scheduling — "book us" is usually
  just "request an estimate," which is the contact form above. If a client genuinely takes
  appointments, embed **Calendly** or **Cal.com** (paste their embed snippet into the
  page). Still no server you maintain.
- **Map:** a Google Maps **embed** iframe (the basic embed needs no API key), or a static
  map image that links to directions.

The umbrella action is the Step 9A "turn the mockup into a production site" prompt — this
reference is the detail for the form/booking piece of it.
