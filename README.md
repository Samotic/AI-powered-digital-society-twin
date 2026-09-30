# SocietyTwin — AI-Powered Digital Society Twin for Türkiye

**Engineering Design II · University research project**

> **Status:** v2 architecture **PROPOSED**. The overall direction is approved for refinement; specific decisions await instructor and team approval. The repository contains documentation and placeholder folders only; implementation has not started.

SocietyTwin is being designed as a **Türkiye-only, data-grounded synthetic society platform**. It will:

1. generate a synthetic population of Türkiye, at configurable scale, from **official aggregate statistics** (primarily TÜİK);
2. **validate** that the population reproduces the published Turkish distributions and the relationships between attributes;
3. **sample cohorts**, construct personas, and turn a small number of them into **AI agents** for reproducible survey and scenario experiments;
4. analyse results **by subgroup**, with uncertainty and limitations stated.

> **SocietyTwin is for population-level research, exploration, and hypothesis generation.** Its personas are synthetic. They do not represent real Turkish citizens, and its results are not predictions of real behaviour.

## Why Türkiye

- **Instructor requirement (CONFIRMED):** SocietyTwin focuses only on Türkiye.
- **Official data:** TÜİK publishes register-based population statistics (ADNKS) every year, down to district level. The 2025 resident population was **86,092,168**. TÜİK also publishes survey statistics on education, labour, households, and ICT use at national and regional levels.
- **Turkish structure:** every synthetic record belongs to one of Türkiye's 81 provinces (İBBS NUTS-3), with its NUTS-2 and NUTS-1 regions. Attributes use TÜİK's official categories, so synthetic results can be compared directly with Turkish statistics.

## Why v2

The instructor confirmed three things:
- SocietyTwin must focus **only on Türkiye**.
- **5,000 synthetic agents is too small.** The system should support a **substantially larger, scalable** population.
- **Large-scale synthetic-persona systems such as MatrAIx** are an important inspiration.

SocietyTwin is **inspired by architectural ideas from large-scale synthetic persona systems such as MatrAIx**. It is its own Türkiye-specific academic project, not a clone ([report §7](docs/societytwin-v2-architecture.md#7-reference-systems)). The earlier 5,000-agent demographic design is superseded and [archived](docs/archive/architecture-v1-demographic.md).

## Core idea: records, personas, and agents

| Level | What it is | Scale | Uses an LLM? |
|---|---|---|---|
| **Population record** | A lightweight, statistically generated fictional member of Türkiye's population | Configurable builds; benchmark scales 10K, 100K, 1M+ | Never |
| **Persona** | A richer view of a sampled record: descriptors, provenance, persona card | Per cohort, on demand | No (template-based) |
| **Active AI agent** | A persona temporarily instantiated with an LLM for one experiment trial | Small, budget-bound pilots | Yes |

**Population size and the number of AI agents are independent.** LLM calls grow with the experiment cohort, not with the population. The final target population size will be set from instructor requirements, available data, and benchmarks (OPEN DECISION). 1M is PROPOSED as the largest MVP benchmark ([report §12](docs/societytwin-v2-architecture.md#12-scalability-strategy)).

## Pipeline (simplified)

```mermaid
flowchart LR
    A["TÜİK aggregate data"] --> B["Ingestion and harmonisation"]
    B --> C["Dependency-aware generator"]
    C --> D[("Synthetic population<br/>configurable size")]
    D --> E["Cohort sampling<br/>and personas"]
    E --> F["AI persona agents<br/>SURVEY or SCENARIO"]
    F --> G["Subgroup analysis"]
    G --> H["Validation"]
    H --> I["Playground"]
```

The full data flow, system context, generation process, persona-to-agent activation, experiment lifecycle, and deployment are in the [v2 architecture report](docs/societytwin-v2-architecture.md).

## Proposed MVP: one complete vertical slice

`official Türkiye data → synthetic population → validation → cohort → personas → small controlled AI experiment → results → dashboard`

- TÜİK ingestion and harmonisation for the core attributes (province, sex, age, marital status, education, labour status), plus target attributes where data is confirmed.
- Dependency-aware generation (conditional sampling with iterative proportional fitting and hard constraints), benchmarked at 10K and 100K, with 1M as the PROPOSED target benchmark.
- Validation against source tables and held-out tables, with an independent-sampling ablation.
- Cohort sampling, template-based persona cards, and a small SURVEY (and, time permitting, SCENARIO) experiment with a stub model and then a budget-bound AI pilot.
- Subgroup comparison, export, reproducibility, and a basic web playground.

Stretch goals, future work, and the roadmap: [report §29–33](docs/societytwin-v2-architecture.md#29-mvp).

## Technology (PROPOSED)

Python 3.12 · NumPy · pandas · PyArrow / Parquet · DuckDB · PostgreSQL · FastAPI · Pydantic · provider-independent LLM adapter · Next.js + TypeScript · Recharts · pytest / Vitest · Docker Compose · GitHub Actions.

Each choice is justified in [report §6.1](docs/societytwin-v2-architecture.md#61-technology-stack-proposed). Mesa is not part of the MVP core.

## Documentation

| Document | Content |
|---|---|
| [v2 architecture report](docs/societytwin-v2-architecture.md) | Full design: decisions, diagrams, MVP, roadmap, risks, open decisions |
| [Project overview](docs/project-overview.md) | Problem, research questions, scope |
| [Architecture reference](docs/architecture.md) | Modules, interfaces, target layout |
| [Persona schema](docs/persona-schema.md) | Attributes, sources, status, dependencies, constraints |
| [Data strategy](docs/data-strategy.md) | TÜİK and other sources, access, licences |
| [Validation strategy](docs/validation-strategy.md) | Five validation levels and metrics |
| [Experiment system](docs/experiment-system.md) | Playground flow, environments, telemetry |
| [Ethics and limitations](docs/ethics-and-limitations.md) | Privacy, bias, misuse, limits |
| [Methodology](docs/methodology.md) | Research methodology |
| [Sources](docs/sources.md) | Literature, reference systems, data sources, source audit |
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

- No dataset, generated population, or experiment result is committed to this repository.
- Only official aggregate statistics are used.
- Special categories of personal data under KVKK Article 6 (such as ethnic origin, religion, political opinion, and health) are excluded, and personas have codes, not names.

See [data/README.md](data/README.md) and [ethics and limitations](docs/ethics-and-limitations.md).
