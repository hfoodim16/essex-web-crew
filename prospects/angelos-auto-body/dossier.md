# Dossier — Angelo's Auto Body, Inc.

**Slug:** `angelos-auto-body`
**Prospecting run:** 2026-08-13 · **Rank 1 of 12 · score 94/100**
**Researched by:** Analyst, with every load-bearing fact verified against the primary source
(their own live site over HTTP, plus `openssl` against their host, on 2026-08-13).

---

## Business summary

A **second-generation, family-owned full-service collision and mechanical repair facility**
in Irvington, Essex County, **founded in 1950** and run today by brothers **George and Nick
Kostakis**, sons of founder **Angelo**. Their own About page puts it plainly: they are
*"working for our third generation of customers."*

This is the most substantial business in the 2026-08-13 pool by a distance. By their own
account the shop occupies a **17,000 sq ft facility with 35 bays plus 30,000 sq ft of secured
parking**, employs staff *"some of whom have been with us as long as 30 years,"* runs its own
towing division (**Rex Towing**), keeps a **dealership-trained mechanic** on staff, and is an
**approved repair facility for over 12 major insurance carriers.** That is payroll, plant and
process — which in prospecting terms means a real marketing budget and a real decision-maker.

They do four distinct things, which is exactly the shape that justifies a multi-page site:
**collision/body repair**, **full mechanical service**, **detailing and cosmetic repair**, and
**towing**. Their **Insurance** page is a genuinely good piece of consumer-advocacy writing
that no competitor in this pool has an equivalent of.

**Currently trading and busy.** Reviews land as recently as **July 2026** and **May 2026**,
and the Yelp listing was **updated June 2026**. No sign of sale, closure, relocation or name
change.

---

## Contact — how Harry reaches them

| | |
|---|---|
| **Owners** | **George Kostakis** and **Nick Kostakis** (brothers) |
| **Phone** | **(973) 371-8700** |
| **Email — Nick** | **nick@angelosautobodyinc.com** |
| **Email — George** | **george@angelosautobodyinc.com** |
| Fax | (973) 371-8394 |
| Rex Towing (their towing division) | (973) 634-6244 |
| Address | **243 Coit Street, Irvington, NJ 07111** |
| Hours | **Mon–Fri 7:00 am – 5:00 pm** (Saturday is disputed — see below) |
| Website | `http://www.angelosautobodyinc.com/` — **HTTP only; HTTPS is cert-blocked** |
| Auto Body Licence | **# 00991A** (printed in their own site footer) |

**This is the best contact position of any prospect in this run — two named owners with two
direct, personal, named email addresses on their own domain.** Both were captured verbatim
from their own Contact Us page on 2026-08-13.

**Recommended channel: EMAIL FIRST, then call.** The reason is specific to this prospect:
the pitch is a technical fact that is easier to *show* than to say — Harry can write one short
message that names the certificate problem and lets them verify it in their own browser in
ten seconds. Send it to **both brothers** rather than picking one; nothing public indicates
which of them handles the business side. Follow up by phone on (973) 371-8700 if there's no
reply.

**Hours conflict — do not publish either version unasked.** Their **Location** page says
*"Monday - Friday, 7am - 5pm."* Their **Contact** page shows the same weekday hours — but the
page source contains **Saturday hours that someone deliberately commented out**:
`<!-- 8am-12am Saturday / (closed Saturdays from Memorial Day to Labor Day) -->`. Meanwhile
**Yahoo Local still publishes Saturday 8:00 am – 12:00 pm.** So their own site removed
Saturday and a directory still advertises it. **Ask.** `[placeholder]`

---

## The website gap — the pitch in one paragraph

**Their website is invisible to any customer whose browser uses HTTPS, because their server
presents a security certificate belonging to somebody else entirely.** Verified with
`openssl` on 2026-08-13:

```
subject=CN=wtcufg.org
X509v3 Subject Alternative Name:
    DNS:sept11educationtrust.org, DNS:september11educationtrust.org,
    DNS:wtcufg.org, DNS:www.sept11educationtrust.org,
    DNS:www.september11educationtrust.org, DNS:www.wtcufg.org
notBefore=Aug 13 13:32:49 2026 GMT
```

