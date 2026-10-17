---
name: lending-domain
description: "Indian home-loan domain for anyone building models, agents or bots at a lending platform: journey, economics, documents, what works in production. Use on home loan, balance transfer, eligibility, sanction, disbursal, DSA, bank statements or KYC."
license: MIT
metadata:
  version: "1"
  updated: "2026-10-18"
  harnesses: "claude-code codex opencode"
  source: "research-2026-10/india-fintech-lending.md A.3, A.4, C, D.2, D.4, D.5, D.6 (17 Oct 2026; RBI, TRAI, Sahamati, company filings and Indian business press)"
---

# Lending domain: Indian home loans

Public domain knowledge for a builder at a lending service provider (LSP) or distribution partner that sits between borrowers and regulated lenders. Everything time-bound is as of Oct 2026 and says so. Every rate, fee and payout below is a public range for orientation; the lender's own rate card and key facts statement (KFS) are the source for any number a customer sees.

The compliance pre-flight for anything customer-facing (disclosure, consent, telecom, model risk) lives in `ai-governance`; this skill names where it applies and stops there.

Read `references/data-map.md` when designing a schema, a CRM field list or a feature set. Read `references/extraction-fields.md` when building document intake, extraction or cross-checks.

## The journey

| Stage | What happens | Who | Time and economics (public, Oct 2026) |
| :--- | :--- | :--- | :--- |
| Lead | Builder site, DSA or connector, aggregator, bank app, click-to-WhatsApp ad | Builders, DSAs, aggregators, LSPs | No credible public funnel benchmark for home loans exists |
| Intent qualification | Purpose (purchase, BT, top-up, LAP), property status (APF, under construction, resale, self-construction), employment type, income, co-applicant, city, timeline | Telecallers, DSAs, bots | Minutes |
| Eligibility, in-principle | FOIR (EMI to net monthly income) 20 to 70% by income slab, bank-specific; LTV caps per RBI: up to 90% to ₹30 lakh, 80% for ₹30 to 75 lakh, 75% above ₹75 lakh; stamp duty excluded from cost except homes up to ₹10 lakh; bureau pull | Lender engines | Minutes for in-principle; 3 to 7 days for formal sanction at a PSU bank after full documents |
| Documentation and KYC | Aadhaar OTP e-KYC, video KYC, CKYC fetch; PAN; income proofs; bank statements by PDF or Account Aggregator (AA); property papers | Lender, LSP, data vendors | AA fulfilment rates 65 to 70%, up from 35 to 40% (industry report, Jan 2026) |
| Credit assessment | Income normalisation, obligations, bureau, FOIR, fraud checks, personal discussion for the self-employed | Credit managers, increasingly agent-assisted | Salaried faster; self-employed 7 to 10 days |
| Sanction | Sanction letter plus KFS: APR, every charge, recovery-agent policy, prepayment terms | Lender | 7 to 15 working days typical |
| Legal and technical | Title search (13 to 30 years for resale), valuation, plan compliance; largely skipped for APF projects | Empanelled advocates and valuers | The slowest phase; APF is what makes under-construction fast |
| Disbursal | Full or stage-wise to the builder; no upfront disbursal to a builder on an under-construction project | Lender | Up to 30 days end to end |
| Servicing | Statements, EMI changes on repo resets, part-prepayment, interest certificates, re-KYC | Lender | |
| BT, top-up, LAP | Penalty-free on floating individual loans sanctioned from 1 Jan 2026 | Everyone; heavy DSA activity | Housing-finance yields around 9.0% on individual home loans, 10.1% non-housing (a large HFC, Mar 2026) |
| Collections | Pre-due reminders, early-bucket bots, field, legal | Lender and agencies | Not an LSP activity unless contracted |

APF, approved project finance: lenders pre-clear a builder's project legally and technically, so each buyer's loan needs only borrower underwriting.

Payouts, public grids: home loans about 0.25 to 0.35% at PSU banks (bank DSA policies, 2024 to 2026, often capped at ₹1 to 1.25 lakh per case) and 0.40 to 1.0% at private banks and HFCs (a published slab book, Apr 2024); LAP 0.7 to 1.5%; unsecured 1.5 to 4%. Paid on disbursal, with clawback when the loan goes 30+ days past due or is transferred out within 6 to 12 months; processing-fee shortfalls can be netted against payout. Re-check before quoting.

