---
name: launch
description: "Plan a launch or announcement for a product, an open-source release, a plugin, or an MCP server: the readiness gate, launch day, which directories and registries to list on, and the week after. Use on \"launch\", \"announce\", \"release post\", \"Product Hunt\", \"Show HN\", or \"list our MCP server\"."
---

# Launch

A launch borrows attention for a day or two. The plan turns that attention into something you own (users, an email list, a community, repo watchers who come back) and makes sure someone is there to answer everyone who shows up.

## 1. Size it

- A new product or major version gets the full plan below.
- An integration or notable feature gets one post, plus a note to the people it affects.
- Fixes go in the changelog.

## 2. Readiness gate

Check each item against the real thing, not the plan for it. Nothing launches until all of them pass.

- `docs/positioning.md` exists (product-marketing).
- The landing page or README passes ui-ux's public web page checks: first screen, raw HTML, `og:image`.
- Every launch line passes mehul-voice's "now you can" test, and a cold reader can say what it is.
- Install or signup works on a clean machine or in a private window, following only the public instructions.
- A demo of 60 to 90 seconds that passes remotion-best-practices' hook test.
- Attention has somewhere to land: an email capture, a waitlist, a Discord, or at minimum the repo's watch button and a clear first step.
- Someone is free all launch day to reply.

## 3. Channels

- **Owned:** your list, site, repo, community. Every other channel points back here.
- **Borrowed:** other people's audiences: a newsletter feature, a podcast, a co-launch with a tool you integrate with, a friend whose followers are the audience. Line these up two to three weeks ahead.
- **Rented:** X, LinkedIn, Reddit, Hacker News, Product Hunt. Pick the one or two where the audience actually is.

For directories and registries (MCP registries, dev-tool and startup directories), use [references/directories.md](references/directories.md). Write a separate description for each kind of surface. Lead with the outcome for founders, with technical depth for developer directories, and with the agent or MCP angle for registries. The same paragraph pasted everywhere reads as spam.

## 4. Launch day

- **Product Hunt,** if you use it: start two to three weeks early by joining in on other launches, set up the upcoming page, and prepare the gallery, the tagline and your first comment. Launch at 12:01am Pacific, Tuesday to Thursday. The first comment is yours: why you built it, what's different, what to try first. Reply to every comment quickly. Ask for feedback, never for upvotes, and never DM strangers.
- **Show HN,** only with a technical story: the architecture, a benchmark, a new approach. Post it as the builder and answer the hard questions straight.
- **Reddit,** only in communities where you already take part, and within each subreddit's rules on self-promotion.
- **Your own post** on X, LinkedIn or Substack, in mehul-voice.

## 5. The week after

- Day two: an honest recap with real numbers: what happened, what surprised you, what you'd change.
- Follow up with everyone who engaged, and move them to an owned channel.
- Put what people said, including their words and objections, into `docs/positioning.md`.
- Plan the next moment. Launches compound when updates keep coming.

## Output

A dated checklist from T-21 to T+7. Each item has an owner and a done-condition you can check.

Adapted from `launch` and `directory-submissions` in coreyhaines31/marketingskills (MIT). See `~/.agents/NOTICE-marketingskills.md`.
