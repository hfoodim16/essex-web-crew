# Dossier — Bloomfield Pest Control

**Slug:** `bloomfield-pest-control`
**Prospecting run:** 2026-08-13 · **Rank 2 of 12 · score 90/100**
**Researched by:** Analyst, with every load-bearing fact verified against the primary source
(the live site, fetched directly on 2026-08-13).

---

## Business summary

An **owner-operated pest control and wildlife removal company** in Bloomfield, Essex County,
in business **since 2001** — 25 years. It describes itself in its own words as
**"an owner-operated and supervised pest control company"** and **"Local, Family-Owned."**

It runs two distinct lines of work, which is unusual and useful for us: **insect
extermination** (termites, bed bugs, roaches, ants, bees, wasps, ticks, spiders, moths,
crickets, beetles, millipedes, flies) **and humane wildlife removal** (mice, rats, possums,
squirrels, raccoons, groundhogs, pigeons, birds) — plus **repair of the damage** those
animals do, and **commercial service plans** for businesses. That is a genuine multi-page
site, not a one-pager with a phone number.

Its published service area is enormous: **100 named towns across six counties** — Essex,
Union, Eastern Morris, Southern Bergen, Southern Passaic and Hudson. That town list is the
single richest piece of real content they own, and it is currently buried on a page nobody
finds.

**Currently trading.** The site's copyright line reads **© 2026**, the Yelp listing was
**updated April 2026**, and the business holds a live EPA registration. No sign of closure,
sale, or name change.

---

## Contact — how Harry reaches them

| | |
|---|---|
| **Owner** | **"John"** — first name only. **No surname is published anywhere I could reach.** |
| **Phone** | **(973) 259-1133** ← the only phone published anywhere |
| **Email** | **bloomfieldpestcontrol@hotmail.com** — see the important caveat below |
| Address | **36 Broughton Ave., Bloomfield, NJ 07003** |
| Hours | **Mon–Fri 8:00 am – 6:00 pm · Sat 8:00 am – 1:00 pm** · Sunday not listed (presumed closed, `[verify]`) |
| Website | `https://www.bloomfieldpestcontrol.com/` — live, but see the gap below |
| Facebook | `https://facebook.com/Bloomfield-Pest-Control-650572238361710/` (page title renders as "Bloomfield Pest **Service**") |
| Twitter/X | `https://twitter.com/BloomfieldPestC` |

### ⚠️ The email, the address and the hours are NOT visible on their own website

This is the most important operational fact in this dossier, and it shapes how Harry opens.

I recovered the email, the street address and the business hours **from the JSON-LD
structured-data block embedded in the page source** — machine-readable markup that search
engines parse and **human visitors never see.** On the rendered page, every one of those
values is replaced by placeholder text (see the gap section). So:

- **The email address is real** — it is what the business itself published to Google via its
  own site's structured data. It is a **Hotmail** address, which is itself a weak-presence
  signal worth noting gently.
- **A customer visiting their website cannot find it, cannot find the address, and cannot
  find the hours.** Only the phone number appears in visible body copy.

**Recommended channel: CALL (973) 259-1133.** The gap is visual and takes fifteen seconds to
demonstrate out loud; email is the weaker opening here because the whole pitch is "look at
what your customers see." Email is the fallback if the calls don't land.

**Ask for the owner's surname on the first call** — we cannot address him properly in
writing until then, and "John" is all any public source gives.

---

## The website gap — the pitch in one paragraph

**Their website publishes its own content-management system's editor scaffolding to
customers, in place of their hours, address, email and service area.** On every one of the
13 pages, this exact string renders where real information belongs:

> **"This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the
> live site, but only within the editor. The Yext Knowledge Tags are successfully installed
> and will be added to the website."**

The misspelling of "Knowledge" as **"Knolwedge"** is on the live site. I counted the
rendered instances by direct fetch on 2026-08-13:

| Page | Blocks |
|---|---|
| `/about` | **25** |
| `/contact` | **17** |
| every other page | 10–12 each |
| **Site total** | **~172** |

