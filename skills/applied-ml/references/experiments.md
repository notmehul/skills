# Experiments: did it work, and who should get it

Read when the question is an effect (A/B test, campaign, pricing change, geo test), when a model will choose who gets a treatment, or when a classifier's threshold is being set. Library versions as of Oct 2026.

## Steps

1. **Ask how treatment was assigned.** Randomised: go to step 3. Not randomised: step 2. The answer to this question decides everything after it.
2. **Observational.** Draw the DAG (DoWhy), list confounders, pick the estimand. Estimate with double ML or doubly robust (EconML). Run the DoWhy refuters: placebo treatment, random common cause, data subset. A failed refuter means the report says "not identifiable with this data". Done when identify, estimate and refute each have a line in the write-up.
3. **Randomised, average effect.**
   - Pre-register before looking: the primary metric, the unit of randomisation, the sample size or run length, the stopping rule, the guardrail metrics. Written down, dated.
   - Power and MDE: from the baseline rate or variance, alpha and power, compute the sample per arm for the effect you care about, or the minimum detectable effect at the sample you will get. Put the MDE in the pre-registration; an underpowered test is decided before it starts.
   - SRM check first: compare assignment counts against the planned ratio with a chi-square test before reading any outcome. A mismatch means the assignment is broken; stop and fix it.
   - Estimate: difference in means with a confidence interval. CUPED when a pre-period covariate exists. No peeking without a sequential rule.
   Done when the pre-registration, the SRM result and the estimate with its interval sit in one document.
4. **Randomised, who to target.** S-learner and T-learner with LightGBM base learners; X-learner when arms are unbalanced; causal forest when you need per-unit intervals. Evaluate on a held-out randomised set with Qini and AUUC together, plus realised uplift at the top-k you will target. Done when both curves and their rank agreement are in the table.
5. **Geo, when units cannot be randomised.** At least 20 units with at least 12 months of pre-period. Synthetic control (CausalPy) with placebo-in-space and placebo-in-time checks. Power-simulate market selection before spending. Vendor guidance for small advertisers (2 to 6 week tests, 15 to 30% spend change in test markets) is a vendor estimate.
6. **Report the effect**: point estimate with its interval, the assumptions in one sentence each, what would falsify it, and the business number it implies. An estimate under assumptions is said to be one.

## Rules

- Qini is never the sole selector. UpliftBench (Aug 2026) found Qini nearly uncorrelated with true effect accuracy on one benchmark while AUUC did better. Report both, their rank agreement, and bootstrap by independent unit. Definitions differ across libraries (prefix-mean AUUC and others), so name the one you used. Sanity check: the top-scored bucket shows higher realised uplift than the lower ones.
- The S-learner is a fine default. On a public 14-million-row ad-uplift dataset (Apr 2026 paper, single author, single dataset) S-learner with LightGBM beat T-, X-learner and causal forest on Qini, and top-20% targeting captured about 78% of incremental conversions.
- The LLM drafts the DAG and lists confounders you forgot. It never estimates the effect.
- Past this (instrumental variables, structural models) book an economist for a week.

## Threshold and calibration for a classifier

- The threshold is a business decision. Write the 2x2 cost matrix in rupees first. Tune the cut-off on held-out folds against that matrix with scikit-learn's `TunedThresholdClassifierCV`; apply a known threshold with `FixedThresholdClassifier(FrozenEstimator(...))`. Never tune on training data.
- Ranked lists (who to call first): precision@k or lift at the capacity you have.
- Probabilities shown to humans or used in expected-value arithmetic: calibration curve plus Brier, with the calibrator fit on data the model did not train on (`CalibratedClassifierCV`). Sigmoid for small samples, isotonic above ~1,000, temperature scaling for multiclass logits. Calibration breaks under label shift: recheck after any change in class prior.
- Treatment decisions (discount, outreach): uplift on a randomised holdout, per the rules above.

## The decision table

Report to the business in one table, not a metric: at threshold *t*, we flag or approve *N* per week, miss *M*, spend ₹X on false positives and save ₹Y, on *W* weeks of data. `data-analysis` carries the same table for non-model questions.

## Libraries

DoWhy 0.14; EconML 0.17.0 (Jul 2026); CausalML 0.18.0 (Oct 2026, Python 3.11 or later); CausalPy 0.9.0 (Jul 2026; the 1.0 release moves to PyMC 6 and breaks, so pin). GeoLift remains an R package; CausalPy tracks parity in an open issue. Pin all four.
