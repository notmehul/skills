# The one-page brief, eval spec and pre-mortem

Fill every line. A blank is a finding, not a gap to paper over.

## Brief

```
Use case:            <verb + object + for whom>  e.g. "Draft the missing-documents message for the loan associate"
Owner (operator):    <name, role>      Sponsor: <name, role>
Workflow step(s):    <from the map>    Class: automate | assist | decision-support
Today:               <volume per week, minutes per item, who, cost of an error>
Proposed:            <what the system does, what the human still does, where it stops and asks>
Inputs:              <systems, documents, fields; personal data yes/no and which>
Outputs and actions: <artefact; tools it may call, each rated low/medium/high risk>
Done means:          <eval threshold + operator metric + business metric + date>
                     e.g. "90% of drafts accepted with at most one edit on a 50-case held-out set;
                     associate time per item from 12 minutes to 4; by 15 Dec"
Not in scope:        <explicitly>
Guardrails:          <what it must never do; what triggers human escalation>
Cost ceiling:        <per task and per month at target volume; see cost-model.md>
Data and governance: <vendor tier, region, retention; consent basis; EU exposure yes/no; where logs live>
Rollout:             <shadow weeks → assisted categories → autonomous categories; rollback trigger; kill date>
Open risks:          <top three from the pre-mortem>
```

## Eval spec

Write it before the build, with the operator.

- **Set.** 30 to 50 real cases, stratified by category and difficulty, with at least 10 hard ones the operator chose. Hold out 20 for the final gate. Add 20 synthetic inputs for rare but nasty scenarios; never synthesise the expected outputs.
- **Judgement.** Binary pass or fail per case against a rubric of three to six lines in the operator's words, plus a one-sentence critique on every fail. No 1-to-5 scales.
- **Thresholds, tiered.** Launch bar, 90-day target, aspiration, for correctness, format and compliance, and operations (latency, cost per task, escalation rate).
- **Judge.** Human for the first 100. If a model judges after that, report its agreement with the operator on a 30-case sample and keep sampling where agreement is weakest. `llm-evals` owns the judge protocol.
- **Cadence.** Re-run the full set on every prompt, model or tool change, and weekly in production on fresh samples. Two consecutive runs below the launch bar roll back to the previous autonomy level.
- **Error analysis.** Every fail gets a free-text note; cluster monthly; fix the largest cluster first.

## Pre-mortem

One row per failure mode:

`failure mode | how we would notice | who it hurts | likelihood 1-3 | severity 1-3 | detection 1-3 (3 = hard to detect) | product | mitigation (guardrail, human gate, monitoring) | owner`

Seed the list with: a wrong but plausible output accepted; stale data; prompt injection through customer content; personal data leaking into a prompt or log; a tool call on the wrong record; a silent vendor model change; cost blow-up from retries; the operator over-trusts and stops checking; the operator ignores it and runs the old way in parallel; the one person who owns it leaves.

## The metric ladder

Report all three, in this order: eval pass rate → operator metric (minutes per item, acceptance rate, edit distance, escalation rate) → business metric (hours freed and where they went, cycle time, a revenue or cost line). A pilot that reports only the first is a demo.
