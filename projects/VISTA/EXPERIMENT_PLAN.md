# VISTA Experiment Plan

## Hypotheses

- **H1:** Requiring evidence IDs for claims reduces unsupported-answer rate.
- **H2:** Claim-level verification improves reliability more than answer-level self-critique alone.
- **H3:** Targeted repair of unsupported claims is more efficient than regenerating the entire answer.

## Dataset plan

Use public chart/document/math-image datasets plus a small controlled set where evidence regions and distractors are explicitly annotated.

## Evaluation

Measure final-answer correctness and whether each answer claim is actually supported by referenced evidence.

## Ablations

Remove evidence ledger, remove claim verifier, remove repair, and vary the maximum number of evidence regions.

## Logging

Each run should retain model/version, prompt, image/document ID, evidence regions, claim-to-region links, verifier decisions, latency, and token usage.
