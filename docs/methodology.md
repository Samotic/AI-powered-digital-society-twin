# Methodology

**Status:** Planned. This document describes how the project intends to work. None of these stages has been carried out yet, and details will be refined once the instructor's dataset is available.

Terms such as *synthetic population*, *baseline society*, and *scenario* are defined in [project-overview.md](project-overview.md#key-terms). The research sources referred to below are listed in [sources.md](sources.md).

## 1. Data understanding

The project will begin by reviewing the instructor-provided dataset. We plan to document:

- which variables are available and how they are categorized;
- the level of aggregation (for example, marginal totals only, cross-tabulations, or anonymized sample records);
- the geographic and time coverage;
- missing values, inconsistencies, and known limitations.

The findings will determine which variables the model can include and which population generation methods are feasible. They will be recorded in the dataset section of [data/README.md](../data/README.md).

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

The project will define agents and households with attributes taken from the dataset, together with behavioral rules for how their state changes over time. We plan to:

- keep rules simple, transparent, and documented;
- make every rule parameter explicit so that it can be tested and varied;
- base rules on published evidence or clearly stated assumptions, and record which is which.

The core model is planned to be rule-based. Research on LLM-driven agents, such as Park et al. (2023), is used as conceptual inspiration for how agents might represent memory and planning. It is not a requirement for SocietyTwin agents.

## 6. Baseline simulation

The model will simulate the synthetic population under the agent rules with no scenario intervention. This baseline society will be the reference point for every scenario comparison. We plan to run the baseline with several random seeds to measure how much outcomes vary by chance alone.

## 7. Scenario definition

The project will define controlled scenarios, each changing one or a small number of conditions relative to the baseline. Each scenario will be described in a configuration file in `experiments/`, recording:

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

## 10. Historical and empirical validation

Where reference or historical aggregate data is available, the project will compare simulated outputs with observed values. The approach will draw on the literature on empirical validation of agent-based models:

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
