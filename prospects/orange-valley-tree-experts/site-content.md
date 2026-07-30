# Site content capture — Orange Valley Tree Experts

**Source:** https://www.orangevalleytreeexperts.com/
**Captured:** 2026-07-29
**Platform:** Hibu (assets on `le-cdn.hibuwebsites.com`) with a **broken/unconfigured Yext
Knowledge Tags integration**.
**Completeness:** all 7 nav pages + 1 orphan page captured. No page failed to fetch.

> This file is the **content-parity source of truth**. Everything the old site says must
> appear on the new site or be listed as deliberately dropped in `website-plan.md`.

## Navigation structure (link labels verbatim)

| Label | URL |
|---|---|
| Home | `/` |
| Tree Removal Service | `/tree-removal-services` |
| Tree Pruning | `/tree-pruning` |
| Stump Grinding | `/stump-grinding` |
| About | `/about` |
| Request a Service | `/request-a-service` |
| Contact | `/contact` |

Plus one **orphan page not in the nav**, linked from the service pages: `/video-splash-pop`.

## THE SITE-WIDE DEFECT — read this before using anything below

This exact string renders on **every one of the 7 pages**, in the `SERVICE AREA`, `CALL US`,
`EMAIL US`, and `HOURS` blocks:

> "This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the
> live site, but only within the editor. The Yext Knowledge Tags are successfully installed
> and will be added to the website."

**The misspelling "Knolwedge" is theirs and is live.** Verified by direct fetch 2026-07-29.
Some instances spell "Knowledge" correctly; both variants ship.

`/request-a-service` additionally leaks raw template tokens:
`{{placeholder_retargeting_pixel}}`, `{{placeholder_dpni}}`,
`{{placeholder_footer_reserve1}}` through `{{placeholder_footer_reserve7}}`.

**Consequence for content parity:** the site's **phone, email, hours, and service-area town
list do not exist as capturable content.** They were never filled in. Those four items are
`[placeholder]` gaps to be sourced from the client, not blocks to transfer.

---

## Page: Home (https://www.orangevalleytreeexperts.com/)

**Tagline (beside logo, all pages):**
> The Best For Less

**Location line:**
> Verona, NJ Area

**Hero H1:**
> 24/7 Emergency Tree Care Services

**Trust strip (three items):**
> 24-Hour Emergency Service
> Free Consultation
> Licensed Tree Care Operator

**Tree Removal Service**
> When you require tree removal services, turn to the professionals at Orange Valley Tree
> Experts. We specialize in tree removal. If your tree is unhealthy, get in touch with us.
> We'll evaluate your tree's health, make an accurate diagnosis, and provide the necessary
> treatment plan.

**Tree Pruning**
> Turn to our crew for quality and efficient tree pruning services. We have over 48 years of
> experience in the tree care field. We provide crane service and bucket truck service so
> that we can meet all your tree care needs. Our rates are affordable. Call us today for a
> FREE estimate.

**Stump Grinding**
> Require stump grinding services? Choose our family-owned and operated business for
> effective stump grinding services. Owner, Kevin Papocchia, is on-site to supervise every
> job while his wife, Karen, is in the office ready to set up your FREE consultation. Reach
> out to us today!

**Company Overview**
> Our #1 concern is the health of your trees and the safety of you, your home, and the
> surrounding neighbors and properties. Orange Valley Tree Experts is a family-owned and
> operated business that has been serving Verona, NJ and the surrounding towns for over 40
> years.

> We provide a full range of services to meet all your tree care needs. Our friendly and
> honest staff focuses on excellent service and guarantees the satisfaction of our clients.

**Client list — exact sentence** (re-captured directly on 2026-07-29 to fix a paraphrase in
the first pass; this is the literal wording):
> We remove and prune trees for our local residents, several local school districts, nursery
> schools, churches, synagogues, condominium complexes, health care facilities, nursing
> homes, museums, and many more.

No individual client is named anywhere on the site.

**Footer:**
> © 2026 The content on this website is owned by us and our licensors. Do not copy any
> content (including images) without our consent.

