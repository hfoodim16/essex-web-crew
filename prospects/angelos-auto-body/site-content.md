# Site content capture — Angelo's Auto Body, Inc.

**Source site:** `http://www.angelosautobodyinc.com/`
**Captured:** 2026-08-13 by the Analyst, by direct `curl` of every page in the navigation.
**Pages captured:** 7 of 7. No fetch failures.

---

## ⚠️ HOW THIS SITE WAS REACHED — read before repeating anything about it

**Over HTTPS the site is hard-blocked by every modern browser. Over plain HTTP it loads
fine and serves the complete, real site.** Both facts are true simultaneously and the
distinction matters on a sales call.

Verified 2026-08-13:

```
$ curl https://www.angelosautobodyinc.com/
curl: (60) SSL: no alternative certificate subject name matches
       target host name 'www.angelosautobodyinc.com'

$ echo | openssl s_client -connect www.angelosautobodyinc.com:443 \
        -servername www.angelosautobodyinc.com | openssl x509 -noout -subject -ext subjectAltName
subject=CN=wtcufg.org
X509v3 Subject Alternative Name:
    DNS:sept11educationtrust.org, DNS:september11educationtrust.org,
    DNS:wtcufg.org, DNS:www.sept11educationtrust.org,
    DNS:www.september11educationtrust.org, DNS:www.wtcufg.org
notBefore=Aug 13 13:32:49 2026 GMT
notAfter =Nov 11 13:32:48 2026 GMT

$ curl http://www.angelosautobodyinc.com/
HTTP 200 — the real site
```

The host serves a Let's Encrypt certificate belonging to **entirely unrelated
organizations** (`wtcufg.org`, `sept11educationtrust.org`). Angelo's own domain appears
nowhere in it. Note the issue date — **the certificate was renewed on 2026-08-13, the same
day I checked** — so the server is actively auto-renewing somebody else's certificate on
this hostname. **This will not fix itself.**

Because the capture below came over HTTP, it is the genuine current content, not an archive.
**No Wayback Machine reconstruction was needed.** (For reference, the Internet Archive's
closest snapshot is `20250710164110`, 2025-07-10, and it matches.)

**Site vintage:** HTML 4.01 Transitional, full table-based layout, no CSS framework, no
viewport meta tag, a `<meta http-equiv="refresh">` splash page, and a duplicated/nested
`<!DOCTYPE>` + `<html><head>` in the home page source (malformed markup). Every page footer
reads **"©2009"**. The logo file's embedded EXIF says **Adobe Photoshop CS, Windows,
2009:05:06 12:21:26** — the site is genuinely 17 years old.

---

## Site-wide chrome (repeats on every page — captured once)

**Navigation (exact labels and order):**
HOME :: ABOUT US :: LOCATION :: SERVICES :: INSURANCE :: GUARANTEE :: CONTACT US

**Footer, every page, verbatim:**
> "WWW.ANGELOSAUTOBODYINC.COM ©2009 | ALL RIGHTS RESERVED
> **AUTO BODY LICENSE # 00991A**"

**Header image:** `images/v1_logo_head.jpg` on every interior page.
**A "join us on Facebook" badge** (`images/facebook_join_us.png`) appears on every page.

---

## Page: Home (`http://www.angelosautobodyinc.com/`)

**Title:** `Angelos Auto Body ~ Home Page`

**This is a splash page, not a home page.** Its entire content is the logo image
(`images/front_logo_splash.jpg`) linked to the About Us page, plus the footer nav. It carries:

```html
<meta http-equiv="refresh" content="5;url=http://www.angelosautobodyinc.com/About_Us.html">
```

— i.e. **it auto-redirects the visitor to the About Us page after 5 seconds.** There is no
body copy, no headline, no phone number, no services, and no call to action on the home page
whatsoever. `<meta name="keywords">` and `<meta name="description">` are both present and
both **empty**.

---

## Page: About Us (`/About_Us.html`)

**Title:** `Angelos Auto Body ~` *(the title is truncated — no page name)*

**Images:** `/user_images/founder.jpg` (captioned "Founder Angelo Kostakes"),
`/user_images/W1.JPG`

### About Us

**Photo caption:** "Founder Angelo Kostakes"

**Heading:** "Working for our third generation of customers"

