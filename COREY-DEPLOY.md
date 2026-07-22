# Putting a site live on Netlify

Harry emails you a single zip file, e.g. `gee-kay-landscaping-site.zip`, once a site is
finished. Everything the site needs is inside it. Don't open it up and forward individual
files — the whole zip is the deliverable.

## First time putting a site live

1. Download the zip. Leave it zipped.
2. Go to **https://app.netlify.com/drop**
3. Drag the zip file onto the page.
4. Wait a few seconds. You get a live URL like `random-name-123.netlify.app`. That's it.

If you want the site to stick around permanently, click **Claim this site** and log into
(or create) a free Netlify account. Unclaimed sites are temporary.

## Giving it a better URL

Once the site is claimed: **Site configuration → Domain management → Options → Edit site name**.
Change it to something like `gee-kay-landscaping.netlify.app` before sending it to a prospect.

## Updating a site later

Open the site in Netlify → **Deploys** tab → drag the new zip onto the drop zone at the
bottom. It replaces the live version in seconds. Don't create a second site for an update.

## Why the zip matters

We used to email a bare `index.html`. When you download the same attachment twice, your
browser silently renames it — `index-4.html`, `index (1).html`, and so on. Netlify and
Vercel only serve a file named exactly `index.html` as the homepage, so a renamed file
gives you a 404 every time. The zip keeps the filenames intact, and it also carries the
stylesheet, scripts, images, and extra pages that some sites need.

## If something looks wrong

- **404 / "Page not found":** the zip got unpacked and repacked somewhere along the way,
  and `index.html` is now nested in a subfolder or renamed. Ask Harry to re-send the zip.
- **Site loads but looks unstyled:** the CSS file didn't make it. Same fix — re-send.
