from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class ToolAction(BaseModel):
    tool_name: str
    arguments: Dict[str, Any] = Field(default_factory=dict)
    risk_level: RiskLevel = RiskLevel.LOW
    requires_confirmation: bool = False


class TaskState(BaseModel):
    objective: str
    authorized_tools: List[str] = Field(default_factory=list)
    authorized_limits: Dict[str, Any] = Field(default_factory=dict)
    known_entities: Dict[str, Any] = Field(default_factory=dict)
    pending_clarification: Optional[str] = None


class VerificationResult(BaseModel):
    allowed: bool
    reasons: List[str] = Field(default_factory=list)
    clarification_needed: bool = False
    clarification_question: Optional[str] = None