> "Brothers George and Nick Kostakis are behind the wheel of Angelo's Auto Body, Inc., the
> premier full-service collision and mechanical repair facility in Essex County. They
> represent over 45 years of combined experience, continuing the tradition started by their
> father Angelo, who started the business in 1950. Quality work and satisfied customers are
> our only focus, and have resulted in our steady growth over the past 60 years."

> "The business was started by Angelo in 1950 as a tiny two-bay shop. As his reputation grew
> over the years, so did the size of the facility, moving to a second larger location in
> Newark, and eventually moving to Irvington in 1965. Our present Irvington location has seen
> several expansions over the past two decades, now including over 30,000 square feet of
> secured parking, and a 17,000 square foot state of the art facility."

> "Angelo retired from the business in 1994, but his commitment to quality work, fair
> pricing, and going the extra mile for each and every customer, continues today."

**"Domestic and foreign vehicle services include:"**
- Collision repair
- Frame and alignment repairs
- Mechanical and suspension repairs
- Towing
- Professional detailing, cosmetic repairs
- Authorized for several major insurance companies
- Computerized, accurate estimates while you wait
- Car rental and towing available
- Lifetime repair warranty
- All work done at our **35-bay facility** by our trained and certified staff, some of whom
  have been with us as long as 30 years

**Link:** "Facility Slide Show"

---

## Page: Location (`/Location.html`)

**Title:** `Angelos Auto Body ~ Location`
**Images:** `/user_images/google_map.jpg` *(a static JPEG screenshot of a map — not an
embedded interactive map)*

### Our Location

**Heading:** "Close to Interstate 78, the Garden State Parkway, and Route 22"

> **Angelo's Auto Body, Inc.**
> **243 Coit Street**
> **Irvington, NJ 07111**

**Hours of Operation**
> **Monday - Friday, 7am - 5pm**

### Directions *(complete, verbatim — this is real, useful content)*

**From Garden State Parkway, heading South:**
> "Take Exit 143A to stop sign. Turn left at end of off ramp & go to first traffic light.
> Make a left onto Lyons Avenue. Proceed to 4th traffic light (Hess gas station on left).
> Make a right onto Coit Street. Our building immediately on the right."

**From Garden State Parkway heading North:**
> "Take Exit 143. At end of off ramp, turn left & proceed to first traffic light. Make a
> right onto Lyons Avenue. Proceed to 3rd traffic light (Hess gas station on left). Make a
> right onto Coit Street. Our building immediately on right."

**From Interstate 78 heading East:**
> "Take Exit 54 (Irvington/Hillside). Go straight on off-ramp to second traffic light. Make
> left onto Lyons Avenue. Proceed to second traffic light (Hess gas station on right). Make
> left onto Coit Street. Our building immediately on right."

**From Interstate 78 heading West:**
> "Stay on the 'Local' side of 78 West. Take Exit 55 (Irvington/Hillside). Go straight on
> off-ramp to first traffic light. Turn right onto Lyons Avenue. Proceed to first traffic
> light (Hess gas station on right). Make left onto Coit Street. Our building immediately on
> right."

**From New Jersey Turnpike:**
> "Take Exit 14 for Route 78 West. After toll booth, stay on 'Local' side of 78. Follow above
> directions."

**From Route 22 East & West:**
> "Take Bloy Street Exit to Bloy Street North. Proceed to first traffic light. Make right
> onto Hillside Avenue and proceed to next traffic light. Make a left onto Chestnut, which
> merges with and becomes Coit Street. Continue to 3rd traffic light. Our building
> immediately on the left after the 3rd light."

*(Note for the Builder: the "Hess gas station" landmark appears in four of these six
direction sets. Hess exited the retail petrol business in 2014 — these landmarks are
probably stale. Confirm with the client; do not silently rewrite them.)*

---

## Page: Services (`/Services.html`)

**Title:** `Angelos Auto Body ~ Services`
**Images:** `/user_images/W7.JPG`, `/user_images/stock1_crash_sample.jpg`,
`/user_images/stock3_detailing.jpg`, `/user_images/stock3_mechanic.jpg`,
`/user_images/stock3_wheel_alignment.jpg`
*(the filenames beginning `stock…` are self-identified stock photography)*

**Testimonial banner at the top of the page (unattributed on the site):**
> "Thank you so much for the excellent work on my husband's Camry. It is so rare these days
> that someone actually does what they say they are going to do…especially when it's ASAP! I
> appreciate the beautiful job you did and that it was done so quickly…"

