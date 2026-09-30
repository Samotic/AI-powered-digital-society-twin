# Methodology (v2, PROPOSED)

**Status:** Planned. Nothing described here has been carried out yet. The design rationale is in the [v2 architecture report](societytwin-v2-architecture.md), and sources are in [sources.md](sources.md).

## 1. Data feasibility

The team will confirm which TÜİK tables exist in the needed form (for example population by province, sex, and age; education by province, sex, and age; labour status by sex, age group, and education), their reference years, and their reuse terms. Attributes without a suitable table are dropped, deferred, or modelled under a documented assumption. Tables to be held out for validation are chosen at this stage ([data-strategy.md](data-strategy.md)).

## 2. Data ingestion and harmonisation

Downloaded tables are recorded in the data manifest with checksums, validated, and harmonised to common geography (İBBS NUTS-1/2/3), age bands, and classifications (ISCED-based education, ISCO-08, NACE Rev. 2). Where official tables disagree on a shared total, ADNKS is the anchor and the discrepancy is recorded.

## 3. Schema definition

The persona schema `tr-persona-1` ([persona-schema.md](persona-schema.md)) defines the attributes, categories, dependency graph, hard constraints, and provenance classes. It is reviewed and approved before generation starts.

## 4. Population synthesis

The MVP method is **synthetic reconstruction from aggregate tables**, the family reviewed by Chapuis, Taillandier and Drogoul (2022):

1. Fit the conditional distribution of each attribute given its parents, using iterative proportional fitting (Deming & Stephan, 1940) to match all available official marginals.
2. Allocate N records to province × sex × age-group cells with controlled rounding that preserves totals.
3. Sample each remaining attribute in dependency order, applying hard-constraint masks only for definitional impossibilities, so that legitimate rare combinations survive.
4. Write the build as partitioned Parquet with a manifest.

An **ablation** build with independently sampled attributes is generated for comparison. If TÜİK microdata becomes available, a Bayesian network learned from microdata and calibrated to official marginals (Sun & Erath, 2015) is the advanced alternative.

## 5. Population validation

Each build is compared with the source tables used in generation (statistical representativeness, an implementation check) and with held-out official tables not used in generation (conditional consistency: association strength, constraint violations, rare cells), across several seeds and at the benchmark scales of 10K, 100K, and 1M records. Metrics and their justification are in [validation-strategy.md](validation-strategy.md). Acceptance thresholds are agreed with the instructor after the first measurements.

## 6. Cohort sampling

Experiments use cohorts drawn with simple random or stratified sampling and a recorded seed. Inclusion weights are kept so that subgroup results can be weighted back to the population.

## 7. AI-persona experiments

Sampled personas are rendered as persona cards and instantiated as AI agents for single trials in SURVEY or SCENARIO environments ([experiment-system.md](experiment-system.md)). Answers are structured and validated. Every trial records the persona, item, model, prompt version, parameters, seed, output, and usage. A deterministic stub model is used for development and testing.

## 8. Persona consistency

Agents are tested for attribute self-report accuracy, controlled persona adherence (as in MatrAIx), stability across repeated runs, robustness to small prompt changes (Ye et al., 2026), and stereotyped language (Cheng et al., 2023).

## 9. Experiment validity

For survey items with published Turkish aggregates that were not used in generation, subgroup response distributions of persona agents are compared with the real aggregates using total variation distance and Jensen–Shannon divergence, against national-average and demographic-only baselines. Within-subgroup variance is reported alongside mean alignment (Wu et al., 2026).

## 10. Reproducibility

Builds, cohorts, and experiments each have a manifest. Seeds are split per partition, so results do not depend on processing order. LLM responses are cached, so experiments can be replayed exactly; fresh re-runs are used to measure run-to-run variation.

## 11. Supporting engines from v1 (optional)

The v1 population-dynamics work (aging, births, deaths, migration) and the Cohort-Component / Matrix Projection benchmark may be added as a STRETCH goal: vectorised yearly dynamics over population records, validated against historical TÜİK data with MAE, RMSE, and age-group errors, and docked against the deterministic cohort-component projection ([report §17](societytwin-v2-architecture.md#17-abm--cohort--ml-integration-decision)). The v1 ML forecasting baseline is future work.

## 12. Ethics

Only official aggregate statistics are used; special-category attributes are excluded; personas have codes, not names; every output is labelled as synthetic and not a prediction. See [ethics-and-limitations.md](ethics-and-limitations.md).
