# Candidates — US-wide run — 2026-08-18

Territory override: nationwide (not Essex County), authorized by Harry in-session for this
run only. Prospecting team only — nothing was built. **No business was contacted.**
Free tools only: `WebSearch` plus page fetches via `rtk curl` (`WebFetch` was denied
session-wide). No Firecrawl, no Perplexity, no paid image generation.

Every candidate below is verified against all three mandatory qualifiers: (1) a findable
literal email address, (2) proof of current activity, (3) a weak/absent website with
specific observed evidence. **The lead re-fetched and read every site in the shortlist
personally** — the HTML observations below are firsthand, not relayed.

## Shortlist — the 3

| # | Business | Town | State | Niche | Web presence | Established signal | Contact | Qualifies? |
|---|----------|------|-------|-------|---------------|---------------------|---------|-----------|
| 1 | Maggio & Sons Land Development Co. | Round Top / Cairo | NY | Land development, septic, excavation, paving | Live site, HTML 4.0 Dreamweaver relic | Est. 1975 (per own About page) | Estimating@MaggioandSons.com · 518-622-9882 | yes |
| 2 | Avery Septic Service, LLC | Somers | CT | Septic pumping, inspection, repair | Site is a "Under Maintenance" placeholder — no real site | "Family Owned & Operated Since 1960" (own site footer) | info@alwaysavery.com · 860-749-9964 | yes |
| 3 | Northern Auto Repair, LLC | Havre | MT | Auto repair | Single page, http-only, nav commented out | Google Analytics property registered 2017; 68 reviews | info@northernauto.repair · 406-265-2841 | yes |

### 1. Maggio & Sons Land Development Company — Round Top / Cairo, NY
- **Email:** `Estimating@MaggioandSons.com` — live `mailto:` link in the homepage footer of
  `https://maggioandsons.com/`. Verified firsthand in the fetched HTML.
- **Active proof:** Yelp business listing "Updated June 2026", 16 reviews, 69 photos
  (`https://www.yelp.com/biz/maggio-and-sons-land-development-round-top`). Birdeye profile
  shows 47 reviews / 4.7 rating. Phone and address on the listings match the live site.
- **Website problem** (all read directly in the served HTML):
  - `<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">` — HTML 4.0, not HTML5
  - `charset=windows-1252`
  - **No `viewport` meta tag** — the site cannot respond to mobile screens
  - Table-based layout with fixed pixel widths (`width="625"`, `width="577"`, `width="178"`)
    and `images/dot.gif` spacer GIFs
  - Dreamweaver-generated rollover JS: `MM_preloadImages()`, `MM_swapImage()`,
    `MM_showHideLayers()`
  - Presentational `<font size="3">` / `<font color="#ff0000">` tags throughout
  - Dead `fb-like-box` Facebook widget (the plugin Facebook deprecated years ago) — renders
    as nothing
  - YouTube links still carrying the `&feature=plcp` parameter, a 2012-era YouTube URL form
- **Services (from their own copy):** blacktop paving, septic systems and pumping, perk
  tests, excavation, concrete, landscaping, hydroseeding, retaining walls, decks and patios,
  ponds, snow plowing and salt sanding.
- **Sources:** `https://maggioandsons.com/` · `https://www.yelp.com/biz/maggio-and-sons-land-development-round-top`

### 2. Avery Septic Service, LLC — Somers, CT
- **Email:** `info@alwaysavery.com` — `mailto:` link on `https://www.alwaysavery.com/`.
  Verified firsthand.
- **Active proof:** Yelp business listing "Updated February 2026"
  (`https://www.yelp.com/biz/avery-septic-services-somers`). Angi rating 5.0/5. Active BBB
  profile. Current listed hours Mon–Fri 8:00–5:00.
- **Website problem:** there is effectively **no website**. The entire domain serves a
  single 2,222-byte page titled `Avery Septic Service | Under Maintenance`, reading
  "Website Under Maintenance — We're making improvements to our website." No services, no
  pages, no navigation — just a logo, phone, email, and the line "Licensed • Insured •
  Family Owned & Operated Since 1960". Verified firsthand by fetching and reading the full
  document.
  - *Correction to an earlier report in this run:* the placeholder page **does** carry a
    viewport meta tag. The defect is not that it's unresponsive — it's that there is no
    site behind it at all.
- **Sources:** `https://www.alwaysavery.com/` · `https://www.yelp.com/biz/avery-septic-services-somers`

### 3. Northern Auto Repair, LLC — Havre, MT
- **Email:** `info@northernauto.repair` — `mailto:` link in the header social box of
  `http://northernauto.repair/`. Verified firsthand.
- **Active proof:** Yelp listing "Updated May 2026"
  (`https://www.yelp.com/biz/northern-auto-repair-havre`). Birdeye: 68 reviews, 4.7 rating.
  CARFAX: 12 verified-customer reviews, 5.0. Current hours in the site's own schema.org
  block (Mon–Fri 07:30–17:30).
