from dataclasses import dataclass


@dataclass(frozen=True)
class TaskSignal:
    complexity: float
    uncertainty: float
    risk: float


def routing_score(signal: TaskSignal) -> float:
    c = min(max(signal.complexity, 0.0), 1.0)
    u = min(max(signal.uncertainty, 0.0), 1.0)
    r = min(max(signal.risk, 0.0), 1.0)
    return 0.35 * c + 0.30 * u + 0.35 * r


def route(signal: TaskSignal, escalation_threshold: float = 0.58) -> str:
    return "large_model" if routing_score(signal) >= escalation_threshold else "small_model"


if __name__ == "__main__":
    examples = {
        "simple_lookup": TaskSignal(0.15, 0.10, 0.05),
        "financial_action": TaskSignal(0.50, 0.45, 0.95),
    }
    for name, signal in examples.items():
        print(name, route(signal), round(routing_score(signal), 3))