## Two dates that change the arithmetic

- **7 Oct 2026**: the repo rate rose 25 bp to 5.50%, the first hike since Feb 2023, stance "calibrated tightening", after 125 bp of cuts in 2025 had taken entry home-loan rates to about 7.5%. Repo-linked EMIs reset upward within weeks. "Will my EMI go up" is the dominant inbound intent this quarter, and every "should I switch" script written in 2025 is wrong-signed.
- **1 Jan 2026**: RBI's prepayment directions (issued 2 Jul 2025) remove prepayment and foreclosure charges on floating-rate loans to individuals for non-business purposes, from any source of funds, with no lock-in, for loans sanctioned or renewed on or after that date. Loans sanctioned earlier may still carry charges by contract. Remaining switching costs: processing fee about 0.25 to 0.50% plus GST, legal and valuation, and state-specific MODT and stamp duty.

## Eligibility arithmetic

Numbers that affect money come from code over a versioned rate card; the model explains them.

```
net_monthly_income  = normalised income (salary credits, ITR, GST turnover rule), per lender
foir_cap            = lender slab for that income band (20 to 70%)
emi_capacity        = net_monthly_income x foir_cap - existing_emis
loan_by_income      = PV(emi_capacity, lender rate for bureau band, tenor to retirement age)
property_cost       = agreement value (+ stamp duty only when cost <= ₹10 lakh)
ltv_cap             = 90% (<= ₹30 lakh) | 80% (₹30 to 75 lakh) | 75% (> ₹75 lakh)
loan_by_property    = min(agreement value, valuation) x ltv_cap
in_principle        = min(loan_by_income, loan_by_property), per lender, with EMI and APR from that lender's KFS
```

Output per lender: in-principle amount, EMI at today's rate, APR per KFS, "subject to lender approval and property checks" stated once.

## What is in production in India

Pattern names and public numbers, 2025 to 2026. Vendor case studies are marked.

- **Document auto-QC and extraction.** A large NBFC runs auto-QC on 41% of files (target 85 to 90%) and extracts 43 document types at about 95 to 96% field accuracy (FY26 investor calls). A listed digital lender's "smart documents" for LAP reports +30% first-time-right and about half the document-stage credit queries (investor presentation, 2026).
- **Call-to-data.** The same large NBFC converted 52 million calls to text and 2.3 million to structured data, and mined offers for 5.2 lakh customers whose only data came from calls. Structured dispositions are the asset that makes every later model possible.
- **Agent-assist underwriting.** An NBFC reports credit-manager efficiency up 35 to 40% with AI-assisted tools; a large private bank runs a bureau-report summariser (20 pages to an analyst summary), document intelligence and financial-statement analysis with humans in the decision loop.
- **WhatsApp intake.** Native forms (Flows) at 58% completion against 22% on mobile web; sending the document request within 10 minutes of form completion lifted submission 27% (vendor case study, Jun 2026). A pre-approved personal loan closed end to end in WhatsApp in 9 minutes with Hinglish negotiation (vendor case study, Sep 2026).
- **Status and support bots.** A digital lender resolves about 80% of support queries end to end, with resolution time from over 4 hours to under 20 minutes, and an explicit ownership split: data science owns model performance, engineering owns data integrity, business owns outcomes; drift alerts trigger rollback or retrain.
- **Reality checks.** RBI's own study of 5.69 million fintech app reviews (Sep 2025): the top complaint is automated responses with no path to a human. A 2,030-customer survey (May 2026): only 25% rate the experience excellent, 8 to 13% value promotional personalisation, 59% want AI as a coach rather than a salesperson. Contact-centre language mix: 70% Hindi, 23% regional, 7% English (ombudsman report, Dec 2025). Hinglish ran at 30% of conversations in one pilot against a 10% estimate (Jul 2026).

## Where to start

Ranked by value over feasibility for a multi-lender LSP whose pilots are handed to non-technical operators.

