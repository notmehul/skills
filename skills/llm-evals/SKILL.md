---
name: llm-evals
description: "Decide whether a prompt, agent or model change is good enough to ship, and keep it that way in CI and production. Use on 'is it good enough', 'write an eval', a regression, before shipping a prompt or agent, a judge that drifts, or 'red team'."
license: MIT
metadata:
  version: "1"
  updated: "2026-10-18"
  harnesses: "claude-code codex opencode"
  source: "research-2026-10/evals-observability.md C, D1-D13 and research-2026-10/agent-frameworks.md D9 (Oct 2026)"
---

# LLM evals

A score is not evidence until you have read the transcripts behind it. Everything here follows from that: graders are binary and ask one question each, a judge earns its number against human labels, and the first afternoon is spent reading, not building. The event row defined in `building-agents` is where every score, fallback and decision lands; this skill tells you what to write into it.

## Steps

1. **Run the afternoon loop** below. Done when you can say "pass-all is X% plus or minus noise on N cases, the top failure mode is Y" and point at the transcripts.
2. **Grow the golden set** with the rules under "The golden set". Done when it has 100 or more cases with a held-out slice before it gates anything.
3. **Calibrate every model judge** with the protocol under "Judge protocol". Done when each judge reports TPR and TNR on a held-out test slice.
4. **For an agent, add the trajectory checks** under "Agent cases". Done when every case grades the end state and every write tool has a case where the right answer is not calling it.
5. **Gate CI and watch production.** Read `references/ci-and-online.md`. Done when a PR fails on a measured regression and a nightly job writes scores with confidence intervals.
6. **Settle the reliability rules** for structured output, retries, fallbacks and personal data in traces. Read `references/reliability.md`. Done when every fallback writes an event row and content capture is off by default.
7. **Spend one afternoon red-teaming** before anything reads untrusted content or holds a write tool. Read `references/red-team.md`. Done when every successful attack is a golden-set case with a code grader.

## The afternoon loop

About four hours. Precondition: the app runs end to end on your machine and emits traces, even to a local JSONL.

1. **(30 min) Pull 30 real traces.** Production if you have it; otherwise run 30 realistic inputs. Sample 20 at random and 10 from any negative signal (thumbs-down, retries, support tickets).
2. **(60 min) Open-code them.** One free-text line per trace: what, if anything, is wrong. No rubric yet. Stop early only if the last 10 produced no new kind of problem.
3. **(20 min) Group the notes into failure modes.** Expect 3 to 7. Name each as a binary question ("Did it call a write tool without a confirmation step?"). Drop anything two experts would not agree on.
4. **(30 min) Pick the cheapest grader per failure mode.** A rule can decide it → a code assertion (regex, schema, tool-name check, database state check). Needs judgement → a model judge, binary PASS or FAIL with an UNKNOWN escape, the rubric written as concrete pass and fail conditions, from a different provider than the app model.
5. **(40 min) Build the set.** 20 to 50 cases as JSONL: `{id, input, expected_outcome or null, failure_modes_to_check[], source: prod|ticket|handwritten|synthetic}`. At least 5 cases where the behaviour should not happen. Every case has a known-good reference answer or state that passes all graders; if you cannot produce one, the task is ambiguous.
6. **(20 min) Run it 3 times per case.** Report pass-all rate and per-failure-mode rate, runs shown separately. Read every failing transcript and decide "agent bug" or "grader bug" before touching the prompt.
7. **(10 min) Commit** the JSONL, the graders and the run report. The next change to the prompt or tools re-runs this.

## The golden set

- Sources in priority order: production transcripts, then the bug tracker and support queue, then 5 to 10 hand-written cases, then synthetic cases each anchored on a real example. Never synthesise the expected outputs.
- Sampling ladder, several rungs per batch: random (always 30% or more of the batch), then a few per cluster by route, tool or intent, then outliers (longest, most tool calls, highest cost, most retries), then cases a cheap classifier flagged, then negative user feedback.
- Size: 20 to 50 to start; 100 or more before it gates CI; 100 or more fresh traces per 2 to 4 week review cycle, with 10 to 20 outlier traces read weekly in between.
- Hygiene: redact personal data before a case enters the repo; record `source` and `added_on`; version the dataset (a dated file in git is enough); never delete a case, deprecate it with a reason.
- Balance: for every "should do X" a "should not do X"; for agents, at least one case per tool where the right answer is not calling it.
- A held-out slice of 30% or more is never touched while hill-climbing a prompt.