**Footer links** — all Hibu boilerplate, all off-site, none of it theirs:
Privacy Policy `http://budurl.com/hibuprivacy` · Do Not Share My Information
`http://budurl.com/hibucookie` · Conditions of Use `http://budurl.com/hibuconditionsofuse` ·
Notice and Take Down Policy `http://budurl.com/hibunotice` · Website Accessibility Policy
`http://b.link/accessibility`

---

## Page: Tree Removal Service (https://www.orangevalleytreeexperts.com/tree-removal-services)

**Page title:** Tree Removal | Tree Care Operators | Verona, NJ
**H1:**
> Rely on Us for All Your Tree Removal Needs

> Whether your tree is dead, diseased, or you just want it removed for aesthetic reasons,
> let us take care of your needs. Orange Valley Tree Experts can safely and efficiently
> remove any size tree.

> Whether it is with one of our cranes, bucket trucks (cherry picker), or climbing the tree
> to remove it by hand, our team of professionals will get the job done.

> All branches and wood will be removed from the property. Our cleanup is so superb you
> won't even know we were there except for, of course, the safely removed tree!

> 24-hour **emergency** services are available at Orange Valley Tree Experts!

*("emergency" is bolded on the page.)*

> We specialize in tree removal services.

---

## Page: Tree Pruning (https://www.orangevalleytreeexperts.com/tree-pruning)

**H1:**
> Choose Our Tree Pruning Services

> Tree Pruning is the act of trimming a tree to improve the overall health and structure of
> the tree. Before we prune or trim any tree, we fully assess the tree. Pruning begins with
> apical dominance which includes pruning to promote a single central stem from the trunk to
> the top of the tree (on most trees). Next, we remove any dead, diseased, or defective
> branches.

> Then, we need to prune competing branches which are branches that create clearance issues
> or perhaps compete with another branch because of size or location. Clearance over
> sidewalks, roadways, roofs, pools, playgrounds, or other structures must always be
> maintained to ensure safety to our clients.

> Competition for light is another issue to be addressed while pruning. Some properties may
> need more light to come through for proper growth of trees, plants, and grasses.

> We're a family-owned and operated business that was founded in 1976. We have over 48 years
> of experience in this field.

**This is the best writing on the site** — real arborist voice, specific and technical.
Carry all of it.

---

## Page: Stump Grinding (https://www.orangevalleytreeexperts.com/stump-grinding)

**Page title:** Stump Grinding | Property Cleanup | Verona, NJ
**H1:**
> Call Us to Grind Your Unwanted Tree Stumps

> When we remove a tree from your property, the stump is left unless you would like it
> removed for perhaps replanting or aesthetic reasons. We grind the stumps 10-12 inches
> below grade allowing you to replant a tree or seed for grass without any issues.

**H2:** Great Customer Services
> Along with stump grinding services, our licensed tree care operator provides great
> property cleanup services. We provide estimates back within the same business day.

---

## Page: About (https://www.orangevalleytreeexperts.com/about)

**H1:**
> About Orange Valley Tree Experts

**THIS PAGE IS ENTIRELY BROKEN.** Every section heading renders; **every content field
beneath every heading is the Yext placeholder string.** Headings present, in order:

`About Us` · `Year Established` · `Products` · `Services` · `Specialties` · `Associations` ·
`Brands` · `Languages` · `Business Hours` (Monday through Sunday, each row a placeholder) ·
`Payment Types` · `Business Attributes` — plus the site-wide `SERVICE AREA` / `CALL US` /
`EMAIL US` / `HOURS` blocks.

**The only real content on the entire About page is one word, under Payment Types:**
> Venmo

There is no About copy to transfer. The homepage "Company Overview" above is the firm's de
facto About text.

---

## Page: Request a Service (https://www.orangevalleytreeexperts.com/request-a-service)

**Page title:** Request a Service From Orange Valley Tree Experts Verona NJ
**Headings:** `Request a Service` · `Website Request Form` · `Free Text`

> Fill out this short form and an Orange Valley Tree Experts representative will contact you
> on the same business day. If you need immediate assistance, please call (973) 857-9675.

