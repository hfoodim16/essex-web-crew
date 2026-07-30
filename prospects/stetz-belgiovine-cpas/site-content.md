# Site content capture — Stetz, Belgiovine, Manwarren & Wallis, P.C.

**Source:** https://www.sbcpas.com/
**Captured:** 2026-07-29
**Platform:** **CCH Site Builder**, template `Arrival`, colorScheme `blue`. Every asset
carries the cache-buster `d=1708180317768` = **2024-02-17**; `sitemap.xml` independently
shows `<lastmod>2024-02-17</lastmod>` on all 9 URLs. **The site has not been regenerated in
2½ years, and the firm-written copy dates to roughly 2003.**
**Completeness:** all 8 nav pages + the hidden contacts page captured. No page failed to fetch.

> This file is the **content-parity source of truth**. Everything the old site says must
> appear on the new site or be listed as deliberately dropped in `website-plan.md`.

## Navigation structure (link labels verbatim)

| Label | URL |
|---|---|
| Home | `home.html` |
| Firm Profile | `firm_profile.html` |
| Client Services | `client_services.html` |
| Info Center | `info_center.html` |
| Newsletters | `newsletters.html` |
| Financial Tools | `financial_tools.html` |
| Links | `links.html` |
| Contact Us | `contact_us.html` |

No sub-navigation, no dropdowns. `index.html` and `home.html` are byte-identical.
**Pages that do NOT exist** (all 404): `client_portal.html`, `financial_guides.html`,
`tax_tools.html`, `services.html`, `about.html`.

**A ninth page exists but is unreachable from the nav and absent from sitemap.xml:**
`contact_us.html?id=19128` — the partner list. It is reachable only by clicking an unstyled
`<input type="submit" value="View Contacts">` button. **The firm's entire team presence is
hidden behind a form button and is uncrawlable.**

## Vendor content vs. firm content — read before transferring

This site is **mostly not theirs.** Three of the eight pages (`info_center.html`,
`newsletters.html`, `financial_tools.html`) are **100% CCH-syndicated vendor widgets** — a
tax-news feed, ~250 financial calculators, and IRS form libraries. The firm neither writes
nor owns any of it.

**Do NOT carry the vendor content into the rebuild.** It is also the source of the site's
staleness illusion: the newsletter feed reads current to 2026 because CCH pushes it
automatically, while everything the firm actually wrote is frozen.

**The firm's own words exist on exactly three pages:** Home (3 paragraphs), Firm Profile,
and Client Services. Those are the parity obligation. Plus two load-bearing live
integrations on the Links page.

---

## Page: Home (https://www.sbcpas.com/ and /home.html)

**Firm-written copy — the complete text, all of it:**

> Welcome and thank you for visiting our Website. In addition to providing you with a profile
> of our firm and the services we provide, this Website has been designed to become a helpful
> resource tool to you, our valued clients and visitors. Our dedication to superior client
> service has brought us to the Internet as we endeavor to continue to provide the highest
> quality professional service and guidance.

> As you browse through our Website, you will see that not only have we highlighted
> background information on our firm and the services we provide, but have also included
> useful resources such as informative articles (in our Newsletter section) and interactive
> financial calculators (in our Financial Tools section). In addition, we have taken the time
> to gather many links to external Websites that we felt would be of interest to our clients
> and visitors (in our Internet Links section).

> While browsing through our Website, please feel free to contact us with any questions or
> comments you may have - we'd love to hear from you. We pride ourselves on being proactive
> and responsive to our clients' inquiries and suggestions.

The rest of the home page is a **CCH-syndicated tax-news feed** (7 auto-fed headline+teaser
blocks) plus a `Message Us` button. Footer contains only: `Designed by CCH Site Builder`.

**Note what is absent:** no tagline, no headline, no hero text, no phone number, no address,
and no service list anywhere on the home page. The only human-written words are the three
"welcome to our website" paragraphs above — **and those are CCH template boilerplate the firm
never replaced.** This page has effectively zero transferable content.

---

## Page: Firm Profile (https://www.sbcpas.com/firm_profile.html)

**Complete verbatim text — this is the firm's entire self-description, all of it:**

