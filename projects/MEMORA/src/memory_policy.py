from dataclasses import dataclass
from typing import Iterable, List
import math
import re


def _tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))


@dataclass(frozen=True)
class MemoryItem:
    text: str
    age_steps: int
    importance: float = 0.5


def relevance(query: str, text: str) -> float:
    q, t = _tokens(query), _tokens(text)
    if not q:
        return 0.0
    return len(q & t) / len(q)


def score(query: str, item: MemoryItem, recency_weight: float = 0.25,
          relevance_weight: float = 0.55, importance_weight: float = 0.20) -> float:
    recency = math.exp(-max(item.age_steps, 0) / 20)
    return (
        recency_weight * recency
        + relevance_weight * relevance(query, item.text)
        + importance_weight * min(max(item.importance, 0.0), 1.0)
    )


def retrieve(query: str, items: Iterable[MemoryItem], k: int = 3) -> List[MemoryItem]:
    ranked = sorted(items, key=lambda x: score(query, x), reverse=True)
    return ranked[:max(k, 0)]


if __name__ == "__main__":
    memories = [
        MemoryItem("User prefers Python for ML experiments", 18, 0.8),
        MemoryItem("Database migration completed successfully", 2, 0.3),
        MemoryItem("Python experiment uses a fixed random seed", 8, 0.9),
    ]
    for item in retrieve("Python experiment", memories, 2):
        print(item)
