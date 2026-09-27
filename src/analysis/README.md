# `analysis`: aggregate statistics and result analysis

**Status:** Planned. Not implemented yet.

## Purpose

This module will summarize simulation outputs at the population level and compare scenarios with the baseline.

## Planned responsibilities

- Compute aggregate statistics from simulation outputs (for example, rates, means, distributions, and breakdowns by group).
- Compare each scenario with the baseline and report the differences.
- Summarize variation across repeated runs with different random seeds.
- Produce tables and charts for reports.

## Inputs and outputs

- **Input:** aggregate results from the `simulation` module
- **Output:** summary tables, comparisons, and figures for documentation and for the `validation` module