The message is telling the customer, in writing, that it "will not appear on the live site"
— **while appearing on the live site.**

Three consequences that are worth stating separately, because each is independently
checkable and each is worse than the last:

1. **The About page has essentially no content.** Ten headings render — *About Us, Year
   Established, Services, Specialties, Languages, Products, Associations, Brands, Business
   Hours, Business Attributes* — and **every single one is followed by the placeholder
   instead of a value.** The only real content on the entire page is the payment-types list:
   Visa, Mastercard, Discover, Cash, Check, Venmo.
2. **The Contact page publishes no address, no email and no hours.** It renders the headings
   "Serving" and "Business Hours" with nothing beneath them. The footer prints
   *Monday Tuesday Wednesday Thursday Friday Saturday Sunday* **with no times next to any of
   them.**
3. **The Reviews page contains zero reviews.** The heading "Bloomfield Pest Control Customer
   Reviews" renders and nothing follows it. On the home page, the heading *"Here's what our
   satisfied customers are saying…"* is likewise followed by nothing at all.

They are **paying Hibu** for this (every asset is served from `hibuwebsites.com`), which
means there is a monthly invoice attached to a site that is publishing broken template text
to their customers.

**One more detail worth having in your pocket:** the header and footer of every page
hard-code the serving location as **"Montclair, NJ"** — the only town named in the site
chrome of a Bloomfield business.

---

## Logo

**Logo:** `https://le-cdn.hibuwebsites.com/293de5e6b3914e0a9433b9c2478e3ddc/dms3rep/multi/opt/bloomfield-logo-480w.png`
— the existing header logo, served at 480 px wide from the Hibu CDN. Confirmed present in
the live homepage markup on 2026-08-13.

**Caveat for the Builder:** this file sits on the *vendor's* CDN, not on a domain the client
controls. Download it, but **ask the client for the original artwork** in the questionnaire —
if they leave Hibu, that URL may stop resolving.

Other real images in the markup (same CDN path): `Hero-1920w.jpg` (also the og:image),
`Home2-1920w.jpg`, `Commercial+Pest-1920w.jpg`. The social icons are Hibu's generic reseller
SVGs, not the client's.

---

## Real reviews

### ⚠️ ATTRIBUTION BLOCKER — read before any testimonial ships

**Yelp and pestcontrolreviews.com both returned HTTP 403 to every free method** I tried on
2026-08-13, and Facebook's page returned only its title. The review **text** below reached me
through search-result snippets that quote it, but **the reviewers' first names did not.**

Per the real-reviews rule, **an unattributed quote cannot ship as a testimonial.** Someone
must open the Yelp or Google listing and capture the matching first names before any of these
appears on a mockup. **Do not invent names.** If the names can't be recovered, the mockup
ships with no testimonial section.

There is a silver lining here: **their own Reviews page is empty**, so if the client can
produce their real reviews during the build, that alone is a visible upgrade.

### Verbatim but UNATTRIBUTED — needs first names before use

> "John and his team are extremely professional, punctual, accommodating and effective. He
> was able to make time to remedy a rodent issue I have in my attic promptly while my husband
> is away on military orders."
> — *name not captured*, review aggregator (surfaced via search; original platform not
> confirmed — likely Yelp or pestcontrolreviews.com)

> "John took care of the hornet nest on my roof and the carpenter bees trying to get in my
> walls three years ago and I haven't seen them back since."
> — *name not captured*, review aggregator (same caveat)

### The negative signal — recorded honestly, NOT as a quote

A search snippet reports a reviewer stating that **the owner gave different prices than what
was originally discussed and was overall difficult to deal with.** I could not retrieve the
original review text, so **this is a paraphrase from a snippet and must never be quoted as
if it were the reviewer's words.** It is recorded because it is real signal: pricing
consistency is a live complaint theme, and Harry should not walk in assuming a spotless
reputation.

### Ratings by platform

