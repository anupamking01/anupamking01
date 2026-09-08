from dataclasses import dataclass, asdict
from typing import Dict, Iterable, Optional


@dataclass
class ApplicationRecord:
    applicant_name: Optional[str] = None
    employer: Optional[str] = None
    member_id: Optional[str] = None
    coverage_amount: Optional[float] = None


def normalize_text(text: str) -> str:
    return " ".join(text.replace("\n", " ").split())


def extract_fields(text: str) -> ApplicationRecord:
    """Deterministic stand-in for text/vision model output parsing."""
    clean = normalize_text(text)
    fields: Dict[str, str] = {}
    for segment in clean.split("|"):
        if ":" in segment:
            key, value = segment.split(":", 1)
            fields[key.strip().lower()] = value.strip()
    amount = fields.get("coverage")
    return ApplicationRecord(
        applicant_name=fields.get("name"),
        employer=fields.get("employer"),
        member_id=fields.get("member id"),
        coverage_amount=float(amount.replace(",", "")) if amount else None,
    )


def validate(record: ApplicationRecord) -> Dict[str, str]:
    errors = {}
    if not record.applicant_name:
        errors["applicant_name"] = "missing"
    if record.member_id and len(record.member_id) < 5:
        errors["member_id"] = "too_short"
    if record.coverage_amount is not None and record.coverage_amount <= 0:
        errors["coverage_amount"] = "must_be_positive"
    return errors


def field_accuracy(predicted: ApplicationRecord, expected: ApplicationRecord, fields: Iterable[str]) -> float:
    names = list(fields)
    if not names:
        return 0.0
    p, e = asdict(predicted), asdict(expected)
    return sum(p[name] == e[name] for name in names) / len(names)


if __name__ == "__main__":
    sample = "Name: Asha Sen | Employer: Example Health | Member ID: MH10293 | Coverage: 250000"
    record = extract_fields(sample)
    print(record)
    print("validation:", validate(record))