### Our Services

#### Body and Collision
> "We've been experts at repairing collision damage for nearly 60 years. This long history of
> quality repairs at a fair price has resulted in Angelo's Auto Body, Inc. being an approved
> repair facility for over a dozen major insurance companies. In most cases, you can just
> drop of your damaged vehicle, or have us pick it up, knowing that we can take care of all
> the details, including managing your claim and getting you in a rental car."

> "Our state of the art facility has the equipment and expert staff needed to perform quality
> repairs you can trust on today's increasing complex vehicles. And it's all backed up by our
> written lifetime warranty."

**Link:** "Before and After Slide Show"

#### Auto Mechanical Service
> "We are also a full service mechanical shop, with a dealership-trained mechanic on staff.
> We can service all your mechanical needs at pricing that is very competitive compared with
> dealership rates."

- Scheduled Maintenance
- Electrical Repairs
- Computerized 4-wheel alignment
- Brakes, struts, exhaust
- Air conditioning service
- Tune-ups
- Electrical repairs

*(preserved as found — "Electrical Repairs" is listed twice)*

#### Detailing
> "Is your vehicle is in need of some tender loving care? We providesame day service for
> cosmetic repairs, Paintless Dent Repair, shampooing and detailing that will make your ride
> look years newer, at pricing that will not break the bank. Detailing services can be
> performed during collision repairs."

*(preserved as found — the typos "Is your vehicle is" and "We providesame day service" are
on the live site)*

#### Towing
> "Expert towing services are available through our **Rex Towing** division. All towing is
> performed using our flatbed wrecker. If you require towing as part of an insurance claim,
> the cost of towing is covered as part of the overall cost of repair."

---

## Page: Insurance (`/Insurance.html`)

**Title:** `Angelos Auto Body ~` *(truncated — no page name)*
**Images:** `/user_images/W3.JPG`

### Insurance Claims

> "Insurance claims are our specialty here at Angelo's Auto Body, Inc. Dealing with an
> insurance claim does not have to be a stressful experience. Our expert front office staff
> is trained to handle all aspects of the claim process on your behalf, including assisting
> in filing claims, arranging and managing rental cars, going over repairs with your
> insurance carrier, and making sure that your vehicle is efficiently returned to
> pre-accident condition. In short, we strive to handle all the details so that you don't
> have to, so that your overall experience is a positive one."

> "Not all insurance is the same, and the truth is that some companies are better than
> others. We are committed to giving you the best possible repair and we work with all
> insurance companies to make this happen. If your insurance does not fully cover all parts
> and procedures that we feel are needed to fully and safely repair your vehicle, we will
> notify you up front. The decision as to who you buy your auto insurance from is an
> important one. If you have any questions when purchasing insurance, feel free to give us a
> call."

> "We are presently an approved repair facility for over 12 major insurance carriers. As a
> result, in most cases we are able to handle all aspects of the claims process, including
> estimating and repairs, without delay. This speeds up your repair process, often enabling
> you to simply drop your vehicle off after an accident, and pick it up a short while later
> after repairs have been completed."

> "Your insurance company may direct you to an 'approved' shop to speed the overall repair
> process, or they may do so in order to control their costs. **You have the CHOICE of where
> to have your vehicle repaired.** Choose your repair shop very carefully, as the quality of
> the repairs can vary greatly from one shop to another. If you do not have a shop that has
> done good work for you in the past, ask a friend or neighbor for a recommendation rather
> than asking your insurance company. A quality body shop will be clean and organized, will
> have a professional staff, and will provide a written guarantee on all repairs. That shop
> should be committed to expertly fixing all your damages, and to dealing with your insurance
> company to ensure that they pay for all necessary parts and procedures. Angelo's Auto Body
> is just that shop."

**⚠️ This is the best-written page on the site and the most valuable content they own.**
"You have the CHOICE of where to have your vehicle repaired" is a genuine consumer-rights
message and a real differentiator. It must carry into the new site.

**No list of the "over 12 major insurance carriers" is published anywhere on the site.**
`[gap — ask the client for the actual carrier list]`

---

## Page: Guarantee (`/Guarantee.html`)

**Title:** `Angelos Auto Body ~ Guarantee`
**Images:** `/user_images/warranty%20symbol.jpg`

### Our Guarantee