| Platform | What I could confirm |
|---|---|
| pestcontrolreviews.com | **8 reviews** (count shown in the search listing; page itself 403) |
| Yelp | Listing exists, **updated April 2026**. Rating and count **not retrievable** — 403. |
| Google | Listing exists. **Rating and count not retrievable** with free tools. `[placeholder]` |
| Their own site | **Zero.** The Reviews page is empty. |

**Do not put a star rating or a review count on the mockup.** I could not verify either.

---

## Credentials

| Credential | Value | Source |
|---|---|---|
| EPA registration | **EPA# 98323A** | Their own site — printed in the footer of every page and repeated in the home-page body copy |
| Insured | **"We are fully insured and licensed… to perform pest control services in New Jersey"** | Their own site, home page |
| Guarantee | **"all our services are 100% guaranteed"** / "100% satisfaction guaranteed" | Their own site, repeated on the home, services, roach, termite and bed-bug pages |
| Year founded | **2001** | Their own site — the visible sentence "Since 2001…" **and** the JSON-LD `"foundingDate": "2001"` |
| Ownership model | **"an owner-operated and supervised pest control company"** | Their own site, home page |
| **"Local, Family-Owned"** | stated as a "Why Choose" bullet | Their own site, home page |
| **"Over 20 Years of Experience"** | stated as a "Why Choose" bullet | Their own site, home page |
| Payment types | Visa, Mastercard, Discover, Cash, Check, Venmo | Their own site, About page |

**NJ pesticide applicator / business licence number: not published anywhere I could reach.**
`[placeholder]` — New Jersey issues these separately from the EPA registration, and a pest
control site normally displays one. Ask in the questionnaire.

**No awards, certifications or trade memberships found.** Their About page has an
"Associations" heading, but its value is a Yext placeholder — so if they hold any (NPMA,
NJPMA), the information exists in their Yext account and simply never rendered. Worth asking;
do not assume.

---

## Services — in their own words, grouped

Full descriptions are captured verbatim in `site-content.md`. Grouped for the page map:

**1. Insect extermination — general** (`/pest-control-services`)
Their own list of what the "Insect Fumigation and Extermination Programs Cover": Termite
control · Bedbug treatment · Bee removal · Wasp removal · Ant control · Cricket control ·
Beetle control · Cockroach control · Spider control · Millipede control · Tick treatment ·
Fly control · Moth control.

**2. Termites** — inspection, prevention, treatment. Their strongest SEO position (the home
page title is "**Termite Specialists**").

**3. Bed bugs** — detailed inspections, treatments, "discover the signs of bed bugs."

**4. Roaches** — entry-point sealing, pesticide treatment, crack repair.

**5. Ants** — indoor treatment, outdoor treatment near windows and doorways, treatment as
needed. Their own hook: *"Did you know that carpenter ants can be more destructive than
termites?"*

**6. Wildlife / animal removal** — humane trapping. Mice · Rats · Possums · Squirrels ·
Raccoons · Groundhogs · Pigeons · Birds. Plus **proofing** the property to keep wildlife out
and **repairing the damage** wildlife caused — a real differentiator most exterminators don't
offer.

**7. Commercial pest management** — preventative treatment, emergency service for commercial
properties, ongoing service plans. Their own framing: *"Whether you run a restaurant or a law
office…"*

---

## Service area — the complete list

**100 towns across six counties**, captured complete in `site-content.md`. Summary:

| County | Count | Notes |
|---|---|---|
| Essex | 17 | Belleville, Bloomfield, Caldwell, Cedar Grove, Essex Fells, Fairfield, Glen Ridge, Livingston, Maplewood, Millburn, Montclair, Nutley, Roseland, Short Hills, South Orange, Verona, West Orange |
| Union | 21 | |
| Eastern Morris | 18 | |
| Southern Bergen | 34 | the largest block |
| Southern Passaic | 18 | |
| Hudson | 10 | |

**Two things to confirm with them, not to fix silently:**
1. The Bergen list contains **"Teaneck" and "Teaneck Township" as separate entries**, and
   several entries — **Ritz, Outwater, Palisade, Morsemere, West Fort Lee** — are
   neighborhood or historic names rather than municipalities. Someone padded this list.
