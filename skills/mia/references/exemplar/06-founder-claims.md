# Founder interview

What was said on the 2026-08-26 intro call and in the deck, checked against public sources. Then the questions for the next call.


## Deal at a glance

| | |
|---|---|
| Company | Northlake Labs Pvt Ltd, Pune. Incorporated 11 Feb 2024. 10 people. Pre-revenue. |
| Products | Keel: local-first AI memory, MIT core on the package index. Ledgerline: governed semantic layer over warehouses, $49-99 per user per month. One patent-applied substrate under both. |
| Ask | $500K at $4M post-money (12.5%). 18-20 months runway. Use: 45% engineering, 25% GTM, 15% compliance, 15% ops. |
| The fund's standard terms | About half the founder's ask at a lower post-money; structure needs reconciling. |
| Team | the founder, CEO (~20 years enterprise data). the chief data scientist, Chief Data Scientist. the advisor, advisor and director, 4%, CTO of another startup, CEO's husband, narrated the technical case. Seeking a technical co-founder. |
| Cap table | Founder-held; advisor 4%; no external investors. INR 1 crore the state grant grant, about half disbursed. the fund's CRM note says 'a bit messy'. |
| Buyer | Head of data or CDO at department level; compliance holds the veto and funds Vault. Users: analysts, business users, agents via the protocol toolbox. |
| Materials | 20-slide deck with speaker notes, 68-minute call transcript, three websites, the package index page, MCA filing. Missing: financial model, data room, contracts, patent filing, benchmark artefact. Ledgerline never demoed. |

## What the founder said, checked

