# MEMORA — Memory Policies for Long-Horizon LLM Agents

**Status:** Independent research project — in progress (Sep 2026–Present)

MEMORA studies how an LLM agent should **write, retain, retrieve, and retire memory** when completing long-horizon tasks under a bounded context window.

## Research question

> Can an adaptive memory policy preserve task-relevant evidence and improve long-horizon consistency compared with recency-only, similarity-only, and summary-only memory baselines, without excessive latency or token cost?

## Motivation

Long-horizon agents cannot keep every interaction in working context. Memory systems therefore make consequential choices about what to store, what to compress, and what to retrieve. Those choices create trade-offs among recall, freshness, latency, cost, and error propagation.

MEMORA treats memory as an experimentally measurable subsystem rather than an unbounded vector store.

## Planned comparison

1. Full-history oracle (upper-bound context)
2. Sliding-window / recency baseline
3. Similarity-only retrieval
4. Summary-only memory
5. Hybrid recency + relevance + importance policy
6. Adaptive policy with memory consolidation

## Metrics

- task success;
- relevant-memory recall@k;
- stale/conflicting-memory retrieval rate;
- context tokens consumed;
- memory write/read latency;
- estimated inference cost;
- performance as task horizon grows.

## Current scaffold

`src/memory_policy.py` implements a deterministic hybrid ranking policy over synthetic memory items. It is intentionally model-independent so the evaluation harness can be tested before connecting an LLM.

See [EXPERIMENT_PLAN.md](EXPERIMENT_PLAN.md).

## Research integrity

No benchmark improvement is claimed yet. Results will be added only after a fixed task set, model configuration, and reproducible evaluation protocol are established.

## Related work

- Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads (2026): https://arxiv.org/abs/2606.06448
- Memex(RL): Scaling Long-Horizon LLM Agents via Indexed Experience Memory (2026): https://arxiv.org/abs/2603.04257
