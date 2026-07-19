# Package Sign-Off Checklist (Critic's gate)

A prospect's package ships only when BOTH the mockup and the email pass. The Critic
records the mockup result in `prospects/<slug>/audit.md`.

## Mockup — the $10K Checklist (score all 8)

1. [ ] **Point of view** — commits to a named art direction that fits the trade; not a template.
2. [ ] **Typography** — paired display + body Google Fonts; NOT Inter or Roboto; hierarchy via scale/weight.
3. [ ] **Restrained color** — 3–5 colors as tokens, used consistently.
4. [ ] **Hierarchy breathes** — clear primary/secondary/tertiary; whitespace does work.
5. [ ] **Imagery with intent** — every image slot is a labeled `AI-IMAGE` placeholder in the art direction's style; NO stock/hotlinked/copyrighted images.
6. [ ] **Motion whispers** — hand-crafted micro-interactions; ALL gated behind `prefers-reduced-motion`.
7. [ ] **Mobile designed, not shrunk** — distinct phone layout decisions, PROVEN by mobile screenshots.
8. [ ] **Invisible expensive stuff** — sub-2s load (no huge assets), WCAG AA contrast, keyboard nav / focus ring, semantic HTML, real meta+OG+favicon.

**Pass = 8/8**, or a documented, defensible exception written into `audit.md`.

## Hard rules (any failure blocks sign-off)

- [ ] No real, stock, or hotlinked images anywhere — placeholders only.
- [ ] No fabricated facts about the business.
- [ ] **Uses the client's real content** — if they had an existing site, its actual
      services/copy/contact/hours/testimonials were reused (not invented); only genuinely
      missing info is a `[placeholder]`.
- [ ] No outbound contact of any kind was performed.

## Outreach (email OR call script)

The copywriter writes ONE of these per prospect, decided by whether the dossier has a
real email address.

**Both paths must pass:**
- [ ] Personalized — opens with a specific, real observation about this business.
- [ ] Accurate — every claim traces to the dossier.
- [ ] References the mockup (link/path) and the Cecere Brothers portfolio piece.
- [ ] Right voice — short, no hard sell, one soft CTA, kills the maintenance objection.
- [ ] Draft only — no send/call action was performed; placeholders left for Harry.

**If `outreach-email.md` (email found):**
- [ ] `To:` line with a real address that traces to the dossier (not a guessed/invented one).
- [ ] A working `mailto:` link at the top.

**If `outreach-call.md` (no email):**
- [ ] Phone number at the top matches the dossier (as a `tel:` link).
- [ ] Script is natural spoken language — lines Harry can actually say, not an essay.
- [ ] Includes the "if they say…" prepared responses (busy / cost / don't need one / yes).

## Package folder complete

- [ ] `dossier.md` (with page map + winnability pitch)
- [ ] `mockup/` (pages per the page map, opens cleanly)
- [ ] `screenshots/` (desktop + mobile)
- [ ] `outreach-email.md` (email + one-pager) OR `outreach-call.md` (phone + call script)
- [ ] `audit.md` (scored $10K result)
