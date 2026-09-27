# `simulation`: simulation engine and scenario execution

**Status:** Planned. Not implemented yet.

## Purpose

This module will advance the agent population through time and run controlled scenarios against a baseline.

## Planned responsibilities

- Run the **baseline society**: the population evolving under the agent rules with no scenario intervention.
- Run **scenarios**: the same population and random seed, with one or more conditions changed according to a scenario configuration.
- Keep random draws aligned between the baseline and each scenario, so that differences in outcomes can be attributed to the scenario change.
- Collect aggregate outputs (for example, rates, averages, and distributions) at each timestep.

## Inputs and outputs

- **Input:** agents from the `agents` module and a scenario configuration from `experiments/`
- **Output:** aggregate time series for the baseline and each scenario, passed to the `analysis` module

The time step, simulation length, and scenario parameters will be defined during the design phase.
