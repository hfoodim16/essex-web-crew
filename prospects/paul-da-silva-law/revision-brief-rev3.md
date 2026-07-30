# Revision brief — Rev 3, `paul-da-silva-law`

**Authorized by Harry, 2026-07-29.** This reopens a signed-off prospect (audit round 3,
PASS on both scoreboards). It is a **type + layout overhaul, not a rebuild.** Planner,
Builder and Critic all read this file first; it outranks `website-plan.md` Rev 2 wherever
they disagree, and sits under `client-answers.md` as always.

## Harry's words

> "Keep the colors, and info. I like how the info is shown in blocks, but I don't love
> font and format as a whole please change with the team."

Scope confirmed with him: **new font pairing + new layout system.** Palette and content
are fixed. So the read is:

- The **palette** is right — he chose blue+gold himself (Q-answer, Rev 2).
- The **information** is right — parity is already banked, don't re-litigate it.
- The **block treatment** is a keeper — discrete, bounded info blocks are what he likes.
  Keep blocks as the organizing unit; re-compose how they sit, size, and rhythm.
- The **font pairing and overall format** are what he doesn't love. That's the work.

## FROZEN — do not change

1. **Every palette token, exact hex.** Copy `:root` colors across verbatim:
   `--tinta #131D33`, `--tinta-2 #0D1526`, `--pedra #F0F2F5`, `--ink #161A24`,
   `--ouro #B3873E`, `--ouro-escuro #806026`, `--muted #566072`, `--linha #C8CDD6`,
   `--lamp #EAD9AE`. Token names stay too. Proportions of use may change (that's layout);
   the colors themselves may not. No new hues, no tints outside these nine.
2. **All content.** Every visible string on all four pages carries over at full
   informational fidelity. `site-content.md` parity contract and the Rev 2 content map
   stand as already satisfied — the Critic re-walks it, nobody re-decides it.
3. **`voice-spec.md` unchanged.** Register, banlist, word budgets, protected strings, and
   the bar-advertising rules all stand. This is not a copy round: rewrite a string ONLY
   where the new layout genuinely needs a different length, and then re-run both
   `copycheck.py` and `aitells.py`.
4. **The two real images** — `assets/hero.webp`, `assets/about.webp`. They passed the
   two-way test at sign-off. **Do NOT regenerate; the 2-image cap is already spent.** If a
   slot's aspect ratio changes, crop/downscale the existing file (`media-processing`),
   never a new generation.
5. **The real logo** — `assets/logo.png`, top-left, unmodified.
6. **The live map embed in `contact.html`.** Harry hand-edited the placeholder block into a
   real live embed. It is currently **uncommitted**, so it exists only in the working tree.
   What is actually there (verified in the file, not assumed):
   - an `<iframe class="map-embed">` pointing at
     `www.openstreetmap.org/export/embed.html?bbox=…&layer=mapnik&marker=…`
     with `loading="lazy"`, `referrerpolicy="no-referrer-when-downgrade"` and
     `title="Map location: 385 Lafayette Street, Newark, NJ 07105"`;
   - directly under it, a **"Get directions"** link to
     `google.com/maps/search/?api=1&query=385+Lafayette+Street,+Newark,+NJ+07105`
     (`target="_blank" rel="noopener"`).

   Carry **both** across byte-for-byte — same provider, same URLs, same attributes. This is
   the one sanctioned live third-party embed on this site. Restyle the surrounding frame
   freely; do not revert it to a placeholder block and do not swap the map provider.
7. **Four pages, same nav:** `index.html`, `practice-areas.html`, `attorney-bio.html`,
   `contact.html`. Same URLs, same nav labels.
8. All standing hard rules: content honesty, real-reviews-only, JS-off readability,
   `LocalBusiness`/`LegalService` JSON-LD matching the footer NAP, local-trade conversion
   patterns (visible `tel:` in the mobile header, service-area towns, trust strip, ≤4-field
   form), offline-capable static build.

## CHANGE — the actual deliverable

1. **New font pairing.** Retire **Besley / Schibsted Grotesk**. Banned on top of that:
   Inter, Roboto, Arial, Helvetica, Fraunces, Instrument Serif, Geist, Plus Jakarta Sans,
   Space Grotesk — and any pairing in the last three `design-memory.md` rows
   (Zilla Slab/Work Sans, Instrument Serif/Hanken Grotesk, Besley/Schibsted Grotesk).
   The new pairing must read as **counsel you'd trust with a serious matter** — this is a
   Newark immigration/criminal/injury practice, not a design studio. Also re-set the whole
   type system, not just the family names: scale, leading, tracking, weight contrast,
   optical sizes, how a block's heading relates to its body.
2. **New layout system.** Retire the Rev 2 archetype — **split-screen advocacy (dark
   identity panel / light content panel) + document-discipline interior stack**. Also
   diverge from the last three logged archetypes. Keep bounded info **blocks** as the unit;
   change how they're composed: block scale contrast, asymmetry, how the dark ink grounds
   and porcelain grounds alternate, section rhythm, container behavior, where brass lands.
   The hero in particular should not be the same shot in a new frame.
3. **New background system and new signature motion.** Rev 2 was ink grounds + azulejo
   monoline lattice + grain + lamp-glow radial, with a clip-wipe "unredacting" reveal.
   Pick differently, from the skill's `backgrounds.md` / `atmosphere.md` / `motion.md`.
   The fade-up + text-delay + count-up trio still fails item 6.
4. **Both gates again from zero.** Step 0 `detect.mjs` to `exit 0`, fail-visible
   measurement, composition checks, $10K Checklist 8/8, rubric no dimension below 7 with
   boldness ≥ 8, plus the interactive click-test on all four pages and both viewports.

## Deliverables

- `website-plan.md` — Rev 3 section appended (do not delete the Rev 2 record; the palette
  rationale and content map are still load-bearing).
- `mockup/` rebuilt to the Rev 3 plan, same four filenames.
- `screenshots/` re-captured, desktop + mobile, all four pages.
- `audit.md` — a fresh `Review round: N` block per round; Rev 2's sign-off stays in the file
  as history.
- `design-memory.md` — the Critic **replaces** the paul-da-silva-law row on pass, noting
  Rev 3 and that the palette is client-locked and deliberately carried over.
