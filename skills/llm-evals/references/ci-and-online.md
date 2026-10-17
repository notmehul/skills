# CI gate, online tiers, A/B rules and budgets

## Regression suite in CI

Generic recipe, pytest or any test runner:

- Dataset: 100 or more cases from core features, past bugs and edge cases, with the held-out slice never used in prompt iteration. Keep cases as JSONL in the repo and graders as plain callables, so cases, graders and results live in git and in the normal test runner.
- PR job: code assertions and outcome checks only; 1 run per case; fail when pass-all drops below the last green minus the measured noise; pin model ids through environment variables so a model rollout cannot pass as a regression.
- Nightly job: the full suite including model judges, 3 runs per case, a cost ceiling, scores written to the trace backend as an experiment; open an issue when the lower confidence bound crosses the bar.
- Every production failure that gets fixed adds a case in the same PR.

Tooling defaults as of Oct 2026: pytest plus pydantic-evals (OTel-native) for the harness in code; Langfuse self-hosted (MIT core, fed over OTLP) as the system of record for traces, scores and datasets, with its `experiment-action` as a PR gate that shows passed, regressed and failed-to-run; Phoenix as the lighter single-container alternative when running Langfuse's four services is too much for one person. Run one of them, never both. DeepEval is the richer metric library if you want prebuilt agent metrics; pin it, since v4.2.0 (Aug 2026) inverted the direction of its Bias, Hallucination, Misuse and Toxicity metrics and old thresholds silently flip.

### Claude Code

For a skill or plugin shipped to Claude Code, `claude plugin eval` measures the plugin's delta over a no-plugin baseline:

```
claude plugin eval . --model <pinned-id> --judge-model sonnet \
  --threshold 0.8 --runs 3 --max-cost-usd 5 --trust-plugin --json results.json
```

- Exit 1 means a case fell under the threshold; exit 2 means the cost ceiling was hit with partial results.
- Graders `regex`, `tool_used`, `tool_order` and `file_exists` are free; `llm` and `baseline` cost three judge calls per run. Use `regex` over a file for long outputs and keep `llm` for short replies with PASS or FAIL rubrics.
- Read the delta (with plugin minus without). A delta near zero with `tool_used: Skill` failing means the skill is not triggering on natural phrasing: fix the description, not the body.
- `--ablation none` halves cost while iterating on graders; restore the baseline before merging.
- MCP servers are mocked by default; `--allow-tools` only what the case needs.
- Apply the afternoon loop's first three steps before accepting any proposed cases, and split a bundled grader into one check per failure mode. The `evals/evals.json` format from skill-creator and the `evals/<case>/` format from plugin eval do not read each other; pick plugin eval for anything you gate.

## Online evals and sampling

- Tier 0, every trace, synchronous, in code: schema valid, forbidden tools absent, a confirmation preceded every write that is not classed audit-tier, personal-data scan on outbound text, cost and latency under budget. A failure writes an event row with `severity`.
- Tier 1, every trace, asynchronous, cheap: rule-based quality flags (empty answer, refusal, truncation, retry count).
- Tier 2, sampled, nightly: model judges per failure mode on a stratified sample. Start at 5 to 10% or 200 traces a day, whichever is smaller; stratify by route and tool; always include a random slice so unknown unknowns still show up.
- Report with confidence intervals and alert on the lower bound, never the point estimate. Every judged failure joins the golden-set candidate queue.
- Humans: 10 to 20 outlier traces a week read by the domain owner, who also settles quality disputes.
- A synchronous model judge never sits in the request path. Guardrails are inline, fast and deterministic (schema, allow-listed tools, personal-data and secret scan); evaluators run after the fact and do not block.

## Prompt A/B rules

1. Offline first: both variants on the full golden set, 3 runs, the same pinned model. Ship nothing whose gain sits inside the noise band.
2. Shadow second: run the challenger on live inputs without serving it; compare judge scores and cost.
3. Live split last, and only for metrics the offline set cannot measure (acceptance of proposals, edit distance after confirmation). Split by a stable unit (user or account), pre-register the metric and the stopping rule, and log `prompt_version` on every event row.
4. One change per experiment. A prompt change and a model change in the same run teach you nothing.
5. Keep the loser's prompt and results; prompts are versioned artefacts.

## Cost and latency budgets

- Per task type define `max_cost_usd`, p50 and p95 latency, `max_steps` and `max_tool_calls`. Store them next to the eval set and assert them in Tier 0.
- Report cost per successful task. A vendor example went from 4.6 cents at 74% to about 1 cent at 98.9% on a 44-ticket bench (vendor numbers, as of Oct 2026; the metric is what to copy).
- Prompt-cache awareness: changing the structured-output schema or the tool set invalidates the prompt cache and, on the Claude API, the grammar cache. Batch schema changes.
- Judge budget: phase out judges that keep passing, prefer code checks on every PR, run judges nightly on samples.
- One monitor for cost, quality and latency spikes, alerting on the same event rows.
