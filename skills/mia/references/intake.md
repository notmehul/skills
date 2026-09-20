# Intake

Intake turns whatever exists on a deal into one brief the research threads
share, then asks the analyst only what the materials could not answer. It
runs in the main conversation because it is the one place questions go to a
human.

## 1. Read everything first

Read in this order and note where each fact came from:

1. Founder-provided documents in Drive: deck, one-pager, financial model,
   product docs. Speaker notes in decks often carry the sizing derivation
   and the valuation logic; read them.
2. The Attio record: stage, source, linked people, analyst notes. Analysts
   maintain it, so its fields are the baseline for identity facts. Its
   enrichment fields (description, location) can be stale; a statutory
   filing or the company's own site wins over them.
3. Fireflies transcripts of calls with the founder. The richest source for
   cap table, pipeline names, competitor framing, and hedged claims that
   never make it into a deck. Read the whole transcript, not the summary.
4. Anything the analyst pasted.
5. The company's own web properties, package registries, filings, for what
   the product actually is today.

When sources disagree on a time-sensitive fact (revenue, customers, product
stage), the most recent source wins and the older one is kept in the brief
as a conflict. When they disagree on a stable fact (incorporation date,
market definition), the more precise source wins. Founder-facing material
outranks CRM enrichment; a call outranks a deck on product stage because
founders are more candid verbally.

Previously AI-generated material in the deal folder (one-pagers, summaries)
is read with a lower weight than the source it summarises.

## 2. Write the brief

`workspace/<slug>/brief.md`, in this shape. Keep every line short; the brief
is read by five subagents and is not the place for narrative.

```markdown
# <Company name>

## Deal at a glance
| | |
|---|---|
| Company | legal name, HQ, incorporation date, headcount, stage |
| Product | what ships today, one line per product, with what is roadmap |
| Buyer and user | who pays, who uses, who holds the veto |
| Geography | HQ, beachhead, claimed reach |
| Ask | amount, valuation, runway, use of funds |
| Team | founders and the people who narrated the deal, with roles and any relationships worth knowing |
| Cap table | as stated, with the source |
| Materials | what was read; what is missing (model, data room, contracts, patent, benchmarks) |

## The problem, in the buyer's words
Two or three sentences. The functional job, who feels the pain, what they do today.

## Category anchor
The category this run is anchored on, and the second category if the company straddles two. This decides the comp set and the TAM.

## Founder claims to test
| # | Claim | Where said | Type |
|---|---|---|---|
| 1 | verbatim or close paraphrase | deck p.4 / call 00:41 | testable / experience / narrative |

Testable claims can be checked against a source. Experience claims rest on the founder's own history and are checked for internal consistency, not by search. Narrative claims ("this is inevitable") are checked by whether anyone independent says the same.

## Conflicts between sources
| Fact | Source A says | Source B says | Used |
|---|---|---|---|

## Scope and depth
Tabs to run, depth (basic or full), anything the analyst asked to skip, and why.

## Analyst answers
Questions asked at intake and the answers, verbatim.
```

## 3. Ask what the materials could not answer

Only after the brief exists. Ask in one round, numbered, each with the
answer you would give if the analyst said "your call". Ask about baseline
facts a market-intelligence run cannot proceed without, and about the
levers that change the whole run. Typical questions, asked only when the
materials leave them open:

```
❓ Q1 - Category anchor: the deck names two markets, memory infrastructure and semantic layers. The comp set and the TAM differ by which one we anchor on. Anchor on memory, on semantic layers, or size the combined problem?
➡️ Combined problem, with the memory layer as the anchor for the comp set, because that is where the patent and the differentiation sit.

❓ Q2 - Geography: the deck says India plus APAC; the call says a Middle East pilot. Which is the beachhead for sizing?
➡️ India, with APAC as the second ring.

❓ Q3 - Scope: run the six default tabs, or also the feature matrix and public sentiment? Depth basic or full?
➡️ Six tabs, basic. Add the feature matrix if the differentiation claim survives the competitor thread.

❓ Q4 - Anything you already know that changes the frame: a prior deal in this sector, a partner view, a customer you have spoken to?
➡️ Nothing assumed.
```

Two or three questions is normal; six is the ceiling. A second round only
when an answer opens a new decision. Write the answers into the brief
before dispatching research. Skip the questions entirely when the
materials answer them; asking what is already written wastes the analyst's
time and trust.

## 4. Scope and depth

The default run is the sense check: Summary, Market size, Trends,
Competitors, Founder claims, Sources. The analyst can add Feature matrix,
Public sentiment, or a bottoms-up cross-check by name, at intake or later on
the same workspace.

Depth is one knob. Basic: each research thread stops when the pattern
stabilises, at about fifteen sources, and the run targets under twenty
minutes. Full: the optional threads run and each thread may go to about
thirty sources. Record the choice in the brief so the composer knows what
was and was not researched.