> Stetz, Belgiovine and Manwarren, P.C. has been operating in its present form since 1993 as
> a prolific accounting firm servicing small to medium size businesses and individuals. The
> firm's Senior Partner and it's Principals were formerly with a medium size accounting firm
> from Central New Jersey. Over the course of a decade, the firm's Principals have devoted
> time and effort to creating a philosophy of customized professional services specific to
> your needs. The firm does this by getting to know you and your business thoroughly and then
> devising the most cost effective solutions. This is accomplished through a team effort of
> intellectual ability, state of the art technology and the benefits of practical experience.
> The firm prides itself in being able to deliver sophisticated technical services to those
> who ordinarily would not have access.

> Our firm's success is based upon some basic concepts. We deliver high quality work
> expeditiously and cost effectively. If you have a problem, we will work with you to find
> alternatives.

> In the spirit of quality the firm is a member of the New Jersey Society of Certified Public
> Accountants and the American Institute of Certified Public Accountants. The firm has also
> successfully completed Peer Review.

> We believe in the value of relationships. We view every client relationship like a
> partnership, and truly believe that our success is a result of your success.

> We are committed to providing close, personal attention to our clients. We take pride in
> giving you the assurance that the personal assistance you receive comes from years of
> advanced training, technical experience and financial acumen. Our continual investment of
> time and resources in professional continuing education, state-of-the-art computer
> technology and extensive business relationships is indicative of our commitment to
> excellence.

**Three flags for the Planner:**
1. **The page calls the firm "Stetz, Belgiovine and Manwarren, P.C." — no Wallis** — while the
   header and page title say "Stetz, Belgiovine, Manwarren and Wallis, P.C." **The site
   contradicts itself on its own name.**
2. Two errors in the opening sentences as published: **"it's Principals"** (should be *its*)
   and **"Over the course of a decade"** — written when the firm was ~10 years old, i.e.
   **circa 2003**, never updated. The firm is 33 years old by its 1993 date, 43 by its 1983 one.
3. **Zero people on this page** — no staff names, no credentials, no bios, no photos, no emails.

**Real facts worth carrying:** member of the **New Jersey Society of Certified Public
Accountants** and the **American Institute of Certified Public Accountants**; has
**successfully completed Peer Review**. Those are genuine credentials and currently buried.

---

## Page: Client Services (https://www.sbcpas.com/client_services.html)

**Intro verbatim:**

> Our firm offers a wide range of services to our individual and business clients. Because our
> firm is relatively small, our clients benefit by getting personalized, quality service that
> is beyond comparison. Below we have listed the services that we offer to our clients along
> with a brief description.

> As the list below is by no means all-inclusive, please feel free to inquire about a service
> if you do not see it listed. If it is not a service we provide, we would be more than happy
> to refer you to a qualified professional.

**Jump-link index at the top, in this order:** Management Advisory Services · Forensic
Accounting · Tax Preparation And Compliance · Litigation Support Services · Estate And
Retirement Planning · Accounting, Auditing, Review & Compilation Services

**Grouping headings preserved exactly as published.** Note they are incoherent — three group
headings for six services, with four services filed under "Miscellaneous". Each service is
followed by a `Go To Top` link.

### Group heading: Consulting Services

**Management Advisory Services**
> Stetz, Belgiovine and Manwarren uses all the benefits of its Accounting, Auditing,
> Computerization, Compliance Regulations, and Taxation skills to render Management Advisory
> Services ("MAS"). MAS is the service of rendering advice on non specific Accounting,
> Auditing and Taxation issues. The firm counsels you from existing knowledge about your
> business, the circumstances, the technical matters involved, representations, and the mutual
> intent of the parties involved. Stetz, Belgiovine and Manwarren acts in an Advisory Capacity
> to develop findings, conclusions, and recommendations for your considerations and decision
> making. The firm also renders Implementation Services, Transaction Services, Staff and other
> Support Services. MAS really allows us to give you full financial services. It allows us to
> interact with you. Interaction with you is the keystone of our philosophy for servicing your
> needs.

> Our Services Include: · Editing business plans. · Recommending computer software. ·
> Operational review and improvement studies. · Analysis of an accounting system. · Assistance
> with strategic planning. · Defining your information system. · Assistance with mergers of
> organizations. · Insolvency services. · Valuation services. · Preparation of information for
> financing. · Analysis of a potential merger or acquisition. · Assistance in substituting for
> bookkeepers. · Assistance in controllership activities

