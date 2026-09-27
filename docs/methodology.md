# Methodology

**Status:** Planned. This document describes how the project intends to work. None of these stages has been carried out yet, and details will be refined once the instructor's dataset is available and the research streams have reported back.

Terms such as *synthetic population*, *baseline*, and *scenario* are defined in [project-overview.md](project-overview.md#key-terms). The research sources referred to below are listed in [sources.md](sources.md).

## Relation to the preliminary architecture

The methodology follows the stages of the [preliminary architecture](architecture.md), which is not final:

| Methodology step | Architecture stage |
|---|---|
| 1. Data understanding, 2. Data preprocessing | Instructor / Aggregate Data, Data Processing |
| 3. Synthetic population generation | Synthetic Population Generator |
| 5. Agent modeling | Agent / Society Model |
| 6. Baseline simulation, 7. Scenario definition | Scenario Manager |
| 8. Simulation execution | Simulation Engine |
| 4. Population validation, 10. Evaluation and historical validation, 11. Model comparison | Evaluation / Historical Validation |
| 9. Aggregate analysis | Population-Level Results |

## 1. Data understanding

The project will begin by reviewing the instructor-provided dataset. We plan to document:

- which variables are available and how they are categorized;
- the level of aggregation (for example, marginal totals only, cross-tabulations, or anonymized sample records);
- the geographic and time coverage;
- missing values, inconsistencies, and known limitations.

The findings will determine which variables the model can include and which population generation methods are feasible. They will be recorded in the dataset section of [data/README.md](../data/README.md).

**The actual population schema will depend on the variables available in the dataset.** The team's research categories (age, occupation, location, socioeconomic characteristics, relationships, preferences, and behavior) will be matched against the dataset, and only variables that are actually present, or can be justifiably derived, will be used.

## 2. Data preprocessing

The project will clean and transform the raw data into a consistent format. We plan to:

- keep the original files in `data/raw/` unchanged;
- harmonize category labels, units, and totals;
- handle missing or inconsistent values using documented rules;
- write all transformations as code in `src/data_processing/`, so that `data/processed/` can be regenerated from the raw data.

## 3. Synthetic population generation

The project will generate a synthetic population of individuals and, where the data supports it, households. The method will depend on the structure of the dataset:

- If only aggregate tables are available, candidate approaches include sampling from the reported distributions and fitting methods such as iterative proportional fitting (IPF), which adjust a table to match known marginal totals.
- If an anonymized sample of records is available, candidate approaches include reweighting or combinatorial optimization, which select and weight records so that the population matches the aggregate totals.

Chapuis, Taillandier and Drogoul (2022) review these families of methods and how they are used in practice, and will guide the choice. Generation will use a recorded random seed, so that the same inputs always produce the same population.

## 4. Population validation

Before the synthetic population is used for simulation, the project will check that it reproduces the source statistics. We plan to:

- compare the synthetic population's marginal and joint distributions with the source tables;
- use standard goodness-of-fit measures, for example total absolute error or a chi-squared comparison, with the final choice made once the data is known;
- agree acceptable tolerances in advance and report the results.

## 5. Agent modeling

The project will turn the synthetic population into an agent / society model: agents and households with attributes taken from the dataset, together with behavioral rules for how their state changes over time. The agent schema will be developed from the team's research on agent attributes, states, behavior, interactions, social networks, and the environment, and will include only what the data and the research can support. We plan to:

- keep rules simple, transparent, and documented;
- make every rule parameter explicit so that it can be tested and varied;
- base rules on published evidence or clearly stated assumptions, and record which is which.

The core model is planned to be rule-based. Research on LLM-driven agents, such as Park et al. (2023), is used as conceptual inspiration for how agents might represent memory and planning. It is not a requirement for SocietyTwin agents.

## 6. Baseline simulation

The model will simulate the synthetic population under the agent rules with no scenario intervention. This baseline society will be the reference point for every scenario comparison. We plan to run the baseline with several random seeds to measure how much outcomes vary by chance alone.

## 7. Scenario definition

The project will define controlled scenarios, each changing one or a small number of conditions relative to the baseline. Scenarios will be defined and checked by the planned Scenario Manager (`src/scenarios/`), which will not run them itself. Each scenario will be described in a configuration file in `experiments/`, recording:

- the population settings and random seed;
- the conditions that differ from the baseline;
- the simulation length and time step.

Which scenarios are studied will depend on the variables available in the dataset.

## 8. Simulation execution

The project will run the baseline and each scenario reproducibly. We plan to:

- use the same synthetic population and the same random draws for the baseline and each scenario, so that differences can be attributed to the scenario change rather than to chance;
- repeat each experiment across multiple seeds;
- record the configuration, seeds, code version, and dataset version for every run.

## 9. Aggregate analysis

The project will analyze simulation outputs at the population level only. We plan to:

- compute aggregate indicators, such as rates, averages, and distributions, overall and by group;
- report each scenario's difference from the baseline, together with its variation across seeds;
- present the results in tables and charts with their assumptions stated.

These population-level results will be reported only together with their evaluation (step 10), so that simulated outputs are not mistaken for real-world outcomes.

## 10. Evaluation and historical validation

The project will evaluate the model at the aggregate level before reporting any results. The planned evaluation areas are:

- **Statistical similarity:** how closely the synthetic population and simulated aggregates match the reference statistics.
- **Aggregate-level evaluation:** whether population-level indicators behave plausibly over time.
- **Historical and empirical validation:** where reference or historical aggregate data is available and permitted, comparing simulated outputs with observed values.
- **Scenario consistency:** for example, checking that a scenario with no change reproduces the baseline, and that scenario effects are consistent across random seeds.

The approach will draw on the literature on empirical validation of agent-based models:

- Windrum, Fagiolo and Moneta (2007) discuss validation challenges and compare approaches such as indirect calibration, the Werker–Brenner approach, and the history-friendly approach.
- Collins, Koehler and Lynch (2024) give an overview of validation methods, including empirical validation, docking, sampling, visualization, and bootstrapping, and discuss when each is appropriate.

We plan to treat validation as an activity throughout development, not a single final step, and to report clearly where the model does and does not agree with the data.

## 11. Model comparison

The project will compare the agent-based model with simpler alternatives, to check whether its added complexity is justified. Planned comparisons include:

- a simple aggregate or statistical baseline model that works on totals without individual agents;
- sensitivity analysis, varying uncertain parameters to see which ones drive the results;
- where feasible, docking: checking that an independent, simplified implementation produces consistent results.

## Ethics and limitations

- The project studies population-level patterns and will not be used to predict the behavior of specific individuals.
- Synthetic agents do not represent real people.
- Instructor-provided data will be handled according to the terms under which it is supplied, and will not be committed to GitHub.
- All results will be reported as simulated outputs based on stated assumptions, together with the model's known limitations.
