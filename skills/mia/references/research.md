# Research threads

Each thread is one subagent. It reads `brief.md`, this file's common section
and its own section, and `sources.md`. It writes one note to
`workspace/<slug>/notes/<thread>.md` and returns a summary of under 300
words to the main agent: what it found, what it could not find, and what it
would ask the founder.

## Common to every thread

- The reader of the note is the composer, who has not seen your sources.
  Write findings as short, complete statements with the number, the date,
  the geography and the link on the same line.
- Every number links to the page it came from, or is labelled
  `Calculated: <how>` or `Assumption: <why>`. A search that found nothing is
  worth recording: "Searched N sources for X; not found" tells the analyst
  where to ask the founder.
- Stop when the pattern stabilises, not when sources run out. At basic
  depth that is about fifteen sources; at full depth about thirty. Note in
  the last section what a deeper pass would look at.
- Company-specificity test for every finding: if the sentence would be
  true of any company in the sector, it does not belong in the note.
- Founder material is a claim until an independent source confirms it.
  Where the brief lists a claim in your area, check it and record the
  verdict with the evidence.
- Distinguish what ships from what is announced. Roadmap is not
  capability.

Note shape:

```markdown
# <Thread>: <Company>

## Findings
- ...

## Numbers used
| Figure | Value | Year | Geography | Source |
|---|---|---|---|---|

## Founder claims checked
| Claim | Verdict | Evidence |
|---|---|---|

## Searched, not found
- ...

## Questions for the founder
- ...

## For a deeper pass
- ...
```

## Market

The question: how big is the problem the company solves, in the geography
it sells into, and is it growing?

- Define the market by the problem and the buyer, then find which analyst
  categories map to it. Most sizing errors start with adopting a report's
  category as the market.
- One TAM. When the company sells into more than one segment, combine the
  segments, then deduct the overlap between them with a stated basis
  (which vendors sell into both, what share of the smaller segment that
  represents). Never one TAM per product.
- Use the analysts' own method where it fits: broad bucket times a
  specialisation factor. The broad bucket is the widest measurable spend
  pool for the problem; the factor is the slice this company's kind of
  product can address. State both.
- Two years: the current year and one projected year, from a published
  CAGR, labelled as projected.
