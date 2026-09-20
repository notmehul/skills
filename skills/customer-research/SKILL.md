---
name: customer-research
description: "Find out what customers or users actually think: plan and run interviews or surveys, mine what they say in public (forums, reviews, issues, job posts), or turn transcripts and notes into themes with confidence levels. Use on \"customer research\", \"user interviews\", \"talk to users\", \"what do people think of X\", \"voice of customer\", \"why did they churn\", or before positioning, copy, or a product call that rests on assumptions about users."
---

# Customer research

Research exists to prove you wrong early and cheaply. Go in trying to break your assumptions; if you only look for confirmation you'll find it, and it'll be worthless.

## 1. Write the assumptions down

List the three to five beliefs the work rests on. Next to each, write the answer that would prove it wrong. If none of your questions could return that answer, rewrite the questions. Done when every assumption has a way to fail.

## 2. Pick the mode

- **Analyze what already exists:** transcripts, call notes, support threads, reviews, survey results.
- **Mine public sources:** where the audience already talks. See [references/sources.md](references/sources.md).
- **Ask directly:** interviews, then surveys.

Mining usually comes before asking, because it tells you what to ask and in whose words. Don't let it stall you, though: if you can talk to five users this week, talk to them.

## 3. Interviews

- Recruit the people you want more of: the ones who got it fast, stayed, or paid the most, not whoever replies first. Close every call with "who else should I talk to?"
- Keep it a conversation, not a study. Don't pitch, and don't defend the product.
- Ask about past behaviour, not opinions or intentions (the Mom Test): "tell me about the last time you…", "what did you try before?", "what did that cost you?". "Would you use…" gets polite lies.
- Ask why three to five times, until you hit the outcome or feeling underneath the first answer.
- Capture their exact words: record with permission, or write the quotes down verbatim.
- Aim for ten conversations; themes usually start repeating by five. If they aren't already users, offer something for their time.

## 4. Surveys

Keep them short. Open questions beat multiple choice for language, and a leading question returns the answer it asked for. For product-market fit, ask Sean Ellis's question, "How would you feel if you could no longer use <product>?" (very / somewhat / not disappointed), then "what's the main benefit you get?" and "who would benefit most?". Analyze the "very disappointed" group separately. Ellis's own rule of thumb is 40% "very disappointed".

## 5. Synthesis

From each source, extract:
- the job they're trying to get done
- pains, with unprompted and emotional ones first
- the trigger that made them look
- the outcome they want, in their words
- the alternatives they tried, including doing nothing
- their exact phrases

Cluster these into themes and label each one:
- **High:** three or more independent sources, raised unprompted, consistent across segments.
- **Medium:** two sources, or only when prompted, or only in one segment.
- **Low:** a single source.

References a founder hand-picked count as prompted. Name the sample's bias: reviews skew to strong opinions, support threads to problems, Reddit and HN to skeptical technical users. Flag contradictions, where people say one thing and do another.

## Output

Agree with the user which one they need:
- a synthesis of themes, confidence levels and quotes
- a quote bank by theme, which feeds "In their words" in `docs/positioning.md`
- a gap list: what we still don't know and how to find out

Every quote carries its source and date.

Adapted from `customer-research` in coreyhaines31/marketingskills (MIT). See `~/.agents/NOTICE-marketingskills.md`.