### Group heading: Accounting Services

**Forensic Accounting**
> We use accounting and auditing skills to provide an analysis of financial records in
> conjunction with dispute resolutions, as well as fraud and theft investigation. Our damage
> measurement methods can determine the extent of financial loss and illegal accounting
> practices.

### Group heading: Miscellaneous

**Tax Preparation And Compliance**
> Stetz, Belgiovine and Manwarren believes that taxation is one of the largest singular
> expenses faced by an individual or business. The firm endorses client awareness and
> education regarding the seriousness of tax laws beyond the financial consequences. Tax laws
> are complex, confusing and ever-changing. Due to the nature of tax laws, our professionals
> attend many continuing professional educational courses. In addition, the firm subscribes to
> various comprehensive tax information services. The acquisition of current information
> enables the firm to keep you in compliance. The firm believes that proper "tax planning" can
> give rise to opportunities for savings. The objective of the firm is to minimize or defer
> your tax liabilities in order to foster growth and security.

> Our Services Include: · Tax return preparation for any kind of entity for Federal and State.
> · Representation before all taxing authorities. · Estate and gift tax return preparation. ·
> Planning of tax strategies for certain transactions, i.e., business dispositions,
> reorganizations, mergers and acquisitions, and real estate.

**Litigation Support Services**
> Due to the litigious nature of today's society and business environment, CPAs are frequently
> called upon by attorneys to explain, support and document issues. Our intimate knowledge of
> your business enables us to assist your attorneys in developing effective strategies for
> you. Our Services Include: · Analyzing all tax records and interpreting financial data. ·
> Calculation of damage claims. · Assistance with trial depositions. · Preparation of trial
> exhibits. · Rendering an expert opinion. · Appearances as an expert witness. · Assistance in
> settlement proceedings. · Business valuation services. · Assistance with mediation.

**Estate And Retirement Planning**
> At Stetz, Belgiovine and Manwarren one of our major concerns is assisting our clients in
> preserving their wealth. With Estate Tax rates reaching as high as 55%, Estate Tax planning
> is probably the most effective planning available. Through a series of interviews, our
> professionals put together a profile of your financial data and personal preferences.
> Recommendations are then brought forward with the objective of asset preservation, asset
> allocation and lowering estate taxes. After completion of the planning stages, we will assist
> you in communicating your goals and objectives to a qualified attorney that can draft the
> proper wills, trusts and other related documents. For retirement planning, our professionals
> acquire an understanding of your financial requirements at retirement. During this process,
> income tax consequences regarding the dispositions of assets, an early retirement package,
> social security benefits and pension distributions are explored. Through discussions and
> analysis of your financial position a plan is developed specifically for you to follow.

⚠️ **DO NOT CARRY THE "55%" FIGURE.** The 55% top federal estate-tax rate **expired in 2001**
and has been 40% since 2013. This is materially misleading tax information sitting live on a
CPA firm's website. The *service* transfers; **that number must be dropped or replaced by the
client**, never copied. Flag it to Harry — it is also the single strongest thing he can point
at on a call.

**Accounting, Auditing, Review & Compilation Services**
> Stetz, Belgiovine and Manwarren the Auditing, Review and Compilation services are the
> foundation for what we do. The firm takes special care to make sure ample time is spent on
> gaining an understanding of your business and its' needs. Our basic accounting services are
> inclusive of designing accounting systems specific for each individual client. The firm
> subscribes to various reporting services and continuing professional educational courses in
> order to keep up to date in the ever-changing environment of accounting and auditing. The
> scope of the firm's services range from Certified Audits for Companies to write ups for "Mom
> and Pop" businesses. Regardless of level of service requested, a professional is chosen that
> matches with the client and the level of expertise required. The members of the firm are
> intimate with a number of industries including but not limited to the following: Automobile,
> Collectibles, Communications, Contractors, Distributors, Entertainment, Fast Food Franchises,
> Health Care, Importers, Law Practices, Licensing, Manufacturing, Music, Not For Profits,
> Professional Practices, Real Estate Developers, Restaurants, Retail, Trucking, and Wholesale.
> In keeping with the fast changing world of computers, the resulting technology has enabled us
> to efficiently and cost effectively integrate computer applications. As a result of this
> technology, we are able to service clients throughout the nation.

