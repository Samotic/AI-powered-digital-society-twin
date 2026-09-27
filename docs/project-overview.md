# Project overview

- **Project:** SocietyTwin — AI-Powered Digital Society Twin
- **Course:** Engineering Design II
- **Status:** Research, requirements analysis, and initial repository setup

> **SocietyTwin is intended for population-level research and simulation, not individual-level prediction.**

## Problem

Real societies are complex systems. The characteristics, circumstances, and interactions of individuals and households combine to produce population-level patterns, such as the distribution of income or changes in employment, that cannot be understood by looking at any single person. These patterns are difficult to study directly: real-world experiments on a population are usually impractical or unethical, and aggregate statistics alone do not show how individual-level mechanisms produce them.

## Proposed approach

SocietyTwin will create a synthetic digital representation of a population using aggregate statistical information and agent-based simulation.

1. Aggregate statistics provided by the instructor will be processed and used to generate a **synthetic population**: artificial individuals and households whose combined characteristics match the real statistics, but who do not correspond to any real person.
2. The synthetic population will become an **agent / society model**, in which each agent or household has documented attributes and behavioral rules.
3. A **Scenario Manager** will define a **baseline** and a set of controlled **scenarios**, each changing one condition at a time.
4. A **Simulation Engine** will run the baseline and each scenario over time.
5. The outputs will go through **evaluation and historical validation** against reference data before being reported as **population-level results**.

This follows the [preliminary architecture](architecture.md), which is not final.

## Main stages

| # | Stage | Description | Architecture stage |
|---|---|---|---|
| 1 | Analyze the instructor-provided dataset | Review the variables, level of aggregation, coverage, and limitations of the data. | Instructor / Aggregate Data, Data Processing |
| 2 | Generate the synthetic population | Create synthetic individuals and households that reproduce the source statistics. | Synthetic Population Generator |
| 3 | Validate the synthetic population | Measure how closely the synthetic population matches the source statistics. | Evaluation / Historical Validation |
| 4 | Define agent behavior | Specify transparent rules for how agents and households change over time. | Agent / Society Model |
| 5 | Create the baseline society | Simulate the population with no scenario intervention. | Scenario Manager, Simulation Engine |
| 6 | Define controlled scenarios | Specify the conditions that each scenario changes relative to the baseline. | Scenario Manager |
| 7 | Run simulations | Execute the baseline and scenarios reproducibly, using recorded random seeds. | Simulation Engine |
| 8 | Collect aggregate outputs | Record population-level indicators at each timestep. | Simulation Engine |
| 9 | Compare results | Compare each scenario with the baseline, and simulated outputs with reference data. | Evaluation / Historical Validation |
| 10 | Validate and document findings | Assess model validity and report results together with their limitations. | Evaluation / Historical Validation, Population-Level Results |

## In Scope

A "digital society twin" can easily grow into an unrealistically large project, so the scope is deliberately limited. The following are **planned capabilities**. None of them has been implemented yet.

- **Processing instructor-provided aggregate/statistical data:** cleaning and harmonizing the dataset supplied by the instructor.
- **Synthetic population generation:** creating artificial individuals and households that reproduce the aggregate statistics.
- **Population-level agent representation:** representing the synthetic population as agents and households whose attributes come from the available data.
- **Agent-based social/economic simulation:** simulating how the agent population changes over time under documented behavioral rules.
- **Controlled scenario definition:** defining a baseline and controlled scenarios through the Scenario Manager.
- **Scenario execution:** running the baseline and each scenario reproducibly in the Simulation Engine.
- **Aggregate result analysis:** computing population-level indicators and comparing scenarios with the baseline.
- **Statistical similarity analysis:** measuring how closely the synthetic population and simulated outputs match the reference statistics.
- **Historical/empirical validation where suitable data exists:** comparing simulated outputs with historical or observed aggregate data, only where such data is available and permitted.
- **Model comparison:** comparing the agent-based model with simpler alternatives to check whether its complexity is justified.
- **Reproducible experiments:** recording configurations, random seeds, code versions, and dataset versions so that every experiment can be repeated.
- **Population-level visualization/results:** presenting aggregate results in tables and charts, together with their assumptions and limitations.

## Out of Scope

SocietyTwin will **not** include, attempt, or support:

- Predicting the behavior of specific real individuals
- Individual surveillance
- Identifying real people
- Reconstructing identifiable individuals from aggregate or synthetic data
- Real-time surveillance systems
- Claiming perfect prediction of society
- Automatically making government or political decisions
- Treating simulation results as guaranteed real-world outcomes
- Building an unlimited or full digital replica of society
- Using private or personally identifiable data without authorization

**SocietyTwin is intended for population-level research and simulation, not individual-level prediction.**

## Population-level focus

SocietyTwin studies aggregate, population-level behavior.

- Synthetic agents are statistical constructs. They are generated to reproduce aggregate distributions and do not represent real people.
- Results will be reported as population-level quantities, such as rates, averages, and distributions.
- The model will not be used, and is not designed, to make predictions or decisions about identifiable individuals.

## Dependency on the instructor dataset

The instructor will provide the dataset at a later stage. **The actual population schema will depend on the variables available in that dataset.** Research categories such as age, occupation, location, socioeconomic characteristics, relationships, preferences, and behavior guide the team's research, but none of them is assumed to exist in the data.

The choice of population generation method, the agent schema, and the scenarios that can be studied all depend on the dataset. Until it arrives, the project is limited to research, requirements analysis, and design.

## Items still to be defined

The following items are still being researched or defined. They are listed here so that they are not assumed.

| Item | Responsible |
|---|---|
| Target users | Bejan (Project Manager / System Architect) |
| Final system boundaries and main capabilities | Bejan, integrating all research streams |
| Population schema, agent schema, and simulation concept | Koray (Data + Population + Simulation Research) |
| Technology choices and their justification | Pakhlavon (Technical Architecture / Technologies) |
| Existing work, gap, and SocietyTwin's contribution | Azra (Existing Systems / Similar Projects) |
| Academic foundations and final source selection | Sam (Literature Research) |

See [team-responsibilities.md](team-responsibilities.md) and [research-integration.md](research-integration.md).

## Key terms

| Term | Meaning in this project |
|---|---|
| Instructor / aggregate data | The aggregate statistical dataset to be provided by the instructor. |
| Synthetic population | A generated set of artificial individuals and households whose aggregate characteristics match real statistics. |
| Agent / society model | The synthetic population represented as agents and households with attributes, states, and behavioral rules. |
| Baseline (baseline society) | The society model simulated with no scenario intervention; the reference for all comparisons. |
| Scenario | A controlled change to one or more conditions, simulated with the same population and random seed as the baseline. |
| Scenario Manager | The planned module that defines and checks the baseline and scenarios. It does not run them. |
| Simulation Engine | The planned module that runs the baseline and scenarios over time. |
| Evaluation / historical validation | Assessing how well the synthetic population and simulation outputs agree with reference or historical data. |
| Population-level results | Aggregate indicators, such as rates, averages, and distributions, reported with their evaluation status. |
