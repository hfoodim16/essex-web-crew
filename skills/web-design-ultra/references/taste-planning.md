# Taste — the planning sections

> **Forked from the `taste-skill` (`design-taste-frontend`), 2026-08-05**, the same way
> the detector and craft floor were forked in from Impeccable: the four sections the
> Planner actually uses, stripped of everything else. The source skill is 12,853 words —
> 85 KB of stack picks, install commands, dial machinery and a block library that are
> build-time concerns and belong to the Builder, not the plan. The Planner was reading all
> of it to use four sections.
>
> **Where the fork and this skill disagree, `web-design-ultra` wins.** Two known
> collisions, already resolved here: taste suggests **Geist**, which is on our banned font
> list, and its content rules say to *invent* premium-sounding brand names and organic-
> looking fake numbers — the exact opposite of our real-facts-only rule. Its reasoning
> transfers; its picks do not.

Four sections, all planning work. Nothing here is build-time.

---

## §0 — Brief inference, and the Design Read

Infer what the client actually wants **before** reaching for an aesthetic. Most generated
design is bad because the model jumps to a default instead of reading the room.

Signals to read, in order:

1. **Page kind** — for us this is nearly always a local service business, but "brochure
   for a 40-year masonry outfit" and "booking-led med spa" are different pages.
2. **Vibe words the client used** in their own answers. Their words, not your reading of
   their trade.
3. **Reference signals** — sites they named, competitors they mentioned, anything they
   pasted.
4. **Audience.** A homeowner pricing a patio, not a design-conscious buyer. **The audience
   picks the aesthetic, not your taste** — and ours is usually someone on a phone who
   wants a phone number.
5. **Brand assets that already exist** — logo, colors, truck livery, signage. For a
   redesign these are starting material, not optional input.
6. **Quiet constraints** — trust-first trades (legal, medical, financial), accessibility,
   anything regulated. **These override aesthetic preference.**

**Write the Design Read into `website-plan.md`, verbatim, in one line:**

> **"Reading this as: `<page kind>` for `<audience>`, with a `<vibe>` language, leaning
> toward `<aesthetic family>`."**

Examples in our register:

- *"Reading this as: a brochure site for homeowners pricing hardscape work, with a
  plain-spoken proof-first language, leaning toward earthy neutrals + heavy slab serif."*
- *"Reading this as: a trust-first site for people who just got a ticket, with a
  document-discipline language, leaning toward porcelain-and-ink with one metal accent."*

The point is to **name the read instead of defaulting to an aesthetic.** `plan-lint.mjs`
requires this field.

**If the brief is genuinely ambiguous, ask ONE question** — never a multi-question dump —
and only when the read actually diverges. If you can infer it from the answers, don't ask.

---

## §0.D — Anti-default discipline

Do not default to: AI-purple gradients, a centered hero over a dark mesh, three equal
feature cards, glassmorphism on everything, infinite-loop micro-animations, Inter +
slate-900. These are the LLM defaults. Reach past them **deliberately, from the design
read** — not randomly.

Our own banned-font list (`SKILL.md` non-negotiable 6) is the same rule with names on it.

---

## §9 — AI tells, at plan time

Run all three directions against this list at Stage 5, before locking one.

**Visual**
- No neon or outer glows — inner borders or tinted shadows instead.
- No pure `#000000`. Off-black, charcoal.
- No oversaturated accents; desaturate to sit with the neutrals.
- No gradient text on large headers. No custom cursors.

**Typography**
- No oversized H1 that just shouts. Control hierarchy with weight and color before scale.
- Serif for editorial, legal, and premium registers — not for a dashboard.

**Layout**
- **No three equal feature cards in a row.** The generic three-identical-cards row is
  banned outright — use a 2-column zig-zag, an asymmetric grid, or a scroll-pinned
  sequence. (Our `section-formats.md` quotas enforce this mechanically.)
- Deliberate spacing. No floating elements with awkward gaps.

**Content — and here the crew rule overrides taste**
- No generic placeholder names or avatars.
- **Taste says invent believable names and messy-looking numbers. We do not.** Every name,
  number, review and date on our pages is real or a labeled placeholder — see the
  real-reviews and content-honesty rules in `CLAUDE.md`. Fabricating an "organic-looking"
  statistic is a hard fail here, not a craft technique.
- No filler verbs — "elevate", "seamless", "unleash", "revolutionize". `banlist.md` and
  `aitells.py` already own this list; the plan should not spec copy that trips them.

**Structure**
- No version-label eyebrows (`V0.6`, `BETA`, `EARLY ACCESS`) unless the brief is literally
  about a launch.
- **No section-number eyebrows** (`001 · Capabilities`, `06 · how it works`). An eyebrow
  names the topic in plain language; it does not enumerate.
- No `01 / 4` pagination on images or tiles. If the reader can count, skip the label.
- No fake product screenshots built out of `<div>`s.

---

## §11 — Redesign protocol

Most of our prospects have an existing site, so this is the common case, not the exception.
**Misclassifying the mode is the biggest source of bad redesign output.**

**Pick the mode first:**
- **Preserve** — modernize without breaking a brand the client is attached to. Audit,
  extract their tokens, evolve.
- **Overhaul** — new visual language over existing content. Greenfield for visuals,
  preserve content and IA.
- **Greenfield** — no real site, or the brand itself is changing.

If ambiguous, ask once: *"Should this keep the look you have now, or start fresh?"*

**Audit before proposing anything.** Document: brand tokens (colors, type, logo
treatment), information architecture (page tree, nav, conversion paths), which content
blocks are doing work and which are filler, patterns worth preserving (a recognizable
hero, their copy voice), patterns to retire (dead links, stock imagery, AI slop), and the
**SEO baseline** — ranking pages, titles, structured data. **SEO migration is the number
one redesign risk.**

**Preservation rules**
- Don't change IA unless asked. Keep slugs, anchor ids, and nav labels stable — for search
  and for the client's own muscle memory.
- Extract brand colors before applying any palette rule. A business that is already green
  stays green (this is the same override `color-conventions.md` describes).
- **Preserve copy voice** unless a rewrite was asked for. Visual modernization is not a
  content rewrite — and our `voice-spec.md` is built from their answers regardless.
- Don't regress accessibility that already works.

**Modernization levers, in priority order** — stop when the brief is satisfied:
1. Typography refresh — the biggest lift per unit of risk.
2. Spacing and rhythm.
3. Color recalibration — desaturate, unify neutrals, keep the brand accent.
4. Motion layer.
5. Hero and key-section recomposition.
6. Full block replacement — only when the block is unsalvageable.

**Targeted evolution vs full redesign:** if IA, content and SEO are sound, levers 1–4 get
roughly 70% of the value at 40% of the risk. Go full redesign when the visual debt is
structural — broken IA, no system, broken mobile.

**Never change silently:** URL structure, primary nav labels, form field names or order,
the logo, or existing legal/consent copy.
