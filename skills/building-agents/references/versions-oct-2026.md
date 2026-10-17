# Pinned versions, read 17 Oct 2026

Record the version and this date in the project. Re-check the package index before upgrading; most of these frameworks crossed a major version between April and October 2026, and samples older than June 2026 do not run unchanged.

| Package or spec | Version |
| :--- | :--- |
| `pydantic-ai` | 2.57.0 |
| `claude-agent-sdk` (Python) | 0.2.168, CLI 2.1.301 |
| `@anthropic-ai/claude-agent-sdk` | 0.3.302 |
| `openai-agents` | 0.24.0 |
| `langgraph` | 1.2.16 |
| `google-adk` | 2.12.0 |
| `crewai` | 1.15.28 |
| `dspy` | 3.3.1 |
| `smolagents` | 1.26.0 (no release since 29 May 2026) |
| `@mastra/core` | 1.73.0 |
| `ai` (Vercel AI SDK) | 7.x |
| Restate | 1.8.0 |
| Inngest | 1.46.0 |
| Hatchet | 0.110.x |
| DBOS Transact Go | 1.6.0 |
| MCP spec | 2026-07-28 (stateless, Streamable HTTP; sampling and roots dropped) |
| A2A | 1.0 |
| Agent Skills spec | agentskills.io; frontmatter keys `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools` |

Model-line changes that break agent code on the current Anthropic models, as of Oct 2026: forced `tool_choice` (`any` or a named tool) returns 400 on Opus 5.5, Sonnet 5.5 and Fable 5.1, so get JSON through the provider's structured-output parameter or strict tools with `auto`; thinking cannot be disabled on Opus 5.5 (use `effort`); `budget_tokens`, `temperature`, `top_p`, `top_k` and prefill are rejected on Haiku 5.5. Re-check the model docs before quoting any of these.
