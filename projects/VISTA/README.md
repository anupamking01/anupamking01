# VISTA — Evidence-Grounded Multimodal Reasoning Verification

**Status:** Independent research project — in progress (Sep 2026–Present)

VISTA studies whether multimodal answers become more reliable when every material claim is linked to an explicit **visual/text evidence ledger** and checked for support before the final response is accepted.

## Research question

> Can evidence-region grounding plus claim-level verification reduce unsupported conclusions in document, chart, and image reasoning without making multimodal systems prohibitively slow?

## Motivation

Vision-language systems can produce plausible reasoning that is weakly tied to what is actually visible in a page, chart, or image. VISTA focuses on the gap between fluent multimodal reasoning and verifiable visual evidence.

## Planned task families

- chart question answering;
- document/table understanding;
- mathematical work shown in images;
- multi-region evidence aggregation;
- adversarial distractor regions.

## Variants

1. Direct multimodal answer
2. Chain-of-thought-style reasoning without evidence ledger
3. Evidence-region extraction + answer
4. Evidence-region extraction + claim verifier
5. VISTA with repair after failed verification

## Metrics

- answer correctness;
- claim support precision/recall;
- evidence-region coverage;
- unsupported-claim rate;
- repair success;
- latency and inference cost.

## Current scaffold

`src/evidence_verifier.py` provides typed evidence regions, claims, and deterministic support checks for experiment traces. Model-specific vision extraction will plug into this interface later.

See [EXPERIMENT_PLAN.md](EXPERIMENT_PLAN.md).

## Research integrity

No multimodal benchmark result is claimed at scaffold stage.