2. **The Animal Removal page's service-area sentence omits Union County**, which the Home and
   Pest Control Services pages both include. Their own pages disagree with each other.

---

## Recommended page map — 8 pages

Driven by the content that already exists. They have seven service pages' worth of real
written material and a 100-town list; the architecture should carry all of it.

| Page | Why |
|---|---|
| **1. Home** | The values their current site hides — phone, address, **hours**, service area — above the fold. Their real differentiators as a trust strip: since 2001, owner-operated, EPA# 98323A, 100% guaranteed, free estimates, emergency + same-day service, warranty available. Entry points to the two halves of the business (insects / wildlife). |
| **2. Termite Control** | Their strongest positioning — their own home-page title calls them "Termite Specialists." Inspection → prevention → treatment. |
| **3. Bed Bugs** | Highest-urgency, highest-margin search intent; they already have full copy for it. |
| **4. Roaches & Ants** | Two shorter service pages' worth of copy that read naturally together — both are "general household insect" intent. Carries the carpenter-ant-vs-termite hook. |
| **5. Other Insects** | The 13-item program list (bees, wasps, ticks, spiders, moths, crickets, beetles, millipedes, flies) that currently sits undifferentiated on one page. Real content, real search terms. |
| **6. Wildlife & Animal Removal** | The genuinely distinct second business line — humane trapping, 8 named animals, **proofing, and damage repair.** Deserves its own page and probably wins work no competitor page does. |
| **7. Commercial Pest Management** | A different buyer entirely (restaurants, offices, property managers) with different language — service plans, emergency response, reputation protection. |
| **8. Service Areas + Contact** | The 100-town list, properly structured by county, plus the NAP block, hours, and a short form. This is the page their current site most conspicuously fails to deliver. |

*(An "About" page is deliberately folded into Home rather than given its own page: their
current About page has no content to carry. If the client supplies a real company story and
John's surname in the questionnaire, promote it back to its own page — flag this to the
Planner.)*

---

## Reputation notes

- **25 years in business** (since 2001), stated on their own site in two independent places.
- **Owner-operated** — the owner, "John", is named in customer reviews as the person doing
  the work, which is the profile of a business that lives on referrals.
- Reviews are **positive but mixed**, with a real pricing-consistency complaint. Do not
  present them as flawless.
- **They have no visible reviews on their own website at all**, despite having a Reviews page
  and a testimonials heading on the home page. Reputation they have earned is sitting on the
  floor — the same "free win" argument that worked in the DiSalvo pitch.

---

## Current-presence critique

1. **~172 blocks of CMS editor scaffolding render to customers** across 13 pages, in place of
   real information.
2. **The About page has no content** — ten labelled sections, ten placeholders, and a
   payment-types list.
3. **The Contact page has no address, no email and no hours.**
4. **The hours are printed as seven bare day names with no times.**
5. **The Reviews page is empty**, and so is the home page's testimonial section.
6. **Their address, email and hours exist only in invisible structured data** — Google can
   read them, customers cannot.
7. **The site header of a Bloomfield business says "Montclair, NJ."**
8. **Their 100-town service area** — their best asset for local search — is a flat unstyled
   list on a page with no internal prominence.
9. **Unrendered template variables in the footer** of every page:
   `{{placeholder_retargeting_pixel}}`, `{{placeholder_footer_reserve1}}`–`7`.
10. **Vendor boilerplate never removed:** the structured data links to
    `plus.google.com/+hibu` — **Hibu's own** Google+ page, on a platform shut down in 2019.
11. **Their own pages contradict each other** on the service area (Union County present on
    two pages, absent on a third).

---

## Why this client is winnable

**The gap needs no argument — it can be read aloud.** Harry does not have to tell John his
site is ugly or dated, which is a matter of taste and puts an owner on the defensive. He
tells him that his website is printing the sentence *"This is a placeholder for the Yext
Knolwedge Tags"* where his hours should be, roughly 172 times, including 25 times on his
About page — and that anyone who visits his Contact page cannot find his address, his email
or his hours. That is a factual report about a customer-facing problem, and John can confirm
it on his phone while they talk.

