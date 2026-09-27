# `validation`: Evaluation / Historical Validation

**Status:** Planned. Not implemented yet.

## Purpose

This module will implement the **Evaluation / Historical Validation** stage of the [preliminary architecture](../../docs/architecture.md). It will measure how well the synthetic population and the simulation outputs agree with reference statistics or historical observations, before any results are reported.

## Planned responsibilities

- **Statistical similarity:** compare the synthetic population's distributions with the source statistics.
- **Historical validation:** compare simulated aggregate indicators with known aggregate or historical data, where suitable and permitted data is available.
- **Scenario consistency:** check, for example, that a scenario with no change reproduces the baseline, and that scenario effects are consistent across random seeds.
- **Model comparison:** compare the agent-based model with simpler alternatives.
- Calculate agreed goodness-of-fit measures and report them together with the model's known limitations.

## Inputs and outputs

- **Input:** the synthetic population, analysis outputs, and reference data from `data/processed/`
- **Output:** validation reports and fit measures

The validation approach is described in [docs/methodology.md](../../docs/methodology.md), and the supporting literature in [docs/sources.md](../../docs/sources.md).