1. **Document intake QC and extraction** with a human-visible "what's missing" message sent within 10 minutes. No credit-decision authority, so it sits below the lender's model-risk tiering; every lender in the network benefits; the data exists today.
2. **Telecaller call-to-data.** Transcribe recorded calls (Indic ASR, Hinglish) into a structured disposition: intent, property stage, budget, co-applicant, objections, next action, promised callback time. Post-call first, live later. Recording consent in the opener; recordings stay in India.
3. **WhatsApp intent-and-eligibility concierge** for inbound high-intent users: Flows-based qualification, the eligibility arithmetic above, a plain explanation of each lender offer in the compliant comparison. Third because it is customer-facing: `ai-governance` pre-flight and a human owner first.
4. **Application-status bot** on utility templates, free inside the 24-hour service window. Low risk; status queries dominate complaints.
5. **BT and top-up propensity** on the existing book, only after 1 to 3 have produced six months of clean dispositions and outcomes. After the Oct 2026 hike the near-term signal is "EMI shock" on older or high-spread loans: a rules-plus-model problem. `applied-ml` takes it from there.

Leave alone at an LSP: autonomous credit decisions (the lender's model-risk perimeter); collections bots (not an LSP function unless contracted, and the most penalised conduct area); insurance cross-sell automation (bundling and mis-selling rules); anything that reads SMS, contacts or net-banking (barred under the 2025 digital lending directions and displaced by AA).

Each pilot ships with a one-page runbook, a weekly 10% human sample and a dashboard whose first tile is "exceptions awaiting a human". `pilot-rollout` owns the hand-off.

## Decision rules

- A number that affects money (rate, EMI, fee, eligibility) is computed by code from a versioned source. The model may only explain it.
- A product fact the bot cannot source from the policy or offer store is answered with "I don't know, a person will answer by [time]" and a hand-off.
- A model output that can change a credit outcome is advisory to a named human until the lender's model-risk process approves otherwise. AI output is a proposal until a human confirms.
- A message that could be read as promotional goes out as marketing, with consent, on the marketing channel. When unsure, it is promotional.
- A user who mentions distress, a legal threat, a death, fraud, or asks for a human: the bot stops selling and routes at once.
- A field a credit manager would not need is not collected.
- Sanction date before 1 Jan 2026: do not state that prepayment is free; check the agreement.
- The first two weeks of any model work go to structured dispositions and logged consents. A model on free-text notes is rebuilt within a quarter.
- A pilot has one KPI the system of record can measure inside the pilot window: completed-document rate, first-time-right, hand-off rate. Never NPS, and never "containment and CSAT" together.
- Vendor language claims are tested on your own recordings (telephony-grade, Hinglish, numbers, scheme names) before signature.
- Every action a system takes (a message sent, a document classified, a disposition written, a consent recorded) writes an event row.

## Question lists

For the business owner bringing a use case
- Who is the regulated lender here, and what does our contract let us do with the borrower's data?
- What decision does a human make today, with which fields, and how long does it take?
- What is the one metric that moves if this works, and where is it recorded today?
- Who operates it after the pilot, and what do they do when it misbehaves?
- Which stage of the journey, and which of the data-map objects already exist as clean data?
- Does any output reach the customer? If yes, `ai-governance` applies in full.

For the lender partner
- Which KFS and offer fields can we consume by API, and how often do rate cards change?
- Do you accept AA data for income, for which segments, and on which AAs are you live?
- Is our bot's content subject to your product-approval or model-risk process?
- What are your payout trigger and clawback terms, and how do you want DSA-sourced files flagged?
- Which video-KYC and KYC vendors must we use?

For the data or AI vendor
- Where is the model hosted; what is logged; what is retained; who else sees the data?
- Per-field extraction accuracy on our documents, by document type and language?
- What happens on telephony transfer to a human (SIP, DLT scrubbing stage, latency)?
- How do we switch it off, and how fast?

The compliance owner's questions (consents held, lender approval for content, grievance path in the user's language) belong to `ai-governance`.

## Output

- The use case placed on a journey stage, with who acts, the time it takes today, and the money it touches.
- The data objects it needs, named from `references/data-map.md`, with the quality trap for each checked.
- The decision rules that apply, and the question lists with answers or named unknowns.
- A start-order position: which of the five it is, or why it is on the leave-alone list.

What takes over: `ai-governance` for anything customer-facing or touching personal data; `use-case-discovery` to score it against the rest of the backlog; `knowledge-and-extraction` to build document extraction; `conversation-design` for a chat or voice flow; `applied-ml` for a propensity or risk model; `pilot-rollout` when it goes to operators.
