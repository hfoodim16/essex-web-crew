# Site Content Capture — Orange Valley Tree Experts

## PROVENANCE

- **Business:** Orange Valley Tree Experts, 20 Derwent Ave, Verona, NJ 07044 — (973) 857-9675
- **Site captured:** https://www.orangevalleytreeexperts.com/
- **Date captured:** 2026-08-13
- **Method:** Raw HTML pulled per-page with `curl` (browser User-Agent), then HTML-stripped to text. Raw HTML was used rather than a summarizing fetcher specifically so the broken CMS placeholder strings survive verbatim.
- **Platform:** **Hibu** — confirmed by markers in the page source: `HIBU_PRODUCTION`, `hibu-analytics.min.js`, asset CDN `le-cdn.hibuwebsites.com`, runtime `hibu.com/mnlt/production/6688/_dm/s/rt/dist/...`, `hibu-runtime.css`, and the Hibu-hosted legal links (`budurl.com/hibuprivacy`, `budurl.com/hibucookie`, `budurl.com/hibuconditionsofuse`, `budurl.com/hibunotice`). Content/NAP is driven by a **Yext** integration (`YextWidget`, `YextLoaded`, `YextPhoneRenderEvent`).
- **Pages found:** 7 in `sitemap.xml`, plus **1 unlisted orphan page** (`/video-splash-pop`) linked from a "Watch Our Video" button on 4 pages. **8 pages captured total.**

### Overall state — THE SITE IS BROKEN

**The Yext integration is not rendering.** Every place the site should print the phone number, email address, business hours, service area, address, year established, payment types, associations, specialties, and business attributes, it instead prints the raw unfilled CMS editor message:

> `This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.`

(Their live typo — "Knolwedge" — is reproduced exactly as it renders. Do not correct it.)

This string appears **on all 8 pages**. The message is self-refuting: it claims it "will not appear on the live site," and it is appearing on the live site.

**Occurrences in the raw HTML, counted 2026-08-13** (some are inside responsive/mobile duplicate blocks, so the number a visitor *sees* is lower — but every one of these is a field with no value behind it):

| Page | Occurrences | Page weight |
|---|---|---|
| `/` (Home) | 9 | 260 KB |
| `/tree-removal-services` | 9 | 161 KB |
| `/tree-pruning` | 9 | 164 KB |
| `/stump-grinding` | 9 | 163 KB |
| **`/about`** | **21** | **329 KB** |
| `/request-a-service` | 7 | 131 KB |
| `/contact` | 13 | 254 KB |
| **Total (7 sitemap pages)** | **77** | — |

### What is NOT wrong with the site (important for an honest pitch)

The infrastructure is fine — the failure is purely content/CMS. Do not pitch this as an old or non-mobile site, because it isn't:

- ✅ Served over **HTTPS with HSTS** (`strict-transport-security: max-age=31536000; preload`)
- ✅ Has a **responsive viewport meta tag** (`initial-scale=1, minimum-scale=1, maximum-scale=5, viewport-fit=cover`) and Hibu's responsive template
- ✅ Runs a **current jQuery (3.7.0)**, not a 2000s-era stack
- ✅ `x-frame-options: SAMEORIGIN` set
- ❌ But pages are **heavy for a 7-page brochure site** — 131–329 KB of HTML alone, before assets

**The accurate pitch is therefore not "your site is outdated" but "your site's content system has failed: it prints editor error messages where your phone number, email address, hours and service area should be, on every page, including the Contact page."**

**Consequences a builder must understand:**

1. **There is NO phone number visible in the body of any page** except where it was hard-typed into copy (the Request a Service form) or into a `<title>`/meta description. The footer "CALL US" block prints the placeholder.
2. **There is NO email address anywhere on the site.** The "EMAIL US" block prints the placeholder on all 8 pages. No `mailto:` and no email string exists anywhere in the source of any page.
3. **There is NO street address anywhere on the site.** The contact page's address slot prints ` , ` (an empty city/state comma) followed by the placeholder.
4. **There are NO business hours.** The About page renders the day labels Monday–Sunday with no times beside them; the hours value is the placeholder.
5. **There is NO service-area town list.** The site never names a single town it serves except "Verona" — the "SERVICE AREA" block is the placeholder on all 8 pages. Any town list must come from the client, not from this site.
6. **There is NO year-established value.** The About page's "Year Established" field is the placeholder. (The founding year appears only in prose on the Tree Pruning page.)
7. **The About page is almost entirely empty** — it is a shell of 10 labelled fields (About Us, Year Established, Products, Services, Specialties, Associations, Brands, Languages, Business Hours, Payment Types, Business Attributes) where **every single value is the placeholder.** The only two real strings on the whole page are the word "Venmo" and the day names.
8. **The "Watch Our Video" button is broken** — it links to `/video-splash-pop`, a page whose entire body content is the literal slug text `video-splash-pop`. There is no video embed, no YouTube/Vimeo URL, no video file anywhere in the source.
9. **Unreplaced Hibu template tokens leak into the footer of every page**: `{{placeholder_retargeting_pixel}}`, `{{placeholder_dpni}}`, and `{{placeholder_footer_reserve1}}` through `{{placeholder_footer_reserve7}}`.
10. **Two Hibu stock-template images are still referenced in the source** and have nothing to do with tree work: `japanese-light.jpg` and `living-room-interior-design-white-sofa.jpg` (both from Hibu's shared `md/dmip/` library, not the client's own asset folder).
11. **Social media is dead.** The 2015 version of this site had working Facebook and Twitter icons. The current site's social links are Yext-templated and never resolve — the source contains only unexpanded JavaScript template literals (`href="https://www.instagram.com/'+ yextData.entities[0].attributes.instagramHandle+'"`).