**Success message:**
> Thank you, your information has been submitted and we will contact you shortly. If you seek
> immediate attention please call (973) 857-9675.

**Error message:**
> Oops, there was an error sending your message. Please try again later.

**Form fields:** `Name*` · `Phone` · `Email*` · `Services` (dropdown: **Tree Removal Service,
Tree Pruning, Stump Grinding, Other**) · `Message`

**Note:** this form's copy is the **only place on the entire site where the phone number
actually renders to a visitor.**

---

## Page: Contact (https://www.orangevalleytreeexperts.com/contact)

**H1:**
> Contact Orange Valley Tree Experts Today

> If you are looking for quality service from experienced tree care professionals, contact
> Orange Valley Tree Experts! Ask about our FREE estimates!

**Credentials — verbatim label text (their own wording, errors included):**
> Business Registration Number - #NJTC791091
> License Tree Care Operating Number - 456

**Form fields:** `Name` · `Email` · `Phone` · `Message`
**Success:** "Thank you for contacting us. We'll get back to you as soon as possible."
**Error:** "Oops, there was an error sending your message. Please try again later"

**Verified by direct fetch 2026-07-29: this Contact page contains no rendered phone number,
no email, no street address, no hours, and no map.** All four blocks are the Yext
placeholder. The phone appears only in the browser tab title. A contact page with no contact
information.

---

## Page: /video-splash-pop (orphan — not in nav)

Near-empty leftover. Contains the tagline "The Best For Less", the nav, "Verona, NJ Area",
the four placeholder blocks, and the footer. Holds a video element labeled
`video-splash-pop` **with no video URL resolved.** Nothing to carry; drop it.

---

## Assets on the existing site (direct URLs, all downloadable)

**Logo** — used in the header of all 7 pages, alt text "Orange Valley Tree Experts Logo".
Verified live 2026-07-29: HTTP 200, `image/jpg`, 16,951 bytes.
- `https://le-cdn.hibuwebsites.com/a2da270233ab4752a5fa9527633f4b20/dms3rep/multi/opt/9279874_516x89-1920w.jpg`
- smaller variant: `…/9279874_516x89-504w.jpg`
- Native size **516×89 px** → a wide horizontal letterhead-style lockup, roughly 5.8:1.
- **It is a JPEG, not a transparent PNG/SVG** — it carries a solid background box, which
  matters if the new header is dark. Builder should trace or matte it.

**Work photos** (all Hibu CDN — download, never hotlink):
- `https://le-cdn.hibuwebsites.com/a2da270233ab4752a5fa9527633f4b20/dms3rep/multi/opt/Tree-service01-349w.jpg`
- `https://le-cdn.hibuwebsites.com/a2da270233ab4752a5fa9527633f4b20/dms3rep/multi/opt/tree%2C-pruning-350w.jpg`
- `https://le-cdn.hibuwebsites.com/a2da270233ab4752a5fa9527633f4b20/dms3rep/multi/opt/stump%2C-grinding-349w.jpg`
- `https://le-cdn.hibuwebsites.com/a2da270233ab4752a5fa9527633f4b20/dms3rep/multi/opt/Stump-grainding-231cd0a4-1920w.jpg` (their filename typo "grainding")
- A truck image on `/tree-pruning` — exact URL not captured; **builder to grab.**

⚠️ **All three service images are 349–350 px wide — unusable at modern sizes.** Only the
stump-grinding image and the logo have 1920w variants. This is why the hero must be a
`GENERATE` slot.

---

## What the old site does NOT contain (gaps, not capture failures)

- **No town list.** The site names exactly one town: Verona. Phrases used are "Verona, NJ
  Area" and "serving Verona, NJ and the surrounding towns." The `SERVICE AREA` block that
  would have held a town list is the broken placeholder on all 7 pages.
- **No hours.** Only the marketing claim "24/7" / "24-Hour Emergency Service."
- **No email address.**
- **No street address.**
- **No About copy.**
- **No tagline beyond "The Best For Less."**
- **No testimonials or reviews on the site at all.**
- **No named client**, despite nine client categories being claimed.
