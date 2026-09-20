# Competitors: what buyers pay for today

Organised by the purchase a buyer actually makes when they want AI over what the organisation knows. Groups ordered from most to least common. Company names link to the funding source.


## Seven ways the problem gets bought

| What the buyer does | Who and what | What they pay | Evidence of spend | So what for Northlake |
|---|---|---|---|---|
| Nothing, or build it in-house | Re-paste context; DIY RAG on an OSS vector database, a third OSS vector database or a a relational database extension; Markdown files and Obsidian; or ban cloud AI outright. | $0 licence; engineering time | The majority. the fund itself runs self-hosted Quarry and a partner's Obsidian graph. Recallio's own marketing targets this behaviour. | The incumbent to beat. No buyer has yet paid to leave it for Northlake. |
| AI inside the warehouse they already pay for | the two warehouse-native assistants, and platform memory from Vendor A, Vendor B, Chainworks. | Bundled into an existing contract; Vendor B file search $0.10 per GB per day | No separate procurement, so no separate revenue to measure. Vendor A memory's launch drew ~70x Recallio Local's engagement. | The bundling threat to both products. Sets the price floor near zero. |
| Enterprise search and knowledge assistants | Findwell, Quarry, Waypoint. 'AI over our company knowledge.' | Findwell $45-65 per user per month with $50-60K minimums; Quarry and Waypoint $20 | Findwell ~$300M ARR by May 2026, up 89%. The only revenue figure in the landscape. Quarry reports three named enterprise logos. | Where the money actually goes today. Adjacent job, same budget owner. A comp for Ledgerline, not Keel. |
| Ledgerlinentic layer and conversational BI | Loom Ledgerlinentic Layer, Prism, Meridian, Clarity. | Clarity $25-50 per user; Prism $40-80 per developer; Loom per queried metric | $1.26B raised across four companies; Meridian took a Series E in Dec 2025. Established budget line. | Ledgerline's real competitors, and the deck names none of them. Ledgerline's edge here is the signed evidence pack, not natural-language querying. |
| Governance and catalog | Vantage, Cairn (India-founded). | Enterprise contracts, unpublished | $802M raised. Compliance-driven purchases with audit relationships in place. | Serves the governance slice of the TAM already. Cairn proves 'Indian vendor' is a feature, not a moat. |
| Retrieval infrastructure | Coralbase, three OSS vector databases, an embedded OSS store. | Usage-based; Coralbase ~4,000 paying customers | $273M raised; Coralbase has had no priced round since 2023. BYOC, health-data attestation and edge features arriving in 2026. | The layer Keel is built on (an embedded OSS store). Sovereignty features are being commoditised into storage. |
| Standalone memory APIs | Recallio, Membase, Tessera, Halcyon, Quillgraph, Persona Labs; free: Recallio Local (sunset), Fennel, Lantern, Sable. | Recallio $19-249 a month; Membase $19-399; Tessera $125-375; free tiers everywhere | About $6M of global spend in 2026. Six funded companies, $52M raised, none past Series A. No ARR disclosed by any. | Keel's category. Capital-light (Tessera reached the standard security attestation on $0.5M) but distribution-heavy: Tessera's engine 27K stars vs Keel 168 downloads a month. |


## Where capital has gone

> Total raised by group, $M. Capital follows budget lines that exist; the memory layer has the least. Chart at right.

## Companies