### Internal factual contradiction on the live site (do NOT resolve — carry both)

The site states its age three different ways:

- **"over 40 years"** — Home page, company description paragraph
- **"over 48 years"** — Home page (Tree Pruning card) AND Tree Pruning page ("We have over 48 years of experience in this field.")
- **"founded in 1976"** — Tree Pruning page

The "over 40 years" string is verifiably stale copy: the **2015** version of this site (Wayback, `20150801182443`) carried the identical sentence with "over 40 years" and a heading "40 Years of Experience". It was never updated when the rest of the copy moved to 48.

---

## Page: Home (https://www.orangevalleytreeexperts.com/)

**Page title:** `Orange Valley Tree Experts | Tree Care Services | Verona, NJ`
**Meta description:** `973-857-9675 - 24-hour emergency service. Free consultation. Tree removal. Tree pruning. Stump grinding.`

```
Orange Valley Tree Experts | Tree Care Services | Verona, NJ

The Best For Less

[button → /request-a-service] Request a Service

[logo image → /] https://le-cdn.hibuwebsites.com/a2da270233ab4752a5fa9527633f4b20/dms3rep/multi/opt/9279874_516x89-504w.jpg
   alt text: "Orange Valley Tree Experts-Logo"

[HEADER PHONE SLOT — should print the phone number:]
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

Verona , NJ Area

[NAV]
Home                    → /
Tree Removal Service    → /tree-removal-services
Tree Pruning            → /tree-pruning
Stump Grinding          → /stump-grinding
About                   → /about
Request a Service       → /request-a-service
Contact                 → /contact

Hi. Do you need any help?
Close
Share On:
Close

[HERO]
24/7 Emergency Tree Care Services

24-Hour Emergency Service
Free Consultation
Licensed Tree Care Operator

24-Hour Emergency Service | Free Consultation | Licensed Tree Care Operator

[HERO PHONE / CTA SLOT — should print the phone number:]
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

[mobile duplicate of the hero:]
24/7 Emergency Tree Care Services
24-Hour Emergency Service | Free Consultation | Licensed Tree Care Operator

[MOBILE HERO PHONE / CTA SLOT — should print the phone number:]
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

[SECTION HEADING]
Reliable Tree Care Operator

[SERVICE CARD 1 → /tree-removal-services]
image: https://le-cdn.hibuwebsites.com/a2da270233ab4752a5fa9527633f4b20/dms3rep/multi/opt/Tree-service01-349w.jpg  (alt: "Tree Removal Service")

Tree Removal

When you require tree removal services, turn to the professionals at Orange Valley Tree Experts. We specialize in tree removal.

If your tree is unhealthy, get in touch with us. We'll evaluate your tree’s health, make an accurate diagnosis, and provide the necessary treatment plan.

Learn More  → /tree-removal-services

[SERVICE CARD 2 → /tree-pruning]
image: https://le-cdn.hibuwebsites.com/a2da270233ab4752a5fa9527633f4b20/dms3rep/multi/opt/tree%2C-pruning-350w.jpg  (alt: "Tree Pruning")

Tree Pruning

Turn to our crew for quality and efficient tree pruning services. We have over 48 years of experience in the tree care field.

We provide crane service and bucket truck service so that we can meet all your tree care needs. Our rates are affordable. Call us [→ /contact] today for a FREE estimate.

Learn More  → /tree-pruning
Learn More  → /tree-pruning

[SERVICE CARD 3 → /stump-grinding]
image: https://le-cdn.hibuwebsites.com/a2da270233ab4752a5fa9527633f4b20/dms3rep/multi/opt/stump%2C-grinding-349w.jpg  (alt: "Stump Grinding")

Stump Grinding

Require stump grinding services? Choose our family-owned and operated business for effective stump grinding services.

Owner, Kevin Papocchia, is on-site to supervise every job while his wife, Karen, is in the office ready to set up your FREE consultation. Reach out to us today!

Learn More  → /stump-grinding
Learn More  → /stump-grinding

[COMPANY DESCRIPTION BLOCK]
Our #1 concern is the health of your trees and the safety of you, your home, and the surrounding neighbors and properties. Orange Valley Tree Experts is a family-owned and operated business that has been serving Verona, NJ and the surrounding towns for over 40 years. We remove and prune trees for our local residents, several local school districts, nursery schools, churches, synagogues, condominium complexes, health care facilities, nursing homes, museums, and many more. We provide a full range of services to meet all your tree care needs. Our friendly and honest staff focuses on excellent service and guarantees the satisfaction of our clients.

Watch Our Video
[link → /video-splash-pop]
play-icon2

[FOOTER]
SERVICE AREA
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

CALL US
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

EMAIL US
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

HOURS
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

[SOCIAL ICON ROW SLOT:]
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

[PAYMENT / ATTRIBUTES SLOT:]
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

Privacy Policy [→ http://budurl.com/hibuprivacy]
| Do Not Share My Information [→ http://budurl.com/hibucookie]
| Conditions of Use [→ http://budurl.com/hibuconditionsofuse]
| Notice and Take Down Policy [→ http://budurl.com/hibunotice]
| Website Accessibility Policy [→ http://b.link/accessibility]

© 2026
The content on this website is owned by us and our licensors. Do not copy any content (including images) without our consent.

Share by:

{{placeholder_retargeting_pixel}}
{{placeholder_dpni}}
{{placeholder_footer_reserve1}}
{{placeholder_footer_reserve2}}
{{placeholder_footer_reserve3}}
{{placeholder_footer_reserve4}}
{{placeholder_footer_reserve5}}
{{placeholder_footer_reserve6}}
{{placeholder_footer_reserve7}}
```