## Judge protocol

1. One judge per failure mode. Binary verdict plus a one-sentence reason. UNKNOWN allowed.
2. The rubric is checkable claims, not adjectives: "PASS if the reply names the processing fee and the fee matches the lender's fee table; FAIL if it states a number not in the table."
3. The judge sees only the slice of the trace it needs.
4. The judge comes from a different provider than the app model, unless you have shown same-model agreement with humans.
5. Label 100 to 200 examples for that failure mode with roughly balanced pass and fail. Split 10 to 20% train, 40 to 45% dev, 40 to 45% test. Tune the rubric on train, check on dev, report once on test.
6. Report TPR (catches real failures) and TNR (passes good output). Both. If either is below about 0.8, read the disagreements by hand before any automated rubric tuning.
7. Stability: run the judge twice on the same 20 outputs; a flip rate above a few percent means the rubric is under-specified. For pairwise judging, swap the order and count position flips.
8. Design against the known biases: position, verbosity, self-preference, format and markdown preference, leniency drift over long sessions.
9. Re-calibrate when the judge model, the app model or the rubric changes, and at least once per review cycle.
10. Retire a judge that has passed at about 100% for three cycles; keep the cheap code check that replaced it.

## Agent cases

For anything that calls tools, start with 20 to 50 tasks from real cases and manual checks before writing the agent's second prompt, and define each task's expected end state of the system (rows, files, messages), never the expected steps.

- Grade the outcome first: the final environment state, not the agent's claim.
- Then four checks per tool call: right tool name; right arguments (schema-valid and semantically right); result handled, including error branches; resulting state correct.
- Trajectory matching: exact order only for a rigid workflow with one correct path; otherwise "required calls present" in any order and "forbidden calls absent".
- Negative cases: no tool should be called; a confirmation step precedes every write; a tool on the deny list is never called.
- Loop and budget assertions: max steps, max calls per tool, max cost per task, no repeated identical call. Ten lines over the trace will do.
- Run 3 or more trials per case. Report pass@k and pass^k, and gate on whichever the product needs: pass^k (k=3 as the floor) for anything customer-facing, pass@k only where one good answer is enough. 75% per trial is 42% pass^3.
- Keep capability evals (low pass rate, drives improvement) apart from regression evals (near 100%, gates releases); promote a capability task once it is stable.
- Record tokens, tool calls, cost and wall time next to every score. Report cost per successful task, not cost per call.
- Subagents: assert the parent's outcome and the child's trace both exist under one trace id; grade the child with its own case file.
- Multi-turn: check the goal for the whole conversation, then find the first upstream failure; generate cases by replaying real prefixes.
- Once you have 50 or more failures, build a transition-failure matrix (last good step by first failed step) and fix the densest cell first.
- A case that scores 0% across many trials is usually a broken task or grader, not a broken agent.
- Rerun the suite on every model or framework bump and keep the result as an event row.

## Output

- The failure-mode list, each a binary question with its grader named.
- The golden set as versioned JSONL with `source`, `added_on` and a held-out slice.
- The judge calibration report: TPR and TNR per judge on the test slice, with the labelled examples.
- The run report: pass-all and per-failure-mode rates with runs shown separately, cost per successful task, and the transcripts behind every failure.
- The CI gate, the nightly job and the online tiers from `references/ci-and-online.md`, live.
- The red-team report with every successful attack converted to a case.

What takes over: `building-agents` for the event row the scores land in and for a harness change the matrix calls for; `pilot-rollout` when the numbers decide an autonomy level; `applied-ml` (its experiments reference) when the question moves from "is the output correct" to "did it change a business metric"; `prove-it-works` before any of this is called done.
