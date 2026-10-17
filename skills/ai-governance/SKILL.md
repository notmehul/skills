---
name: ai-governance
description: "Governance for an AI system that reaches customers or decides about people: the system card, DPDP, an EU AI Act screen, vendor data terms, and the India finance-bot pre-flight. Use on 'compliance', 'RBI', 'DPDP', 'can we store this', or vendor terms."
license: MIT
metadata:
  version: "1"
  updated: "2026-10-18"
  harnesses: "claude-code codex opencode"
  source: "research-2026-10/business-use-cases.md A5, D6 and research-2026-10/india-fintech-lending.md A.6, D.1, D.5, D.6 (Oct 2026)"
---

# AI governance

The artefact a deployer needs is a one-page system card per deployment. The checklists here fill its rows, and the India finance-bot pre-flight extends it for anything that talks to Indian consumers about a loan, a card or an insurance product. Every date in this skill is as of Oct 2026 and the deadlines move: re-check the gazette or the regulator's page before quoting one. Build for the deadline now; consent logs and six-month event logs are cheap on day one and expensive to retrofit. Two invariants apply to any system that acts: AI output is a proposal until a human confirms it, and every action writes an event row.

## Steps

1. **Classify the deployment.** Answer six questions, yes or no: does a person interact with it; does it generate text, image, audio or video shown to people; does it make or help make a decision about a person; does any user or customer sit in the EU; does it touch Indian personal data; does it talk to Indian consumers about a financial product. Done when all six have an answer and the yeses name which checklists below apply.
2. **Write the system card.** Done when every line has a value or a named unknown with an owner.
3. **Run the DPDP checklist** when any Indian personal data is involved. Done when each line is yes or no with an owner, and every no has a date.
4. **Run the EU AI Act screen** when any user or customer sits in the EU. Same completion rule.
5. **Run the vendor terms checklist** for the tier actually bought, not the tier on the pricing page. Done when the system card's model line links to the evidence for "training use = no".
6. **Run the India finance-bot pre-flight** when the system talks to Indian consumers about a financial product. Read `references/india-finance-bot-preflight.md` and run all five blocks. Read `references/india-regulation-table.md` when a line cites an instrument and you need its in-force or draft status. Done when every line is yes or no with an owner, and every no has a date before go-live.
7. **Ask the compliance owner and the lender partner** the question lists below and record the answers on the card. Done when no answer is "we assume".
8. **Set the review dates.** Done when the card carries a last-review and next-review date, and the open items have owners and dates.

## The system card

```
Name / owner / sponsor / go-live date / autonomy level per action category
Purpose and users; who is affected by its outputs (customers, employees, applicants)
Model(s) and version; vendor tier; region; retention; training-use = no (evidence: link)
Tools it can call, each with a risk rating and whether a human gate applies
Inputs: data fields; personal and sensitive fields; lawful basis or consent; source systems
Eval: set size, rubric, latest pass rate, date, judge type and agreement with the operator
Known failure modes and mitigations (from the pre-mortem)
Human oversight: who reviews what share, authority to pause, escalation path
Logs: what is logged, where, retention (at least 6 months), who can read them
Disclosures: AI-interaction notice shown? Generated-content marking? (EU Art 50 if any EU user)
Incident runbook link; last review date; next review date
```

The eval line belongs to `llm-evals`; the oversight and autonomy lines belong to `pilot-rollout`. Point at their artefacts rather than copying them.

## DPDP checklist

India's DPDP Act 2023 with the DPDP Rules 2025, notified 13 Nov 2025. The Board and definitions are in force now; consent-manager provisions apply from 13 Nov 2026; notice, security, breach notification, data-principal rights and the remaining substantive duties apply from 13 May 2027. Penalties reach ₹250 crore per instance once the Board has full powers. Build for May 2027 now.

- Itemised notice for this purpose, in English plus the user's language on request (any Eighth Schedule language).
- Consent recorded and withdrawable, with withdrawal as easy as consent. If a consent manager will be used, the integration is planned for after 13 Nov 2026.
- Purpose limitation: the AI use sits inside the purpose the data was collected for, or a new consent is taken.
- Retention and erasure rule written for inputs, outputs, logs and vendor-side copies. Where the Third Schedule applies (large e-commerce, gaming and social platforms, 3-year cap), 48 hours' notice before erasure.
- Breach runbook: notify affected people promptly; the Board without delay; a detailed report within 72 hours.
- Children's data: verifiable parental consent, or exclude children.
- Cross-border: the vendor region is documented; an India residency option is used where the vendor offers one.
- Rights requests answered within 90 days; records kept at least 1 year (the rule number differs between sources; check the gazette).
- Significant Data Fiduciary watch: if the company could cross the government's volume or sensitivity thresholds, or profiles people with AI, plan for an India-based DPO, an independent audit and a DPIA. One source lists "algorithmic due diligence" as an SDF duty; the brief could not confirm the wording in the final Rules (UNVERIFIED): read the gazette text before relying on it.

