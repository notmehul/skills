---
name: study-design
description: "Design or check a human-AI user study: 'measure trust' or reliance, 'is this result real', 'should this be a study', sample size, preregistration, ethics without an IRB, Indian recruitment, or a CHI, CSCW or HCOMP write-up."
license: MIT
metadata:
  version: "1"
  updated: "2026-10-18"
  harnesses: "claude-code codex opencode"
  source: "research-2026-10/human-centred-ai-research.md C, D1-D4, D6-D8 (Oct 2026)"
---

# Study design

A study of how an AI interface changes what people do: reliance, verification, delegation, and what is left of the skill afterwards. The field moved to behaviour in 2025 and 2026 because self-reported trust predicts behaviour weakly and people's confidence in model answers is miscalibrated; reviewers now ask for a behavioural dependent variable (the DV) and a frozen stimulus set that can be rerun after the next model release. The two things an engineer gets wrong first are building the system before writing the question, and comparing the new thing to nothing.

## Steps

1. **Decide whether it should be a study at all** with the three questions under "Should this be a study". Done when all three are yes, or the answer is "build it" or "run a formative interview study and say so" (`customer-research`).
2. **Fill the design checklist.** Every item under "Design checklist" gets a written answer. Done when none says "later".
3. **Choose the shape** with the rules under "Within or between" and "Real outputs or Wizard-of-Oz". Done when the design, the counterbalancing scheme and the stimulus source are each one sentence.
4. **Size the sample** from "Sample size". Done when N, the smallest effect of interest and the stopping rule are written down, and the fallback (a Bayesian analysis or a formative framing) is named if N is out of reach.
5. **Pick measures** from `references/measurement-menu.md`. Done when there is one primary DV computed from named log fields, a capped list of secondaries, and both AI-correct and AI-wrong trials in the design.
6. **Preregister** with the outline under "Preregistration". Done when the time-stamped record exists and its link sits in checklist item 13.
7. **Settle ethics, consent and recruitment** with "Ethics without an IRB", "Data handling" and "Recruitment". Done when the ethics sentence for the paper is written.
8. **Pilot with 3 to 5 people**, then compute the primary DV from the pilot logs end to end. Done when the number comes out of the recorded data without manual repair, and duration and pay are re-estimated.
9. **Ask the five pre-launch questions** of a collaborator or reviewer. Done when each has an answer you would put in the paper.
10. **Analyse** with "Analysis decision tree". Done when the preregistered primary test is reported with effect size, 95% CI, exact N per condition after exclusions, model formula and software versions.
11. **Write up** with `references/paper-skeleton.md` and the venue rule, and publish the reproducibility package. Done when a stranger can rerun the figures from the repository.

## Should this be a study

- Can the answer change a design decision or a theoretical claim? If not, build the thing instead.
- Is there a behavioural DV (switch rate, accuracy against ground truth, unaided performance afterwards, verification actions in the logs)? If only satisfaction can be measured, run a formative interview study and call it that.
- Can the stimuli be frozen and shared? If not, the result will not replicate past the next model release.

## Design checklist

1. One-sentence research question with the behavioural DV named.
2. What decision or design changes if the answer goes either way.
3. The closest three prior studies, with DOIs, and what this adds: new population, new mechanism, replication under 2026 models, or a measurement improvement. `research-brief` (its literature-review branch) owns this.
4. Design: within or between; conditions; counterbalancing scheme; pre/with/post phases.
5. Stimuli: real pinned model outputs or Wizard-of-Oz; model id, date and prompts archived; ratio of correct to incorrect AI outputs; verified ground truth.
6. Primary DV and exactly how it is computed from the logs. Secondary DVs listed and capped.
7. Smallest effect size of interest; power against CHI local standards; resulting N; stopping rule.
8. Participants: population, inclusion criteria, platform or local route, pay rate and currency, expected duration.
9. Attention and comprehension checks consistent with platform policy (Prolific, Nov 2025 rules: at least 2 failed attention checks before rejection on studies over 5 minutes; a failed comprehension check is never grounds for rejection).
10. Exclusion rules written before data collection: speed, failed checks, duplicate IPs, incomplete sessions.
11. Consent text, data minimisation, retention period, storage location, de-identification plan, DPDP-style notice.
12. Ethics route (institutional, independent committee, or documented self-review) and the sentence that will go in the paper.
13. Preregistration platform and link.
14. Analysis plan: model, random effects, covariates, multiplicity handling, Bayesian or frequentist, software.
15. Pilot with 3 to 5 people; fix instructions; re-estimate duration and pay.
16. Logging checked end to end on pilot data: the primary DV computes from what was recorded.
17. Repository skeleton created before data collection: stimuli, code, analysis, README.

## Within or between

Default to within-subjects, counterbalanced with a Latin square, two or three conditions, order as a covariate. Within when carry-over is small and the manipulation is visible (interface, explanation format); it halves recruitment. Between when exposure changes the person (learning, skill, deception) or the manipulation would be obvious across conditions. For a question about skill or offloading, use the pre/with/post template: within for time, between for AI condition, with unaided performance measured in the post phase.

