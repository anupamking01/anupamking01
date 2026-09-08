# VERA — Verification-Guided Reliable Autonomous LLM Agents

**Status:** Independent research project — in progress (Sep 2026–Present)

VERA studies whether explicit planning, structured state validation, scoped tool permissions, self-verification, adaptive replanning, and human clarification can improve the reliability of long-horizon tool-using LLM agents.

## Research question

> How much can verification and explicit state control improve autonomous-agent task success while reducing invalid or unsafe actions, without excessive latency or inference cost?

## Motivation

LLM agents can plan, call tools, and complete multi-step workflows, but they may still act on ambiguous instructions, call the wrong tool, violate task constraints, or fail to recover after an execution error. VERA treats reliability as a systems problem rather than relying only on an additional LLM critic.

## Planned architecture

```text
User request
    |
    v
Intent / ambiguity analysis
    |
    v
Planner -> Task plan / DAG
    |
    v
Policy & permission gate
    |
    v
Executor -> Tool call
    |
    v
State validator
    |
    v
Verifier
    |
    +---- accept
    +---- re-plan / retry
    +---- request human clarification
```

The project combines LLM reasoning with deterministic checks where possible. Examples include validating tool arguments, enforcing authorization limits, checking expected state transitions, and requiring clarification before ambiguous or high-impact actions.

## Current scaffold

The initial implementation in `src/` contains:

- typed task/action/verification state models using Pydantic;
- deterministic policy checks for authorization and ambiguous actions;
- a verifier interface for precondition and state-transition validation;
- unit tests for core safety-policy behavior.

## Planned experimental comparison

VERA will be compared with progressively stronger baselines:

1. ReAct-style tool-using agent
2. Plan-and-execute agent
3. Planner + verifier
4. Planner + verifier + state validation
5. Full VERA with scoped permissions, recovery, and clarification

See [`EXPERIMENT_PLAN.md`](EXPERIMENT_PLAN.md) for the current study design.

## Evaluation metrics

- task completion / scenario success;
- invalid or disallowed tool-action rate;
- recovery success after injected failures;
- clarification precision and unnecessary-clarification rate;
- number of tool calls / reasoning steps;
- latency;
- token usage and estimated inference cost.

## Reproducibility and research integrity

This repository intentionally does **not** claim benchmark improvements before the experiments are completed. Results, ablations, plots, and failure analysis will be added only after reproducible evaluation.

## Research interests supported by this project

Reliable autonomous agents • LLM reasoning and planning • trustworthy AI • agent evaluation • human-agent interaction • efficient AI systems
