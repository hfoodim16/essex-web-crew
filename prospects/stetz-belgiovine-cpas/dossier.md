# Dossier — Stetz, Belgiovine, Manwarren and Wallis, P.C.

**Slug:** `stetz-belgiovine-cpas`
**Prospecting run:** 2026-07-29 · **Rank 3 of 12 · score 91/100**
**Dossier written:** 2026-08-13 (run completed late — see the note at the end)
**Researched by:** Analyst. Every load-bearing defect below was re-verified against the live
site by direct fetch on 2026-08-13; the partner history was verified against the firm's own
2002 Wayback capture. What was carried forward rather than re-verified is labelled as such.

---

## Business summary

A **four-partner CPA firm in Verona, Essex County**, at **155 Pompton Avenue** — a building
**they own**, purchased in **2011**. Before that they were in Montclair, at 45 Park Street. In
business, by the firm's own directory listing, **since 1983**, which makes 2026 their **43rd
year**. Their own website says the firm "has been operating in its present form since 1993" —
which is a statement about the *partnership's composition*, not the founding, and the two
figures reconcile rather than contradict (see "Establishment evidence" below).

Four named partners, all CPAs: **Larry W. Stetz, Alex Belgiovine, Robert Manwarren, Chris
Wallis.** Six described services, grouped as consulting, accounting and (their word)
"Miscellaneous." A **20-industry client list** buried in the middle of the sixth service
description, which is the single most useful piece of content the firm owns and is currently
invisible to everyone.

They are not a storefront practice. The material they publish is heavy on **forensic
accounting, litigation support, business valuation, expert-witness testimony, estate
planning, and management advisory work** — the higher-margin end of a CPA practice, aimed at
"small to medium size businesses." Their own Firm Profile says it plainly: *"The firm prides
itself in being able to deliver sophisticated technical services to those who ordinarily would
not have access."*

**Currently active, and paying for the web presence they have.** The CCH Site Builder template
was regenerated **2024-02-17** (the cache-buster on every stylesheet decodes to that date, and
it matches `<lastmod>` on all nine sitemap URLs). Their CPACharge payment portal and their
SmartVault client portal are both live. The site is being paid for; nobody is reading it.

---

## Contact — how Harry reaches them

| | |
|---|---|
| **Firm** | **Stetz, Belgiovine, Manwarren and Wallis, P.C.** — Certified Public Accountants |
| **Address** | **155 Pompton Avenue, Suite 204, Verona, NJ 07044** (the suite number is on Patch/CPAdirectory/IRS-PTIN listings; **their own site omits it**) |
| **Phone** | **(973) 433-1100** |
| **Fax** | (973) 433-1111 |
| **Email — general** | **alex@sbcpas.com** ← use this one |
| **Best first move** | **Email `alex@sbcpas.com`, then follow up by phone.** |
| Website | sbcpas.com — live, responsive, and 25 years stale |

**Direct lines and emails, all four partners** (from the firm's own hidden "View Contacts"
page; extensions verified in the live HTML today):

