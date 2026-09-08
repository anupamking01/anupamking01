# MEMORA Experiment Plan

## Hypotheses

- **H1:** Hybrid retrieval improves relevant-memory recall over recency-only retrieval under fixed context budgets.
- **H2:** Explicit freshness handling reduces stale-memory errors on tasks with changing facts.
- **H3:** Memory consolidation reduces context growth while preserving task success better than naive truncation.

## Task families

Use synthetic and public long-horizon tasks containing:
- persistent preferences;
- fact updates and corrections;
- multi-session dependency chains;
- distractor interactions;
- conflicting historical evidence.

## Controlled variables

Hold model, prompt, tool set, task ordering, context budget, and retrieval depth fixed while varying the memory policy.

## Primary metrics

Task success, recall@k, stale-memory rate, tokens retained, latency, and estimated cost.

## Ablations

Remove recency, relevance, and importance terms one at a time. Vary top-k and context budgets.

## Reporting

Publish raw task specifications, random seeds, configuration, commit SHA, and per-task traces before reporting aggregate results.
