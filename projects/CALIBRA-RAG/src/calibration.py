from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Evidence:
    relevance: float
    supports_claim: bool
    contradicts_claim: bool = False


def confidence(evidence: Iterable[Evidence]) -> float:
    items = list(evidence)
    if not items:
        return 0.0
    relevance = sum(max(0.0, min(1.0, e.relevance)) for e in items) / len(items)
    support = sum(e.supports_claim for e in items) / len(items)
    contradiction = sum(e.contradicts_claim for e in items) / len(items)
    return max(0.0, min(1.0, 0.45 * relevance + 0.45 * support - 0.35 * contradiction))


def decision(evidence: Iterable[Evidence], answer_threshold: float = 0.70,
             retrieve_more_threshold: float = 0.40) -> str:
    c = confidence(evidence)
    if c >= answer_threshold:
        return "answer"
    if c >= retrieve_more_threshold:
        return "retrieve_more"
    return "abstain"


if __name__ == "__main__":
    trace = [
        Evidence(0.92, True),
        Evidence(0.84, True),
        Evidence(0.50, False, True),
    ]
    print({"confidence": round(confidence(trace), 3), "decision": decision(trace)})