> ✔ verified in an independent source. ◐ partly true or hedged. ✘ contradicted. ? no evidence either way.
| # | Founder said | Where | Status | What we found |
|---|---|---|---|---|
| 1 | 'About 16,000 downloads' of the open-source core | [Call](https://sources.example/022) | Contradicted | the package index on 2026-09-03: 168 downloads last month, 10 last week, one release (v0.7.0, 2026-07-17). Two orders of magnitude apart. The only quantified demand signal. |
| 2 | a large telco is 'likely to be our first customer commercially, possibly, if it works out' | [Call](https://sources.example/022) | Unverified | No contract, LOI or pilot claimed. A conversation, triple-hedged in one sentence. |
| 3 | a state government has promised to be the first customer | [Call](https://sources.example/022) | Partly | The INR 1 crore grant is verifiable (1 of 33 the state grant winners, ~50% disbursed). The customer promise is verbal and milestone-contingent. |
| 4 | a storage incumbent is 'very interested' and wanted exclusivity | [Call](https://sources.example/022) | Unverified | Offered an accelerator seat with a resale exclusivity, declined. By the founder's own account a storage incumbent is also building the same thing in-house. |
| 5 | Pilots with a a central-government department and an incubator; design partners across six sectors | [Deck, call](https://sources.example/023) | Partly | Department unnamed. two incubators used interchangeably and never expanded. Three anonymised testimonials on semalayer.com. No count, names or contract status. |
| 6 | TAM $23B by 2030; SAM $6.4B APAC; $18M ARR from 250 accounts at $72K | [Deck](https://sources.example/023) | Partly | Rebuilt on the Market size tab: $18.4B in 2030 (range $13-27B). The founder's figure counts all of governance, none of retrieval, deducts no overlap. The $72K ACV has no derivation and implies 60-120 seats at list. |
| 7 | 'Cloud-native memory vendors cannot retrofit local-first sovereignty; we started there' | [Deck](https://sources.example/023) | Contradicted | Recallio shipped Recallio Local (local-first, protocol-served, audited) in May 2025. Membase sells self-hosted and air-gapped tiers. Quillgraph raised $7.5M in Feb 2026 to build an offline edge engine. |
| 8 | Three-signal fusion (semantic, temporal, relational); an internal recall metric = 0.958 | [the package index, call](https://sources.example/024) | Partly | The relational signal ships at fusion weight 0, 'not yet net-positive'. The headline number is two-signal and on an internal eval set. Not comparable to any published benchmark. |
| 9 | 'Beats every other' memory layer; the public benchmark comparison against Recallio planned | [Call](https://sources.example/022) | Unverified | The comparison has not been run. Recallio, Membase and Tessera publish scores; Northlake publishes none. |
| 10 | Patent applied on the substrate | [Deck](https://sources.example/023) | Unverified | No jurisdiction, date, number or claims. The reference implementation is MIT on the package index. Components are commodity; prior art in Sable, Lantern and Fennel. |
| 11 | 18-month window before Warehouse B, Warehouse A and Vantage move into the semantic layer | [Deck](https://sources.example/023) | Contradicted | Warehouse A assistant and Warehouse B assistant already ship. Prism, Meridian (Series E, Dec 2025) and Loom already occupy the position and are not named. |
| 12 | Data-protection-driven data residency makes buying from an Indian vendor a requirement | [Deck](https://sources.example/023) | Contradicted | The notified Rules impose audit-trail and consent duties, no general residency mandate. Localisation needs a future the IT ministry notification. Cairn is Indian-founded and never sold that. |
| 13 | Ledgerline: 40+ connectors, eleven live modules, security attestation / health-data attestation / the regional privacy law evidence packs | [semalayer.com](https://sources.example/025) | Partly | Modules and connector list are on the site (company's own count). Ledgerline generates security attestation evidence packs; the company does not hold the standard security attestation. Two Business-tier headline features are marked V2. |
| 14 | Keel agent-protocol server 'going live next week'; ingests images and video | [Call](https://sources.example/022) | Unverified | Site listed the agent-protocol server as 'coming soon'. Image and video ingestion appears on neither site; documents, mail and calendar do. |
| 15 | Vault (PII redaction, egress audit) is the enterprise upsell | [Deck](https://sources.example/023) | Partly | Named as a funded 6-8 month milestone. It carries the enterprise price point and does not exist. |
| 16 | Everything is owned by the founder; advisor owns 4% | [Call](https://sources.example/022) | Verified | Consistent with the MCA filing (two directors). Reconcile against the fund's 'messy' note. |


## Next call: questions in priority order

| # | Question | Why | What a good answer looks like |
|---|---|---|---|
| 1 | What does the patent claim? Jurisdiction, filing date, application number. | Moat cannot be assessed without the claim set. Prior art exists for the assembly. | A narrow, specific claim on content-addressed fusion or attribution, with the number. 'It's filed' is not an answer. |
| 2 | 16,000 downloads versus the package index's 168 a month: what is being counted? | Only quantified demand signal; two orders of magnitude apart. | A named source (the code host clones, a mirror, a pre-release artefact) that can be checked. |
| 3 | How does a $72K blended ACV arise from a $49-99 seat list? | The $18M ARR plan rests on it. | A platform-licence price, or an honest revision toward 25-60 seats at list. |
| 4 | Which product is the company? Ledgerline has the price list and the budget line; Keel has the patent and the pitch. | The TAM, the comp set and the hiring plan differ by answer. | A sequencing: Ledgerline funds the runway, Keel is the option, with a date for deciding. |
| 5 | a large telco, a storage incumbent, a state government: contract, LOI, pilot or conversation? | Every named logo is hedged. | One document, or a plain 'conversations'. |
| 6 | Why do you think Recallio sunset Recallio Local? | Consolidation and no-demand readings have opposite implications for the wedge. | Evidence of demand for a standalone local memory product from someone other than the founder. |
| 7 | Dated milestones for Vault GA and the standard security attestation. | Both carry the enterprise price point; neither exists. | Months, owners, and what the INR 1 crore second tranche depends on. |
| 8 | When will the the public benchmark comparison run, and will you publish it either way? | Cheapest headwind to remove; unbenchmarked reads as evasive. | A date within the quarter and a commitment to publish. |
| 9 | Why does the comp set omit Tessera, Halcyon, Quillgraph, Prism, Meridian and Loom? | The named set is consumption surfaces and hyperscalers. | Awareness of the open-core peers and a specific reason Keel wins against Tessera. |
| 10 | Who is the technical co-founder, and when? | The technical narrator is a part-time advisor with another CTO role. | A name, or a search with a deadline. |

