# `scenarios`: Scenario Manager

**Status:** Planned. Not implemented yet.

## Purpose

The Scenario Manager will define and configure the controlled scenarios that SocietyTwin simulates. It sits between the Agent / Society Model and the Simulation Engine in the [preliminary architecture](../../docs/architecture.md).

It will **not** run simulations. Executing scenarios is the job of the Simulation Engine (`src/simulation/`).

## Planned responsibilities

- Define the **baseline scenario**: the population under the agent rules with no intervention.
- Define **controlled scenarios**, each changing one or a small number of conditions relative to the baseline.
- Read scenario configuration files from `experiments/configs/`.
- Check each configuration before it is used, and reject invalid or out-of-range settings with a clear error.
- Make sure each scenario uses the same synthetic population and random seed as its baseline, so that differences in outcomes can be attributed to the scenario change.
- Record the information needed to reproduce each scenario run: configuration, seeds, code version, and dataset version.

## Inputs and outputs

- **Input:** scenario configuration files from `experiments/configs/`, and the parameters exposed by the Agent / Society Model
- **Output:** validated scenario definitions passed to the Simulation Engine

## Open questions

Which scenarios can be studied depends on the variables in the instructor-provided dataset. The configuration format and the list of adjustable parameters will be defined once the dataset has been reviewed and the population and agent schemas are agreed (see [docs/team-responsibilities.md](../../docs/team-responsibilities.md)).