---

## Page: Tree Removal Service (https://www.orangevalleytreeexperts.com/tree-removal-services)

**Page title:** `Tree Removal | Tree Care Operators | Verona, NJ`
**Meta description:** `973-857-9675 - Orange Valley Tree Experts - 24-hour emergency service. Free consultation. Tree removal. Tree care operators.`

```
Tree Removal | Tree Care Operators | Verona, NJ

The Best For Less
[button → /request-a-service] Request a Service

[logo → /] https://le-cdn.hibuwebsites.com/a2da270233ab4752a5fa9527633f4b20/dms3rep/multi/opt/9279874_516x89-1920w.jpg  (alt: "Orange Valley Tree Experts-Logo")

[HEADER PHONE SLOT:]
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

Verona , NJ Area

[NAV — identical on every page]
Home / Tree Removal Service / Tree Pruning / Stump Grinding / About / Request a Service / Contact

[PAGE HEADER]
Tree Removal Service
Rely on Us for All Your Tree Removal Needs

24-Hour Emergency Service
Free Consultation
Licensed Tree Care Operator

24-Hour Emergency Service | Free Consultation | Licensed Tree Care Operator

[HERO PHONE SLOT:]
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

[mobile duplicate:]
Rely on Us for All Your Tree Removal Needs
24-Hour Emergency Service | Free Consultation | Licensed Tree Care Operator

[MOBILE HERO PHONE SLOT:]
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

[BODY]
Whether your tree is dead, diseased, or you just want it removed for aesthetic reasons, let us take care of your needs. Orange Valley Tree Experts can safely and efficiently remove any size tree. We will assess the health and location of the tree so that we can determine what state-of-the-art equipment and instruments of the trade will safely remove the tree.

Whether it is with one of our cranes, bucket trucks (cherry picker), or climbing the tree to remove it by hand, our team of professionals will get the job done. All branches and wood will be removed from the property. Our cleanup is so superb you won’t even know we were there except for, of course, the safely removed tree! Get in touch with our tree care operator for a FREE consultation.

24-hour emergency services are available at Orange Valley Tree Experts! Contact us [→ /contact] today.

We specialize in tree removal services.

Watch Our Video
[link → /video-splash-pop]
play-icon2

[FOOTER — identical to Home: SERVICE AREA / CALL US / EMAIL US / HOURS blocks all rendering:]
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.
(×6 occurrences)

Privacy Policy | Do Not Share My Information | Conditions of Use | Notice and Take Down Policy | Website Accessibility Policy

© 2026
The content on this website is owned by us and our licensors. Do not copy any content (including images) without our consent.

Share by:
{{placeholder_retargeting_pixel}}
{{placeholder_dpni}}
{{placeholder_footer_reserve1}} … {{placeholder_footer_reserve7}}
```

---

## Page: Tree Pruning (https://www.orangevalleytreeexperts.com/tree-pruning)

**Page title:** `Tree Pruning | Tree Trimming | Verona, NJ`
**Meta description:** `973-857-9675 - Orange Valley Tree Experts - 24-hour emergency service. Free consultation. Tree pruning. Tree trimming.`

