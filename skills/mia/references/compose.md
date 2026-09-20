# Composing the workbook

The composer reads `brief.md`, every note in `notes/`, `sheet-dialect.md`,
this file and the exemplar, then writes one file per tab into `sheet/`. It
is one subagent with everything in context, so it can write the Summary
from the tabs rather than from the notes.

The reader is an analyst with ten minutes before a partner check-in. They
should be able to read the Summary alone and act, and open any other tab to
see the evidence behind one line of it. The exemplar in `exemplar/` shows
the density that works; match it.

## Writing rules

- Every cell carries information the reader would otherwise have to go and
  find. A cell that restates its row, hedges, or fills a column for
  symmetry is left empty.
- Table cells hold one or two sentences. Lead paragraphs hold two. Notes
  under a section hold one. The checker enforces 350 characters per cell.
- Numbers come with their unit and, where the column mixes text, their
  year: `$3.34B (2026)`. Where a column is numeric, the unit sits in the
  header and the cells hold plain numbers so they sort.
- Every number, date and price links to its source, inline, on the first
  place it appears in a tab. The Sources tab lists each URL once.
- Plain words. Say what a thing does or what a number is, in sentences
  with a verb. Straight quotes, hyphens, periods and commas; the checker
  rejects em dashes, en dashes and curly quotes.
- Founder statements appear as claims with a status glyph, never as facts.
- Say what was not found. "Searched three sources; no ARR disclosed" is a
  finding the analyst can act on.
- Write from this deal's notes. The exemplar is a fictional company and
  shows shape, not content.

## Tab by tab

### 01-summary.md

Title: `<Company>: market intelligence`. Subtitle: one line with HQ, age,
headcount, stage, the ask, and the products in a clause each.

1. **Read.** Five or six bullets, each under 30 words, each a conclusion
   with its number. Written last, from the other tabs. The first bullet is
   the market in one line; the last is the regulatory or timing read.
2. **Key numbers.** A table: Metric, Value, Compared to. Eight rows at most:
   ask, runway, team, the traction number, paying customers, published
   price, the competitive capital fact, non-dilutive money. "Compared to"
   holds the number that gives the value meaning.
3. **Signals.** The four forces that decide the deal, from Trends: Signal,
   What it does, Direction, Horizon, Caveat.
4. **What could change.** Two key-value rows: Toward invest, Toward pass.
5. **Legend.** The glyphs, the direction arrows, the status marks, the chart
   accent, and which optional tabs were not run.
6. Two charts: the funnel from Market size (TAM, geography, SAM, SOM pool)
   and capital raised by buying group from Competitors.

### 02-market-size.md

Title `Market size`. Subtitle: the one-TAM rule in a sentence and the
currency.

1. **The problem being sized.** One paragraph: the job, the budget lines
   that pay for it today, and any line that barely exists yet.
2. **TAM, SAM, SOM.** One table: Step, Line, current year, projected year
   (labelled projected), Basis and what moves it. Section rows for TAM,
   SAM, SOM. Overlap deductions as negative rows. The TAM row's basis
   carries the range and the founder comparison. No confidence column;
   confidence lives in the basis text.
3. **Sanity checks.** Three or four bullets: what buyers pay today for the
   exact category, the TAM without the weakest line, the weakest links and
   what they do to SOM, what was deliberately not used. The bottoms-up
   cross-check lands here when run.
4. **Growth.** A table of drivers with points of annual growth, one
   counter-driver at least, and the evidence. One chart of the same
   points, signed format.
5. One chart: the funnel.

### 03-trends.md

Title `Trends`. Subtitle: the count of tailwinds and headwinds and the
verdict.

1. **Net assessment.** Key-value rows: dominant tailwind, dominant
   headwind, why one wins, what tips to net tailwind, what tips to net
   headwind. One chart: tailwinds and headwinds by category, stacked.
2. **Forces.** One table: #, Trend, Direction, Category, Horizon, What it
   does to the company, What flips it. Ten to fourteen rows; every row
   survives the company-specificity test.
3. **What buyers and incumbents are doing.** Three to five bullets:
   analyst placement, incumbent moves, named large buyers piloting or
   procuring, with links.
4. **Checked and dropped.** Bullets naming the forces that failed the
   specificity test, so the omission is visible.

### 04-competitors.md

Title `Competitors: what buyers pay for today`. Subtitle: the organising
principle in a sentence.

1. **How the problem gets bought.** One table, groups ordered from most to
   least common: #, What the buyer does, Who and what, What they pay,
   Evidence of spend, So what for the company. Status quo is row one.
2. **Where capital has gone.** A note and one chart: raised by group, the
   company's own group highlighted.
3. **Companies.** One table with section rows per group: #, Grp, Company
   (linked to the funding source), What the buyer pays and traction, Raised
   $M, Stage and last round and lead, Why it matters. Blank funding cells
   are intentional and the note above the table says so.
4. **Claimed white space, and who is already in it.** A table: Claim,
   Occupied from (above, below, side), By, Read. Then a "what remains" row.
5. **Founder's reference set, checked.** Key-value rows: genuine comps,
   adjacent, incumbents, missing.
6. **Could not be determined from desk research.** Bullets.

### 05-founder-claims.md

Title `Founder claims`. Subtitle: what was said where, and that it was
checked against public sources.

1. **Deal at a glance.** Key-value rows from the brief: company, products,
   ask, the fund's standard terms, team, cap table, buyer, materials.
2. **What the founder said, checked.** A note with the status legend, then
   a table: #, Founder said, Where (linked), Status, What we found. Twelve
   to twenty rows; the TAM comparison and the reference-set check are rows
   here.
3. **Next call: questions in priority order.** A table: #, Question, Why,
   What a good answer looks like. Eight to ten rows.

### 06-feature-matrix.md (optional)

Title `Feature matrix`. Subtitle: the glyph legend and the evidence base.
A **Read** of three bullets. Then `<!-- matrix -->` tables with the target
in a bold header column: differentiators for the primary set, a scorecard
table (Feature, target glyph, strongest other), the secondary set if the
company straddles two categories, a pricing table, and a chart of total
score per solution. Table stakes are one note line, not a table. End with
caveats.

### 07-public-sentiment.md (optional)

Title `Public sentiment`. Subtitle: which platforms, when pulled, what was
inaccessible. A **Read** of three or four bullets. Tables: claims against
the public record (Claim, Verdict, Evidence, Tier, Confidence), pain
themes (Theme, Frequency, Evidence, Severity, Affects), opportunities the
pitch does not name (bullets), coverage (one bullet).

### 99-sources.md

Title `Sources`. One table: Source (linked), Publisher, Tier, Used for. Every
URL that appears on any tab, once. Grouped by tab with section rows when
there are more than thirty.

## Before handing back

Run the `render_sheet.py <workspace>` command your dispatch prompt gives you;
it carries the absolute path to the script. Read `checks.md`. Fix every fail in the tab file it names and render again
until the result line reads PASS. Warnings are read and either fixed or
mentioned in the delivery note.
