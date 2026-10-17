# Prompt injection: the design checklist and a red-team afternoon

The vendor position hardened in 2026 (Anthropic, Google and OpenAI alike): the defence is architecture, not the model or a classifier. Anthropic's own containment post (May 2026) names the environment layer as primary, and the Aug 2026 auto-mode bypass was answered with "working as designed". A classifier is a bonus layer; the boundary is the sandbox, the allow list and the confirmation step.

## Design checklist, per agent

- [ ] Which of the three legs does this session hold: private data, untrusted content, an outbound channel or state change? If all three, split the session or gate the third behind confirmation.
- [ ] The tool allow list is decided before any untrusted content is read; read-only variants exist for every tool where possible.
- [ ] Every state-changing tool call is a proposal row; the confirmation screen shows the diff, never a summary the agent wrote.
- [ ] Unattended runs live in a container or VM with an egress allow list (each allowed domain is a capability), no credentials in the sandbox, no home-directory mounts.
- [ ] Tool outputs and fetched pages are data: strip or quarantine text that looks like instructions; a fetched archive is never the working directory of an interpreter (a planted `struct.py` runs on import).
- [ ] Auto-approve or YOLO permission modes never run on a machine with real credentials.
- [ ] Every tool decision is logged with its source so approval fatigue can be audited. A human approval rate above 90% means the prompts are noise and the boundary has to move into the sandbox.

## Red-team afternoon

About three hours with promptfoo (MIT, local; attack generation defaults to OpenAI since the Mar 2026 acquisition announcement, so set a custom attack provider if that matters).

1. `promptfoo redteam init --no-gui`; the target is your HTTP endpoint or Python entry point; write a one-paragraph `purpose`.
2. Pick 5 to 8 plugins mapped to your real risks (indirect injection through tool output, personal-data leak, excessive agency or tool misuse, system-prompt leak, policy violation) and 2 strategies (basic, one multi-turn).
3. `promptfoo redteam run`, then `report`. Triage: every success becomes a golden-set case with a code grader ("tool X must not be called when the input contains Y").
4. Re-run the same config monthly and after any tool or model change; keep the `label` constant so runs compare.
5. Manual pass: five hand-written indirect injections planted in the real data sources (a PDF, a web page, a database row, an email, a subagent's output). For a document-extraction agent, one of them sits inside a scanned bank statement.

Model-layer numbers exist (Anthropic reported about 0.1% single-attempt and 5 to 6% after 100 adaptive attempts for one model on an agent red-teaming benchmark, as of Oct 2026) but they are context-bound and do not replace the checklist. Deep agent exercises in an isolated environment with state assertions are a job for Inspect AI, not promptfoo.
