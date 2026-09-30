# Validation Strategy (PROPOSED)

> **Status: PROPOSED.** No validation has been run. **No acceptance thresholds are set.** Thresholds are an **OPEN DECISION**, to be agreed with the instructor after the first baseline measurements.

SocietyTwin must **not** claim that its synthetic people represent real Turkish people. It makes narrower, testable claims.

## Three kinds of evidence

| Evidence | Data compared | What it can show | What it cannot show |
|---|---|---|---|
| **A. Source-table comparison** | Synthetic population vs the TÜİK tables **used** in generation | The generator reproduces its fitting targets (an implementation check) | That dependencies beyond the fitted tables are right |
| **B. Held-out-table comparison** | Synthetic population vs official TÜİK tables **not used** in generation | Whether dependencies between attributes were preserved (the main statistical evidence) | That personas behave like real people |
| **C. AI persona behavioural evaluation** | Agent responses vs the persona's attributes, and vs published Turkish survey aggregates not used in generation | Persona consistency, robustness, stereotyping, and group-level alignment | That any individual answer reflects a real person |

## Five validation levels

| Level | Question | Evidence type |
|---|---|---|
| 1. Statistical representativeness | Does the synthetic population reproduce the source distributions? | A |
| 2. Conditional consistency | Are relationships between attributes preserved, and are impossible combinations absent? | B (plus constraint checks) |
| 3. Persona consistency | Does an instantiated AI agent behave consistently with its assigned persona? | C |
| 4. Experiment validity | Do experiment outputs correspond reasonably with held-out Turkish aggregate data, where comparison is possible? | C |
| 5. Reproducibility | Can the same population and experiment be reproduced? | Manifests, checksums, cache replay |

## Metric choices

All distributions are categorical (for example the education distribution of women aged 25–34 in one province). Let *p* be the reference distribution and *q* the synthetic distribution over the **same set of categories**.

