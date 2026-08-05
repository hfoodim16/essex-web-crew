# Design Gates — Essex Web Crew

**These gates now live inside `web-design-ultra` itself.** They are not a crew-specific bolt-on any
more, and this file is no longer where the rules are written down — keeping a second copy here is how
the two versions drift apart.

Everything the crew runs comes from the skill, which every agent already invokes as PRIMARY:

| Gate | Where it lives now | When it runs |
|---|---|---|
| **Plan lint** — section-format quotas, banned fonts, required plan fields | `skills/web-design-ultra/scripts/plan-lint.mjs` | Planner, on `website-plan.md`, **before handoff** — must exit 0 |
| **Mechanical scan** — 60+ deterministic rules, no LLM, ~1s. Impeccable's audit engine | `references/critique.md` → "Step 0", script at `skills/web-design-ultra/scripts/detect.mjs` | Builder before handoff; Critic first, before any screenshot. **Every `mockup/*.html` page**, not just the homepage |
| **Fail-visible measurement** — % of page text hidden at rest | `references/critique.md` → the JS-off test | Critic, in the browser session it already opens, **before** force-revealing for capture |
| **Composition checks** — hero stack, CTA wrap/intent, nav line, no-repeated-family (superseded the zigzag cap), layout variety, consistency locks, grid cell count, contrast | `references/critique.md` → "Composition checks" | Critic, folded into the existing gate |
| **Build quality floor** — contrast, depth, spacing, states, defaults to refuse | `references/craft-floor.md` | Builder, immediately before editing UI |
| **Fix-loop methods** — amplify a flat section / calm an overloud one | `references/bolder.md` · `references/quieter.md` | Critic's fix loop, per round |

Four more gates are ours, not the skill's, and run outside that table:

| Gate | Where it lives | When it runs |
|---|---|---|
| **Sheet review (B1b)** — judgment pass on `build-sheet.md` + `voice-spec.md` BEFORE any code | `.claude/agents/critic.md` · `CLAUDE.md` pipeline stage B1b | Critic, after the Planner hands off. **No build starts without SHEET GO** (≤2 rounds, then the lead) |
| **Copy-voice gate** — register + page shape | `skills/trade-copy/scripts/copycheck.py` · `skills/web-humanizer/scripts/aitells.py` | Builder before handoff, Critic at Stage 8. Both must exit 0; neither replaces the say-aloud read |
| **Content parity** — the new site never knows less than the old one | `templates/package-checklist.md` · `.claude/agents/critic.md` | Critic, walking `site-content.md` block by block. Counts facts, not words |
| **Release form** — signed form gates delivery entirely | `templates/package-checklist.md` · `docs/delivery.md` | Critic checks the artifact at sign-off; the lead re-checks before packaging |

Read those files. Don't re-derive the rules from this page.

---

## What stays crew-specific

The skill is general-purpose; these are ours and belong here, not in it:

- **The $10K Checklist** — the client-facing 8-item scoreboard (Metics Media Field Guide No. 01).
  External to the skill, and it should stay that way. Full text in
  `templates/package-checklist.md` (CLAUDE.md only references it).
- **`audit.md` and its two scoreboards** — the Critic writes one per review round, with the
  `Review round: N` line, the Gate A result, both scoreboards, and the numbered fix list. The skill
  has no equivalent artifact; this is how a stalled loop stays distinguishable from a live one.
- **The project-local `design-memory.md`** — the crew keeps its own anti-repetition ban list so
  prospects diverge from *each other*, not from Harry's unrelated test builds. The skill reads and
  appends to whichever log the project has (Stage 4 / Stage 8); ours is the one it must use.
- **Local-trade conversion patterns** — tap-to-call, service-area towns, license line, ≤4-field
  estimate form, NAP footer. In the skill as `references/local-trade.md`, but non-negotiable for us
  in a way it isn't for a general build: a beautiful hero with no visible phone number is a failed
  build.
- **The copy-voice gate** — `voice-spec.md` + `copycheck.py` + `aitells.py` + the say-aloud
  read. Entirely ours. `copycheck.py` (`trade-copy`) measures register; `aitells.py`
  (`web-humanizer`) measures page shape — interchangeable heroes, abstract card titles, no
  checkable fact, stamped card lengths. Both must exit 0; neither replaces the read.

## Precedence

Unchanged, and it still runs one way:

> **client brief + `voice-spec.md`** → **`web-design-ultra` direction + `local-trade.md`** → **the gates**

A gate never overrules a direction the Planner locked for a real reason. Trades carry their own
colour conventions — a landscaper in earth tones is *correct*, even though the detector's
`cream-palette` rule and the premium-consumer palette ban both point the other way. What those rules
forbid is *defaulting* there without deciding. State the exception in `website-plan.md`, waive it
in-file with a reason, and the Critic accepts it.

## Baseline (2026-07-27) — historical snapshot, not a live count

> Superseded: there are nine prospect builds now, and `gee-kay-landscaping` was rebuilt
> after this was written. Kept as the record of what the gates found when they first ran —
> re-measuring it is not required, and per the **Lessons flow forward** doctrine in
> `CLAUDE.md`, neither build gets reopened to satisfy a newer rule.

As of that date, six of eight prospect mockups scanned clean. Two bounce, both `overused-font`: `fora-digital`
(Instrument Serif) and `gee-kay-landscaping` (Fraunces, plus 27 em-dashes advisory).

**Both are frozen and stay as they are** — sign-off freezes a prospect, and a new gate is not a reason
to reopen one. They're listed so nobody mistakes the bounce for a broken detector.

Those two fonts are now named in the skill's own banned set (`SKILL.md` non-negotiable 6), alongside
Geist, Plus Jakarta Sans and Space Grotesk. We shipped Fraunces twice and Instrument Serif once before
any rule named them.
