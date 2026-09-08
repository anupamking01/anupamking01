from dataclasses import dataclass
from typing import List
import re


@dataclass
class TestAction:
    verb: str
    target: str
    value: str | None = None


@dataclass
class StructuredTestCase:
    title: str
    actions: List[TestAction]
    expected_outcome: str
    entities: dict


ACTION_PATTERNS = [
    (re.compile(r"click\s+(?:on\s+)?(.+)", re.I), "click"),
    (re.compile(r"enter\s+(.+?)\s+in\s+(.+)", re.I), "enter"),
    (re.compile(r"select\s+(.+?)\s+from\s+(.+)", re.I), "select"),
]


def parse_step(step: str) -> TestAction:
    clean = step.strip().rstrip(".")
    for pattern, verb in ACTION_PATTERNS:
        match = pattern.fullmatch(clean)
        if not match:
            continue
        if verb == "click":
            return TestAction(verb, match.group(1).strip())
        value, target = match.group(1).strip(), match.group(2).strip()
        return TestAction(verb, target, value)
    return TestAction("manual", clean)


def extract_entities(text: str) -> dict:
    return {
        "urls": re.findall(r"https?://\S+", text),
        "ticket_ids": re.findall(r"\b[A-Z]{2,10}-\d+\b", text),
        "quoted_values": re.findall(r"['\"]([^'\"]+)['\"]", text),
    }


def structure_test_case(title: str, steps: List[str], expected_outcome: str) -> StructuredTestCase:
    joined = " ".join([title, *steps, expected_outcome])
    return StructuredTestCase(
        title=title,
        actions=[parse_step(step) for step in steps],
        expected_outcome=expected_outcome,
        entities=extract_entities(joined),
    )


if __name__ == "__main__":
    case = structure_test_case(
        "AUTH-104 login happy path",
        ["Enter 'demo@example.com' in email field", "Enter 'secret' in password field", "Click login button"],
        "Dashboard is displayed",
    )
    print(case)
