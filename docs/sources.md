# Research sources

**Owner:** Sam (Literature Research)

This document records the academic, technical, and data sources behind SocietyTwin v2. Sources are grouped as the v2 architecture requires:

1. [Core methodology sources](#core-methodology-sources): methods SocietyTwin applies (population synthesis, validation, persona-conditioned LLM agents).
2. [Reference systems](#reference-systems): existing systems used as inspiration or comparison. SocietyTwin is **not** a clone of any of them.
3. [Data sources](#data-sources): official statistics, legal texts, and licences.
4. [Future-research sources](#future-research-sources): relevant to stretch goals or later work.

## How this document is maintained

- Bibliographic details were checked against publishers' pages, Crossref, arXiv, ACL Anthology, official repositories, or official statistics publications. Sources that could not be verified are not listed as citations.
- Descriptions marked **"per the abstract"** or taken from a repository README reflect only those texts. Read the full text before citing specific findings in the presentation or the TÜBİTAK proposal.
- Fields that cannot be filled from verified material are marked **"TODO: Requires source review."**
- The five sources reviewed in the research phase keep their full review fields (Problem, Method, Data, Model / Architecture, Results, Limitations). Newer sources use a shorter format: citation, contribution, use in SocietyTwin, and limitations.

## Core methodology sources

### A. Synthetic population generation

### Generation of Synthetic Populations in Social Simulations: A Review of Methods and Practices

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

**Relevance to SocietyTwin (v2):** Main review behind the v2 generator design: it frames the choice between synthetic reconstruction from aggregate tables (the MVP approach, because only TÜİK aggregates are assumed) and methods that need microdata (the advanced approach). Also informs population validation.

### On a Least Squares Adjustment of a Sampled Frequency Table When the Expected Marginal Totals are Known

- **Citation:** Deming, W. E., & Stephan, F. F. (1940). *The Annals of Mathematical Statistics*, 11(4), 427–444. doi:[10.1214/aoms/1177731829](https://doi.org/10.1214/aoms/1177731829)
- **Contributes:** The original iterative proportional fitting (IPF) procedure: adjusting a frequency table so that it matches known marginal totals.
- **How SocietyTwin uses it:** Fits the conditional tables of the dependency model to every available official TÜİK marginal ([report §11](societytwin-v2-architecture.md#11-synthetic-population-generation)).
- **Limitations / relevance:** IPF keeps the interaction structure of its starting table and cannot create dependencies that no table contains; zero cells stay zero.

### Creating synthetic baseline populations

- **Citation:** Beckman, R. J., Baggerly, K. A., & McKay, M. D. (1996). *Transportation Research Part A: Policy and Practice*, 30(6), 415–429. doi:[10.1016/0965-8564(96)00004-3](https://doi.org/10.1016/0965-8564(96)00004-3)
- **Contributes:** Classic reference for generating synthetic baseline populations with IPF-based synthetic reconstruction.
- **How SocietyTwin uses it:** Background for the MVP generator (synthetic reconstruction from aggregate tables).
- **Limitations / relevance:** Developed for a different national context. TODO: Requires source review (data requirements of the original method).

### A methodology to match distributions of both household and person attributes in the generation of synthetic populations

- **Citation:** Ye, X., Konduri, K. C., Pendyala, R. M., Sana, B., & Waddell, P. (2009). Paper presented at the 88th Annual Meeting of the Transportation Research Board, Washington, DC.
- **Contributes:** Iterative proportional updating (IPU): matches household-level and person-level marginals at the same time.
- **How SocietyTwin uses it:** Candidate method for linked households (STRETCH) and for calibrating a microdata-based generator.
- **Limitations / relevance:** Conference paper; requires a household sample with person records.

### Simulation based population synthesis

- **Citation:** Farooq, B., Bierlaire, M., Hurtubia, R., & Flötteröd, G. (2013). *Transportation Research Part B: Methodological*, 58, 243–263. doi:[10.1016/j.trb.2013.09.012](https://doi.org/10.1016/j.trb.2013.09.012)
- **Contributes:** A simulation-based (Markov chain Monte Carlo) alternative to fitting-based population synthesis.
- **How SocietyTwin uses it:** Alternative considered for the generator ([report §11](societytwin-v2-architecture.md#11-synthetic-population-generation)); not chosen for the MVP.
- **Limitations / relevance:** Needs conditional distributions estimated from data; more complex to validate in one semester.

### A Bayesian network approach for population synthesis

- **Citation:** Sun, L., & Erath, A. (2015). *Transportation Research Part C: Emerging Technologies*, 61, 49–62. doi:[10.1016/j.trc.2015.10.010](https://doi.org/10.1016/j.trc.2015.10.010)
- **Contributes:** Population synthesis with a Bayesian network, which represents dependencies between attributes as a directed graph.
- **How SocietyTwin uses it:** Conceptual basis for the DAG dependency model; the advanced generator (learned network) if TÜİK microdata becomes available.
- **Limitations / relevance:** Learning the network structure requires microdata, which the MVP does not assume.

### Prediction of rare feature combinations in population synthesis: Application of deep generative modelling

- **Citation:** Garrido, S., Borysov, S. S., Pereira, F. C., & Rich, J. (2020). *Transportation Research Part C: Emerging Technologies*, 120, 102787. doi:[10.1016/j.trc.2020.102787](https://doi.org/10.1016/j.trc.2020.102787)
- **Contributes:** Addresses rare attribute combinations that sample-based synthesis can miss.
- **How SocietyTwin uses it:** Motivates keeping legitimate rare combinations (soft constraints are not masked) and the rare-cell recall metric.
- **Limitations / relevance:** Uses deep generative models, which are FUTURE WORK for SocietyTwin.

### Generating a Two-Layered Synthetic Population for French Municipalities: Results and Evaluation of Four Synthetic Reconstruction Methods

- **Citation:** Yameogo, B. F., Vandanjon, P.-O., Gastineau, P., & Hankach, P. (2021). *JASSS*, 24(2), 5. doi:[10.18564/jasss.4482](https://doi.org/10.18564/jasss.4482)
- **Contributes:** Per the abstract: compares four synthetic reconstruction methods and two integerisation approaches for households and individuals; hierarchical IPF and relative entropy minimisation performed best with truncate-replicate-sample allocation.
- **How SocietyTwin uses it:** Guides the choice of integerisation (controlled rounding) and the STRETCH linked-household design.
- **Limitations / relevance:** French census context; results may not transfer directly to TÜİK tables.

### B. Validation of synthetic data and simulations

### Empirical Validation of Agent-Based Models: Alternatives and Prospects

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

**Relevance to SocietyTwin (v2):** Informs how historical and empirical validation is framed (calibration versus validation data) for the optional population-dynamics engine, and the principle of validating against data not used for calibration, which v2 applies through held-out official tables.

### Methods That Support the Validation of Agent-Based Models: An Overview and Discussion

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

**Relevance to SocietyTwin (v2):** Provides a menu of validation-supporting methods. Empirical validation, sampling (multiple seeds and sizes), and docking (the Cohort-Component benchmark for the optional dynamics engine) appear related to the v2 validation strategy. TODO: Requires source review (confirm how the paper defines each method before relying on this link).

### General and Specific Utility Measures for Synthetic Data

- **Citation:** Snoke, J., Raab, G. M., Nowok, B., Dibben, C., & Slavkovic, A. (2018). *Journal of the Royal Statistical Society Series A*, 181(3), 663–688. doi:[10.1111/rssa.12358](https://doi.org/10.1111/rssa.12358)
- **Contributes:** Framework for measuring how useful synthetic data is, both in general and for specific analyses.
- **How SocietyTwin uses it:** Informs the distinction between marginal fit and analysis-specific checks in the validation strategy; general utility measures apply if record-level reference data (microdata) becomes available.
- **Limitations / relevance:** Several measures require record-level reference data, which the MVP does not use.

### SimBench: Benchmarking the Ability of Large Language Models to Simulate Human Behaviors

- **Citation:** Hu, T., Baumann, J., Lupo, L., Collier, N., Hovy, D., & Röttger, P. (2026). ICLR 2026. arXiv:[2510.17516](https://arxiv.org/abs/2510.17516)
- **Contributes:** Per the abstract: a standardised benchmark of group-level simulation across 20 datasets; the best models reach modest fidelity (40.80/100), and demographic simulation is particularly challenging.
- **How SocietyTwin uses it:** Supports comparing *group-level response distributions* (not individual answers) in experiment validity, and sets realistic expectations.
- **Limitations / relevance:** Datasets are not Türkiye-specific.

### C. Persona-conditioned LLM agents: fidelity, bias, and robustness

### Out of One, Many: Using Language Models to Simulate Human Samples

- **Citation:** Argyle, L. P., Busby, E. C., Fulda, N., Gubler, J., Rytting, C., & Wingate, D. (2023). *Political Analysis*. doi:[10.1017/pan.2023.2](https://doi.org/10.1017/pan.2023.2)
- **Contributes:** Per the abstract: proposes studying language models as proxies for specific human sub-populations, arguing that model biases are not uniform properties of a model.
- **How SocietyTwin uses it:** Motivates conditioning agents on demographic persona cards and comparing responses by subgroup.
- **Limitations / relevance:** Evidence comes from another national context; transfer to Türkiye and to Turkish-language prompts is untested.

### Using Large Language Models to Simulate Multiple Humans and Replicate Human Subject Studies

- **Citation:** Aher, G., Arriaga, R. I., & Kalai, A. T. (2023). ICML 2023. arXiv:[2208.10264](https://arxiv.org/abs/2208.10264)
- **Contributes:** Per the abstract: introduces "Turing Experiments" to test how far a model can simulate aspects of human behaviour, and shows they can reveal consistent distortions.
- **How SocietyTwin uses it:** Informs the design of replication-style checks and the expectation of systematic distortions.
- **Limitations / relevance:** Replicates known studies; does not address national population synthesis.

### LLM Agents Grounded in Self-Reports Enable General-Purpose Simulation of Individuals

- **Citation:** Park, J. S., Zou, C. Q., Kamphorst, J., Egan, N., Shaw, A., Hill, B. M., Cai, C., Morris, M. R., Liang, P., Willer, R., & Bernstein, M. S. (2024, revised 2026). arXiv:[2411.10109](https://arxiv.org/abs/2411.10109). Earlier versions were titled "Generative Agent Simulations of 1,000 People".
- **Contributes:** Per the abstract: agents built from interviews and surveys of 1,052 Americans reached 82–86% of individual test–retest consistency on held-out items, versus 74% for demographic-only baselines.
- **How SocietyTwin uses it:** SocietyTwin personas are **demographic-only by design** (no real-person data), so this paper sets the expectation that their fidelity is limited and must be measured, and it motivates demographic-only baselines.
- **Limitations / relevance:** Relies on real interview data, which SocietyTwin does not use; US sample.

### Whose Opinions Do Language Models Reflect?

- **Citation:** Santurkar, S., Durmus, E., Ladhak, F., Lee, C., Liang, P., & Hashimoto, T. (2023). arXiv:[2303.17548](https://arxiv.org/abs/2303.17548) (published at ICML 2023; proceedings details to verify).
- **Contributes:** Per the abstract: a quantitative framework for measuring which opinions LMs reflect, using public opinion polls and their human responses.
- **How SocietyTwin uses it:** Informs distribution-comparison metrics (for example Jensen–Shannon divergence) and awareness of model opinion bias.
- **Limitations / relevance:** US opinion polls.

### Towards Measuring the Representation of Subjective Global Opinions in Language Models

- **Citation:** Durmus, E., Nguyen, K., Liao, T. I., Schiefer, N., Askell, A., Bakhtin, A., Chen, C., Hatfield-Dodds, Z., Hernandez, D., Joseph, N., Lovitt, L., McCandlish, S., Sikder, O., Tamkin, A., Thamkul, J., Kaplan, J., Clark, J., & Ganguli, D. (2023). arXiv:[2306.16388](https://arxiv.org/abs/2306.16388)
- **Contributes:** Per the abstract: LLMs may not represent diverse global perspectives equitably; proposes a framework to measure whose opinions model responses resemble.
- **How SocietyTwin uses it:** Cross-national framing for checking whether persona agents reflect Turkish rather than other countries' opinion patterns.
- **Limitations / relevance:** TODO: Requires source review (whether Türkiye-specific items are included).

### Marked Personas: Using Natural Language Prompts to Measure Stereotypes in Language Models

- **Citation:** Cheng, M., Durmus, E., & Jurafsky, D. (2023). *Proceedings of the 61st Annual Meeting of the ACL (Volume 1: Long Papers)*, 1504–1532. doi:[10.18653/v1/2023.acl-long.84](https://doi.org/10.18653/v1/2023.acl-long.84)
- **Contributes:** Per the abstract: a prompt-based method to measure stereotypes in LLM-generated personas for intersectional demographic groups.
- **How SocietyTwin uses it:** Basis for the stereotype audit of persona rationales ([validation-strategy.md §3](validation-strategy.md#3-persona-consistency)).
- **Limitations / relevance:** English-language study; Turkish-language behaviour must be checked separately.

### Large language models that replace human participants can harmfully misportray and flatten identity groups

- **Citation:** Wang, A., Morgenstern, J., & Dickerson, J. P. (2025). *Nature Machine Intelligence*, 7, 400–411. doi:[10.1038/s42256-025-00986-z](https://doi.org/10.1038/s42256-025-00986-z)
- **Contributes:** Argues and shows (with 3,200 human participants across 16 identities and 4 LLMs) that LLM stand-ins can misportray and flatten demographic groups.
- **How SocietyTwin uses it:** Central to the ethics and limitations framing: no claims that personas represent real Turkish people; within-group variance must be reported.
- **Limitations / relevance:** Results concern the identities and models studied; Türkiye was not the focus.

### LLM-Based Social Simulations Require a Boundary

- **Citation:** Wu, Z., Peng, R., Ito, T., Onizuka, M., & Xiao, C. (2026). ICML 2026 Position Paper Track. arXiv:[2506.19806](https://arxiv.org/abs/2506.19806)
- **Contributes:** Per the abstract: LLMs tend to produce an "average persona"; recommends reporting behavioural variance alongside mean alignment and limiting conclusions when variance is insufficient.
- **How SocietyTwin uses it:** Adopted as a reporting rule in experiment validity.
- **Limitations / relevance:** Position paper.

### Stop Drawing Scientific Claims from LLM Social Simulations Without Robustness Audits

- **Citation:** Ye, J., Cao, L., Chen, D., & Ferrara, E. (2026). arXiv:[2605.18890](https://arxiv.org/abs/2605.18890)
- **Contributes:** Per the abstract: small changes such as persona formatting can shift simulated outcomes substantially (up to 76 percentage points in one case study); proposes the TRAILS taxonomy for robustness audits.
- **How SocietyTwin uses it:** Basis for robustness audits before any conclusion is drawn from persona experiments.
- **Limitations / relevance:** Preprint; case studies are games and social-media models rather than surveys.

## Reference systems

### MatrAIx: Simulating the World with 8.3 Billion Persona Agents

- **Citation:** Li, X., Hao, Y., Hou, J., et al. (2026). arXiv:[2608.04205](https://arxiv.org/abs/2608.04205). Code: <https://github.com/MatrAIx-ai/MatrAIx-Persona-8B> (MIT licence). Dataset: Persona 1M on Hugging Face (`MatrAIx2026/MatrAIx_Persona_1M`).
- **Contributes:** Per the paper: a population-scale simulated-user evaluation infrastructure for AI systems and digital products. Persona 8B has 8.3 billion records over 1,290 categorical dimensions (Background, Psychology, Capability, Behavior and Interaction, Lifestyle), sampled from a dependency graph with compatibility masks or derived from human-authored sources; a ~1M coreset is released. The Playground has Survey, AI Chatbot, Web, and App environments; each trial stores persona, task, agent, model, and seed; run manifests keep the requested and realised cohort. Validation includes a 400-trial adherence study (91.5%).
- **How SocietyTwin uses it:** Main architectural inspiration: DAG sampling with masks, separation of records from LLM agents, cohort selection, per-trial telemetry, run manifests, adherence tests, cross-model checks ([report §7](societytwin-v2-architecture.md#7-reference-systems)).
- **Limitations / relevance:** Different purpose (product evaluation) and global scope; SocietyTwin does **not** copy its schema size, its human-grounded extraction from web sources, or its Web/App environments. MatrAIx itself states that human studies remain necessary before applying conclusions to real populations.

### Position: Synthetic Persona Needs Explicit Grounding and Standardized Reporting

- **Citation:** MatrAIx Research Community (2026). Accepted at the COLM 2026 Workshop on Social Simulation with LLMs. <https://matraix.ai/research/synthetic-persona-grounding.html>
- **Contributes:** A six-item reporting checklist for persona studies: persona provenance, grounding evidence, selection or sampling logic, internal consistency checks, enactment checks, intended use and inference scope.
- **How SocietyTwin uses it:** Adopted for every SocietyTwin validation report.
- **Limitations / relevance:** Workshop position paper; arXiv version listed as forthcoming.

### Social Simulation Arena

- **Citation:** Social Atoms at MIT, with collaborators. Repository: <https://github.com/Social-Atoms/social-sim-arena>; website: <https://social-simulation-arena.com>
- **Contributes:** A live benchmark: entrants forecast how a population will answer a poll or behave before the real data is published; forecasts are locked 48 hours before publication, hashed and timestamped, and scored with CRPS, energy score, or rank-biased overlap (arena score: persistence = 0, perfect oracle = 100).
- **How SocietyTwin uses it:** Inspiration for pre-registered validity tests against future TÜİK releases (FUTURE WORK) and for proper scoring of distributional predictions.
- **Limitations / relevance:** Papers describing the arena are listed as forthcoming; population coverage not stated in the repository.

### Generative Agents: Interactive Simulacra of Human Behavior

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

**Relevance to SocietyTwin (v2):** Foundational reference for LLM agents conditioned on a persona. SocietyTwin v2 uses **short-lived, single-trial** agents without memory or reflection in the MVP; long-running generative agents are FUTURE WORK.

*Note:* the abstract used here is from the arXiv preprint (arXiv:2304.03442). It should be checked against the UIST 2023 version.

### AgentSociety: Large-Scale Simulation of LLM-Driven Generative Agents Advances Understanding of Human Behaviors and Society

- **Citation:** Piao, J., Yan, Y., Zhang, J., et al. (2025, revised 2026). arXiv:[2502.08691](https://arxiv.org/abs/2502.08691)
- **Contributes:** Per the abstract: an LLM-driven social simulator with realistic environments and over 10,000 agents, applied to polarisation, inflammatory messages, universal basic income, external shocks, and urban sustainability.
- **How SocietyTwin uses it:** Reference point for what large interacting LLM societies involve; such societies are FUTURE WORK for SocietyTwin.
- **Limitations / relevance:** Resource-intensive; not a Türkiye-specific system.

### On the limits of agency in agent-based models (AgentTorch)

- **Citation:** Chopra, A., Kumar, S., Giray-Kuru, N., Raskar, R., & Quera-Bofarull, A. (2024). arXiv:[2409.10568](https://arxiv.org/abs/2409.10568)
- **Contributes:** Per the abstract: "LLM archetypes" allow millions of adaptive agents while balancing cost and expressiveness; demonstrated with 8.4 million agents representing New York City during COVID-19.
- **How SocietyTwin uses it:** FUTURE WORK option for population-wide AI behaviour without one LLM call per record.
- **Limitations / relevance:** Archetypes trade individual expressiveness for scale.

### Synthpop++: A Hybrid Framework for Generating A Country-scale Synthetic Population

- **Citation:** Neekhra, B., Kapoor, K., & Gupta, D. (2023). AI4ABM workshop at ICLR 2023. arXiv:[2304.12284](https://arxiv.org/abs/2304.12284)
- **Contributes:** Per the abstract: combines multiple surveys with overlapping attributes into a country-scale synthetic population (India) with demographic, socioeconomic, health, and geolocation attributes and family structures.
- **How SocietyTwin uses it:** Evidence that country-scale, multi-source synthesis is feasible; informs multi-survey harmonisation.
- **Limitations / relevance:** Different country and data sources; workshop paper.

### Mesa 3 and mesa-frames

- **Citation:** ter Hoeven, E., Kwakkel, J., Hess, V., Pike, T., Wang, B., rht, & Kazil, J. (2025). Mesa 3: Agent-based modeling with Python in 2025. *Journal of Open Source Software*, 10(107), 7668. doi:[10.21105/joss.07668](https://doi.org/10.21105/joss.07668). mesa-frames: <https://github.com/projectmesa/mesa-frames> (Apache-2.0).
- **Contributes:** Mesa is the Python ABM framework used in v1. mesa-frames stores agents in Polars DataFrames and reports up to 10× faster bulk updates at scale (per its README).
- **How SocietyTwin uses it:** Mesa is optional in v2, for small interaction experiments; mesa-frames is a candidate if large rule-based ABMs are needed ([report §12](societytwin-v2-architecture.md#12-scalability-strategy)).
- **Limitations / relevance:** mesa-frames does not state a stable release status.

## Data sources

Details and access status: [data-strategy.md](data-strategy.md).

### Official Statistics Programme 2022–2026

- **Citation:** Turkish Statistical Institute (TÜİK) (2023). *Official Statistics Programme 2022–2026*. Publication No. 4689. <https://www.resmiistatistik.gov.tr/media/pdf/rip/resmi_istatistik_programi_en.pdf>
- **Contributes:** Lists each official statistic with its responsible institution, periodicity, data collection method, classifications, geographic estimation level, and dissemination form; documents confidentiality rules and microdata access.
- **How SocietyTwin uses it:** Primary source for the geographic levels of every TÜİK table in the persona schema and data strategy.
- **Limitations / relevance:** Planning document; actual table forms must be checked on the data portal.

### Address Based Population Registration System Results, 2025

- **Citation:** TÜİK (February 2026). *Adrese Dayalı Nüfus Kayıt Sistemi Sonuçları, 2025*. <https://www.tuik.gov.tr/media/announcements/ADNKS_2025TR.pdf>; official announcement by TurkStat: population of Türkiye 86,092,168.
- **Contributes:** Resident population by province, sex, and age; degree of urbanisation shares.
- **How SocietyTwin uses it:** Root joint distribution of the generator and the population anchor for reconciliation.
- **Limitations / relevance:** Reuse terms **OPEN DECISION**.

### Other TÜİK statistics used

- **Citation:** TÜİK Household Labour Force Survey; National Education Statistics Database; statistics on marital status, place of birth, internal migration, and household type from administrative registers; ICT Usage Survey in Households and by Individuals; Income and Living Conditions Survey; Household Budget Survey; Life Satisfaction Survey. Portal: <https://veriportali.tuik.gov.tr>
- **Contributes:** Conditional distributions for education, labour status, occupation, sector, household, internet use, and income (stretch); held-out aggregates for experiment validity.
- **How SocietyTwin uses it:** See [persona-schema.md](persona-schema.md#3-population-record-schema-mvp-candidate-attributes).
- **Limitations / relevance:** Table forms, years, and cross-tabulations must be verified in the feasibility phase.

### TÜİK microdata access

- **Citation:** TÜİK. *Instruction on Micro Data Access and Usage* (enacted 01.09.2012); microdata page <https://www.tuik.gov.tr/Kurumsal/Mikro_Veri>; Electronic Data Research Centre (E-VAM) <https://evam.tuik.gov.tr>
- **Contributes:** Group B microdata (identifiers hidden) available to eligible researchers after application and commitment; Group A only in Data Research Centres or E-VAM.
- **How SocietyTwin uses it:** Governs any future use of microdata for the advanced generator.
- **Limitations / relevance:** Eligibility and timeline **OPEN DECISION**.

### Personal Data Protection Law No. 6698 (KVKK)

- **Citation:** Republic of Türkiye, Law No. 6698 on the Protection of Personal Data (24 March 2016).
- **Contributes:** Article 6 defines special categories of personal data; Article 28(b) (as cited in TÜİK's Official Statistics Programme) exempts processing for research, planning, and statistics when data is anonymised.
- **How SocietyTwin uses it:** Basis for excluding special-category attributes and for the privacy design ([ethics-and-limitations.md](ethics-and-limitations.md)).
- **Limitations / relevance:** Legal interpretation should be confirmed by the course or university if questions arise.

### World Bank Open Data

- **Citation:** World Bank. Data licence: Creative Commons Attribution 4.0 International (CC BY 4.0). <https://datacatalog.worldbank.org/public-licenses>
- **Contributes:** National indicators for Türkiye.
- **How SocietyTwin uses it:** Cross-checks only.
- **Limitations / relevance:** National level only.

### World Population Prospects 2024

- **Citation:** United Nations, Department of Economic and Social Affairs, Population Division (2024). *World Population Prospects 2024*. Licence: CC BY 3.0 IGO. <https://population.un.org/wpp/>
- **Contributes:** National population estimates and projections.
- **How SocietyTwin uses it:** Cross-check of national totals.
- **Limitations / relevance:** Modelled estimates; national level.

## Future-research sources

### Agent-Based Computational Economics: Growing Economies From the Bottom Up

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

**Relevance to SocietyTwin (v2):** *Future-research source.* Background for bottom-up agent-based modelling. In v2, rule-based population dynamics and economic or policy scenarios are STRETCH or FUTURE WORK, so this source supports those extensions rather than the MVP.

### How to generate micro-agents? A deep generative modeling approach to population synthesis

- **Citation:** Borysov, S. S., Rich, J., & Pereira, F. C. (2019). *Transportation Research Part C: Emerging Technologies*, 106, 73–97. doi:[10.1016/j.trc.2019.07.006](https://doi.org/10.1016/j.trc.2019.07.006)
- **Contributes:** Deep generative models for population synthesis.
- **How SocietyTwin uses it:** FUTURE WORK: an alternative generator for high-dimensional schemas.
- **Limitations / relevance:** Requires microdata for training; harder to explain and validate.

## How the sources map to the v2 architecture

| v2 component | Sources |
|---|---|
| Dependency model and generator | Chapuis et al. (2022); Deming & Stephan (1940); Beckman et al. (1996); Sun & Erath (2015); Farooq et al. (2013); Yameogo et al. (2021); MatrAIx (2026) |
| Constraints and rare combinations | Garrido et al. (2020); MatrAIx (2026) |
| Households (stretch) | Ye et al. (2009); Yameogo et al. (2021) |
| Population validation | Chapuis et al. (2022); Snoke et al. (2018); Collins et al. (2024) |
| AI-agent activation and experiments | MatrAIx (2026); Park et al. (2023; 2024); Argyle et al. (2023); Aher et al. (2023) |
| Persona consistency and robustness | MatrAIx (2026); Cheng et al. (2023); Ye et al. (2026); Wu et al. (2026) |
| Experiment validity | SimBench (Hu et al., 2026); Santurkar et al. (2023); Durmus et al. (2023); Social Simulation Arena |
| Ethics and limitations | Wang et al. (2025); MatrAIx grounding position paper (2026); KVKK |
| Data layer | TÜİK Official Statistics Programme; ADNKS 2025; other TÜİK statistics; World Bank; UN WPP |
| Optional dynamics (stretch) | Windrum et al. (2007); Collins et al. (2024); Tesfatsion (2002); Mesa 3 |

## Additional literature to investigate

> These are **research targets, not citations.** Nothing below has been reviewed or verified.

| # | Research target | What to look for |
|---|---|---|
| A | Türkiye-specific synthetic populations or microsimulation | Existing Turkish population synthesis or microsimulation studies using TÜİK data |
| B | Turkish-language LLM persona evaluation | How LLMs behave in Turkish when simulating respondents; known biases |
| C | Digital society twin definitions | Definitions of social or society-level digital twins, to position SocietyTwin's terminology |
| D | Linked household synthesis with Turkish data | Household–person synthesis using TÜİK household tables or SILC |
| E | Evaluation of synthetic survey respondents against national surveys | Methods comparing LLM survey responses with national statistical-office survey results |

### Verification checklist for new sources

- [ ] Located at the publisher's page or an official repository.
- [ ] Title, authors, year, publication, and DOI or URL copied from that page, not from memory or an AI tool.
- [ ] Contribution, use in SocietyTwin, and limitations written from the source itself, or marked "TODO: Requires source review."
