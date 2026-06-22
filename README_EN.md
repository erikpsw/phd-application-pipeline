# PhD Application Pipeline Skill

[中文说明](README.md)

An end-to-end PhD outreach workflow for Codex and compatible agent environments. It connects applicant-profile analysis, school and advisor discovery, research-fit verification, Feishu/Lark tracking, Gmail draft creation, and professor-reply triage.

## Features

- Extract research themes and matching keywords from a CV
- Discover advisors across ME, CS, ECE/EECS, Robotics, ISyE, and adjacent fields
- Verify advisor details using official university and lab sources
- Score research fit conservatively
- Draft concise, personalized, and evidence-based outreach emails
- Track status, next actions, and risks in Feishu/Lark Base
- Create Gmail drafts with CV attachments and verify them
- Triage professor replies and create reply drafts
- Detect duplicate advisor records and resume interrupted batches safely

## Installation

Clone the repository into your Codex skills directory:

```bash
git clone https://github.com/YOUR_USERNAME/phd-application-pipeline.git \
  ~/.codex/skills/phd-application-pipeline
```

You may also copy the repository into the skills directory of another compatible agent.

## Example Prompts

```text
Read my CV and find 20 robotics PhD advisors for Fall 2027.
Verify their official profiles and recent work, rank them by fit,
and add them to my Feishu Base tracker.
```

```text
Review professor replies from the last 14 days, update the outreach
statuses, and create Gmail reply drafts where needed. Do not send.
```

## Configuration

This repository contains no real personal data or credentials. Prepare:

- applicant name, email, target intake, and research interests,
- an absolute local path to the CV,
- Feishu Base Token, Table ID, and View ID,
- an authenticated Gmail connector,
- web access for advisor verification.

See [references/setup-guide.md](references/setup-guide.md).

## Privacy And Safety

- Never commit CVs, personal email addresses, tokens, table IDs, or private email content.
- The skill creates drafts by default and never sends email without explicit approval.
- Delete tracker rows only when they are clearly duplicates.
- Advisor matching must rely on verifiable sources. Never fabricate intake, funding, or research details.

## License

[MIT](LICENSE)