Everything else says he can and will buy. **25 years** in business is staying power. He is
**already paying a vendor monthly** — Hibu — so there is an existing website budget to
redirect rather than a new expense to justify; that is a materially easier conversation than
selling a first website. He is **owner-operated**, so the person Harry gets on the phone is
the person who decides. And the business needs exactly what we build: **a static brochure
site, eight pages, no bookings, no inventory, no weekly updates** — built once and barely
touched.

There is a real commercial argument too, not just an aesthetic one. Pest control is an
**emergency-search category** — people find a bed bug at 11pm and search on a phone. Right
now that searcher lands on a page that cannot tell them whether the business is open, where
it is, or what anyone thinks of it.

### The honest counter-argument

- **We only have his first name.** For a run whose whole deliverable is contact info, that is
  a genuine weakness — Harry is calling a business and asking for "John."
- **The reviews are mixed**, with a specific complaint about quoted prices changing. A
  business with a pricing-consistency reputation may also negotiate hard on ours.
- **He has tolerated this site for a long time.** The placeholder text is not new, and
  somebody has been paying for it while it looked like this. That is either a man who never
  looks at his own website — good for us, easy to shock — or a man who does not care what it
  says. The first call will tell.
- **He is a direct competitor of Advantage Termite & Pest (West Orange)**, our rank-4
  candidate. Pitch one, not both in the same week.

---

## Do not claim — statements that sound true but are NOT supported

- ❌ **"Your website is down"** — it is not. It returns HTTP 200 on every page and loads fine.
  The accurate statement is: *"your site is publishing its editor's placeholder text where
  your hours, address and email should be."*
- ❌ **"Your site isn't mobile-friendly."** I did not test this and have no evidence for it.
  Hibu templates are generally responsive. **Do not say it.**
- ❌ **Any star rating or review count.** Yelp, Google and the review mirrors were all
  unreachable to free tools. We do not know their rating.
- ❌ **"Family-owned since 2001 by John [surname]"** — we have no surname, and "Local,
  Family-Owned" is their own marketing bullet, not a documented ownership structure.
- ❌ **"Over 20 years of experience"** as *our* claim — it is **their** website's bullet.
  Attribute it to them or use the sourced figure: in business since 2001.
- ❌ **A NJ pesticide applicator licence number.** We have the **EPA registration (98323A)**
  only. These are different things; do not print one as the other.
- ❌ **Any trade association membership** (NPMA, NJPMA). Their "Associations" field never
  rendered. We do not know.
- ❌ **The two review quotes with a name attached.** They are real text but unattributed.
- ❌ **The negative review as a verbatim quote** — what I have is a search-snippet
  paraphrase.
- ❌ **"You're not on Google"** — they are. Their structured data is intact and complete;
  that is precisely why the machine-readable layer knows things the visible page doesn't.

---

## Gaps to close in the questionnaire

- **The owner's full name.** The single most important one.
- **A better email than Hotmail** — or confirmation that `bloomfieldpestcontrol@hotmail.com`
  is genuinely where they want customer mail to go.
- **Confirm the hours** — Mon–Fri 8–6, Sat 8–1 comes from structured data, not from anything
  a human wrote recently. And confirm Sunday is closed.
- **Their NJ licence number(s)** and any trade memberships (the "Associations" field they
  never filled).
- **Their real reviews** — ask them to point us at their Google and Yelp listings so we can
  capture attributed quotes.
- **The service-area list:** is it really 100 towns? Which are the towns they actually want
  work in? And does wildlife removal cover Union County or not — their pages disagree.
- **Whether "Montclair, NJ" in the site header is deliberate** (a second location? a
  primary market?) or vendor error.
- **The original logo artwork**, since the current file lives on Hibu's CDN.
- **Real job photography** — every image on the current site is generic. Their own photos of
  a crawlspace exclusion or a bed-bug treatment would carry the whole site.
- **Are they under contract with Hibu, and when does it end?** Practical, and it tells us
  what budget is already committed.