*(First sentence is broken English as published — "Stetz, Belgiovine and Manwarren the
Auditing, Review and Compilation services are the foundation…"; also `its' needs`.)*

**That 20-industry list is the single most valuable content asset on the site** — real,
specific, and a ready-made industries grid: Automobile · Collectibles · Communications ·
Contractors · Distributors · Entertainment · Fast Food Franchises · Health Care · Importers ·
Law Practices · Licensing · Manufacturing · Music · Not For Profits · Professional Practices ·
Real Estate Developers · Restaurants · Retail · Trucking · Wholesale.

**Parity note:** parity here means **carrying the facts, not the structure.** The "Miscellaneous"
grouping is incoherent and must be re-grouped; the 20-industry list and every "Our Services
Include" bullet must survive.

---

## Page: Info Center (https://www.sbcpas.com/info_center.html)

Complete verbatim — two CCH-hosted vendor widget descriptions, no firm-authored content:

> **Events Calendar**
> The interactive calendar highlights federal and state tax due dates, special firm events and
> other important dates that may be of interest to you. Because the calendar is continually
> updated, check back often to keep track of filing requirements, deadlines and other events
> that will help you stay current and up-to-date.

> **Federal Tax Forms & IRS Publications**
> Looking for a federal tax form? Browse this online tax forms library to find downloadable
> IRS forms. The forms are presented in PDF format and are acceptable for filing with the IRS.
> You may also choose from dozens of helpful tax publications developed by the IRS to help
> taxpayers have a better understanding of various tax issues. Available in PDF format, these
> publications are written in a plain language format geared specifically to taxpayers.

**Vendor content — do not carry.**

---

## Page: Newsletters (https://www.sbcpas.com/newsletters.html)

**100% CCH-syndicated feed. No firm-authored content whatsoever.** Section labels: `Tax
Alerts`, `Tax Briefing(s)`. Briefing links verbatim: `2026 Post-Filing Season Update` ·
`2025 Tax Year-in-Review` · `2025 Year-End Tax Planning` · `One Big Beautiful Bill Act
(Signed Into Law July 4, 2025)`. Feed carries federal and multi-state items (NJ, NY, CT, PA).

**Vendor content — do not carry.** This feed is the reason the site *looks* maintained.

---

## Page: Financial Tools (https://www.sbcpas.com/financial_tools.html)

**Intro verbatim** (the only firm-written words on the page):

> Should I refinance my mortgage? How much do I need to save for my child's college education?
> As accounting professionals, these are some of the questions that are posed to us on a daily
> basis. We are providing these interactive financial calculators and other tools to assist
> you with some of the day-to-day questions and concerns that may arise. While these financial
> tools are not a substitute for financial advice from a qualified professional, they can be
> used as a starting point in your decision making process.

**~250 CCH-hosted calculators in 11 categories:** Auto (4), Business (15), Debt and Credit
Cards (12), Insurance (13), Investment (23), Loan (13), Mortgage (25), Personal Finance (9),
Retirement (32), Savings (16), Tax (11).

⚠️ **Stale-content proof, verbatim from the vendor descriptions:**
- Self-Employment Tax Calculator: *"…use this calculator to determine your self-employment
  taxes for **tax year 2019**."*
- `U.S. 1040EZ Tax Form Calculator` — **the 1040EZ was abolished after tax year 2017.**
- `Roth (after-tax) Account or Pre-Tax Account?` — *"**Starting in 2006**, you may have the
  option to contribute to Roth account."*

**Vendor content — do not carry.**

---

## Page: Links (https://www.sbcpas.com/links.html)

**Intro verbatim:**

> There are many great sites on the World Wide Web but trying to actually find those great
> sites can be a frustrating experience. We have compiled a list of Websites that we have
> found to be helpful resources of information. When you click on a link, a new window will
> pop up. Close the window when you are ready to return to this page.

Grouped exactly as published, with verbatim descriptions and resolved hrefs:

**Others**
- `Pay Your Bill` → `https://secure.cpacharge.com/pages/sbcpas/payments`
  — **LIVE CPACharge payment portal. LOAD-BEARING: must survive the rebuild.**
- `Check IRS Refund Status` → `https://sa2.www4.irs.gov/irfof/lang/en/irfofgetstatus.jsp`
  — "Track your tax return through the IRS website."
- `SBCPAS - Secure File Transfer` → `https://sbcpas.smartvault.com/`
  — "Please click this link to transfer files (encypted) to our firm."
  — **This IS the client portal (SmartVault). LOAD-BEARING.** *(their typo "encypted")*

**Internet Resource**
- `Quickbooks Web Site` → `http://quickbooks.com` — "QuickBooks is a fast, easy way to manage
  your business finances.QuickBooks is also simple to learn and customizable to your business.
  That's why it is the #1 best selling accounting software." *(missing space after the period,
  as published)*

