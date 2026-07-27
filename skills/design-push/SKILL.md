---
name: design-push
description: Publish a finished website into Claude Design (claude.ai/design) as a browsable design-system project — one card per section, tokens as foundations. Re-run it after a revision to update the same project in place. Also the /design-push command. Use when a build passes the web-design-ultra critique gate, when a site has changed and its Claude Design copy is stale, or when backfilling an older site.
---

# design-push

Turn a finished static site into a Claude Design design-system project: each section becomes its own preview card, the `:root` tokens become foundations, and the assembled page ships as a template. Running it again on the same site **updates that project in place**.

**Args:** a site directory (contains `index.html`; defaults to cwd) and optionally a client name. If no name is given, derive one from the directory and confirm it — the name is the project identity and a typo creates a duplicate project.

## Why decompose

The Design System pane renders **one card per file**. Pushing a whole `index.html` gives one giant card, which is useless for precise work. One card per section is the entire point.

## Steps

### 0. Pre-flight: has anyone edited this project in Design?

A push overwrites the same paths, so if the user refined something in the Design pane
since the last push, pushing now destroys it. **Check before bundling** — run the
`design-pull` skill's `--check` (steps 1–3 there: match the project, fetch
`styles.css` / `components/*` / `pages/*`, run `design-pull.py --check`).

- Clean → carry on to step 1.
- **Drift → stop and offer `/design-pull` first.** Do not push past it because the edit
  looks minor; you can't tell from a diff whether the user meant to keep it.

Skip only when there's no project yet (a first push has nothing to lose). `--force` on the
pull check is for a loss the user has explicitly chosen, not for getting past the gate.

### 1. Bundle

```bash
python3 ~/.claude/skills/web-design-ultra/scripts/design-bundle.py \
  --src <site-dir> --name "<Client Name>" --out /tmp/ds-<slug>
```

Deterministic and offline. It handles the three shapes the crew ships (single-page sections, SPA `.page` views, multi-page **including nested sub-sites** like `work/<client>/index.html`), rewrites every relative path, copies every asset dir recursively plus loose assets beside a nested page, carries all stylesheets and scripts, generates `foundations/color.html` / `type.html` / `motion.html`, and emits both `templates/landing/` and `templates/mobile/`.

**The last line is the one that matters:**

```
coverage: blocks 9/9 · pages 2/2 · assets 3/3 · tokens 19/19
```

It counts what the source has against what got written, and **exits non-zero if anything is short or any warning fired** — so a `$?` of 0 is your evidence the bundle is a faithful copy. Never push a bundle that exited non-zero; fix the cause. `--force` overrides, and is for a gap you have understood and can explain, not for getting past the gate.

Two categories of message, deliberately kept apart:
- `warning:` — a bundling fault. Blocks.
- `note (site defect, not bundling):` — already broken in the source site (a dead image ref, a 1.7 MB un-recompressed hero). Worth fixing in the site, but a faithful copy of a broken link is *correct* behaviour, so it never blocks. If these blocked, the gate would cry wolf and stop being trusted.

This gate exists because every bug this script has had was severe *specifically because it was quiet*. It once emitted 4 cards for a 9-section site and printed a summary that looked like success.

### 2. Spot-check one card

Serve the bundle and screenshot one component headless (technique in `web-design-ultra/references/critique.md`):

```bash
python3 -m http.server 8799 --directory /tmp/ds-<slug> &
```

A blank card means the site's own `main.js` threw on the fragment. `lib/card-boot.js` should have already settled the DOM — if it didn't, that's a bundler bug worth fixing rather than shipping around.

### 3. Find or create the project

```
DesignSync list_projects
```

Match on the client name.

- **Found → this is a re-push.** Reuse that `projectId`; writing the same paths updates in place.
- **Not found → `create_project`** with the client name.

**Say which one is happening before you write.** A silent create when the user expected an update means a duplicate project, and that's the failure mode worth catching early. Verify the target with `get_project` — it must be `type: PROJECT_TYPE_DESIGN_SYSTEM`, which is immutable at creation.

### 4. Push

```
DesignSync finalize_plan
  projectId, localDir: /tmp/ds-<slug>
  writes:  ["readme.md","styles.css","theme.json","thumbnail.html",
            "foundations/*.html","components/*.html","pages/*.html",
            "templates/landing/*.html","lib/*.js","vendor/*.js","assets/*"]
  deletes: []          ← required field even when empty; omitting it errors
```

Then `write_files` with the `localPath` form from `_manifest.json` (contents stream from disk, never through context; ≤256 files per call).

Skip `register_assets` — the pane builds its index from the `@dsCard` markers.

### 5. Verify and report

`list_files` to confirm. Report: project name, **created or updated**, file count, card count. If this was a re-push, confirm the count matches the previous push — a jump means the site gained sections, a drop means something didn't upload.

## The manifest compiles once, ever — confirmed, not just suspected

`_ds_manifest.json` — the file that drives the project's card sidebar — is compiled
client-side by the claude.ai/design app, not by anything `DesignSync` triggers. Evidence
from three separate tests, escalating each time a fix seemed plausible:

1. A single corrected file (`templates/landing/index.html`) pushed via `write_files` →
   manifest byte-for-byte unchanged.
2. A **full re-push of all 29 files** in one `finalize_plan`/`write_files` batch (in case
   the compiler only rescans on a complete sync, not a single-file patch) → still
   byte-for-byte unchanged.
3. Four browser refreshes on the user's end → no change.

