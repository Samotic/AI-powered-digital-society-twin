# `agents`: agent and household model

**Status:** Planned. Not implemented yet.

## Purpose

This module will define the simulated agents (individuals and, where relevant, households) and the behavioral rules that determine how their state changes during a simulation.

## Planned responsibilities

- Define the attributes each agent or household carries, based on the variables available in the dataset.
- Define transparent, documented behavioral rules (for example, how employment status or household composition may change over a timestep).
- Keep every rule parameter explicit and documented, so that it can be reviewed, tested, and varied in experiments.

## Design notes

- Agents are building blocks for studying **population-level** outcomes. They do not represent, and are not intended to predict, specific real people.
- The core model is planned to be rule-based. Behavioral rules will be simple enough to explain and validate.

## Inputs and outputs

- **Input:** a synthetic population from the `population` module
- **Output:** agent objects used by the `simulation` module
