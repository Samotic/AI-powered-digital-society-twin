# `population`: synthetic population generation

**Status:** Planned. Not implemented yet.

## Purpose

This module will generate a synthetic population of individuals and households whose aggregate characteristics match the statistics in the processed dataset.

## Planned responsibilities

- Create synthetic individuals and, if the data supports it, group them into households. The population schema (which attributes each synthetic person has) will depend on the variables available in the instructor-provided dataset.
- Assign attributes so that the population's distributions match the source statistics (for example, marginal totals and cross-tabulations).
- Use a recorded random seed, so that the same configuration always produces the same population.
- Report how closely the generated population matches the source statistics, for use by the `validation` module.

## Inputs and outputs

- **Input:** processed aggregate tables from `data/processed/`, plus a population size and random seed
- **Output:** a synthetic population ready to be turned into agents

The generation method will be chosen once the structure of the dataset is known. Candidate approaches are described in [docs/methodology.md](../../docs/methodology.md).
