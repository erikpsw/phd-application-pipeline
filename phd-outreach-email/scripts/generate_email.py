#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


FORBIDDEN = (
    "groundbreaking",
    "world-class",
    "prestigious",
    "fascinating",
    "incredible",
    "transformative",
    "deeply inspired",
    "perfect fit",
)


def clean(value: object) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def required(data: dict, key: str, section: str) -> str:
    value = clean(data.get(key))
    if not value:
        raise ValueError(f"Missing required field: {section}.{key}")
    return value


def last_name(name: str) -> str:
    value = re.sub(r",?\s*Ph\.?D\.?", "", name).strip()
    value = re.sub(r"^\s*Professor\s+", "", value, flags=re.I).strip()
    parts = value.split()
    return parts[-1] if parts else "Professor"


def infer_angle(advisor: dict) -> str:
    text = clean(
        " ".join(
            str(advisor.get(key, ""))
            for key in ("angle", "keywords", "evidence", "research_summary")
        )
    ).lower()
    if any(term in text for term in ("digital twin", "cyber-physical", "cps")):
        return "digital twins and cyber-physical systems"
    if any(
        term in text
        for term in ("inspection", "quality", "sensing", "anomaly", "metrology", "computer vision")
    ):
        return "AI-enabled inspection and quality control"
    if any(term in text for term in ("robot", "manipulation", "planning", "slam", "autonomous")):
        return "robotics, perception, and planning for physical systems"
    if any(term in text for term in ("additive", "advanced manufacturing", "fabrication", "assembly")):
        return "advanced manufacturing and data-driven process intelligence"
    if any(term in text for term in ("optimization", "machine learning", "data-driven", "surrogate")):
        return "machine learning and data-driven modeling"
    if any(term in text for term in ("industry 4.0", "mes", "industrial digitalization")):
        return "industrial digitalization and smart manufacturing systems"
    return clean(advisor.get("angle")) or "data-driven engineering systems"


def subject(angle: str, intake: str) -> str:
    if "digital twin" in angle:
        topic = "Digital Twins and Cyber-Physical Systems"
    elif "inspection" in angle or "quality" in angle:
        topic = "AI-enabled Inspection"
    elif "robotics" in angle:
        topic = "Robotics and Physical Intelligence"
    elif "advanced manufacturing" in angle:
        topic = "Data-driven Advanced Manufacturing"
    else:
        topic = "Data-driven Engineering Systems"
    return f"PhD Inquiry: {topic} ({intake})"


def select_evidence(applicant: dict, angle: str) -> str:
    evidence = applicant.get("evidence", {})
    if not isinstance(evidence, dict):
        raise ValueError("applicant.evidence must be an object")

    primary = clean(evidence.get("primary"))
    if not primary:
        raise ValueError("Missing required field: applicant.evidence.primary")

    if "inspection" in angle or "quality" in angle:
        secondary = clean(evidence.get("vision") or evidence.get("secondary"))
    elif "robotics" in angle or "planning" in angle:
        secondary = clean(evidence.get("robotics") or evidence.get("secondary"))
    elif any(term in angle for term in ("manufacturing", "industrial", "digital", "process")):
        secondary = clean(evidence.get("manufacturing") or evidence.get("secondary"))
    else:
        secondary = clean(evidence.get("secondary"))

    return f"{primary} {secondary}".strip()


def future_context(applicant: dict) -> str:
    role = applicant.get("future_role")
    if not role:
        return ""
    if not isinstance(role, dict):
        raise ValueError("applicant.future_role must be an object")
    organization = required(role, "organization", "applicant.future_role")
    area = required(role, "area", "applicant.future_role")
    return (
        f"I will soon join {organization}, where I expect to gain exposure to {area}."
    )


def draft(data: dict) -> str:
    applicant = data.get("applicant")
    advisor = data.get("advisor")
    if not isinstance(applicant, dict) or not isinstance(advisor, dict):
        raise ValueError("Input must contain applicant and advisor objects")

    applicant_name = required(applicant, "name", "applicant")
    applicant_email = required(applicant, "email", "applicant")
    status = required(applicant, "status", "applicant")
    intake = required(applicant, "target_intake", "applicant")
    advisor_name = required(advisor, "name", "advisor")
    advisor_detail = required(advisor, "verified_research_detail", "advisor")

    angle = infer_angle(advisor)
    evidence = select_evidence(applicant, angle)
    future = future_context(applicant)

    body = f"""Subject: {subject(angle, intake)}

Dear Professor {last_name(advisor_name)},

My name is {applicant_name}, and I am {status}. I am writing to inquire about PhD opportunities for {intake}. Your research on {advisor_detail} aligns with the direction I hope to pursue.

{evidence}

Looking ahead, I am interested in how {angle} can support reliable analysis and decision-making in real engineering systems. {future}

I have attached my CV and would appreciate knowing whether you anticipate taking PhD students for {intake}.

Thank you for your time.

Best regards,
{applicant_name}
{applicant_email}
"""
    for phrase in FORBIDDEN:
        body = re.sub(re.escape(phrase), "", body, flags=re.I)
    body = body.replace("—", ",").replace("–", ":")
    return re.sub(r" +\n", "\n", body).strip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a concise PhD advisor outreach email from JSON."
    )
    parser.add_argument("--input", required=True, help="Input JSON path")
    parser.add_argument("--output", help="Optional output text path")
    args = parser.parse_args()

    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    text = draft(data)
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
