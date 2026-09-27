# `analysis`: aggregate statistics and population-level results

**Status:** Planned. Not implemented yet.

## Purpose

This module will summarize simulation outputs at the population level and compare scenarios with the baseline. It supplies statistics to Evaluation / Historical Validation and produces the **Population-Level Results** stage of the [preliminary architecture](../../docs/architecture.md). Results will be reported together with their evaluation status.

## Planned responsibilities

- Compute aggregate statistics from simulation outputs (for example, rates, means, distributions, and breakdowns by group).
- Compare each scenario with the baseline and report the differences.
- Summarize variation across repeated runs with different random seeds.
- Produce tables and charts for reports.

## Inputs and outputs

- **Input:** aggregate results from the `simulation` module
- **Output:** summary tables, comparisons, and figures for documentation and for the `validation` module