```
Tree Pruning | Tree Trimming | Verona, NJ

The Best For Less
[button → /request-a-service] Request a Service

[logo → /] https://le-cdn.hibuwebsites.com/a2da270233ab4752a5fa9527633f4b20/dms3rep/multi/opt/9279874_516x89-1920w.jpg

[HEADER PHONE SLOT:]
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

Verona , NJ Area

[NAV — identical]
Home / Tree Removal Service / Tree Pruning / Stump Grinding / About / Request a Service / Contact

[PAGE HEADER]
Tree Pruning
Choose Our Tree Pruning Services

24-Hour Emergency Service
Free Consultation
Licensed Tree Care Operator

24-Hour Emergency Service | Free Consultation | Licensed Tree Care Operator

[HERO PHONE SLOT:]
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

[mobile duplicate:]
Choose Our Tree Pruning Services
24-Hour Emergency Service | Free Consultation | Licensed Tree Care Operator

[MOBILE HERO PHONE SLOT:]
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

[BODY — the most substantive technical content on the whole site; CARRY IN FULL]
Tree Pruning is the act of trimming a tree to improve the overall health and structure of the tree. Before we prune or trim any tree, we fully assess the tree. Pruning begins with apical dominance which includes pruning to promote a single central stem from the trunk to the top of the tree (on most trees). Next, we remove any dead, diseased, or defective branches.

Then, we need to prune competing branches which are branches that create clearance issues or perhaps compete with another branch because of size or location. Clearance over sidewalks, roadways, roofs, pools, playgrounds, or other structures must always be maintained to ensure safety to our clients.

Competition for light is another issue to be addressed while pruning. Some properties may need more light to come through for proper growth of trees, plants, and grasses.

[image] https://le-cdn.hibuwebsites.com/a2da270233ab4752a5fa9527633f4b20/dms3rep/multi/opt/Truck-1920w.jpg  (alt: "Truck")

About Our Tree Care Business

We're a family-owned and operated business that was founded in 1976. We have over 48 years of experience in this field. You will be pleased to know that we provide fast response time with all our services.

FREE consultations are available at Orange Valley Tree Experts! Contact us [→ /contact] today.

We provide 24-hour emergency services.

Watch Our Video
[link → /video-splash-pop]
play-icon2

[FOOTER — identical; SERVICE AREA / CALL US / EMAIL US / HOURS all rendering:]
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.
(×6 occurrences)

Privacy Policy | Do Not Share My Information | Conditions of Use | Notice and Take Down Policy | Website Accessibility Policy

© 2026
The content on this website is owned by us and our licensors. Do not copy any content (including images) without our consent.

Share by:
{{placeholder_retargeting_pixel}} … {{placeholder_footer_reserve7}}
```

---

## Page: Stump Grinding (https://www.orangevalleytreeexperts.com/stump-grinding)

**Page title:** `Stump Grinding | Property Cleanup | Verona, NJ`
**Meta description:** `973-857-9675 - Orange Valley Tree Experts - 24-hour emergency service. Free consultation. Stump grinding. Property grinding.`

```
Stump Grinding | Property Cleanup | Verona, NJ

The Best For Less
[button → /request-a-service] Request a Service

[logo → /] https://le-cdn.hibuwebsites.com/a2da270233ab4752a5fa9527633f4b20/dms3rep/multi/opt/9279874_516x89-1920w.jpg

[HEADER PHONE SLOT:]
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

Verona , NJ Area

[NAV — identical]
Home / Tree Removal Service / Tree Pruning / Stump Grinding / About / Request a Service / Contact

[PAGE HEADER]
Stump Grinding
Call Us to Grind Your Unwanted Tree Stumps

24-Hour Emergency Service
Free Consultation
Licensed Tree Care Operator

24-Hour Emergency Service | Free Consultation | Licensed Tree Care Operator

[HERO PHONE SLOT:]
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

[mobile duplicate:]
Call Us to Grind Your Unwanted Tree Stumps
24-Hour Emergency Service | Free Consultation | Licensed Tree Care Operator

[MOBILE HERO PHONE SLOT:]
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

[BODY — contains the only hard specification number on the site: "10-12 inches below grade"]
When we remove a tree from your property, the stump is left unless you would like it removed for perhaps replanting or aesthetic reasons. We grind the stumps 10-12 inches below grade allowing you to replant a tree or seed for grass without any issues. When a stump is ground, the remaining woodchips remain in the hole.

[image] https://le-cdn.hibuwebsites.com/a2da270233ab4752a5fa9527633f4b20/dms3rep/multi/opt/Stump-grainding-231cd0a4-1920w.jpg  (alt: "Stump Grinding")
   [NOTE: the client's own filename contains a typo — "Stump-grainding"]

Great Customer Services

Along with stump grinding services, our licensed tree care operator provides great property cleanup services. We provide estimates back within the same business day. If you have questions about our stump grinding or property cleanup services, get in touch with our friendly staff today.

24-hour emergency services are available at Orange Valley Tree Experts! Contact us [→ /contact] today.

We provide a FREE consultation.

Watch Our Video
[link → /video-splash-pop]
play-icon2

[FOOTER — identical; SERVICE AREA / CALL US / EMAIL US / HOURS all rendering:]
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.
(×6 occurrences)

Privacy Policy | Do Not Share My Information | Conditions of Use | Notice and Take Down Policy | Website Accessibility Policy

© 2026
The content on this website is owned by us and our licensors. Do not copy any content (including images) without our consent.

Share by:
{{placeholder_retargeting_pixel}} … {{placeholder_footer_reserve7}}
```

