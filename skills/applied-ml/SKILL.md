---
name: applied-ml
description: "Train or choose a model for a business prediction: churn, lead scoring, demand forecast, fraud, segmentation, uplift. Use on 'train a model', 'which model', 'forecast', an A/B test or 'did it work', or before a model number reaches a decision maker."
license: MIT
metadata:
  version: "1"
  updated: "2026-10-18"
  harnesses: "claude-code codex opencode"
  source: "research-2026-10/applied-ml.md (17 Oct 2026); research-2026-10/evals-observability.md A5, D14 (17 Oct 2026)"
---

# Applied ML

Agents are good at the loop between decisions; humans still own the decisions: what to predict, which split mirrors deployment, which feature is leakage dressed as signal, which metric and threshold the business acts on, and whether to ship. This skill carries those decisions as checklists so the loop runs against a plan instead of a hunch. Every number, version and licence here is as of Oct 2026.

Read `references/problem-map.md` when the problem is not a plain classification or regression on one table (recommendation, search, segmentation, anomaly, text). Read `references/forecasting.md` when the target is a series over time. Read `references/experiments.md` when the question is "did it work" or "who should get the treatment". Read `references/stack.md` when setting up the environment or pinning versions.

## The first two hours

Time boxes: 20 minutes framing, 30 minutes inventory and split, 40 minutes ladder, 30 minutes audit and brief.

1. **Write the prediction sentence** before opening the data: "At time *t*, for each *unit*, predict *target* over *window*, to drive *decision*, judged by *business metric*." Done when every blank is filled in words the sponsor agrees with. A blank you cannot fill is a question for the human, not a guess.
2. **Inventory the data** with DuckDB over the raw files: row grain, time column, unit key, target definition and its prevalence, and the timestamp at which each feature becomes available. Done when `data/README.md` holds all five.
3. **Choose the split** with the rules under "Split design" and freeze it: code that returns ids, ids saved to `splits/*.parquet`, split hash logged. Done when every later experiment loads those ids and nothing re-splits.
4. **Run the baseline ladder** (below), one MLflow run per rung on the frozen split, wall time recorded. Done when rungs 0 to 2 exist.
5. **Run the leakage checklist** against the rung-2 feature importances. Done when each of the top five features has a one-line "known at *t* because ..." note.
6. **One diagnostic plot per model**: calibration (classification) or residual against prediction (regression), plus lift at the top-k the business will act on. `tufte-viz` owns how the plot reads.
7. **Write the brief**, at most one page: the prediction sentence, the inventory, the split and why, the ladder table, the leakage notes, the one number the business will see, and the next experiment. Done when the human has read it. Tuning waits for that.

## The baseline ladder

Run in order. Each rung beats the previous on the frozen validation split or carries a sentence explaining why not.

| Rung | Classification | Regression | Forecasting |
| :--- | :--- | :--- | :--- |
| 0 | Majority class or prevalence | Mean or median | SeasonalNaive, Naive |
| 1 | Logistic regression, at most 5 hand-picked features | Ridge, at most 5 features | AutoETS or AutoTheta (statsforecast) |
| 2 | LightGBM defaults, every feature available at *t* | LightGBM defaults | mlforecast + LightGBM with lags and calendar |
| 3 | TabICLv2 (up to ~100K rows) or TabPFN via API | TabICL regressor | Chronos-2 zero-shot with covariates |
| 4 | Tuned GBDT (at most 50 Optuna trials) or an ensemble | Same | Fine-tuned Chronos-2 or an ensemble of 2 to 3 |

Rules: rung 2 exists before any rung 3 or 4 claim. Every results table shows rung 0 and rung 2 beside the winner. When rung 3 beats rung 2 by less than rung 2's seed-to-seed spread, call it a tie and ship rung 2.

## GBDT or tabular foundation model

Tabular foundation models (TFMs) top the i.i.d. benchmarks as of Oct 2026 and lose ground under temporal or grouped splits. Decide by your backtest under your split, never by a leaderboard rank; the 2026 meta-feature study found no dataset rule that beats a simple default.

```
rows <= 100K, features <= 500, i.i.d. split
    -> run TabICLv2 and LightGBM; pick by frozen-split metric. Expect the TFM to win.
rows <= 100K, temporal or grouped split
    -> tuned LightGBM or CatBoost is the default; try TabICLv2 with the group id as a
       categorical feature; trust the TFM only when it wins on every backtest fold.
100K < rows <= 1M
    -> LightGBM first. TabPFN-3 or 3.5 via API when licence and budget allow and the gap matters.
rows > 1M, or latency under 10 ms, or CPU-only serving
    -> GBDT. When a TFM won offline, distil it into XGBoost or CatBoost on out-of-fold soft
       labels and verify the student on the frozen split.
commercial product or client-side deployment
    -> TabICLv2 or GBDT.
want a ceiling estimate and have an hour
    -> AutoGluon "best" preset once, as the reference number; say whether the preset used
       non-commercial models before quoting it.
```

Licence caveat: TabICLv2 (Feb 2026) ships BSD-3 weights and is the open default. TabPFN-3 and 3.5 (May and Sep 2026) have Apache-2.0 code but non-commercial, non-production weights, and the vendor's FAQ counts internal evaluation that influences a commercial decision as commercial use; reach them through the API or a paid licence. Every shipped artifact names its licence in the model card.

## Split design

Decide once, write it down, and have every experiment load the same ids.

