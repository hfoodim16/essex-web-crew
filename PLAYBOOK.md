# Harry's Playbook

> **`CLAUDE.md` is canonical.** Rules, checklists, and role/skill assignments are defined
> there. If this file disagrees with `CLAUDE.md`, `CLAUDE.md` wins — fix this file.

> **⚠️ The business model changed — read this first.** We work **ask-first**: find a
> business that could use a site → **you** reach out personally → anyone who says yes gets
> the master questionnaire → build FROM their answers → keep refining it with them. We do
> **not** build a site speculatively and pitch it.
>
> In practice there are **two independent teams with you in the middle**, and both prompts
> live in `KICKOFF.md`:
>
> 1. **Team 1 — Prospecting run** (`scout` + `analyst`). Ends at a shortlist of 3 real
>    businesses **with their contact info**. Nothing is built, and there's no approval
>    pause — the shortlist *is* the output.
> 2. **You, between the teams — no agents at all.** You call or email them yourself, in
>    your own words. There are no drafted emails and no call scripts. Whoever's interested
>    gets **`templates/Website-Questionnaire.docx`** — a standing, ready-to-send questionnaire
>    that already sits in the repo. You collect their answers.
> 3. **Team 2 — Build run** (`planner` + `builder` + `critic`). You paste their answers in;
>    the team plans from them, builds, and audits. Then you review the finished site
>    **with the client** and iterate on their feedback.
>
> The nine steps below keep their original numbers, but since your outreach now happens
> *before* anything is built, the real order you walk them in is
> **1 → 2 → 3 → 4 → 8 → 5 → 6 → 7 → 9**. **Step 8 is the hinge:** it's where you make
> contact, send the questionnaire, kick off the Build run, and show the client the result.

> This playbook covers the **pitch phase** — from summoning the team to a client saying
> yes. For what happens *after* a yes (real content + photos, production build, buying the
> domain, going live, and maintenance), see **`FULL-PROCESS.md`**, which continues these
> same steps through Step 15.

Two scripts live in this file:

- **Script 1 — The Whole Run, In Plain English.** Read this top to bottom. It walks you
  from literally summoning the team to the absolute end — your outreach, the build,
  follow-up, closed prospect. No jargon.
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
| They're interested — what do I send them? | Script 2, Step 8A |
| Their questionnaire answers are in — now what? | Script 2, Step 8B |
| The client wants changes to the built site | Script 2, Step 8C |
| No reply / they said no | Script 2, Step 8D |
| Client's happy with the site | Script 2, Step 9A |
| No reply after a week | Script 2, Step 9B |
| Client said no | Script 2, Step 9C |
| All three prospects flopped | Script 2, Step 9D |
| How do I generate & place the images? | Part 3, Reference A |
| The client gave me info — where do I put it? | Part 3, Reference B |
| How do I make a small edit to a site? | Part 3, Reference C |
| How do I connect the contact form / booking? | Part 3, Reference D |

---

# Script 1 — The Whole Run, In Plain English

Read this once, start to finish, before your first run. It's the map. The detailed
"what if it's not good" branches live in Script 2, which uses these same nine steps.
Remember the real-time order: **1 → 2 → 3 → 4 → 8 → 5 → 6 → 7 → 9.**

**Step 1 — Summon the team.**
Open Terminal and run `~/Projects/essex-web-crew/run.sh`. That starts Claude Code inside
the project with agent teams turned on. You'll see a normal Claude prompt — nothing has
started yet. You're just sitting at the controls.

**Step 2 — Give the kickoff order.**
Open `KICKOFF.md`, copy the **Team 1 — Prospecting run** prompt, and paste it in. The lead
now builds the team: a scout that searches Essex County for businesses with weak or
missing websites, then an analyst that scores them and researches the best few. Only those
two run — nothing gets built in this run.

**Step 3 — Wait and watch.**
Press `Ctrl+T` to see the task list, and use the arrow keys to peek at what each
teammate is doing. Scouting plus scoring usually takes 15–30 minutes together. You don't
have to do anything during this stretch — let it cook.

