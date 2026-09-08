# CALIBRA-RAG — Uncertainty-Aware Retrieval and Abstention for Trustworthy RAG

**Status:** Independent research project — in progress (Sep 2026–Present)

CALIBRA-RAG studies whether a retrieval-augmented generation system should **answer, retrieve more evidence, or abstain** when retrieved context is weak, noisy, or contradictory.

## Research question

> Can retrieval-quality signals and calibrated abstention reduce confident unsupported answers under retrieval noise while preserving useful answer coverage?

## Motivation

RAG quality is not equivalent to answer correctness. A system may retrieve irrelevant evidence, retrieve mutually conflicting sources, or produce a confident answer even when support is weak. This project separates retrieval confidence from generation confidence and makes abstention a first-class outcome.

## Planned comparison

1. Standard top-k RAG
2. RAG + relevance threshold
3. RAG + evidence coverage score
4. RAG + contradiction penalty
5. CALIBRA-RAG: confidence score + retrieve-more/abstain policy

## Metrics

- answer accuracy;
- unsupported-claim rate;
- selective accuracy at different coverage levels;
- abstention precision/recall;
- expected calibration error;
- retrieval noise sensitivity;
- latency and token cost.

## Current scaffold

`src/calibration.py` implements a transparent evidence-confidence function and answer/retrieve/abstain policy for synthetic retrieval traces.

See [EXPERIMENT_PLAN.md](EXPERIMENT_PLAN.md).

## Research integrity

The current repository contains methodology and deterministic scaffolding, not claimed benchmark results.

## Related work

- URAG: A Benchmark for Uncertainty Quantification in Retrieval-Augmented Large Language Models (2026): https://arxiv.org/abs/2603.19281
- RAGCHECKER: A Fine-grained Framework for Diagnosing RAG (2024): https://arxiv.org/abs/2408.08067
