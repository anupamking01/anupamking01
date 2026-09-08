# Professional AI Portfolio

Clean-room, sanitized implementations inspired by technical problem classes from my professional experience. These examples do **not** contain employer code, confidential data, customer information, or proprietary prompts. They are portfolio reproductions designed to demonstrate architecture, interfaces, evaluation thinking, and runnable local behavior.

## Included projects

1. **Multi-Agent Insurance Intelligence** — routes requests across retrieval, SQL-style analytics, and web-search interfaces, then synthesizes an answer with source traces.
2. **Multimodal Document Intelligence** — schema-first extraction pipeline for document text/vision outputs with validation and field-level quality metrics.
3. **Biomedical Knowledge-Graph RAG** — biomedical entity normalization, lightweight graph construction, retrieval, and evidence assembly.
4. **AI Mathematics Tutor & Marker** — answer parsing, step-level checks, misconception feedback, and concept-level tutoring hints.
5. **Document Fraud Intelligence** — OCR-oriented document checks, GST/RC identifier validation, QR/amount consistency, anomaly signals, and explainable risk scoring.
6. **Speech + Education AI** — transcript normalization plus Bloom's-taxonomy-aligned question generation.
7. **NLP Test-Case Automation** — converts Jira-like test descriptions into structured actions, entities, expected outcomes, and automation-ready records.
8. **Enrollment Assistant / Bedrock-ready interface** — employer/employee enrollment validation, deterministic policy gates, and a provider-neutral payload shape for Bedrock integration.
9. **Churn, Forecasting & Recommendation Analytics** — deterministic demonstration of churn risk scoring, moving-average forecasting, and category recommendation logic over synthetic events.
10. **OCR/NLP Incident Remediation** — classifies OCR text from application-error screenshots and maps detected incidents to transparent remediation runbooks.

## Run

All examples use the Python standard library so they can run without API keys.

```bash
cd projects/professional-ai-portfolio
python multi_agent_insurance.py
python document_intelligence.py
python biomedical_kg_rag.py
python math_tutor.py
python document_fraud.py
python speech_education.py
python nlp_testcase_automation.py
python enrollment_assistant.py
python ml_analytics.py
python incident_remediation.py
python -m unittest discover -s tests -v
```

## Architecture principles

- explicit schemas instead of free-form outputs;
- deterministic validation around probabilistic AI components;
- source/evidence tracing;
- modular tool boundaries;
- measurable failure modes;
- privacy-preserving synthetic examples;
- clear separation between production experience and public portfolio code.

## Extension points

The deterministic local components are intentionally provider-neutral. Production-grade extensions can plug in LangGraph/LangChain, AWS Bedrock/OpenAI, vector stores, OCR/vision models, Neo4j, Pinecone, SQL engines, speech-to-text providers, BigQuery, or external search without changing the public data model.

## Integrity note

The repository demonstrates the kinds of systems described on my resume, but it does not claim that this public code is the original employer implementation. Metrics in these demos are illustrative unless explicitly produced by the included tests.
