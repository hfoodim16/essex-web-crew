# Site content capture — Bloomfield Pest Control

**Source site:** `https://www.bloomfieldpestcontrol.com/` (live, HTTP 200)
**Captured:** 2026-08-13 by the Analyst, by direct `curl` of each page in the nav.
**Platform:** Hibu website builder (all assets served from `le-cdn.hibuwebsites.com` /
`cdn.websites.hibu.com`), with a **Yext Knowledge Tags** integration layered on top.
**Pages captured:** 13 of 13 in the navigation. No fetch failures.

---

## ⚠️ READ THIS BEFORE USING THIS FILE

This site is **broken in a specific way that this capture has to preserve literally.**

Every page renders the following string, verbatim, in the places where the business's
**hours, address, phone, email, service area, founding year, associations and business
attributes** are supposed to appear:

> **"This is a placeholder for the Yext Knolwedge Tags. This message will not appear on the
> live site, but only within the editor. The Yext Knowledge Tags are successfully installed
> and will be added to the website."**

(The misspelling of "Knowledge" as **"Knolwedge"** is theirs, and it is on the live site.)

I counted the rendered instances per page:

| Page | Rendered Yext placeholder blocks |
|---|---|
| `/about` | **25** |
| `/contact` | **17** |
| `/` (home) | 12 |
| `/pest-control-services` | 12 |
| `/termite-exterminating` | 12 |
| `/bed-bug-exterminating` | 12 |
| `/roach-exterminating` | 12 |
| `/ant-exterminating` | 12 |
| `/animal-removal` | 12 |
| `/commercial-pest-management` | 12 |
| `/service-areas` | 12 |
| `/reviews` | 12 |
| `/request-form` | 10 |
| **Total** | **~172 across the site** |

**Where you see `[YEXT PLACEHOLDER — no value rendered]` below, the real value does not
exist on the visible page.** A builder must not guess it. Some of the missing values were
recoverable from the page's invisible JSON-LD (see "Data that exists only in structured
data" at the end) — that is the ONLY place several of these facts appear.

Also present in the footer of every page, unrendered template variables:
`{{placeholder_retargeting_pixel}}`, `{{placeholder_footer_reserve1}}` through
`{{placeholder_footer_reserve7}}`.

---

## Site-wide chrome (repeats on every page — captured once)

**Top banner:** "Protect Your Home And Your Family" · button: "Request an Estimate"

**Header location line:** `[YEXT PLACEHOLDER — no value rendered]` then a comma, then
`[YEXT PLACEHOLDER]`, then the literal text **"Montclair, NJ"**.
*(Note: the only town hard-coded into the header of a Bloomfield business's site is
**Montclair**. Flagged — see dossier.)*

**Navigation (exact labels and order):**
- Home
- Pest Managing Services
  - Pest Control Services
  - Termite Exterminating
  - Bed Bug Exterminating
  - Roach Exterminating
  - Ant Exterminating
  - Animal Removal
  - Commercial Pest Management
- Service Areas
- Request an Estimate
- Reviews
- About
- Contact

**Sub-header bullets (on every page, printed twice in the markup):**
- Free Estimates & Consultations
- Warranty Available
- Emergency Service Available

**"Hours:"** label followed by `[YEXT PLACEHOLDER — no value rendered]`.

**Footer blocks:**
- "SERVING" → `[YEXT PLACEHOLDER]` + "Montclair, NJ"
- "HOURS" → `[YEXT PLACEHOLDER]` (the heading appears **twice**), then the literal day names
  "Monday Tuesday Wednesday Thursday Friday Saturday Sunday" with
  `[YEXT PLACEHOLDER — no times rendered]` where the hours belong — **the day list renders
  with no hours next to it.**
- "CONTACT US" → `[YEXT PLACEHOLDER — no phone, no email, no address rendered]`
- **"EPA# 98323A"** ← real, and one of the few hard values visible anywhere on the site
- Chat widget text: "Hi. Do you need any help?"
- "Share On:" / "Share by:"
- Legal links: "Privacy Policy | Do Not Share My Information | Conditions of Use | Notice
  and Take Down Policy | Website Accessibility Policy"
