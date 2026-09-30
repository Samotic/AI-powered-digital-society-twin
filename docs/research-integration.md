# Research integration

This document explains how the team's five research streams come together into one SocietyTwin design. Roles and deliverables are listed in [team-responsibilities.md](team-responsibilities.md).

## Structure

```mermaid
flowchart TD
    B["Bejan<br/>System Definition"]
    S["Sam<br/>Academic Foundations"]
    A["Azra<br/>Existing Systems / Gaps"]
    P["Pakhlavon<br/>Technical Architecture"]
    K["Koray<br/>Population / Agents / Simulation"]
    I["Integrated SocietyTwin Design<br/>(integrated by Bejan)"]
    O["System definition · Architecture · Scope<br/>Presentation · TÜBİTAK proposal"]

    B --> S
    B --> A
    B --> P
    B --> K
    S --> I
    A --> I
    P --> I
    K --> I
    I --> O
```

1. **Bejan** (Project Manager / System Architect) sets the initial system definition: the objective, main problem, and boundaries that the research streams work within.
2. **Sam, Azra, Pakhlavon, and Koray** each research one part of the system.
3. **Bejan** integrates their outputs into the final SocietyTwin design and the documents built from it.

## What each research stream contributes

| Research stream | Question it answers | Output | Feeds into |
|---|---|---|---|
| Sam: Academic Foundations | What does the research literature say about digital twins, social simulation, synthetic populations, and agents? | Reviewed sources ([sources.md](sources.md)) | Theoretical basis for the system definition; references for the presentation and TÜBİTAK proposal |
| Azra: Existing Systems / Gaps | What systems already exist, and what can they not do? | Comparison of existing systems | The gap SocietyTwin addresses and its stated contribution |
| Pakhlavon: Technical Architecture | How could SocietyTwin be built, and why does it need each technology? | Justified technology assessment | Technical side of the architecture; tools listed in `requirements.txt` |
| Koray: Population / Agents / Simulation | How will the population, agents, simulation, and evaluation work? | Population Schema + Agent Schema + Simulation Concept | In v2: the [persona schema](persona-schema.md), the dependency model, and the [validation strategy](validation-strategy.md) |

## Integrated outputs

The Project Manager / System Architect combines the research outputs into:

| Output | Main inputs |
|---|---|
| Final system definition (objective, target users, problem, boundaries, capabilities) | All streams |
| Architecture ([v2 architecture report](societytwin-v2-architecture.md), PROPOSED) | Pakhlavon, Koray |
| Scope ([project-overview.md](project-overview.md#scope)) | All streams, especially Azra's gap analysis |
| Presentation | All streams; at least 5 sources selected from Sam's list |
| TÜBİTAK proposal | All streams, especially Sam's sources and Azra's gap and contribution |

## From existing work to contribution

Azra's and Sam's research together should support a clear argument for the presentation and the TÜBİTAK proposal:

```text
Existing Work               (Azra: existing systems; Sam: literature)
      ↓
Existing Limitation / Gap
      ↓
Our Contribution            (integrated by Bejan into the system definition)
```

This argument has not been written yet. It depends on the research outputs above.

## Status

New instructor feedback (Türkiye only, a substantially larger scalable population, MatrAIx-inspired persona capabilities) led to the PROPOSED [SocietyTwin v2 architecture](societytwin-v2-architecture.md). The existing research responsibilities remain valid and map onto v2 topics as follows. This mapping describes research questions, **not** implementation ownership, which is an **OPEN DECISION**.

| Research stream | Relevant v2 topics |
|---|---|
| Sam: Academic Foundations | Population synthesis, persona-conditioned LLM agents, validation literature ([sources.md](sources.md)) |
| Azra: Existing Systems / Gaps | Reference systems such as MatrAIx, Social Simulation Arena, AgentSociety, and country-scale synthetic populations ([report §7](societytwin-v2-architecture.md#7-reference-systems)) |
| Pakhlavon: Technical Architecture | Technology stack and scalability ([report §6.1 and §12](societytwin-v2-architecture.md#61-technology-stack-proposed)) |
| Koray: Population / Agents / Simulation | Persona schema, dependency model, TÜİK data, validation |
| Bejan: System Definition | Scope, MVP, open instructor decisions ([report §29 and §35](societytwin-v2-architecture.md#35-open-instructor-decisions)) |

This document describes how the research streams feed the design. It does not record individual research findings.
