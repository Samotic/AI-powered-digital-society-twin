# Project overview

- **Project:** SocietyTwin — AI-Powered Digital Society Twin
- **Course:** Engineering Design II
- **Status:** Research, requirements analysis, and initial repository setup

## Problem

Real societies are complex systems. The characteristics, circumstances, and interactions of individuals and households combine to produce population-level patterns, such as the distribution of income or changes in employment, that cannot be understood by looking at any single person. These patterns are difficult to study directly: real-world experiments on a population are usually impractical or unethical, and aggregate statistics alone do not show how individual-level mechanisms produce them.

## Proposed approach

SocietyTwin will create a synthetic digital representation of a population using aggregate statistical information and agent-based simulation.

1. Aggregate statistics provided by the instructor will be used to generate a **synthetic population**: artificial individuals and households whose combined characteristics match the real statistics, but who do not correspond to any real person.
2. Each synthetic individual or household will become an **agent** with documented behavioral rules.
3. The agents will be simulated over time to form a **baseline society**.
4. Controlled **scenarios** will change one condition at a time relative to the baseline, and the resulting **aggregate outcomes** will be compared.
5. The synthetic population and the simulation outputs will be **validated** against reference or historical aggregate data.

## Main stages

| # | Stage | Description |
|---|---|---|
| 1 | Analyze the instructor-provided dataset | Review the variables, level of aggregation, coverage, and limitations of the data. |
| 2 | Generate the synthetic population | Create synthetic individuals and households that reproduce the source statistics. |
| 3 | Validate the synthetic population | Measure how closely the synthetic population matches the source statistics. |
| 4 | Define agent behavior | Specify transparent rules for how agents and households change over time. |
| 5 | Create the baseline society | Simulate the population with no scenario intervention. |
| 6 | Define controlled scenarios | Specify the conditions that each scenario changes relative to the baseline. |
| 7 | Run simulations | Execute the baseline and scenarios reproducibly, using recorded random seeds. |
| 8 | Collect aggregate outputs | Record population-level indicators at each timestep. |
| 9 | Compare results | Compare each scenario with the baseline, and simulated outputs with reference data. |
| 10 | Validate and document findings | Assess model validity and report results together with their limitations. |

## Population-level scope

SocietyTwin studies **aggregate, population-level behavior**. It does not attempt to predict what any specific individual will do.

- Synthetic agents are statistical constructs. They are generated to reproduce aggregate distributions and do not represent real people.
- Results will be reported as population-level quantities, such as rates, averages, and distributions.
- The model will not be used, and is not designed, to make predictions or decisions about identifiable individuals.

This system is intended for population-level research and simulation. It is not intended to predict the behavior of specific individuals.

## Dependency on the instructor dataset

The instructor will provide the dataset at a later stage. The variables in the model, the choice of population generation method, and the scenarios that can be studied all depend on what that dataset contains. Until it arrives, the project is limited to research, requirements analysis, and design.

## Key terms

| Term | Meaning in this project |
|---|---|
| Synthetic population | A generated set of artificial individuals and households whose aggregate characteristics match real statistics. |
| Agent | A simulated individual or household with attributes and behavioral rules. |
| Baseline society | The synthetic population simulated with no scenario intervention; the reference for all comparisons. |
| Scenario | A controlled change to one or more conditions, simulated with the same population and random seed as the baseline. |
| Aggregate results | Population-level indicators produced by a simulation, such as rates, averages, and distributions. |
| Validation | Assessing how well the synthetic population and simulation outputs agree with reference or historical data. |