- "© 2026"
- "The content on this website is owned by us and our licensors. Do not copy any content
  (including images) without our consent."

**Recurring CTA block at the bottom of every service page:**
> "Be sure to ask about our warranty!
> Call today for a FREE estimate!
> **(973) 259-1133**"

**Meta description (home):** "Pest control services. Animal removal. Termites. Bed bugs.
Emergency service available. Call us today!"

**og:image:** `https://le-cdn.hibuwebsites.com/293de5e6b3914e0a9433b9c2478e3ddc/dms3rep/multi/opt/Hero-1920w.jpg`

---

## Page: Home (`https://www.bloomfieldpestcontrol.com/`)

**Title:** `Bloomfield Pest Control | Termite Specialists | Bloomfield, NJ`

**H1:** Pest Control Services in Bloomfield, NJ

### Residential and Commercial Pest Managing Solutions

> "Since 2001, Bloomfield Pest Control has offered pest control, pest management, animal
> control, and animal removal services to the residential and business community throughout
> Essex County, Union County, Bergen County, Passaic County, Morris County, Hudson County,
> NJ and the surrounding areas."
>
> "**Contact** us for all your pest control and animal problems."

### Pest Control Experts

> "Has an animal destroyed part of your home or business? We repair damage made to your
> property by insect infestation or wildlife issues. We also service agreements to help keep
> any unwanted guests out."

*(link: "Learn More")*

### Commercial Pest Management

