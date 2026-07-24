# Package Sign-Off Checklist (Critic's gate)

A client's package ships only when the built site passes every gate below. The Critic records the result in `prospects/<slug>/audit.md` **every review
round** (NEEDS-WORK rounds included, with a `Review round: N` line), carrying BOTH
scoreboards below.

## Mockup, scoreboard 1 — the $10K Checklist (score all 8)

1. [ ] **Point of view** — commits to a named art direction that fits the business; not a template.
2. [ ] **Typography** — paired display + body Google Fonts; NEVER Inter, Roboto, Arial, or Helvetica; hierarchy via scale/weight.
3. [ ] **Restrained color** — 3–5 colors as tokens, used consistently.
4. [ ] **Hierarchy breathes** — clear primary/secondary/tertiary; whitespace does work.
5. [ ] **Imagery with intent** — the **2 Planner-marked `GENERATE` slots (hero + one priority slot) hold REAL generated images** stored locally as WebP in `mockup/assets/` and passing the two-way realism test below; **every other slot is a labeled `AI-IMAGE` placeholder** in the art direction's style. More than 2 generated images = budget fail. NO stock/hotlinked/copyrighted images.
6. [ ] **Motion whispers** — hand-crafted micro-interactions; ALL gated behind `prefers-reduced-motion`.
7. [ ] **Mobile designed, not shrunk** — distinct phone layout decisions, PROVEN by mobile screenshots.
8. [ ] **Invisible expensive stuff** — sub-2s load (no huge assets), WCAG AA contrast, keyboard nav / focus ring, semantic HTML, real meta+OG+favicon.

**Pass = 8/8**, or a documented, defensible exception written into `audit.md`.
**Never exceptable:** a placeholder sitting in either of the 2 priority image slots.

## Mockup, scoreboard 2 — the web-design-ultra 10-dimension rubric

Score all 10 from the screenshots per
`~/.claude/skills/web-design-ultra/references/critique.md`: boldness/distinctiveness,
visual hierarchy, typography craft, color & contrast, spacing rhythm, background/depth,
imagery quality, responsiveness, motion polish, cohesion.

- [ ] **No dimension below 7.**
- [ ] **Boldness ≥ 8.**
- [ ] For a redesign of an existing site: the **bold test** passes (obviously different at a glance).

## Generated-imagery realism — the two-way test

*Would the business proudly put this on their own website — AND would a visitor believe
they took it themselves?* Both halves must hold. Open each generated image full size.

- [ ] No **rendering tells** — warped straight lines (fences, pavers, window frames), melted/duplicated detail, unnaturally repeating texture.
- [ ] Not **"too perfect"** — magazine/stock-ad staging fails even if technically flawless.
- [ ] Not **"too shabby"** — run-down setting, mess implying sloppy work, dreary light, crooked framing.
- [ ] **No fabricated branding** — no readable business name, lettering, signage, or logo inside a generated image (automatic fail). The client's REAL logo composited into the markup is correct.
- [ ] **Distinct property per project photo** — no same-house gallery.
- [ ] **One register site-wide** — no casual phone shot beside a glossy editorial shot.
- [ ] Correct fit — right resolution for the slot, WebP, scrim under any text over a photo.

## Local-service conversion checklist

- [ ] **Tap-to-call** — real `tel:` link visible in the mobile header; CTA repeated top / mid / footer.
- [ ] One plain primary action ("Get a free estimate"), not clever wordplay.
- [ ] Service-area block with real town names.
- [ ] Trust strip — years / license / insured / rating (real values or clearly labeled placeholders).
- [ ] Project or before/after gallery present.
- [ ] Estimate form ≤ 4 fields, phone-first.
- [ ] Consistent NAP footer matching the dossier.

## Hard rules (any failure blocks sign-off)

- [ ] **Images** — exactly 2 locally-stored generated images; every other slot a labeled placeholder; the client's real logo served as a LOCAL file. No stock, hotlinked, or copyrighted images anywhere.
- [ ] **Real logo present** — if the dossier has a `**Logo:**` URL, the actual file is in `mockup/assets/` and renders in the header (local `src`, not hotlinked, not a substituted text wordmark).
- [ ] **Real reviews only** — every testimonial traces to a real review in the dossier's "Real reviews" section (same quote, reviewer, platform). No dossier reviews → no testimonial section, or a clearly labeled placeholder. Invented praise = automatic fail.
- [ ] **Current facts, not stale** — the mockup reflects business-announced changes (owner, name, address); no outdated version presented as current.
- [ ] No fabricated facts about the business.
- [ ] **Uses the client's real content** — if they had an existing site, its actual
      services/copy/contact/hours/testimonials were reused (not invented); only genuinely
      missing info is a `[placeholder]`.
- [ ] **CONTENT PARITY** — *the new site never knows less than the old site.* Walk
      `site-content.md` block by block against the mockup: every block is present at full
      informational fidelity (descriptions as descriptions, articles as articles, full
      town lists) or on the plan's "Deliberately dropped" list with a reason. Missing or
      thinned-to-a-mention content = numbered fail list to the builder.
- [ ] **Every clickable works (click-tested in the browser, not inferred from code)** —
      hamburger opens AND closes (checked on a non-index page too for multi-page sites),
      every nav / card / CTA / footer link navigates, every `#fragment` target exists,
      and the form submit shows its inline demo confirmation. **No dead clicks and no
      misleading affordances** — if it looks clickable (hover lift, pointer cursor,
      cursor label, arrow, card styling), the whole element must work, not just a small
      inner link. Disabled grey submit buttons and silent dead clicks both fail.
- [ ] No outbound contact of any kind was performed.

## Package folder complete

**From the Prospecting team (may already exist, or be captured in the build run):**
- [ ] `dossier.md` (with page map + winnability pitch + contact info)
- [ ] `site-content.md` (full-text capture of the existing site — required whenever the
      client had one)

**The build itself:**
- [ ] `client-answers.md` (saved verbatim by the lead)
- [ ] `website-plan.md` (the Planner's design contract, incl. the **"Client answers →
      decisions"** section and the content map)
- [ ] `mockup/` (pages per the **plan's** page map, opens cleanly) incl. `assets/` (logo + 2 generated images)
- [ ] `screenshots/` (desktop + mobile)
- [ ] `release-form.pdf` — valid one-page PDF; no `{{` tokens left in its `.html`
      source; Client/Business, Contact Name and Pages Included filled; **Pages Included
      matches the pages actually built**; no invented domain/preview link (blank is
      correct); signature, date and checkbox fields left blank for the client.
- [ ] `audit.md` (BOTH scoreboards: $10K + 10-dimension rubric, with `Review round: N`)

## Before sign-off

- [ ] **Distinctiveness check vs. our recent work** — compare this mockup against the
      **last 3 `design-memory.md` rows** (and the most recent signed prospect's hero
      screenshot if it's on disk). Hunting the softer sameness the ban list misses:
      section rhythm, imagery register, motion vocabulary, a hero that's the same shot in
      different colors. Reads like a sibling of a recent build → back to the builder while
      it's still unsigned. Reading a frozen prospect's files is research, not a reopening.
- [ ] **`design-memory.md` row appended** on sign-off (date · slug · font pairing ·
      palette family · layout archetype · background system · signature motion).
