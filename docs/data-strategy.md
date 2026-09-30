# Türkiye Data Strategy (PROPOSED)

> **Status: PROPOSED.** No dataset has been downloaded, and no dataset is committed to this repository. Access, table formats, years, and reuse terms must be confirmed in the data-feasibility phase.

SocietyTwin is **CONFIRMED** to be Türkiye-only. Its synthetic population is built from **official aggregate statistics**, with TÜİK (Turkish Statistical Institute) as the primary candidate source; other sources only supplement or cross-check where justified. Attribute-level details, including each attribute's data status (CONFIRMED DATA, CANDIDATE DATA, PROPOSED, OPEN DECISION), are in [persona-schema.md](persona-schema.md).

## 1. Principles

1. **Official aggregates first.** Population records are generated from published aggregate tables. No individual-level data is needed for the MVP.
2. **Provenance for every number.** Every downloaded file is recorded in [`data/manifest.yaml`](../data/manifest.yaml) with its source, URL, reference year, scope, variables, licence, download date, and checksum.
3. **Nothing is invented.** If a needed table does not exist, the attribute is dropped, moved to a later stage, or modelled under a documented assumption (provenance class `MODELLED` or `ASSUMED`).
4. **Data never enters Git.** Raw files, processed tables, generated populations, and experiment results are git-ignored ([data/README.md](../data/README.md)).

## 2. Source catalogue

Geographic levels and periodicity below are taken from TÜİK's **Official Statistics Programme 2022–2026** (primary source, see [sources.md](sources.md#türkiye-data-sources)). İBBS is Türkiye's statistical regional unit classification: NUTS-1 has 12 regions, NUTS-2 has 26 regions, and NUTS-3 corresponds to the 81 provinces.

| Source | Producer | Content used by SocietyTwin | Geographic level | Periodicity | Access | Reuse / licence | Status |
|---|---|---|---|---|---|---|---|
| Address Based Population Registration System (ADNKS) | TÜİK | Population by province, sex, age; degree of urbanisation | Türkiye, NUTS-1/2/3, district, municipality, village, quarter | Annual (t+1 month) | Public tables and database | **OPEN DECISION** | MVP core. 2025 total: 86,092,168 |
| Statistics on internal migration, marital status, place of civil registration, place of birth, and household type (administrative registers) | TÜİK | Marital status, household type and size, place of birth | NUTS-3 | Annual (t+7 months) | Statistical web tables, database | **OPEN DECISION** | MVP |
| National Education Statistics Database (NESD) | TÜİK | Educational attainment | NUTS-3, district | Annual (t+4 months) | Database | **OPEN DECISION** | MVP |
| Household Labour Force Survey (HLFS) | TÜİK | Labour status, occupation (ISCO-08), sector (NACE Rev. 2), by education (ISCED) | Annual: Türkiye, NUTS-1, NUTS-2 | Monthly and annual (t+80 days) | Press release, database, microdata set | **OPEN DECISION**; microdata via application | MVP |
| ICT Usage Survey in Households and by Individuals | TÜİK | Internet use | NUTS-1 | Annual (t+8 months) | Press release, database | **OPEN DECISION** | MVP |
| Income and Living Conditions Survey (SILC) | TÜİK | Income quintiles, poverty | Türkiye, NUTS-1, NUTS-2 (cross-sectional) | Annual (t+6 months) | Press release, database, microdata set | **OPEN DECISION**; microdata via application | STRETCH |
| Household Budget Survey | TÜİK | Consumption structure | Türkiye annually; NUTS-1/2 from 3-year combined data | Annual | Press release, database, microdata set | **OPEN DECISION** | FUTURE WORK |
| Birth, death, and cause-of-death statistics | TÜİK | Vital events (for population dynamics and validation) | Türkiye, NUTS-1/2/3, district | Annual | Tables, database | **OPEN DECISION** | STRETCH (dynamics) |
| Life tables | TÜİK | Mortality by age and sex | Türkiye, NUTS-3 | Annual | Tables | **OPEN DECISION** | STRETCH (dynamics) |
| Population projections | TÜİK | Future marginals for time-shifted populations | NUTS-3 | Periodic | Tables | **OPEN DECISION** | FUTURE WORK |
| Life Satisfaction Survey | TÜİK | Held-out survey aggregates for experiment validity | *verify* | Annual | Press release, tables | **OPEN DECISION** | MVP candidate for validity pilot |
| Türkiye Demographic and Health Survey | Hacettepe University Institute of Population Studies | Fertility, family, health indicators | Türkiye, urban–rural, 5 regions, NUTS-1 (specific indicators) | Every 5 years | Reports; data on application (*verify*) | **OPEN DECISION** | FUTURE WORK |
| World Bank indicators | World Bank | National cross-checks | Türkiye (national) | Annual | Open data | CC BY 4.0 (verified) | Cross-check only |
| UN World Population Prospects 2024 | UN DESA Population Division | National population cross-check | Türkiye (national) | Periodic revisions (latest: 2024) | Open data | Figures and tables in the publication: CC BY 3.0 IGO; data-file licence **OPEN DECISION** | Cross-check only |
| Eurostat | European Commission | Harmonised indicators where Türkiye is covered | Varies | Varies | Open data | Coverage for Türkiye **verify** | FUTURE WORK |

