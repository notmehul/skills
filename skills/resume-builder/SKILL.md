---
name: resume-builder
description: Write, rewrite, tailor, or review a resume or CV. Use on "my resume", "my CV", "tailor this to the job description", or any document a person will submit with a job application.
---

# Resume builder

Produce a resume that passes a recruiter's **5-second scan**: current title, relevant skills, level of experience, and a reason to keep reading, all visible before they scroll. Layout, fonts, and file rendering are not this skill's job; hand those to the design or document skills once the content is settled.

Which path:

| Request | Path |
| --- | --- |
| Build from scratch | Gather → Structure → Write → Review |
| Improve an existing one | Read it against Review, then rewrite the bullets that fail |
| Tailor to a job description | Tailor, then Review |
| "Review my resume" | Review only, findings ordered by impact |

## Gather

Collect, and keep asking until each is answered:

1. **Work history**: title, company, dates, and for each role the **domain context**: what industry, what kind of system, what data (payments, health records, PII), who the users were. "Developed web apps" and "developed fintech credit-management systems handling card issuance and settlement" describe the same job; only one gets a call.
2. **Numbers from the user**: users served, requests per day, revenue touched, team size, time saved. Every figure on the page comes from them. Where they have none, use scale words ("thousands of daily orders", "a 6-person team") or drop the claim.
3. **Skills**: languages, frameworks, infrastructure, tools, methods.
4. **Education and projects**.
5. **Target**: roles, market, and the job description if there is one.
6. **Length**: 1 page under about 5 years of experience, 2 pages above. Never 3.

Done when every role has a domain and at least one real measure of scale.

## Structure

Order sections by what the target reader scans for first:

- **Experienced (3+ years)**: Name and contact → Skills → Experience → Projects (optional) → Education.
- **Junior or new graduate**: Name and contact → Education → Skills → Experience (internships, freelance) → Projects.

Use the plain headings a parser and a recruiter both expect: "Skills", "Experience", "Projects", "Education". Contact is one line: email, GitHub or portfolio, LinkedIn, as bare URLs with no labels. Leave out photo, address, age, marital status, and "references available on request".

Each role:

```
Title, Company – City (Remote)                    Mon YYYY – Present
• bullet
• bullet
Technologies: only what this role actually used
```

Dates: month and full year, "Present" for the current role, an en dash with spaces, reverse chronological. Education carries a graduation date only.

## Write

Every bullet follows **XYZ**: accomplished X, measured by Y, by doing Z. In practice: action verb + what you built + domain context + impact.

> Reduced checkout API latency 40% across 15 high-traffic endpoints serving 200K monthly users by adding a Redis cache layer and rewriting PostgreSQL query plans

Rules that hold for every bullet:

- Open with a plain past-tense verb: Built, Designed, Led, Migrated, Reduced, Shipped, Automated, Mentored, Cut, Scaled. Plain beats grand: "spearheaded", "orchestrated", "leveraged", "utilized", and "responsible for" all say less than "led" or "built".
- One to two lines, one sentence, no closing period, no pronouns.
- Digits for every number: 8 not eight, 30% not thirty percent.
- Name the specific technology, not the category.
- Order within a role from most relevant to least.
- Leave out self-assessment ("passionate", "fast learner"), table-stakes tools, reasons for leaving, and buzzwords with no referent.

Bullets per role by recency: current role 5–7, roles from the last three years 4–6, older ones 2–3.

Done when no bullet on the page starts with a weak verb or lacks either domain or impact.

## Tailor

When a job description exists:

1. Pull its required and preferred technologies, domain words, and seniority signals (mentoring, architecture ownership, cross-team work).
2. Map each to a place in the user's real experience. A skill that appears in the list but in no bullet gets written into the bullet where it was used.
3. Reorder rather than rewrite: most relevant bullets to the top of each role, the matching skill category first.
4. Match the posting's terms where the user has the experience ("CI/CD" if they say CI/CD). Everything on the page will be asked about in the interview, so nothing goes on it the user can't defend.

**What an ATS is**: a database recruiters search. Modern ones (Greenhouse, Lever, Workday, iCIMS) parse PDF and DOCX equally, match synonyms, and don't auto-reject on a score. Humans do the rejecting, in seconds. Keyword stuffing and hidden white text lose to a page a human can scan. The parsing constraints that do matter: single column, no tables or text boxes for layout, no graphics, nothing important in a header or footer.

## Review

Check every line against this before delivering, and report each miss with a rewrite:

- 5-second scan: title, skills, and level readable without scrolling
- Every role names its domain and carries a real measure of scale
- Every bullet opens with a strong verb and ends in impact
- No invented numbers; each figure traceable to the user
- Standard headings, reverse chronological, consistent date format
- No pronouns, no closing periods on bullets, digits for numbers
- Skills in the list also appear in at least one bullet
- Page count fits the experience level with page 2 at least half full
- Spelling and grammar clean, no in-house jargon or codenames

Deliver the content as markdown in the structure above. When the user wants a file, pass the finished markdown to the document or design skill with the parsing constraints from Tailor; the content is done.
