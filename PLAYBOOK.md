# PLAYBOOK — Harry's Post-Run Script

> The team's job ends when 3 packages are on disk. **This is your script from that
> moment until the pitch is sent and tracked.** Start at Step 1 and go in order.
> Every step ends with outcomes — each outcome tells you exactly where to go next.
> Lettered steps (2b, 3b, …) are rework branches; they tell you where to rejoin.

All paste-able prompts below work in a **fresh session** — start one with
`~/Projects/essex-web-crew/run.sh` and paste. You don't need the original team
session to still be alive.

## Quick reference

| You're thinking… | Go to |
|---|---|
| "Did the run even finish?" | Step 1 |
| "Is this client actually worth pitching?" | Step 2 |
| "This client is bad / facts are wrong" | Step 2b |
| "I need a replacement prospect" | Step 2b (swap) / 2c (re-scout) |
| "Is the website good?" | Step 3 |
| "Website is close but has problems" | Step 3b |
| "Website is the wrong vibe entirely" | Step 3c |
| "Is the email good?" | Step 4 |
| "Email sounds like AI / is generic" | Step 4b |
| "Time to add real images" | Step 5 |
| "Ready to send" | Step 6 |
| "Sent — now what?" | Step 7 |
| "They replied!" | Step 7b |
| "No reply yet" | Step 7c |
| "All 3 flopped" | Step 7e |

---

## Step 1 — Confirm the run finished (2 min)

Check that each of the 3 `prospects/<slug>/` folders has all 6 artifacts:

```
dossier.md   website-plan.md   mockup/   screenshots/   outreach-email.md   audit.md
```

One command:

```bash
ls prospects/*/
```

**Outcome A — everything's there** → continue to **Step 2**.

**Outcome B — something's missing** → the pipeline didn't finish. Paste this in a
fresh session, then return to **Step 1** when it's done:

```
Read CLAUDE.md and the relevant files in .claude/agents/. The pipeline run left
prospects/<slug>/ incomplete: it is missing <list what's missing>. Spawn only the
teammates needed to finish those artifacts (planner for website-plan, builder for
mockup+screenshots, copywriter for the email, critic for the audit), following the
per-prospect output contract in CLAUDE.md. Do not redo work that already exists.
```

---

## Step 2 — Vet the client (per prospect, ~5 min each)

Do this step for **each prospect** before touching any websites. Read
`prospects/<slug>/dossier.md`, then spot-check the AI's claims yourself:

- Look up their Google Business / Facebook page. Real? Still operating?
- Open their current website (if the dossier says they have one). Is it really as
  weak as claimed?
- Is the phone/email in the dossier findable and plausible?
- Gut check: established business, obvious web gap, could actually pay for a site?