TÜİK publications state that TÜİK reserves the rights to its publications under Law No. 5846. The reuse terms for tables downloaded from the TÜİK data portal have **not** been confirmed and are recorded as an **OPEN DECISION**.

## 3. Microdata (not required for the MVP)

TÜİK distributes anonymised microdata under its *Instruction on Micro Data Access and Usage*:

- **Group B microdata** (identifying information hidden, no restriction on distribution) can be requested by eligible researchers through TÜİK's application system, after signing a commitment.
- **Group A microdata** can be used only inside TÜİK Data Research Centres or the remote Electronic Data Research Centre (E-VAM).

Microdata from HLFS or SILC would allow a stronger generator (a Bayesian network or IPU calibration, see [report §11](societytwin-v2-architecture.md#11-synthetic-population-generation)). **OPEN DECISION:** whether a student team is eligible, whether the timeline allows an application, and whether the instructor wants it. If used, microdata is never committed, never copied outside the approved environment, and never used to create records that resemble real respondents.

## 4. Ingestion pipeline (PROPOSED)

1. **Acquire.** Download each table manually or with a download script. Record the manifest entry, including the checksum.
2. **Validate.** Check schema, category labels, totals, and missing cells. Report problems rather than silently fixing them.
3. **Harmonise.**
   - Geography: map every table to İBBS codes (NUTS-1/2/3) and keep a single geography dimension table.
   - Age: map every table's age groups to a common set of age bands, and record the mapping.
   - Categories: map education to ISCED-based levels, occupations to ISCO-08 major groups, and sectors to NACE Rev. 2 broad sectors.
   - Years: record the reference year of each table. Where tables come from different years, record the mismatch as a known limitation.
4. **Reconcile.** Where two official tables disagree on a shared total (for example the same province total in two tables), keep ADNKS as the anchor and record the discrepancy.
5. **Publish constraint tables.** Write the harmonised marginals and cross-tabulations as Parquet files in `data/processed/` for the generator. This folder is git-ignored.

## 5. Held-out data for validation

Some official tables must be **kept out of generation** so that they can test whether dependencies were preserved ([validation-strategy.md](validation-strategy.md)). The held-out set will be chosen once the available cross-tabulations are known. **OPEN DECISION**

## 6. Known data limitations

- Different tables have different reference years, geographies, and population bases (administrative registers versus sample surveys).
- Sample surveys (HLFS, ICT, SILC) have sampling error and publish regional detail only at NUTS-1 or NUTS-2.
- Joint distributions of more than two or three attributes are generally not published, so higher-order dependencies are modelled, not measured.
- Categories change over time (for example the HLFS definitions aligned with the 19th ICLS from 2021).
- Coverage of foreign residents and people under temporary protection needs to be clarified before any citizenship-related attribute is considered.
