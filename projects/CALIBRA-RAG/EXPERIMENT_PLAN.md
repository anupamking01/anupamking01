# CALIBRA-RAG Experiment Plan

## Hypotheses

- **H1:** Confidence-aware abstention lowers unsupported-answer rate under retrieval noise.
- **H2:** Contradiction-aware confidence performs better than relevance-only thresholding.
- **H3:** Retrieve-more routing improves coverage without sacrificing selective accuracy.

## Perturbations

Evaluate clean retrieval plus controlled corruption:
- irrelevant passages;
- missing gold evidence;
- conflicting passages;
- duplicate evidence;
- stale evidence.

## Metrics

Accuracy, selective accuracy, coverage, unsupported-claim rate, ECE/Brier-style calibration measures, latency, and cost.

## Ablations

Remove contradiction penalty, support coverage, or minimum-source diversity. Sweep abstention and retrieve-more thresholds.

## Reproducibility

Freeze task sets and corruption seeds. Store retrieved contexts, scores, decisions, final outputs, and configuration with each run.
