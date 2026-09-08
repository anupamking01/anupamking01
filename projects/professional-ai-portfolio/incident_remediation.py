from dataclasses import dataclass
from typing import Dict, List
import re


@dataclass
class Remediation:
    incident_type: str
    confidence: float
    actions: List[str]
    evidence: List[str]


RUNBOOKS: Dict[str, List[str]] = {
    "database_connection": ["verify database endpoint", "check credentials/secret version", "test network route", "retry connection pool"],
    "authentication": ["check token expiry", "verify identity-provider availability", "refresh service token", "retry request"],
    "disk_capacity": ["inspect filesystem usage", "rotate/archive logs", "remove temporary files", "re-check free capacity"],
}


KEYWORDS = {
    "database_connection": {"connection refused", "database", "sqlstate", "timeout"},
    "authentication": {"unauthorized", "forbidden", "token", "401", "403"},
    "disk_capacity": {"no space left", "disk full", "filesystem", "capacity"},
}


def classify_ocr_error(ocr_text: str) -> Remediation:
    normalized = " ".join(ocr_text.lower().split())
    best_type, best_hits = "unknown", []
    for incident_type, words in KEYWORDS.items():
        hits = [word for word in words if word in normalized]
        if len(hits) > len(best_hits):
            best_type, best_hits = incident_type, hits
    confidence = min(1.0, len(best_hits) / 2) if best_hits else 0.0
    actions = RUNBOOKS.get(best_type, ["request manual triage"])
    return Remediation(best_type, confidence, actions, best_hits)


def extract_error_code(ocr_text: str) -> str | None:
    match = re.search(r"\b(?:ERR|ORA|SQLSTATE)[-: ]?[A-Z0-9-]{3,12}\b", ocr_text, flags=re.I)
    return match.group(0) if match else None


if __name__ == "__main__":
    sample = "Application screenshot OCR: SQLSTATE 08001 database connection refused timeout"
    print(classify_ocr_error(sample))
    print("error code:", extract_error_code(sample))
