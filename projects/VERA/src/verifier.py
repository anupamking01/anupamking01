from __future__ import annotations

from .models import TaskState, ToolAction, VerificationResult


def verify_action(state: TaskState, action: ToolAction) -> VerificationResult:
    reasons = []

    if action.tool_name not in state.authorized_tools:
        reasons.append(f"Tool '{action.tool_name}' is not authorized for this task.")

    if action.requires_confirmation:
        return VerificationResult(
            allowed=False,
            reasons=reasons or ["Action requires explicit confirmation."],
            clarification_needed=True,
            clarification_question="Please confirm that I should execute this action.",
        )

    # Example deterministic authorization limit for monetary actions.
    if "amount" in action.arguments and "max_amount" in state.authorized_limits:
        try:
            amount = float(action.arguments["amount"])
            max_amount = float(state.authorized_limits["max_amount"])
            if amount > max_amount:
                reasons.append(
                    f"Requested amount {amount} exceeds the authorized limit {max_amount}."
                )
        except (TypeError, ValueError):
            reasons.append("Amount could not be validated as a number.")

    # Example ambiguity check for named entities.
    if action.arguments.get("recipient") == "AMBIGUOUS":
        return VerificationResult(
            allowed=False,
            reasons=reasons or ["Recipient is ambiguous."],
            clarification_needed=True,
            clarification_question="Which recipient did you mean?",
        )

    return VerificationResult(allowed=not reasons, reasons=reasons)
