# Cost per completed task

The unit is cost per completed task, never cost per call. Agents re-read their growing context on every turn, so input tokens dominate and an agent loop costs 4 to 30 times what a single chat turn costs.

## Worksheet

```
tokens_in per attempt (system prompt + retrieved context + tool results + history) = ____
tokens_out per attempt = ____
attempts per task (retries, agent turns) = ____
cache-hit share of input = ____        (cached input bills at roughly 0.05 to 0.1 x list price)
model price in / out per million tokens = ____ / ____
success rate on the eval set = ____
human review minutes per task x loaded cost per minute = ____
cleanup cost per escaped error x escape rate = ____

cost per completed task = (token cost per attempt x attempts) / success rate + review cost + cleanup cost
monthly = cost per task x volume; compare with today's minutes per item x loaded cost
```

Levers, in order of effect: shorter context and prompt caching; route easy cases to the cheap tier behind a confidence check; batch anything not latency-bound (about half price); fewer agent turns through better tools; the frontier model only on the hard tail.

## Reference prices, read 17 Oct 2026

USD per million tokens, input / output. Re-check the vendor page before quoting; model names and prices change monthly.

| Vendor | Frontier | Mid | Cheap | Notes |
| :--- | :--- | :--- | :--- | :--- |
| Anthropic | Fable 5.1 10 / 50 | Opus 5.5 4 / 20; Sonnet 5.5 2 / 10 | Haiku 5.5 0.10 / 0.50 (up to 100K context) | Batch half price; US-only inference 1.1x; web search $10 per 1,000 |
| OpenAI | gpt-6-astra 10 / 50 | gpt-6.1-sol 2 / 10; gpt-5.6-sol 4 / 20 | gpt-6-luna 0.10 / 0.50 | Batch and Flex half price; residency endpoints +10% |
| Google | gemini-3.1-pro-preview 2 / 12 | gemini-4-argon 2 / 10, doubles 1 Dec 2026 | gemini-3.8-flash 0.75 / 3.75, doubles 1 Jan 2027; 2.5-flash-lite 0.10 / 0.40 | Batch half price; the unpaid tier trains on your data |

Rule for a budget: model it at today's price and at the announced 2027 price, and present the higher one. Default to the mid tier; the frontier tier only where the task's hourly value justifies it.