---

## Page: About (https://www.orangevalleytreeexperts.com/about)

**Page title:** `About Orange Valley Tree Experts | Verona, NJ Tree Trimming`
**Meta description:** `Learn more about Orange Valley Tree Experts. 24-hour emergency service. Free consultation. Tree removal. Call 973-857-9675.`

> **⚠️ THIS PAGE HAS ESSENTIALLY NO CONTENT.** It is a Yext-driven field shell. Every one of the 11 labelled fields renders the placeholder instead of a value. The only real strings on the page are the seven weekday names and the word "Venmo". A visitor clicking "About" learns nothing about the business — not the founding year, not the services, not the hours, not the associations. This is the single worst page on the site.

```
About Orange Valley Tree Experts | Verona, NJ Tree Trimming

The Best For Less
[button → /request-a-service] Request a Service

[logo → /] https://le-cdn.hibuwebsites.com/a2da270233ab4752a5fa9527633f4b20/dms3rep/multi/opt/9279874_516x89-504w.jpg

[HEADER PHONE SLOT:]
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

Verona , NJ Area

[NAV — identical]
Home / Tree Removal Service / Tree Pruning / Stump Grinding / About / Request a Service / Contact

[PAGE HEADER]
About
About Orange Valley Tree Experts

24-Hour Emergency Service
Free Consultation
Licensed Tree Care Operator

24-Hour Emergency Service | Free Consultation | Licensed Tree Care Operator

[HERO PHONE SLOT:]
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

[mobile duplicate:]
About Orange Valley Tree Experts
24-Hour Emergency Service | Free Consultation | Licensed Tree Care Operator

[MOBILE HERO PHONE SLOT:]
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

Hi. Do you need any help?
Close
Share On:
Close

[BODY — every label below is followed by the placeholder instead of its value]

About Us
   [VALUE MISSING — renders:] This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

Year Established
   [VALUE MISSING — renders:] This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

Products
   [VALUE MISSING — renders:] This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

Services
   [VALUE MISSING — renders:] This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

Specialties
   [VALUE MISSING — renders:] This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

Associations
   [VALUE MISSING — renders:] This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

Brands
   [VALUE MISSING — renders:] This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

Languages
   [VALUE MISSING — renders:] This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

Business Hours
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
   [ALL TIMES MISSING — the day names render with no hours beside them; renders:] This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.
   [second occurrence:] This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

Payment Types
   [VALUE MISSING — renders:] This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.
Venmo
   [^ "Venmo" is the ONLY real value that survives anywhere on this page]

Business Attributes
   [VALUE MISSING — renders:] This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

[FOOTER — identical; SERVICE AREA / CALL US / EMAIL US / HOURS all rendering:]
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.
(×6 occurrences)

Privacy Policy | Do Not Share My Information | Conditions of Use | Notice and Take Down Policy | Website Accessibility Policy

© 2026
The content on this website is owned by us and our licensors. Do not copy any content (including images) without our consent.

Share by:
{{placeholder_retargeting_pixel}} … {{placeholder_footer_reserve7}}
```

---

## Page: Request a Service (https://www.orangevalleytreeexperts.com/request-a-service)

**Page title:** `Request a Service From Orange Valley Tree Experts Verona NJ`
**Meta description:** `Request a service from Orange Valley Tree Experts. Tree removal. Tree pruning. Stump grinding.`

> **NOTE:** This is the ONLY page where the phone number is hard-typed into visible body copy rather than pulled from the broken Yext feed — it appears twice, as `(973) 857-9675`. It survives the outage because someone typed it manually.

```
Request a Service From Orange Valley Tree Experts Verona NJ

The Best For Less
[button → /request-a-service] Request a Service

[logo → /] https://le-cdn.hibuwebsites.com/a2da270233ab4752a5fa9527633f4b20/dms3rep/multi/opt/9279874_516x89-1920w.jpg

[HEADER PHONE SLOT:]
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

Verona , NJ Area

[NAV — identical]
Home / Tree Removal Service / Tree Pruning / Stump Grinding / About / Request a Service / Contact

[PAGE HEADER]
Request a Service
Request a Service

[FORM]
Website Request Form

Fill out this short form and an Orange Valley Tree Experts representative will contact you on the same business day. If you need immediate assistance, please call (973) 857-9675.

Name*
Phone
Email*
Services
   [dropdown/checkbox options:]
   Tree Removal Service
   Tree Pruning
   Stump Grinding
   Other
Message

[form success message:]
Thank you, your information has been submitted and we will contact you shortly. If you seek immediate attention please call (973) 857-9675.
Orange Valley Tree Experts

[form error message:]
Oops, there was an error sending your message.
Please try again later.

[FOOTER — identical; SERVICE AREA / CALL US / EMAIL US / HOURS all rendering:]
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.
(×6 occurrences)

Privacy Policy | Do Not Share My Information | Conditions of Use | Notice and Take Down Policy | Website Accessibility Policy

© 2026
The content on this website is owned by us and our licensors. Do not copy any content (including images) without our consent.

Share by:
{{placeholder_retargeting_pixel}} … {{placeholder_footer_reserve7}}
```