**Step 4 — Read the shortlist (this is the run's final output).**
The analyst presents 3 businesses, each with how to reach them (phone, email, owner's
name), why they're winnable, the angle to lead with, and the recommended scope. Then the
run ends — there's nothing to approve, because nothing is being built yet. Pick who you're
going to contact and go to **Step 8**. (Don't like one of the three? Script 2, Step 4B
swaps it.)

**Step 5 — The team builds (this happens after Step 8).**
Once a client has answered the questionnaire, you paste the **Team 2 — Build run** prompt
from `KICKOFF.md` with their answers in it. The lead saves the answers to
`prospects/<slug>/client-answers.md`, the planner (Fable) designs the site **from those
answers**, one builder builds it, and the critic audits and keeps sending fixes back until
it's genuinely good. This is the longest stage — often 30+ minutes. When it passes, the
lead gives you a summary and the run is done.

**Step 6 — Review the website.**
The client now has a folder `prospects/<name>/`. Open its `mockup/index.html`
(double-click) and click through every page. This is your own pass before the client sees
it — you're checking it's good enough to put in front of them.

**Step 7 — Add the remaining images.**
Every slot the plan marked `GENERATE` already holds a **real AI-generated image** the
builder made (they're in `prospects/<slug>/mockup/assets/`). The remaining picture slots
are labeled placeholder boxes with a ready-to-use prompt baked in — those are where the
client's own job photos belong. If a slot really needs a generated image instead, you can
make one (Part 3, Reference A) — the build budget closed at sign-off, so that's your own
call and costs about $0.04–0.06 an image. Drop them in and check the site still looks
right. Then show it to the client (back at **Step 8C**).

**Step 8 — Reach out yourself, then run the build (the hinge — comes right after Step 4).**
The team never contacts anyone, and it no longer writes you anything to send. You take the
contact info from `prospects/<slug>/dossier.md` and reach out **in your own words** —
call or email, whichever suits that business. Anyone who's interested gets
**`templates/Website-Questionnaire.docx`** exactly as it is; it's already written and sitting
in the repo. When their answers come back you paste them into the **Team 2 — Build run**
prompt (that's **Step 5**), review the result yourself (**Steps 6–7**), then walk the
client through it and fix whatever they want changed.

**Step 9 — Follow up and close out.**
Log every call and email you send, follow up once after about a week of silence, and stop
after two touches. A client who's happy with their site becomes a real, paying client;
everything else you close out and learn from.

That's the entire lifecycle. Every "what if" is handled in Script 2 below, step for step.

---

# Script 2 — The Same Run, With the Branches

Same nine steps as Script 1, same numbers, walked in the same real-time order
(**1 → 2 → 3 → 4 → 8 → 5 → 6 → 7 → 9**). Steps 1, 2, 3, and 5 can't really go wrong, so
they're single. Steps 4, 6, 7, 8, 9 split into lettered branches — read the one that
matches your situation, do it, and it tells you the next step. No dead ends.

Every paste-able prompt works in a **fresh session**: run
`~/Projects/essex-web-crew/run.sh` and paste it. (If the original team session is still
open, you can paste there instead.)

---

### Step 1 — Summon the team

Open Terminal, run `~/Projects/essex-web-crew/run.sh`. → continue to **Step 2**.

### Step 2 — Give the kickoff order

Copy the **Team 1 — Prospecting run** prompt from `KICKOFF.md`, paste it to the lead.
→ continue to **Step 3**.

### Step 3 — Wait and watch

`Ctrl+T` for the task list; arrow keys to peek at each teammate. Scout + analyst take
15–30 min. → continue to **Step 4**.

---

### Step 4 — Read the shortlist (the Prospecting run's final output)

The analyst gives you 3 businesses with a pitch and contact info each, then the run ends.
Nothing is built, so there's nothing to approve — you're just deciding who to call.

- **Step 4A — you'd contact all 3.** → continue to **Step 8** (reach out).
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
  remains, spawn a scout (Sonnet) to find new ones first."* Once you're happy with the
  replacement, → continue to **Step 8**.

---

### Step 5 — The team builds (you trust the plan)

*(You arrive here from **Step 8B**, once a client has answered the questionnaire.)*

You've pasted the **Team 2 — Build run** prompt from `KICKOFF.md` with their answers in
it, so let the team run: planner (Fable) designs **from the client's answers**, ONE builder
(Opus) builds, critic (Opus) audits until it passes. You don't second-guess the design plan
here — you listen to Fable. Just wait for the lead's "signed off" summary. → continue to
**Step 6**.

---

### Step 6 — Review the website (your own pass, before the client sees it)

Open `prospects/<slug>/mockup/index.html`, click every page, narrow the window to phone
width, and skim `audit.md` (it now carries TWO scoreboards — the $10K Checklist 8/8 AND
the 10-dimension rubric with no dimension below 7 and boldness ≥ 8). Check that it uses
the client's real content and invents no facts, and specifically:
- **Testimonials are real** — every quote traces to an actual review in the dossier's
  "Real reviews" section, with a real reviewer name and platform. No dossier reviews
  should mean no testimonial section, never invented praise.
- **Their real logo is there** — if the business has one, it should be the actual logo in
  the header, not a text wordmark.
- **The facts are current** — e.g. if ownership changed, the site says so rather than
  repeating a stale directory listing.
- **Every `GENERATE` slot holds a real image**, not a placeholder box — the hero above all.
- **It matches what the client actually told you** — skim
  `prospects/<slug>/client-answers.md` against the site. Their answers outrank the dossier,
  their old site, and design instinct; an ignored answer is a fix-list item.
Gut check: **would you pay for this site?**

*(Leftover `[placeholder]` gaps — hours, exact towns, the owner's story — are fine at this
stage if the client skipped those questions. You fill them in as they come back to you;
see **Part 3, Reference B**.)*

- **Step 6A — you love it.** → continue to **Step 7**.
- **Step 6B — right direction, but has problems** (typos, a broken/ugly section, weak
  page, mobile issue). Write your complaints as a numbered list and paste:

  ```
  Read CLAUDE.md, prospects/<slug>/build-sheet.md, and .claude/agents/builder.md.
  Harry is explicitly reopening this signed-off mockup — the freeze rule permits
  this only on his say-so, so treat the fix list below as authorized.
  Spawn ONE builder (Opus) scoped ONLY to prospects/<slug>/mockup/ and
  prospects/<slug>/screenshots/. The build sheet is its spec — it does NOT read
  website-plan.md. Keep the existing design — do NOT redesign.
  Fix exactly this list:
  1. <problem>
  2. <problem>
  If any fix would change what the sheet specifies, stop and tell me — that is a
  planner change, not a builder change (Step 6C).
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
  should feel bright and trustworthy">. Harry is explicitly reopening this
  signed-off prospect — the freeze rule permits this only on his say-so.
  Spawn the planner (Fable, claude-fable-5) to REVISE website-plan.md AND regenerate
  prospects/<slug>/build-sheet.md and voice-spec.md to match — the sheet is the
  builder's only spec, so a revised plan without a revised sheet is a defect.
  Run plan-lint on both, show me the new plan, and wait for my OK. After my OK:
  a critic (Opus) reviews the sheet (B1b) and returns SHEET GO, then relay that GO
  to a builder (Opus) to rebuild prospects/<slug>/mockup/ from the SHEET with full
  QA and fresh screenshots, then the critic audits the build.
  ```

  When it's done, re-review. → then continue to **Step 7**.

---

### Step 7 — Add the real images

*(Full how-to, including how to generate the images: **Part 3, Reference A**.)*

List every image prompt in the mockup:

```bash
grep -rn "AI-IMAGE" prospects/<slug>/mockup/
```

Generate each image through `/generate` (Reference A), save them to
`prospects/<slug>/mockup/assets/`, then paste this to swap them in:

```
In prospects/<slug>/mockup/, I've added real images to the assets/ folder.
Harry is explicitly reopening this signed-off mockup to place them — the freeze rule
permits this only on his say-so, so treat this as authorized.
Replace each AI-IMAGE placeholder div with an <img> tag pointing at the matching file
(keep the aria-labels as alt text, add loading="lazy", keep aspect ratios consistent).
Change nothing else — this is a swap, not a revision.
Then open it in the browser pane, verify every section still looks right on desktop
and at 375px wide, and update prospects/<slug>/screenshots/.
Finally, remind me that the Claude Design copy is now stale and needs /design-push.
```

Re-open `index.html` yourself to confirm.

- **Step 7A — all images look good.** → go back to **Step 8C** and show the client.
- **Step 7B — one or two won't come out right.** Fine **for `PLACEHOLDER` slots only**:
  leave those as the styled placeholders (they're designed to look
  intentional), or ask a builder to reframe that section so it doesn't need the image.
  **Not fine for any `GENERATE` slot, the hero above all** — those must hold real images
  that pass the realism test (the critic already enforced this). If one of those looks
  wrong, send it back for ONE regeneration naming the flaw; if it fails again, escalate
  rather than shipping a placeholder there. → go back to **Step 8C**.

  *(The client's own job photos beat AI images anyway — question 11 of the questionnaire
  asks for them. Once they send some, swap them in: **FULL-PROCESS Step 11**.)*

---

### Step 8 — Reach out yourself, then run the build (the hinge — you get here from Step 4)

**No agent is involved in this step, and there is nothing waiting for you to send.** There
are no drafted emails and no call scripts anymore — you reach out in your own words.

**Before you dial or type:** open `prospects/<slug>/dossier.md` and take the contact block
(owner's name, phone, email) plus the one or two specifics that make this business winnable
— the angle the analyst wrote is there so you have something real to open with, not so you
can read it aloud. Then pick the channel that suits them: for trades, a call early in the
morning before the crews head out usually beats an email; for a professional office, email.
Things worth having in front of you either way: what's actually wrong with their current
site, that Cecere Brothers Landscaping is your reference, and that you want to hear what
*they* want before designing anything.

**Pre-contact checklist:** the name and number match the dossier and are spelled right ·
you can say in one sentence why you're calling THIS business · you're not promising a
finished site, you're offering to build one from their answers · you know where you'll log
it (below).

- **Step 8A — they're interested.** Send them **`templates/Website-Questionnaire.docx`** —
  as-is, no run needed, it's already written and sitting in the repo. Paste it into an
  email or text them the questions; if you're on the phone with a talker, just walk the
  questions yourself and type their answers as they go. Skipped questions are fine. Then
  wait for the answers. → **Step 8B** when they come back.
- **Step 8B — their answers are in.** Open `KICKOFF.md`, copy the **Team 2 — Build run**
  prompt, fill in the `CLIENT:` slug and paste their answers verbatim into the
  `THEIR ANSWERS TO THE QUESTIONNAIRE:` slot, however they gave them to you (email reply,
  your phone notes, a photo you typed up). The lead saves them to
  `prospects/<slug>/client-answers.md`, and from then on their answers outrank everything
  else. Update the log to `building`. → continue to **Step 5**, then **Step 6** and
  **Step 7**, then come back here at **8C**.
- **Step 8C — the site's built; show it to the client.** Walk them through it — screen
  share on a call is best, or drag `prospects/<slug>/mockup/` onto Netlify Drop
  (app.netlify.com/drop) for a link they can open on their phone (a `file://` path won't
  work for them). Write down every change they ask for, in their words. Then:
  - **They want changes** → paste the **Step 6B** fix-list prompt with their feedback as
    the numbered list (it's the authorized-reopen prompt — that's exactly what this is).
    Re-review at **Step 6**, then show them again. Repeat until they're happy; 1–2 rounds
    is normal.
  - **They're happy with it** → continue to **Step 9** (that's **Step 9A**).
- **Step 8D — no reply, or a no.** Nothing was built, so there's nothing to salvage —
  just log it. Silent after 5–7 days → **Step 9B** (one follow-up, max two touches).
  A clear no → **Step 9C** (closed).

**Log every touch in `pipeline/outreach-log.md`** — that file is yours, not the team's; you
keep it. One row per prospect, updated as it moves:

```markdown
| Prospect | Contacted | Channel | Status | Next action |
|---|---|---|---|---|
| anthonys-landscaping | 2026-07-20 | call (owner, Tony) | questionnaire sent | chase 7/27 |
| john-sessa-cpa | 2026-07-20 | email | waiting | follow up 7/27 |
```

Statuses worth using, in order: `waiting` → `followed up` → `questionnaire sent` →
`answers in` → `building` → `won` / `closed`. Once you're into the client phase
(FULL-PROCESS Steps 10–15) add `launched` when the real site goes live.

---

### Step 9 — Follow up and close out (repeat per business)

- **Step 9A — the client's happy with their site** (you got here from **Step 8C**). This
  is a sales conversation now. Selling points: built from their own answers, almost zero
  maintenance (static — no monthly fees), fast, looks expensive; Cecere Brothers
  Landscaping is your credibility anchor. On a verbal yes, turn the mockup into the real
  thing:

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

  Update the log to `won`. **The pitch phase is done — the client phase begins:
  continue to Step 10 in `FULL-PROCESS.md`** (real content + photos, production build,
  domain, go-live, handoff, maintenance).
- **Step 9B — no reply 5–7 days after you reached out.** ONE short follow-up, in your own
  words — same channel or a step down (called first? a text is fine). Something like:

  > Hi <name> — just floating this back up. Happy to put together a website for
  > <business> whenever you've got ten minutes to tell me what you'd want on it. If now's
  > not the right time, no worries at all. — Harry

  Update the log to `followed up`. If they reply → **Step 8A** (send the questionnaire) or
  **9C**. Still silent after another week → **Step 9C**. Never more than 2 touches.
- **Step 9C — not interested / closed.** Reply politely if they said no, update the log
  to `closed` (note the reason), and keep whatever exists — a dossier is reusable research,
  and a built site is portfolio material. If the reason is worth learning from ("we just
  paid for a site"), add a line to `pipeline/rubric.md`. **This business is done.**
- **Step 9D — all three flopped** (2 touches each, no bites). Tune the machine before
  the next run. Paste:

  ```
  Read CLAUDE.md, pipeline/rubric.md, pipeline/candidates.md, and
  pipeline/outreach-log.md. All 3 prospects got no traction when I reached out.
  What I observed: <no answer / "we're happy with Facebook" / wrong trade / etc.>.
  Propose concrete edits to the rubric (who we target and why they'd say yes),
  plus 2-3 alternative niches or towns to scout next. Wait for my approval, then
  apply them.
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

Every slot the plan marked `GENERATE` already contains a **real AI-generated image** (the
builder made them — they live in `mockup/assets/`). The site's whole media spend is capped
all-in at **$1.00, or $1.50 if it ships a video**, images included. Every `PLACEHOLDER`
slot is a labeled box with a written image prompt baked in (e.g. "wide drone shot of a
finished bluestone paver patio at golden hour") — those are where the client's own job
photos belong. List the remaining ones:

```bash
grep -rn "AI-IMAGE" prospects/<slug>/mockup/
```

**Generate the images** — two ways:

1. **Have Claude make them for you.** In a session, paste:
   ```
   Read prospects/<slug>/website-plan.md and note the imagery REGISTER it set
   (usually "proud contractor" — casual phone photo, natural light, honest framing).
   Then read prospects/<slug>/mockup/index.html, pull out every AI-IMAGE prompt, and
   use the /generate skill on nano-banana-2 (never the -lite draft tier) to generate
   each image in that SAME register so they match the ones already in assets/.
   Rules: no readable business name, lettering, signage, or logo in any image; a
   different property in each project photo; sized for where it sits on the page.
   Tell me the projected cost first (~$0.04 at 1K, ~$0.06 at 2K) and how much of this
   site's budget is already spent — $1.00 all-in with no video, $1.50 with one. Copy
   each result into prospects/<slug>/mockup/assets/ with clear filenames, then check
   each for AI tells (warped lines, stock-ad staging, shabby setting) before placing.
   ```
   **All generation goes through `/generate`** — it owns model choice, provider routing,
   and the API keys, so nothing asks you for one. Do not route image generation through
   `ai-multimodal`, and do not paste an API key anywhere.
2. **Use your own photos.** Real job photography from the client always beats a generated
   image — that is exactly what the placeholder slots are for. Drop the files into
   `prospects/<slug>/mockup/assets/` and skip generation entirely.

   Avoid making these in ChatGPT/Midjourney/DALL·E: they land outside the register the
   plan set, outside the spend ledger the critic audits, and with licence terms we have
   not checked for client work.

**Place them** — paste this and Claude swaps every placeholder for a real image:

```
In prospects/<slug>/mockup/, I've added real images to the assets/ folder.
Harry is explicitly reopening this signed-off mockup to place them — the freeze rule
permits this only on his say-so, so treat this as authorized. Change nothing else.
Replace each AI-IMAGE placeholder div with an <img> tag pointing at the matching file
(keep the aria-labels as alt text, add loading="lazy", keep aspect ratios consistent),
then open it and confirm every section still looks right on desktop and mobile.
Then remind me the Claude Design copy is stale and needs /design-push.
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
  the primary buttons a darker green. I'm explicitly reopening this signed-off mockup —
  the freeze rule permits that on my say-so. Change only what I named.
  Then show me how it looks, and remind me the Claude Design copy needs /design-push.
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
