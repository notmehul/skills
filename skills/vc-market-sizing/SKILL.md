---
name: vc-market-sizing
description: "VC-grade market sizing for a startup or company: define the market, compute TAM/SAM/SOM with bottom-up, top-down, and value-based methods, triangulate results, and write an investor-ready market sizing section with explicit assumptions and citations. Use for: 'size the market for X', 'TAM/SAM/SOM', 'market sizing', 'investment memo market', 'pitch deck market size', or when evaluating if an opportunity is venture-scale."
---

# VC Market Sizing

Produce a defensible, investor-grade market sizing (TAM/SAM/SOM) for a startup/company, with explicit assumptions, citations, and at least two independent estimation methods.

## Output Standard

Always produce:

1. A one-page market sizing section (numbers + narrative)
2. A table of assumptions (each with a source link or explicit "assumption")
3. A sensitivity view (at minimum: low/base/high)

## Intake (Ask First)

Capture these inputs before doing math:

- Company: what is sold, to whom (buyer), and the wedge vs the full product vision
- Business model: SaaS, usage, take-rate, payments, ads, services, hardware, etc.
- Geography: initial + expansion; currencies
- ICP: customer type, size band, and who approves budget
- Pricing metric: per seat, per location, per transaction, per $ volume, per API call, etc.
- Time horizon: "today" vs 5-10 year expanded definition
- Constraints: distribution channel, regulation, deployment friction, switching costs

If any are unknown, proceed with a reasonable default but label it as an assumption and add a sensitivity range.

## Workflow

### 1) Define the Market Precisely

Define the market in the same units your business model captures (this prevents nonsense TAMs).

- Buyer and budget: who pays, from what budget line
- Unit of analysis: org, location, seat, asset, transaction, etc.
- Scope boundaries: what is included/excluded
- Time basis: annual recurring revenue vs spend vs GMV vs units shipped

Write the definition in one sentence and reuse it consistently.

### 2) Build 2-3 Independent Models

Do not rely on a single analyst report number. Triangulate.

#### A) Bottom-up (Preferred for early-stage)

Compute from "count of units" x "revenue per unit".

Examples:

- Seat-based SaaS: (# target employees) x (penetration) x (price per seat)
- Location-based SaaS: (# locations) x (penetration) x (annual contract)
- Payments: (payment volume) x (take rate)
- Marketplace: (GMV) x (take rate)
- Usage-based: (events/API calls) x (price per event)

Where to get counts and benchmarks: see `references/source-hierarchy.md` and `references/industry-insights.md`.

#### B) Top-down (Use to sanity check)

Start with a credible "total spend" or "industry revenue" and apply filters:

- Geography filter
- Segment filter (vertical, customer size, product category)
- Category capture filter (what portion is realistically addressable)

Explicitly note the definition mismatch risk (most reports define markets differently than your wedge).

#### C) Value-based (When your product changes the cost curve)

Anchor on value created:

TAM ~= (# units) x (value per unit per year) x (realistic capture rate)

Use this to justify expansion to adjacent budgets or new workflows.

### 3) Convert to TAM / SAM / SOM

- TAM: maximum revenue in the defined market if you were the only supplier
- SAM: portion of TAM you can serve given product scope + geo + ICP constraints
- SOM: portion of SAM you can obtain in a concrete horizon given distribution and competition

SOM must be grounded in a go-to-market constraint (sales capacity, channel throughput, procurement cycles), not vibes.

### 4) Triangulate + Reconcile

If model A and B disagree materially:

- Check unit/definition mismatch (spend vs revenue vs GMV)
- Check double-counting (multiple layers of the value chain)
- Check geography/year mismatch
- Check who pays (buyer) vs who benefits

Pick a base case and keep low/high cases that reflect the uncertainty.

### 5) Add Industry Insights (So the Number Has a Story)

Include 5-10 bullets of "why this market exists and moves":

- spend drivers and constraints (regulation, labor, budgets, cycles)
- buyer incentives and procurement friction
- market structure (fragmented vs concentrated), incumbents, switching costs
- tech inflection points (e.g., AI enabling new workflows)
- distribution: how products are actually purchased in this category

Use primary sources where possible (filings, government stats, regulator publications). See `references/industry-insights.md`.

### 6) Write the Memo-Ready Section

Use `references/memo-template.md` (or copy from `assets/market_sizing_memo_template.md`).

## Common Pitfalls (Avoid)

- "Gartner says..." as the entire argument (no math, no definitions)
- Confusing TAM with SOM (or claiming venture-scale SOM without GTM constraints)
- Mixing spend/GMV/revenue without explaining conversion
- Ignoring who pays (budget owner) vs who uses
- Hiding key assumptions; no sensitivity

## Bundled Resources

- `references/source-hierarchy.md`: source prioritization + where to find credible inputs
- `references/industry-insights.md`: what to look for and where to find it
- `references/business-model-formulas.md`: formulas by business model + gotchas
- `references/assumptions-register.md`: assumptions table template
- `references/memo-template.md`: market sizing memo template
- `references/further-reading.md`: curated links for frameworks and data sources
- `scripts/market_size.py`: quick math + sensitivity table generator
- `assets/market_sizing_memo_template.md`: copy/paste template
