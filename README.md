# SocietyTwin — AI-Powered Digital Society Twin for Türkiye

**Engineering Design II · University research project**

> **Status:** v2 architecture **PROPOSED**, awaiting instructor and team approval. The repository contains documentation and placeholder folders only; implementation has not started.

SocietyTwin is being designed as a **Türkiye-only, large-scale, data-grounded synthetic society platform**. It will:

1. generate a large synthetic population of Türkiye from **official aggregate statistics** (primarily TÜİK);
2. **validate** that the population reproduces the source distributions and the relationships between attributes;
3. **sample cohorts** and turn a small number of sampled personas into **AI agents** for reproducible survey and scenario experiments;
4. analyse results **by subgroup**, with their uncertainty and limitations stated.

> **SocietyTwin is for population-level research, exploration, and hypothesis generation.** Its personas are synthetic. They do not represent real Turkish citizens, and its results are not predictions of real behaviour.

## Why v2

The instructor confirmed that SocietyTwin must focus **only on Türkiye**, that **5,000 synthetic agents is too small**, and that the platform should have capabilities **inspired by large-scale synthetic-persona systems** such as MatrAIx / Persona-8B. The earlier 5,000-agent demographic design is superseded and [archived](docs/archive/architecture-v1-demographic.md). SocietyTwin is **not** a clone of MatrAIx. It adopts selected ideas at a scale a semester project can build and validate ([report §7](docs/societytwin-v2-architecture.md#7-reference-systems)).

## Core idea: records, personas, and agents

| Level | What it is | Scale (PROPOSED) | Uses an LLM? |
|---|---|---|---|
| **Population record** | A lightweight, statistically generated fictional member of Türkiye's population | Builds of 10K, 100K, and **1M** records (1M default) | Never |
| **Persona** | A richer view of a sampled record: descriptors, provenance, and a persona card | Per cohort, on demand | No (template-based) |
| **Active AI agent** | A persona temporarily instantiated with an LLM for one experiment trial | Small, budget-bound pilots per experiment | Yes |

Population size and the number of AI agents are **different** things. The number of LLM calls grows with the experiment cohort, not with the population.

## Pipeline (simplified)

```mermaid
flowchart LR
    A["TÜİK aggregate data"] --> B["Ingestion and harmonisation"]
    B --> C["Dependency-aware generator"]
    C --> D[("Synthetic population<br/>up to 1M records")]
    D --> E["Cohort sampling"]
    E --> F["AI persona agents<br/>SURVEY / SCENARIO"]
    F --> G["Subgroup analysis"]
    G --> H["Validation"]
    H --> I["Playground"]
```

The full data flow, system context, generation process, persona-to-agent activation, experiment lifecycle, and deployment diagrams are in the [v2 architecture report](docs/societytwin-v2-architecture.md).

## Proposed MVP

- Ingest and harmonise selected TÜİK tables: population by province, sex, and age; marital status; education; labour status, occupation, and sector; household type; internet use.
- Persona schema `tr-persona-1` with about a dozen attributes, each with a source and provenance.
- Dependency-aware generation (conditional sampling with iterative proportional fitting) at 10K, 100K, and 1M records.
- Statistical validation: marginal and conditional fit, constraint checks, performance.
- Cohort filtering and sampling; SURVEY and SCENARIO experiments with a small number of AI agents.
- Subgroup comparison, export, and full reproducibility (seeds, configurations, versions).
- A basic web playground.

Stretch goals, future work, and the semester roadmap: [report §29–33](docs/societytwin-v2-architecture.md#29-mvp).

## Technology (PROPOSED)

Python 3.12 · NumPy · pandas · PyArrow / Parquet · DuckDB · PostgreSQL · FastAPI · Pydantic · provider-independent LLM adapter · Next.js + TypeScript · Recharts · pytest / Vitest · Docker Compose · GitHub Actions. Each choice is justified in [report §6.1](docs/societytwin-v2-architecture.md#61-technology-stack-proposed). Mesa is not part of the MVP core.

## Documentation

| Document | Content |
|---|---|
| [v2 architecture report](docs/societytwin-v2-architecture.md) | Full design: decisions, diagrams, MVP, roadmap, risks, open decisions |
| [Project overview](docs/project-overview.md) | Problem, research questions, scope |
| [Architecture reference](docs/architecture.md) | Modules, interfaces, target layout |
| [Persona schema](docs/persona-schema.md) | Attributes, sources, dependencies, constraints |
| [Data strategy](docs/data-strategy.md) | TÜİK and other sources, access, licences |
| [Validation strategy](docs/validation-strategy.md) | Five validation levels and metrics |
| [Experiment system](docs/experiment-system.md) | Playground, environments, telemetry |
| [Ethics and limitations](docs/ethics-and-limitations.md) | Privacy, bias, misuse, limits |
| [Methodology](docs/methodology.md) | Research methodology |
| [Sources](docs/sources.md) | Literature, reference systems, data sources |
| [Migration plan](docs/migration-plan.md) | v1 → v2 repository changes |
| [Team responsibilities](docs/team-responsibilities.md) and [research integration](docs/research-integration.md) | Roles and research streams |
| [Data handling](data/README.md) | Data folders and rules |

**Labels used in the documentation:** CONFIRMED · PROPOSED · OPEN DECISION · FUTURE WORK.

## Team

| Team member | Role |
|---|---|
| Bejan | Project Manager / System Architect |
| Sam | Literature Research |
| Pakhlavon | Technical Architecture / Technologies |
| Azra | Existing Systems / Similar Projects |
| Koray | Data + Population + Simulation Research |

Ownership of the new v2 modules has not been assigned yet (OPEN DECISION).

## Data and privacy

No dataset, generated population, or experiment result is committed to this repository. Only official aggregate statistics are used. Special-category attributes (such as ethnic origin, religion, political opinion, and health) are excluded, and personas have codes, not names. See [data/README.md](data/README.md) and [ethics and limitations](docs/ethics-and-limitations.md).