- **Random k-fold** only when rows are exchangeable and nothing about deployment is time-ordered. Rare in business data.
- **Time-based holdout** when the model scores future rows: train up to T0, validate (T0, T1], test (T1, T2], with a gap of one label window between train and validation so no label leaks backwards.
- **Group k-fold** when units repeat (customer, store, document source): group by the unit that will be new at deployment.
- **Rolling origin** for forecasts (`references/forecasting.md`).
- Report the metric's spread across folds or seeds. A single number is not a result.

## Leakage checklist

Run before trusting any number, and again before the brief.

Target leakage
- Any feature computed from data after prediction time *t*? ("to date" aggregates, status fields, "last contact" dates)
- Any feature a proxy for the label? (cancellation reason, refund amount, a second churn flag)
- Rows filtered on the outcome? (only customers with a purchase in the window)
- Right-censored units labelled as negatives?

Train and test contamination
- Scalers, encoders, imputers or target encoders fit on the full data? Fit inside the pipeline, per fold.
- Duplicates or near-duplicates straddling the split? (same customer, same document, resampled series)
- Any group in both train and test? Any training row later than a validation row?

Availability leakage
- Will every feature exist at serving time with the same freshness? (ETL lag, late-arriving events)
- Any feature derived from a system that reads the model's own output?

Evaluation leakage
- Test set touched more than once? It is a validation set now.
- Model selection done on the split reported as test?
- Forecasting foundation model whose pretraining corpus plausibly includes your evaluation data?

Red flags that usually mean leakage: AUC above 0.95 on a behavioural problem; one feature with over half the importance; validation better than training; a date-derived feature at the top; a score far above chance on shuffled targets.

## When to stop tuning

Stop when any of these holds:

1. The gain over the last 20 trials is smaller than the fold-to-fold standard deviation of the metric.
2. You have spent more than three times rung 2's wall time for under 2% relative gain.
3. The gain changes no business decision: same top-k, same reorder quantity, same threshold crossings.
4. The next idea is a feature that fails the leakage checklist.
5. Calibration or stability across windows got worse while the headline metric improved.

Budget: at most 50 Optuna trials for a GBDT; no tuning on a TFM beyond estimator count or context length. Spend the saved time on error analysis: slice validation by segment, time and source, and find the worst slice.

## LLM or trained model

For classification and extraction.

- **Trained model** when: around 500 or more labelled examples (50 or more per class), a fixed label set, volume above ~10K items a month, latency under a second, retraining as behaviour drifts, or the output must be a calibrated probability.
- **LLM** when: under ~200 labels, a taxonomy still moving, the task needs reading comprehension or multi-field extraction, low volume, or an explanation per item.
- **Hybrid**, the common case: the LLM labels a seed set, a human corrects 10%, embeddings plus logistic regression (or a small fine-tune) serve at volume, the LLM takes the low-confidence tail and new categories. Keep a 200-item gold set the LLM never saw and score both on it.
- An LLM is never the scorer for churn, credit or fraud at volume. Use it to label intent from tickets and call notes and feed that as a feature; use it to draft the causal DAG; use it to explain a flagged case. `knowledge-and-extraction` owns the document-extraction build; `llm-evals` owns judging an LLM.

## Ship checklist and model card

One markdown page per shipped model, in the repo.

- Prediction sentence, owner, date, data range used.
- Split design and why; the metric table with rung 0, rung 2 and the shipped model, with fold or seed spread.
- Calibration plot or interval coverage at the operating point. The threshold comes from the cost matrix in rupees, tuned on held-out data (`references/experiments.md`), never 0.5 by default.
- Leakage checklist outcome, naming the two or three features you were least sure about.
- Known failure slices: worst segment, worst time window.
- Serving: input schema (pandera), latency, fallback (rung 0 or rung 2).
- Monitoring: the three numbers watched weekly (input drift on the top features, score distribution, realised metric once labels arrive) and the retrain trigger. Re-calibrate after any change in class prior.
- Every prediction logged with its features and a decision id: the event row. A score that changes a decision about a person is a proposal to a named human until `ai-governance` says otherwise.
- Licence of every model artifact.

## Operating rules for the agent

- `PLAN.md` first: prediction sentence, split, ladder, stop rule. The human approves; the agent executes.
- A lab notebook, one row per experiment: hypothesis, change, metric with spread, decision. Append only. `show-me-your-work` owns the trail format when a reviewer needs it.
- The eval script is locked. The agent edits training code and features, never the split or the scorer.
- One MLflow run per experiment with split hash, git sha, seed and wall time. The agent reports the run id; the human reads the table.
- The agent does not touch the test set. A test-set number in the log before the final run means the split is regenerated.
- Each experiment has a wall-time budget; one that overruns is killed and logged as such.
- "Done" is answered with rung 0 and rung 2 beside the result, the fold spread, and the leakage checklist. Anything less is premature completion.
- marimo notebooks for exploration; promote a cell to `src/` once it is reused twice; `marimo check` in CI.

## Output

- `PLAN.md`, `data/README.md`, the frozen split ids, the MLflow table with rung 0 and rung 2.
- The one-page brief after the first two hours, and the model card at ship time.
- The leakage checklist with its answers.

What takes over: `data-analysis` for the decision table the business reads; `llm-evals` when the model under test is an LLM; `pilot-rollout` to put the model in front of operators; `ai-governance` when the score touches a customer or decides about a person; `tufte-viz` for every chart; `prove-it-works` before declaring done.
