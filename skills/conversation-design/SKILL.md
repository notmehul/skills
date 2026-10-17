---
name: conversation-design
description: "Design a chatbot or voice flow for high-intent Indian consumers in a regulated setting: WhatsApp, voice, Hinglish, handoff to a human. Use on 'intent', a service or sales bot, an IVR or voice agent, or scoring a flow before it ships."
license: MIT
metadata:
  version: "1"
  updated: "2026-10-18"
  harnesses: "claude-code codex opencode"
  source: "research-2026-10/india-fintech-lending.md A.4, A.5, D.3, D.5 (Oct 2026)"
---

# Conversation design

The public evidence on consumer bots in Indian finance is blunt. An RBI staff study of 5.69 million reviews across 107 fintech apps (Sep 2025) found customer support the top complaint, and inside it, automated replies with no path to a human. An EY survey of 2,030 bank customers (20 May 2026) had 25% rating their experience excellent, 8 to 13% valuing promotional personalisation, and 59% wanting AI as a financial coach rather than a salesperson. Calls to the RBI Ombudsman's contact centre ran 70% Hindi, 23% regional languages and 7% English (FY25 report, 1 Dec 2025). The flows that convert answer first, ask one thing per turn, pull every number from a system, and keep a human one word away. The running example is a salaried borrower who has picked a flat and wants to know the EMI.

## Steps

1. **Fix the channel and the moment.** Pick from the channel table below, and write down whether the first message is inbound (the user opened the thread) or outbound (you did), because the telecom rules and the price differ. Done when the flow has a channel, a direction, and a named template category or number series.
2. **Write the opener.** Disclosure plus the first useful answer in the same message: the bot says it is automated, names who it works for, offers "type or say HUMAN", and then answers the question the user actually asked. Done when a user who typed a question gets a real answer in the first reply, before any qualifying question.
3. **Write the turns.** One question per turn, buttons where the answers are few, free text allowed everywhere, a native form (WhatsApp Flows) for anything past three fields. Mirror the user's language and script; numbers in digits, amounts in lakh and crore with ₹. Done when no turn asks two things and no known fact is asked twice.
4. **Wire the numbers.** Every rate, EMI, APR, fee, eligibility figure and prepayment term comes from code over a versioned source, for a loan the lender's Key Facts Statement or offer object. The model explains the number and shows the assumptions (rate, tenor) and the KFS link. Done when every number in the script names the field it is read from, and the bot's answer to an unsourced rate is "I can't quote that yet" plus a handoff.
5. **Write the stop rules and the handoff spec.** Done when the rules under "Stop rules" are in the system prompt and the handoff payload lists what the human sees.
6. **Script the objection answers.** Bureau-score impact, hidden charges, insurance pressure, "why does the builder want me to use you", "is this rate guaranteed". Truthful, short, and the bot may say "I don't know; a person will answer by <time>". Done when each objection has a scripted answer the compliance owner has read.
7. **Choose the model split** (voice flows). A frontier model for reasoning and policy adherence; an Indic speech stack for recognition and synthesis on the phone. Done when the speech vendor has been tested on your own call recordings (telephony grade, Hinglish, numbers, scheme names) and the word error rate is written down, before any contract is signed.
8. **Score the flow on the rubric.** 0 to 2 on each of the 12 lines; ship at 80% or better, which is 20 of 24. Done when the sheet is filled and every line under 2 has a fix or a reason.
9. **Name the one KPI.** One number the system of record can measure inside the pilot window: completed-document rate, first-time-right, handoff rate. Done when the sponsor agrees to that one number and nothing else decides the pilot.

## The rubric

Score each flow 0 (absent), 1 (partial), 2 (met). Ship at 20 of 24 or better.

| # | Line | 2 looks like |
| :--- | :--- | :--- |
| 1 | Answer first, qualify second | "Bank A 7.5% ya Bank B?" gets today's comparison from the KFS, or an honest "rates reset after the 7 Oct 2026 repo change; here is what each lender shows today", before any question back |
| 2 | Mirror language and script | Hinglish in, Hinglish out; no language picker before the first useful answer; digits, ₹, lakh and crore |
| 3 | One question per turn | Buttons where possible, free text always accepted, a native form past three fields |
| 4 | Say what you are | Automated, who it works for, how to reach a person; repeated on request without friction |
| 5 | Numbers from systems, words from the model | EMI, APR, fees and eligibility computed; assumptions and KFS link shown |
| 6 | Never promise outcomes | "In-principle" and "subject to lender approval and property checks" stated once, plainly, not as boilerplate every turn |
| 7 | The next step is concrete and timed | "Upload three salary slips now; I'll confirm within 10 minutes" rather than "our team will contact you" |
| 8 | Respect the clock | No outbound before 08:00 or after 19:00 for collections; sales inside the declared window; a cap on nudges per application; "don't call, message me" honoured |
| 9 | Handoff keeps context | The human sees the summary, the documents and the exact question; the user repeats nothing; a human is reachable in-thread or on a 1600-series number |
| 10 | Objection honesty | Scripted truthful answers on score impact, charges, insurance, the builder tie-up; "I don't know, a person will answer by <time>" allowed |
| 11 | No sales nudges disguised as service | Nothing promotional inside a service thread; a mixed message is a marketing message and needs consent |
| 12 | Exit and erase | The user can stop, withdraw consent and ask for deletion in one message; the bot confirms what happens next |

## What converts and what annoys

From public evidence, vendor case studies included and labelled as such.

Converts: in-chat forms (one vendor case study, Jun 2026: 58% completion on a native form against 22% on mobile web); an instant document checklist, with the document request sent within 10 minutes of the form (same study: +27% submission); same-day follow-up; vernacular voice for low-literacy segments; pre-filled offers from data you already hold.

