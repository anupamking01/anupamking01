# Anupam Poddar

**AI/ML Engineer · Generative AI · Agentic AI · RAG · LLM Evaluation**

I build AI systems for **retrieval, document intelligence, and tool-using workflows**. My professional work spans multi-agent assistants, structured extraction, and educational AI; my research explores **reliable agents, trustworthy retrieval, and quality–latency–cost trade-offs**.

**Open to:** remote AI/ML consulting, contract opportunities, and research collaboration.  
**Academic goal:** MS in Computer Science, Spring 2027.

[Runnable portfolio](#applied-ai-experience-and-examples) · [Publication](#publication) · [Research](#research-in-progress) · [Open source](#open-source-engineering) · [LinkedIn](https://www.linkedin.com/in/anupam-king01) · [Email](mailto:anupampoddar1@gmail.com)

## Start here

**Research reviewers:** begin with the agent study and published work. **Engineering reviewers:** start with the runnable portfolio, its tests, and the upstream pull requests below.

| Explore | What you can review | Current stage |
| --- | --- | --- |
| **[AI Research Agent](https://github.com/anupamking01/Ai-Researcher-Agent)** | Web-research system with source tracking and a **40-run study** of retrieval, planning, and verification. [Study overview](https://github.com/anupamking01/Ai-Researcher-Agent/blob/d5d9fcd4762092c4a79f2e830d1f688dfe1f9cc8/README.md) · [Automated results](https://github.com/anupamking01/Ai-Researcher-Agent/blob/d5d9fcd4762092c4a79f2e830d1f688dfe1f9cc8/paper/MAIN_STUDY_INFERENCE.md) | Experimental system; study on a draft branch |
| **[Published research](#publication)** | Co-authored work on technical/non-technical skill extraction and project-team allocation. [Publisher record](https://link.springer.com/chapter/10.1007/978-981-15-1366-4_14) · [BibTeX](https://github.com/anupamking01/anupamking01/blob/main/publications.bib) | Springer, 2020; separate from the current agent research |
| **[Professional AI Portfolio](https://github.com/anupamking01/anupamking01/tree/main/projects/professional-ai-portfolio)** | **10 Python examples** illustrating routing, document validation, retrieval, tutoring, and analytics with synthetic data. [Quick start and scope](https://github.com/anupamking01/anupamking01/blob/main/projects/professional-ai-portfolio/README.md) · [Smoke tests](https://github.com/anupamking01/anupamking01/blob/main/projects/professional-ai-portfolio/tests/test_portfolio.py) | Deterministic local demonstrations |
| **[VERA](https://github.com/anupamking01/anupamking01/tree/main/projects/VERA)** | Typed agent state, permission checks, and action validation. [Code](https://github.com/anupamking01/anupamking01/tree/main/projects/VERA/src) · [Study design](https://github.com/anupamking01/anupamking01/blob/main/projects/VERA/EXPERIMENT_PLAN.md) | Research scaffold; experiments planned |

## Publication

**[Extraction of Technical and Non-technical Skills for Optimal Project-Team Allocation](https://link.springer.com/chapter/10.1007/978-981-15-1366-4_14)**  
Kanika Bhatia, Shampa Chakraverty, Sushama Nagpal, Amit Kumar, Mohit Lamba, and **Anupam Poddar**.  
*Machine Intelligence and Signal Processing*, MISP 2019, Advances in Intelligent Systems and Computing, vol. 1085, pp. 173–184. Springer, **2020**.  
**DOI:** `10.1007/978-981-15-1366-4_14` · [BibTeX citation](https://github.com/anupamking01/anupamking01/blob/main/publications.bib)

The work investigates technical and non-technical skill extraction and project-team matching using formal concept analysis and a project-oriented stable marriage algorithm.

## Applied AI: experience and examples

My professional experience covers **RAG/SQL/web-search assistants**, **LangGraph workflows**, **schema-first document extraction**, and **AI tutoring and answer evaluation**.

Explore these small, runnable examples of the underlying problem classes:

| Problem | Public code | What the example demonstrates |
| --- | --- | --- |
| Multi-agent routing | [Insurance assistant](https://github.com/anupamking01/anupamking01/blob/main/projects/professional-ai-portfolio/multi_agent_insurance.py) | Rule-based routing across retrieval, analytics, and web interfaces, with source traces |
| Document intelligence | [Extraction and validation](https://github.com/anupamking01/anupamking01/blob/main/projects/professional-ai-portfolio/document_intelligence.py) | Structured records, field validation, and field-level comparison |
| Educational AI | [Math tutor and marker](https://github.com/anupamking01/anupamking01/blob/main/projects/professional-ai-portfolio/math_tutor.py) | Step-token matching and feedback in a small local demonstration |

The [full portfolio](https://github.com/anupamking01/anupamking01/tree/main/projects/professional-ai-portfolio) uses synthetic inputs and provider-neutral interfaces. These are clean-room demonstrations of professional problem classes; employer implementations remain separate.

### Try an example

**Python 3.10+** for the complete portfolio and test suite; standard library only; no API key required.

```bash
git clone https://github.com/anupamking01/anupamking01.git
cd anupamking01/projects/professional-ai-portfolio
python3 multi_agent_insurance.py
python3 document_intelligence.py
python3 math_tutor.py
python3 -m unittest discover -s tests -v
```

See the [portfolio README](https://github.com/anupamking01/anupamking01/blob/main/projects/professional-ai-portfolio/README.md) for all ten examples, expected outputs, implementation boundaries, and verification scope. The current suite contains seven smoke tests for local deterministic behavior—not production integrations or model quality.

## Research in progress

### Where should a research agent spend its budget?

My **AI Research Agent** study compares **10 tasks × 4 variants = 40 treatment runs**: direct retrieval at two browse budgets, planning, and planning with verification.

**Automated analysis is complete; blinded human evaluation remains pending.** The three primary comparisons did not establish statistically significant gains on this small original live-web task set. The project remains an in-progress research artifact, with its study changes tracked in [draft PR #1](https://github.com/anupamking01/Ai-Researcher-Agent/pull/1).

[Analysis plan](https://github.com/anupamking01/Ai-Researcher-Agent/blob/d5d9fcd4762092c4a79f2e830d1f688dfe1f9cc8/paper/ANALYSIS_PLAN.md) · [Frozen automated results](https://github.com/anupamking01/Ai-Researcher-Agent/blob/d5d9fcd4762092c4a79f2e830d1f688dfe1f9cc8/paper/MAIN_STUDY_INFERENCE.md) · [Human evaluation protocol](https://github.com/anupamking01/Ai-Researcher-Agent/blob/d5d9fcd4762092c4a79f2e830d1f688dfe1f9cc8/paper/HUMAN_EVAL_PROTOCOL.md)

<details>
<summary><strong>Study methodology and reproducibility</strong></summary>

The research branch includes:

- a common post-hoc evidence-support evaluator, separate from treatment-time verification;
- source provenance and token, latency, model-call, and cost accounting;
- a frozen paired analysis with bootstrap confidence intervals, exact sign-flip tests, and multiple-comparison adjustment;
- deterministic blinded evaluation packets and tooling to freeze human ratings before unblinding.

</details>

**VERA — Verification-Guided Reliable Autonomous LLM Agents** explores whether explicit state validation, scoped permissions, verification, and recovery improve long-horizon agent reliability. Its current scaffold contains Pydantic state models, deterministic policy checks, and verifier tests.

## Open-source engineering

I contribute focused reliability fixes and regression coverage to AI tooling. Selected upstream pull requests:

| Project | Engineering focus | Evidence |
| --- | --- | --- |
| **GPT Researcher** | Preserve accumulated state when deep research generates no queries | [PR #2111](https://github.com/assafelovic/gpt-researcher/pull/2111) |
| **GPT Researcher** | Keep failed-search metadata separate from previous source provenance | [PR #2131](https://github.com/assafelovic/gpt-researcher/pull/2131) |
| **GPT Researcher** | Bound external requests and handle transport or malformed-response failures | [Bing #2133](https://github.com/assafelovic/gpt-researcher/pull/2133) · [Semantic Scholar #2130](https://github.com/assafelovic/gpt-researcher/pull/2130) |
| **Pydantic AI** | Snapshot per-call metadata at deferred-tool ownership boundaries | [Draft PR #8366](https://github.com/pydantic/pydantic-ai/pull/8366) |

**Status checked 25 September 2026:** the highlighted GPT Researcher PRs are open; the Pydantic AI PR is an open draft. All are awaiting upstream acceptance. [Contribution log, additional PRs, and verification limits](https://github.com/anupamking01/anupamking01/blob/main/OPEN_SOURCE.md).

## Technical focus

**Agents & retrieval:** Python, LangGraph, LangChain, Pydantic, RAG, vector search, knowledge graphs, AWS Bedrock.  
**ML & multimodal:** PyTorch, TensorFlow, scikit-learn, Hugging Face, NLP, OCR, OpenCV.  
**Engineering & data:** FastAPI, SQL, Docker, Git, AWS, PostgreSQL/pgvector, Neo4j, Pinecone, Weaviate.

<details>
<summary><strong>Additional research explorations</strong></summary>

These are early experimental scaffolds and study plans, not completed papers or validated benchmark results.

| Exploration | Research question |
| --- | --- |
| [MEMORA](https://github.com/anupamking01/anupamking01/tree/main/projects/MEMORA) | Which memory policies help long-horizon agents under bounded context windows? |
| [CALIBRA-RAG](https://github.com/anupamking01/anupamking01/tree/main/projects/CALIBRA-RAG) | When should a retrieval system answer, seek more evidence, or abstain? |
| [VISTA](https://github.com/anupamking01/anupamking01/tree/main/projects/VISTA) | Can evidence-grounded verification reduce unsupported multimodal conclusions? |
| [SAGE](https://github.com/anupamking01/anupamking01/tree/main/projects/SAGE) | When should tool-using agents escalate from smaller to larger models? |

</details>

<details>
<summary><strong>Earlier projects and coding profiles</strong></summary>

Earlier work is kept separate from active research; inclusion here does not imply a novel method or a currently maintained production service.

- [End-to-End RAG](https://github.com/anupamking01/End_to_End_Rag) — tutorial-style local PDF retrieval and generation workflow.
- [CHAT-PDF](https://github.com/anupamking01/CHAT-PDF) — legacy PDF question-answering application.
- [Nutrify](https://github.com/anupamking01/Nutrify), [Loan Default Prediction](https://github.com/anupamking01/Loan-Default-prediction), and [Garment Search Engine](https://github.com/anupamking01/Garment-search-Engine).

[LeetCode](https://leetcode.com/anupamking01/) · [HackerRank](https://www.hackerrank.com/anupampoddar1997) · [CodeChef](https://www.codechef.com/users/anupamp11) · [GeeksforGeeks](https://www.geeksforgeeks.org/profile/champgamy?tab=activity) · [Certificates](https://drive.google.com/drive/folders/1Q9E4g6cW3UR6QDN-dkId6tt_08j53bYU?usp=sharing)

</details>

## Let's connect

For **remote AI/ML consulting or contract work**, contact me about RAG, agent workflows, document intelligence, or LLM evaluation. For **research collaboration**, my interests include reliable agents and trustworthy retrieval.

[Email: anupampoddar1@gmail.com](mailto:anupampoddar1@gmail.com) · [LinkedIn](https://www.linkedin.com/in/anupam-king01)
