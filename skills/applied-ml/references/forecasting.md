# Forecasting

Rolling-origin backtesting is the step people skip, and the one that decides the model. SeasonalNaive is always in the table. State of play as of Oct 2026.

## Backtest protocol

1. The decision cadence sets `h` (horizon) and `step_size` (how often you re-forecast). A weekly reorder means `h = 4 weeks`, `step_size = 1 week`.
2. `n_windows >= 8`, covering at least one full seasonal cycle; more when the series is noisy.
3. Candidates: SeasonalNaive, AutoETS, AutoTheta, mlforecast + LightGBM (lags, rolling means, calendar, known-future covariates), Chronos-2 zero-shot with the same covariates. `refit=False` for the cheap first pass, `refit=True` for the final run. `cross_validation(h, n_windows, step_size, refit=...)` in statsforecast and mlforecast; AutoGluon-TimeSeries 1.6 runs all three families under one `cross_validation` and wraps Chronos-2 with `fine_tune` and `known_covariates_names`.
4. Metrics: MASE and sMAPE for point forecasts; pinball loss or CRPS at the quantiles you will use (0.5, 0.9, 0.95 for service levels). Weight by SKU value when the business is value-weighted. Report error per horizon step; residual error on the training window is not forecast error.
5. Covariate hygiene: a feature at time *t* for horizon *t + k* uses only values known at *t*. Known-future covariates (price, promo, holiday) take the planned value, never the realised one. Stockouts censor demand: flag those days and impute or exclude them from the loss.
6. The winner beats SeasonalNaive on at least 70% of series and on the value-weighted aggregate. Otherwise ship SeasonalNaive and say so.
7. Hierarchies: reconcile (MinT or bottom-up) only after the base forecasts pass step 6.
8. Record per-window scores. A model that wins on average and loses the last three windows is drifting.

Done when the results table has one row per candidate including SeasonalNaive, one column per horizon step, and the per-window scores saved beside it.

## Models

All zero-shot capable. Licence decides what you can ship.

| Model | Date | Covariates | Licence |
| :--- | :--- | :--- | :--- |
| Chronos-2 | 17 Oct 2025 | Past and known-future, real and categorical; multivariate; cross-series | Apache-2.0 |
| TimesFM-2.5 | 15 Sep 2025 | Via external regressors | Apache-2.0 |
| TimesFM-3 | 31 Aug 2026 | Native multivariate and covariates | Weights non-commercial; commercial only through the vendor's cloud SQL product; code Apache-2.0 |
| Toto 2.0 | 19 May 2026 | Not stated | Apache-2.0 |
| TiRex-2 | 2026 | Multivariate and covariates, streaming | Apache-2.0 (a paid tier exists) |
| Moirai 2.0 | Nov 2025 | None | Not checked |

Chronos-2 is the open covariate-aware default. Covariate tasks are where it pulls ahead on fev-bench, because few other models use the covariates at all. TimesFM-3 claims the top of the leaderboards but its weights cannot ship in a client product.

Against GBDT: a Jul 2026 electrical-load benchmark put transformer foundation models 6.6 to 10.7% ahead of LightGBM with covariates, and a 2026 quick-commerce study found zero-shot models competitive on intermittent demand. No rigorous retail-demand head-to-head of fine-tuned Chronos-2 against tuned LightGBM and statsforecast was found as of Oct 2026. Run your own.

## Leakage on time-series benchmarks

Quoting a GIFT-Eval rank without its leakage column is a red flag. GIFT-Eval flags pretraining overlap per row; a 2026 comparison excluded Moirai-2.0 and TimesFM-2.5 for 28% and 10% overlap with fev-bench; the TIME benchmark (Feb 2026) exists to supply 50 fresh, leakage-free datasets. For your own evaluation data, ask whether a public dataset you are scoring on plausibly sits in a model's pretraining corpus, and say so in the brief.

## Tooling

statsforecast 2.1.1 (Jul 2026; conformal intervals, Numba dropped), mlforecast 1.1.0 (Jul 2026; conformal intervals, horizon-specific features), `chronos-forecasting`, or AutoGluon-TimeSeries 1.6 for all three under one API. Ship intervals, not points.
