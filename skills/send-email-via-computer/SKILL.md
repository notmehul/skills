---
name: Send email via computer
description: >-
  use this whenever sending email for Mehul — always browser Gmail on this computer, never the Gmail MCP connector
---
# Send email via computer

Send mail only through signed-in Chrome Gmail on this computer. Never use the Gmail MCP (or any mail API) to send.

## Inputs

- `{from_account}` — which Gmail account (e.g. probablymehul@gmail.com)
- `{to}` — recipient(s)
- `{subject}`
- `{body}` — final wording already approved if this is outreach
- `{attachments}` — optional file paths (PDF etc.)
- `{links}` — any URLs in the body must be real `https://` links, never placeholders

## Steps

1. Open Gmail for `{from_account}` in Chrome on this computer.
2. Compose a new message. Fill To, Subject, Body.
3. Attach `{attachments}` if any (use the paperclip / file picker).
4. Before send: confirm recipients, subject, that links are real https URLs, and attachments landed.
5. **Stop and confirm with Mehul before clicking Send** unless he already explicitly asked to send this exact message to these recipients.
6. After send (only when approved): note the account used, recipients, subject, and whether attachments went out.

## Hard rules

- Computer/browser only — no Gmail MCP send, no curl, no SMTP.
- Do not invent recipient addresses.
- Do not send unprompted; drafting is the default when unsure.
- Preserve Mehul's wording for outreach; run mehul-voice / unslop only when asked to revise.

## Report

Account, To, Subject, attachments yes/no, sent or still a draft.