| # | Grp | Company | What the buyer pays; traction | Raised $M | Stage, last round, lead | Why it matters |
|---|---|---|---|---|---|---|
| **Group 7: standalone memory APIs (Keel's category)** |  |  |  |  |  |  |
| 1 | 7.0 | [Recallio](https://sources.example/001) | $0 / $19 / $249 / custom. ~62.5K stars on the code host, 186M API calls a quarter, no ARR. | 24.0 | Series A, 2025-10, a US seed fund | The benchmark Northlake named but has not run. Built and retired Recallio Local, a local-first agent-protocol memory server: Northlake's product, withdrawn by the biggest funnel. |
| 2 | 7.0 | [Membase](https://sources.example/002) | $0 / $19 / $100 / $399 self-hosted / air-gapped Enterprise. Self-published the public benchmark #1. | 3.0 | Seed, 2025-10, a US seed fund | 'Same thing on cloud' per the founder. Now sells self-hosted and air-gapped, clearing the residency gate from a better-distributed position. |
| 3 | 7.0 | [Tessera](https://sources.example/003) | $125 / $375 / custom. Tessera's engine ~27K stars; the standard security attestation, health-data attestation; large-enterprise logos. | 0.5 | Seed, 2024-04, an accelerator | Closest architectural analogue. Its relational and temporal signal is live; Keel's ships at weight 0. Proves $0.5M is survivable when open source does the distribution. |
| 4 | 7.0 | [Halcyon](https://sources.example/004) | Free BYOK, $20 Pro. Halcyon's paper 13K+ stars. $70M post-money at seed. | 10.0 | Seed, 2024-09, a US VC | Research-credibility comp: peer-reviewed paper, PhD team, $70M post with zero revenue. Northlake offers an unseen patent instead. |
| 5 | 7.0 | [Quillgraph](https://sources.example/005) | OSS core; managed cloud in build. Berlin, ~24 staff. | 9.1 | Seed $7.5M, 2026-02, a US seed fund | Most direct threat: raised specifically to build a a systems language edge engine for offline, private memory, the differentiation Northlake calls unretrofittable. |
| 6 | 7.0 | [Persona Labs](https://sources.example/006) | OSS library, hosted agent-protocol server, Vendor A's coding agent plugin. Three a top ML conference papers. | 5.95 | Seed, 2025-04, a US seed fund | Same 'memory belongs to you' framing, US-distributed, research-backed. |
| 7 | 7.0 | [Free: Recallio Local, Fennel, Lantern, Sable](https://sources.example/007) | Free. Fennel: 19-tool offline agent-protocol server, audit log, verified deletion, 9 stars. Lantern 36.6K stars with an on-prem tier. Sable: same an embedded OSS store + a local model runtime stack, archived. |  | Unfunded | Fennel matches most of Keel's shipped surface with no company behind it. Sable shows the stack is standard, not proprietary. Lantern caps what OSS pull alone is worth. |
| **Group 2: platform-native and warehouse-native (bundled, free)** |  |  |  |  |  |  |
| 8 |  | [Vendor A: memory tool and stores](https://sources.example/008) | No separate charge. Memory tool GA on Vendor A's model 4+; the agent protocol 400M+ SDK downloads a month. |  | n/a | Client-side storage the developer controls: the 'your memory, rented back' problem answered free, in the customer's infrastructure. Most under-priced threat in the deck. |
| 9 |  | [Vendor B: API state and file search](https://sources.example/009) | $0.10 per GB per day, $2.50 per 1K calls; remote the agent protocol free. |  | n/a | The price floor a buyer compares Ledgerline's $49-99 and Vault's unpriced tier against. |
| 10 |  | [Chainworks framework memory](https://sources.example/010) | Free inside Chainworks. Chainworks ~118K stars, $1.25B valuation. | 125.0 | Series B, 2025-10, a growth investor | A Chainworks developer gets memory free and never evaluates a standalone vendor. Removes the developer-pull funnel the near-zero-CAC thesis needs. |
| 11 |  | the two warehouse-native assistants | Bundled in the warehouse contract. |  | Public | Ledgerline's bundling threat. The deck says they will move; they have moved. Not independently researched this pass. |
| **Group 3: enterprise search (where the budget goes today)** |  |  |  |  |  |  |
| 12 |  | [Findwell](https://sources.example/011) | $45-65 per user per month, $50-60K minimums (third-party). ~$300M ARR, $7.2B valuation. | 765.0 | Series F, 2025-06, a growth investor | The buyer's default for 'AI over our company knowledge'. Consumption surface, not substrate, but it will be in the room. |
| 13 |  | [Quarry](https://sources.example/012) | MIT core; cloud $20 per user. ~31K stars; three named enterprise logos reported. | 10.0 | Seed, 2025-03, two US VCs | The live substitute inside the fund: self-hosted on GCP with Vendor C's model. A paying-customer-shaped buyer solved this for $0 of licence. |
| 14 |  | [Waypoint](https://sources.example/013) | $20 per user. ~70 employees across three products. | 27.0 | Series A, date unknown | Benchmarked by the fund, found slower than Quarry. Single tier-3 source. |
| **Group 4: semantic layer and conversational BI (Ledgerline's competitors)** |  |  |  |  |  |  |
| 15 |  | [Prism](https://sources.example/014) | Free tier; $40-80 per developer; custom. ~52 staff, Prism.js widely deployed. | 48.0 | Series B, 2024-06 | The most direct Ledgerline comp and the deck omits it entirely. |
| 16 |  | [Meridian](https://sources.example/015) | Consumption on semantic objects. ~154 staff. | 120.0 | Series E, 2025-12 | Fresh Series E: the category is being recapitalised, not consolidated. |
| 17 |  | [Loom](https://sources.example/016) | Per queried metric inside Loom Cloud. ~1,173 staff, $4.2B valuation. | 415.9 | Series D, 2022-02, a growth investor | Owns where metrics are authored. Ledgerline must import Loom models or ask customers to define metrics twice. No source answers which. |
| 18 |  | [Clarity](https://sources.example/017) | $25-50 per user; Spotter capped at 25 queries a month on Pro. ~1,749 staff. | 674.0 | Series F, 2021-11 | 'Plain English in, chart out' is a 14-year-old category. Ledgerline's novel part is the signed evidence pack. |
| **Group 5: governance and catalog** |  |  |  |  |  |  |
| 19 |  | [Vantage](https://sources.example/018) | Enterprise contracts. ~1,116 staff, $5.25B valuation (2021). | 596.3 | Series G, 2021-11 | One of three names the 18-month window rests on. No priced round since 2021; a bolt-on acquisition arrives faster than organic entry and prices Northlake as an acqui-hire. |
| 20 |  | [Cairn](https://sources.example/019) | Enterprise contracts. ~544 staff, $750M valuation. India-founded. | 206.0 | Series C, 2024-05, a sovereign fund | The governance slice is already served by an Indian-founded company that never sold 'Indian' as the pitch. |
| **Group 6: retrieval infrastructure (what Keel is built on)** |  |  |  |  |  |  |
| 21 |  | [Coralbase](https://sources.example/020) | Usage-based. ~4,000 paying customers; BYOC and health-data attestation shipped 2026. | 138.0 | Series B, 2023-04, a growth investor | No priced round since 2023 while the AI boom ran: value is migrating up-stack. Good for the category, neutral for this vendor. |
| 22 |  | [three OSS vector databases](https://sources.example/021) | OSS cores with managed tiers. an OSS vector database ~29K stars and an embedded OSS vector engine; another OSS vector database 2,000+ production companies. | 50 / 67 / 18 | B / B-C / Seed | an embedded OSS vector engine collides with the on-device story: embedded, local retrieval as a free primitive. Funding figures from tier-3 blogs. |
| 23 |  | an embedded OSS store | OSS embedded vector store. Keel's own on-disk store, and Sable's. |  | Not researched | On-device retrieval is bought, not built. The claimed novelty must sit in the fusion and content-addressing above it. |


## Claimed white space, and who is already in it

| Claim | Occupied from | By | Read |
|---|---|---|---|
| Local-first, sovereign, cited memory | Above | Recallio's Recallio Local: local dashboard, per-client revoke, audit logs, the agent protocol. Shipped May 2025, now sunset. | Falsifies 'cloud vendors cannot retrofit local-first'. |
|  | Below | Fennel, Sable, Lantern: the shipped surface, free. | The feature surface is not scarce. |
|  | Side | Quillgraph's $7.5M edge engine; Membase air-gapped; an embedded OSS vector engine. | The window the thesis needs is largely closed. |
| What remains |  | Content-addressed deterministic citations (Keel); full offline inference with cite-or-abstain on GPU-free hardware (Keel); cryptographically signed evidence packs with plan-time RBAC (Ledgerline). | Real, months not weeks to copy, not structurally protected. The sharpest one is on Ledgerline. |


## Founder's reference set, checked

| | |
|---|---|
| Genuine memory comps (2 of 8) | Membase, Recallio. |
| Enterprise search (3 of 8) | Findwell, Waypoint, Quarry. Adjacent budget, different job. |
| Ledgerlinentic-layer incumbents, Ledgerline only (3 of 8) | Warehouse B, Warehouse A, Vantage. |
| Missing entirely | Tessera, Halcyon, Quillgraph, Persona Labs, Chainworks memory, Prism, Meridian, Loom, and all platform-native memory: the companies running the same open-core playbook in both categories. |

## Could not be determined from desk research

- Revenue for any private memory comp. Findwell's ~$300M is the only ARR figure and it is tier-3 sourced.
- Whether any memory pure-play has enterprise contracts in India or APAC.
- What the patent claims. With commodity components and prior art in Sable, Lantern and Fennel, the moat cannot be assessed without the claim set.
- Head-to-head retrieval quality: the the public benchmark comparison is unrun.
- Why Recallio sunset Recallio Local. Consolidation and no-demand readings have opposite implications.

```chart
title: Capital raised by what buyers spend on, $M
highlight: 5
Ledgerlinentic layer and BI (4 cos) | 1257.9
Enterprise search (3 cos) | 802.0
Governance and catalog (2 cos) | 802.3
Retrieval infrastructure (4 cos) | 273.0
Agent framework (Chainworks) | 125.0
Standalone memory APIs (6 cos) | 52.55
```

```chart
title: Memory pure-plays, raised $M (none past Series A)
Recallio | 24.0
Halcyon | 10.0
Quillgraph | 9.1
Persona Labs | 5.95
Membase | 3.0
Tessera | 0.5
```
