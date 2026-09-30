# Validation Strategy (PROPOSED)

> **Status: PROPOSED.** No validation has been run. **No acceptance thresholds are set.** Thresholds are an **OPEN DECISION**, to be agreed with the instructor after the first baseline measurements.

SocietyTwin must **not** claim that its synthetic people represent real Turkish people. It makes narrower, testable claims at five levels. Each level answers a different question and uses different evidence.

| Level | Question | Evidence |
|---|---|---|
| 1. Statistical representativeness | Does the synthetic population reproduce the source distributions? | Marginal distributions versus the tables used for generation |
| 2. Conditional consistency | Are relationships between attributes preserved, and are impossible combinations absent? | Held-out cross-tabulations and constraint checks |
| 3. Persona consistency | Does an instantiated AI agent behave consistently with its assigned persona? | Controlled adherence tests, repeated runs, stereotype audits |
| 4. Experiment validity | Do experiment outputs correspond reasonably with held-out real aggregate data, where comparison is possible? | Published TÜİK survey aggregates not used in generation |
| 5. Reproducibility | Can the same population and experiment be reproduced? | Manifests, checksums, replay from cache |

Performance and cost are measured alongside validity (section 6).

## Metric choices

All distributions below are categorical (for example the education distribution of women aged 25–34 in one province). Let *p* be the reference distribution and *q* the synthetic distribution over the same categories.

