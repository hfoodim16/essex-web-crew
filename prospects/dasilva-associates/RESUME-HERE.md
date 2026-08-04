# RESUME HERE — `dasilva-associates`

**Paused by Harry, 2026-08-03 ~13:58 EDT.** Build run (Team 2), mid-flight. Nothing is signed off.
Read this file first at resume; it is the state of the world.

---

## What this build is

A **second, separate** site for DaSilva & Associates, LLC, built from **Paul's real completed
questionnaire** (handwritten, scanned 2026-08-03).

> ⛔ **`prospects/paul-da-silva-law/` is FROZEN.** That is the earlier *speculative* build, Harry keeps
> it, it is not being replaced, and nothing in this run may read from, write to, or disturb it.
> Its `site-content.md` and `dossier.md` were copied into this folder as reference — use the copies.

**Harry's standing instruction, verbatim: "always listen to the questionnaire."** `client-answers.md`
outranks the old site, the dossier, the frozen build, every convention and every gate. Where a gate and
an answer collide, the answer wins and the exception gets documented.

## Where it stopped

| Stage | Owner | State |
|---|---|---|
| Questionnaire → `client-answers.md` | lead | **done** |
| Stages 1–5 — `voice-spec.md` + `website-plan.md` | planner | **done**, `plan-lint` exit 0 (verified independently) |
| Stage 6 — 2 AI images | builder | **done**, ~$0.10, cap spent |
| Stage 7 — 4-page build | builder | **built and handed off**, then **mid-repaint when paused** |
| Stage 8 — audit | critic | **Round 1 COMPLETE — NEEDS-WORK.** 4 fixes outstanding; see below + `audit.md` |

**Agents all shut down.** Respawn fresh at resume; do not assume any teammate remembers anything.

## ✅ Palette state — VERIFIED CLEAN at pause (checked by the lead, 14:03)

**The azul+gold repaint completed before the pause and is internally consistent.** No half-painted
stylesheet to repair:

```
--verde / --bone / --garnet  →  0 references
--azul / --gold / --paper    →  60 references
hex 7E2D35 (garnet)          →  0 occurrences
style.css 28.9K, 14:00:26
```

Re-verify with the same grep at resume if you want, but this is not a blocker.

**Stale, do not trust:** the 12 files in `screenshots/` show the **garnet** build. Every one must be
re-shot. Likewise every contrast figure in `audit.md` is garnet-on-bone / bone-on-verde and is void.

**Gates after the repaint: ALL pending.** Nothing was re-run post-repaint — `detect.mjs`, `copycheck.py`,
`aitells.py` and the full contrast sweep all have to run again before anything is judged.

### 🔴 NEW, and it needs judging at resume: the divergence table narrowed

Harry's azul+gold instruction had a side effect nobody flagged at the time. **Rev 3's accent is
brass. Gold is the same metal-accent family.** The plan originally claimed "zero brass/gold" on the
palette axis; that claim is now false and I have corrected `website-plan.md` §18 rather than leave it
flattering.

Divergence is now **4 of 5 clean, palette PARTIAL** — still over the ≥3 requirement, so nothing is
blocked. What still separates them is real: Rev 3 is light-first (63% porcelain) with brass *demoted
to structure* (`--ouro` is text in exactly one rule); this is dark-first with gold as a full working
accent on deep azul. Opposite ground, opposite role for the metal.

**But the Critic's round-1 distinctiveness PASS was reached against the GREEN build.** It must be
re-run against the azul+gold screenshots, comparing gold-on-azul here against brass-on-porcelain
there. If it comes back too close, that is a **direction issue for Harry**, not a Builder fix.

### `website-plan.md` — AMENDED by the lead, plan-lint still exit 0

§1 and §3 now describe the azul+gold system as built: the full token table, the structural
accent-flip, all 14 verified ratios, the restated colour-convention call (including the on-record
risk that blue-and-gold *is* the category default Paul called "too vanilla"), and the removal of the
`cream-palette` waiver. §18 carries the honesty note above.

**Sections 4 onward still say "verde" and "bone" in descriptive prose.** A terminology note at the
end of §3 directs readers to read `verde` → `azul` and `bone` → `paper`. The layouts, formats,
openers, content map and composition device in those sections are current — only colour words are
stale. The Stage 3 evidence sheets (§16) describe *other people's* sites; their colour words are
correct as written and must not be swept.