| Metric | Definition | Why and where it is used | Where it is not used |
|---|---|---|---|
| **Total variation distance (TVD)** | ½ Σ \|pᵢ − qᵢ\| | Primary distribution metric (levels 1, 2, 4). Bounded 0–1; the share of probability mass that would have to move to make the distributions equal. | – |
| **Jensen–Shannon divergence (JSD, base 2)** | ½ KL(p‖m) + ½ KL(q‖m), m = (p + q)/2 | Levels 1, 2, 4. Symmetric, bounded 0–1, finite when one distribution has zero cells; common in LLM opinion-alignment work ([Santurkar et al., 2023](sources.md#persona-and-llm-research); [Durmus et al., 2023](sources.md#persona-and-llm-research)). | – |
| KL divergence | Σ pᵢ log(pᵢ/qᵢ) | – | Headline reporting: asymmetric, and infinite when the synthetic population legitimately has a zero cell where the reference does not |
| **MAE / RMSE** | Mean absolute / root mean squared error over cell shares or counts | Levels 1 and 2; continues v1 reporting. RMSE penalises large cell errors. | – |
| **SRMSE** | RMSE of cell counts divided by the mean cell count | Levels 1 and 2; standard in population synthesis; comparable across tables of different sizes. | Shares (use MAE/RMSE) |
| **Subgroup error** | Any of the above per province, age group, sex, or education | All levels; averages hide large errors in small groups, especially small provinces. | – |
| **Cramér's V difference** | \|V_ref − V_syn\| for a pair of nominal attributes | Level 2; checks that the *strength* of an association (for example education–occupation) is preserved. | Ordinal-only comparisons, where rank correlation is more suitable |
| **Constraint violation rate** | Share of records breaking a hard constraint | Level 2; must be exactly zero (any violation is a generator bug). | – |
| **Rare-cell recall** | Share of reference cells with expected count ≥ 1 that are non-empty in the synthetic population | Level 2; detects sampling or masking that erases legitimate rare combinations. | – |
| **Persona adherence rate** | Share of controlled trials in which the agent's behaviour matches the declared attribute (or correctly does not express it), with a confidence interval | Level 3; used by MatrAIx ([Li et al., 2026](sources.md#reference-systems)). | – |
| Chi-squared tests | – | – | Pass/fail decisions: with large builds almost every small difference becomes "significant", so effect sizes (TVD, JSD) are more informative |

**Statistical appropriateness.**
- **Small agent cohorts:** experiment cohorts are much smaller than builds, so every level-3 and level-4 metric is reported with bootstrap confidence intervals and the number of agents per subgroup.
- **Small subgroups:** subgroups below a minimum size are not reported separately. The minimum size is an OPEN DECISION.
- **Category alignment:** distributions are compared only after both sides have been mapped to the same categories.

## 1. Statistical representativeness (evidence A)

For every table used in generation:

- compute TVD, JSD, and MAE of shares for each marginal, at every published geography (Türkiye, NUTS-1, NUTS-2, province);
- report subgroup errors, with **small provinces reported separately**;
- repeat for several seeds and at each benchmark scale (10K, 100K, 1M) to separate sampling noise from systematic error.

**Expected behaviour (hypothesis, not a claim):** random sampling error in a cell shrinks roughly with the square root of the number of records in that cell, so small provinces need large builds. Bayburt, reported as the least populous province in ADNKS 2025 with 82,836 residents (*verify in the TÜİK table*), would have about 960 records at N = 1M and about 96 at N = 100K. This is why 1M is PROPOSED as a working scale for province-level analysis ([report §12](societytwin-v2-architecture.md#12-scalability-strategy)); the final target size is an OPEN DECISION.

## 2. Conditional consistency (evidence B)

This level tests what independent sampling would break.

- **Held-out cross-tabulations.** Selected official cross-tabulations are not used in generation ([data-strategy.md §5](data-strategy.md#5-held-out-data-for-validation)). They are compared with the synthetic population using conditional TVD per parent category and Cramér's V difference.
- **Ablation baseline.** A population with the same marginals but independently sampled attributes is generated. Dependency-aware generation should have lower held-out conditional error; the difference quantifies the value of the dependency model.
- **Hard constraints.** The violation rate must be zero.
- **Soft constraints and rare cells.** The frequency of unusual-but-possible combinations and rare-cell recall are reported.

## 3. Persona consistency (evidence C)

Applies only to active AI agents.

- **Attribute self-report.** Agents answer neutral questions whose answers follow from their persona (for example age group or region). Mismatches measure basic prompt adherence.
- **Controlled adherence tests.** Following MatrAIx, matched personas that differ in one attribute test whether the relevant behaviour appears only where it should. The adherence rate is reported per attribute and environment.
- **Stability.** Identical trials are repeated without the cache, and the variation is reported.
- **Robustness audit.** Small perturbations (persona-card wording, option order, instruction phrasing) are applied, and the change in results is reported. [Ye et al. (2026)](sources.md#validation-research) show that such perturbations can change simulated outcomes substantially.
- **Cross-model check.** Where the budget allows, key experiments are repeated with a second model.
- **Stereotype audit.** Generated rationales are inspected for stereotyped language by subgroup, following the Marked Personas approach ([Cheng et al., 2023](sources.md#persona-and-llm-research)).

## 4. Experiment validity (evidence C)

- **Items.** Survey items whose **real Turkish aggregate results are published** but which were **not used** in generation (candidate: TÜİK Life Satisfaction Survey items; *verify availability and breakdowns*).
- **Comparison.** The same items are asked to a sampled cohort of persona agents, and subgroup response distributions are compared with the published aggregates using TVD and JSD, with bootstrap intervals.
- **Baselines.** Two simple baselines: (a) the national distribution for everyone; (b) a demographic-only statistical baseline that assigns each subgroup its published subgroup distribution where available. The persona approach is informative only if it beats baseline (a).
- **Variance.** LLM agents can behave like an "average persona" and under-represent diversity ([Wu et al., 2026](sources.md#validation-research); [Wang et al., 2025](sources.md#persona-and-llm-research)), so within-subgroup variance is reported next to mean alignment.
- **Scope of conclusions.** Where alignment is weak, conclusions are restricted to exploratory, collective-level patterns.

**FUTURE WORK:** pre-registered comparisons. As in the MIT [Social Simulation Arena](sources.md#reference-systems), predictions for a not-yet-published TÜİK release could be locked in advance and scored when the release appears.

## 5. Reproducibility

- **Population builds:** the same data manifest, schema version, generator version, seed, and size must produce a byte-identical population (checked with a checksum).
- **Cohorts:** the same build, filter, sampling method, and seed must produce the same set of record IDs.
- **Experiments:** a re-run from the response cache must reproduce identical results. A fresh re-run (without the cache) is expected to differ because LLM outputs are not fully deterministic; the difference is reported as run-to-run variation, together with the model, parameters, and versions recorded for each call ([report §14.1](societytwin-v2-architecture.md#141-metadata-recorded-for-every-ai-call)).

## 6. Benchmark dimensions

The four scale dimensions of the architecture ([report §12](societytwin-v2-architecture.md#12-scalability-strategy)) are measured at 10K, 100K, and 1M:

| Dimension | Scale type |
|---|---|
| Generation time | Population generation |
| Peak memory | Generation, storage and query |
| Storage size | Storage and query |
| Query and filter time | Storage and query |
| Sampling time | Storage and query |
| Experiment runtime | Active AI agents |
| Number of AI calls | Active AI agents |
| Input and output tokens | Active AI agents |
| Estimated AI cost | Active AI agents |

Targets are an **OPEN DECISION** until baseline benchmarks exist; no performance guarantee is made.

## 7. Reporting

Every validation report states:
- the population build, schema version, data sources, and years;
- the metrics above;
- known limitations;
- the six items of the MatrAIx grounding checklist ([sources.md](sources.md#validation-research)): persona provenance, grounding evidence, selection or sampling logic, internal consistency checks, enactment checks, and intended use and inference scope.