- **Website problem** (all read directly in the served HTML):
  - **No HTTPS at all** — `http://northernauto.repair/` returns 200 and stays on `http://`
    through the redirect chain; every internal URL and the schema.org `@id` are `http://`
  - **Single page with no navigation** — the entire nav block is commented out in the
    source: `<!--div id="menu">...</div-->`, and the commented menu contains only "Home"
  - Still firing **Google Universal Analytics** (`gtag('config','UA-107131578-1')`) — a
    property type Google shut off in July 2023, so the tag has collected nothing for 3 years
  - Visible mojibake from a character-encoding fault: "We**Â** are open every weekday…" in
    the body copy and "**Â**© 2026" in the footer
  - Google Maps embed carrying the timestamp `4v1513223746444` — December 2017
  - Runs on "Avallo, Custom CMS", a legacy platform the owner almost certainly can't edit
- **Sources:** `http://northernauto.repair/` · `https://www.yelp.com/biz/northern-auto-repair-havre` · `https://reviews.birdeye.com/northern-auto-repair-156044667101451`

## Backup candidate (verified site defect; activity evidence weaker)

### King Septic Service, Inc. — Cedar Hill, MO
- **Email:** `contact@kingsepticservice.com` — `mailto:` in both the header and footer of
  `http://www.kingsepticservice.com/`. Verified firsthand.
- **Website problem** (read directly): footer reads
  `King Septic Service INC. Copyright ©2012`; **empty `<title></title>`** (no page title at
  all — a serious SEO defect); http-only, no HTTPS; jQuery **1.5.1** (released 2011) with a
  1.4.2 fallback; IE6/7/8/9 conditional-comment stylesheets and the `dd_belatedpng.js` IE6
  PNG fix; page filenames containing spaces (`King_Tank Cleaning.html`); typos in their own
  body copy ("establsihed", "equiptment").
- **Active proof — weaker:** 4.8/5 from 53 Google reviews and an active Facebook page, but
  **no individual review or post dated within the last 12 months could be confirmed** from a
  page that could be fetched. Held out of the top 3 for that reason alone.
- **Currency note for Harry:** their site says the company "has been owned and operated by
  **John** Ganey since 1980"; current directory listings name **Paul** Ganey (John's son,
  also named on the site) as owner. Worth a casual confirm on a call — not a blocker.
- **Sources:** `http://www.kingsepticservice.com/` · `https://www.septicseeker.com/missouri/cedar-hill/king-septic-service-inc-cedar-hill`

## Rejected — and why (useful signal for the next run)

The binding filter is the **email**, not the bad website. Bad websites are everywhere;
businesses that publish a real address on a fetchable page are rare. The second most common
kill was discovering the business had already modernized once the site was actually opened.

| Business | Location | Failed qualifier |
|---|---|---|
| AAA Ajax Pumping Service | Phoenix, AZ | No email — contact form only (site itself was excellent evidence: WordPress 3.9.40 from 2014, http-only) |
| Alexander Drilling, Inc. | Hill City, SD | No email — contact form only (WordPress 5.0.4, http-only, images orphaned on a developer's personal domain) |
| Big Bend Septic Tank Co. | Tallahassee, FL | Email traceable only to a Cloudflare-blocked aggregator; freshest viewable reviews 7–8 years old |
| High Country Portables | Meeker, CO | Email only via a blocked aggregator; FMCSA record confirms the business is real but carries no email |
| Kass Septic Services | Arlington, VT | No email published anywhere |
| Mountain View Tree Service | Rathdrum, ID | No confirmable email; aggregators conflate it with a possibly-separate business |
| W.E. Miller Tree Service | Westerville, OH | Site republished Jan 2026 on a modern platform with HTTPS — no longer a bad site |
| American Tree Service | Priest River, ID | Ancient site found, but they also run a current professional site at a second domain |
| Frost Septic LLC | Levant, ME | Modern responsive site (viewport, Bootstrap 4.6, 2026 copyright) |
| Smitty's Nursery & Landscape | Windham, NY | Modern responsive WordPress theme |
| Patterson Pest Control | Athens, NY | Modern GoDaddy builder site, responsive |
| Town and Country Auto Repair | Mount Airy, MD | Modern responsive site |
| The Repair Shop | Mifflinburg, PA | Modern GoDaddy builder site |
| Unclog Sewer Drain Service | Tannersville, NY | Has its own active website |
| Van Etten & Sons Tree and Crane | Ravena, NY | No reviews / not yet rated; also has a modern site on a related domain |
| Sierra Pest Control · Little Stinker Septic · AAA Organic Pest Control · AAA Sewer Service · Arizona Joe Tree Care · Frank Chapman Law Office · Steele Veterinary Clinic | ID / NV / AZ | All have current, mobile-friendly sites |
| Wyoming Tree Care | WY | Abandoned Weebly page injecting a script from an unrelated domain; activity unconfirmable |
| Dan's Septic Service | Prattsville, NY | No website (good) and email on a county directory, but freshest dated evidence was a May 2025 Facebook post — outside the ~12-month window |
| KJ Enterprises | Coxsackie, NY | No website (good), email on a county directory, strong ratings — but no dated activity evidence within 12 months could be pinned from a fetchable page |

## Method note

The single most productive source for real email addresses was a **county-run community
business directory** (Greene County NY's `buyingreene.com`), which publishes literal
`mailto:` links. National aggregators — BBB, Angi, Yellow Pages, Manta, Yelp, Birdeye,
chamberofcommerce.com — are either Cloudflare-blocked or render contact details
client-side, so they are close to useless for this qualifier. **Next run: start from
county and chamber directories, not national aggregators.**

<!-- RUN COMPLETE: 3 shortlisted, 1 backup -->