**`angelosautobodyinc.com` appears nowhere in that certificate.** `curl` fails with exit 60,
*"no alternative certificate subject name matches target host name."* A visitor typing their
address into Chrome, Safari or Edge gets a **full-page red security warning** — *"Your
connection is not private"* — before a single word of the site loads. Most people leave there.

Two details make this urgent rather than merely bad:

1. **The certificate was issued on 2026-08-13 — the same day I checked it.** The host is
   *actively auto-renewing* a certificate for an unrelated organization on their hostname.
   **This is not a lapse that will expire and get noticed; it is a misconfiguration that
   renews itself indefinitely.** Nobody is watching.
2. **Over plain HTTP the site loads perfectly.** So from the owners' side — and from any
   bookmark saved years ago that still says `http://` — everything looks fine. That is very
   likely why this has gone unnoticed. It is also why the phrasing matters enormously (see
   "Do not claim").

And behind that broken lock sits a site that stopped being updated **seventeen years ago**:

- Every page footer reads **"©2009."**
- The logo file's embedded EXIF metadata says **Adobe Photoshop CS, Windows,
  2009:05:06 12:21:26.**
- HTML 4.01 Transitional, a **full table-based layout**, no viewport meta tag, and a
  **duplicated/nested `<!DOCTYPE>` and `<html><head>`** in the home page source.
- **The home page is a 5-second `<meta http-equiv="refresh">` splash screen** that auto-bounces
  the visitor to the About Us page. It contains no headline, no phone number, no services and
  no call to action — just a logo image. Its `<meta name="description">` and
  `<meta name="keywords">` are both **empty**.
- The Location page's "map" is a **static JPEG screenshot** of a map.
- Four of their six sets of driving directions navigate by a **"Hess gas station"** landmark —
  Hess left the retail petrol business in 2014.
- Several images are self-identified stock photos (`stock1_crash_sample.jpg`,
  `stock3_mechanic.jpg`, `stock3_detailing.jpg`, `stock3_wheel_alignment.jpg`) — on a
  **35-bay body shop that repairs cars all day and could photograph anything.**

---

## Logo

**Logo:** `http://www.angelosautobodyinc.com/images/v1_logo_head.jpg` — 465 × 155 JPEG, 61 KB
— **a dark red heraldic badge with a gold double-rule border, "ANGELO'S AUTO BODY" in gold
serif capitals, "Quality Since" in white script above and "1950" in white script below, on a
dark charcoal ground.**

Larger splash version: `http://www.angelosautobodyinc.com/images/front_logo_splash.jpg` (97 KB).

**I opened this file and looked at it. It is genuinely good** — a proper vintage automotive
crest, not a clip-art wordmark. It carries their tagline inside it: **"Quality Since 1950."**

Two notes for the Builder: both files are **HTTP-only** (HTTPS is cert-blocked), and at
465 px wide the raster is too small for a modern hero. **Ask the client for vector artwork.**
Do not redesign this mark — it is an asset.

---

## Real reviews

**All quotes below carry the reviewer's displayed name and date**, captured from Yahoo Local's
listing (which aggregates the Yelp reviews) on **2026-08-13**. Yelp, Carwise,
autobody-review.com and YellowPages all returned **HTTP 403** to every free method.

**Rating: 4.0★ across 14 reviews** (Yahoo Local, checked 2026-08-13). Yelp's own listing
header shows **13 reviews and 11 photos**, updated June 2026 — the counts differ slightly
between the two; both are recorded rather than reconciled.

### Usable — attributed

> "my experience here was great ! they transformed my car back to brand new. these are very
> generous people that actually care about making you're car looking it's best & making sure
> you leave happy…"
> — **Axel R.**, Yelp (via Yahoo Local), 5★, 05/23/2026

> "My 2004 Aura TL was transformed into a new vehicle and they even replaced a leaky radiator
> free of charge. I will recommend every to Angelo Auto Body they are the best"
> — **Nwankwo O.**, Yelp (via Yahoo Local), 5★, 02/05/2026

> "I highly recommend Angelo's, I had such a good experience with them. They were fast,
> friendly, and did great work. I will definitely be using them in the future."
> — **Nicole G.**, Yelp (via Yahoo Local), 5★, 03/01/2022