### Exactly what landed before the pause — verified from disk by the lead, 14:06

The Builder was working the Critic's fix list when the pause hit, so it is **partway through**. Verified
directly rather than taken on report:

| Item | State | Evidence |
|---|---|---|
| Critic fix **2** — bare `<h1>` at 34px under its own 44px `<h2>`s | ✅ **DONE** | `.pagehead h1` rule now sets 3.5rem/900, 3 occurrences |
| Critic fix **3** — `main.js` runtime-throw hole (71% hidden) | ❌ **NOT STARTED** | `main.js` untouched, 2920 B, mtime 13:13:03 |
| Critic fix **4** — missing `pointer: coarse` rule | ❌ **NOT STARTED** | 0 `pointer: coarse` rules in `style.css` |
| Critic fix **1** — `1996` numeral overlapping its `<h2>` by 43px | ⚠️ **UNVERIFIED** | `.steps-head .big-num` has responsive steps (4rem / 3.2rem) but the overlap needs a real render to confirm — **re-measure, don't assume** |
| Open item — `.kicker-free` → `.band-lead` | ✅ **DONE** | 0 `kicker-free` left, 4 `band-lead` |
| Open item — resize `newark-street.webp` | ✅ **DONE** | now 1100×821 (was 1200) |
| Open item — address out of the streetscape split | ✅ **LIKELY DONE** | `385 Lafayette` appears only in JSON-LD (L46), the sticky header (L62) and the footer NAP (L242); the image sits at L203 with no address beside it. Eyeball once at resume. |

**So the remaining build work is small and well-defined:** Critic fixes **3** and **4**, a re-measure of
**1**, then re-run every gate and re-shoot all 12 screenshots against the azul+gold palette.

## Critic round 1 — NEEDS-WORK. Four fixes, none started.

Completed just as the pause landed, so this is real work already banked. **All four are execution defects
that are palette-independent — the azul+gold repaint does not change or invalidate any of them.** The
Critic audited the pre-repaint build, so its *colour* observations are stale; these four are not.

Scores: **$10K 4/8** (fails on 2 typography, 4 hierarchy, 7 mobile, 8 invisible). Rubric **boldness 9**
(the direction is working), dims 2, 3, 8 at 6.

1. **`attorney-bio.html` §15 — real text overlap.** `1996` at 80px renders ~173px of glyphs into a 104px
   grid column and **overlaps its own `<h2>` by 43px**; the screen reads *"1996ducation and career"*.
   Visible in the Builder's own screenshot. (`practice-areas` §11 is fine — `③` is a single glyph.)
2. **`attorney-bio.html` + `contact.html` — `<h1>` outranked by its own `<h2>`s.** No rule sizes a bare
   `h1`, so both fall to the 34px browser default while their `<h2>`s render at 44px.
3. **`main.js` — the JS-off guard only half works.** `motionOK()` (line 7) clears the dead-man timer
   *before* the reveals are wired, and the head's error listener catches resource-load failures but not
   runtime throws. Script **404 → 0% hidden (passes)**; script **throws → 71% hidden (fails)**. Two-line
   fix. This is the one that actually matters — it is the failure mode the JS-off gate exists to catch.
4. **No `pointer: coarse` rule exists anywhere** — footer links 22px, burger 42px, header tap-to-call 43px.

### Verified clean in round 1 — do not re-audit at resume

All eight of `critic-prep.md`'s predictions checked out independently. Detector **0 errors, 0 advisory**
on all 4 pages, exit 0, engine proven live against a deliberately-bad control file (7 findings fired).
**Zero computed contrast failures across every text node on all 4 pages** — the garnet-on-verde trap is
never hit and `.form input:focus` sits on a light band at 7.06:1. Fail-visible passes on every path that
matters (script missing 0%, reduced-motion 0%, full-height 0%); the 54–80% at-rest figure is below-fold
IO state, not hidden content. Composition device lands on all 4 pages at 3.18×–4.94×. Kicker budgets
pass. Cell number absent. All 13 `tel:` hrefs digit-match. `og-image.webp` confirmed by eye as a crop of
the hero — 2 paid calls total, no video.