## EU AI Act quick screen

The Digital Omnibus on AI, Regulation (EU) 2026/1744, entered into force on 27 Jul 2026. Stand-alone high-risk (Annex III) obligations apply from 2 Dec 2027; product-embedded (Annex I) from 2 Aug 2028. Article 50 transparency has applied since 2 Aug 2026, with fines up to €15M or 3% of turnover (the lower figure for SMEs).

- A person interacts with the system? Disclose that it is AI, unless obvious. In force.
- It generates text, image, audio or video shown to people? Machine-readable marking (grace to 2 Dec 2026 for systems already on the market), deepfake disclosure, and disclosure of AI-generated text published to inform the public unless a human edited it. In force.
- It makes or helps make decisions about people in Annex III areas (hiring, credit, education, essential services, law enforcement)? High-risk track from 2 Dec 2027. Design the deployer duties (Art 26) now: use per the provider's instructions, trained and authorised human oversight, representative input data, monitoring and incident reporting with the power to suspend, auto-generated logs kept at least 6 months, notice to workers' representatives, notice to affected individuals, provider information feeding the DPIA.
- Staff literacy (Art 4, since Feb 2025, softened to "support" by the omnibus): a short training record for the people who use it.

## Vendor terms checklist

Checked 17 Oct 2026. Ask per tier actually purchased, and re-check before signing.

- **Training on our data: must be no.** Paid API tiers at Anthropic, OpenAI and Google state no training. The unpaid Gemini tier uses prompts and outputs for product improvement with human review; it is not for personal or confidential data.
- **Retention.** Anthropic deletes inputs and outputs within 30 days by default, longer for policy violations, zero data retention (ZDR) by agreement; a "Covered Models" safety-retention carve-out is reported but UNVERIFIED. OpenAI keeps abuse-monitoring logs up to 30 days; ZDR needs approval and is endpoint-specific, available on chat completions, responses, embeddings, audio and realtime, and excluded for conversations, agents, assistants, vector stores, files, fine-tuning, evals and batches. Google's paid tier logs for a limited unspecified period for abuse detection, Grounding stores prompts and outputs 30 days, and no ZDR option is published.
- **Region.** Storage residency and inference residency are separate questions. OpenAI offers India residency for storage only, with in-region inference in the US, EU and UAE, at +10% on residency endpoints for models released after 5 Mar 2026. Anthropic prices US-only inference at 1.1x. Google: per contract.
- **Who can read flagged content**, and under which policy.
- Sub-processors; export of prompts, evals and data on exit; model deprecation notice period; price-change notice period.

## Decision rules

The operating rules for a lending system (money numbers computed by code, unsourced product facts hand off, credit outcomes advisory to a named human, promotional when unsure, distress routes to a person) have one home: `lending-domain`. `conversation-design` carries the bot subset as stop rules for the system prompt. Check the system card against that list rather than restating it here.

## Question lists

For the compliance owner:

- Which consents do we hold for this person, under which notice version, and can they withdraw in one step?
- Do we have the regulated entity's written approval for this customer-facing content?
- Where is the grievance path, and is it in the user's language?
- Who pulls the kill switch, and when was it last tested?

For the lender or regulated partner:

- Which of your Key Facts Statement and offer fields can we consume by API, and how often do rate cards change?
- Is our system's content subject to your product-approval or model-risk process?
- Do you accept Account Aggregator data for income, and for which segments?
- Which of your KYC and video-KYC vendors must we use?
- How do you want partner-sourced files flagged, and what triggers payout or clawback?

## Output

- The system card, one page, every line filled or carrying a named unknown.
- The completed checklists: DPDP, EU screen, vendor terms, and the India pre-flight where it applied, each line yes or no with an owner.
- The open-items list: every no, with owner and date, sorted by go-live blockers first.
- The regulatory dates that bind this deployment, copied onto the owner's calendar.

What takes over: `pilot-rollout` for the staged go-live and the handoff pack; `llm-evals` for the red-team file and the weekly sample; `conversation-design` for the disclosure copy and the handoff turns; `grilling` when the compliance owner and the builder disagree on scope.
