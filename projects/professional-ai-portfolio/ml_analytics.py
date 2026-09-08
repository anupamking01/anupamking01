from collections import defaultdict
from dataclasses import dataclass
from statistics import mean
from typing import Dict, Iterable, List, Tuple


@dataclass
class UserEvent:
    user_id: str
    days_since_last_activity: int
    trips_last_30d: int
    spend_last_30d: float
    category: str


def churn_risk(event: UserEvent) -> float:
    inactivity = min(1.0, event.days_since_last_activity / 60)
    low_usage = 1.0 if event.trips_last_30d == 0 else max(0.0, 1 - event.trips_last_30d / 8)
    low_spend = 1.0 if event.spend_last_30d == 0 else max(0.0, 1 - event.spend_last_30d / 5000)
    return round(0.5 * inactivity + 0.3 * low_usage + 0.2 * low_spend, 3)


def moving_average_forecast(history: List[float], window: int = 3) -> float:
    if not history:
        return 0.0
    values = history[-window:]
    return round(mean(values), 2)


def recommend_categories(events: Iterable[UserEvent], top_k: int = 3) -> Dict[str, List[Tuple[str, float]]]:
    by_user: Dict[str, Dict[str, float]] = defaultdict(lambda: defaultdict(float))
    for event in events:
        by_user[event.user_id][event.category] += event.spend_last_30d + 100 * event.trips_last_30d
    output = {}
    for user, scores in by_user.items():
        output[user] = sorted(scores.items(), key=lambda x: (-x[1], x[0]))[:top_k]
    return output


if __name__ == "__main__":
    sample = UserEvent("u-1", 35, 1, 700, "transport")
    print("churn risk:", churn_risk(sample))
    print("forecast:", moving_average_forecast([120, 150, 130, 170]))
    print("recommendations:", recommend_categories([sample, UserEvent("u-1", 2, 4, 2200, "fuel")]))
