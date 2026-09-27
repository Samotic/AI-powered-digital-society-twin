# `simulation`: Simulation Engine

**Status:** Planned. Not implemented yet.

## Purpose

This module will implement the **Simulation Engine** stage of the [preliminary architecture](../../docs/architecture.md). It will advance the society model through time and execute the baseline and scenarios defined by the Scenario Manager (`src/scenarios/`).

## Planned responsibilities

- Run the **baseline society**: the population evolving under the agent rules with no scenario intervention.
- Run **scenarios**: the same population and random seed, with one or more conditions changed according to a scenario definition from the Scenario Manager.
- Keep random draws aligned between the baseline and each scenario, so that differences in outcomes can be attributed to the scenario change.
- Collect aggregate outputs (for example, rates, averages, and distributions) at each timestep.

## Inputs and outputs

- **Input:** the society model from the `agents` module and validated scenario definitions from the `scenarios` module
- **Output:** aggregate time series for the baseline and each scenario, passed to Evaluation / Historical Validation (`validation` and `analysis` modules)

The time step, simulation length, and scenario parameters will be defined during the design phase.
