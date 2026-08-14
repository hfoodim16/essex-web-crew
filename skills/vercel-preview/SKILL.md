---
name: vercel-preview
description: |
  Deploy a static site (prospect pitch, mockup, one-off build) to Vercel so it
  has a live, clickable URL to hand a non-technical client — no file to
  download, no login for them. Use whenever the user wants to "deploy a
  preview", "send this to the client", "get a shareable link", "put this
  online so he can see it", or otherwise needs a built site to go from local
  files to something a client can open in a browser. Free Vercel Hobby tier —
  unlimited deploys for this use case, don't hesitate to redeploy after every
  revision.
---

# vercel-preview

Takes a static site (HTML/CSS/JS, no build step needed) and gets it a live
`https://<project>.vercel.app` URL the user can hand straight to a client.

## Steps

1. **Confirm login.**
   ```bash
   cd <site-dir> && vercel whoami
   ```
   If it errors with "specified token is not valid", the user has to log in
   themselves — `vercel login` opens a browser for interactive auth, which you
   cannot click through for them. Give them the command and stop; resume once
   they confirm they're logged in.

2. **Fix the output directory before deploying, if needed.** Vercel guesses
   `outputDirectory` as `public/` if that folder exists, otherwise `.`. If the
   site has a `public/` folder that's just an assets folder (images, fonts —
   `index.html` still lives at the project root), that guess is wrong and the
   deploy 404s. Check for this case up front and write:
   ```json
   {"outputDirectory": "."}
   ```
   to `vercel.json` in the site root before deploying. (If `index.html` is
   genuinely inside `public/`, skip this — the default is already correct.)

3. **Deploy.**
   ```bash
   cd <site-dir> && vercel --prod --yes
   ```
   First deploy for a project links it automatically. Don't pass `--name` —
   it's deprecated and Vercel derives the project slug from the directory
   name. If the directory name has uppercase letters, the derived name can
   fail project-name validation (must be lowercase); if that happens, `cd`
   into a lowercase-named copy or symlink rather than fighting the flag.

4. **Verify before handing off.** Open the printed `Aliased` URL (the stable
   `https://<project>.vercel.app` one, not the per-deploy hash URL) in the
   Browser pane and screenshot it. Don't report the link as ready until you've
   seen the page actually render — a wrong `outputDirectory` or a missing
   asset path shows up as a blank page or 404 that only becomes obvious on
   load.

5. **Hand off the stable URL** — the `https://<project>.vercel.app` alias, not
   the hashed per-deployment URL. Redeploying (step 3 again) updates this same
   URL in place, so re-running this whole flow after a revision is exactly
   right and doesn't need a new link.

## Scope notes

- Hobby (free) tier: 100GB bandwidth/mo, 100 deployments/day, unlimited
  projects. Comfortably unlimited for pitch/preview use — don't ask before
  redeploying.
- This is for **previews**, not the client's permanent production domain.
  If a prospect signs and wants the real site on their own domain, that's a
  separate conversation (custom domain, possibly Vercel Pro, or their own
  host) — don't conflate the two.
