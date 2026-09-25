# Professional AI Portfolio

**10 deterministic Python demonstrations of routing, structured data, evidence handling, and validation.**

These clean-room examples illustrate problem classes from my professional AI/ML work. They use synthetic inputs and local, provider-neutral components: **no API key, paid service, or model download is required**. They are not employer implementations or production deployments.

[Profile and research](../../README.md) · [Source files](.) · [Smoke tests](tests/test_portfolio.py)

## Start with these three examples

| Review focus | Code | What is implemented | Boundary to keep in mind |
| --- | --- | --- | --- |
| Tool routing and provenance | [Multi-agent insurance assistant](multi_agent_insurance.py) | Keyword-based routing, typed tool results, answer assembly, and deduplicated source identifiers | Retrieval, SQL, and web tools return synthetic responses; no live database, search, or LLM is called |
| Structured document processing | [Document intelligence](document_intelligence.py) | Delimited-text parsing into a dataclass, field validation, and exact-match field comparison | This is not an OCR/vision model or a learned document extractor |
| Educational feedback | [Math tutor and marker](math_tutor.py) | Reference-step token overlap, matched/missing-step feedback, and a templated hint | Token overlap is a heuristic, not mathematical equivalence checking or validated automated grading |

## Quick start

Use **Python 3.10 or later** for the complete portfolio and test suite. Some modules use `X | None` type annotations, which require Python 3.10+. The examples use only the standard library.

```bash
python3 --version

git clone https://github.com/anupamking01/anupamking01.git
cd anupamking01/projects/professional-ai-portfolio

python3 multi_agent_insurance.py
python3 document_intelligence.py
python3 math_tutor.py

python3 -m unittest discover -s tests -v
```

On Windows, use `py -3` in place of `python3` when appropriate for your installation.

The routing demo reports `['rag', 'sql']` for its included coverage-and-claims question. The document demo prints an `ApplicationRecord` followed by `validation: {}`. The math demo reports a score of `0.5` for its included steps; this is an illustrative token-overlap score, not an accuracy benchmark.

## All examples

| Example | Implementation | Local demonstration |
| --- | --- | --- |
| Multi-agent insurance intelligence | [multi_agent_insurance.py](multi_agent_insurance.py) | Routing across synthetic retrieval, analytics, and web interfaces |
| Document intelligence | [document_intelligence.py](document_intelligence.py) | Structured records, field validation, and field-level comparison |
| Biomedical knowledge-graph retrieval | [biomedical_kg_rag.py](biomedical_kg_rag.py) | Entity normalization, graph traversal, lexical document retrieval, and evidence assembly |
| Mathematics tutor and marker | [math_tutor.py](math_tutor.py) | Step-token matching, missing-step feedback, and hints |
| Document consistency checks | [document_fraud.py](document_fraud.py) | Identifier-format checks and weighted signals over supplied fields, including amount mismatches |
| Transcript and education utilities | [speech_education.py](speech_education.py) | Text normalization and Bloom-level question templates |
| NLP test-case automation | [nlp_testcase_automation.py](nlp_testcase_automation.py) | Rule-based conversion of written steps into structured actions and entities |
| Enrollment assistant | [enrollment_assistant.py](enrollment_assistant.py) | Enrollment validation, policy checks, and a provider-neutral integration payload |
| Churn, forecasting, and recommendation analytics | [ml_analytics.py](ml_analytics.py) | Deterministic analytics over synthetic events |
| Incident remediation | [incident_remediation.py](incident_remediation.py) | Classification of supplied incident text and runbook selection |

Run another example from this directory with `python3 <filename>.py`.

## Tests and verification scope

The existing [test suite](tests/test_portfolio.py) contains **seven smoke tests** covering routing, document validation, graph context, step matching, amount-mismatch handling, transcript/question utilities, and action parsing.

**Local verification, 25 September 2026:** all seven smoke tests and the three quick-start demos passed under Python **3.13.5**. The eight source/test files used for the suite were checked against their GitHub blob hashes before execution. The documented minimum of Python 3.10 follows from the code's syntax; this verification did not run a Python 3.10 interpreter or a multi-version compatibility matrix.

These tests are not comprehensive coverage. In particular, the current suite does not include dedicated tests for enrollment, analytics, or incident remediation. Passing smoke tests does not establish real-world model quality, security, clinical validity, or production readiness.

## Design choices

The examples make data structures and tool boundaries inspectable, retain source identifiers where relevant, and put deterministic checks around inputs and outputs. Synthetic data keeps the demonstrations separate from employer systems and customer information.

A production extension would require real provider adapters, secret management, access controls, input/error handling, persistence, observability, and evaluation on representative data. LangGraph/LangChain, AWS Bedrock, vector databases, OCR/vision models, SQL, and speech services are possible integration directions—not dependencies or completed integrations of these local examples.

## Limitations and provenance

The code demonstrates software structure and selected workflows, not novel trained models. Biomedical examples are illustrative and are not medical guidance. Document risk scores are hand-set heuristics, not calibrated fraud probabilities or official identifier verification. Educational scores are not validated assessment instruments.

No employer code, confidential customer data, proprietary prompts, or production credentials are included. Professional experience and these public demonstrations should be evaluated separately.