**Tax**
- `The Internal Revenue Service` → `http://www.irs.gov` — "Home of the IRS on the Web. The IRS
  has definitely done a nice job on their Website."
- `Form - SS4 Application for ID Number` → `http://www.irs.gov/pub/irs-pdf/fss4.pdf` —
  "Download Form SS4 From IRS Web Site / Adobe Acrobat Required"
- `Form - 2848 Power of Attorney` → `http://ftp.fedworld.gov/pub/irs-pdf/f2848.pdf` —
  "Download Form 2848 From the IRS Web site / Adobe Acrobat Required"
  — ⚠️ **DEAD LINK. FedWorld was shut down in 2011.**
- `Form - I9 Emloyment Eligibility Verification` →
  `http://www.ins.usdoj.gov/graphics/formsfee/forms/files/i-9.pdf`
  — ⚠️ **DEAD LINK. The INS ceased to exist in 2003.** *(and "Emloyment" is misspelled in the
  published label)*

**Client Sites**
- `Bit by Bit Computer Consutants` → `http://bitxbit.com` — "Bit by Bit has been in the
  business of providing technology solutions to companies in and around the Tri-State area.
  Our clients tell us that the solutions we provide allow them to experience better
  productivity, enhanced communications with their customers and most importantly, a
  significant increase in the bottom line."
  *("Consutants" misspelled as published; and the description is in **Bit by Bit's own first
  person** — "**Our** clients tell us" — pasted unedited onto the CPA firm's site.)*

**Two dead federal links and three misspellings on one page.** The most concrete,
screenshot-able defect for outreach. **Carry only the two load-bearing integrations
(CPACharge, SmartVault) plus the IRS refund link; drop the rest.**

---

## Page: Contact Us (https://www.sbcpas.com/contact_us.html)

Verbatim (re-verified by direct fetch 2026-07-29):

> **Stetz, Belgiovine, Manwarren and Wallis, P. C.**
> Certified Public Accountants
>
> **United States**
> 155 Pompton Ave
> Verona, NJ 07044
> Phone : 973-433-1100
> Fax : 973-433-1111
> Email  Loading Email...

*(`P. C.` with a space here vs `P.C.` in the header.)* Buttons: `Message Us`, `View Contacts`,
`Get Directions`. Google Maps daddr: `155+Pompton+Ave,+Verona,+NJ,+07044`. Tel links are real
and correct: `tel:9734331100`, `tel:9734331111`.

**Confirmed by my own fetch: only ONE office — Verona. No Montclair address anywhere in the
visible content.** No hours published. No suite number on the site (directories say Suite 204).

**`Email` renders as the literal string "Loading Email..."** — it resolves only after JS runs
*and* the visitor moves a mouse. **On a phone, or with JS off, the contact page shows no email
address at all.**

---

## Page: Contact Us → View Contacts (https://www.sbcpas.com/contact_us.html?id=19128)

The only page on the site with people on it. Verbatim, in order:

> **Larry W. Stetz , CPA** — Partner — Phone : 973-433-1100 ext. 130 — Email  Loading Email...
> **Alex Belgiovine , CPA** — Partner — Phone : 973-433-1100 ext. 110 — Email  Loading Email...
> **Robert Manwarren , CPA** — Partner — Phone : 973-433-1100 ext. 140 — Email  Loading Email...
> **Chris Wallis , CPA** — Partner — Phone : 973-433-1100 ext. 260 — Email  Loading Email...

*(The spacing before the commas is as published.)* **No bios, no photos, no titles beyond
"Partner", no visible emails.** Not in the nav, not in sitemap.xml.

**The four direct-dial extensions are real, transferable content and currently invisible.**

---

## Site defects — concrete and quotable (for the pitch and the rebuild brief)

**What IS wrong:**
- **No logo.** `/images/logo.gif` is referenced as the logo but is a **43-byte, 1×1
  transparent GIF spacer** — downloaded and verified 2026-07-29 (`GIF image data, version
  89a, 1 x 1`). The visible header is a plain text wordmark in the template's default font
  (`<span class="title">Stetz,  Belgiovine, Manwarren and Wallis, P.C. </span>` — note the
  double space, as published).
- **Header image is a stock photo of New York City.** `/images/header.jpg`, 1900×450, 122 KB
  — a night shot of the Lower Manhattan skyline with the Brooklyn Bridge, from the CCH
  "Arrival / blue" template. **A photo of Manhattan atop a New Jersey firm's website.**
- **No tagline, no hero.** The `<div class="container slogan">` exists in the markup and is
  **empty**; `<div class="header__img--message">` is empty too.
- **Footer has no NAP and no copyright.** `<div id="copyright" class="copyright footer">`
  contains only `Designed by CCH Site Builder`. Its three columns (`col-left`, `col-middle`,
  `col-right`) are entirely whitespace.
- **Zero local SEO.** Grep across `home.html`: `application/ld+json` **0** · `LocalBusiness`
  **0** · `canonical` **0** · `og:` **0** · `twitter:` **0**. `<title>` is `Stetz,  Belgiovine,
  Manwarren and Wallis, P.C.  - Home` — double spaces, **names no service and no town.**
- **Meta description truncated mid-word**, ending at `"Our dedica"`, and it is template
  boilerplate naming neither service nor town.
- **Deprecated KEYWORDS meta with four typos of their own:** "Certified Public **Accountanta**",
  "**Compliation**", "**Entrepenuer**", "**Finacial Statemets**" — and it names **Gary Stetz**,
  who appears nowhere on the site.
- **Ancient dependencies:** jQuery **1.11.1** (May 2014) alongside jQuery 3.5.1, Bootstrap 3
  (EOL 2019), jQuery UI 1.12.1.
- **An IE6-era proprietary PNG hack, still shipping:**
  `<style>img { behavior:url("images/pngbehavior.htc"); }</style>`
- **IE8 conditional stylesheet** + `ie10-viewport-bug-workaround.js` + `X-UA-Compatible`.
- **Non-standard doctype:** `<!DOCTYPE html SYSTEM "about:legacy-compat">`
- **Table-based layout on the content pages** — `contact_us.html` nests the whole address
  block in stacked `<table>`s with `align="left"` and `<b>` for headings.
- **Inline styles with a mobile-overflow bug:**
  `<div style="float: right;width: 100%; padding-right: 100px; padding-bottom: 10px;">`
- **The only contact form is a 1990s popup:**
  `window.open('//www.sbcpas.com/content/plugins/leadgenerator.php','_blank','width=550,height=760,…,resizable=no')`
  — popup blockers eat it and **it is unusable on a phone.**
- **Team page behind a form submit button**, unstyled, uncrawlable, absent from sitemap.
- **Email requires JS + a mousemove** to exist at all (Obfuscapery v1.10, © 2011). **Fails our
  own JS-off gate.**
- **Two dead federal links**; **materially wrong tax content** ("55%" estate rate, "tax year
  2019", 1040EZ, "Starting in 2006").
- **No hours, no suite number, no team photos, no bios, no imagery of the firm, no service-area
  page, no Google Business Profile found.**

**What is NOT wrong — do not claim these, he'd know:**
`<meta name="viewport" content="width=device-width, initial-scale=1">` **is present** (verified
by my own fetch); Bootstrap 3 grid classes are real and the **hamburger nav works**; `tel:`
links are real and correct; the site is served over HTTPS; **SmartVault and CPACharge are live
and modern.** This is a *responsive but dated* site, not a fixed-width one.
