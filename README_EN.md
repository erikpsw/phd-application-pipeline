# PhD Application Pipeline Skill

[中文说明](README.md)

A PhD outreach toolkit for Codex and compatible agent environments. It includes:

- `phd-application-pipeline` for end-to-end orchestration, advisor discovery, tracking, and reply triage.
- `phd-outreach-email` for concise, evidence-based supervisor inquiry emails.

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

Clone the repository:

```bash
git clone https://github.com/erikpsw/phd-application-pipeline.git
```

Install both skills:

```bash
cp -R phd-application-pipeline ~/.codex/skills/phd-application-pipeline
cp -R phd-application-pipeline/phd-outreach-email \
  ~/.codex/skills/phd-outreach-email
```

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