---

## Page: Contact (https://www.orangevalleytreeexperts.com/contact)

**Page title:** `Contact Orange Valley Tree Experts Verona NJ | 973-857-9675`
**Meta description:** `Call Orange Valley Tree Experts at 973-857-9675 for all your tree removal, tree pruning, or stump grinding services.`

> **⚠️ THE CONTACT PAGE CONTAINS NO CONTACT INFORMATION.** Phone, email, address, and hours all render the placeholder. The address slot renders as a bare ` , ` — an empty city/state pair. The page's only real hard data is the two license/registration numbers, which are hard-typed into the copy and therefore survive.

```
Contact Orange Valley Tree Experts Verona NJ | 973-857-9675

The Best For Less
[button → /request-a-service] Request a Service

[logo → /] https://le-cdn.hibuwebsites.com/a2da270233ab4752a5fa9527633f4b20/dms3rep/multi/opt/9279874_516x89-504w.jpg

[HEADER PHONE SLOT:]
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

Verona , NJ Area

[NAV — identical]
Home / Tree Removal Service / Tree Pruning / Stump Grinding / About / Request a Service / Contact

[PAGE HEADER]
Contact
Contact Orange Valley Tree Experts Today

[BODY]
If you are looking for quality service from experienced tree care professionals, contact Orange Valley Tree Experts! Ask about our FREE estimates!

Business Registration Number - #NJTC791091
License Tree Care Operating Number - 456

[CONTACT DETAILS BLOCK — all values missing]
SERVICE AREA
 ,
   [^ the street address / city / state renders as an empty comma]
   [VALUE MISSING — renders:] This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

PHONE/EMAIL
   [VALUE MISSING — renders:] This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.
   [second slot, VALUE MISSING — renders:] This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

HOURS
   [VALUE MISSING — renders:] This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.
   [second slot, VALUE MISSING — renders:] This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

Venmo
   [VALUE MISSING — renders:] This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

[FORM]
Send Us a Message
Get in Touch With Us

Please fill out this short form and we'll contact you shortly.

Name:
Email:
Phone:
Message:

[form success message:]
Thank you for contacting us. We’ll get back to you as soon as possible.

[form error message:]
Oops, there was an error sending your message.
Please try again later

[FOOTER — identical; SERVICE AREA / CALL US / EMAIL US / HOURS all rendering:]
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.
(×6 occurrences)

Privacy Policy | Do Not Share My Information | Conditions of Use | Notice and Take Down Policy | Website Accessibility Policy

© 2026
The content on this website is owned by us and our licensors. Do not copy any content (including images) without our consent.

Share by:
{{placeholder_retargeting_pixel}} … {{placeholder_footer_reserve7}}
```

---

## Page: video-splash-pop — ORPHAN / BROKEN (https://www.orangevalleytreeexperts.com/video-splash-pop)

**Page title:** `video-splash-pop`

> **⚠️ BROKEN PAGE.** Not listed in `sitemap.xml`, but linked from the "Watch Our Video" button on Home, Tree Removal, Tree Pruning, and Stump Grinding. The entire body content is the literal page slug. **There is no video** — no YouTube embed, no Vimeo embed, no `<video>` element, no media file URL anywhere in the source. Four pages promise a video that does not exist.

```
video-splash-pop

The Best For Less
[button → /request-a-service] Request a Service

[logo → /] https://le-cdn.hibuwebsites.com/a2da270233ab4752a5fa9527633f4b20/dms3rep/multi/opt/9279874_516x89-1920w.jpg

[HEADER PHONE SLOT:]
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.

Verona , NJ Area

[NAV — identical]
Home / Tree Removal Service / Tree Pruning / Stump Grinding / About / Request a Service / Contact

[BODY — this is the ENTIRE body content of the page:]
video-splash-pop

[FOOTER — identical; SERVICE AREA / CALL US / EMAIL US / HOURS all rendering:]
This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the live site, but only within the editor. The Yext Knowledge Tags are successfully installed and will be added to the website.
(×6 occurrences)

Privacy Policy | Do Not Share My Information | Conditions of Use | Notice and Take Down Policy | Website Accessibility Policy

© 2026
The content on this website is owned by us and our licensors. Do not copy any content (including images) without our consent.

Share by:
{{placeholder_retargeting_pixel}} … {{placeholder_footer_reserve7}}
```

---

## Asset inventory (all images referenced across the site)

