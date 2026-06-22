---
name: phd-outreach-email
description: Draft, revise, batch-generate, and evaluate concise PhD supervisor outreach emails from an applicant profile and verified advisor research. Use for 套磁邮件、PhD cold emails、导师联系邮件、supervisor inquiry emails, advisor-profile rows, CSV/Base records, and Gmail draft preparation.
---

# PhD Outreach Email

## Core Workflow

1. Verify the advisor before drafting:
   - use the official university profile, lab page, recent papers, or funded-project pages;
   - confirm current role, email, research activity, and advising relevance;
   - record at least one concrete research detail and its source date.
2. Load the applicant profile:
   - name, email, degree, institution, target intake, and target fields;
   - one primary publication or research result;
   - optional thesis, project, or industry evidence;
   - CV path when preparing a draft.
3. Choose one primary angle:
   - `DT`: digital twins, CPS, predictive maintenance, process monitoring;
   - `AM`: advanced or additive manufacturing, fabrication, assembly;
   - `Quality`: inspection, sensing, anomaly detection, quality control;
   - `Robotics`: manipulation, planning, SLAM, autonomous systems, HRI;
   - `Method`: ML, optimization, data-driven or surrogate modeling;
   - `IDT`: industrial digitalization, MES, Industry 4.0, manufacturing systems.
4. Select no more than two applicant evidence points for a first email.
5. Draft the subject and email.
6. Audit facts, tone, word count, recipient, and attachment.

Read `references/style-guide.md` when drafting or revising.

## Email Structure

Write:

1. a specific subject line;
2. a correct greeting;
3. applicant identity and target intake;
4. one verified advisor research connection;
5. one concise applicant-evidence paragraph;
6. one forward-looking research-interest paragraph;
7. a CV line and a question about PhD availability;
8. a professional signature.

## Style Rules

- Target 170–230 words for first contact.
- Prefer four short body paragraphs.
- Use one concrete advisor detail, not a keyword list.
- Connect applicant evidence to the advisor's research problem or method.
- Use plain, restrained language.
- Avoid exaggerated praise and claims of perfect fit.
- Do not use em dashes.
- Do not include a standalone skills list unless requested.
- Do not fabricate research, publications, roles, deployment results, funding, or intake.
- Keep planned roles explicitly in future tense.
- Never describe future responsibilities as completed work.

## Evidence Selection

Use the strongest evidence for the selected angle:

- `DT` or `IDT`: digital-twin, process-monitoring, manufacturing-system, or industrial-data evidence.
- `AM`: fabrication, manufacturing experiments, process modeling, or robotic-manufacturing evidence.
- `Quality`: inspection, sensing, segmentation, anomaly detection, or metrology evidence.
- `Robotics`: peer-reviewed robotics work, manipulation, planning, control, perception, or embodied-AI evidence.
- `Method`: optimization, ML, data-driven modeling, simulation, or surrogate-model evidence.

Use future employment only as brief context when it clearly improves the match.

## Deterministic Generator

For a reproducible draft from JSON:

```bash
python3 scripts/generate_email.py --input advisor.json
```

The input must contain `applicant` and `advisor` objects. See the script help and validation errors for required fields.

```json
{
  "applicant": {
    "name": "Alex Chen",
    "email": "alex@example.com",
    "status": "a final-year engineering student",
    "target_intake": "Fall 2027",
    "evidence": {
      "primary": "My first-author paper studies motion planning for robotic manipulation.",
      "robotics": "I also developed a ROS-based perception and control prototype."
    }
  },
  "advisor": {
    "name": "Professor Jane Smith",
    "verified_research_detail": "safe manipulation planning under uncertainty",
    "keywords": "robotics manipulation planning"
  }
}
```

## Gmail Draft Workflow

When asked to create Gmail drafts:

1. Confirm recipient, subject, exact body, and CV path.
2. Create a draft, not a sent message.
3. Pass `attachment_files` as an array of absolute paths.
4. Verify recipient, subject, and `has_attachment`.
5. Store the exact final subject and body in the tracker.
6. Follow pagination for batch verification.
7. Keep a manifest of advisor, recipient, subject, body, draft ID, attachment status, and tracker record ID.

Example shape:

```json
{
  "to": "professor@example.edu",
  "subject": "PhD Inquiry: Research Topic (Fall 2027)",
  "body": "Dear Professor ...",
  "attachment_files": ["/absolute/path/applicant_cv.pdf"]
}
```

Do not send unless the user explicitly approves sending.
