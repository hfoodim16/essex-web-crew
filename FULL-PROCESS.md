# The Full Process — Demo to Delivered

> **⚠️ Ask-first model.** We find a business, send them the **10-question
> questionnaire**, build FROM their answers, and keep refining it with them. We never
> build a site speculatively and pitch it. So the early steps run as **Run A** (prospect
> + ask, *no mockup*), and the build happens in **Run B** — the "skip to planner" prompt
> in `KICKOFF.md` — once their answers come back. Everything from the client phase
> (Steps 10–15) onward is unchanged.

The whole journey in one place: from summoning the agent team, through the pitch, to a
**live website on the client's own domain**, and the light maintenance after. Same style
as the playbook — plain English, numbered steps in order, lettered branches when things
can go more than one way, and a paste-able prompt anywhere you'd otherwise touch code.

- **Steps 1–9 = the pitch phase.** Same as `PLAYBOOK.md` (Script 2). Summarized here so
  this doc stands alone; for the deep "what if it's not perfect" detail and the hands-on
  references (images, client info, edits, backend), see **`PLAYBOOK.md`**.
- **Steps 10–15 = the client phase.** New: closing the deal, collecting real content and
  photos, the production pass, buying the domain and going live, handoff, and maintenance.

**Golden rules the whole way:** you never hand-edit code (you paste prompts and Claude
does it) · the team never contacts a business (every send/call is you) · nothing about a
business gets invented — only real facts they give you (that includes reviews: every
testimonial must be a real one with a source, and if something changed, like ownership,
the site says so).

### Quick reference — jump to your step

| Where you are | Go to |
|---|---|
| Starting a fresh run | Step 1 |
| Don't like one of the top 3 | Step 4B |
| Website needs fixes / wrong vibe | Step 6B / 6C |
| Adding the images | Step 7 (how-to: PLAYBOOK Part 3, Ref A) |
| Sending the email | Step 8A–8C |
| No email — I have to call | Step 8D |
| They're interested | Step 9A → **Step 10** |
| No reply / they said no / all flopped | Step 9B / 9C / 9D |
| **Client said yes — now what?** | **Step 10** |
| Getting their info & photos | Step 11 (info how-to: PLAYBOOK Part 3, Ref B) |
| Building the real site | Step 12 |
| Buying the domain & going live | Step 13 |
| Launch checklist & handing it off | Step 14 |
| A client wants a change later | Step 15A |
| Wiring the contact form / booking | PLAYBOOK Part 3, Ref D |

---

# Part 1 — The Pitch Phase (Steps 1–9)

*(Condensed from `PLAYBOOK.md`. The branches and prompts here are the essentials; the
playbook has the full versions.)*

### Step 1 — Summon the team
Open Terminal, run `~/Projects/essex-web-crew/run.sh`. → **Step 2**.

### Step 2 — Give the kickoff order
Copy the **Full run** prompt from `KICKOFF.md`, paste it to the lead. → **Step 3**.

### Step 3 — Wait and watch
`Ctrl+T` for the task list. Scout + analyst take 15–30 min. → **Step 4**.

### Step 4 — Approve the shortlist
The analyst gives you 3 businesses with a pitch each.
- **4A — you like all 3.** Approve. → **Step 5**.
- **4B — you don't like one.** Paste the swap prompt (see PLAYBOOK Step 4B) to promote the
  next candidate, approve the replacement. → **Step 5**.

### Step 5 — The team builds (trust the plan)
Planner designs, builders build, copywriter drafts outreach, critic audits until it
passes. Wait for "all packages signed off." → **Step 6**.

### Step 6 — Review the websites (per business)
Open `prospects/<slug>/mockup/index.html`, click every page, check phone width and
`audit.md`. Gut check: **would you pay for this?**
- **6A — you love it.** → **Step 7**.
- **6B — needs fixes** (keep the design). Paste the fix-list prompt (PLAYBOOK Step 6B),
  re-review. → **Step 7**.