Annoys: no human path; canned "we have noted your concern"; re-asking a known fact; English-only IVR trees; promotional messages in a service thread; implying insurance is mandatory.

## Channels

As of Oct 2026. Prices and number rules change; re-check before quoting.

| Channel | Rule | Cost and mechanics |
| :--- | :--- | :--- |
| WhatsApp, inbound | A utility reply inside the 24-hour service window is free | Per-message pricing since 1 Jul 2025. India utility and authentication templates about ₹0.115, marketing about ₹0.86 per message (BSP price lists 2025-26; marketing raised again 1 Jan 2026). The platform reclassifies utility templates that read as promotional, since Apr 2025 without prior notice. Flows (native forms) are the biggest completion lever |
| WhatsApp, outbound | Marketing template only with consent and an opt-out in every message; re-consent 90 days after an opt-out | Marketing rate applies |
| Voice, service or transactional | 1600-series mandatory for RBI-regulated entities (banks from 1 Jan 2026, NBFCs above ₹5,000 crore from 1 Feb 2026, the rest from 1 Mar 2026; TRAI Direction 19 Nov 2025). A provider calling on a lender's behalf inherits the lender's obligations (RBI circular 17 Jan 2025) | Transactional means within 30 minutes of a customer-initiated transaction |
| Voice, promotional | 140-series only, with digital consent registered on DLT. Promotional content inside a service call makes the whole call promotional | Calling windows: 08:00 to 19:00 for collections (FACE guidelines, 29 Aug 2025); a declared window for sales |
| Synthetic voice, any direction | Audible "this is an automated call" opener (IT Rules amendment on synthetically generated information, effective 20 Feb 2026, read conservatively) | Adds two seconds; keeps you out of a contested reading of the rules |

## Language and the model split

- Hinglish and code-mixing are the norm. One published pilot post-mortem (Jul 2026) found Hinglish in 30% of conversations against a 10% estimate; build the test set to match.
- Independent benchmarks, Oct 2026 snapshot: frontier proprietary models still lead on Indic knowledge and instruction following, with Hindi near English parity and lexical or cross-lingual constraints weak. Indian speech vendors post the lowest word error rates on Indian-language and Indian-accented English benchmarks, with streaming and diarisation. A neutral Indic evaluation suite exists (Oct 2026); use it over vendor numbers.
- Split accordingly: a frontier model for reasoning and policy adherence, Indic speech recognition and synthesis for the phone, and your own call audio as the test, never the vendor demo.

## Stop rules

Copy these into the system prompt and the eval set.

- If the user mentions distress, a legal threat, a death, fraud, or asks for a human, the bot stops selling and routes at once. The handoff payload carries the summary, the documents and the exact last message.
- If a number affects money, code computes it from a versioned source; the model only explains it.
- If the bot cannot source an answer from the policy or offer store, it says so and hands off. It never improvises a product fact.
- If a message could be read as promotional, it goes out as marketing, with consent. When unsure, it is promotional.
- If the loan was sanctioned before 1 Jan 2026, the bot does not say prepayment is free; it points to the agreement.
- If a credit manager would not need a field, the bot does not ask for it.
- When the bot triggers anything beyond a reply (a document request, a callback booking, a consent withdrawal, an erasure), the action is a proposal that a human or a deterministic system confirms, and every action writes an event row.

## The running example

Inbound on WhatsApp, Hinglish, numbers as placeholders for the fields they come from.

```
User: Bank A 7.5% de raha hai, Bank B better hai kya? Flat finalise ho gaya.

Bot:  Main <platform> ka automated assistant hoon, <lender list> ke liye kaam karta hoon.
      Kabhi bhi HUMAN likhiye, ek person se baat hogi.
      Aaj ke KFS ke hisaab se (rates 7 Oct 2026 ke baad reset hue hain):
      Bank A: rate <kfs.rate>, APR <kfs.apr>, EMI ₹<calc.emi> on ₹<input.amount> / <input.tenor> saal
      Bank B: rate <kfs.rate>, APR <kfs.apr>, EMI ₹<calc.emi>
      Ranking: APR (lowest first). <unmatched lenders>: abhi match nahi hue. KFS: <links>
      Aapka loan amount kitna hai? [₹25-50L] [₹50L-1Cr] [₹1Cr+] [type karein]

User: 60 lakh. Builder bol raha hai aap se hi lena padega, insurance bhi.

Bot:  Nahi. Aap kisi bhi lender se loan le sakte hain, aur insurance kisi bhi insurer se,
      ya bilkul nahi; loan ke liye zaroori nahi hai.
      ₹60L / 20 saal par: Bank A EMI ₹<calc.emi>, Bank B ₹<calc.emi> (in-principle;
      lender approval aur property check ke baad final).
      Agla step: 3 salary slips, PAN, masked Aadhaar yahin upload karein.
      10 minute mein confirm karunga ki kuch missing hai ya nahi. [Upload] [HUMAN]
```

Every number above is a field read, the disclosure is in the first message, the objection gets a truthful answer, and the next step is timed.

## Output

- The flow script: opener, turns, templates by category, with every number annotated with its source field.
- The handoff spec: triggers, payload, the human path per channel.
- The scripted objection answers, read by the compliance owner.
- The rubric sheet with the score and a fix per line under 2.
- The one KPI and where it is recorded.

What takes over: `ai-governance` for the compliance pre-flight before go-live; `llm-evals` for the eval set built from the rubric and the stop rules; `knowledge-and-extraction` when the bot answers from documents or a policy store; `pilot-rollout` when the flow goes to real users.
