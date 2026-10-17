---
name: data-analysis
description: "Answer a business question from a database, warehouse or spreadsheet: SQL, EDA, a decision memo. Use on 'pull the numbers', 'write a query', a dashboard figure that looks wrong, 'why did X move', or when a text-to-SQL agent needs a context layer."
license: MIT
metadata:
  version: "1"
  updated: "2026-10-18"
  harnesses: "claude-code codex opencode"
  source: "research-2026-10/knowledge-and-data-agents.md A4, D4; research-2026-10/applied-ml.md A5; research-2026-10/evals-observability.md D14 (all 17 Oct 2026). Assumptions-log and metric-reconciliation shapes after nimrodfisher/data-analytics-skills (pushed 25 Sep 2026); statistics cautions after anthropics/knowledge-work-plugins data/statistical-analysis (pushed 17 Oct 2026). Shapes only, no text copied."
---

# Data analysis

Accuracy on a data question is a property of the context layer, not the model. The same model on the same schema goes from unusable to shippable as names, join paths, metric definitions and domain rules are written down: one vendor's published walkthrough (2026) moved a 13-question set from 0% to about 50% with names and descriptions, about 75% with metric definitions, and 100% with domain rules and global filters. So the guide file comes before the query, the sanity checks come before the answer, and the assumptions ship with the number.

## Steps

1. **Restate the question** as one sentence with the decision it feeds, the grain, the time window, the metric by its name in the guide file, and the segment. Ask the two or three questions that would most change the answer; no more. Done when the asker agrees with the sentence.
2. **Open or build the guide file** (`analytics/GUIDE.md`, spec below). Done when every table the question needs has a section and every metric it uses has an exact SQL definition. A missing definition is a finding: write it, get it confirmed, then query.
3. **Run the query loop**: plan the joins in words, draft the SQL, `EXPLAIN` or dry-run, execute with a row limit, run the sanity checks (row count against expectation, nulls in key columns, a total against a known metric), then answer with the SQL shown. Refuse a question that needs a relationship the guide does not define, and say which one. Done when the sanity checks pass or the answer says which failed.
4. **Reconcile** against a number someone already trusts (a dashboard tile, last month's report, a finance figure). Use the reconciliation shape below when they disagree. Done when the gap is explained or named as open.
5. **Log every assumption** in the shape below as you go. Done when the log has a row for each choice the asker did not make.
6. **Run the statistics cautions** before any comparison, trend or "significant" is written.
7. **Write the answer**: the number with its unit, window and grain; the SQL; the assumptions log; the decision table when the question is a threshold or a trade-off. Charts go through `tufte-viz`.
8. **Add to the eval set** when the query will be reused or an agent will run it (spec below). Done when the question, the reference SQL and the reference result are saved.

## The guide file

`analytics/GUIDE.md`, loaded into the agent's context or exposed as a resource. Scope one guide to 5 to 10 tables; many small spaces beat one large one.

- One section per table: purpose, grain (one row is one what), primary keys, join paths with the key on each side, columns to avoid and why (deprecated, duplicated, PII, wrong grain).
- One section per metric: the exact SQL, the allowed dimensions, the owner.
- Domain rules: fiscal year, currency and units (lakh against rupees, monthly against annual), test accounts to exclude, global filters, time zone.
- 10 to 30 verified queries: question, SQL, expected shape of the result.
- Forbidden columns and forbidden operations, stated once.

Example from a home-loan platform: `applications` is one row per application, `sanctions` one row per sanction letter; the metric "sanction rate" joins on `application_id`, counts sanctions in the month of the application, and excludes test builders.

## Tools for a text-to-SQL agent

Give the agent `list_tables`, `describe_table`, `sample_rows(n <= 5)`, `run_sql(read_only=True)` and `run_metric(name, dims, filters)`. The metric tool is the governed path; raw SQL is the escape hatch. Writes go through a separate tool with a human gate: the agent proposes the statement, a human confirms, derived tables land in a scratch schema, and every write logs an event row (who, what, when, the statement). A semantic layer pays once several consumers need the same metrics: dbt's MCP server when dbt exists, Cube or Lightdash otherwise.

## Assumptions log

One row per choice the asker did not make. The shape:

`id | assumption | why it was needed | which result it touches | how to verify | status (open, confirmed, wrong)`

Typical rows: the time zone of a timestamp column; whether a cancelled record counts; the dedupe key for repeated leads; which of two "amount" columns is the one in rupees; the date a metric definition changed. Ship the log with the number. A wrong assumption discovered later gets a new row and a corrected result, never a silent edit.

## Metric reconciliation

When two sources give two numbers for one metric:

1. Name both sources and the number each shows, with the date each was read.
2. Write each one's definition: table, grain, filters, time window, time zone, dedupe rule, currency.
3. Compute each side step by step from the raw table, one filter at a time, and record the count after each step.
4. Find the step where the two paths diverge. That step is the explanation.
5. State which number is right for which purpose, and record the bridge (A minus B, itemised) in the guide file so the next person does not redo it.

Done when the bridge sums to the gap.

## Statistics cautions

Before writing a comparison, a trend or the word "significant":

- Multiple comparisons: twenty segments tested at 5% produce one false "finding" by chance. Correct for the number of tests, or call it exploratory.
- Simpson's paradox: a trend in every subgroup can reverse in the aggregate when group sizes differ. Check the split by the obvious confounder (channel, city, ticket size) before reporting the total.
- Survivorship: an analysis of current customers, active loans or completed applications excludes the ones who left. Say what the population is.
- False precision: report to the precision the data supports. A conversion rate on 40 applications is not 17.5%.
- Mean and median together, and the count behind them. One number hides a skewed tail; loan amounts and incomes are always skewed.
- Small counts: under about 30 events in a group, show the count and a range rather than a rate.

## Notebooks and spreadsheets

- marimo notebooks: plain `.py`, so they diff and the agent edits them directly. The notebook runs top to bottom with a fixed seed before it is handed back, or the hand-back says it does not. `marimo check` in CI. Promote a cell to `src/` once it is reused twice. Secrets and raw PII never sit in a cell output.
- Spreadsheets: work in code (openpyxl, pandas or Polars). The model sees aggregates, not cells; thousands of rows pass through a sandbox, never through the prompt.

## The decision table

A number is not an answer; a decision table is. When the question is a threshold or a trade-off:

`at threshold t | flagged or approved per week N | missed M | cost of false positives ₹X | saved ₹Y | weeks of data behind it`

One row per candidate threshold. The asker picks the row. `applied-ml` produces the same table for a model.

## The eval set

For any query an agent will run or a question that recurs: 30 to 50 questions from real asks, each with reference SQL and the reference result. Grade by result equivalence, never SQL string match. Track the refusal rate separately; a refusal is a failure under every grading rule. Re-run on every change to the guide file. Expect the curve from the opening paragraph; when the set stalls, the missing piece is in the guide, not the model.

## Output

- The answer: number, unit, window, grain, the SQL, the assumptions log, and the decision table where one applies.
- The guide-file delta (new tables, metric definitions, domain rules, verified queries) and the eval-set delta.
- The reconciliation bridge when two numbers disagreed.

What takes over: `tufte-viz` for every chart; `applied-ml` when the analysis becomes a model or an effect estimate; `ai-governance` when the data is personal or the answer reaches a customer; `use-case-discovery` when the question turns out to be "should we automate this"; `prove-it-works` before declaring done.
