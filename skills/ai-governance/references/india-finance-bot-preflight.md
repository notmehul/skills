# Compliance pre-flight for a customer-facing finance bot in India

As of Oct 2026. Run before go-live and again on every scope change. Each line is a yes or no with an owner; a no needs a date before go-live. Instrument status and dates are in `india-regulation-table.md`.

## 1. Identity and disclosure

- The bot says it is automated in its first message, or in the first five seconds of audio, in the user's language, and offers "type or say HUMAN" at any point (RBI draft Model Risk Management Guidance, Jun 2026; FREE-AI; FACE recovery guidelines).
- The regulated lender or lenders on whose behalf it acts are named. The platform's own name, its grievance officer, the lender's grievance officer and the RBI complaint portal link are reachable in-chat (Digital Lending Directions 2025, grievance and website disclosures).
- Synthetic-voice outbound audio opens with an audible "this is an automated call" (IT Rules amendment on synthetically generated information, effective 20 Feb 2026, read conservatively: whether a lender's own text-to-speech falls under it is contested).

## 2. Consent and data

- A standalone, itemised consent notice exists for each purpose: eligibility check, bureau pull, document processing, marketing. Withdrawal is one tap. The consent log stores purpose, timestamp, channel and notice version (DPDP Rules 3 and 4; Digital Lending Directions 2025).
- The bot never asks for or stores a full Aadhaar number, an OTP, a password, net-banking credentials or a card number. Uploaded Aadhaar is masked. The app requests no contacts, file or call-log permissions; camera, microphone and location are one-time and for KYC only (Digital Lending Directions 2025; UIDAI).
- The bureau pull is soft and consented, and the "will this hurt my score" question is answered truthfully.
- Data at rest and model calls stay in India, or are processed abroad and deleted within 24 hours. The vendor list in the privacy policy names the model provider (Digital Lending Directions 2025).
- Personal data is redacted before any transcript or document reaches a third-party model. Logs hold no phone numbers or OTPs in plaintext.

## 3. Telecom

- Outbound voice uses 1600-series numbers for service and transactional calls, and 140-series only for promotional calls with consent registered on the DLT platform (digital consent acquisition). No 10-digit numbers, including through telecallers or sales agents (RBI circular 17 Jan 2025; TRAI Direction 19 Nov 2025).
- Messaging templates are correctly categorised. No marketing content in a utility template; an opt-out in every marketing message; re-consent only 90 days after an opt-out (TCCCPR amendments 2025).
- Calling windows: 08:00 to 19:00 for collections, a declared window for sales. Predictive-dialer abandonment stays within TRAI limits.

## 4. Money and product truth

- Every number the bot quotes (rate, EMI, APR, fee, prepayment terms, cooling-off period) is read from the lender's Key Facts Statement or offer object, never generated. The bot refuses to quote a rate it cannot source (KFS circular, 15 Apr 2024).
- A multi-lender comparison shows every matched lender with APR, EMI, tenor, penal charges and a KFS link, names the unmatched lenders, and ranks by a published metric. No "recommended" badge without that metric (Digital Lending Directions 2025, para 6, in force since 1 Nov 2025).
- The bot never says insurance, a deposit or any third-party product is required for the loan. Asked, it states the customer may buy from any provider (Responsible Business Conduct Directions; IRDAI policyholder protection circular, 5 Sep 2024).
- No financial advice beyond product explanation. No "you should prepay" or "you should switch" without a disclosed calculator and its assumptions. No guarantee of approval, rate or turnaround time.
- Rejection or ineligibility messages give a reason category and the right to ask the lender for reasons. Eligibility logic uses no demographic proxies (Fair Practices Code; FREE-AI fairness sutra).

## 5. Model risk

Mapped to the RBI draft Model Risk Management Guidance of 24 Jun 2026. The final text had not been found as of 17 Oct 2026 (UNVERIFIED); build to the draft.

- An entry in the AI and model inventory: owner, risk tier, validator, go-live date, vendor dependencies.
- A red-team file covering prompt injection through uploaded documents, jailbreaks that extract a rate quote, language-switch exploits, personal-data exfiltration, and abusive-user handling. `llm-evals` runs it.
- A tested kill switch: one operator action disables the bot and routes to humans within minutes. Record the test date.
- Hallucination controls: retrieval over a versioned policy and offer store; refusal on out-of-corpus questions; a human scores a 10% weekly sample of conversations; drift metrics on intent distribution and refusal rate.
- Human-in-command: a named person reviews exceptions daily, and an override and incident log is kept.
