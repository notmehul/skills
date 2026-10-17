---
name: pilot-rollout
description: "Take a POC to real operators: shadow, assisted, then autonomous per action category, each behind a numeric gate, with rollback triggers, a kill date and a handoff pack. Use on 'handoff', 'shadow mode', 'who maintains this', or a pilot going live."
license: MIT
metadata:
  version: "1"
  updated: "2026-10-18"
  harnesses: "claude-code codex opencode"
  source: "research-2026-10/business-use-cases.md D4 and research-2026-10/india-fintech-lending.md C (Oct 2026)"
---

# Pilot rollout

A pilot with no owner, no gate and no kill date ends in pilot purgatory, and that is the default outcome. This skill takes the agreed brief from `use-case-discovery` and moves the system to real operators through three stages. Promotion happens per action category, never for the system as a whole, and the numbers that decide each promotion are written down before the first production input arrives. Two invariants hold at every stage: AI output is a proposal until a human confirms it, and every action writes an event row.

## Steps

1. **Split the system's actions into categories.** One category per distinct action and risk level: a drafted message to an applicant, a field written to the CRM, a salary slip marked as read. Each category moves through the stages on its own. Done when the stage table has a row per category with its current stage, and the brief names the money or customer threshold that makes an item high-stakes.
2. **Write the exit conditions before shadow starts.** Copy the rollback triggers below into the brief, pick the kill date, and put it on the sponsor's calendar. Done when the sponsor has agreed in writing what happens on the kill date if the launch bar is not met: the pilot shuts down and gets written up.
3. **Run shadow mode.** Two to four weeks; at least eight in a regulated workflow (credit, health, legal, anything that decides about a person). The system reads production inputs and writes only to its log, never to production. The operator does not see its output in real time, so their own behaviour stays uncontaminated. Log every disagreement as agent-right, human-right or ambiguous, with a reason code. Done when each category has 500 logged items or two full weekly cycles, whichever comes later.
4. **Promote to assisted, one category at a time.** The system drafts or proposes; the operator reviews 100% and accepts, edits or rejects each item. Track accept, edit and reject counts and time-to-review. Done when the category has met the assisted gate and the operator has confirmed the review step works in their own tooling.
5. **Promote low-risk categories to autonomous.** Canary at 5%, then 25%, then 100% over two to three weeks. Keep 5% random human review for the life of the system and 100% review of high-stakes items. Done when the category runs at 100% and the review sample is still scored every week.
6. **Fill the weekly pilot sheet** every week and send it to the sponsor. Done when the sheet carries this week's decision (hold, promote or rollback) and names next week's category.
7. **Run the adoption plan** from the first assisted week. Done when the 30-, 60- and 90-day measurements exist by role.
8. **Assemble the handoff pack and hand over.** Done when the maintainer has, with you out of the room, run the evals and read the result, edited the prompt and previewed the change, and walked the runbook for one failure sign.

## Stage gates

| Stage | Enter when | Operator sees | Review | Minimum sample |
| :--- | :--- | :--- | :--- | :--- |
| Shadow | The brief is agreed and the kill date is on the calendar | Nothing in real time | Disagreement log, coded | 500 per category or two weekly cycles |
| Assisted | Category agreement of 85 to 90% or better on the shadow sample, and zero critical errors | Draft or proposal with reasoning and sources inline | 100%, with accept, edit, reject and time-to-review | Until the autonomous gate is met |
| Autonomous | 95% or better per category on the latest 500 or more samples, no regression in the past week, the owner has read 50 random decisions by hand, and the rollback plan is written | Exceptions only | 5% random, 100% of high-stakes items | For the life of the system |

A critical error is one of policy, money or data. Regulated workflows stay at assisted until the regulator's own process (for Indian lending, the lender's model-risk process) approves otherwise; `ai-governance` carries that rule.

## Rollback triggers

Pre-agreed and written in the brief. Any one of them drops the category to the previous stage the same day:

- Agreement below 80% two days running, or two consecutive weekly eval runs below the launch bar.
- Any critical error.
- A vendor incident, or a model change not yet re-evaluated against the golden set (`llm-evals` owns the set).
- The owner says stop.

## Weekly pilot sheet

One page, one row per week, shared with the founder:

`week | volume | pass rate on eval | accept / edit / reject | escalations and why | cost per task | incidents | decision this week (hold, promote, rollback) | next week's category`

## Adoption plan

- The operator writes the rubric and may edit the prompt; the engineer owns the harness.
- Name one super-user per team. Hold a 30-minute calibration session every week for the first month with the builder, the operator and whoever owns risk.
- Show the system's reasoning and sources inline. Make "reject with reason" one click.
- Measure at 30, 60 and 90 days by role: usage, acceptance rate, confidence (ask them), and whether the old workflow still runs in parallel.
- Before workplace use, tell staff what it does, what it logs, and that they can override it. The EU AI Act will require this of deployers of high-risk systems from 2 Dec 2027 (as of Oct 2026); it is cheap now and expensive to retrofit.

## Handoff pack

The maintainer is not an engineer. Everything in the pack works without one.

- The one-page system card. `ai-governance` owns the format.
- The eval set, the rubric, and a "run the evals" button or script with the expected output written beside it.
- Prompt and config in one place the maintainer can edit without code: plain-English field names, a preview before publish, version history.
- The one-page runbook below.
- A dashboard whose first tile is "exceptions awaiting a human".
- A weekly 10% sample review the maintainer runs and records. A regulated customer-facing flow may need 100%; the pre-flight in `ai-governance` decides.
- A monthly 30-minute review on the calendar with the operator and the founder: pass rate, cost per task, incidents, the top error cluster.
- Vendor contacts, contract tier, renewal date, and the data-export instructions.

### The one-page runbook

```
What it does:                  <two sentences, in the operator's words>
What it must never do:         <from the brief's guardrails>
Three failure signs to watch:  <sign, where to see it, the number that trips it> x3
Kill switch:                   <the one action, who may take it, how fast traffic reaches humans; tested on <date>>
When quality drops:            <pause promotions; run the evals; compare with last week's sheet; call the first name below>
When the vendor changes the model: <hold at the current stage; re-run the evals; promote only on a pass>
When a customer complains:     <find the event row; read the transcript; reply within <N> hours; log the incident>
When the bill spikes:          <read cost per task on the sheet; cap retries; call the first name below>
Whom to call, in order:        <name, role, number> x3
```

Test the kill switch before handover and write the date on the runbook.

## Output

- The stage table: each category's current stage with its gate history.
- The weekly pilot sheets, one per week of the pilot.
- The adoption measurements at 30, 60 and 90 days.
- The handoff pack, signed off by the maintainer after walking it alone.
- The kill-date write-up when the launch bar was not met: what was tried, the numbers, why it stopped.

What takes over: `ai-governance` for the system card and the compliance pre-flight; `llm-evals` for the golden set, judge calibration and the weekly re-runs; `show-me-your-work` for the decision trail while shadow mode runs unattended; `prove-it-works` before any promotion is declared.