| Metric | Definition | Why it is used | Where it is not used |
|---|---|---|---|
| **Total variation distance (TVD)** | ½ Σ \|pᵢ − qᵢ\| | Bounded between 0 and 1 and directly interpretable as the share of probability mass that would have to move to make the distributions equal. Primary distribution metric. | – |
| **Jensen–Shannon divergence (JSD, base 2)** | ½ KL(p‖m) + ½ KL(q‖m), with m = (p + q)/2 | Symmetric, bounded between 0 and 1, and finite even when one distribution has zero cells. Standard in LLM opinion-alignment work ([Santurkar et al., 2023](sources.md#core-methodology-sources); [Durmus et al., 2023](sources.md#core-methodology-sources)), so results are comparable. | – |
| KL divergence | Σ pᵢ log(pᵢ/qᵢ) | Not used as a headline metric: it is asymmetric and becomes infinite when the synthetic population has a zero where the reference does not, which can happen legitimately for rare cells. | Headline reporting |
| **MAE / RMSE of shares or counts** | Mean absolute / root mean squared error over cells | Easy to explain; RMSE penalises large cell errors. Continues the MAE/RMSE reporting of the earlier SocietyTwin design. | – |
| **Standardised RMSE (SRMSE)** | RMSE of cell counts divided by the mean cell count | Common in population-synthesis evaluation; allows comparison across tables of different sizes. | – |
| **Subgroup error** | Any of the above computed per subgroup (province, age group, sex, education) | Averages can hide large errors in small groups, especially small provinces. | – |
| Chi-squared tests | – | Not used for pass/fail: with 10⁵–10⁶ records almost every small difference becomes "significant", so effect sizes (TVD, JSD) are more informative. | Pass/fail decisions |
| **Cramér's V difference** | \|V_ref − V_syn\| for a pair of attributes | Checks that the *strength* of an association (for example education–occupation) is preserved, not only the cell shares. | – |
| **Constraint violation rate** | Share of records breaking a hard constraint | Must be exactly zero; any violation is a generator bug. | – |
| **Rare-cell recall** | Share of reference cells with expected count ≥ 1 that are non-empty in the synthetic population | Detects over-aggressive masking or sampling that erases legitimate rare combinations. | – |
| **Persona adherence rate** | Share of controlled trials where the agent's behaviour matches the declared attribute (or correctly does not express it) | Used by MatrAIx ([Li et al., 2026](sources.md#reference-systems)); directly measures persona consistency. | – |
| Performance | Runtime, peak memory, storage size, tokens, estimated cost | Scalability is a confirmed requirement; cost bounds the number of active agents. | – |

## 1. Statistical representativeness

For every table used in generation:

- compute TVD, JSD, and MAE of shares for each marginal, at every published geography (Türkiye, NUTS-1, NUTS-2, province);
- report subgroup errors, with **small provinces reported separately**;
- repeat for several seeds and for each population size (10K, 100K, 1M) to separate sampling noise from systematic error.

**Expected behaviour (hypothesis, not a claim):** random sampling error in a cell shrinks roughly with the square root of the number of records in that cell, so small provinces need large builds. The smallest provinces have well under 100,000 residents (*verify with ADNKS 2025*). At a scale of about 1 record per 86 residents (N = 1,000,000), they have on the order of a thousand records; at N = 100,000 they have about a hundred. This is one reason the MVP targets 1M records ([report §12](societytwin-v2-architecture.md#12-scalability-strategy)).

## 2. Conditional consistency

This level tests what independent sampling would break.

- **Held-out cross-tabulations.** Some official cross-tabulations are deliberately not used in generation ([data-strategy.md §5](data-strategy.md#5-held-out-data-for-validation)). Compare them with the synthetic population using conditional TVD per parent category and Cramér's V difference.
- **Ablation baseline.** Generate a population with the same marginals but independent attributes. Dependency-aware generation should have lower held-out conditional error. This quantifies the value of the dependency model.
- **Hard constraints.** The violation rate must be zero.
- **Soft constraints and rare cells.** Report the frequency of unusual-but-possible combinations and rare-cell recall.

## 3. Persona consistency

Applies only to active AI agents.

- **Attribute self-report.** Ask agents neutral questions whose answers follow from their persona (for example age group or region). Mismatches measure basic prompt adherence.
- **Controlled adherence tests.** Following MatrAIx, create matched personas that differ in one attribute and check whether the relevant behaviour appears only where it should. Report the adherence rate per attribute and per environment.
- **Stability.** Repeat identical trials without the cache and report the variation.
- **Robustness audit.** Apply small perturbations (persona-card wording, option order, instruction phrasing) and report how much results change. [Ye et al. (2026)](sources.md#core-methodology-sources) show that such perturbations can change simulated outcomes substantially.
- **Cross-model check.** Where the budget allows, repeat key experiments with a second model, as MatrAIx recommends.
- **Stereotype audit.** Inspect generated rationales for stereotyped language by subgroup, using the Marked Personas approach ([Cheng et al., 2023](sources.md#core-methodology-sources)).

## 4. Experiment validity

- Use survey items whose **real Turkish aggregate results are published** but which were **not used** to generate the population (candidate: TÜİK Life Satisfaction Survey items, *verify availability and breakdowns*).
- Ask the same items to a sampled cohort of persona agents and compare subgroup response distributions with the published aggregates using TVD and JSD.
- Compare against simple baselines: (a) the national average for everyone, and (b) a demographic-only statistical baseline that assigns each subgroup its published subgroup distribution where available. An LLM persona approach is only informative if it beats the national-average baseline.
- **Report variance, not just means.** LLM agents can behave like an "average persona" and under-represent diversity ([Wu et al., 2026](sources.md#core-methodology-sources); [Wang et al., 2025](sources.md#core-methodology-sources)). Report within-subgroup variance next to mean alignment.
- **Scope of conclusions.** Where alignment is weak, conclusions are restricted to exploratory, collective-level patterns.

**FUTURE WORK:** pre-registered comparisons. As in the MIT [Social Simulation Arena](sources.md#reference-systems), predictions for a not-yet-published TÜİK release could be locked in advance and scored when the release appears.

## 5. Reproducibility

- **Population builds:** the same data manifest, schema version, generator version, seed, and size must produce a byte-identical population (checked with a checksum).
- **Cohorts:** the same build, filter, sampling method, and seed must produce the same set of record IDs.
- **Experiments:** a re-run from the response cache must reproduce identical results. A fresh re-run (without the cache) is expected to differ because LLM outputs are not fully deterministic; the difference is reported as run-to-run variation.

## 6. Performance and cost

Reported for every build and experiment: runtime, peak memory, storage size, number of LLM calls, input and output tokens, cache hit rate, and estimated cost. Performance targets are an **OPEN DECISION** until baseline benchmarks exist; no performance guarantee is made.

## 7. Reporting

Every validation report states the population build, schema version, data sources and years, the metrics above, known limitations, and the six items of the MatrAIx grounding checklist ([sources.md](sources.md#reference-systems)): persona provenance, grounding evidence, selection or sampling logic, internal consistency checks, enactment checks, and intended use and inference scope.
