# VERA Experiment Plan

## Objective

Evaluate whether explicit verification, state validation, scoped tool permissions, adaptive replanning, and human clarification improve the reliability of long-horizon LLM agents.

## Baselines

- ReAct-style tool-using agent
- Plan-and-execute agent
- Planner + verifier
- Planner + verifier + state validator
- Full VERA

## Experimental factors

The current plan is to vary the following components independently and in combination:

- explicit task decomposition / planning;
- typed tool arguments;
- deterministic precondition checks;
- post-action state validation;
- scoped tool permissions;
- verifier / critic stage;
- adaptive retry / replanning;
- ambiguity-triggered human clarification.

## Metrics

Primary metrics:

- task completion rate;
- invalid/disallowed action rate;
- recovery rate after injected failures;
- clarification precision;
- unnecessary clarification rate.

Efficiency metrics:

- total tool calls;
- reasoning steps;
- latency;
- input/output token usage;
- estimated inference cost.

## Failure categories

Planned error analysis will categorize failures such as:

- incorrect tool selection;
- invalid tool arguments;
- constraint violation;
- stale or inconsistent state;
- hallucinated intermediate facts;
- execution failure without recovery;
- unnecessary tool execution;
- failure to request clarification;
- excessive clarification;
- premature task termination.

## Ablation study

The study will remove one component at a time from the full architecture to estimate its marginal contribution:

- VERA minus verifier;
- VERA minus state validation;
- VERA minus scoped permissions;
- VERA minus clarification;
- VERA minus adaptive replanning.

## Reporting policy

No performance improvement will be reported until it is supported by reproducible experiment logs. Raw experiment outputs, evaluation scripts, plots, and a concise technical report will be added as the study progresses.