## Real outputs or Wizard-of-Oz

For reliance, verification or calibration questions, use real, pre-generated, pinned model outputs: a fixed stimulus set with verified correct and incorrect answers in a known ratio (70/30 is common), model id and date recorded, prompts and outputs archived. The manipulation (sources, explanations, uncertainty) lives in the text, so there is no deception and the study reruns. Wizard-of-Oz is right for a capability that does not exist yet, or for interaction choreography.

## Sample size

CHI local standards, not Cohen's defaults. A CHI 2016 survey of CHI 2014 papers found a median N of 18, a mode of 12, and 70% of studies under 30; a 17-person two-condition within-subjects study has power 0.49 for a large effect. A CHI 2025 meta-study put a medium effect at about d 0.44 between subjects and 0.52 within.

Working numbers (alpha .05 two-sided, 80% power, standard G*Power arithmetic; recompute for your own smallest effect of interest):

| Design | Effect | N |
| :--- | :--- | :--- |
| Paired (within) | d = 0.5 | about 34 participants |
| Two groups (between) | d = 0.5 | about 64 per group |
| Two groups (between) | d = 0.44 | about 82 per group |

If you cannot reach these, preregister a Bayesian analysis or frame the study as qualitative or formative. Ten people per cell in a between-subjects design is noise read as signal.

## Preregistration

AsPredicted (free, nine short questions, time-stamped PDF) for experiments; OSF (free, with templates for qualitative, replication and secondary-data work) for mixed or qualitative studies. It is the cheapest credibility signal an unaffiliated researcher has. The nine items below paraphrase the AsPredicted form (UNVERIFIED against the live wording):

1. Has any data been collected? ("No", or explain.)
2. Hypothesis: directional, one per primary DV.
3. Dependent variables: primary first, computed how, from which log fields.
4. Conditions: list, assignment (within or between), counterbalancing.
5. Analyses: the exact test or model per hypothesis, including random-effects structure and covariates.
6. Outliers and exclusions: rules, thresholds, order of application.
7. Sample size: N, rationale with the effect-size source, stopping rule.
8. Other: anything else you want held to.
9. Study name and type.

Human-AI extensions, under "Other" or in an OSF addendum: the model (provider, id, version or date, decoding settings, system prompt; whether outputs were pre-generated and frozen); the stimulus set (item count, proportion with incorrect AI output, how correctness was established); reliance definitions as you will compute them (agreement, switch, over-reliance, under-reliance, RAIR and RSR); self-report instruments with exact versions and timing; manipulation and attention checks with pass criteria; exploratory analyses you already intend, labelled; and where deviations will be logged (OSF wiki or the repo CHANGELOG).

## Ethics without an IRB

Ranked. Take the highest you can reach.