> "I took my auto in to Angelo's for there know reputation in auto repair, to replace my door
> lock. It was a nice experience to have Mike, explain in detail what work was needed in a way
> I…" *(truncated on the source page)*
> — **Lisa H.**, Yelp (via Yahoo Local), 3★, 02/20/2026

*(All four are reproduced exactly as displayed, including their spelling and punctuation. Do
not clean them up. Lisa H.'s is truncated at the source — if it's used, use only the portion
above or recover the full text first. It also names a staff member, **"Mike"**.)*

### ⚠️ The negative review — recorded honestly, and it is recent

> "Avoid , put a camera in your car before leaving anything with them. You'll be amazed."
> — **None Y.**, Yelp (via Yahoo Local), 1★, **07/19/2026**

**This is dated less than a month before this research and it alleges theft.** It is recorded
because Harry should not walk into this call believing the reputation is spotless, and because
a 4.0★ average on 14 reviews means roughly one bad review meaningfully moves their number.
Two things to hold at once: the reviewer's display name is **"None Y."** (no real name given),
and it is a single unanswered allegation against three recent 5★ reviews. **Do not raise it on
the first call.** It is context, not ammunition.

### Unattributed — NOT usable as testimonials

These reached me as search-snippet text with no reviewer name, so **they cannot ship**:
*"The insurance said it was a total loss but when I asked Angelo's to save my car, they did"* ·
*"Approximately one month ago my car was serviced at Angelo's Auto Body. The work done on my
2006 Toyota Avalon was to say the least exceptional!"* · *"Five star service from the guys over
@ Angelos Auto Body in Irvington, NJ!!! They helped me deal with my cheap insurance company and
got my car fixed right at no extra cost to me."*

**Their own site also carries one unattributed testimonial** on the Services page:
*"Thank you so much for the excellent work on my husband's Camry…"* — real, but anonymous on
the source. Ask the client whether they hold the original with a name.

**Their Mechanic Advisor listing is "unclaimed"** and shows **0.0 stars / 0 reviews** — free
reputation sitting on the floor, and a generous, credible thing to point out on a call.

---

## Credentials

| Credential | Value | Source |
|---|---|---|
| **NJ Auto Body Licence** | **# 00991A** | **Their own site** — printed in the footer of all 7 pages |
| Year founded | **1950** | Their own About page; also inside their logo ("Quality Since 1950") |
| Ownership | **George and Nick Kostakis**, sons of founder Angelo; 2nd generation | Their own About page |
| Founder retired | **1994** | Their own About page |
| Moved to Irvington | **1965** (from a second, larger Newark location) | Their own About page |
| Combined experience | **"over 45 years of combined experience"** (the two brothers) | Their own About page |
| Facility | **17,000 sq ft** + **over 30,000 sq ft of secured parking**; **35 bays** | Their own About page |
| Staff tenure | **"some of whom have been with us as long as 30 years"** | Their own About page |
| Insurance approvals | **"approved repair facility for over 12 major insurance carriers"** | Their own Insurance page |
| Warranty | **written lifetime repair warranty** ("a true written Guarantee") | Their own Guarantee + Services pages |
| Mechanic | **dealership-trained mechanic on staff** | Their own Services page |
| Towing division | **Rex Towing**, flatbed wrecker | Their own Services + Contact pages |
| State Farm | **approved/select repair shop** — `UNVERIFIED — search-snippet paraphrase of a customer review, not a company statement` | search result |
| I-CAR / ASE certifications | **None found.** Their site says "trained and certified staff" but names no certifying body | — |
| BBB | **Not found** — no BBB profile located | — |

**The carrier list is a gap.** They claim "over 12 major insurance carriers" but **name none
of them anywhere on the site.** For a body shop that is the highest-value missing content on
the page — customers search by their insurer. `[placeholder — ask the client]`

**The warranty document is a gap.** Their Guarantee page links to a warranty PDF I did not
capture. **Do not paraphrase warranty terms we have not read.** `[placeholder]`

---

## Contradictions found (recorded, not resolved)

