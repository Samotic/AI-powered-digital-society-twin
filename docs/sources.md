# Research sources

These sources inform the design of SocietyTwin. Bibliographic details were checked against the publishers' pages and Crossref. The summaries are brief paraphrases of each work's stated aims; team members should read the full texts before citing specific findings.

## 1. Synthetic population generation

- **Title:** Generation of Synthetic Populations in Social Simulations: A Review of Methods and Practices
- **Authors:** Kevin Chapuis, Patrick Taillandier, Alexis Drogoul
- **Year:** 2022
- **Publication:** *Journal of Artificial Societies and Social Simulation* (JASSS), 25(2), article 6
- **URL:** <https://www.jasss.org/25/2/6.html>
- **DOI:** [10.18564/jasss.4762](https://doi.org/10.18564/jasss.4762)

**Summary:** A review of methods for generating synthetic populations for agent-based social simulation. It compares the methods described in the literature with how populations are actually built in published simulation models, based on a review of models published in JASSS.

**Relevance to SocietyTwin:** This is the main reference for generating a synthetic population from demographic and aggregate information, for choosing a generation method that suits the instructor's dataset, and for validating the resulting population.

## 2. Generative agents

- **Title:** Generative Agents: Interactive Simulacra of Human Behavior
- **Authors:** Joon Sung Park, Joseph O'Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein
- **Year:** 2023
- **Publication:** *Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology* (UIST 2023)
- **DOI:** [10.1145/3586183.3606763](https://doi.org/10.1145/3586183.3606763)

**Summary:** Presents an architecture for "generative agents": software agents that use a large language model to store a record of their experiences, reflect on them, and plan their behavior. The agents are demonstrated interacting in a small simulated town.

**Relevance to SocietyTwin:** This work provides conceptual inspiration for computational agents with memory, planning, reflection, and interaction. SocietyTwin's core model is planned to be rule-based, and this source does **not** imply that every SocietyTwin agent must use a large language model.

## 3. Agent-based computational economics

- **Title:** Agent-Based Computational Economics: Growing Economies From the Bottom Up
- **Author:** Leigh Tesfatsion
- **Year:** 2002
- **Publication:** *Artificial Life*, 8(1), 55–82 (MIT Press)
- **DOI:** [10.1162/106454602753694765](https://doi.org/10.1162/106454602753694765)

**Summary:** An introduction to agent-based computational economics (ACE): the study of economies as evolving systems of autonomous, interacting agents. It outlines the approach and surveys areas of research that use it.

**Relevance to SocietyTwin:** This source provides the theoretical foundation for bottom-up simulation, in which population-level economic and social patterns emerge from interactions between autonomous agents rather than being specified directly.

## 4. Empirical validation of agent-based models

- **Title:** Empirical Validation of Agent-Based Models: Alternatives and Prospects
- **Authors:** Paul Windrum, Giorgio Fagiolo, Alessio Moneta
- **Year:** 2007
- **Publication:** *Journal of Artificial Societies and Social Simulation* (JASSS), 10(2), article 8
- **URL:** <https://www.jasss.org/10/2/8.html>

**Summary:** Discusses the methodological problems of empirically validating agent-based models, particularly in economics. It compares three approaches (indirect calibration, the Werker–Brenner approach, and the history-friendly approach) and identifies open research questions.

**Relevance to SocietyTwin:** This source explains how agent-based models can be calibrated and validated against empirical data, and will inform how SocietyTwin compares its simulated outputs with reference and historical statistics.

## 5. Methods for validating agent-based models

- **Title:** Methods That Support the Validation of Agent-Based Models: An Overview and Discussion
- **Authors:** Andrew Collins, Matthew Koehler, Christopher Lynch
- **Year:** 2024
- **Publication:** *Journal of Artificial Societies and Social Simulation* (JASSS), 27(1), article 11
- **URL:** <https://www.jasss.org/27/1/11.html>
- **DOI:** [10.18564/jasss.5258](https://doi.org/10.18564/jasss.5258)

**Summary:** An overview of methods that support the validation of agent-based models, including data analytics, docking, empirical validation, sampling, visualization, bootstrapping, causal analysis, inverse generative social science, and role-playing. It discusses the benefits and limitations of each.

**Relevance to SocietyTwin:** This source provides a modern framework for validating the model systematically throughout development, and will guide the choice of validation methods at each stage.

## How the sources map to the project stages

| Project stage | Sources |
|---|---|
| Synthetic population generation and validation | Chapuis et al. (2022) |
| Agent modeling | Tesfatsion (2002); Park et al. (2023) as inspiration only |
| Baseline and scenario simulation | Tesfatsion (2002) |
| Historical and empirical validation | Windrum et al. (2007); Collins et al. (2024) |
| Model comparison | Collins et al. (2024) |
