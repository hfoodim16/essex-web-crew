# Delivery to Corey — full procedure

> Extracted from CLAUDE.md (token diet, 2026-08-03): read ON DEMAND by the role that
> needs it, instead of by every teammate at spawn. CLAUDE.md keeps the binding summary;
> where the two ever disagree, CLAUDE.md wins.

## Delivery to Corey

Corey Rapkin (**crapkin@foradigital.com**) is the one who puts a site live via Netlify
Drop — he needs the packaged zip, not loose files.

**The Critic's sign-off means the BUILD is done. It does not mean "publish it."**
Delivery has its own gate, below.

**Only the lead session does this.** Teammates have no Gmail tools; the Critic signals
sign-off, the lead performs delivery. Harry can also trigger it any time with
"deliver `<slug>`".

Delivery sends a **zip for deploying**. That's separate from keeping the two Macs in sync
— for that, invoke **`github-push`** after a run finishes and **`github-pull`** before
starting one. A signed-off prospect should go up to GitHub as well as out as a zip, so
whoever picks it up next has the source.

**The procedure:**

0. **Check the signed release form FIRST — this is a hard gate.** Confirm with Harry that
   the client has returned a **signed** `release-form.pdf`. The Critic only verifies the
   form exists and is filled correctly; it cannot know whether the client signed it. No
   signature on file → **stop here.** Say what's missing and let the package wait. Nothing
   goes to Corey, because the next thing that happens to that zip is a real business's
   name, phone number, and address appearing on the public internet, and an AI score is
   not the client's permission to publish. A signed-off `audit.md` means the build is
   finished, never that it may go live.

1. Package the site:
   ```bash
   pipeline/package-site.sh <slug>
   ```
   This writes `prospects/<slug>/<slug>-site.zip` — the whole site, correctly named
   `index.html` at the top level, assets included, dev scratch stripped.

   **The packager is gated and will refuse a failing build.** It re-runs the detector
   against the staged copy, greps for placeholder leakage (`[placeholder: …]`,
   `[… — confirm]`, `PLACEHOLDER_TOKENS`), and checks the build has a `design-memory.md`
   row. Any failure → it names the problem, writes nothing, and exits 2. This exists
   because gee-kay's `deploy-ready/` folder shipped with a visible
   `[placeholder: a short note from owner…]` and 27 contrast failures in it — packaging
   used to run after critique and check nothing. `--force` packages anyway but renames
   the artifact `<slug>-site-UNGATED.zip`, so an override is visible in the filename.

   **Then publish it to Claude Design** — invoke the `design-push` skill on
   `prospects/<slug>/mockup/` with the client's name. The finished site lands at
   claude.ai/design as a card-per-section design system you can refine visually.
   One DesignSync permission prompt per push; that's inherent to the tool and can't
   be automated away. **After a revision round, run `/design-push` again** — it writes
   the same paths, so the same project updates in place rather than duplicating.

   **It's a round trip, not a one-way publish.** The repo stays the source of truth and a
   re-push overwrites, so edits made *inside* Claude Design have to come back to the site
   first — that's **`/design-pull`**, which finds them on its own (it re-bundles the source
   and diffs, so nobody has to remember what they changed) and verifies every write-back by
   round-trip. `/design-push` refuses to run while unpulled edits exist, so refining a site
   in the Design pane can't silently cost you the work.

2. Create a Gmail draft with the Gmail MCP `create_draft` tool:
   - **to:** `crapkin@foradigital.com`
   - **subject:** `<Business Name> website — ready to put live on Netlify`
   - **body:** four lines, no fluff — which business this is, drag the attached zip onto
     https://app.netlify.com/drop, claim the site and rename the subdomain to
     `<slug>.netlify.app`, reply with the live URL.
   - **attachment:** if the zip is **≤ 200 KB**, attach it (`base64 -i <zip>`, mimeType
     `application/zip`). If it's larger, create the draft *without* the attachment and
     open the body with a line Harry can't miss:
     `ATTACH BEFORE SENDING: <absolute path to zip>`. Base64-ing a multi-MB file through
     a tool call is not workable — image-heavy sites will always take this path, and a
     mockup carrying a vendored GSAP tier (~45 KB zipped) may tip a borderline one over.

3. **Draft only — never send.** Report the draft ID and the zip path back to Harry, and
   say plainly whether the zip was attached or he has to attach it himself.

4. **When Corey replies with the live URL, register the site for monitoring.** Add it to
   `~/Projects/site-caretaker/sites.json` (the `caretaker` agent owns that file and its
   format — hand it the URL and let it do the write). This is the ONLY thing that puts a
   published site under the hourly uptime/DNS/TLS monitor. Skip it and the site is live,
   carrying a client's phone number, and watched by nobody. A delivery isn't finished at
   the draft — it's finished when the live URL is in the registry.

