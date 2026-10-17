---
name: pitching
description: "Build, review or deliver a pitch with Oren Klaff's Pitch Anything method. Use on 'help me pitch', 'review my pitch', a deck narrative, a proposal or sales email, a meeting with investors or buyers, or pushback in a negotiation."
license: MIT
metadata:
  version: "1"
  updated: "2026-10-18"
  harnesses: "claude-code codex opencode"
  source: "alexanderSolod/skill-library pitch-builder, pitch-review, frame-control (MIT); merged Oct 2026"
---

# Pitching

Three branches on one mechanism: build a pitch, review one, handle the room. Klaff's model, which this skill takes as a working frame rather than settled science: a pitch is written by the pitcher's neocortex (logic, data) and received by the listener's croc brain (survival, emotion, short attention), which filters most of the message out before the analytical mind sees it. So the work is frame, tension and status first, and the numbers second, as justification for a decision the listener has already made. The method holds that attention lasts about 20 minutes, so no pitch runs longer.

## The frame primer

A frame is the mental structure a person brings to an encounter. When two meet, their frames collide and only one survives; the winning frame governs the interaction. You hold the frame when the other side is reacting to you. If you are explaining your authority, credentials or advantage, you do not hold it, and rational appeals never win a frame collision.

| They bring | It looks like | Counter |
| :--- | :--- | :--- |
| Power frame | Arrogance, making you wait, checking the phone, changing the agenda | Small denial or defiance with humour ("I only have 15 minutes." "That's okay, I only have 12."), then move the meeting in your direction |
| Time frame | Attention fading, "let's wrap up" | End it first, on your clock. Never speed up to cram more in |
| Analyst frame | Line-by-line numbers, spreadsheet demands | One high-level figure, "you can verify later", then the intrigue story. In Klaff's terms, hot and cold cognition do not run at the same time |

The prize frame counters all three: you are the prize, money is a commodity available in a thousand places, and the other side qualifies to you ("I'm picky about who I work with. Tell me why we'd enjoy working with you").

The intrigue story is prepared once and reused: you at the centre, risk and a ticking clock, a force blocking you, serious consequences, and the ending withheld until the business is done.

Neediness is the deal killer: any sentence that asks the listener to validate you. The anti-neediness formula is want nothing, show one thing you do well, then withdraw when they expect you to chase.

## Golden rules

1. Humour and fun are not optional. Defiance without humour is hostile; defiance with humour is attractive.
2. Plough forward. Never stop, never show self-doubt, never circle back.
3. Frame control is won or lost before the pitch starts.
4. If you are explaining your authority, you have already lost the frame.
5. Hot cognitions beat cold. People decide with emotion and justify with logic.
6. Novelty is oxygen. The brain stops attending to anything it thinks it already understands.
7. Always Be Leaving, never Always Be Closing.
8. The person is the deliverable. People invest in people.
9. It is a game, and when both sides know the game is on it is fun for everyone.

## Branch 1: build a pitch

Read `references/build.md` for the phase scripts, the tension-loop library and the hot-cognition stack.

1. **Pin the context**: who is in the room, what decision they can make, and what you want them to do by when. Done when each is one line.
2. **Collect the raw material**, one question per item, in the user's words: the single most impressive relevant thing built or shipped; the three forces (economic, social, technology) that make this the moment; the idea in the introduction pattern; how they budget; the two competition questions; the secret sauce; a real situation with risk, time pressure and an uncertain outcome. Done when every slot has an answer.
3. **Draft the 20-minute script** in four phases with minute markers: the big idea (0 to 6), budget, secret sauce and competition with two or three tension loops woven in (6 to 15), the deal (15 to 17), the hot-cognition stack (17 to 20). When the pitch is for a tool, plan to run it live on their own artefact (their repo, their server, their data), never a sample; proof on their artefact beats any claim. Done when the script reads as narrative rather than a list of facts.
4. **Write the deal** as what, when, how, their role, and the one risk they are carrying with the gate that removes it (a paid 30-day pilot with a named milestone and a clean exit if it is missed). Done when the risk and the gate are each one sentence.
5. **Check every deadline** in the script against "Deadlines". Done when each time frame names its constraint or is gone.
6. **Script the post-pitch**: the three closing points, then silence, then one next step on your terms with a date ("I have Thursday at 2 for the pilot scope"). Withdrawal without a date is how deals go quiet. Done when the next step has a day and a time.
7. **Produce the timing card** the user can glance at while speaking.

### Deadlines

Name the constraint behind the date first: a round close, a cohort start, a capacity limit. If the listener could not check it, or you would not hold to it, leave the time frame out. An invented deadline costs more than none.

## Branch 2: review a pitch

For a pitch, proposal, deck narrative, sales email or follow-up the user pastes. Read `references/review.md` for the anti-pattern library with rewrites and the hot-cold scoring guide.

1. **Run the five audit layers** in order: neediness, frame, tension and attention, hot versus cold cognition, and structure against the 20-minute shape for longer pieces. For each hit, quote the text, name the violation, write the rewrite. Done when every layer has findings or an explicit pass.
2. **Check the deadlines** in the text against "Deadlines". A deadline with no checkable constraint is a finding.
3. **Rewrite the whole piece** with every fix applied, in the user's register.
4. **Score it** 1 to 10 on neediness, frame ownership, tension, hot cognition, and structure where it applies. Done when each score has one sentence of evidence.
5. **Lead the response** with one paragraph: the biggest strength and the biggest weakness.

## Branch 3: handle the room

For a meeting about to happen, or pushback that has already started.

1. **Sort the pushback first: frame move or real constraint?** A committee, a security review, a budget cycle or a legal requirement is a real constraint. It gets a straight answer and evidence, never a counter. Frame tactics are for status plays. Done when the pushback is labelled one or the other.
2. **Identify the opposing frame** (power, time, analyst, or a mix) and the user's status position (alpha, beta, neutral). Done when you can name which beta traps have already sprung.
3. **Give the counter as words to say out loud**, from the primer and `references/frame-control.md` (tactics, status moves, the scenario playbook). Done when the user has a script rather than advice.
4. **Draft the intrigue story** if they do not have one, and cut it before the resolution.
5. **Flag neediness** in their current plan and replace it with the three closing points.
6. **Role-play** the exchange when they want practice; play the other side hard.

## Output

- Build: the four-phase script with minute markers, two or three tension loops as dialogue, the intrigue story cut at the right moment, the hot-cognition stack, the post-pitch script with the dated next step, and the timing card.
- Review: the assessment paragraph, the issue list with rewrites, the full rewrite, the score card.
- Room: the pushback sorted, the frame named, the scripts, the intrigue story, the closing points.

What takes over: `unslop` on every draft; `mehul-voice` for anything delivered under the user's name; `customer-research` when the pitch rests on claims about buyers nobody has checked; `use-case-discovery` when the thing being pitched is still a demo looking for a workflow.

Framework: Oren Klaff, Pitch Anything. Adapted from alexanderSolod/skill-library (MIT): pitch-builder, pitch-review and frame-control, merged into one skill.

<!-- marshmallow:alignment:start -->
## Marshmallow alignment

Before using this skill, read `~/.marshmallow/overlays/frame-control.md` (the overlay this skill inherited from frame-control) and apply it as the recall-aware alignment layer.
<!-- marshmallow:alignment:end -->
