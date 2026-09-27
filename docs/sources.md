# Research sources

**Owner:** Sam (Literature Research)

This document records the academic and technical sources behind SocietyTwin. The Project Management document asks for at least 5 strong sources for the presentation, with approximately 8–10 collected first so that the team can select the strongest.

**Current state:** 5 verified core sources. Further sources are listed as research targets in [Additional Literature To Investigate](#additional-literature-to-investigate) and have not been added to the bibliography yet.

## How this document is maintained

- Bibliographic details (title, authors, year, publication, DOI, URL) were checked against the publishers' pages and Crossref.
- Fields marked **"per the abstract"** are paraphrased from the published abstract only. They should be confirmed against the full text before being cited in the presentation or the TÜBİTAK proposal.
- Fields that cannot be filled from verified material are marked **"TODO: Requires source review."** They must not be filled in until someone has read the relevant part of the paper.
- No quotations, statistics, or findings are included beyond what is stated in the abstracts.

## Core verified sources

### 1. Generation of Synthetic Populations in Social Simulations: A Review of Methods and Practices

- **Authors:** Kevin Chapuis, Patrick Taillandier, Alexis Drogoul
- **Publication:** *Journal of Artificial Societies and Social Simulation* (JASSS), 25(2), article 6
- **URL:** <https://www.jasss.org/25/2/6.html>
- **DOI:** [10.18564/jasss.4762](https://doi.org/10.18564/jasss.4762)

**Year:** 2022

**Problem:** Per the abstract: agent-based models increasingly incorporate data to represent social systems realistically. Data on the attributes of social agents, which together make up synthetic populations, is particularly important but is usually difficult to collect and use in simulations.

**Method:** Per the abstract: a review of the state of the art in methodologies and theories for building realistic synthetic populations for agent-based models, together with a quantitative and narrative review of practices in work published in JASSS.

**Data:** Per the abstract: work published in JASSS between 2011 and 2021. TODO: Requires source review (number of articles or models reviewed, and selection criteria).

**Model / Architecture:** Review article. Section 2, "Methods to Generate Synthetic Populations", surveys generation methods. TODO: Requires source review (summarize the families of methods covered).

**Results:** Per the abstract: the paper highlights discrepancies between theory and practice in synthetic population generation, outlines the challenges in bridging that gap, and presents ideas to help modelers adopt better practices. TODO: Requires source review (specific findings).

**Limitations:** TODO: Requires source review.

**Relevance to SocietyTwin:** This is the main reference for generating a synthetic population from demographic and aggregate information, for choosing a generation method that suits the instructor's dataset, and for validating the resulting population.

### 2. Generative Agents: Interactive Simulacra of Human Behavior

- **Authors:** Joon Sung Park, Joseph O'Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein
- **Publication:** *Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology* (UIST 2023)
- **DOI:** [10.1145/3586183.3606763](https://doi.org/10.1145/3586183.3606763)

**Year:** 2023

**Problem:** Per the abstract: believable proxies of human behavior could support interactive applications, such as immersive environments, rehearsal spaces for interpersonal communication, and prototyping tools.

**Method:** Per the abstract: the authors introduce "generative agents", software agents that simulate believable human behavior, place them in an interactive sandbox environment inspired by *The Sims*, and evaluate them, including an ablation study of the architecture's components.

**Data:** Per the abstract: a sandbox town populated by twenty-five agents, with which end users interact in natural language. The abstract does not describe an external dataset. TODO: Requires source review (evaluation design and participants).

**Model / Architecture:** Per the abstract: an architecture that extends a large language model to store a complete record of each agent's experiences in natural language, synthesize those memories over time into higher-level reflections, and retrieve them dynamically to plan behavior. The components named are observation, planning, and reflection.

**Results:** Per the abstract: the agents produced believable individual and emergent social behaviors. For example, starting from a single user-specified idea that one agent wants to throw a Valentine's Day party, the agents spread invitations, made new acquaintances, and coordinated to attend. The ablation indicated that observation, planning, and reflection each contribute critically to the believability of agent behavior.

**Limitations:** TODO: Requires source review.

**Relevance to SocietyTwin:** This work provides conceptual inspiration for computational agents with memory, planning, reflection, and interaction. SocietyTwin's core model is planned to be rule-based, and this source does **not** imply that every SocietyTwin agent must use a large language model.

*Note:* the abstract used here is from the arXiv preprint (arXiv:2304.03442). It should be checked against the UIST 2023 version.

### 3. Agent-Based Computational Economics: Growing Economies From the Bottom Up

- **Author:** Leigh Tesfatsion
- **Publication:** *Artificial Life*, 8(1), 55–82 (MIT Press)
- **DOI:** [10.1162/106454602753694765](https://doi.org/10.1162/106454602753694765)

**Year:** 2002

**Problem:** TODO: Requires source review. Per the abstract, the article introduces agent-based computational economics (ACE): the computational study of economies modeled as evolving systems of autonomous interacting agents.

**Method:** Per the abstract: a methodological overview and survey. It outlines the main objectives and defining characteristics of the ACE methodology, discusses similarities and differences between ACE and artificial life research, and highlights publications in each of the ACE research areas it identifies.

**Data:** TODO: Requires source review.

**Model / Architecture:** Per the abstract: ACE is presented as a methodology, a specialization to economics of the complex adaptive systems paradigm, rather than as a single model. TODO: Requires source review.

**Results:** Per the abstract: the article identifies eight ACE research areas, considers open questions and directions for future research, and discusses the potential benefits of ACE modeling.

**Limitations:** Per the abstract: the article discusses some potential difficulties associated with ACE modeling. TODO: Requires source review (what these difficulties are, and the limitations of the article itself).

**Relevance to SocietyTwin:** This source provides the theoretical foundation for bottom-up simulation, in which population-level economic and social patterns emerge from interactions between autonomous agents rather than being specified directly.

### 4. Empirical Validation of Agent-Based Models: Alternatives and Prospects

- **Authors:** Paul Windrum, Giorgio Fagiolo, Alessio Moneta
- **Publication:** *Journal of Artificial Societies and Social Simulation* (JASSS), 10(2), article 8
- **URL:** <https://www.jasss.org/10/2/8.html>

**Year:** 2007

**Problem:** Per the abstract: methodological problems in the empirical validation of agent-based models in economics.

**Method:** Per the abstract: a methodological discussion that identifies validation issues common to agent-based modelers, presents a taxonomy of the key dimensions along which agent-based models differ, and compares alternative approaches to empirical validation.

**Data:** TODO: Requires source review.

**Model / Architecture:** TODO: Requires source review. Per the abstract, the paper compares validation approaches rather than presenting a new model.

**Results:** Per the abstract: the paper compares three approaches (indirect calibration, the Werker–Brenner approach, and the history-friendly approach) and identifies unresolved issues for future research. TODO: Requires source review (conclusions about each approach).

**Limitations:** TODO: Requires source review.

**Relevance to SocietyTwin:** This source explains how agent-based models can be calibrated and validated against empirical data, and will inform how SocietyTwin compares its simulated outputs with reference and historical statistics.

### 5. Methods That Support the Validation of Agent-Based Models: An Overview and Discussion

- **Authors:** Andrew Collins, Matthew Koehler, Christopher Lynch
- **Publication:** *Journal of Artificial Societies and Social Simulation* (JASSS), 27(1), article 11
- **URL:** <https://www.jasss.org/27/1/11.html>
- **DOI:** [10.18564/jasss.5258](https://doi.org/10.18564/jasss.5258)

**Year:** 2024

**Problem:** Per the abstract: validation is critical for a simulation model's credibility, but it is difficult, and there is no universally accepted approach. This is especially challenging for agent-based modeling and simulation because of the complexity of the models and of the systems they represent.

**Method:** Per the abstract: a review of nine methods that support validation. Foundational topics include docking, empirical validation, sampling, and visualization, and advanced topics include bootstrapping, causal analysis, inverse generative social science, and role-playing. The paper's section headings also include data analytics.

**Data:** TODO: Requires source review.

**Model / Architecture:** Review article. TODO: Requires source review.

**Results:** Per the abstract: each method is reviewed with respect to its benefits and limitations for agent-based validation, and the paper offers suggestions to support a validation plan. It is intended as an introductory guide for developers of all experience levels.

**Limitations:** TODO: Requires source review.

**Relevance to SocietyTwin:** This source provides a modern framework for validating the model systematically throughout development, and will guide the choice of validation methods at each stage.

## How the sources map to the architecture

| Architecture stage | Sources |
|---|---|
| Synthetic Population Generator | Chapuis et al. (2022) |
| Agent / Society Model | Tesfatsion (2002); Park et al. (2023) as inspiration only |
| Scenario Manager and Simulation Engine | Tesfatsion (2002) |
| Evaluation / Historical Validation | Chapuis et al. (2022) for population validation; Windrum et al. (2007); Collins et al. (2024) |

## Additional Literature To Investigate

> These are **research targets, not citations.** No source below has been selected, reviewed, or verified yet. A source may be added to the core list only after it has passed the verification checklist below.

The aim is to reach approximately 8–10 verified sources in total, covering all of the research areas assigned to Literature Research: digital twins, social / digital society twins, agent-based modeling, synthetic populations, generative agents, social simulation, LLM-based agents, socio-technical systems, and population-level simulation.

| # | Research target | What to look for | Current coverage |
|---|---|---|---|
| A | Digital twins and social / digital society twins | Definitions of a digital twin, and work that applies the idea to societies, cities, or populations rather than physical assets | Not covered yet |
| B | Socio-technical digital twins | Twins that model interactions between people and technical systems, and how they handle human behavior | Not covered yet |
| C | LLM-based agents and LLM-based social simulation | Work that uses large language models to drive agents in social simulations, including reported costs, scale limits, and evaluation methods | Partly covered by Park et al. (2023) |
| D | Large-scale, population-level agent-based social simulation | Agent-based models of whole populations built from statistical data, and how they report and evaluate aggregate outcomes | Partly covered by Tesfatsion (2002) |
| E | Synthetic population validation | Methods and metrics for checking synthetic populations against source statistics | Partly covered by Chapuis et al. (2022) |

### Verification checklist for new sources

Before a source is added to the core list:

- [ ] The paper has been located and opened at its publisher's page or an official repository.
- [ ] Title, authors, year, publication, and DOI or URL have been copied from the publisher's page, not from memory or an AI tool.
- [ ] Each required field (Problem, Method, Data, Model / Architecture, Results, Limitations, Relevance) is filled in from the paper, or marked "TODO: Requires source review."
- [ ] Relevance to SocietyTwin has been stated in one or two sentences.

### Template for a new source

```markdown
### Paper Title

- **Authors:**
- **Publication:**
- **URL / DOI:**

**Year:**

**Problem:**

**Method:**

**Data:**

**Model / Architecture:**

**Results:**

**Limitations:**

**Relevance to SocietyTwin:**
```
