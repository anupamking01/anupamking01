# SAGE Experiment Plan

## Hypotheses

- **H1:** Small-model-first routing reduces cost per successful task versus large-model-only execution.
- **H2:** Risk-aware escalation preserves high-impact tool accuracy better than confidence-only routing.
- **H3:** A lightweight verifier reduces missed escalations without eliminating cost savings.

## Task categories

- schema extraction;
- API/function selection;
- argument filling;
- retrieval query generation;
- multi-step tool planning;
- high-impact action validation.

## Experimental controls

Fix prompts, tools, temperature, retry budget, and task set across routing policies.

## Metrics

Success, schema validity, executable-call rate, cost per successful task, p50/p95 latency, escalation rate, and verifier overhead.

## Ablations

Remove risk, uncertainty, or complexity terms. Sweep escalation thresholds and verifier strictness.

## Reproducibility

Record exact model identifiers, prices used for cost calculation, hardware/API configuration, task version, and commit SHA.
