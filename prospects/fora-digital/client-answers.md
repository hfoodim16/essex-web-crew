# Client answers — Fora Digital (our own agency site)

> **Run type:** B (Build & Perfect). The client is Harry himself — answers collected
> directly in conversation on 2026-07-22. No Run A, no scout/analyst.
> **These answers are the top authority.** Everything below is real, client-supplied
> fact. Do not embellish, invent, or "improve" any of it.

## The business

- **Name:** Fora Digital
- **Domain:** foradigital.com (emails below confirm it)
- **Who we are:** a two-person web agency — Harry Foodim and Corey Rapkin, co-owners.
- **Positioning / one-liner (client's words):** "Modern sites for local businesses"
- **Purpose of THIS site:** for potential clients to (1) look at our portfolio of past
  projects and (2) get a background on both of us. Portfolio + founders. That's the job.

## Contact (real — use exactly)

- Harry Foodim — **hfoodim@foradigital.com**
- Corey Rapkin — **crapkin@foradigital.com**
- No phone number, no street address supplied. **Do not invent either.** Contact section
  is the two emails only.

## Founder bios — VERBATIM FACTS, do not embellish

**Harry Foodim — Co-Owner**
- Co-Owner at Fora.
- Currently a sophomore at The Ohio State University, studying accounting.
- Graduated from West Essex High School.
- Loves playing sports, going to the gym, and spending time with family and friends.

**Corey Rapkin — Co-Owner**
- Co-Owner at Fora.
- Sophomore at the University of Georgia, studying accounting.

> **Honesty rule (hard):** these are real people. Write their bios from ONLY the facts
> above. No invented years of experience, no fabricated credentials, no made-up
> specialties ("Harry handles design, Corey handles clients" is NOT stated — do not
> assert it). You may write these facts in warm, well-crafted prose; you may not add
> new facts. If a layout wants a third bio line and there isn't one, change the layout.

## Headshots

- **Placeholder slots.** Styled frames (e.g. initials monogram) clearly designed for real
  photos to drop in later. **Never AI-generate faces of real people.**

## Portfolio — what to feature and how to label it

Honest labeling is mandatory. We have one real client; say so proudly, don't inflate it.

1. **Cecere Brothers Landscaping** — *real client work.* Label as a real client project.
   Source build: `~/Projects/cecere-test/` (screenshot provided in `assets-src/`).
2. **Corey Blake's Steakhouse** — *concept / sample build.* Must be labeled as a concept
   or sample, NOT presented as a paying client. Source: `~/Claude Code/corey-blakes-steakhouse/`
   (screenshot provided in `assets-src/`).
3. **1–2 empty "coming soon" slots** — Harry plans to add 1–2 more samples. Design real,
   styled placeholder cards that look intentional (e.g. "Next project — in progress").
   **Never fake a project, logo, client name, or screenshot to fill them.**

- **No fabricated testimonials, review counts, client counts, or stats.** We have one real
  client. No "50+ projects delivered." If a section needs social proof and we don't have
  it, cut the section.

## Imagery budget — ZERO

- **Generate no AI images for this build.** Portfolio images are real screenshots (already
  captured into `assets-src/`); headshots are placeholder frames. If you believe an image
  is needed, ask the lead — do not spend.

## Technical / structural notes

- Static mockup profile: `mockup/index.html` + `style.css` + `main.js`, opens by
  double-click, all assets local in `mockup/assets/` (never hotlink).
- Include `ProfessionalService` (or `Organization`) JSON-LD with the real business name
  and the two real emails. Omit address/phone entirely rather than using placeholder junk
  in structured data.
- Meta essentials: title, description, OG tags, favicon.
- Accessibility + reduced-motion gates on all animation, per the skill.
- Mandatory deliverable: desktop **and** 375px mobile screenshots into `screenshots/`.

## Anti-repetition — real bans (crew `design-memory.md`, last 3 signed-off)

Do NOT reuse from: **john-sessa-cpa** (Spectral / Public Sans · precision-professional
porcelain+ink-navy+manila+verdigris · sidebar-anchored letterhead), **cedar-grove-transmission**
(Archivo / Barlow · industrial graphite+steel+red · industrial spec-sheet + bento),
**happy-trees-by-mgm** (Zilla Slab / Work Sans · bark+moss+sky+hi-vis lime ·
canopy-descent full-bleed).

Motion wasn't recorded for those three, but **`fade-up` and number `count-up` are flagged
defaults** — pick a real signature move from `references/motion.md` instead.

## One judgement call for the planner

This is a **web agency** site. The category convention is dark/tech-slick/gradient. Per
`references/color-conventions.md`, make the honor-or-break call explicitly and say why —
and remember our clients are *local trade businesses*, so a site that alienates a
landscaper is the wrong answer even if it wins design points.
