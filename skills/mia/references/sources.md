# Sources

Sources are the analyst's biggest time sink and the reason the workbook is
trusted. Every number, date, price and quote in the workbook links to where
it came from, and the reader can tell at a glance how much to trust it.

## Link format

Write links inline in the note or the cell, markdown style, on the thing the
source supports: `[$24M raised](https://...)`, `[168 downloads last month](https://...)`.
When a whole cell is the source, link the name: `[Recallio](https://...)`.

Only link a URL you opened in this run. A fact you remember without a page
you visited is written as `Assumption: <rationale>` or left out. A page you
could not open is noted as "not accessible" with the URL, not cited as read.

Every URL used on any tab is also listed once on the Sources tab with the
publisher, the tier it was trusted at, and what it was used for.

## Credibility model

Tier is a property of the claim a source supports, not of the publisher. A
company's own blog is tier 1 for what that company shipped and tier 3 for
the size of its market.

**Tier 1, primary and reproducible.** Regulator filings and gazettes (SEBI,
ROC, RBI, SEC, MeitY), DRHPs and annual reports, statutory disclosures,
package registries and repositories for what a product contains, pricing
pages for what a product costs, Big Four and MBB reports that disclose
methodology.

**Tier 2, credible secondary.** Established research houses with stated
methodology (Gartner, Forrester, IDC, MarketsandMarkets, Mordor, Grand View,
IMARC, BCC, Allied), industry bodies (NASSCOM and trade associations),
Reuters, Bloomberg, ET, Mint for events and quotes, Crunchbase, PitchBook,
Tracxn and press releases for funding, World Bank and UN agencies for macro.

**Tier 3, usable with a caveat.** Consultant reports made for one company,
comparison blogs, forums and social platforms for sentiment, G2, Capterra and
Product Hunt for feature and review signal, vendor marketing pages for
claims about themselves. A tier 3 source carries a finding only when a tier
1 or 2 source corroborates it; on its own it earns a flag in the cell or the
note.

**Not credible for numbers.** Statista and similar aggregators (find the
original they cite and go there), SEO-driven market-size posts, Wikipedia as
a final source, AI-generated summaries without a primary source.

**An unfamiliar source** is judged on four things: methodology disclosed,
sample and scope concrete, conflict of interest, and independent
corroboration. Two of four is a tier 3; all four is a tier 2.

## Disagreement

When two credible sources disagree, keep both numbers, say which one the
sheet uses and why, and link both. Averaging two different definitions
produces a number nobody published.

## Founder material

Decks, one-pagers and call transcripts are tier 1 for what the founder said
and tier 3 for whether it is true. Record the statement as a claim with its
source, then look for the independent source that confirms or contradicts
it. Founder-shared pricing and cost data is the best available anchor for
sizing and is used, labelled as founder-provided.

## Sector playbook

Where the signal lives, by sector, from the analysts' own practice:

| Need | Look at |
|---|---|
| Problem in the buyer's own words | Reddit, sector forums, GitHub issues, support threads |
| Product feature and pricing signal | G2, Capterra, Product Hunt, vendor pricing pages, package registries |
| B2B sourcing and unit economics in India | IndiaMART enquiries, franchise and distributor calls, DRHPs of listed peers |
| Buyer behaviour at scale | Job postings that name tools or build in-house, procurement notices, case studies with named vendors |
| Regulation | Gazette notifications, ministry press releases, law-firm client notes for dates and scope |
| Category status | Analyst hype cycles and quadrants, conference tracks, category names in research titles |
