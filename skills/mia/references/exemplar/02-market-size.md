# Market size

One problem-anchored TAM, not a TAM per product. The segments Northlake sells into are combined, overlaps are subtracted, then geography and buyer filters bring it down to SAM and SOM. All figures USD.


## The problem being sized

Giving AI models and agents governed, provable access to what an organisation already knows. Three budget lines pay for that today: the semantic layer (business meaning over warehouses, Ledgerline's market), the access, policy and audit slice of data governance (Ledgerline's compliance features), and retrieval and context infrastructure (what Keel replaces). Memory APIs as a standalone line barely exist yet: about $6M of global spend in 2026, which is why they are a slice of the third line rather than a fourth.


## TAM, SAM, SOM

> Confidence: amber = low. Every assumption names what would move it.
| Step | Line | 2026 | 2030 (projected) | Basis and what moves it |
|---|---|---|---|---|
| **TAM: global spend on the problem** |  |  |  |  |
| A | Ledgerlinentic layer and metrics platforms | $3.34B | $7.73B | Research house A, $2.71B in 2025 at 23.3%, verified at the publisher. Exact fit for Ledgerline. |
| B | Data governance, addressable slice (40%) | $2.54B | $6.07B | Research house B, $5.09B in 2025 at 24.5%, via the deck. Only policy, access control and audit evidence are addressable; catalog, lineage and quality are not. A 30-50% slice gives $1.9-3.2B in 2026. |
| C | Retrieval and context infrastructure | $3.30B | $7.80B | RAG tooling ($2.69B) plus vector databases ($3.38B), less 25% for bundled platforms. Range $2.0-4.55B. Includes the ~$6M memory-API line. |
|  | Less: A overlaps B | -$0.84B | -$1.93B | Vantage, Cairn and Warehouse A sell into both. 25% of A. |
|  | Less: A overlaps C | -$0.54B | -$1.29B | Ledgerlinentic layer plus knowledge graph for agents (Research house C, $1.07B in 2026) sits in both. Half counted here. |
| TAM | Total addressable, global | $7.8B | $18.4B | Range $5.6-10.1B in 2026 and $13-27B in 2030. Implied growth ~24% a year. The founder's $23B for 2030 sits inside the range: it counts all of governance, none of retrieval, and deducts no overlap. |
| **SAM: the part Northlake can serve** |  |  |  |  |
|  | Asia-Pacific share (25%) | $1.95B | $4.59B | APAC is 24.8% of the vector-database market (Research house A) and ~28% of the semantic-web market (deck). Beachhead is India plus APAC. |
|  | Buyers for whom provenance or sovereignty decides the purchase (25%) |  |  | Regulated banking, healthcare and government plus data teams that need audit evidence. Cut from 35% because the data-protection rules require audit trails, not residency. A the IT ministry localisation notification pushes it back above 35%. |
| SAM | Serviceable, APAC | $488M | $1.15B |  |
| **SOM: what is realistically obtainable** |  |  |  |  |
|  | India share of APAC (15%) | $73M | $172M | All distribution assets are domestic: the the home state grant channel, a a central-government pilot, no sales presence elsewhere in APAC. This is the India pool, not a forecast. |
| SOM | Obtainable in three years at published prices | $0.2-2.9M |  | 12-40 accounts x 25-60 seats x $588-1,188 per seat per year (Ledgerline list). That is 0.2-3.9% of the India pool. Only Ledgerline has a price; Keel's core is free and Vault is unpriced. |


## Sanity checks

- What buyers pay today for a standalone AI memory layer is about $6M globally (Recallio's 62M monthly API calls at its published $0.00045 per request, scaled and divided by a 40-60% cohort share; an analyst house's under-1% penetration for Context Graphs agrees). The memory slice of this TAM is demand to be created. Ledgerline's slice has a budget line, a buyer and a price.
- The TAM without line C (retrieval infrastructure) is $5.0B in 2026 and $11.9B in 2030. Use that if you read retrieval as substrate Northlake builds on rather than budget it competes for.
- Weakest links, in order: the 40% governance slice, the 25% provenance filter, the 25% overlap haircuts. Together they move the 2026 SOM pool between $45M and $110M.
- Not used anywhere: the 16,000-downloads claim, the $72K blended ACV (implies 60-120 seats per account at list), the three hedged logos, the patent application.

## Growth: what drives the 24% and what caps it

| Driver |  | Points | Evidence |
|---|---|---|---|
|  | Agent deployment volume | +15.0 | an analyst house: agentic AI in 33% of enterprise apps by 2028 from under 1% in 2024; 40% of agentic projects cancelled by 2027 already netted out. |
|  | Context intensity per workload | +5.5 | Retrieval tooling compounds 10.9 points faster than the vector storage beneath it. |
|  | Regulatory provenance (data-protection, the regional AI act) | +4.0 | Audit-trail duties from 13 May 2027 in India; EU high-risk deadline moved to Dec 2027. Lifts the category more than Northlake. |
|  | Asia-Pacific mix | +4.0 | APAC grows 2.7-4.6 points faster than global across two research houses. |
|  | On-device inference | +3.0 | a second analyst house: NPU laptops near 60% of shipments by 2027. Keel needs neither NPU nor GPU. |
|  | Platform absorption (counter) | -7.5 | Vendor A, Vendor B and Chainworks ship memory free; Recallio sunset Recallio Local. The pool grows, the standalone line does not. |


```chart
title: From TAM to the India pool, 2026, $M
highlight: 3
TAM global | 7805.55
APAC (25%) | 1951.39
SAM: provenance buyers (25%) | 487.85
SOM pool: India (15%) | 73.18
```