- **6C — wrong vibe** (redesign). Paste the planner-redesign prompt (PLAYBOOK Step 6C),
  re-review. → **Step 7**.

### Step 7 — Add the remaining images (per business)
The hero and one priority slot already hold real AI-generated images (in
`mockup/assets/`). List what's still a placeholder:
`grep -rn "AI-IMAGE" prospects/<slug>/mockup/`. Generate and place — full how-to in
**PLAYBOOK Part 3, Reference A** (match the register the plan set; no business names or
signage in generated images).
- **7A — all good.** → **Step 8**.
- **7B — one won't come out right.** For a SECONDARY slot, leave the styled placeholder or
  reframe the section. The hero and the other priority slot must stay real images — send
  those back for one regeneration instead.
  → **Step 8**.

*(The pitch mockup ships with exactly 2 real AI images plus labeled placeholders beyond —
that's the standard, not a shortfall. Leftover `[placeholder]` TEXT gaps are fine; you
finalize everything properly in Steps 11–12 once they're a paying client.)*

### Step 8 — Reach out (per business)
Check which file the copywriter wrote:
- `outreach-email.md` → an email. **8A** send as-is · **8B** small edits yourself ·
  **8C** off → rewrite prompt (PLAYBOOK Step 8C). Then send, log it. → **Step 9**.
- `outreach-call.md` → **8D**: no email was found, so it's a phone script. Read it, fill
  blanks, call at a smart time, use the "if they say…" answers. Log the call
  (Channel = phone). → **Step 9**.

### Step 9 — Follow up and close out (per business)
- **9A — they're interested.** Get them on a call, walk the mockup, anchor on Cecere
  Brothers. **This is where the pitch phase ends and the real work begins → continue to
  Step 10.**
- **9B — no reply after 5–7 days.** One short follow-up (call or text if you phoned). Reply
  → 9A/9C; still silent → 9C. Max 2 touches.
- **9C — not interested.** Log `closed`, keep the mockup as portfolio. Done.
- **9D — all three flopped.** Tune the rubric + voice (PLAYBOOK Step 9D), start fresh →
  **Step 1**.

---

# Part 2 — The Client Phase (Steps 10–15)

They said yes. Now you turn the demo into a real, live website they own — and keep it
running. This is where you actually get paid.

---

### Step 10 — Close the deal

A real conversation (call or in person). Walk them through the mockup live on your screen,
then agree the terms out loud and confirm them in a short text/email afterward:

- **Scope** — which pages, what's included, and how many revision rounds (1–2 is normal).
  Write it down so "can you also…" later is a clear yes/no.
- **Price & payment** — state your number plainly. Anchor the value: a custom site built
  for them, **no monthly fees** (unlike Wix/Squarespace subscriptions or agencies that
  charge $100+/mo), fast, and it makes them look established. A common structure is
  **half up front, half at launch**. *(Leave `[your price]` / `[deposit]` as your call —
  this doc doesn't set your rates.)*
- **What you need from them** — the two things that unblock everything: **answers to the
  open questions** (Step 11) and **photos of their work** (Step 11). Tell them the site
  can't go live until you have those.

Branches:
- **10A — verbal yes + deposit agreed.** → continue to **Step 11**.
- **10B — they're hesitant / "let me think."** Don't push. Drop back to the **Step 9B**
  follow-up rhythm (one nudge, max 2 touches). If they come back → Step 10 again.

---

### Step 11 — Collect the real content and photos

Now you fill in every real fact and swap in real pictures. Two tracks — do both.

**Track 1 — the written info.** Same loop as **PLAYBOOK Part 3, Reference B**:
1. Turn the site's bracketed gaps into a question sheet — paste:
   ```
   Read prospects/<slug>/mockup/index.html and prospects/<slug>/dossier.md. List every
   bracketed placeholder or "confirm" gap as a plain-English question for the client,
   and write them to prospects/<slug>/client-intake.md with a blank line under each.
   ```
2. Ask the client, type their answers into `client-intake.md`.
3. Apply them — paste:
   ```
   Read prospects/<slug>/client-intake.md — I've filled in the client's real answers.
   Put them into the site, replacing the matching bracketed placeholders. Don't invent
   anything; if an answer is blank, leave the placeholder. Then show me the result.
   ```

**Track 2 — the photos.** Real photos of their actual work beat AI images on a real site.
Ask for their best **10–20 job photos** (phone pictures are fine — before/afters, finished
patios, clean lawns, crew shots). Then:
- **11A — they sent photos.** Drop them in `prospects/<slug>/production/images/` (you make
  the `production/` copy in Step 12) and have Claude place + tidy them — paste:
  ```
  I've added the client's real photos to prospects/<slug>/production/images/. Crop and
  compress them for the web (use the media-processing skill), then place them: replace
  the AI-IMAGE placeholders with the best-fitting real photo in each slot, AND swap out
  the two AI-generated images in assets/ (hero + priority slot) wherever a client photo
  of their own work is genuinely better — real job photos beat AI on a live site. Keep
  alt text and
  aspect ratios. Show me before/after.
  ```
- **11B — they have no usable photos.** Generate final AI images the **Reference A** way
  for now, and note a real photo pass for later (offer to shoot a batch on your phone next
  time you meet, or schedule it post-launch). → either way, continue.

→ continue to **Step 12**.

---

### Step 12 — The production pass

Turn the approved demo into the real, final site. First make a clean production copy so
the pitch mockup stays intact for your portfolio, then finalize everything. Paste:

```
Read CLAUDE.md and prospects/<slug>/. Copy prospects/<slug>/mockup/ to
prospects/<slug>/production/ (keep the original mockup untouched). Then finalize the
production copy for a real launch:
- All the client's confirmed info is in (no leftover [placeholders] except ones we
  agreed to omit).
- Real images everywhere (client photos where we have them, final AI images otherwise).
- Favicon, <title>, meta description, and Open Graph/Twitter tags use the real business
  name, town, and a real description.
- Replace any demo embeds: wire the contact form to a real service and add the map
  (see below), or remove the block cleanly if we're not using it.
- Do a full desktop + mobile QA pass and save fresh screenshots to
  prospects/<slug>/production-screenshots/.
Then have a critic (Opus) audit the production site against BOTH scoreboards — the $10K
Checklist (8/8) AND the web-design-ultra 10-dimension rubric (no dimension below 7,
boldness >= 8) — plus the hard rules: real reviews only (every testimonial traces to a
real captured review), the client's real logo in place, current business facts, and
generated imagery passing the two-way realism test. Write it to
prospects/<slug>/production-audit.md. List anything still needed from the client.
```

Wire the **contact form** during this pass (this is the "backend") — full how-to in
**PLAYBOOK Part 3, Reference D**: sign up for **Formspree** / **Web3Forms** / **Netlify
Forms** (free), so form submissions email the client. Simplest option if they just want
calls: a big `tel:` "Call or text us" button — zero setup. Add a **Google Maps embed** for
their service area if it fits.

→ when the production site passes, continue to **Step 13**.

---

### Step 13 — Domain, hosting, and go-live

Getting it on the internet. Three pieces — the domain (their address), the host (where the
files live), and DNS (connecting the two). Keep it cheap and static; **the client should
own the domain.**

**A. The domain.**
- **13A — they already have a domain** (old site, or bought one): use it. You'll point its
  DNS at the new host in step C. Note if there's an **old site to retire** — don't cancel
  the old host until the new site is confirmed live.
- **13B — brand-new domain:** buy it under **the client's own account** so they own it
  (Cloudflare Registrar, Namecheap, or Porkbun — roughly $10–20/year). If you buy it for
  them, transfer it to them or at minimum keep the login theirs. Never trap a client on a
  domain only you control.

**B. The host (free, static).** Host on **Netlify** or **Cloudflare Pages** — both host
static sites free with automatic HTTPS. Easiest: drag the `production/` folder onto
**Netlify Drop** (app.netlify.com/drop) for an instant live URL, or connect it properly for
future updates. Ask Claude to prep it — paste:
```
Prep prospects/<slug>/production/ for deployment to Netlify (static site). Make sure all
asset paths are relative, add a netlify.toml if useful, confirm there's no build step,
and give me step-by-step instructions to deploy this folder and get a live URL.
```

**C. Point the domain at the host.** Once the site is live on a host URL, connect the real
domain. Paste:
```
My site is live on <host URL> and the client's domain is <domain>, registered at
<registrar>. Give me the exact DNS records to add (and which to remove), plus the
click-by-click path in <registrar>'s dashboard, to point <domain> at the site. Note how
long propagation takes and how I'll know it worked.
```
HTTPS turns on automatically on both hosts once DNS resolves.

→ when the real domain loads the site, continue to **Step 14**.

---

### Step 14 — Launch checklist and handoff

Prove it works, then hand the client something clean.

**Verify (do all of these on the real domain):**
- Loads on **your phone and a desktop**, every page and nav link works.
- **Submit the contact form yourself** — confirm the message actually lands in the
  client's inbox. (A form that looks fine but doesn't deliver is the #1 launch bug.)
- Images all load, nothing is a broken placeholder.
- Get it indexed by Google — paste:
  ```
  Generate a sitemap.xml for the production site and give me step-by-step instructions
  to add <domain> to Google Search Console and submit the sitemap.
  ```
- Have the client add the new site link to their **Google Business Profile** (huge for a
  local trade — it's where most of their customers actually find them).

**Hand off.** Give the client a plain one-pager so they know what they own — paste:
```
Write prospects/<slug>/client-handoff.md for the client in plain, non-technical language:
what they own (their domain + registrar login, the form service account), where the site
is hosted, their live URL, how to reach me for changes, and a short "what to expect"
(it's a fast static site with basically nothing to break). Keep it friendly and short.
```

Then: collect the **second payment**, ask for a **testimonial** (you'll use it like the
Cecere Brothers reference on future pitches), and ask **"who else do you know who needs
this?"** — referrals from a happy trade client are your best next lead. Mark the prospect
`launched` in `pipeline/outreach-log.md`.

→ continue to **Step 15**.

---

### Step 15 — Maintenance and aftercare

The honest pitch was "build once, barely touch it" — a static site has no plugins,
databases, or updates that rot, so almost nothing breaks on its own. Maintenance is just
the occasional content change, and each one is a quick Claude session + redeploy.

- **15A — client asks for a change** (new photos, a price or service update, a seasonal
  banner, a new testimonial). Paste:
  ```
  The client for <slug> wants this change to their live site: <describe it>. Edit
  prospects/<slug>/production/, keep the design consistent, then give me the deploy step
  to push it live and tell me how to verify it.
  ```
  Then redeploy and check the live URL. How you charge is your call — options: a small
  **per-change flat fee**, a low **annual care plan**, or **free tiny tweaks** to keep the
  relationship (and referrals) warm. *(Leave `[price]` as yours to set.)*
- **15B — they want something bigger later** (online booking, a whole new section, an
  e-commerce piece). That's a **new mini-project**, not maintenance — scope and price it
  separately. Booking/embeds: **PLAYBOOK Part 3, Reference D**. Bigger builds: run it
  through the planner→builder→critic loop like a fresh site.
- **15C — the site's just running.** Do a **quarterly check**: load the live site, submit
  the form to confirm it still delivers, and note the **domain renewal date** so it never
  lapses. A 5-minute ping keeps the client happy and the door open.

**Then close the loop:** a happy, launched client is your strongest asset — use their site
as the new portfolio piece, cash the referral, and point the machine at the next prospect
→ back to **Step 1**.
