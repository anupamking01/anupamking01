from dataclasses import dataclass
from typing import List
import re


@dataclass
class MarkingResult:
    score: float
    matched_steps: List[str]
    missing_steps: List[str]
    feedback: str


class MathTutorMarker:
    """Step-aware clean-room math marker and tutoring demo."""

    @staticmethod
    def _tokens(step: str) -> set[str]:
        return set(re.findall(r"[a-zA-Z]+|[-+*/=()0-9.]+", step.lower()))

    def mark(self, student_steps: List[str], reference_steps: List[str]) -> MarkingResult:
        matched, missing = [], []
        student_sets = [self._tokens(step) for step in student_steps]
        for ref in reference_steps:
            ref_tokens = self._tokens(ref)
            overlap = max((len(ref_tokens & s) / max(1, len(ref_tokens)) for s in student_sets), default=0.0)
            if overlap >= 0.6:
                matched.append(ref)
            else:
                missing.append(ref)
        score = len(matched) / max(1, len(reference_steps))
        feedback = self._feedback(missing)
        return MarkingResult(score, matched, missing, feedback)

    @staticmethod
    def _feedback(missing: List[str]) -> str:
        if not missing:
            return "All reference reasoning steps are represented."
        return "Review these concepts/steps: " + "; ".join(missing)

    def hint(self, problem: str, concept: str) -> str:
        return f"For '{problem}', start from the governing idea: {concept}. State the relation before substituting values."


if __name__ == "__main__":
    marker = MathTutorMarker()
    result = marker.mark(
        ["2x + 4 = 10", "2x = 6", "x = 3"],
        ["subtract 4 from both sides", "2x = 6", "divide both sides by 2", "x = 3"],
    )
    print(result)
    print(marker.hint("Solve 2x + 4 = 10", "inverse operations"))
