# Team responsibilities

This document records the team's current task allocation, as set out in the Project Management document. Update it whenever roles or responsibilities change.

How the five research streams come together is described in [research-integration.md](research-integration.md).

## Summary

| Team member | Role | Main research responsibility | Expected deliverable |
|---|---|---|---|
| Bejan | Project Manager / System Architect | Define the system and integrate the team's work | Integrated system definition, architecture, scope, presentation structure, and TÜBİTAK form |
| Sam | Literature Research | Academic foundations of the project | Approximately 8–10 reviewed sources, from which the team selects at least 5 |
| Pakhlavon | Technical Architecture / Technologies | How the system could technically be built | Technology assessment in which every technology is justified |
| Azra | Existing Systems / Similar Projects | Existing academic, industry, and open-source systems | Comparison of existing systems leading to SocietyTwin's gap and contribution |
| Koray | Data + Population + Simulation Research | How the population, agents, simulation, and evaluation could work | Population Schema + Agent Schema + Simulation Concept |

## Bejan

**Role:** Project Manager / System Architect

**Main research responsibility:** Define the system and integrate the team's work.

**Responsibilities:**

- Project objective
- Target users
- Main problem
- System boundaries
- Main capabilities
- Overall system architecture
- Integration of everyone's research
- Presentation structure
- IN SCOPE / OUT OF SCOPE definition
- Final GitHub structure
- Coordination of the TÜBİTAK form

**Expected deliverable:** An integrated SocietyTwin system definition, combining the four research streams into the final system definition, architecture, scope, presentation, and TÜBİTAK proposal.

**Related documents:** [project-overview.md](project-overview.md), [architecture.md](architecture.md)

## Sam

**Role:** Literature Research

**Main research responsibility:** Research the academic foundations behind the project.

**Research areas:**

- Digital twins
- Social / digital society twins
- Agent-based modeling
- Synthetic populations
- Generative agents
- Social simulation
- LLM-based agents
- Socio-technical systems
- Population-level simulation

**Expected deliverable:** Approximately 8–10 strong academic or technical sources, each recorded with Paper Title, Year, Problem, Method, Data, Model / Architecture, Results, Limitations, and Relevance to SocietyTwin. The team will select at least 5 of the strongest for the presentation.

**Related document:** [sources.md](sources.md), which currently contains 5 verified core sources and a list of further research targets.

## Pakhlavon

**Role:** Technical Architecture / Technologies

**Main research responsibility:** Research how the system could technically be built.

**Research areas:**

- Programming languages
- Agent frameworks
- AI / LLM technologies
- Simulation frameworks
- Databases
- APIs
- Data processing
- Visualization
- Backend
- Frontend
- Testing
- GitHub workflow

**Guiding rule:** Technologies should not be selected simply because they sound impressive. Every proposed technology must answer the question:

> "Why does SocietyTwin actually need this technology?"

**Expected deliverable:** A technology assessment covering the areas above. A suggested format for each entry:

| Area | Candidate technology | Why SocietyTwin needs it | Alternatives considered | Status |
|---|---|---|---|---|

**Related documents:** [architecture.md](architecture.md), [requirements.txt](../requirements.txt)

## Azra

**Role:** Existing Systems / Similar Projects

**Main research responsibility:** Research existing academic, industry, and open-source systems related to:

- Social digital twins
- Socio-technical digital twins
- Synthetic population systems
- Agent-based society simulations
- Generative-agent systems

**For each system, record:**

| System name | What it does | Technology | Strengths | Limitations | What SocietyTwin can learn from it |
|---|---|---|---|---|---|

**Expected deliverable:** A comparison of existing systems that establishes:

```text
Existing Work
      ↓
Existing Limitation / Gap
      ↓
Our Contribution
```

**Related document:** [research-integration.md](research-integration.md)

## Koray

**Role:** Data + Population + Simulation Research

**Main research responsibility:** Research how SocietyTwin could represent the population and agents, run simulations, and evaluate them.

**Population representation (research categories):**

- Age
- Occupation
- Location
- Socioeconomic characteristics
- Relationships
- Preferences
- Behavior

> These are research categories only. The instructor's future dataset is **not** assumed to contain all of these variables. The actual population schema will depend on the variables available in the dataset.

**Agent research:** agent attributes, agent states, agent behavior, agent interactions, social networks, and the environment.

**Simulation research:** how agents interact, how scenarios are introduced, how society changes over time, and how simulation outputs are measured.

**Evaluation research:** historical validation, statistical similarity, aggregate-level evaluation, model comparison, and scenario consistency.

**Expected deliverable:**

```text
Population Schema
        +
Agent Schema
        +
Simulation Concept
```

**Related documents:** [methodology.md](methodology.md), [data/README.md](../data/README.md)
