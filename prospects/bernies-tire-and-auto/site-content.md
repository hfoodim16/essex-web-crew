# Site content capture — Bernie's Tire & Auto

**Source site:** `http://www.berniestireandauto.com/`
**Captured by:** Analyst, 2026-08-17, via direct `curl` of every page in the navigation.
**Fetch note:** the site **must be fetched over `http://`**. HTTPS fails closed — the
certificate is self-signed AND expired (see the dossier). No page here was retrieved over a
valid TLS connection, because none can be.

> **This is the PRESERVATION copy.** Everything the current site says is below, verbatim.
> The new site must not know less than this file. Nothing here has been trimmed or
> editorialized.

**Content-parity warning for the Planner:** this is one of the thinnest site captures this
crew has produced — **roughly 350 words of body copy across the entire seven-page site.**
Every service description is generic industry boilerplate that would apply to any shop in
America. **There is not one sentence anywhere on this website that is specifically about
Bernie's** — no founding year, no address, no hours, no owner, no history, no reviews, no
staff, no brands carried. Content parity is therefore trivially easy to clear and almost
entirely beside the point: nearly all real content for the new site must come from the
client questionnaire, not from here.

---

## Site-wide elements (appear on every page)

**Header — contact bar:**

```
(973) 763-4432
Berniestire@verizon.net
```

**Site title / tagline lockup:**

```
Bernie's Tire & Auto
Auto Mechanic In Millburn, NJ
```

**Navigation heading — reproduced with its typo intact:**

```
Servcies
```

*(The site's own navigation heading is misspelled "Servcies". This is on the live site
today, on every page. Preserved here exactly; obviously corrected on the new site.)*

**Navigation items:**

- Auto Inspections → `/auto-inspections/`
- Brake Check and Repair → `/brake-checks-and-repair/`
- Computer Diagnostics → `/computer-diagnostics-2/`
- Suspension Repair → `/suspension-repair/`
- Tire Replacement → `/tire-replacement/`
- Wheel Alignment → **`/sample-page/`** ← the untouched WordPress starter-page slug

**Footer, verbatim:**

```
Bernie's Tire & Auto - Proudly Powered by WordPress
Theme by Grace Themes
```

*(An unmodified free-theme credit line. There is no copyright notice, no address, no
hours, and no business information of any kind in the footer.)*

---

## Page: Home (http://www.berniestireandauto.com/)

`<title>`: `Bernie's Tire & Auto – Auto Mechanic In Millburn, NJ`

The homepage consists of the contact bar, the title lockup, a "Servcies" grid of the six
service tiles (each showing a truncated preview of the service page's first sentence,
cut off with `[…]`), a "Contact Bernie" heading, and an embedded Google map labelled
"Bernies Tire and Auto Location".

**Complete body text of the homepage, verbatim:**

```
Servcies

Auto Inspections
Vehicles need to be inspected once every two years in New Jersey, […]

Brake Check and Repair
Brake service maintenance for the entire braking system and brake problems, such […]

Computer Diagnostics
Diagnostic tests can reveal problems within a car's engine, transmission, exhaust system, brakes, and other major components, […]

Suspension Repair
Balance, stability and smoothness – they're what ensure a comfortable ride for […]

Tire Replacement
There is no way to tell exactly how long a tire lasts. […]

Wheel Alignment
Inspect suspension and steering systems, including air pressure and tire condition Vehicle […]

Contact Bernie

Bernies Tire and Auto Location
[embedded Google map]
```

**Gaps on the homepage, recorded explicitly:** no street address in text, no business
hours, no "about" or history, no founding year, no owner name, no testimonials, no
photographs of the shop or crew, no tire brands carried, no calls to action beyond the
phone number in the header. The heading "Contact Bernie" is followed by a map and nothing
else — **no contact form, and no address in text form.**

---

## Page: Auto Inspections (http://www.berniestireandauto.com/auto-inspections/)

`<title>`: `Auto Inspections – Bernie's Tire & Auto`

**Complete body text, verbatim:**

```
Vehicles need to be inspected once every two years in New Jersey, except for new vehicles,
which need a five-year inspection. Check the inspection sticker on your windshield to find
the date your vehicle is due. You may get an inspection up to two months prior to the
expiration date.

See information on
inspection of commercial vehicles
```

*(Note: "inspection of commercial vehicles" is link text. It is the only outbound
informational link on the site.)*

*(Note for the Planner: this page describes **New Jersey's state inspection rules** — it
never says whether Bernie's actually performs state inspections, or is a licensed NJ
inspection facility. That is a question for the questionnaire, not an assumption.)*

---

## Page: Brake Check and Repair (http://www.berniestireandauto.com/brake-checks-and-repair/)

`<title>`: `Brake Check and Repair – Bernie's Tire & Auto`

**Complete body text, verbatim:**

