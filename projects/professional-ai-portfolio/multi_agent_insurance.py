from dataclasses import dataclass
from typing import Callable, Dict, List


@dataclass
class ToolResult:
    tool: str
    answer: str
    sources: List[str]


class MultiAgentInsuranceAssistant:
    """Provider-neutral clean-room demo of RAG + SQL + web agent routing."""

    def __init__(self, tools: Dict[str, Callable[[str], ToolResult]]):
        self.tools = tools

    def route(self, query: str) -> List[str]:
        q = query.lower()
        selected = []
        if any(k in q for k in ("policy", "coverage", "document", "wording")):
            selected.append("rag")
        if any(k in q for k in ("count", "premium", "claim", "portfolio", "average")):
            selected.append("sql")
        if any(k in q for k in ("latest", "market", "regulation", "news")):
            selected.append("web")
        return selected or ["rag"]

    def answer(self, query: str) -> dict:
        tool_results = [self.tools[name](query) for name in self.route(query)]
        evidence = " | ".join(result.answer for result in tool_results)
        return {
            "query": query,
            "agents_used": [r.tool for r in tool_results],
            "answer": evidence,
            "sources": sorted({s for r in tool_results for s in r.sources}),
        }


def _rag(_: str) -> ToolResult:
    return ToolResult("rag", "Policy wording says flood cover is subject to the declared limit.", ["policy_demo.pdf#p12"])


def _sql(_: str) -> ToolResult:
    return ToolResult("sql", "Synthetic portfolio: 14 open claims, average reserve 18,250.", ["synthetic_claims.csv"])


def _web(_: str) -> ToolResult:
    return ToolResult("web", "External market lookup interface executed in demo mode.", ["demo://market-source"])


if __name__ == "__main__":
    assistant = MultiAgentInsuranceAssistant({"rag": _rag, "sql": _sql, "web": _web})
    print(assistant.answer("What is the flood coverage and average open-claim reserve?"))
