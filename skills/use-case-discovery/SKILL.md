---
name: use-case-discovery
description: "Scope where AI belongs in a business process: shadow the operator, map and classify each step, score and gate candidates, write the one-page brief and eval spec. Use on 'where should we use AI', 'can we automate X', or a new team or process."
license: MIT
metadata:
  version: "1"
  updated: "2026-10-18"
  harnesses: "claude-code codex opencode"
  source: "research-2026-10/business-use-cases.md (Oct 2026); SVPG four risks"
---

# Use-case discovery

Value in 2026 sits in narrow, high-volume, back-office steps with a verifiable output, redesigned around the model and owned by the team that runs the workflow. Founders guess wrong about where that is: in Stanford's WORKBank study (Jun 2025), 41% of startup task mappings landed where operators did not want automation or where it was not feasible. So discovery starts next to the operator, and a pilot earns its place through gates, never through a demo.

## Steps

1. **Pick the workflow, not the department.** Ask the sponsor for the three processes that consume the most people-hours or create the most customer-visible delay. Choose one. Done when you can name the workflow and the person who does it most days.
2. **Shadow the operator for two hours.** Sit with them while they work. Capture every step, the inputs and the system each comes from, the decision made, the exception handled, the artefact produced, and the time taken. Done when the step table below has a row for every step you watched.
3. **Interview the operator for 45 minutes** with the questions under "Operator questions", in order, in their words. Stop when the map stops changing.
4. **Classify every step** with the rules under "Classification". Done when each row carries one of automate, assist, decision-support or leave human.
5. **Run the agent test** on each automate or assist step that is itself multi-step. A step that fails any line stays a workflow of deterministic steps plus single model calls.
6. **Score and gate the candidates** with the rubric under "Scoring". Done when every candidate has a priority score and either passes all four gates or names the gate it fails.
7. **Hold the 90-minute workshop** when there is a team around the workflow. Read `references/workshop.md` for the agenda. Skip it for a one-person process.
8. **Write the brief for the first pilot** using `references/brief-template.md`, with its eval spec and pre-mortem. Read `references/cost-model.md` to fill the cost ceiling. Done when every line of the brief has a value or a named unknown.

## Operator questions

Ask in this order and record the answers verbatim.

- Walk me through the last one you did, start to finish. What did you open first?
- How many of these per day or week? What does the busiest day look like?
- Where do you wait on someone else, and for how long?
- Which step do you dread? Which step would you not trust anyone else to do?
- What do you check before you hit send, submit or approve? What would make you reject it?
- When this goes wrong, how do you find out, and what does it cost in money, time or a customer?
- Show me three recent ones that were hard. What made them hard?
- What do you keep in your head, a notebook or WhatsApp that is not in the system?
- If the system drafted this for you, what would you need to see to accept it in under a minute?
- Which part would you happily never do again? Which part would you miss?
- Who touches this before and after you?
- Is there a record of past cases with the final outcome attached? Where?

## The step table

One row per step:

`step | who | trigger | inputs (system, document, verbal) | decision made | rules or judgement | exceptions per week | output | how the output is checked | reversible | minutes per item | volume per week | pain 1-3 | past cases with outcomes (yes, no, partial)`

## Classification

- **Automate** when the output is checkable by a rule, a test, a downstream system or a sample review; the action is reversible or low-stakes; volume is at least ~50 per week; and a labelled history exists or can be built in a week.
- **Assist** (the system drafts or proposes, a human approves) when judgement is real but bounded, volume justifies drafting, and the operator can verify faster than they can produce. This is the default for anything customer-facing.
- **Decision-support** (surface, summarise, flag, never act) when a wrong action is costly or irreversible, ground truth arrives late, or the decision is legally a human's: credit, hiring, health, legal, and anything else that decides about a person.
- **Leave human** when volume is low, the task is relationship or negotiation, or the operator's "would miss" answer lands here.

Cross-check against what the operators said they want. A step they do not want automated and cannot verify is a red light. Build elsewhere, however good the demo.

### The agent test

A step is an agent candidate only when every line holds:

- Deterministic automation has already failed here or would need an unmaintainable rulebook.
- Inputs are unstructured (documents, email, conversation) or the step is judgement-heavy with exceptions.
- Every sub-step has an observable success signal: a test, a lookup, a human check.
- Every tool the agent would use can be rated low, medium or high risk by read versus write, reversibility, permissions and money, and the high-risk ones pause for a human.
- One agent with tools is enough. Needing a second agent on day one means you have two use cases.

