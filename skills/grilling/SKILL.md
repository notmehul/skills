---
name: grilling
description: "Interview the user to a settled design, one round at a time. Use to stress-test a plan, decision, or architecture (\"grill me\", \"poke holes in this\"), and equally when an idea is still vague and the requirements are unstated (\"what if we built\", \"how should this work\"). Works a design tree: asks the whole answerable frontier each round with a recommendation per question, finds its own facts, and lands the result as a design before anything gets built."
---

Interview the user relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask _now_ without guessing at answers you haven't heard yet. Ask the whole frontier in one round: number each question and give your recommended answer. Then wait for the user's answers before the next round.

Each question should be formatted like so:

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>
```

Before you send a round, read your recommendations back. If every one follows the way the user already leans, the round is a mirror: add one question that carries the strongest grounded objection to that lean, in its best form, with the evidence that would settle it.

Each round the user answers reshapes the tree: settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a _later_ round, not this one.

Finding _facts_ is your job, never the user's. When a frontier question needs a fact from the environment (filesystem, tools, etc.), dispatch a sub-agent to find it; don't ask the user for anything you could look up yourself. Don't block on it: a running exploration is an unsettled prerequisite, so only the questions downstream of it wait for the sub-agent to report; ask the rest of the frontier now. The _decisions_ are the user's: put each to them and wait.

The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed. Do not act on it until the user confirms you have reached a shared understanding.

## Landing it

An empty frontier is not a design yet, it is a pile of settled answers. Read them back as one shape before anyone builds against it.

Present the design in sections of 200-300 words and stop after each to ask whether it holds. Cover the shape of the thing, its parts, how data moves, what happens when it fails, and how it gets verified. A section the user corrects reopens its branch of the tree: go back, re-ask, land it again.

Keep this in the conversation. A document is the exception, not the finish line, and writing one early buries the disagreement you were trying to surface. Write `docs/plans/YYYY-MM-DD-<topic>-design.md` only when the user asks for it, or when the work will outlive this session and someone else has to pick it up.