1. **Facility size: 17,000 sq ft vs 18,000 sq ft.** Their **own About page** says *"a 17,000
   square foot state of the art facility."* Directory/search copy says *"an 18,000 square foot
   facility employing 15 technicians."* **Per the currency rule the business's own statement
   wins — use 17,000** — but note the directory is the only source for the **15 technicians**
   figure, which their own site never states. `UNVERIFIED — directory only.`
2. **The founder's surname is spelled two ways on their own site.** The About page photo
   caption reads **"Founder Angelo Kostakes"**; the same page's body text calls the sons
   **"George and Nick Kostakis"**, and both email addresses are `@angelosautobodyinc.com` under
   the name **Kostakis**. One page, two spellings. **Ask which is correct before printing the
   founder's name.**
3. **Age of the business.** Their site says *"nearly 60 years"* and *"over the past 60 years"*
   — but the site is copyright **2009**, so those figures were written when the business was 59.
   **In 2026 the correct figure is 76 years.** Do not copy "60 years" forward; it is stale
   arithmetic, not a claim about today. Directory copy repeating "60 years" is repeating 2009.
4. **Saturday hours:** removed (commented out) on their own Contact page vs still published as
   **Sat 8:00 am – 12:00 pm** by Yahoo Local. Their own site is more current — but it removed
   rather than restated, so this needs a direct answer.
5. **Review counts:** Yahoo Local shows **14 reviews / 4.0★**; Yelp's listing header shows
   **13 reviews**. Both recorded.
6. **Business name rendering:** "Angelo's Auto Body, Inc." (their site) vs "Angelos Auto Body"
   (their own `<title>` tags, no apostrophe) vs "Angelo Auto Body" (in a customer review).
   **Their logo and body copy use the apostrophe.**

---

## Services — in their own words, grouped

Full text in `site-content.md`. Four genuine service lines:

**1. Body & Collision** — *"We've been experts at repairing collision damage for nearly 60
years."* Approved for 12+ carriers, claim management, rental-car arrangement, drop-off or
pick-up, written lifetime warranty. Frame and alignment repairs.

**2. Auto Mechanical Service** — a full mechanical shop with a dealership-trained mechanic:
scheduled maintenance, electrical repairs, computerized 4-wheel alignment, brakes, struts,
exhaust, air conditioning service, tune-ups. Positioned explicitly against dealer pricing.

**3. Detailing & Cosmetic** — same-day cosmetic repairs, **Paintless Dent Repair**,
shampooing and detailing; can be done during a collision repair.

**4. Towing — Rex Towing division** — flatbed wrecker; towing cost covered within an insurance
claim.

**Plus a fifth thing that isn't a service but is their best content: Insurance claims
advocacy.** Their Insurance page tells customers *"You have the CHOICE of where to have your
vehicle repaired"* and coaches them on how to pick a shop. That is a real point of view and it
must survive into the new site.

---

## Service area

**They publish no town list at all** — the only geography on the site is their address and six
sets of driving directions. Their own positioning line is *"the premier full-service collision
and mechanical repair facility in **Essex County**."*

`[gap]` A body shop draws from a wide radius and Essex County towns are exactly what people
search. **Ask for a town list in the questionnaire** — this is a straightforward, high-value
addition the old site never had.

Their own geographic hooks, worth keeping: *"Close to Interstate 78, the Garden State Parkway,
and Route 22"* — concrete and genuinely useful.

---

## Recommended page map — 6 pages

Their existing site already has seven pages of real, substantial content. The gap is that the
**home page has none of it** — it's a 5-second splash screen. The map below keeps their
structure, kills the splash, and adds the service area they never had.

