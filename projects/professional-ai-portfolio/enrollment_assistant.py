from dataclasses import dataclass
from typing import Dict, List


@dataclass
class EnrollmentRequest:
    employee_id: str
    plan: str
    dependents: int = 0


class EnrollmentAssistant:
    """Clean-room employer/employee enrollment assistant with deterministic policy gates."""

    def __init__(self, eligible_plans: Dict[str, dict]):
        self.eligible_plans = eligible_plans

    def validate(self, request: EnrollmentRequest) -> List[str]:
        errors = []
        if request.plan not in self.eligible_plans:
            errors.append("unknown_plan")
            return errors
        plan = self.eligible_plans[request.plan]
        if request.dependents > plan.get("max_dependents", 0):
            errors.append("dependent_limit_exceeded")
        return errors

    def respond(self, request: EnrollmentRequest) -> dict:
        errors = self.validate(request)
        if errors:
            return {"status": "needs_correction", "errors": errors}
        plan = self.eligible_plans[request.plan]
        return {
            "status": "eligible",
            "employee_id": request.employee_id,
            "plan": request.plan,
            "monthly_employee_cost": plan["employee_cost"] + request.dependents * plan.get("dependent_cost", 0),
            "next_action": "confirm_enrollment",
        }


def bedrock_prompt_payload(request: EnrollmentRequest, policy_context: str) -> dict:
    """Provider-neutral payload shape that can be adapted to AWS Bedrock runtime calls."""
    return {
        "system": "Answer enrollment questions only from supplied policy context.",
        "context": policy_context,
        "request": request.__dict__,
    }


if __name__ == "__main__":
    plans = {"gold": {"max_dependents": 3, "employee_cost": 2500, "dependent_cost": 700}}
    assistant = EnrollmentAssistant(plans)
    print(assistant.respond(EnrollmentRequest("EMP-102", "gold", 2)))
