from projects.VERA.src.models import TaskState, ToolAction
from projects.VERA.src.verifier import verify_action


def test_blocks_unauthorized_tool():
    state = TaskState(objective="send report", authorized_tools=["search"])
    action = ToolAction(tool_name="send_email", arguments={"recipient": "a@example.com"})
    result = verify_action(state, action)
    assert result.allowed is False


def test_blocks_amount_over_limit():
    state = TaskState(
        objective="make approved payment",
        authorized_tools=["transfer_money"],
        authorized_limits={"max_amount": 2000},
    )
    action = ToolAction(tool_name="transfer_money", arguments={"amount": 5000})
    result = verify_action(state, action)
    assert result.allowed is False


def test_requests_clarification_for_ambiguous_recipient():
    state = TaskState(objective="send report", authorized_tools=["send_email"])
    action = ToolAction(
        tool_name="send_email",
        arguments={"recipient": "AMBIGUOUS"},
    )
    result = verify_action(state, action)
    assert result.clarification_needed is True


def test_allows_valid_action():
    state = TaskState(
        objective="make approved payment",
        authorized_tools=["transfer_money"],
        authorized_limits={"max_amount": 2000},
    )
    action = ToolAction(tool_name="transfer_money", arguments={"amount": 1500})
    result = verify_action(state, action)
    assert result.allowed is True
