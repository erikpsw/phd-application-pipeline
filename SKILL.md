---
name: phd-application-pipeline
description: Manage an end-to-end PhD application outreach pipeline from applicant profile analysis to advisor discovery, matching, tracker updates, Gmail drafts, reply triage, and status management. Use for PhD申请规划、导师匹配、套磁进度管理、飞书多维表格更新、Gmail草稿与回复、批量筛选院校和导师.
---

# PhD Application Pipeline

## Purpose

Orchestrate a practical PhD outreach workflow:

1. read the applicant's CV and preferences,
2. discover suitable schools, labs, and advisors,
3. verify advisor fit using official sources,
4. draft concise personalized outreach emails,
5. update a Feishu/Lark Base tracker,
6. create Gmail drafts with CV attachments,
7. triage professor replies,
8. draft replies and update pipeline statuses.

Use the bundled `phd-outreach-email` skill for individual email wording. Never send email without explicit user approval.

## Applicant Configuration

Do not hard-code personal data. At the start of a new workflow, collect or load:

- `[APPLICANT_NAME]`
- `[APPLICANT_EMAIL]`
- `[TARGET_INTAKE]`
- `[TARGET_FIELDS]`
- `[DEGREE_AND_INSTITUTION]`
- `[GPA_OR_RANK]`
- `[CORE_INTERESTS]`
- `[KEY_PUBLICATION_OR_PROJECT]`
- `[OPTIONAL_INDUSTRY_EXPERIENCE]`
- `[CV_PATH]`

Treat planned employment, unpublished work, and future responsibilities as future or tentative. Never present them as completed achievements.

## Tracker Configuration

Use Feishu/Lark Base when a tracker URL or configuration is available. Load these from user input or environment configuration:

- `[BASE_TOKEN]`
- `[TABLE_ID]`
- `[VIEW_ID]`

Recommended fields:

- `姓名`
- `学校`
- `邮件`
- `官网链接`
- `研究方向主线`
- `研究方向摘要`
- `匹配度`
- `优先级`
- `学校池层级`
- `导师验证状态`
- `邮件内容`
- `套磁信版本`
- `状态`
- `下一步动作`
- `风险备注`

Prefer user identity for Lark CLI operations:

```bash
lark-cli base +record-list --as user ...
lark-cli base +record-upsert --as user ...
lark-cli base +record-delete --as user ... --yes
```

If authorization is required:

```bash
lark-cli auth login --domain base
```

Ask the user to complete the device authorization flow before continuing.

## Setup

Read `references/setup-guide.md` when the user asks how to install tools, connect Gmail or Feishu, configure a tracker, or reproduce the workflow.

Minimum setup:

1. Codex or another compatible agent environment.
2. Lark/Feishu CLI with Base access.
3. An authenticated Gmail connector.
4. A Feishu Base tracker using the recommended schema.
5. A local CV PDF.
6. Web access for advisor verification.

## School And Advisor Discovery

Build a school pool across departments relevant to the applicant, such as:

- Mechanical Engineering
- Computer Science
- ECE/EECS
- Robotics
- Industrial and Systems Engineering
- Operations Research
- Human-Centered AI
- Computer Vision
- Cyber-Physical Systems

Include adjacent departments only when there is a concrete bridge to the applicant's evidence. Avoid generic matches based on broad keywords alone.

### Advisor sourcing

Use official sources first:

- department faculty directory,
- research-area page,
- lab page,
- professor homepage,
- research-center page,
- recent papers,
- funded-project or university news pages.

For each advisor, collect:

- name,
- school and department,
- verified email,
- official profile URL,
- one concrete research detail,
- research-direction category,
- fit score,
- risk note,
- source and verification date.

### Pitch selection

Choose a pitch based on the advisor's actual research:

- Manufacturing: smart manufacturing, inspection, digital twins, process monitoring, quality, and cyber-physical systems.
- Computer vision: defect detection, segmentation, multimodal perception, and physical-world verification.
- Robotics: manipulation, planning, SLAM, control, robot learning, and embodied AI.
- HCI/HRI: human-robot collaboration, interpretable interaction, and reliable assistance.
- ECE/CPS: sensing, controls, real-time decision-making, digital twins, and process data.

## Fit Scoring

Use conservative scoring and define the scale in the tracker.

- `5.0–6.0`: strong direct fit and worth contacting.
- `4.0–4.9`: good fit; contact when the advisor and program are attractive.
- `3.0–3.9`: edge fit; contact only with a concrete reason.
- `<3.0`: normally do not contact.

Boost:

- direct topic overlap,
- recent active projects,
- clear PhD advising scope,
- strong methodological overlap,
- strong program resources.

Penalize:

- no verified profile or email,
- inactive, retired, or emeritus status,
- weak evidence of current advising,
- generic topic similarity,
- unclear funding or intake.

Keep program strength and advisor fit as separate fields.

## Email Generation

Before drafting:

1. verify the advisor online,
2. identify one concrete research detail,
3. select one or two applicant evidence points,
4. check the advisor's current role and lab activity.

First-contact rules:

- normally 170–230 words,
- use one concrete advisor research detail,
- connect it to specific applicant evidence,
- ask whether the advisor anticipates taking students for `[TARGET_INTAKE]`,
- avoid exaggerated praise,
- avoid generic standalone skills lists,
- do not fabricate publications, roles, results, or research fit,
- keep planned roles explicitly in future tense.

After drafting, update:

- `邮件内容`
- `套磁信版本`
- `下一步动作`

Audit:

- recipient and professor name are verified,
- the email contains a concrete research connection,
- the applicant evidence is accurate,
- no duplicate advisor row exists,
- the exact saved subject and body match the Gmail draft.

## Gmail Draft Creation

Create drafts only. Do not send unless explicitly requested.

```json
{
  "to": "professor@example.edu",
  "subject": "PhD Inquiry: [RESEARCH_TOPIC] ([TARGET_INTAKE])",
  "body": "Dear Professor ...",
  "attachment_files": ["/absolute/path/applicant_cv.pdf"]
}
```

After creating drafts:

- verify recipient,
- verify subject,
- verify `has_attachment`,
- record the draft or message ID,
- write the exact subject and body back to the tracker,
- use pagination when verifying large batches,
- keep a deterministic local manifest to prevent duplicates.

If authentication expires, ask the user to reconnect Gmail.

## Reply Triage

Search recent inbox messages, then read the full thread before classifying.

Recommended search:

```text
in:inbox newer_than:14d
```

Use `references/status-taxonomy.md` for classifications:

- `积极回复`
- `流程型回复`
- `等待回复`
- `低优先级`
- `暂不考虑`
- `已发送`
- `草稿已创建`

Reply drafts should:

- be shorter than the initial email,
- thank the professor,
- mirror the professor's instructions,
- state a clear follow-up plan for positive replies,
- close politely for rejections or unavailable funding.

Never classify an automated reply as a positive response.

## Deduplication

Find duplicates using normalized:

- `姓名 + 学校`
- `邮件`

Keep the more complete row. Merge useful information when both rows contain unique data. Delete only clearly inferior duplicates, and ask before deleting when uncertain.

## Safety

- Never send emails without explicit approval.
- Never publish or commit personal data, credentials, tracker IDs, or private CV paths.
- Never delete uncertain tracker rows.
- Never infer a positive response from an auto-reply.
- Never fabricate advisor facts or application outcomes.
- Keep program reputation, advisor fit, funding, and intake likelihood separate.