> "Bloomfield Pest Control is an owner-operated and supervised pest control company. We are
> fully insured and licensed (EPA# 98323A) to perform pest control services in New Jersey
> and all our services are 100% guaranteed."

*(link: "Learn More")*

### Testimonials heading

> "Here's what our satisfied customers are saying…"

**⚠️ The heading renders, and no reviews render beneath it.** See the Reviews page below.

### Why Choose Bloomfield Pest Control?

- Over 20 Years of Experience
- Quick Response Time
- Same-Day Services
- Warranty Available
- Free Consultations
- Local, Family-Owned

*(link: "Learn More About Bloomfield Pest Control")*

---

## Page: Pest Control Services (`/pest-control-services`)

**Title:** `Termite Control and Ant Control | Bloomfield, NJ`

**H1:** Pest Control Services

### Handling All Your Pest Control Needs and More

> "Bloomfield Pest Control specializes in termite inspection, termite treatment, termite
> control, and termite extermination as well as carpenter ant control, and bed bug
> treatment. As a licensed exterminator to perform pest control services in New Jersey,
> Bloomfield Pest Control guarantees all its pest control work."

### Our Insect Fumigation and Extermination Programs Cover

- Termite control
- Bedbug treatment
- Bee removal
- Wasp removal
- Ant control
- Cricket control
- Beetle control
- Cockroach control
- Spider control
- Millipede control
- Tick treatment
- Fly control
- Moth control

> "Serving the residential and business community throughout Essex County, Union County,
> Southern Bergen County, Southern Passaic County, Eastern Morris County, Hudson County, NJ
> and the surrounding areas."
>
> "All our services are 100% guaranteed."
>
> "**Contact** us today for all your pest control and animal problems."

**Image caption / block label:** "Fly Control"

---

## Page: Termite Exterminating (`/termite-exterminating`)

**Title:** `Termite Inspection and Extermination | Bloomfield, NJ`

**H1:** Termite Exterminating Services

### Completely Demolish the Termites

> "When termites are left undetected, they can easily eat through your house. Don't let this
> happen! Let us inspect your home for termite problems."

### Take Back Your Home From Unwanted Visitors

> "The best way to get rid of termites is before they even get into your home. You can have
> our help in blocking entry points for termites or providing suggestions on how to keep the
> termites from wanting to take control of your house."

- Termite inspection
- Termite prevention
- Termite treatment

> "If our inspection does turn up with termites on the premises, you can count on our
> courteous and reliable service to treat the situation. Your worries will be a thing of the
> past with our 100% satisfaction guaranteed service plan."
>
> "**Call** Bloomfield Pest Control today."

**Block label:** "Termite Elimination Services"

---

## Page: Bed Bug Exterminating (`/bed-bug-exterminating`)

**Title:** `Bed Bug Extermination | Bloomfield, NJ`

**H1:** Bed Bug Exterminating Services

### Stop a Bed Bug Infestation in Its Tracks

> "Bed bugs are a problem that can quickly spread. These tiny little bugs can easily hitch a
> ride and enter your home, multiplying into a major problem - one that we can solve!"
>
> "[Call] Bloomfield Pest Control to learn more!"

### Get Help Finding Bed Bugs and Dealing With Them

> "Bed bugs are tiny and are known for hiding in places where they are not easily seen to the
> naked eye. If you suspect that you have a bed bug problem, call in the experts for help to
> determine if you have bed bugs and how to treat the situation."

- Detailed inspections to find the bed bugs
- Bed bug treatments for your situation
- Discover the signs of bed bugs in your home

> "With FREE estimates on all of our initial inspections, you don't have to guess if you are
> dealing with bed bugs on your property. You can trust that the bed bugs in your home or
> business will be eliminated, and you will have 100% satisfaction guaranteed with our
> treatments."

**Block label:** "Don't Let Bed Bugs Ruin Your Sleep"

---

## Page: Roach Exterminating (`/roach-exterminating`)

**Title:** `Cockroach and Pesticide Treatments | Bloomfield, NJ`

**H1:** Roach Exterminating Services

### Stop the Cockroach Problem and Keep Them From Returning

> "Bring in our fully insured company to determine the extent of your cockroach infestation.
> Once the situation is assessed, you'll have our help in figuring out the best treatment
> method."

- Stop potential entry points for the cockroach
- Pesticide treatment
- Repair cracks that could be a hiding place for cockroaches

> "Cockroaches can carry a lot of diseases into a home, as well as damage your property as
> they try to find food. You can trust that your cockroach problem will be eliminated and
> will have 100% satisfaction guaranteed with our treatments."
>
> "**Call** Bloomfield Pest Control for a FREE estimate!"

**Block label:** "Pesticide Treatment for Cockroaches"

---

## Page: Ant Exterminating (`/ant-exterminating`)

**Title:** `Ant Extermination and Treatment | Bloomfield, NJ`

**H1:** Ant Exterminating Services

### Wipe Away the Army of Ants for Good

> "Keep ants outside where they belong with our ant extermination service. You will be
> treated with a service plan that will get rid of the ants and keep your family safe."

### Don't Let Ants Be a Nuisance or Damage Your Property

> "Did you know that carpenter ants can be more destructive than termites? Don't let them
> destroy your house. We will show you the steps that need to be taken to get rid of your ant
> problem."

- Indoor ant treatment
- Outdoor treatment near the windows and doorways
- Treatment as needed

> "Warmer weather often means that ants start to come out more. With our service through all
> of Essex County, you can call on our help to prevent ants from taking your food or
> destroying your house while they look for food."
>
> "[Call] Bloomfield Pest Control today!"

**Block label:** "Indoor and Outdoor Ant Treatment"

---

## Page: Animal Removal (`/animal-removal`)

**Title:** `Raccoon Removal and Mice Removal | Bloomfield, NJ`

**H1:** Animal Removal Services

### Your Animal Control and Animal Removal Experts

> "Bloomfield Pest Control specializes in humane animal removal. We set up traps to help
> remove problematic wildlife. We help you get rid of skunks, get rid of squirrels (such as
> squirrels in the attic) from your property repair any damage done to your property by
> wildlife."

### 100% Satisfaction – Guaranteed!

> "As a licensed pest control company to perform pest control services in New Jersey,
> Bloomfield Pest Control guarantees all its pest control work. Our animal control services
> include proofing your home or business to keep wildlife out."

### Affordable Animal Control and Removal of All Types of Wildlife

- Mice removal
- Rat removal
- Possum removal
- Squirrel removal
- Raccoon removal
- Ground hog removal
- Pigeon removal
- Bird removal

> "Serving the residential and business community throughout Essex County, Southern Bergen
> County, Southern Passaic County, Eastern Morris County, Hudson County, NJ and the
> surrounding areas."
>
> "Wildlife can be pests that may cause harm to your family's health. Contact us today at
> **973-259-1133** for all your unwanted wildlife removal needs."

**Block label:** "Raccoon and Mice Removal Services"

**⚠️ Note the inconsistency, preserved as found:** this page's service-area sentence omits
**Union County**, which the Home and Pest Control Services pages both include.

---

## Page: Commercial Pest Management (`/commercial-pest-management`)

**Title:** `Commercial Pest Control Services | Bloomfield, NJ`

**H1:** Commercial Pest Management Services

### No Pests in Sight and No Pests in Mind for Your Business

> "Whether you run a restaurant or a law office, any close encounter with pests will drive
> away customers or clients. Save your reputation and give Bloomfield Pest Control a **call**
> today!"

### Complete Commercial Pest Management System

> "Part of running a business means happy customers. Most customers are not going to be happy
> with pest problems connected to your business. We can help in stopping pest problems before
> they even start."

- Preventative treatment for pests
- Emergency service for commercial properties

> "From regular maintenance plans that keep pests out in the first place to emergency service
> for unexpected problems, you can enjoy a pest-free place of business. Take advantage of our
> service plans."

**Block label:** "Commercial Property Preventative Pest Service Plans"

---

## Page: Service Areas (`/service-areas`)

**Title:** `Bloomfield Pest Control Service Areas | Bloomfield, NJ`

**H1:** Bloomfield Pest Control Service Areas

### Bloomfield Pest Control Will Be There for You

> "Serving communities near you all around the Northeastern New Jersey area. Get a FREE
> estimate today! Contact us at (973) 259-1133 for all your pest control and animal
> problems."

**This is the richest real content on the site — 100 named towns across six counties.
Captured complete, in the site's own order.**

**Essex County, NJ Pest Control Services** (17)
Belleville · Bloomfield · Caldwell · Cedar Grove · Essex Fells · Fairfield · Glen Ridge ·
Livingston · Maplewood · Millburn · Montclair · Nutley · Roseland · Short Hills ·
South Orange · Verona · West Orange

**Union County, NJ Pest Control Services** (21)
Berkeley Heights · Clark · Cranford · Elizabeth · Fanwood · Garwood · Hillside · Kenilworth ·
Linden · Mountainside · New Providence · Plainfield · Rahway · Roselle · Roselle Park ·
Scotch Plains · Springfield · Summit · Union · Vauxhall · Westfield

**Eastern Morris County, NJ Pest Control Services** (18)
Boonton · Butler · Cedar Knolls · Chatham · East Hanover · Florham Park · Green Village ·
Lincoln Park · Madison · Montville · Morris Plains · Morristown · Mountain Lakes ·
Parsippany · Pequannock · Pompton Plains · Riverdale · Whippany

**Southern Bergen County, NJ Pest Control Services** (34)
Bogota · Carlstadt · Cliffside Park · East Rutherford · Edgewater · Elmwood Park · Fort Lee ·
Garfield · Hackensack · Hasbrouck Heights · Leonia · Little Ferry · Lodi · Lyndhurst ·
Maywood · Moonachie · Morsemere · North Arlington · Outwater · Palisade · Palisades Park ·
Ridgefield · Ridgefield Park · Ritz · Rochelle Park · Rutherford · Saddle Brook ·
South Hackensack · Teaneck · Teaneck Township · Teterboro · Wallington · West Englewood ·
West Fort Lee · Wood Ridge

**Southern Passaic County, NJ Pest Control Services:** (18)
Awosting · Bloomingdale · Clifton · Great Notch · Hawthorne · Little Falls · Macopin ·
Mountain View · Packanack Lake · Pines Lake · Pompton Junction · Pompton Lakes · Preakness ·
Singac · Totowa · Wayne · Woodland Park · Uttertown

**Hudson County, NJ Pest Control Services** (10)
Bayonne · Harrison · Hoboken · Jersey City · Kearny · North Bergen · Secaucus · Union City ·
Weehawken · West New York

**Block label:** "We Provide Residential and Commercial Pest Services"

*(Preserved as found: the Bergen list contains "Teaneck" and "Teaneck Township" as separate
entries, and "Ritz", "Outwater", "Palisade", "Morsemere" and "West Fort Lee" are
neighborhood/historic names rather than municipalities. Do not silently clean this list —
confirm it with the client.)*

---

## Page: Reviews (`/reviews`)

**Title:** `Reviews | Bloomfield Pest Control`

**H1:** Bloomfield Pest Control Customer Reviews

**⚠️ THE PAGE IS OTHERWISE EMPTY.** Below the heading there is no review content of any
kind — no quotes, no names, no star ratings, no feed. The page carries 12 Yext placeholder
blocks and nothing else. The Home page's "Here's what our satisfied customers are saying…"
heading is likewise followed by nothing.

**This business has a Reviews page that contains zero reviews.**

---

## Page: About (`/about`)

**Title:** `About Bloomfield Pest Control Bloomfield Residential Animal Control`

**H1:** About / About Bloomfield Pest Control

**⚠️ THIS PAGE IS ALMOST ENTIRELY PLACEHOLDER.** It carries 25 Yext placeholder blocks —
the most on the site. Every one of the following is a **heading with no value under it**:

| Section heading (renders) | Value |
|---|---|
| About Us | `[YEXT PLACEHOLDER — no value rendered]` |
| Year Established | `[YEXT PLACEHOLDER — no value rendered]` |
| Services | `[YEXT PLACEHOLDER — no value rendered]` |
| Specialties | `[YEXT PLACEHOLDER — no value rendered]` |
| Languages | `[YEXT PLACEHOLDER — no value rendered]` |
| Products | `[YEXT PLACEHOLDER — no value rendered]` |
| Associations | `[YEXT PLACEHOLDER — no value rendered]` |
| Brands | `[YEXT PLACEHOLDER — no value rendered]` |
| Business Hours | `[YEXT PLACEHOLDER]` — the day names Monday–Sunday render with no times |
| Business Attributes | `[YEXT PLACEHOLDER — no value rendered]` |

**The ONLY real content on the entire About page:**

**Payment Types**
- Visa
- Mastercard
- Discover
- Cash
- Check
- Venmo

*(This is a near-exact repeat of the Orange Valley Tree Experts finding from the 2026-07-29
run, whose About page's only real content was likewise the word "Venmo." Same Yext/Hibu
template, same failure.)*

---

## Page: Contact (`/contact`)

**Title:** `Contact Bloomfield Pest Control | Bloomfield, NJ`

**H1:** Contact Bloomfield Pest Control

**Headings that render with NO value beneath them:**
- "Serving" → `[YEXT PLACEHOLDER — no towns rendered]`
- "Business Hours" → `[YEXT PLACEHOLDER — no hours rendered]`

**Real copy on the page:**

### Don't Wait Until Tomorrow. Emergency Service is Available!

> "Pests don't wait for a convenient time to get in your way and you don't have to wait for
> our help. Call us today at **(973) 259-1133** with your pest control problems."
>
> "Enjoy courteous and reliable service whenever you need to call for pest control service.
> From prevention to maintenance or a routine check - count on Bloomfield Pest Control."

### Get in Touch With Us / Get In Touch With Us / Free Text

> "Please fill out this short form and we'll contact you shortly."

Form fields: Name · Email:* *(and further form fields)*

**⚠️ The Contact page publishes no street address, no email address and no business hours.**
The only contact route a visitor can actually see is the phone number in the body copy and
the form. This page carries 17 Yext placeholder blocks — the second-most on the site.

---

## Page: Request an Estimate (`/request-form`)

**Title:** *(estimate-request form page)*

A short contact form. 10 Yext placeholder blocks. No unique body copy beyond the
site-wide chrome and the form itself.

---

## Data that exists ONLY in structured data (invisible to human visitors)

**This is the most important single finding in this capture.** The facts missing from the
visible pages **are present in the page's JSON-LD block** — machine-readable, invisible to a
customer. Search engines can read it; a person cannot. Retrieved verbatim from the home
page's `application/ld+json` on 2026-08-13:

```json
{
  "@type": "LocalBusiness",
  "name": "Bloomfield Pest Control",
  "address": {
    "streetAddress": "36 Broughton Ave.",
    "addressLocality": "Bloomfield",
    "addressRegion": "NJ",
    "postalCode": "07003",
    "addressCountry": "US"
  },
  "geo": { "latitude": "40.81251", "longitude": "-74.1897" },
  "url": "https://www.bloomfieldpestcontrol.com",
  "telephone": "(973) 259-1133",
  "email": "bloomfieldpestcontrol@hotmail.com",
  "sameAs": [
    "https://twitter.com/BloomfieldPestC",
    "https://plus.google.com/+hibu",
    "https://facebook.com/Bloomfield-Pest-Control-650572238361710/"
  ],
  "openingHoursSpecification": [
    { "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
      "opens": "08:00", "closes": "18:00" },
    { "dayOfWeek": ["Saturday"], "opens": "08:00", "closes": "13:00" }
  ],
  "foundingDate": "2001",
  "description": "Bloomfield Pest Control provides residential pest control, commercial pest control services to the Northeastern New Jersey area",
  "makesOffer": [
    "Pest Control Services", "Termite Extermination", "Bed Bug Extermination",
    "Roach Extermination", "Ant Extermination", "Animal Removal",
    "Commercial Pest Management"
  ]
}
```

**So the real values are:**

| Fact | Value | Where it lives now |
|---|---|---|
| Address | **36 Broughton Ave., Bloomfield, NJ 07003** | JSON-LD only — not visible on any page |
| Phone | **(973) 259-1133** | JSON-LD **and** visible in body copy |
| Email | **bloomfieldpestcontrol@hotmail.com** | JSON-LD only — not visible on any page |
| Hours | **Mon–Fri 8:00 am – 6:00 pm; Sat 8:00 am – 1:00 pm** | JSON-LD only — the visible pages print the day names with no times |
| Founded | **2001** | JSON-LD, **and** the visible home-page sentence "Since 2001…" |
| Sunday | **Not listed** in the hours spec — presumed closed. `[verify]` | — |

*(The `sameAs` list includes a `plus.google.com/+hibu` URL — that is **Hibu's own** Google+
page, not the client's, and Google+ has been shut down since 2019. It is boilerplate the
vendor never removed.)*

---

## Logo

**Logo:** `https://le-cdn.hibuwebsites.com/293de5e6b3914e0a9433b9c2478e3ddc/dms3rep/multi/opt/bloomfield-logo-480w.png`
— the site header logo, served at 480 px wide from the Hibu CDN. Confirmed present in the
homepage markup on 2026-08-13.

**Other images referenced in the markup** (Hibu CDN, all under
`le-cdn.hibuwebsites.com/293de5e6b3914e0a9433b9c2478e3ddc/dms3rep/multi/opt/`):
- `Hero-1920w.jpg` — the og:image / hero
- `Home2-1920w.jpg`
- `Commercial+Pest-1920w.jpg`
- `vid-splash-play-1920w.png` (a video splash play button, from a different Hibu account id)

Social icons are Hibu's generic reseller SVGs (`hibu_facebook.svg`, `hibu_instagram.svg`,
`hibu_twitter.svg`), not the client's assets.
