# SAGE — Small-Model-First Adaptive Routing for Tool-Using Agents

**Status:** Independent research project — in progress (Sep 2026–Present)

SAGE studies whether an agent can route structured tool tasks to a smaller language model by default and escalate only difficult or high-risk cases to a larger model.

## Research question

> Can uncertainty- and risk-aware SLM→LLM routing minimize cost per successful agent task while maintaining tool-call accuracy and acceptable tail latency?

## Motivation

Many agent actions are schema-constrained: classify intent, fill arguments, select a tool, or validate a structured response. Using the largest model for every step may waste latency and cost. The hard question is not whether smaller models are cheaper, but **when escalation is actually necessary**.

## Planned comparison

1. Large-model-only baseline
2. Small-model-only baseline
3. Static task-type routing
4. Confidence-based routing
5. SAGE: confidence + risk + complexity routing with verifier fallback

## Metrics

- task success;
- executable/schema-valid tool-call rate;
- cost per successful task;
- p50/p95 latency;
- escalation rate;
- false-escalation and missed-escalation rates;
- energy proxy where measurable.

## Current scaffold

`src/router.py` implements an interpretable routing policy over task complexity, uncertainty, and action risk.

See [EXPERIMENT_PLAN.md](EXPERIMENT_PLAN.md).

## Research integrity

No cost or performance advantage is claimed until measured on fixed model versions and task sets.

## Related work

- Small Language Models for Agentic Systems: A Survey of Architectures, Capabilities, and Deployment Trade offs (2025): https://arxiv.org/abs/2510.03847