None of it moves the needle. Combined with the original stuck-project symptom (a
deleted card's file was gone but the sidebar kept listing it as "file not found"), the
conclusion is: **the manifest compiles once, when the claude.ai/design app has the project
loaded, and is then cached.** Nothing you can do from this side recompiles it afterwards —
not a write, not a delete, not a refresh, not a bigger write. Any path added to a project
*after* it has compiled will never appear as a card, however correct the file and its marker.

One observed refinement: a push into a project the user currently has **open in a browser**
does compile immediately (seen on a fresh project — its manifest went from 404 to fully
populated during the push). A project nobody has opened stays at 404 until first open. So
the trigger is the app having the project loaded, not a literal first-ever visit. The
operational rule is unchanged either way: **once compiled, new paths never appear.**

**The fix: push into a brand-new project instead of trying to repair the stuck one.** A
fresh `create_project` has no manifest yet, so its first browser-side open has nothing
frozen to inherit. Confirm with `get_file` on `_ds_manifest.json` that it 404s (nothing
compiled yet) before handing the project back — that 404 is the actual proof it will
compile clean, not just a hopeful guess. There is no `delete_project` in `DesignSync`;
tell the user to remove the stuck one manually in-browser once the new one's confirmed.

### So: re-push, or fresh project?

The freeze makes this a real decision, not a formality. **Compare the card PATHS**, not the
content — content updates fine in place; only the index is frozen.

| Situation | What to do |
|---|---|
| Same paths, changed content (a revision round: copy edits, colour tweaks, restyled section) | **Re-push.** Updates in place, cards stay correct. |
| Any NEW path (a section added, a page added, the bundler gained a foundation or template, a slug changed) | **Fresh project.** A re-push writes the file and the sidebar never shows it. |

Diff `list_files` against the new bundle's `_manifest.json` before deciding — if the path
sets differ at all, it's a fresh project. Getting this wrong is invisible: the push reports
success, the file really is there, and the card simply never appears.

A slug change counts, and they do change: card names come from `id` → role class →
`aria-label` → heading, so **editing a section's heading can rename its card**. That's the
right trade (readable names beat stable ones for finding a section), but it means a copy
edit can quietly turn into a new-path situation.

## The `templates/` marker is NOT `@dsCard` — a real bundler bug, now fixed

`components/*.html`, `foundations/*.html`, and `pages/*.html` are indexed from a
first-line `<!-- @dsCard group="…" name="…" subtitle="…" viewport="…" -->` comment. A
file under `templates/<slug>/` is indexed from a **completely different** marker:
`<!-- @template name="…" description="…" -->` — confirmed against the user's own working
Modernist project, which populates a real `templates` array in its manifest this way.
`design-bundle.py`'s `landing()` method used to write the `@dsCard` form for
`templates/landing/index.html`; that card silently never appeared — no error, valid
file, wrong marker, permanently invisible once the enclosing project's manifest froze
(see above). Fixed: `landing()` now emits the correct `@template` marker. If you ever
hand-author a template file outside the bundler, use the `@template` form or it will
suffer the exact same silent fate.

## Multi-page sites: internal nav links need rewriting too

A multi-page site's nav (dropdown menus, "back to services," the logo-to-home link)
uses bare relative hrefs — `service-lawn-care.html`, `index.html` — that only resolve
because every page sits in the same folder on the real site. The SAME nav markup gets
reused verbatim across `components/nav.html`, `components/services.html` (or wherever
the source repeats the link list), every `pages/*.html` card's own header, and
`templates/landing/index.html` — and in the bundle those pages scatter across
`pages/`, `components/`, and `templates/landing/`, so a bare href almost never lands on
the right file. Clicking it 404s, even though the page it's pointing at genuinely
exists in the project.

`rewrite()` now handles this automatically via `self.sibling_pages` (every non-index
`.html` file at the site root, mapped to its `pages/<slug>.html` bundle path) — every
call site gets it for free. If you ever hand-roll a card outside the normal
`page()`/`rewrite()` path, remember: sibling page links → `{up}pages/<slug>.html`,
bare `index.html` → `{up}templates/landing/index.html`.

## Rules

- **The repo is the source of truth.** A re-push overwrites the same paths, so **any edit made inside Claude Design is lost** unless it is pulled back first. That direction is deliberate; losing the edit silently is not, which is why step 0 gates on it. Use the **`design-pull` skill** (`/design-pull`) to bring Design edits into the source — it detects them automatically by re-bundling and diffing, and verifies each write-back by round-trip. For motion, a copy-back isn't enough: distill it into a *named* recipe in `motion.md` / `gsap.md` / `reactive-backgrounds.md`, because an animation is only usable by the crew once it has a name a planner can put in a direction brief and the anti-repetition log can ban.
- **Only push a site that passed the gate.** Claude Design is for finished work, not works in progress.
- **One project per client.** Never a shared portfolio project — the pane would mix unrelated token systems in one card index.
- Recompress assets over ~200 KB to WebP first (`web-design-ultra/references/imagery.md`).
- The bundle carries nothing the public site doesn't already show. No client PII, no unpublished pricing.

## Checklist

- [ ] Bundler ran clean; the file list matches the site's real sections.
- [ ] One card spot-checked headless — styled, content visible, images resolve.
- [ ] Correct project matched (or a create explicitly announced), and it's a design-system project.
- [ ] `finalize_plan` included `deletes: []`.
- [ ] `list_files` confirms; created-vs-updated and card count reported.
