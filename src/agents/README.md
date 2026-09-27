# `agents`: Agent / Society Model

**Status:** Planned. Not implemented yet.

## Purpose

This module will implement the **Agent / Society Model** stage of the [preliminary architecture](../../docs/architecture.md). It will define the simulated agents (individuals and, where relevant, households) and the behavioral rules that determine how their state changes during a simulation.

## Planned responsibilities

- Define the attributes each agent or household carries, based on the variables available in the dataset. The agent schema will come from the team's research on agent attributes, states, behavior, interactions, social networks, and the environment, and will include only what the data supports.
- Define transparent, documented behavioral rules (for example, how employment status or household composition may change over a timestep).
- Keep every rule parameter explicit and documented, so that it can be reviewed, tested, and varied in experiments.

## Design notes

- Agents are building blocks for studying **population-level** outcomes. They do not represent, and are not intended to predict, specific real people.
- The core model is planned to be rule-based. Behavioral rules will be simple enough to explain and validate.

## Inputs and outputs

- **Input:** a synthetic population from the `population` module
- **Output:** the society model, whose documented parameters the Scenario Manager (`src/scenarios/`) can vary and which the Simulation Engine (`src/simulation/`) runs