> "Our commitment to you does not end when we hand you your keys and put you back in your
> vehicle. Our goal is your complete satisfaction, and so we at Angelo's Auto Body, Inc. back
> up our workmanship with a true written Guarantee that you will not find at many other
> shops."

> "We have been standing behind the quality of our work since we first opened our doors in
> 1950. You can rest assured that Angelo's Auto Body, Inc. will be there in the future to
> stand behind our work and to serve all your automotive needs."

> "Click image below to view our warranty. (Opens new window PDF)"

`[gap — the warranty PDF itself was not captured. Ask the client for the current warranty
document; do not reproduce warranty terms we have not read.]`

---

## Page: Contact Us (`/Contact_Us.html`)

**Title:** `Angelos Auto Body ~ Contact Us`
**Images:** `/user_images/W8.JPG`, `/user_images/W9.JPG` *(captioned as the two owners —
`W8` and `W9` appear beside the names "Nick Kostakis" and "George Kostakis")*

### Contact Us

**"Reach us by phone, fax or e-mail"**

| | |
|---|---|
| **Phone** | **973.371.8700** |
| **Fax** | **973.371.8394** |
| **Rex Towing** | **973.634.6244** |
| **E-mail** | **Nick Kostakis — nick@angelosautobodyinc.com** |
| **E-mail** | **George Kostakis — george@angelosautobodyinc.com** |

**Hours of Operation (as rendered to a visitor):**
> **7am-5pm Monday thru Friday**

### ⚠️ Removed content found in the HTML — do NOT treat as current

Immediately after the weekday hours, the page source contains this, **inside an HTML
comment** — i.e. deliberately switched off and invisible to visitors:

```html
<!-- <div spellcheck="true">8am-12am Saturday</div>
     <div spellcheck="true">(closed Saturdays from Memorial Day to Labor Day)</div> -->
```

**Somebody removed the Saturday hours by commenting them out.** The current published hours
are **weekdays only**. Recorded here because it is evidence the site *has* been edited since
2009 and because the Saturday question is worth asking — but the new site must publish
**Mon–Fri 7am–5pm** unless the client says otherwise. *(The commented text also reads
"8am-12am", which is almost certainly a typo for 12pm/noon — another reason not to resurrect
it unasked.)*

---

## Logo

**Logo:** `http://www.angelosautobodyinc.com/images/v1_logo_head.jpg` — 465 × 155 JPEG,
61 KB. **A dark red heraldic badge/plaque with a gold double-rule border, carrying
"ANGELO'S AUTO BODY" in gold serif capitals, the words "Quality Since" in white script
above it and "1950" in white script below, set on a dark charcoal ground.**

**Larger splash version:** `http://www.angelosautobodyinc.com/images/front_logo_splash.jpg`
— 97 KB, the same mark at larger size.

⚠️ **Both are served over HTTP only** (HTTPS is cert-blocked), and the EXIF records
**Adobe Photoshop CS / Windows / 2009-05-06**. Download over HTTP. **Ask the client for
vector artwork** — this is a genuinely good mark that deserves a clean redraw, and at
465 px it is too small for a modern hero.

**Their tagline is in the logo:** **"Quality Since 1950."**

---

## Other images on the site (all HTTP-only, all confirmed HTTP 200)

| File | Note |
|---|---|
| `/user_images/founder.jpg` | 47 KB — **photo of founder Angelo Kostakes.** Irreplaceable; get the original from the client. |
| `/user_images/W1.JPG` | 159 KB — About page |
| `/user_images/W3.JPG` | Insurance page |
| `/user_images/W7.JPG` | Services page |
| `/user_images/W8.JPG`, `/user_images/W9.JPG` | Contact page — **the two owners' photos** |
| `/user_images/google_map.jpg` | 166 KB — a **static JPEG screenshot of a map**, not an embedded map |
| `/user_images/stock1_crash_sample.jpg` | self-identified **stock** photo |
| `/user_images/stock3_detailing.jpg` | self-identified **stock** photo |
| `/user_images/stock3_mechanic.jpg` | self-identified **stock** photo |
| `/user_images/stock3_wheel_alignment.jpg` | self-identified **stock** photo |
| `/user_images/warranty%20symbol.jpg` | Guarantee page |

Two slide shows are referenced by link but their contents were not captured:
**"Facility Slide Show"** (About) and **"Before and After Slide Show"** (Services).
`[gap — a body shop's before/after gallery is its single best sales asset. Ask the client
for the real images.]`