## Scoring

Score 1 to 3 on each dimension. Priority = value x volume. The first pilot must score at least 2 on verifiability, reversibility, data readiness and owner; a candidate that fails a gate goes to "later" with the failing gate named.

| Dimension | 1 | 2 | 3 |
| :--- | :--- | :--- | :--- |
| Value | Under 2 person-hours a week, no revenue or risk link | 2 to 10 hours a week, or removes a known customer delay | Over 10 hours a week, or moves revenue, margin, churn or compliance exposure by a number the sponsor agrees to |
| Volume and repeatability | Under 20 items a week, each different | 20 to 200 a week, same shape | Over 200 a week or growing, same shape |
| Verifiability | Only an expert can tell, slowly | Spot-checkable in under a minute, or the downstream system rejects errors | A rule, test or reconciliation checks it |
| Reversibility | Irreversible, or customer-, money- or legal-facing | Reversible with effort, or internal only | Reversible instantly, internal, or draft only |
| Data readiness | Fails two or more checks below | Fails one | Passes all |
| Owner | No operator wants it | An operator is curious | A named operator wants it and will review 50 samples a week |
| Integration effort | New credentials or APIs across two or more systems, none documented | One system with a documented API or export | Files, email, a spreadsheet, or an API you already hold keys for |

Re-score quarterly: effort and feasibility fall as models and connectors improve.

### Data readiness checks

Each check has a pass condition and an artefact that proves it.

1. Examples exist: at least 50 past cases with the final outcome attached. Artefact: the export.
2. Access: you can pull them without a human copying files, within a week. Artefact: a working query or API call.
3. Ground truth is real: the recorded outcome is what happened, not what was typed to close the ticket. Artefact: 10 spot-checked by the operator.
4. Coverage: every category that occurs in at least 5% of months has at least 20 examples. Artefact: a count table.
5. Freshness: the process has not changed since the examples ("what changed this year?"). Artefact: a one-line note.
6. Personal data inventory: which fields are personal or sensitive, whose consent covers this purpose, where it will be stored, for how long. Artefact: a row in the system card (`ai-governance`).
7. Label agreement: two operators label the same 20; agreement of 80% or better, or the rubric needs work before the model does. Artefact: the 20 with both labels.

### Build, buy or partner

- **Buy** when a category product exists (helpdesk AI, document extraction, voice, CRM enrichment, meeting notes), the workflow is not the company's product, and the vendor's paid tier meets the data terms. Purchased solutions succeeded about twice as often as internal builds in the 2025 MIT and Menlo surveys.
- **Build thin** when the value is in company-specific rules, prompts, data joins or an integration the vendor lacks. Keep the build to glue, prompts and the eval harness, on a bought platform.
- **Build deep** only when the workflow is the product or the data moat, and someone will staff it after you leave.
- **Partner** when the pilot needs a capability you would use once.

Ask every vendor: data retention and training terms on the tier you would buy; export of your data and prompts; per-task cost at your volume; the human you call.

### The first-pilot picker

Among gate-passing candidates, pick the one with the highest verifiability x reversibility x owner, even when its value is lower. Say why in one sentence: the first pilot buys a working eval loop and an internal champion. Value comes from the second pilot onward.

## The four risks

Before the brief is written, the top candidate has an answer for each: **value** (will they use it), **viability** (does it work for the business and its rules), **usability** (can the operator work it in under a minute per item), **feasibility** (can it be built with the data and access you have). A risk without an answer becomes one of the brief's three unknowns.

## Red flags

Name these out loud when you see them.

- Nobody can produce 20 past examples with outcomes.
- The sponsor wants it, the operator does not, and the operator is not in the room.
- The "use case" is a feature of a tool they already pay for.
- The value depends on an integration nobody has credentials for.
- The step decides about a person. Decision-support only, and the governance path opens.

## Output

- The workflow map (the step table, with classifications).
- The scored backlog: one row per candidate with priority score, the four gates, and the failing gate named where it fails.
- The one-page brief for the first pilot, with eval spec, pre-mortem and cost ceiling.
- Three unknowns to verify next: usually data access, true volume, and ground truth.

What takes over: `pilot-rollout` once the brief is agreed; `ai-governance` when the output reaches a customer or decides about a person; `customer-research` when the evidence about users is thin; `grilling` to settle the design before anything is built.
