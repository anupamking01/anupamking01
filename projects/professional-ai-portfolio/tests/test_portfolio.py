import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from multi_agent_insurance import MultiAgentInsuranceAssistant, ToolResult
from document_intelligence import extract_fields, validate
from biomedical_kg_rag import BiomedicalKGRAG
from math_tutor import MathTutorMarker
from document_fraud import DocumentFraudIntelligence
from speech_education import generate_questions, normalize_transcript
from nlp_testcase_automation import parse_step


class PortfolioSmokeTests(unittest.TestCase):
    def test_multi_agent_routes_sql_and_rag(self):
        tools = {
            "rag": lambda q: ToolResult("rag", "r", ["doc"]),
            "sql": lambda q: ToolResult("sql", "s", ["db"]),
            "web": lambda q: ToolResult("web", "w", ["web"]),
        }
        out = MultiAgentInsuranceAssistant(tools).answer("policy coverage and average claim")
        self.assertEqual(out["agents_used"], ["rag", "sql"])

    def test_document_schema_validation(self):
        record = extract_fields("Name: Asha | Member ID: ABC12 | Coverage: 1000")
        self.assertFalse(validate(record))

    def test_graph_context(self):
        graph = BiomedicalKGRAG()
        graph.add_relation("drug-a", "treats", "condition-b")
        self.assertTrue(graph.graph_context("drug-a"))

    def test_math_marker(self):
        result = MathTutorMarker().mark(["x = 3"], ["x = 3"])
        self.assertEqual(result.score, 1.0)

    def test_fraud_amount_mismatch(self):
        out = DocumentFraudIntelligence().inspect({"amount": 100, "qr_amount": 50})
        self.assertEqual(out["decision"], "review")

    def test_bloom_and_transcript(self):
        self.assertIn("hypertension", normalize_transcript("hy per tension"))
        self.assertEqual(generate_questions("RAG", ["apply"])[0].bloom_level, "apply")

    def test_nlp_action_parse(self):
        action = parse_step("Click login button")
        self.assertEqual(action.verb, "click")


if __name__ == "__main__":
    unittest.main()