**Outcome A — good client** (facts check out, gap is real, they're reachable) →
continue to **Step 3** for this prospect.

**Outcome B — bad client** → go to **Step 2b**.

### Step 2b — Discard and swap a bad prospect

This covers both flavors of bad:
- **The AI got facts wrong** — business closed, site is actually fine, wrong
  contact info.
- **Facts are right but it's not winnable** — too small, brand new, wrong trade,
  clearly wouldn't pay.

Do both of these:

1. **If it was a judgment miss (not a fact error):** add one line to
   `pipeline/rubric.md` describing the disqualifying trait (e.g. "disqualify:
   businesses under 2 years old") so future runs filter it automatically.
2. **Swap in a replacement.** Paste this in a fresh session:

```
Read CLAUDE.md, .claude/agents/analyst.md, and pipeline/candidates.md. I rejected
the prospect "<slug>" because: <your reason>. Spawn an analyst (Opus) to: verify
that my reason is reflected accurately, delete prospects/<slug>/, pick the
next-highest-scoring candidate from the "## Scoring" section of
pipeline/candidates.md, re-verify it still qualifies, research it, and write
prospects/<new-slug>/dossier.md per the dossier spec. Then present it to me with
a winnability pitch and STOP — do not spawn a planner or builder until I approve.
```

**Outcome A — replacement approved** → run the rest of the pipeline for it (paste
below), then return to **Step 2** to vet nothing further — you already vetted it —
and go to **Step 3** when its package lands:

```
Read CLAUDE.md and all files in .claude/agents/. Prospect <new-slug> is approved
and has a dossier. Run stages 4–7 of the pipeline for it only: planner (Fable)
writes website-plan.md, builder (Opus) implements the mockup with screenshots,
copywriter (Sonnet) drafts outreach-email.md, critic (Opus) audits until sign-off.
```

**Outcome B — no good candidates left in the list** → go to **Step 2c**.

### Step 2c — Re-scout (candidate list exhausted)

Paste this in a fresh session, then return to **Step 2** when the new shortlist
arrives:

```
Read CLAUDE.md and .claude/agents/scout.md. The previous candidate list
(pipeline/candidates.md) is exhausted. Spawn a scout (Sonnet) to find 10–15 NEW
qualifying Essex County businesses — exclude every business already listed in
pipeline/candidates.md and prospects/. Adjust focus: <e.g. "try different towns"
or "try gutter cleaning and power washing">. Then spawn an analyst (Opus) to
score, research the top <N needed>, write dossiers, and present the shortlist.
STOP for my approval before any planner or builder is spawned.
```

---

## Step 3 — Review the website (per prospect, ~10 min each)

Open the mockup and actually use it:

```bash
open prospects/<slug>/mockup/index.html
```

- Click **every** nav link and page.
- Narrow the browser window to phone width (or open the screenshots in
  `prospects/<slug>/screenshots/`) — does mobile look *designed*, not shrunk?
- Skim `prospects/<slug>/audit.md` — did the critic pass it 8/8? Any noted exceptions?
- Check honesty: is the content **their real content** (from the dossier)? Any
  invented facts, fake reviews, made-up years in business? That's an automatic fix.
- Are all image slots labeled `AI-IMAGE` placeholder blocks (no stock photos)?

**Outcome A — love it** → continue to **Step 4** for this prospect.

**Outcome B — right direction, but has problems** (typos, a broken section, bad
spacing, one weak page, mobile issue) → go to **Step 3b**.

**Outcome C — wrong direction entirely** (fonts, colors, or overall vibe miss the
business) → go to **Step 3c**.

### Step 3b — Fix list (keep the design, fix the flaws)

Write your complaints as a numbered list, then paste this in a fresh session.
When the builder reports done, **return to Step 3** and re-review:

```
Read CLAUDE.md, prospects/<slug>/website-plan.md, and .claude/agents/builder.md.
Spawn one builder (Opus) scoped ONLY to prospects/<slug>/mockup/. Keep the
existing design direction — do NOT redesign. Fix exactly this list:
1. <problem 1>
2. <problem 2>
3. <problem 3>
Re-run the desktop and mobile QA loops from the Mockup Recipe, update the
screenshots in prospects/<slug>/screenshots/, then spawn a critic (Opus) to
re-audit against the $10K Checklist and update prospects/<slug>/audit.md.
```

### Step 3c — Wrong direction (redesign via the planner)

Design decisions belong to the **planner**, not the builder — never ask a builder
to re-decide the vibe. Describe what's wrong and what you want instead, paste this
in a fresh session, and when done **return to Step 3** to re-review:

```
Read CLAUDE.md, prospects/<slug>/dossier.md, and prospects/<slug>/website-plan.md.
The current design direction is wrong for this business. My notes: <what feels
wrong, and any direction you'd rather see — e.g. "too dark and luxury; this is a
friendly family lawn crew, should feel warm and approachable">. Spawn the planner
(Fable, claude-fable-5) to REVISE website-plan.md per my notes — new art
direction, fonts, palette as needed, keeping the page map unless my notes say
otherwise. Then spawn a builder (Opus) to re-implement prospects/<slug>/mockup/
from the revised plan with full desktop+mobile QA and fresh screenshots, and a
critic (Opus) to audit until sign-off.
```

---

## Step 4 — Review the email (per prospect, ~3 min each)

Read `prospects/<slug>/outreach-email.md`. Check:

- Does it open with a **real, specific observation** about *their* business?
- Is everything it claims actually in the dossier (no invented compliments/stats)?
- Does it mention the mockup and the Cecere Brothers portfolio piece?
- Would *you* say it out loud? Does it sound like a person, not a bot?

**Outcome A — good** → continue to **Step 5**.

**Outcome B — minor tweaks** (a phrase you'd change, a detail to add) → just edit
`outreach-email.md` yourself; it's faster than an agent round-trip. Then continue
to **Step 5**.

**Outcome C — wrong voice / generic / inaccurate** → go to **Step 4b**.

### Step 4b — Copywriter re-run

Paste this in a fresh session; when the redraft lands, **return to Step 4**:

```
Read CLAUDE.md, templates/email-voice.md, prospects/<slug>/dossier.md, and the
current prospects/<slug>/outreach-email.md. Spawn a copywriter (Sonnet) to
rewrite it. My notes: <what's wrong — e.g. "sounds like AI", "too salesy",
"the observation about their site is generic — use the specific detail about X
from the dossier">. The copywriter must invoke the humanizer skill before
finalizing, then a critic must check it against templates/package-checklist.md.
```

---

## Step 5 — Generate the real images (per prospect)

The mockup ships with labeled `AI-IMAGE` placeholders. List every prompt:

```bash
grep -rn "AI-IMAGE" prospects/<slug>/mockup/
```

1. Generate each image with your image tool of choice, following the prompt in
   the comment (they're written to match the art direction).
2. Save them to `prospects/<slug>/mockup/images/` with readable names.
3. Swap the placeholders for real `<img>` tags — easiest is to paste this in a
   session:

```
In prospects/<slug>/mockup/, I've added real images to the images/ folder.
Replace each AI-IMAGE placeholder div with an <img> tag pointing at the matching
file (keep the aria-labels as alt text, add loading="lazy", keep sizing/aspect
ratios consistent with the layout). Then open it in the browser pane and verify
every section still looks right on desktop and mobile, and update the screenshots
in prospects/<slug>/screenshots/.
```

4. Re-open `index.html` yourself and confirm it looks right.

**Outcome A — all images in, looks great** → continue to **Step 6**.

**Outcome B — one or two images won't come out right** → that's fine for a pitch:
either leave those as styled placeholders (they're designed to look intentional)
or ask for that section to be reframed around no image. Then continue to **Step 6**.

---

## Step 6 — Send the pitch (per prospect)

**You** send it — the team never contacts anyone.

Pre-send checklist:

- [ ] Contact (email/phone) matches the dossier and you've double-checked it.
- [ ] Owner/business name spelled correctly everywhere.
- [ ] Every `[placeholder]` in the email is filled in (your name, phone, etc.).
- [ ] You have the one-pager from `outreach-email.md` handy for a reply or call.
- [ ] The mockup is shareable — pick one:
  - **Screenshots attached** (default, zero setup) — use the best desktop + mobile
    shots from `screenshots/`.
  - **Screen-recorded scroll-through** (30s phone-and-desktop video, feels premium).
  - **Live link** — a `file://` path won't work for them; host it free instead
    (e.g. drag the `mockup/` folder onto Netlify Drop at app.netlify.com/drop)
    and send that URL.

Copy the email text into Gmail, attach/link the mockup, send.

**Outcome — sent** → continue to **Step 7**.

---

## Step 7 — Track and follow up

Log every send in `pipeline/outreach-log.md` (create it the first time):

```markdown
| Prospect | Sent | Channel | Status | Next action |
|---|---|---|---|---|
| anthonys-landscaping | 2026-07-20 | email | waiting | follow up 7/27 |
```

Then watch for replies:

**Outcome A — they're interested** → go to **Step 7b**.

**Outcome B — no reply yet** → go to **Step 7c**.

**Outcome C — not interested** → go to **Step 7d**.

**Outcome D — all 3 prospects flopped** (2 touches each, no bites) → go to **Step 7e**.

### Step 7b — Interested!

1. Get them on a call. Use the one-pager bullets; anchor credibility on the
   Cecere Brothers site.
2. Selling points for this kind of site: built custom for them, almost zero
   maintenance (static site — no monthly platform fees), fast, looks expensive.
3. Once there's a verbal yes, turn the mockup into the real deliverable — paste:

```
Read CLAUDE.md. <slug> said yes and is becoming a real client. Help me turn
prospects/<slug>/mockup/ into a production site: final content pass with the
client's confirmed info, real images everywhere, contact details wired in, favicon
and meta double-checked, and a deployment plan (static hosting options + connecting
their domain). List everything I still need to collect from the client.
```

Update the log. **Done — this one's a client.**

### Step 7c — No reply

Wait **5–7 days**, then send ONE short follow-up. Template:

```
Hi <name> — just floating this back up. The mockup I built for <business name>
is still yours to look at whenever: <link/screenshots attached>. If now's not
the right time, no worries at all. — Harry
```

**Outcome A — they reply** → **Step 7b** (interested) or **Step 7d** (pass).

**Outcome B — still nothing after the follow-up** → stop at 2 touches. Mark the
log `closed — no response` and go to **Step 7d**'s note about the portfolio.

### Step 7d — Not interested / closed

- Mark the log entry `closed`, with the reason if they gave one.
- **Keep the mockup** — it's now a portfolio piece. A closed pitch for a
  landscaper still proves what you can do for the next landscaper.
- If they gave a reason worth learning from ("we just paid for a site", "too
  busy"), add a line to `pipeline/rubric.md` so scouting improves.

### Step 7e — All 3 flopped: retro and rerun

Before burning another run, make the next one smarter. Paste:

```
Read CLAUDE.md, pipeline/rubric.md, templates/email-voice.md, and
pipeline/outreach-log.md. All three outreach attempts failed: <what happened —
no responses / "already have a site" / wrong trade>. Help me run a retro:
propose concrete edits to the rubric (better targeting) and the email voice
guide (better hook), and suggest 2–3 alternative niches or towns. Don't spawn
any teammates yet — we'll adjust first, then kick off a fresh run.
```

Apply the edits, then start a fresh run from `KICKOFF.md` → you're back at
**Step 1** when it finishes.
