# Stack for one builder

Versions read 17 Oct 2026. Re-check before pinning; several of these moved in the last 30 days. One `pyproject.toml`, one `uv.lock`, PEP 723 inline deps for one-off scripts.

| Layer | Choice | Version, Oct 2026 | Note |
| :--- | :--- | :--- | :--- |
| Environment | uv | 0.12.20 | `uv run`, lockfile, PEP 723 scripts. |
| Dataframes | Polars, pinned `<2` | 2.0 released 6 Oct 2026 | 2.0 makes the streaming engine default, stops guaranteeing row order on join, group_by and unpivot, and tightens dtypes. Stay on 1.x until the pipeline is tested; add `maintain_order=True` where order matters; then upgrade deliberately. pandas only where a library demands it (scikit-learn reads both through narwhals). |
| SQL, local warehouse | DuckDB | 1.5.6 | Reads Parquet, CSV and Postgres directly. Use it for the data inventory and anything over memory. |
| Notebooks | marimo | 0.25.1 | Plain `.py`, diffable, agent-editable; `marimo check` as a CI gate; `marimo pair` and an agent-facing CLI put the agent in a live kernel. Jupyter only when collaborators expect `.ipynb`. Promote a cell to `src/` once reused twice. |
| Core ML | scikit-learn | 1.9.1 | `metrics.metric_at_thresholds`, experimental callbacks, narwhals for Polars I/O. Deprecated: `SVC(probability=)` (use `CalibratedClassifierCV`), `TargetEncoder(shuffle, random_state)`, `friedman_mse`. |
| GBDT | LightGBM first, CatBoost when categoricals dominate | LightGBM 4.7.0, CatBoost 1.2.10, XGBoost 3.4.2 | LightGBM for speed and native categoricals. XGBoost or CatBoost as the distillation student. |
| Tabular foundation models | `tabicl` | TabICLv2, BSD-3 | `tabpfn-client` only when the API is acceptable to the client; TabPFN-3 and 3.5 weights are non-commercial. |
| Forecasting | statsforecast, mlforecast, `chronos-forecasting` | 2.1.1, 1.1.0 | Or AutoGluon-TimeSeries 1.6 for all three under one `cross_validation`. |
| Causal | dowhy, econml, causalml, causalpy | 0.14, 0.17.0, 0.18.0, 0.9.0 | Pin. CausalML needs Python 3.11 or later; CausalPy 1.0 breaks on PyMC 6. |
| Validation | pandera | 0.34.1 | Schemas at ingestion and at the model boundary; Polars and pyarrow supported. Great Expectations Cloud was withdrawn 1 Jun 2026; GX Core survives under new stewardship, still without native Polars. |
| Uncertainty | MAPIE | 1.1.0 | v1 API: `fit`, `conformalize`, `confidence_level`. Or the native conformal intervals in statsforecast and mlforecast. Ship intervals, not points. |
| Tracking | MLflow, local | 3.17.0 | SQLite backend and `./mlruns` is enough for one person; the client's data stays on the laptop. 3.14 and later also trace the coding agent that ran the experiment. |
| Serving | FastAPI + uvicorn | | Modal for bursty or GPU work with no ops; BentoML when packaging several evolving models. Distilled GBDT or ONNX for latency. |
| Feature store | None | | Every 2026 guide says skip it below ~3 models or 2 teams. A versioned SQL or Python feature module is the middle ground. |
| Orchestration | `make` or `just` plus cron | | Until there are three live models. |

Why these: each is the maintained default of its category or the only open-licensed option that competes. Polars, DuckDB and marimo are text-first and local, so the agent reads and edits the artifacts directly. MLflow over a hosted tracker because self-hosted.

Do not adopt yet (Oct 2026): TimesFM-3 or TabPFN-3.5 weights in anything a client runs (licence); LLM rerankers in recommendation (cost, mixed evidence); fully autonomous AutoML agents on client data (self-reported benchmark numbers on a small split).
