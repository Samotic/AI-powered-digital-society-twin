# Project overview

- **Project:** SocietyTwin — AI-Powered Digital Society Twin for Türkiye
- **Course:** Engineering Design II
- **Status:** v2 architecture **PROPOSED**; implementation not started
- **Full design:** [SocietyTwin v2 Architecture Report](societytwin-v2-architecture.md)

> **SocietyTwin is intended for population-level research and simulation, not individual-level prediction.** Its personas are synthetic and do not represent real Turkish citizens.

## Direction (CONFIRMED by the instructor)

- SocietyTwin focuses **only on Türkiye**.
- **5,000 synthetic agents is too small.** The population must be substantially larger, and the architecture must scale.
- SocietyTwin should have capabilities **inspired by large-scale synthetic-persona / AI-society systems**, with MatrAIx / Persona-8B as the main reference. SocietyTwin is not a clone of MatrAIx.

The exact population size is not specified by the instructor (**OPEN DECISION**).

## Problem

Researchers and students who want to explore how different groups in Türkiye might respond to a question or a hypothetical situation cannot easily run large studies with real people, and real individuals' data is protected. LLM-based simulated respondents are a possible tool for exploration, but the literature shows that they can misrepresent or flatten groups and that their results can be fragile. Existing synthetic-persona systems are global or product-oriented rather than grounded in Turkish official statistics.

SocietyTwin addresses a narrower, testable problem: **generate a synthetic population of Türkiye whose statistical properties are traceable to official sources and measurably validated, and provide a reproducible way to sample from it and run bounded AI-persona experiments with explicit limitations.**

## Research questions (PROPOSED)

**Primary.** To what extent can a synthetic population of Türkiye generated only from official aggregate statistics reproduce the source distributions and their published cross-tabulations as its size grows, and under what conditions do AI agents instantiated from its personas respond consistently with their persona attributes and comparably to held-out Turkish survey aggregates?

**Secondary.**

1. How much does dependency-aware generation reduce error on held-out cross-tabulations compared with independent-attribute sampling, and how does fidelity change from 10K to 1M records, particularly for small provinces?
2. What are the runtime, memory, and storage costs of generating, storing, and querying 10K, 100K, and 1M records on a single machine?
3. How consistently do LLM agents express their assigned attributes across repeated runs, prompt perturbations, and models?
4. For survey items with published TÜİK aggregates that were not used in generation, how close are subgroup response distributions of persona agents to the real aggregates, compared with simple baselines?

The previous research question (comparing ABM, Cohort-Component / Matrix Projection, and ML models) is superseded. Whether the TÜBİTAK 2209-B proposal can be revised accordingly is an **OPEN DECISION** ([report §5](societytwin-v2-architecture.md#5-research-questions)).

## Approach

1. **Data:** ingest, validate, and harmonise official TÜİK tables ([data-strategy.md](data-strategy.md)).
2. **Schema:** a small, evidence-backed Türkiye persona schema with provenance for every attribute ([persona-schema.md](persona-schema.md)).
3. **Generation:** dependency-aware, vectorised generation of population builds of 10K, 100K, and 1M records.
4. **Validation:** statistical representativeness and conditional consistency, including held-out tables ([validation-strategy.md](validation-strategy.md)).
5. **Cohorts:** reproducible filtering and sampling with weights.
6. **Experiments:** SURVEY and SCENARIO experiments in which a small number of sampled personas are instantiated as AI agents ([experiment-system.md](experiment-system.md)).
7. **Analysis:** subgroup comparison, persona-consistency and experiment-validity checks, and full reproducibility.

## Scope

**In scope (MVP, PROPOSED):** Türkiye aggregate data ingestion; persona schema; dependency-aware generation up to 1M records; statistical validation; cohort sampling; SURVEY and SCENARIO experiments with bounded AI activation; telemetry; subgroup analysis; reproducibility; a basic web playground.

**Stretch:** CHAT environment; linked households; income quintile; microdata-based generator; full-scale (about 86.1 million) build; vectorised population dynamics with the Cohort-Component / Matrix Projection benchmark; maps; cross-model audits.

**Future work:** web and app environments; interacting LLM societies and social networks; survey-grounded dispositions; pre-registered validity tests; economic and policy scenarios.

## Out of scope

SocietyTwin will **not**:

- cover any country other than Türkiye;
- predict the behaviour of specific real individuals;
- identify, reconstruct, or impersonate real people;
- support individual surveillance or real-time surveillance systems;
- model special-category attributes (ethnic origin, religion or sect, political opinion, health, and other categories under KVKK Article 6) or mother tongue;
- run an LLM for every stored record;
- claim that its personas represent real Turkish citizens or that its results predict Türkiye's future;
- make or automate government or political decisions;
- use private or personally identifiable data without authorisation.

## Key terms

| Term | Meaning |
|---|---|
| Population record | A lightweight, statistically generated fictional member of Türkiye's synthetic population |
| Persona | A richer view of one record: descriptors, provenance, and a persona card |
| Active AI agent | A persona temporarily instantiated with an LLM for one experiment trial |
| Population build | One generated population (schema version, data version, generator version, seed, size) |
| Cohort | A filtered and sampled set of records used by an experiment |
| Trial | One agent completing one item in one environment |
| Provenance class | How an attribute was obtained: official joint, official conditional, modelled, derived, assumed, or generated text |
| Held-out table | An official table deliberately not used in generation, kept for validation |

## Superseded material

The v1.0 architecture (5,000-agent demographic prototype) is archived in [archive/architecture-v1-demographic.md](archive/architecture-v1-demographic.md). What was kept, changed, or dropped is described in the [migration plan](migration-plan.md).
