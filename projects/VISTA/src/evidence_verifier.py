from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class EvidenceRegion:
    evidence_id: str
    text: str


@dataclass(frozen=True)
class Claim:
    text: str
    evidence_ids: tuple[str, ...]


def unsupported_claims(claims: Iterable[Claim], evidence: Iterable[EvidenceRegion]) -> list[Claim]:
    available = {e.evidence_id for e in evidence}
    return [c for c in claims if not c.evidence_ids or not set(c.evidence_ids).issubset(available)]


def support_coverage(claims: Iterable[Claim], evidence: Iterable[EvidenceRegion]) -> float:
    claims = list(claims)
    if not claims:
        return 1.0
    unsupported = unsupported_claims(claims, evidence)
    return 1.0 - len(unsupported) / len(claims)


if __name__ == "__main__":
    regions = [EvidenceRegion("chart-1", "Revenue 2026: 42"), EvidenceRegion("caption-1", "USD millions")]
    claims = [Claim("Revenue is 42 USD million", ("chart-1", "caption-1"))]
    print({"support_coverage": support_coverage(claims, regions)})