| Page | Why |
|---|---|
| **1. Home** | The page that currently does not exist. Hero on "Quality Since 1950" with the real crest; the four service lines as entry points; the trust strip they've earned but never displays (since 1950, third generation, 35 bays, licence #00991A, approved for 12+ carriers, written lifetime warranty, 30-year staff tenure); reviews; tap-to-call; **the phone number, which the current home page does not contain.** |
| **2. Collision & Body Repair** | Their core business and highest search intent. Frame/alignment, claim handling, rental arrangement, lifetime warranty. **The "Before and After" gallery belongs here** — a body shop's single best sales asset, currently a dead link. |
| **3. Mechanical Service** | A genuinely separate customer who doesn't know they offer it. Dealership-trained mechanic, the seven-item service list, priced against dealer rates. This page probably wins work the current site loses entirely. |
| **4. Insurance Claims** | **Keep this as its own page — their best writing is on it.** The "you have the CHOICE" consumer-advocacy argument plus the carrier list (once we have it). Nobody else in this pool has content this good. |
| **5. Detailing & Towing** | The two smaller lines together — cosmetic repair, Paintless Dent Repair, detailing, and Rex Towing with its own number. Enough material for one solid page, not two. |
| **6. About / Contact / Location** | The 1950 story, Angelo's photo, the brothers, the 76-year timeline, the 17,000 sq ft / 35-bay facility, the written guarantee, staff tenure — plus address, hours, both owners' emails, the directions, and a real embedded map replacing the JPEG screenshot. **For a third-generation family shop this page does a lot of the selling.** |

---

## Reputation notes

- **4.0★ across 14 reviews**, with three 5★ reviews inside the last twelve months (Feb 2026,
  May 2026) — the business is active and people are still writing about it.
- **76 years, three generations, same family, same street since 1965.** That is the strongest
  establishment evidence in the entire 2026-08-13 pool.
- **Staff who have stayed 30 years** — their own claim, and a real trust signal for a trade
  where turnover is the norm.
- Balanced against that: **a 1★ review from July 2026 alleging theft**, and a 3★ review. On 14
  reviews, that is a reputation worth actively managing — which is itself a reason they may
  want a better web presence.
- **Their Mechanic Advisor profile is unclaimed** (0.0★, 0 reviews).

---

## Current-presence critique

1. **HTTPS is hard-blocked by a wrong-domain certificate**, and it renews itself daily.
2. **The home page is a 5-second auto-redirect splash** with no content, no phone number and
   empty meta description and keywords.
3. **The site is copyright 2009** and built in HTML 4.01 tables, with **no viewport meta tag**
   — it does not adapt to a phone.
4. **Malformed markup** — the home page contains a duplicated, nested `<!DOCTYPE>` and
   `<html><head>`.
5. **Two page `<title>`s are truncated** to `Angelos Auto Body ~` with no page name (About Us
   and Insurance) — those are the search-result headlines.
6. **A 35-bay body shop is using stock photography** of other people's cars and mechanics.
7. **Both slideshows are dead ends** — "Facility Slide Show" and "Before and After Slide Show"
   go nowhere I could capture. The before/after gallery is the most persuasive thing a body
   shop owns.
8. **The Location map is a JPEG screenshot** — not clickable, not zoomable, no "directions"
   button on a phone.
9. **Driving directions navigate by a gas-station brand that left the market in 2014.**
10. **They never name the 12+ insurance carriers** they're approved for — the single most
    searched thing about a body shop.
11. **No service-area town list anywhere.**
12. **Their unclaimed Mechanic Advisor profile shows 0.0 stars** while Yelp shows 4.0.

---

## Why this client is winnable

**The gap is a fact, not an opinion, and they can verify it themselves in ten seconds.** Harry
is not telling two men who have run a body shop for decades that their website looks dated —
that is a taste argument and it invites a shrug. He is telling them that **their website's
security certificate belongs to an unrelated charity, so every customer using a modern browser
hits a full-page security warning before the site loads** — and that because it still works
over the old `http://` address, they had no way of knowing. That is a specific, verifiable,
face-saving message, and it is the strongest opening line this crew has had since the DiSalvo
dead-domain finding.

Everything else says they can and will buy. **76 years and three generations** is the deepest
establishment evidence in the pool. **A 17,000 sq ft facility with 35 bays and a payroll**
means a real budget and a real decision-maker. **Two named owners with two personal email
addresses on their own domain** is the best contactability we've found in three runs — Harry
can reach the decision-maker directly, by name, today. And the business needs precisely what
we build: **a static brochure site, six pages, no bookings, no inventory, no weekly updates.**