Hibu serves these at multiple widths via a `-<width>w` suffix; the base file is listed.
Client's own asset folder: `https://le-cdn.hibuwebsites.com/a2da270233ab4752a5fa9527633f4b20/dms3rep/multi/opt/`

| File | Used as |
|---|---|
| `9279874_516x89.jpg` | **THE LOGO** — header on all 8 pages |
| `Tree-service01.jpg` | Home — Tree Removal card |
| `tree,-pruning.jpg` | Home — Tree Pruning card |
| `stump,-grinding.jpg` | Home — Stump Grinding card |
| `Truck.jpg` | Tree Pruning page body |
| `Stump-grainding-231cd0a4.jpg` | Stump Grinding page body (client's own filename typo: "grainding") |
| `Tree-Service.jpg` | referenced in source |
| `Tree-Pruning.jpg` | referenced in source |
| `Stumps.jpg` | referenced in source |
| `A1.jpg`, `A2.jpg` | referenced in source |
| `V_1.jpg` (also `mobile/V_1.jpg`) | referenced in source |

**Hibu shared-template stock leftovers still referenced in the source** (NOT the client's, and irrelevant to tree work — from `le-cdn.hibuwebsites.com/md/dmip/dms3rep/multi/opt/`):
- `japanese-light.jpg`
- `living-room-interior-design-white-sofa.jpg`

**Favicon:** `hibu.com/1c02a5e3326248d48476e9bb6fdaa9d8/site_favicon_16_1555599949070.ico` — a Hibu-hosted generic favicon, not a branded one.

---

## Prior site version — Wayback Machine (context, NOT current content)

The domain has been continuously live since at least **2011-02-02** (earliest Wayback capture). The pre-Hibu site (captured `20150801182443`) carried **real content the current site has since LOST**. Recorded here because it is the client's own prior published statement and a builder may want to ask about restoring it — but it is **2015 content and must be confirmed with the client before use**.

Prior page title: `Orange Valley Tree Experts | Tree Care | Verona, NJ`
Prior meta description: `FREE estimates. 24/7 Emergency Service. Satisfaction Guaranteed. Over 40 years of experience. Family owned and operated. Call today 973-857-9675.`

Prior nav (5 items): `HOME / TREE REMOVAL SERVICE / TREE PRUNING / STUMP GRINDING / CONTACT US`
Same tagline: `The Best For Less` — Same logo file: `9279874_516x89.jpg`
Had **working Facebook and Twitter icons** (`9295414_31x31.png` facebook, `9295417_31x31.jpg` twitter) — both gone from the current site.

Content present in 2015 and **absent from the current site**:

> "We do our best to save any tree, however sometimes a tree is so damaged and unsafe it cannot be repaired.  When you hire us, for a job we will tell you exactly what you need.  We will evaluate your tree’s health, make an accurate diagnosis, and provide the necessary treatment plan."

> "Our #1 concern is the health of your trees and the safety of you, your home and the surrounding neighbors and properties.  From pruning and trimming to the most difficult removals and even stump grinding, we provide our customers with the best possible service."

> "We offer crane service and a bucket truck service so that we can meet all your tree care needs. **When Hurricane Sandy and other storms hit New Jersey, we were right there to help our communities.** Our rates are affordable. We truly are “The Best For Less”.  Call us today for a free estimate."

> Headings: `40 Years of Experience` · `Outstanding Tree Services` · `24/7 Emergency Service`

> "Orange Valley Tree Experts is a family-owned and operated business that’s been serving Verona, NJ and the surrounding towns for over 40 years.  We remove and prune trees for our local residents, several local school districts, nursery schools, churches, synagogues, condominium complexes, health care facilities, nursing homes, museums, and many more.  We provide a full range of services to meet all your tree care needs.  Our friendly and honest staff focus on excellent service and guarantee the satisfaction of our clients.  **Owner Kevin Papocchia is on site to supervise every job while his wife Karen is in the office ready to set up your free estimate and consultation.**"

> Copyright line in 2015: `© 2015. The content on this website is owned by us and our licensors. Do not copy any content (including images) without our consent.`

**The Hurricane Sandy line is the single best piece of lost content** — a concrete, checkable, locally-resonant fact (Sandy hit NJ Oct 2012) that the current site dropped entirely.

**Note on the "over 40 years" contradiction:** the identical "over 40 years" sentence appears in the 2015 capture. The current site still carries it on the Home page while simultaneously claiming "over 48 years" twice. It is stale 2015 copy that was never updated, not a live disagreement about the founding date.

`FETCH NOTE:` The 2011 snapshot (`20110202092220`) and the 2015 contact-us page returned HTTP 503 from web.archive.org (rate limiting), so the pre-2015 design and the 2015 contact details were not captured. Not required for the build; noted for completeness.

---

## ⭐ RECOVERED: the missing Yext data (what the broken placeholders SHOULD be showing)

**This is the single most useful finding in this capture.** The site's placeholders fail because the Yext feed isn't rendering — but **that same Yext feed is syndicating correctly to third-party directories.** The values below were pulled from `mylocalservices.com`, which is demonstrably fed by the client's own Yext account (the page carries a Yext tracking pixel `pl.yext.com/plpixel?...&ids=8169491` and serves its images from Yext's CDN `a.mktgcdn.com`).

Source: https://www.mylocalservices.com/Orange+Valley+Tree+Experts-Verona-New+Jersey-21227597.html (captured 2026-08-13)

| Field the site fails to render | Recovered value (verbatim) |
|---|---|
| **EMAIL US** | `k.papocchiallc@yahoo.com` — a real, live `mailto:` link on that page |
| **HOURS / Business Hours** | `Mon-Sun 24hr` |
| **Payment Types** | `Cash, Check` — ⚠️ **conflicts with the "Venmo" that survives on the client's own About and Contact pages** |
| **Year Established** | `1975` — ⚠️ **conflicts with "founded in 1976" on their own Tree Pruning page** |
| **Languages** | `English` |
| **Specialties** | `Tree Removal` |
| **Services** | `All branches and wood will be removed from the property, Crane service and bucket truck service, Stump grinding, Tree care, Tree pruning and trimming services, Tree removal` |
| **Business type / categories** | `Shrub / Tree Services`, `Cranes & Derricks` |
| **Business Information** (the "About Us" field) | `Orange Valley Tree Experts provides tree removal services, tree pruning services, stump grinding services, and FREE consultations to the Verona, NJ area.` |

**⚠️ Every value above must still be confirmed with the client** — it is a syndicated feed, some of it stale, and it disagrees with their own site in two places. It is a starting point for the questionnaire, not an authority.

### Real photography exists — it is just not on the website

The same Yext feed carries **three real photographs of this business** that appear nowhere on their own site. All three verified live (HTTP 200) on 2026-08-13:

1. **`https://a.mktgcdn.com/p/tyBCYhKb9P_jMMIXtYsBCnVy_oqmVvvpxh35qKy9x6s/1908x751.jpg`** (1908×751) — A white chip-body truck in a residential driveway, photographed side-on. The door and body carry the full brand livery in navy serif caps. **Two phone numbers are painted on the truck: `973-857-9675` and `973-325-0280`, separated by a small navy pine-tree glyph, over `VERONA, NJ`.** The cab door additionally reads **`SNOW PLOWING`** — a service that appears nowhere on their website. A red crane/loader is working at frame right; cut brush lies in the foreground.
2. **`https://a.mktgcdn.com/p/RLEVR26n9hYUEm8p7FMXj4JnW3P66g8OQDf_O-S6zM8/1876x742.jpg`** (1876×742) — **The full crew and family**, ~13 people lined up between the white chip truck and a red crane truck. Men in navy company tee-shirts with a chest logo, orange and yellow hard hats with ear defenders, work boots. A woman holding an infant, a second woman, a man holding a toddler, and a young girl in a pink dress stand at the left end — the family-business claim, visibly true. A Stihl chainsaw rests on the ground in front.
3. **`https://a.mktgcdn.com/p/PiL6mEro2hFAyFW-c3zmUPnGqmcvQIde0aSHia6LdMc/1869x734.jpg`** (1869×734) — The full fleet on a clear day: a yellow **Bandit** chipper at left, the white chip truck centre (`ORANGE VALLEY TREE EXPERTS` / `973-857-9675 ✦ 973-325-0280` / `VERONA, NJ`), and a red boom/crane truck at right with **`ORANGE VALLEY TREE EXPERTS` lettered along the boom**, loaded with large trunk sections on the flatbed. Crew of ~8 standing between the trucks.

**Implication for a rebuild:** the "real photos or labeled placeholders, never stock" requirement can likely be met with the client's own images. Confirm ownership and get originals from Kevin — do not hotlink Yext's CDN on a shipped site.

---

## What is NOT on this site (the build must source these from the client)

Every item below is genuinely absent — it is not that we failed to find it, it is that the site does not contain it:

- ❌ **Email address** — no `mailto:` and no email string in the source of any of the 8 pages
- ❌ **Street address** — the contact page renders an empty ` , `
- ❌ **Business hours** — day names with no times
- ❌ **Service-area town list** — only the word "Verona" ever appears; no town list
- ❌ **Year established as a data field** — only in Tree Pruning prose
- ❌ **Any customer review or testimonial** — the site has no testimonial section at all, on any page
- ❌ **Any named institutional client** — the nine categories are named, but no individual school, church, or complex is
- ❌ **Any staff photo, crew photo, or photo of Kevin or Karen**
- ❌ **Any insurance statement** ("fully insured", coverage amounts) — absent entirely
- ❌ **Any ISA / TCIA / NJ Board of Tree Experts membership or certification claim**
- ❌ **Any pricing, price range, or minimum charge**
- ❌ **Any working social media link**
- ❌ **The video the "Watch Our Video" button promises**