**Distinctiveness: PASS, no escalation.** The `gee-kay` numerals worry is resolved — it is a light
plan-paper two-column with thin Newsreader and spruce numerals on a tick-field; DaSilva is a dark
full-bleed photographic band, 900-weight Frank Ruhl over the image, god rays, zero rule-work. The shared
element is one widespread pattern (a numeral trust strip under the hero), executed differently. Not siblings.

## Harry's rulings — carry these forward

1. **The palette is azul and gold. The green and beige are gone.** His words: *"Do azul and gold colors
   rather than the green and beige."* Tokens locked and pair-verified by the lead:

   ```css
   --azul-950:#041E30;  --azul-deep:#062B44;  --azul-900:#0A3A58;   /* dark grounds */
   --azul:    #00588A;  --azul-hov: #00426B;                        /* accent on LIGHT only */
   --gold:    #C8A24A;  --gold-hov: #D9B75F;  --gold-deep:#7E5F16;  /* accent on DARK only */
   --paper:   #F4F6F7;  --paper-2:  #E4EAEE;  --paper-dim:#AFC0CC;  /* cool near-white, NOT beige */
   --ink:     #0D1B24;  --ink-dim:  #44586A;
   ```

   **The rule that matters:** never `--gold` on `--paper` (2.17:1), never `--azul` on any dark ground
   (1.78:1). Gold is the first accent that can live on a dark band (6.07:1 on `--azul-deep`), which is
   why the **hero CTA is a gold-filled button with `--ink` text** (7.27:1). Verified passes:
   gold/azul-deep 6.07 · gold/azul-900 4.96 · gold/azul-950 7.07 · ink/gold 7.27 · paper/azul-deep 13.48 ·
   paper/azul-950 15.70 · paper-dim/azul-deep 7.82 · ink/paper 16.15 · ink-dim/paper 6.80 · azul/paper 7.01 ·
   azul/paper-2 6.26 · azul-hov/paper 9.73. Only `gold-deep` on `paper-2` (4.89) is near the line.

   **The old garnet-vs-azul argument is dead** — it resolved past both options. Ignore it wherever it
   still appears in `website-plan.md`, `critic-prep.md`, or agent transcripts.

2. **The three open items were approved** and may or may not have landed before the pause — verify:
   - Move *"The office is at 385 Lafayette Street in Newark."* **out of** the Home split that holds the
     generated streetscape (layout implied it was his building). Address stays in footer NAP + contact.
   - Resize `newark-street.webp` to ~1100px intrinsic (was 1200px against 549px CSS).
   - Rename `.kicker-free` → `.band-lead` (3 pages). It is not a kicker; the name misleads a grep.

3. **The Home band rhythm stays as shipped** (light · light · dark · light · light · dark). The Planner's
   revert order is permanently moot — it existed to protect accent numerals on light bands, and gold
   solves that. Do not reinstate it.

## 🔴 OPEN — needs Harry before the build can be called done

**A real photo of the office.** Harry said he added one to `assets/`; it was **not there** at pause —
the lead searched `mockup/assets/`, every `assets/` dir in the repo, `~/Downloads`, `~/Desktop`, and all
recently-modified images under `~`. **Ask him for the path.**

When it arrives, the recommendation on record: **use it to replace the generated `newark-street.webp`**
in the Home service-area section. That retires a compromise rather than filling a gap — the generated
street is an invented block that needed careful captioning precisely *because* it isn't his building. A
real photo also lets the address line move back beside it (undoing open item 2 above). Second-choice
home is a labeled placeholder on `contact.html`.

Note: the no-readable-signage rule applies to **generated** images only, to stop the model inventing
fake branding. On a real photo of his real office, legible real signage is an **asset** — keep it.

## Also open, lower priority

- **An outcome claim.** The practice-areas lede carries his live site's own wording: *"…which often gets
  a good result without the expense of needless additional litigation costs."* Carried because it is his
  published sentence and plan §7 maps it there. **NJ bar-advertising rules are strict about outcome
  language — Harry should ask Paul before launch.** Added to the Confirm list.