| Partner | Ext. | Email |
|---|---|---|
| **Larry W. Stetz, CPA** — Partner (name partner; the Firm Profile's "Senior Partner") | 130 | Larry@sbcpas.com |
| **Alex Belgiovine, CPA** — Partner (**his address is also the firm's general email**) | 110 | Alex@sbcpas.com |
| **Robert Manwarren, CPA** — Partner | 140 | Bob@sbcpas.com |
| **Chris Wallis, CPA** — Partner | 260 | Chris@sbcpas.com |

**Why Alex Belgiovine, and how I know the address is real.** The Contact page's general "Email"
field and Alex's personal field resolve to **the same address** — `alex@sbcpas.com` is
functionally the firm's front door. I did not take that on the capture's word: I pulled the
firm's **2002-01-21 Wayback capture**, where the same addresses were published as **plaintext
`mailto:` links** before the anti-spam script was ever added. `alex@sbcpas.com` is the general
address in their own markup, and has been for 24 years. That is as hard as an email gets
without contacting them.

⚠️ **The email is invisible to anyone who visits the site.** Every one of the five addresses is
hidden behind **Obfuscapery v1.10** (a 2011 anti-spam script), which only injects the address
after a **mouse-move event**. I confirmed this myself by fetching the Contact page and all four
partner pages: the served HTML contains the literal string **`Loading Email...`** and no
address anywhere. On a phone or tablet — no mouse, no mouse-move — **"Loading Email..." *is*
the firm's published email address.** It is also invisible to search engines. **This is the
single most useful thing Harry can tell them,** and it is checkable in five seconds on a phone
while he's on the call with them.

**Office hours: none published anywhere.** Not on their site, not on Patch, not on
CPAdirectory, not on any directory I could reach. `[placeholder]` — a questionnaire item.
For a firm whose busiest season is January–April, publishing no hours is a real cost.

**No license or registration numbers are published anywhere** — see Credentials.

---

## The website gap — the pitch in one paragraph

**A firm of certified public accountants is publishing a federal estate tax rate that expired
in 2001.** On their Client Services page, in the Estate and Retirement Planning section, live
right now — I fetched it today and grepped for it:

> *"With Estate Tax rates reaching as high as **55%**, Estate Tax planning is probably the most
> effective planning available."*

The top federal estate tax rate is **40%**. The 55% figure lapsed with EGTRRA in 2001. The
sentence appears verbatim in the Wayback capture of 2005 and has never been touched. **For a
CPA firm, that is not a design problem — it is a competence signal**, sitting on the page
that sells their highest-margin service, where a prospective estate-planning client will read
it.

It is not the only one. **The body copy of the Home, Firm Profile and Client Services pages is
byte-identical to the 2001 and 2005 Wayback captures — the prose on this website is 21 to 25
years old.** The homepage opens by explaining that the firm has *"come to the Internet."* The
Links page opens with *"There are many great sites on the World Wide Web."* The About page
names the firm **without Wallis** — "Stetz, Belgiovine and Manwarren, P.C." — because it was
written before he made partner and nobody has edited it since.

That is the whole pitch, and none of it requires an argument about taste.

---

## Logo

**Logo: No logo found.**

This is not "I couldn't locate one" — the firm demonstrably does not have one, and the site
proves it. The header markup is
`<img class="logo__img" src="images/logo.gif" alt="Logo">`, and I downloaded that file myself
today:

```
$ curl -s https://www.sbcpas.com/images/logo.gif -o sb_logo.gif -w "%{http_code} %{size_download}\n"
200 43
$ file sb_logo.gif
sb_logo.gif: GIF image data, version 89a, 1 x 1
```

**A 43-byte, 1×1 transparent spacer GIF.** Nothing renders. Beside it, the firm name is set as
plain browser text: `Stetz,  Belgiovine, Manwarren and Wallis, P.C.` (double space after the
first comma, present in the source). There is no logo on Facebook — **there is no Facebook
page**; the site's `<div id="socialMedia">` is eight blank lines. There is no logo on any
directory listing.

**There is also no tagline anywhere on this website.** The template's slogan div is present in
the markup and **empty on every page**. No positioning line, no hero message, nothing. This is
a rare case where we have nothing of theirs to build a hero around, so the questionnaire has to
supply it.

**Consequence worth knowing:** the only social-share hint on the site is a legacy
`<link rel="image_src" href="http://www.sbcpas.com/images/logo.gif">` — pointing at the 1×1
spacer, and hard-coded `http://` on an HTTPS site. **Every link to sbcpas.com shared in an
email, a text, or on LinkedIn previews as a blank box.** For a referral-driven professional
practice, that is a live business cost.

`[placeholder]` — **a logo, or a decision to make one, is the top design-side questionnaire ask
on this job.**

---

## Real reviews

**There is exactly one public review of this firm anywhere, and it is anonymous. Nothing here
is usable as a shipping testimonial.**

I checked: Clutch, CPAdirectory, Superpages, Yelp, Patch, dotax, Buzzfile, Crunchbase,
Experience.com, SoftwareWorld, Refetrust. Result:

| Platform | Reviews | Note |
|---|---|---|
| **Clutch** | **1** | anonymous; profile appears unclaimed; **403s to every free tool** |
| CPAdirectory | **0** | fetched directly — *"There are currently no accountants listed at Stetz Belgiovine Manwarren & Wallis P.C."*, zero reviews |
| Yelp | none surfaced | listing exists ("Updated July 2026"); Cloudflare-blocked to every free method |
| Patch | **0** | fetched directly — "Reviews/Ratings: None provided" |
| Google | not established | no rating or count surfaced in any reachable source |
| BBB | no profile found | — |

### The one review — recorded, NOT usable

Clutch's own profile page and its mirrors (SoftwareWorld, Refetrust) all **403 to free tools**,
so I could only recover fragments through search-result snippets. Reproduced exactly as the
snippets carried them, and no further:

> "They look out for us and do a good job at a reasonable rate."
> — **anonymous**, Clutch

Surrounding context from the same snippets, recorded as reputation evidence only: the reviewer
describes a **computer consulting company** that began working with the firm *"about 15 years
ago, so around 2005"*, and mentions the firm helping with **R&D tax credits for software
products**.

**Three separate reasons this cannot ship on a mockup:**

1. **No reviewer name.** Clutch shows it anonymously. The real-reviews rule forbids an
   unattributed testimonial, and forbids inventing a name.
2. **I could not read the full review text** — only search snippets. I will not stitch or
   complete a fragment.
3. ⚠️ **Independence problem.** The reviewer is a computer consulting company that has been a
   client ~15 years. **The firm's own Links page carries a reciprocal link to "Bit by Bit
   Computer Consutants"** *(their typo)* — a computer consulting company — described in Bit by
   Bit's own first-person marketing copy, pasted onto the CPA firm's site. I have **not** proven
   these are the same company and I am not asserting it. But the overlap is close enough that
   **the firm's single public review probably comes from a business it reciprocal-links to**,
   which is exactly the kind of thing that should never be presented as independent social
   proof.

**Verdict: no usable reviews found.** The mockup ships with **no testimonial section**, or a
clearly-labelled empty placeholder block. **Harry should not cite reviews as a strength on the
call** — see "Do not claim."

**The flip side is a genuine, generous thing to raise with them.** A 43-year-old firm with a
20-industry book has decades of satisfied clients and **not one of them has been asked for a
review.** Their competitors have. That is a free, high-value fix Harry can hand them before
he sells anything.

---

## Credentials

| Item | Value | Source |
|---|---|---|
| **NJCPA membership** | *"the firm is a member of the New Jersey Society of Certified Public Accountants"* | **their own Firm Profile page, verbatim** |
| **AICPA membership** | *"…and the American Institute of Certified Public Accountants"* | **their own Firm Profile page, verbatim** |
| **Peer Review** | *"The firm has also successfully completed Peer Review."* | **their own Firm Profile page, verbatim** |
| **CPA designation** | All four named partners published as `, CPA` | their own hidden Contacts page |
| **Year founded** | **1983** | Patch business directory listing, "Founded: 1983" |
| **Present partnership form** | **since 1993** | their own Firm Profile page, verbatim |
| **Owns its building** | purchased **155 Pompton Avenue in 2011** | Patch listing |
| Firm size | **2–9 employees** | Clutch profile (via search snippet) — `UNVERIFIED — directory` |

**These three claims — NJCPA, AICPA, and a completed Peer Review — are the most valuable
credentials the firm owns, and all three are buried in the fourth paragraph of an About page
nobody reads.** Peer Review in particular is a real quality gate that a lot of small firms
never complete. It belongs on the homepage.

**Not found anywhere — genuinely absent, not merely unlocated:**

- **No NJ State Board of Accountancy firm registration number.** `[placeholder]`
- **No individual CPA license numbers** for any of the four partners. `[placeholder]`
- **No PTIN or EFIN published.** `[placeholder]`
- **No partner biographies of any kind** — I fetched all four individual partner pages myself.
  Each contains only a name, ", CPA", "Partner", a phone extension, and `Loading Email...`.
  **No education, no years of experience, no specialisation, no university, no other
  designation** (no MST, MBA, CFE, CVA, ABV, PFS — nothing). `[placeholder]`
- **No headshot or photograph of any person, the office, or the building.** `[placeholder]`
- **No awards, rankings, or "Best of" listings.** `[placeholder]`
- **No client logos, industry badges, or AICPA/NJCPA marks displayed anywhere.**
- **No pricing or engagement information.**

⚠️ **The Peer Review claim carries no date.** "Has successfully completed Peer Review" is
written in copy that is 21+ years old, so it is a true statement about *some* review cycle, not
evidence of a current one. **Do not put a year on it.** Ask.

---

## Establishment evidence — 1983 vs 1993, and why both are probably right

| Figure | Where it comes from | Weight |
|---|---|---|
| **In business since 1983** (43 years) | **Patch business directory listing** — "Founded: 1983" | directory (level 3) |
| **"operating in its present form since 1993"** (33 years) | **their own Firm Profile page**, verbatim | the firm's own statement (level 2) |
| Predecessor firm | *"The firm's Senior Partner and it's Principals were formerly with a medium size accounting firm from Central New Jersey"* | their own Firm Profile page |
| Montclair → Verona | *"Prior to moving to Verona the Firm was located in Montclair, NJ"*; *"in 2011 purchased the building located at 155 Pompton Avenue"* | Patch listing |
| Montclair address, in their own 2002 markup | **45 Park St, Montclair, NJ 07042 · Phone 973-655-0440 · Fax 973-655-0016** | **their own site, 2002-01-21 Wayback capture — I pulled this myself** |

**These are not actually in conflict, and Harry should not treat them as a gotcha.** "Operating
in its **present form** since 1993" is a carefully qualified sentence about when the current
partnership took shape — the same paragraph explains the principals came over from a Central
New Jersey firm. A 1983 founding with a 1993 restructuring is the ordinary reading, and it is
the reading the currency rule supports: neither source contradicts the other.

**Operative line: in business since 1983 — 43 years — with the current partnership formed in
1993.** Confirm it in the first two minutes of the call; it is a warm opener and it is the
number that should lead the new homepage. Right now **neither figure appears anywhere a visitor
would see** — the "since 1993" is in paragraph one of an About page, and the 1983 date is on a
Patch directory listing the firm probably doesn't know exists.

### The partner roster has moved, twice, and the site records neither move

Verified myself against the **2002-01-21 Wayback capture of their own contact page**, which
listed five people:

| 2002 (their own site) | Today (their own site) |
|---|---|
| **Gary S. Stetz, CPA — Partner** | **absent** |
| Larry W. Stetz, CPA — Partner | Larry W. Stetz, CPA — Partner |
| Alex Belgiovine, CPA — Partner | Alex Belgiovine, CPA — Partner |
| Robert Manwarren, CPA — Partner | Robert Manwarren, CPA — Partner |
| **Chris Wallis — Associate** *(no CPA suffix in 2002)* | **Chris Wallis, CPA — Partner** |

So **Chris Wallis was an associate in 2002 and is a name partner today** — which is exactly why
the About page still says "Stetz, Belgiovine and Manwarren, P.C." It was written before his
promotion. That is a good, human, 24-year story that the website has managed to record only as
an inconsistency.

**And Gary S. Stetz is a live open question.** He is gone from the site's partner roster, but:

- he is still in the site's own **meta keywords** today (I read them myself — see below);
- the **IRS PTIN directory** (via taxrpo mirror) lists **"Gary Scott Stetz Sr, CPA"** at
  **155 Pompton Avenue, Suite 204** with phone (973) 433-1100 and website sbcpas.com.

The same PTIN listing shows **five preparers at that address** — verbatim:
**Gary Scott Stetz Sr, CPA · Alexander Belgiovine Jr, CPA · Anne Murphy Mountjoy ·
Anthony M Cicitta, CPA · Christopher Wallis.** **Larry W. Stetz and Robert Manwarren are not
in it, and three of the five names appear nowhere on the firm's website.**

**Recorded, not resolved.** The site's roster may be out of date in *both* directions. Do not
publish any of these names without the firm confirming them, and **do not raise it as a gotcha
on the call** — "who actually works here now" is a questionnaire question, not an accusation.

---

## Services — in their own words

Six services, published under three category headings. Full text is in `site-content.md`; these
are their own descriptions, quoted, not paraphrased.

**Their own framing, verbatim:** *"Our firm offers a wide range of services to our individual
and business clients. Because our firm is relatively small, our clients benefit by getting
personalized, quality service that is beyond comparison."* And: *"As the list below is by no
means all-inclusive, please feel free to inquire about a service if you do not see it listed.
If it is not a service we provide, we would be more than happy to refer you to a qualified
professional."*

### Under "Consulting Services"

**1. Management Advisory Services (MAS)** — the longest description on the site, and the only
one with any voice: *"MAS really allows us to give you full financial services. It allows us to
interact with you. Interaction with you is the keystone of our philosophy for servicing your
needs."* Carries a **13-item bullet list**: editing business plans · recommending computer
software · operational review and improvement studies · analysis of an accounting system ·
assistance with strategic planning · defining your information system · assistance with mergers
of organizations · insolvency services · valuation services · preparation of information for
financing · analysis of a potential merger or acquisition · assistance in substituting for
bookkeepers · assistance in controllership activities.

### Under "Accounting Services"

**2. Forensic Accounting** — the shortest description on the site, two sentences, no bullets,
and it is describing one of their highest-value services: *"We use accounting and auditing
skills to provide an analysis of financial records in conjunction with dispute resolutions, as
well as fraud and theft investigation. Our damage measurement methods can determine the extent
of financial loss and illegal accounting practices."* **Underwritten by a mile.**

### Under "Miscellaneous" *(their heading — see the note below)*

**3. Tax Preparation And Compliance** — *"Stetz, Belgiovine and Manwarren believes that
taxation is one of the largest singular expenses faced by an individual or business… The firm
believes that proper 'tax planning' can give rise to opportunities for savings. The objective of
the firm is to minimize or defer your tax liabilities in order to foster growth and security."*
4 bullets: returns for any entity, federal and state · **representation before all taxing
authorities** · estate and gift tax return preparation · planning for business dispositions,
reorganizations, mergers and acquisitions, and real estate.

**4. Litigation Support Services** — *"Due to the litigious nature of today's society and
business environment, CPAs are frequently called upon by attorneys to explain, support and
document issues. Our intimate knowledge of your business enables us to assist your attorneys in
developing effective strategies for you."* 9 bullets including **calculation of damage claims ·
assistance with trial depositions · preparation of trial exhibits · rendering an expert opinion
· appearances as an expert witness · business valuation services · assistance with mediation.**

**5. Estate And Retirement Planning** — *"one of our major concerns is assisting our clients in
preserving their wealth… Through a series of interviews, our professionals put together a
profile of your financial data and personal preferences."* Two full paragraphs, estate and
retirement. ⚠️ **Contains the expired 55% estate-tax rate. The fact must be re-stated correctly
by the client; do not copy that sentence forward.**

**6. Accounting, Auditing, Review & Compilation Services** — *"the Auditing, Review and
Compilation services are the foundation for what we do."* Range stated plainly and well:
*"The scope of the firm's services range from Certified Audits for Companies to write ups for
'Mom and Pop' businesses."* Also: *"we are able to service clients throughout the nation."*
**This is the description that hides the 20-industry list.**

**Two things about this page a rebuild must fix, both content decisions rather than design
ones:**

1. **"Tax Preparation And Compliance" is filed under the heading "Miscellaneous."** So are
   litigation support and estate planning — three of the six services, including the one that
   pays the January-to-April bills. The grouping is simply unmaintained.
2. **A seventh service has been dropped.** The 2001 capture lists **`SEC Related Services`**,
   which appears nowhere today. Confirm whether that was deliberate before deciding whether to
   reinstate it.

**Grammar defects present in their live source, preserved for the record and to be corrected in
any rebuild:** *"it's Principals"* (should be "its"), *"its' needs"*, *"prolific accounting
firm"*, and a broken opening sentence in service 6 (*"Stetz, Belgiovine and Manwarren the
Auditing, Review and Compilation services are the foundation for what we do"*).

**Also on the site, and not in the nav where they belong** — two live, working business
functions buried at the bottom of a page called "Links":

- **`Pay Your Bill`** → `secure.cpacharge.com/pages/sbcpas/payments` — their **CPACharge**
  online payment portal, with **no label explaining what it is**.
- **`SBCPAS - Secure File Transfer`** → `sbcpas.smartvault.com` — their **SmartVault** client
  document portal. Description verbatim, typo included: *"Please click this link to transfer
  files (encypted) to our firm."*

A client trying to pay an invoice or send a tax document has to find a page called "Links" and
scroll past the IRS refund tracker. **Both belong in the primary navigation.**

---

## Service area — and the 20-industry list

**There is no service area on this website.** The firm never names Verona, never names Essex
County, and never names a single New Jersey town outside its own postal address — while
simultaneously claiming *"we are able to service clients throughout the nation."* No towns
list, no county, no radius. `[placeholder]` — a required questionnaire item.

**What they do have instead is better, and it is completely buried.** The complete industry
list, in the exact order published, from the middle of the sixth service description:

> Preamble, verbatim: *"The members of the firm are intimate with a number of industries
> including but not limited to the following:"*

1. Automobile
2. Collectibles
3. Communications
4. Contractors
5. Distributors
6. Entertainment
7. Fast Food Franchises
8. Health Care
9. Importers
10. Law Practices
11. Licensing
12. Manufacturing
13. Music
14. Not For Profits
15. Professional Practices
16. Real Estate Developers
17. Restaurants
18. Retail
19. Trucking
20. Wholesale

> Closing claim, verbatim: *"we are able to service clients throughout the nation."*

**This is the firm's real differentiator and it is a run-on sentence in paragraph three of
service six.** "Collectibles," "Music," "Entertainment" and "Licensing" on one CPA firm's list
is genuinely unusual and genuinely interesting — those are specialist books of business, not
boilerplate. A business owner searching "Verona NJ accountant for trucking company" or "CPA for
restaurant" cannot find this firm, because the twenty words that would match them are welded
into a paragraph Google has no reason to surface.

---

## Current website assessment

The site is **sbcpas.com**, built on **CCH Site Builder** (Wolters Kluwer), theme "Arrival",
colour scheme blue. Its predecessor was an **Execusite** build from 1999–2000.

### Verified by me, by direct fetch, on 2026-08-13

1. **No logo.** `/images/logo.gif` → HTTP 200, **43 bytes**, `GIF image data, version 89a,
   1 x 1`. Downloaded and file-typed. Nothing renders.
2. **The expired estate-tax rate is live.** Fetched `client_services.html` and grepped:
   `as high as 55%`. Present today.
3. **The email is not in the HTML at all.** Fetched the Contact page and all four partner
   pages: every one serves the literal string `Loading Email...` inside
   `<span id="mailto_0">`, with **no address anywhere in the source**. Injected only by
   `obfuscapery.js?v=3.0.3` on a mouse-move. **Invisible on mobile and to search engines.**
4. **Zero structured data.** `grep -c 'application/ld+json'` → **0**. No `LocalBusiness`, no
   `AccountingService`, no `Organization`.
5. **Zero OpenGraph, zero Twitter Card, zero canonical.** Combined grep → **0**.
6. **Two jQuery versions configured on one page** — `jquery/1.11.1/jquery.min.js` (2014) as
   primary, with `jquery/3.5.1/jquery.min.js` as a conditional fallback.
7. **An IE6-era PNG transparency hack ships on every page** — `pngbehavior.htc`, a proprietary
   Microsoft `behavior` property, still referenced in the live markup.
8. **Both federal links are dead at the DNS level.** `host ftp.fedworld.gov` and
   `host www.ins.usdoj.gov` both fail to resolve. FedWorld was decommissioned by NTIS in 2014;
   the INS ceased to exist on 2003-03-01. A **CPA firm is linking clients to Form 2848 and
   Form I-9 at hosts that have not existed for 12 and 23 years.**
9. **No favicon.** `/favicon.ico` → **HTTP 404**, despite being referenced in every page's
   `<head>`.
10. **The banner is a stock night photo of the Lower Manhattan skyline with the Brooklyn
    Bridge** — `/images/header.jpg`, HTTP 200, **122,082 bytes**, 1900×450. On a **New Jersey**
    firm's website. No overlay text; the message div is empty.
11. **The meta keywords tag, verbatim, in full** (deprecated since ~2009, and still here):

    > `Stetz,  Belgiovine, Manwarren and Wallis, P.C. , Verona , NJ, 07044, CPAs, Certified
    > Public Accountanta, Montclair, NJ, Gary Stetz, Larry Stetz, Alex Belgiovine, Robert
    > Manwarren, Chris Wallis, Accountants, Tax, IRS, Payroll, Compliation, Business,
    > Entrepenuer, Tax Preparation, Finacial Statemets, CPA, income tax`

    **Four misspellings in the firm's own keywords** — *Accountanta*, *Compliation*,
    *Entrepenuer*, *Finacial Statemets*. Plus **"Montclair, NJ"**, an office that closed in
    **2011**, and **"Gary Stetz"**, a partner the site no longer lists.
12. **`Designed by CCH Site Builder`** is the only text in the entire footer, sitewide.
13. **The 2002 Wayback capture** confirms the partner history and the plaintext emails (above).

### Carried forward from the `site-content.md` capture (same day, prior analyst)

Recorded as capture findings rather than my own re-verification:

14. **Body copy on Home, Firm Profile and Client Services is byte-identical to the 2001 and
    2005 Wayback captures** — the prose is 21–25 years old.
15. **The template was regenerated 2024-02-17** (cache-buster `d=1708180317768`; matches
    `<lastmod>` on all nine sitemap URLs). **The template was updated; the content was not.**
16. **The contact "form" is a 550×760 `window.open` JavaScript popup** (`Message Us` →
    `content/plugins/leadgenerator.php`) — a pattern modern browsers and mobile devices
    frequently block outright. **There is no inline contact form anywhere on the site.**
17. **The footer's three columns and four sections are all empty.** No address, no phone, no
    hours, no email, no copyright year, no navigation.
18. **The tagline div and the social-media div are present in markup and completely empty on
    every page.**
19. **No canonical tag, and `sitemap.xml` lists both `https://www.sbcpas.com` and
    `https://www.sbcpas.com/home.html`** as separate URLs — actively instructing search engines
    to index duplicate content. The homepage also answers at `/index`.
20. **`robots.txt` exists and is empty** (`User-agent: *`, no directives).
21. **The only page naming the partners is hidden** — `contact_us.html?id=19128` is not in the
    nav and not in `sitemap.xml`, reachable only by clicking a `View Contacts` button.
22. **The Newsletters page is 100% CCH-syndicated national content** — no firm-authored
    article, blog post or tax tip exists anywhere on the site. The syndicated feed surfaces
    **CT, NY and PA** items alongside a single NJ one, on a New Jersey firm's website.
23. **`careers.html`, `services.html`, `tax_tips.html`, `newsletter.html` all return 404.**
24. **The Info Center offers only 2 of the ~7 CCH modules** (Events Calendar and Federal Tax
    Forms); items 2–6 — typically Tax Rates, Due Dates, Retention Guide, Track Your Refund —
    were never enabled. The forms page still shows an **"Adobe Reader" download badge.**
25. **The Links page's reciprocal client link** names **"Bit by Bit Computer Consutants"**
    *(typo theirs)* and pastes **Bit by Bit's own first-person marketing copy** onto the CPA
    firm's site — so on that page "our clients" refers to a different company's clients.
    Naming a client publicly is also a **confidentiality question worth raising**.
26. **No privacy policy, terms of use, or accessibility statement of any kind.**
27. **The "Get Directions" control is a form POST to Google Maps.** The address is not a link
    and there is no embedded map.
28. **The Contact page heading reads "P. C." with a space**, against "P.C." in the title and
    nav; and the block is headed **"United States"**, implying a multi-office template the firm
    never used.

### What is NOT wrong with it

**The site is mobile-responsive and works fine on a phone.** See "Do not claim."

---

## Recommended page map — 6 pages

An information-architecture sketch, driven by the content that actually exists. Their material
supports more than a brochure and less than a sprawl: **six real service descriptions, a
20-industry list, four partners, and two live client portals that currently have nowhere to
live.**

| Page | What justifies it |
|---|---|
| **1. Home** | Carries what the current homepage doesn't: who they are, where they are, what they do, and since when. The **1983 founding**, the **NJCPA / AICPA / completed Peer Review** credentials (all three currently buried in About paragraph four), the six services as entry points, the **20-industry list surfaced as real navigation**, phone and email above the fold, and prominent links to **Pay Your Bill** and **Secure File Transfer**. The existing homepage copy — the 25-year-old "we have come to the Internet" welcome — carries no facts and does not survive. |
| **2. Services — Tax** | *Tax Preparation and Compliance*, currently filed under "Miscellaneous." Their own description plus the four bullets, including **representation before all taxing authorities** — a distinct, high-intent search. This is the page that has to work in February. |
| **3. Services — Accounting, Audit & Advisory** | *Accounting, Auditing, Review & Compilation* + *Management Advisory Services*. These belong together: the audit-to-write-up range (*"from Certified Audits for Companies to write ups for 'Mom and Pop' businesses"*) plus the 13-item MAS list. Substantial existing copy, two descriptions' worth. |
| **4. Services — Forensic Accounting & Litigation Support** | *Forensic Accounting* + *Litigation Support*. **The highest-value page on the site and today the thinnest** — forensic gets two sentences. The audience is attorneys, not homeowners, and the existing 9-bullet litigation list (damage claims, depositions, trial exhibits, expert opinion, expert witness, business valuation, mediation) is genuinely strong material. Needs expansion from the client, not invention. |
| **5. Services — Estate & Retirement Planning** | Two full paragraphs of existing copy, and its own audience. ⚠️ **The 55% estate-tax sentence must be re-stated correctly by the client before this page is built.** |
| **6. About & Contact** | The page that does the most work and currently doesn't exist. **1983, the 1993 partnership, the move from Montclair, the building they bought in 2011**, the four partners **with bios and direct extensions** (the site's partner roster is a hidden page today), NJCPA / AICPA / Peer Review, **office hours**, **a visible email address**, an inline form replacing the popup, and complete NAP with the suite number. |

**Structural fixes that are IA decisions, not design ones:**

- **`Pay Your Bill` (CPACharge) and `Secure File Transfer` (SmartVault) move into the primary
  navigation.** They are live business functions currently buried on a page called "Links."
- **The 20-industry list becomes navigable content** rather than a run-on sentence.
- **The partner roster stops being a hidden page.**
- **The Links page mostly dies.** Of its 8 outbound links, 2 are dead federal hosts, 2 are the
  firm's own portals (promoted above), 1 names a client (a confidentiality question), and the
  rest are IRS pages that belong as inline references. Keep the IRS refund tracker; drop
  the rest.
- **The Newsletters and Financial Tools modules are a client decision, not ours.** Both are
  vendor-syndicated CCH content with **zero firm-authored material** — carrying them forward
  means carrying a CCH dependency into a static site. The Financial Tools intro is one of only
  two places on the site with any voice (*"Should I refinance my mortgage? How much do I need
  to save for my child's college education? As accounting professionals, these are some of the
  questions that are posed to us on a daily basis."*) and that **copy** is worth keeping even
  if the ~150-calculator library is not. Ask.
- **The Info Center is 2 enabled modules out of ~7** and contains no firm content. Same call.

---

## Competitive context (for Harry's call, not a design reference)

**Bederson LLP — `bederson.com`, West Orange** — one town over, and a **direct competitor for
the exact services Stetz publishes least well**: forensic accounting, litigation support,
business valuation, and expert-witness work. Bederson is a well-established Essex County firm
that markets those practices deliberately. **Stetz's forensic accounting page is two sentences
long.** That is the competitive gap in one line, and it is worth Harry knowing before he calls:
this is not a firm being out-designed, it is a firm whose highest-margin service is
under-described while a competitor eight minutes away describes it properly.

*(Design references, art direction, fonts and palettes are Planner work in a Build run and are
deliberately not in this dossier.)*

---

## Contradictions found (recorded, not resolved)

1. **Firm name, four renderings.** *"Stetz, Belgiovine, Manwarren and Wallis, P.C."* (title,
   nav) · *"Stetz, Belgiovine, Manwarren & Wallis, P.C."* (Patch, Clutch, directories) ·
   *"Stetz, Belgiovine, Manwarren and Wallis, P. C."* with a space (Contact page heading) ·
   **"Stetz, Belgiovine and Manwarren, P.C."** — **without Wallis** — on their own About page.
   The last one is a stale-copy artifact, not a legal-name question, but only the firm can
   confirm the correct rendering.
2. **Founding: 1983 (Patch) vs "present form since 1993" (their own About page).** Reconcilable
   — see Establishment evidence — but not confirmed.
3. **Partner roster: site vs IRS PTIN directory.** The site lists Larry Stetz, Alex Belgiovine,
   Robert Manwarren, Chris Wallis. The PTIN directory at the same address lists Gary Scott
   Stetz Sr, Alexander Belgiovine Jr, Anne Murphy Mountjoy, Anthony M Cicitta, Christopher
   Wallis. **Three names are on one and not the other, in both directions.**
4. **Gary Stetz.** Absent from the site's roster; present in the site's own meta keywords, in
   the 2002 capture as a partner, and in the current PTIN directory at this address.
5. **Address: suite number.** Their own site says *"155 Pompton Ave"*; Patch, CPAdirectory and
   the PTIN directory all say **"155 Pompton Avenue, Suite 204."**
6. **Montclair.** Office closed in 2011 per Patch; still in the site's meta keywords today.
7. **Service count: 6 today vs 7 in 2001** — `SEC Related Services` dropped without explanation.
8. **Reach: "throughout the nation"** on a site that names no town, county or state it serves.
9. **Chris Wallis's title:** "Associate" in 2002, "Partner" today. Not a conflict — a promotion
   the About copy never caught up with.

---

## Do not claim — things that sound true but aren't supported

Harry should not say any of these on a call:

1. ❌ **"Your site isn't mobile-friendly."** **It is.** I confirmed the markup:
   `<meta name="viewport" content="width=device-width, initial-scale=1">` is present, Bootstrap
   3 is loaded, and a standard `navbar-toggle` hamburger with three `icon-bar` spans is wired
   via `data-toggle="collapse"` to `#navbar--collapse`. **It works on a phone.** Saying
   otherwise is a false statement to a client who can check it in three seconds, and it costs
   the meeting. **The true and much stronger version: their site works fine on a phone and
   still won't show a phone visitor their email address.**
2. ❌ **Anything about their reviews being good, or numerous, or a strength.** **There is
   exactly one public review of this firm anywhere.** It is **anonymous**, it is on an unclaimed
   Clutch profile, I could only recover fragments of it, and it most likely comes from a client
   the firm reciprocal-links to. **Do not cite reviews as a strength, do not quote it, and do
   not put it on a mockup.**
3. ❌ **"You have no website."** They do, it is live, it is responsive, and the template was
   regenerated in **February 2024**. The pitch is that the **content** is 25 years old, not
   that the site is absent.
4. ❌ **"You've been in business 43 years"** — as a stated fact. Their own site says "present
   form since 1993"; the 1983 date is a directory listing. **Ask, then say it.**
5. ❌ **Any partner's license number, education, designation or tenure.** None is published
   anywhere. Nothing beyond "CPA" exists for any of the four.
6. ❌ **"You completed Peer Review in [year]."** The claim is real and it is theirs, but it
   carries **no date** and sits in copy that is 21+ years old.
7. ❌ **Any service-area town, county, or radius.** They have never published one.
8. ❌ **Anything about Gary Stetz, Anne Murphy Mountjoy or Anthony Cicitta's status at the
   firm.** Directory data against a website that disagrees. **Ask; don't assert.**
9. ❌ **"Nobody has touched your site in 25 years."** Not quite true and easy to rebut — the
   *template* was regenerated in Feb 2024. **The accurate and more damaging version: "your
   template was rebuilt two years ago and your words weren't."**

---

## Why this client is winnable

**The strongest argument is not that the site looks old — it's that a firm of certified public
accountants is publishing a tax rate that expired in 2001.** Harry can read the sentence to
them off their own page: *"With Estate Tax rates reaching as high as 55%…"* The top federal
rate is 40%. No CPA argues with that, and nobody at that firm knows it is there, because the
words were written before the rate changed and nobody has opened the page since.

Then the second one, which is checkable while he's on the phone: **their email address does not
exist on their website.** Not hidden well — genuinely absent from the served HTML, replaced by
the words "Loading Email..." on every page including all four partner pages. Any client on a
phone, and every search engine, sees exactly that. For a practice that runs on referrals and
email, that is revenue on the floor.

**Everything else says they can and will buy.**

- **43 years in business** and **they own their building** — purchased in 2011. That is a firm
  with a balance sheet, not a side practice.
- **Four partners and a 20-industry book** — automobile, entertainment, music, licensing,
  trucking, healthcare, not-for-profits. This is a real practice with real revenue.
- **They already pay for software.** A CCH Site Builder subscription, **CPACharge** for
  payments, **SmartVault** for secure document exchange. They are not allergic to spending
  money on tools; they simply have never been shown that the website is one.
- **They are in the business of noticing when a document is out of date.** The
  professional-embarrassment argument lands harder on a CPA than on almost any other trade,
  and it lands without being insulting — it wasn't sloppiness, it was a vendor template nobody
  looked at.
- **The scope is honest and small: six pages, static, no bookings, no inventory, built once.**
  That is exactly what we sell, and a CPA firm's website is the most naturally static site in
  Essex County.
- **The content already exists.** We are not writing a firm's story from nothing — six service
  descriptions, a 20-industry list, and three real credentials are already written. The job is
  structure, currency and identity.

### The honest counter-argument — what would make them say no

- **CPAs are the hardest professional to sell marketing to, and for a good reason.** A 43-year
  practice with a 20-industry book gets its clients from referrals, attorneys and CPAs who
  retire. If the answer is *"every client we have came from another client,"* the website is
  genuinely low-stakes to them — and the pitch has to shift from lead generation to
  **protecting a reputation** and **not embarrassing themselves in front of a referring
  attorney** who Googles them.
- **Four partners means four opinions and no single decision-maker.** Unlike a
  sole-owner trade, this cannot be closed by one person on one call. Expect *"I'll raise it
  with the other partners."* Harry should ask, early, **who decides.**
- **Timing is a real risk, and it cuts both ways.** A CPA firm is unreachable and uninterested
  from January through April 15. **August is close to the right time to call** — but if the
  first attempt lands wrong, the fallback ask is *"can we talk in September, before the October
  15 extension deadline?"*, which is a credible thing to say and shows he knows their calendar.
- **The gap is less visually dramatic than DiSalvo's or Orange Valley's.** Nothing is broken on
  screen. A partner glancing at the site on his phone sees a working, tidy, blue website. **The
  argument is entirely about content**, so Harry has to arrive with the two specifics — the 55%
  rate and the missing email — rather than a general case that it looks dated. A general
  "your site looks old" call fails here.
- **They may see it as a compliance-free zone.** Nothing on that site is legally required to be
  current. "It's just a brochure, nobody uses it" is the objection to be ready for — and the
  answer is the referring attorney, and the estate-planning client reading a 55% rate.

### The opening line

> *"Your Client Services page tells people estate tax rates reach 55%. That rate expired in
> 2001 — it's been 40% for twenty-five years. It's on your site right now, on the estate
> planning section."*

And, if he wants a second one for the same call:

> *"Pull your Contact page up on your phone. Where your email address should be, it says
> 'Loading Email...' — that's what your clients see."*

---

## Gaps to close in the questionnaire

- **The 55% estate-tax sentence.** They must supply the correct current figure and framing.
  **Do not let anyone downstream copy that sentence forward or guess a replacement number.**
- **A logo** — there is none, anywhere. Or a decision to have one made.
- **A tagline / positioning line** — the site's slogan div has been empty for 25 years.
- **Office hours.** Published nowhere.
- **Service area** — towns, counties, and what "throughout the nation" actually means.
- **The correct firm name rendering**, and whether the About page's omission of Wallis is
  simply stale copy.
- **Founding year — 1983, or 1993, or both?**
- **Who is currently at the firm.** The site lists four partners; the IRS PTIN directory lists
  five different-ish names at the same address. Ask warmly, not forensically.
- **Partner bios, credentials, license numbers, and headshots.** Nothing exists for anyone.
  **A firm sold on relationships publishes nothing about its four people** — this is the
  highest-value content ask on the job.
- **Peer Review — what year, and is there a current cycle?**
- **`SEC Related Services`** — deliberately discontinued, or lost?
- **Do they want the CCH Newsletters, Info Center and the ~150-calculator Financial Tools
  library carried forward?** All vendor-syndicated; keeping them means keeping a CCH
  dependency.
- **Is the reciprocal client link (Bit by Bit) intentional, and is naming a client by name
  something they want to continue?**
- **A photograph of anything** — the office, the building they own, the four of them. The
  entire site has two images: a 1×1 spacer and a stock Manhattan skyline.
- Worth mentioning as free wins, not as a sale: **two dead federal links** (Form 2848 and Form
  I-9 both point at hosts that no longer exist), **four typos in their own meta keywords**,
  **no favicon**, and the fact that **every link to their site previews as a blank box** when
  shared. Also: **nobody has ever asked their clients for a review.**

---

## Note on this dossier's timing

The 2026-07-29 prospecting run scored all 12 candidates and named three finalists, but only the
DiSalvo dossier was written before the run was interrupted. The Orange Valley and Stetz
dossiers complete it. The `site-content.md` full-text capture for this firm was written the
same day as this dossier; its findings are marked above as either **re-verified by me against
the live site and the firm's own 2002 archive on 2026-08-13**, or **carried forward from the
capture**. The 07-29 scoring notes' three headline claims — no logo, the 55% rate, and the
"Loading Email..." render — all held up under direct re-verification.