- SAM by geography (the beachhead's share of the global pool, sourced),
  then by the buyer segment for whom the product's differentiator decides
  the purchase. SOM as the pool in the first market (India, typically) and,
  separately, what the company could plausibly earn in three years at its
  published price with a stated account and seat count.
- Name the biggest and fastest-growing geography for this problem outside
  the United States, with the source. That is a standing question from the
  partners.
- Growth as named drivers with points of annual growth each, including at
  least one counter-driver, summing to the forward rate. Read the trends
  note if it exists; do not invent generic drivers.
- Sanity checks before writing: does the TAM exceed $10 trillion (the
  definition is too broad), is SAM below TAM and SOM below SAM, what do
  buyers actually pay today for this exact category (a realised figure
  from vendor disclosures is often a hundredth of the analyst pool, and
  that gap is a finding), and what happens to the SOM if the two weakest
  assumptions move.
- Build the chain before reading the founder's figure. Then compare: is
  the founder's number inside your range, and what did they count that you
  did not.

## Trends

The question: over the next five to ten years, is the market moving for or
against this company, and what is the single force that dominates?

- Scan six directions: regulatory, technology, buyer behaviour, macro,
  competitive, social. Render only forces with a transmission mechanism to
  this company's buyer, price, distribution or cost. Record the directions
  that produced nothing.
- Each force: direction (tailwind or headwind), category, horizon (0-2y,
  2-5y, 5y+), what it does to this company in one or two sentences, what
  would flip it, and a caveat on the evidence if the source is single or
  interested.
- Include what the large players and customers are saying and doing about
  the problem: analyst hype-cycle placement and category names (check the
  analyst houses by name), incumbents shipping or bundling into the space,
  large buyers piloting or procuring. This is the buyer-behaviour lens; a
  named procurement is worth more than ten press releases.
- Force headwinds. A scan with no headwinds has not looked. Name the
  strongest one and say plainly whether it could break the thesis.
- Structural forces (statute, physics, ratified standards, open-source
  substitution) compound; cyclical ones (rates, sentiment) reverse. Say
  which each is.
- Net assessment: the dominant tailwind, the dominant headwind, why one
  outweighs the other, and what would tip the balance either way.

## Competitors

The question: if this company did not exist, what would the buyer do, and
what do they pay for it today?

- Organise by the purchase the buyer actually makes, from most to least
  common: doing nothing or building in-house; a feature inside a platform
  they already pay for; adjacent products that solve the same job; the
  direct category; the infrastructure the product is built on. Status quo
  is always the first group.
- For each group: who and what, what the buyer pays (price points), the
  evidence of spend (revenue, customer counts, capital raised), and what it
  means for this company.
- For each named company: what the buyer pays and the traction evidence,
  capital raised in $M as a number, stage and last round with the lead
  investor, and one or two sentences on why it matters for this deal. Link
  the company name to the funding source. Blank funding means "searched N
  sources, not found", written in the note.
- India and global both. Name the local players even when the global ones
  dominate the deck.
- Check the founder's reference set: which named competitors are genuine
  comps, which are adjacent, and which real comps the founder omitted.
  Omissions are the finding.
- Claimed white space: who already occupies it from above (incumbents),
  below (free and open source) and the side (funded entrants), and what
  genuinely remains. Say whether what remains is months or years to copy.
- Business models: how each group captures value (per seat, usage, bundled,
  free core plus enterprise tier) and why each competitor chose its
  approach. Different approaches are bets, not mistakes; write the why.

## Claims

The question: which of the founder's statements survive contact with
independent evidence?

- Take every claim from the brief. For each: verdict (verified, partly,
  contradicted, unverified), the evidence with links, and the question to
  ask next if it is unresolved.
- Testable claims (numbers, customers, features shipped, patents) are
  checked against filings, registries, package indexes, the company's own
  sites, and the other threads' notes. Experience claims (the founder's
  history) are checked for internal consistency across the deck and the
  call. Narrative claims are checked by whether any independent source says
  the same thing.
- Coordinate with the other threads: the market thread produces the
  founder-TAM comparison, the competitor thread the reference-set check,
  the trends thread the why-now check. Read their notes when they exist and
  cite them instead of repeating the work.
- Produce the next-call questions in priority order: what to ask, why it
  matters, and what a good answer looks like.

## Features (optional)

The question: on the capabilities this buyer evaluates, where does the
product lead, where does it lag, and where is nobody strong?

- Axes come from how buyers evaluate, not from vendor menus. Three tiers:
  table stakes (present or absent, summarised in one line, not a table),
  differentiators (0-3, using the full range: 1 basic, 2 solid, 3 best in
  set), and architectural bets (a sentence each, not scored).
- Score only what documentation, pricing pages, registries or a trial
  shows. Marketing copy earns "unverified", not a score. Announced but
  unshipped scores 0.
- Compute the strongest other solution per row and the total per solution.
  Pricing tiers per solution in one table.
- Name the white space, whether the target stands in it, and which
  differentiators are converging to table stakes.

## Sentiment (optional)

The question: what do real users and developers say about the incumbents
and the problem, and does it match the founder's story?

- Discovery before validation: collect pain themes, workarounds and
  switching triggers first, then check the founder's claims against them.
  Starting from the claims finds only confirmation.
- Sources by signal type: experiential and specific (detailed reviews,
  issues with reproduction steps) carry the most weight; comparative
  (versus threads, migration posts) next; directional (short reviews,
  social) and indirect (job posts, workaround questions) only with
  corroboration. Ratings are not evidence.
- Sample until patterns stabilise; note sample size per finding and where a
  platform was inaccessible.
- Report unmet needs the pitch does not name; those are often the finding.

## Bottoms-up (optional)

A cross-check on the top-down number, not a second tab: customer count in
the beachhead times a price anchor (founder-shared pricing first, then
current-alternative spend, then comparable products), with the fund-math
question answered in one line. It lands as a row in Market size's sanity
checks; a divergence above threefold from the top-down SAM is written up as
a finding, not reconciled away.