1. Co-author with someone whose institutional committee can cover the protocol.
2. An Independent Ethics Committee. ICMR National Ethical Guidelines 2017, section 4.2.5, allow independent ECs for researchers with no institutional attachment, if the EC is a registered legal entity following national SOPs (registry: the DHR's NECRBHR or Naitik portal). Cost and turnaround are UNVERIFIED.
3. Minimal-risk studies with competent adults only, a documented self-review against an ICMR or Belmont-style checklist, informed consent, data minimisation, and the situation stated plainly in the paper. SIGCHI asks authors to confirm the appropriate approval process at their institution; CHI 2026 guidance recognises that environments vary and asks for a short note on context.

Under no route: minors, clinical populations, or deception without formal review.

### Data handling

Behave as if the DPDP obligations of May 2027 already apply: an itemised consent notice (purpose, data, how to withdraw, how to complain), purpose limitation, a retention schedule, a breach plan, and India-resident storage where feasible. The research exemption (Rule 16, Second Schedule) is conditional; participants and reviewers will judge the practice, not the exemption.

### Recruitment

General online samples: Prolific, pay at least £9 or $12 per hour, Nov 2025 attention-check rules (checklist item 9). Prolific's participant-country list does not include India (as of 2026), so Indian participants come from college networks, professional WhatsApp groups, a lab's own community, or commercial Indian panels (quotes seen in Oct 2026 ran ₹500 to ₹2,000 per session and up to ₹4,000 per hour for interviews; re-check before quoting). Academic pay norms in Indian HCI papers are UNVERIFIED; a defensible default is ₹300 to ₹500 for a 20 to 30 minute online task and ₹1,000 to ₹2,000 per hour in person, paid by UPI, stated before consent.

## Analysis decision tree

Mixed-effects first; one preregistered primary DV; everything else labelled exploratory.

1. Binary DV per trial (follow or reject, correct or incorrect): mixed-effects logistic regression with a participant random intercept, and an item intercept when items vary. Report odds ratios with 95% CI and marginal probabilities. `lme4::glmer`; in Python `pymer4` (wraps lme4) or `bambi` for Bayesian; `statsmodels.MixedLM` is linear only.
2. Continuous DV, repeated measures: linear mixed model (`lmer`, `statsmodels.MixedLM`), condition as fixed effect, participant random intercept, random slopes if they converge. Report standardised and unstandardised effect sizes with CIs; plot paired differences.
3. Two conditions, one measurement per participant, N under 40: paired or Welch t-test with bootstrap CI and Cohen's d or Hedges' g, plus a Bayes factor (`pingouin`, JASP) so "no evidence of difference" is interpretable.
4. Likert or ordinal DV: cumulative-link mixed model (`ordinal::clmm`, `brms` with `cumulative`), or at minimum medians with Wilcoxon and an effect size. ANOVA on a raw single Likert item is the one entry on this list that gets a paper rejected on its own.
5. Many DVs: one preregistered primary; Holm correction over the small secondary set; the rest exploratory and labelled.
6. Small N with a directional prior: Bayesian estimation (`brms`, JASP) with weakly informative priors; report posterior intervals and probability of direction.
7. Observational or platform data (forum posts, usage logs): propensity matching plus difference-in-differences, with the threats to validity written out.

Report every time: effect size with 95% CI, exact N per condition after exclusions, model formula, software and versions, data and code links. Figures reviewers trust: estimation plots of paired differences, per-participant lines across conditions, over- and under-reliance as two bars per condition, calibration curves. `tufte-viz` reviews them.

## The five pre-launch questions

Ask a collaborator or a reviewer before data collection.

1. What result would make you say the study was not worth running?
2. Which of our DVs would a sceptic say is contaminated by demand characteristics?
3. If the AI is right 70% of the time, what trivial strategy could a participant follow, and would our metrics catch it?
4. What is the smallest effect we would still care about, and does our N detect it?
5. Where will model drift break this in six months, and have we frozen enough to still be checkable?

## Venue rule

Dates as of Oct 2026; re-check before planning around them.

- Preliminary result, small N: CHI Poster (6 pages, non-archival, due 21 Jan 2027), an HCOMP Talk (1,500 words, June 2027), or a NeurIPS or ICLR human-AI workshop (non-archival).
- Complete preregistered study, modest scope: CHI short paper (5,000 words, September deadline) or CSCW rolling (no deadlines from CSCW 2027; decisions in 2 to 4 months).
- Replication of a 2025 finding under 2026 models or in an Indian sample: CSCW rolling or an HCOMP full paper (6,000 words). CHI's reviewing guide says constructive replication is valued.
- A position paper with no data: a NeurIPS or ICLR human-AI workshop. There is no alt.chi track; provocations go to Posters or workshops.

Post to arXiv after submission, not before, to limit de-anonymisation. Non-archival venues do not count as prior publication. Ship a reproducibility package every time: stimuli, prompts, model version and date, de-identified logs, analysis notebook, preregistration link, and a README that reruns the figures.

## Common mistakes engineers make

- Building the system before writing the research question and the DV.
- No control or baseline; comparing the new thing to nothing.
- Measuring satisfaction or self-reported trust instead of behaviour.
- Between-subjects with 10 people per cell, then reading noise as signal.
- Many DVs, one that "worked", no preregistration.
- Model version, prompts and stimuli not pinned, so the study cannot be rerun.
- Treating LLM output as the participant. Simulated users correlate with humans at about rho 0.7 on the best benchmark; that is a ceiling, not a licence.
- Thin related work.
- Overclaiming generality from one task, one model, one session.
- Consent, data handling and the ethics sentence left until the paper is due.
- Writing a spec (features, architecture) where the reader wants a finding (what changed, by how much, for whom, with what uncertainty).
- Posting the arXiv preprint before submission with the full author list.

### What convinces

Admissions readers and lab leads look for the same evidence: a question taken to a finished, honest artifact. In order of weight: a preregistered study with public materials and a short write-up (a rejected preprint with its reviews still shows the loop closed); a replication or extension of a 2025 result under 2026 models or in an Indian sample; an open tool or dataset others use (a reliance-study harness that freezes outputs, randomises, logs switches and exports an analysis-ready table); short, well-figured write-ups that state N, design, effect size, CI and limitations in the first screen; letters from people who watched you do the first three. Write claims sized to the evidence, limitations specific ("single-session, English-only, one model, 70/30 correctness ratio"), and prior work engaged by finding.

## Output

- The design document: the 17 checklist answers, the shape in three sentences, N with its arithmetic.
- The preregistration text with the human-AI extensions, and its link once posted.
- The analysis plan and, after data, the results in the reporting format above.
- The ethics sentence, consent notice and data-handling plan.
- The paper from `references/paper-skeleton.md` and the reproducibility package.

What takes over: `research-brief` for the related work; `customer-research` when step 1 ends in a formative interview study; `tufte-viz` for the figures; `unslop` on every draft; `mehul-voice` for anything that goes out under the user's name.