```
Brake service maintenance for the entire braking system and brake problems, such as brake
pads, brake fluid, and rotors, are important in helping ensure the safety of you and your
passengers in your car, truck or other automobile with brake issues.
```

*(One sentence. That is the entire page.)*

---

## Page: Computer Diagnostics (http://www.berniestireandauto.com/computer-diagnostics-2/)

`<title>`: `Computer Diagnostics – Bernie's Tire & Auto`

**Complete body text, verbatim:**

```
Diagnostic tests can reveal problems within a car's engine, transmission, exhaust system,
brakes, and other major components, as well as performance issues with the fuel injector,
air flow and coolant, ignition coils, and throttle
```

*(One sentence, unterminated — there is no closing full stop on the live page. Also note
the URL slug is `computer-diagnostics-2`, implying an earlier `computer-diagnostics` page
was created and abandoned.)*

---

## Page: Suspension Repair (http://www.berniestireandauto.com/suspension-repair/)

`<title>`: `Suspension Repair – Bernie's Tire & Auto`

**Complete body text, verbatim:**

```
Balance, stability and smoothness – they're what ensure a comfortable ride for you and your
passengers, and your car's steering and suspension are what make this possible. Steering
and suspension are responsible for keeping your wheels firmly intact with the ground, and a
major player in keeping your car from veering to one side or the road.
```

*(Two sentences. Reproduced exactly, including "firmly intact with the ground" and "to one
side or the road", both of which are garbled in the original.)*

---

## Page: Tire Replacement (http://www.berniestireandauto.com/tire-replacement/)

`<title>`: `Tire Replacement – Bernie's Tire & Auto`

**Complete body text, verbatim:**

```
There is no way to tell exactly how long a tire lasts. The lifespan and mileage of a tire
depends of a combination of factors: its design, the driver's habits, the climate, the road
conditions and the care that's put into the tires.
```

*(Reproduced exactly, including "depends of a combination of factors".)*

*(Note for the Planner: the page for a **tire shop's** core service does not name a single
tire brand, size, price, or fitting service.)*

---

## Page: Wheel Alignment (http://www.berniestireandauto.com/sample-page/)

`<title>`: `Wheel Alignment – Bernie's Tire & Auto`

⚠️ **This page lives at `/sample-page/`** — the default slug WordPress creates on a new
install. It was never renamed.

**Complete body text, verbatim:**

```
Inspect suspension and steering systems, including air pressure and tire condition
Vehicle placed on alignment rack, where sensors are mounted and compensated
Print initial tire alignment readings.
Camber, caster and toe angles are adjusted according to manufacturer specifications
Print final tire alignment readings.
Test drive the vehicle
```

*(A six-step process list. This is the single most specific and most useful piece of copy
on the entire website — and it sits on a page whose URL still says "sample-page".
Inconsistent punctuation preserved: steps 1, 2, 4 and 6 have no terminating full stop.)*

---

## Images present on the site

All served over `http://` from `/wp-content/uploads/2021/01/`, which dates the build to
**January 2021**. Filenames suggest stock/vendor sourcing rather than photographs of
Bernie's own shop — several carry hash suffixes and dimension strings typical of a stock
library or a template demo pack.

| File | Used for |
|---|---|
| `cropped-BernieLogo-1.jpg` | site logo (200×87) |
| `inspection-auto-repairjpg-2383ca52a96ccddc.jpg` | Auto Inspections tile |
| `BRAKES-480x480-1.jpg` | Brake Check and Repair tile |
| `computer-diagnostics-1-480x480-1.jpg` | Computer Diagnostics tile |
| `rsw-bmw-suspension-repair-newjersey-480x480-1.jpg` | Suspension Repair tile |
| `tirereplacement2-1-300x225-1.jpg` | Tire Replacement tile |
| `Wheel_alignment_on_a_Ford_Focus_1-480x480-1.jpg` | Wheel Alignment tile |

**`Wheel_alignment_on_a_Ford_Focus_1` is the filename of a well-known Wikimedia Commons
image** — a strong indication the service tiles are stock, not Bernie's own shop.
`UNVERIFIED — filename inference; not confirmed against the Commons original.` Either way,
**no photograph on this site has been confirmed to show Bernie's premises, staff, or work**,
which is the single largest asset gap for the rebuild.

---

## Pages NOT present on the current site

Recorded because their absence is the content story, and every one of them is a
questionnaire item:

- No About / history page (a business operating since ~1962 publishes no history)
- No Contact page with an address in text, hours, or a form
- No testimonials/reviews page (despite ~1,000 public reviews across three platforms)
- No staff/team page, and the owner is never named
- No tire brands / manufacturers page
- No coupons, financing, or warranty page
- No privacy policy, terms, or accessibility statement
- No blog

**No page returned a fetch error. `FETCH FAILED` does not apply anywhere in this capture —
every page in the navigation was retrieved successfully over `http://`.**
