# Anupam Poddar

**AI/ML Engineer · Agentic AI · Retrieval-Augmented Generation · LLM Evaluation**

I build AI systems that connect language models with tools, structured data, and evidence. My experience spans data science, machine learning, and applied generative AI; my research interests center on **reliable autonomous agents, trustworthy retrieval, and the quality–latency–cost trade-off**.

Preparing for **MS in Computer Science, Spring 2027**. Open to research collaboration and remote AI/ML consulting or contract opportunities.

[LinkedIn](https://www.linkedin.com/in/anupam-king01) · [Publication](#publication) · [Open source](#open-source-engineering) · [Research](#research-in-progress) · [Contact](mailto:anupampoddar1@gmail.com)

## Featured work

| Project | What to explore | Status |
| --- | --- | --- |
| **[AI Research Agent](https://github.com/anupamking01/Ai-Researcher-Agent)** | Planner–execution web research, source tracking, streamed reports, and offline evaluation utilities. [Architecture](https://github.com/anupamking01/Ai-Researcher-Agent/blob/main/docs/ARCHITECTURE.md) · [Evaluation protocol](https://github.com/anupamking01/Ai-Researcher-Agent/blob/main/docs/EVALUATION.md) | Experimental research system |
| **[VERA](https://github.com/anupamking01/anupamking01/tree/main/projects/VERA)** | Verification-guided agents: typed state, permission checks, action validation, and an explicit experimental plan. [Code](https://github.com/anupamking01/anupamking01/tree/main/projects/VERA/src) · [Study design](https://github.com/anupamking01/anupamking01/blob/main/projects/VERA/EXPERIMENT_PLAN.md) | Research scaffold; in progress |
| **[Professional AI Portfolio](https://github.com/anupamking01/anupamking01/tree/main/projects/professional-ai-portfolio)** | Ten clean-room Python demonstrations covering multi-agent routing, document intelligence, knowledge-graph retrieval, tutoring, and analytics. | Deterministic local examples |

## Publication

**[Extraction of Technical and Non-technical Skills for Optimal Project-Team Allocation](https://link.springer.com/chapter/10.1007/978-981-15-1366-4_14)**  
Kanika Bhatia, Shampa Chakraverty, Sushama Nagpal, Amit Kumar, Mohit Lamba, and **Anupam Poddar**.  
*Machine Intelligence and Signal Processing*, MISP 2019, Advances in Intelligent Systems and Computing, vol. 1085, pp. 173–184. Springer, **2020**.  
**DOI:** `10.1007/978-981-15-1366-4_14`

The work investigates technical and non-technical skill extraction and project-team matching using formal concept analysis and a project-oriented stable marriage algorithm.

## Open-source engineering

I contribute focused reliability fixes and regression coverage to AI tooling. Selected upstream pull requests:

| Project | Engineering focus | Evidence |
| --- | --- | --- |
| **GPT Researcher** | Preserve accumulated state when deep research generates no queries | [PR #2111](https://github.com/assafelovic/gpt-researcher/pull/2111) |
| **GPT Researcher** | Keep failed-search metadata separate from previous source provenance | [PR #2131](https://github.com/assafelovic/gpt-researcher/pull/2131) |
| **GPT Researcher** | Bound external requests and handle transport or malformed-response failures | [Bing #2133](https://github.com/assafelovic/gpt-researcher/pull/2133) · [Semantic Scholar #2130](https://github.com/assafelovic/gpt-researcher/pull/2130) |
| **Pydantic AI** | Snapshot per-call metadata at deferred-tool ownership boundaries | [Draft PR #8366](https://github.com/pydantic/pydantic-ai/pull/8366) |

These are **submitted contributions, not claims of upstream acceptance**. The highlighted GPT Researcher PRs are open and the Pydantic AI PR is a draft as of **25 September 2026**. [Contribution log, additional PRs, and verification limits](https://github.com/anupamking01/anupamking01/blob/main/OPEN_SOURCE.md).

## Research in progress

**VERA — Verification-Guided Reliable Autonomous LLM Agents** asks whether planning, explicit state validation, scoped permissions, verification, and recovery can improve long-horizon agent reliability without excessive inference cost. The current public scaffold includes Pydantic state models, deterministic policy checks, and verifier tests; the broader comparison is documented as planned work.

**AI Research Agent** provides a complementary web-research workflow for investigating source coverage, failure modes, latency, token usage, and report quality. Its README acknowledges the project's GPT Researcher architectural lineage.

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

## Professional experience → public demonstrations

My professional work includes multi-agent conversational systems combining RAG, SQL, and web search; a LangGraph-based replacement for a legacy RASA workflow; schema-first document extraction; and AI tutoring and answer-evaluation systems. Other applied work spans knowledge-graph retrieval, OCR/NLP, forecasting, recommendations, and fraud detection.

The [public portfolio](https://github.com/anupamking01/anupamking01/tree/main/projects/professional-ai-portfolio) illustrates these problem classes with synthetic inputs and provider-neutral interfaces. **It is not employer source code or a set of production deployments**; its local examples do not require model API keys.

## Technical focus

**Agentic AI & retrieval:** Python, LangGraph, LangChain, Pydantic, RAG, vector search, knowledge graphs, AWS Bedrock.  
**ML & multimodal systems:** PyTorch, TensorFlow, scikit-learn, Hugging Face, NLP, OCR, OpenCV.  
**Engineering & data:** FastAPI, SQL, Docker, Git, AWS, PostgreSQL/pgvector, Neo4j, Pinecone, Weaviate.

<details>
<summary><strong>Earlier projects and coding profiles</strong></summary>

Earlier work is kept separate from active research; inclusion here does not imply a novel method or a currently maintained production service.

- [End-to-End RAG](https://github.com/anupamking01/End_to_End_Rag) — tutorial-style local PDF retrieval and generation workflow.
- [CHAT-PDF](https://github.com/anupamking01/CHAT-PDF) — legacy PDF question-answering application.
- [Nutrify](https://github.com/anupamking01/Nutrify), [Loan Default Prediction](https://github.com/anupamking01/Loan-Default-prediction), and [Garment Search Engine](https://github.com/anupamking01/Garment-search-Engine).

[LeetCode](https://leetcode.com/anupamking01/) · [HackerRank](https://www.hackerrank.com/anupampoddar1997) · [CodeChef](https://www.codechef.com/users/anupamp11) · [GeeksforGeeks](https://www.geeksforgeeks.org/profile/champgamy?tab=activity) · [Certificates](https://drive.google.com/drive/folders/1Q9E4g6cW3UR6QDN-dkId6tt_08j53bYU?usp=sharing)

</details>

## Let's connect

For research collaboration in reliable agents and trustworthy RAG, or consulting on agent workflows, document intelligence, and retrieval systems: **[anupampoddar1@gmail.com](mailto:anupampoddar1@gmail.com)** · **[LinkedIn](https://www.linkedin.com/in/anupam-king01)**.
