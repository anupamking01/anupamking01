from collections import defaultdict, deque
from dataclasses import dataclass
from typing import Dict, List, Set, Tuple


@dataclass(frozen=True)
class Entity:
    text: str
    kind: str


class BiomedicalKGRAG:
    """Clean-room biomedical entity + lightweight knowledge-graph retrieval demo."""

    def __init__(self):
        self.graph: Dict[str, Set[Tuple[str, str]]] = defaultdict(set)
        self.documents: Dict[str, str] = {}

    @staticmethod
    def normalize_entity(text: str) -> str:
        return " ".join(text.lower().strip().split())

    def add_relation(self, source: str, relation: str, target: str) -> None:
        s, t = self.normalize_entity(source), self.normalize_entity(target)
        self.graph[s].add((relation, t))
        self.graph[t].add((f"inverse:{relation}", s))

    def add_document(self, doc_id: str, text: str) -> None:
        self.documents[doc_id] = text

    def graph_context(self, entity: str, depth: int = 1) -> List[str]:
        start = self.normalize_entity(entity)
        queue = deque([(start, 0)])
        seen = {start}
        facts = []
        while queue:
            node, level = queue.popleft()
            if level >= depth:
                continue
            for relation, target in sorted(self.graph.get(node, set())):
                facts.append(f"{node} --{relation}--> {target}")
                if target not in seen:
                    seen.add(target)
                    queue.append((target, level + 1))
        return facts

    def retrieve_documents(self, query: str, limit: int = 3) -> List[Tuple[str, str]]:
        terms = set(self.normalize_entity(query).split())
        scored = []
        for doc_id, text in self.documents.items():
            score = len(terms & set(self.normalize_entity(text).split()))
            if score:
                scored.append((score, doc_id, text))
        scored.sort(reverse=True)
        return [(doc_id, text) for _, doc_id, text in scored[:limit]]

    def evidence_pack(self, query: str, anchor_entity: str) -> dict:
        return {
            "query": query,
            "graph_facts": self.graph_context(anchor_entity, depth=2),
            "documents": self.retrieve_documents(query),
        }


if __name__ == "__main__":
    rag = BiomedicalKGRAG()
    rag.add_relation("metformin", "treats", "type 2 diabetes")
    rag.add_relation("type 2 diabetes", "associated_with", "hyperglycemia")
    rag.add_document("demo-1", "Metformin is commonly used in type 2 diabetes management.")
    print(rag.evidence_pack("metformin diabetes", "metformin"))