- **No attorney-advertising disclaimer — LEAD DECISION MADE, not yet implemented.** The Builder cut its
  draft, reasoning that inventing legal boilerplate equals inventing a licence number. The Critic showed
  that reasoning is wrong (a licence number asserts a fact that may be false; a disclaimer asserts
  nothing and only narrows inference — opposite kinds of statement) but reached the same conclusion for
  a better reason: **what legal furniture goes on a lawyer's site is Paul's call.**
  **Ruling: ship the labeled placeholder**, exactly as the frozen Rev 3 did on this same client —
  `[Standard attorney-advertising / no-attorney-client-relationship disclaimer — for Paul's review]` in
  the footer. That is the crew's standard device for "a real thing belongs here and we can't supply the
  value": neither invented boilerplate nor a silent omission. It matters more than usual **because the
  site does carry an outcome claim**, and a page with an outcome claim and no disclaimer is the riskier
  of the two states. Fold into round 2. Pair it with the outcome-claim question as **one ask to Paul.**
- **Documented exception:** visible placeholder labels read `Photo slot: …` rather than the playbook's
  literal `AI-IMAGE — …`, because `copycheck.py`'s placeholder gate flags that string in visible copy.
  The machine-readable `<!-- AI-IMAGE: … -->` comments are intact. Not a fail; record it in `audit.md`.
- **Distinctiveness watch:** `gee-kay-landscaping` (signed the day before) also uses oversized numerals
  as its hierarchy engine. Two consecutive builds whose loudest visual event is a wall of giant numbers
  is soft sameness the ban list misses. Judge from the final screenshots. **If it fails it is a direction
  issue — escalate to Harry, don't send it to the Builder.**
- **Boldness bar is now higher, not lower.** Blue-and-gold is the legal category default and *"too
  vanilla"* was Paul's own complaint about his current site (Q7). Harry chose it and that is settled —
  do not fail the build for it. But the poster-stack, the oversized Frank Ruhl numerals and the
  dark-first inversion must carry the distinctiveness alone. The audit must say plainly whether they do.
- **Stale dev server on port 8231** belongs to the DiSalvo prospect and briefly served the Builder
  screenshots of the wrong site. Left alone deliberately; reap it if convenient.

## Gate results as of the pause (pre-repaint — ALL must be re-run after it)

Everything below was green on the garnet build. **Colour-dependent results are void; structural ones hold.**

- `detect.mjs` exit 0, all 4 pages, no DEGRADED banner · `copycheck.py` exit 0 · `aitells.py` exit 0
- Contrast 0 failures across 31 pairs incl. hover/focus; hero scrim 7.64:1 worst case — **VOID, re-run**
- Exactly one `<h1>` per page · landmarks on all 4 · visible `:focus-visible` ring
- **Fail-visible 0.0%** (0 of 2358 chars hidden with `main.js` gone; threshold ~15%) · reduced-motion renders complete
- Kicker budget per file: index 1/3 · practice-areas 1/2 · bio 0/2 · contact 1/1 — all under
- Composition device ≥3× per page: 4.9× · 4.7× · 4.7× · 3.3×
- Click-test clean, no dead clicks · true 375px, no overflow · offline verified, 676 KB
- Cell number `973-747-6196` absent (grep-verified) · no `openingHours`, no published email
- 2 generations only (~$0.10), 2 sidecar logs, 2 task IDs. `og-image.webp` is a PIL crop of the hero,
  **not** a third paid call. No video. **The image cap is spent — no further generations without Harry.**

## Resume sequence

1. Read this file, then `client-answers.md`, then the Builder's final state report.
2. Verify the palette is consistent (command above); finish the repaint if it is not.
3. Get the office photo path from Harry; place it per the recommendation above.
4. Respawn the Builder to finish the repaint + open items, then re-run **all** gates and re-shoot all 12
   screenshots.
5. Respawn the Critic with the brief in `critic-prep.md` (note its **LEAD OVERRIDE** block) plus
   `audit.md`, for the visual half: rubric, boldness, imagery, distinctiveness.
6. Gate is both scoreboards: $10K Checklist 8/8 (or documented exceptions) **and** no rubric dimension
   below 7 with boldness ≥ 8.
7. On pass: append the `design-memory.md` row **recording the accent as it actually ships**, then the
   lead runs `/design-push`.

**Not yet due:** delivery to Corey. That needs a *signed* `release-form.pdf` back from Paul — a hard gate,
and an AI sign-off is not the client's permission to publish.