There's a commercial argument too. A body shop's customers arrive **immediately after a car
accident**, on a phone, often at the roadside, searching "body shop near me" or "State Farm
approved body shop Irvington." Right now that person gets a red security warning — and their
competitor gets the job. Meanwhile Angelo's owns the two things that would win that search and
publishes neither: **the list of insurers they're approved for**, and **before-and-after
photographs of their own work.**

### The honest counter-argument

- **Seventeen years of not touching it** is a long time to be comfortable. Two owners who
  haven't updated a website since 2009 may simply not believe a website matters to their
  business — and a shop that fills 35 bays on insurance referrals and word of mouth might be
  right about that. This is the real risk with this prospect, and it is a mindset risk, not a
  money one.
- **The certificate problem invites a cheap fix.** A competent host could correct it in an
  afternoon for nothing. Harry should lead with it as *evidence that nobody is minding the
  store* — the 2009 copyright, the empty home page, the dead galleries, the stock photos —
  rather than as the product being sold.
- **A recent 1★ review alleging theft.** It is unanswered, which is itself part of the "nobody
  is minding the store" picture, but it means the reputation isn't spotless.
- **Two decision-makers, not one.** Brothers can defer to each other indefinitely. Emailing
  both at once is the mitigation.

---

## Do not claim — statements that sound true but are NOT supported

- ❌ **"Your website is down"** — it is not. **Over plain HTTP it loads perfectly.** The
  accurate statement is: *"your site's security certificate is issued to a different
  organization, so browsers block visitors with a security warning before the page loads."*
  Getting this wrong is fatal: they will type `http://` into their own browser, see the site
  load fine, and conclude Harry doesn't know what he's talking about.
- ❌ **"You've been hacked."** A misissued certificate is a hosting misconfiguration. There is
  **no evidence** of compromise and it would be an alarming, unsupported accusation.
- ❌ **"60 years in business"** — that is their **2009** copy. In 2026 it is **76 years**.
- ❌ **"18,000 square feet" / "15 technicians"** — their **own** site says **17,000 sq ft** and
  never mentions a technician count. The 18,000/15 figures are directory-only.
- ❌ **"Founded by Angelo Kostakis"** — their own site spells the founder **"Kostakes"** in the
  photo caption and the sons **"Kostakis"**. Confirm before printing the founder's name.
- ❌ **I-CAR or ASE certification.** They say "trained and certified staff" and **name no
  certifying body.** Do not print a certification logo we cannot source.
- ❌ **"State Farm approved."** That came from a paraphrased customer review, **not** from the
  company. Their own site says only "over 12 major insurance carriers" and names none.
- ❌ **Any specific insurance carrier's name or logo** until the client supplies the list.
- ❌ **Any warranty terms.** We have not read the warranty PDF. "Written lifetime warranty" is
  their own phrase and is safe; specifics are not.
- ❌ **Saturday hours.** Their site removed them; a directory still shows them. Publish
  **Mon–Fri 7am–5pm** until they say otherwise.
- ❌ **The three unattributed review quotes**, and their own site's anonymous Camry
  testimonial, as attributed testimonials.
- ❌ **A service-area town list.** They have never published one. Do not invent it.

---

## Gaps to close in the questionnaire

- **The insurance carrier list** — the 12+ companies they're approved for. Highest-value
  missing content on the whole site.
- **Before-and-after photographs** of real repairs, and photos of the facility. Both slideshows
  on the current site are dead. **This is the single highest-value asset request** — a 35-bay
  shop can supply these easily and they'd carry the entire site.
- **The service-area town list.**
- **Vector artwork for the 1950 crest**, and the original of the founder's photograph.
- **Correct spelling of the founder's name** — Kostakes or Kostakis.
- **Current facility figures** — is it still 17,000 sq ft / 35 bays? How many technicians?
- **Saturday hours** — kept, dropped, or seasonal?
- **Certifications** — I-CAR? ASE? Which, and can they supply the certificates?
- **The current warranty document** (the PDF the Guarantee page links to).
- **Whether the driving-direction landmarks are still accurate** (the Hess station).
- **Who owns the domain and the hosting account** — needed to fix the certificate, and worth
  knowing before promising anything about it.
- **Which brother is the decision-maker.**
- Worth mentioning as a free win, not as a sale: **claim the Mechanic Advisor profile**, which
  currently shows them at 0.0 stars.
