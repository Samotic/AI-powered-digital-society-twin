# SocietyTwin Master Persona Variables

**Version:** 1.0  
**Status:** Working Specification  
**Scope:** Türkiye Digital Society Twin  
**Schema:** tr-persona-1 compatible

---

## 1. Purpose

This document defines the candidate variables used to construct synthetic
population records, personas, and contextual information in SocietyTwin.

Variables are organised into four layers:

- **CORE** — demographic, household, education, labour, and income attributes.
- **BEHAVIOR** — digital and consumption behaviour.
- **OVERLAY** — survey-grounded attitudes and subjective indicators.
- **CONTEXT** — characteristics of the environment in which a persona lives.

Scenario outcomes are not permanent persona attributes. They are generated
during experiments from the interaction between persona, context, scenario,
and active AI agents.

---

## 2. Status Definitions

| Status | Meaning |
|---|---|
| `VERIFIED` | Variable and source mapping have been verified |
| `SOURCE_VERIFIED` | Suitable source identified; exact raw mapping still requires validation |
| `DERIVED` | Computed from other variables |
| `TARGET` | Intended for implementation; data integration is incomplete |
| `OPTIONAL` | Candidate for a later schema version |
| `NOT_SUPPORTED` | Insufficient evidence for inclusion |

---

# 3. CORE Variables

CORE variables describe the main statistical characteristics of synthetic
population records.

## 3.1 Demography

| Variable | Description | Source | Dataset | Processing | Parents | Geography | MVP | Status |
|---|---|---|---|---|---|---|---|---|
| `province` | Province of residence | TÜİK | ADNKS 2025 | Controlled allocation | Root | NUTS-3 | YES | VERIFIED |
| `sex` | Sex category | TÜİK | ADNKS 2025 | Controlled allocation | province | NUTS-3 | YES | VERIFIED |
| `age` | Age | TÜİK | ADNKS / GYKA 2025 | Direct | province, sex | Individual | YES | VERIFIED |
| `age_group` | Harmonised age group | SocietyTwin | Derived | Age grouping | age | Individual | YES | DERIVED |
| `marital_status` | Marital status | TÜİK | GYKA / marital statistics | Conditional distribution | age, sex, geography | Individual | YES | SOURCE_VERIFIED |
| `urbanisation_class` | Degree of urbanisation | TÜİK | Urban-rural statistics | Geographic mapping | province | Settlement | TARGET | SOURCE_VERIFIED |
| `born_in_other_province` | Birth province differs from residence | TÜİK | Population statistics | Conditional | age, province | Individual | TARGET | SOURCE_VERIFIED |

---

## 3.2 Household

| Variable | Description | Source | Dataset | Processing | Parents | Geography | MVP | Status |
|---|---|---|---|---|---|---|---|---|
| `household_role` | Position within household | TÜİK | GYKA 2025 | Category mapping | age, sex | Household | NO | SOURCE_VERIFIED |
| `household_size` | Number of household members | TÜİK | Household Statistics / GYKA | Conditional | province, age, marital_status | Household | YES | SOURCE_VERIFIED |
| `household_type` | Household composition | TÜİK | Household Statistics / GYKA | Conditional | household_size, marital_status | Household | YES | SOURCE_VERIFIED |
| `household_income` | Household disposable income | TÜİK | GYKA 2025 | Numeric / weighted | household_type, labour_status | Household | NO | SOURCE_VERIFIED |
| `financial_difficulty` | Perceived household financial difficulty | TÜİK | GYKA 2025 | Category mapping | household_income | Household | NO | SOURCE_VERIFIED |
| `unexpected_expense_capacity` | Ability to meet an unexpected expense | TÜİK | GYKA 2025 | Category mapping | household_income | Household | NO | SOURCE_VERIFIED |
| `internet_at_home` | Household internet availability | TÜİK | GYKA 2025 | Binary mapping | household_income | Household | NO | SOURCE_VERIFIED |
| `car_ownership` | Household car ownership | TÜİK | GYKA 2025 | Category mapping | household_income | Household | NO | SOURCE_VERIFIED |

---

## 3.3 Education

| Variable | Description | Source | Dataset | Processing | Parents | Geography | MVP | Status |
|---|---|---|---|---|---|---|---|---|
| `education_level` | Highest education level | TÜİK | GYKA / National Education Statistics | Harmonisation | age, sex, region | Individual | YES | SOURCE_VERIFIED |
| `student_status` | Current education participation | TÜİK | GYKA 2025 | Category mapping | age, education_level | Individual | NO | SOURCE_VERIFIED |

---

## 3.4 Labour

| Variable | Description | Source | Dataset | Processing | Parents | Geography | MVP | Status |
|---|---|---|---|---|---|---|---|---|
| `labour_status` | Labour force status | TÜİK | GYKA / HLFS | Harmonisation | age, sex, education_level, region | Individual | YES | SOURCE_VERIFIED |
| `employment_type` | Employment arrangement | TÜİK | GYKA 2025 | Category mapping | labour_status | Individual | NO | SOURCE_VERIFIED |
| `occupation_group` | Occupation group | TÜİK | GYKA / HLFS | ISCO-08 harmonisation | labour_status, education_level | Individual | TARGET | SOURCE_VERIFIED |
| `economic_sector` | Economic activity | TÜİK | GYKA / HLFS | NACE Rev.2 harmonisation | labour_status, region | Individual | TARGET | SOURCE_VERIFIED |
| `working_hours` | Working hours | TÜİK | GYKA 2025 | Numeric | labour_status, occupation_group | Individual | NO | SOURCE_VERIFIED |
| `months_worked` | Months worked | TÜİK | GYKA 2025 | Numeric | labour_status | Individual | NO | SOURCE_VERIFIED |

---

## 3.5 Income

| Variable | Description | Source | Dataset | Processing | Parents | Geography | MVP | Status |
|---|---|---|---|---|---|---|---|---|
| `employment_income` | Employment income | TÜİK | GYKA 2025 | Numeric / weighted | labour_status, occupation_group | Individual | NO | SOURCE_VERIFIED |
| `individual_income` | Individual income | TÜİK | GYKA 2025 | Numeric / weighted | labour_status, education_level | Individual | NO | SOURCE_VERIFIED |
| `income_quintile` | Equivalent disposable income quintile | TÜİK | GYKA | Derived distribution | household_income, household_size | Household / Individual | STRETCH | DERIVED |

---

# 4. BEHAVIOR Variables

BEHAVIOR variables represent statistically grounded digital and consumption
behaviour.

## 4.1 Digital Behaviour

| Variable | Description | Source | Processing | Parents | MVP | Status |
|---|---|---|---|---|---|---|
| `internet_use` | Recent internet use | TÜİK ICT Survey | Conditional | age, sex, education_level, labour_status, region | TARGET | SOURCE_VERIFIED |
| `internet_frequency` | Frequency of internet use | TÜİK ICT Survey | Conditional | internet_use, age | NO | SOURCE_VERIFIED |
| `social_media_use` | Social network use | TÜİK ICT Survey | Conditional | internet_use, age, education_level | NO | SOURCE_VERIFIED |
| `ecommerce_use` | Online purchasing behaviour | TÜİK ICT Survey | Conditional | age, education_level, income_quintile | NO | SOURCE_VERIFIED |
| `egovernment_use` | e-Government service use | TÜİK ICT Survey | Conditional | age, education_level, internet_use | NO | SOURCE_VERIFIED |
| `online_banking_use` | Online banking use | TÜİK ICT Survey | Conditional | age, education_level, internet_use | NO | TARGET |
| `online_learning_use` | Online learning activity | TÜİK ICT Survey | Conditional | age, education_level | NO | TARGET |
| `generative_ai_use` | Generative AI usage | TÜİK AI Statistics | Conditional | age, education_level, labour_status | NO | OPTIONAL |

---

## 4.2 Consumption Behaviour

| Variable | Description | Source | Processing | Parents | MVP | Status |
|---|---|---|---|---|---|---|
| `food_spending_share` | Share of household expenditure on food | TÜİK HBA | Derived | income, household | NO | TARGET |
| `housing_spending_share` | Housing expenditure share | TÜİK HBA | Derived | income, household | NO | TARGET |
| `transport_spending_share` | Transport expenditure share | TÜİK HBA | Derived | income, household | NO | TARGET |
| `restaurant_spending_share` | Restaurant/accommodation expenditure share | TÜİK HBA | Derived | income, household | NO | TARGET |
| `clothing_spending_share` | Clothing expenditure share | TÜİK HBA | Derived | income, household | NO | TARGET |
| `communication_spending_share` | Communication expenditure share | TÜİK HBA | Derived | income, household | NO | TARGET |
| `recreation_spending_share` | Recreation/culture expenditure share | TÜİK HBA | Derived | income, household | NO | TARGET |

> **Constraint:** HBA-derived expenditure behaviour must not be presented as
> province-level estimates unless the relevant source supports that geographic
> resolution.

---

# 5. OVERLAY Variables

OVERLAY variables represent survey-grounded subjective characteristics.

They are **not part of the initial `tr-persona-1` population build** and are
candidates for later schema versions.

| Variable | Description | Source | Processing | MVP | Status |
|---|---|---|---|---|---|
| `life_satisfaction` | Overall life satisfaction | TÜİK YMA | Conditional | NO | OPTIONAL |
| `happiness_level` | Self-reported happiness | TÜİK YMA | Conditional | NO | OPTIONAL |
| `future_hope` | Hope regarding the future | TÜİK YMA | Conditional | NO | OPTIONAL |
| `health_satisfaction` | Satisfaction with health | TÜİK YMA | Conditional | NO | OPTIONAL |
| `education_service_satisfaction` | Satisfaction with education services | TÜİK YMA | Conditional | NO | OPTIONAL |
| `transport_service_satisfaction` | Satisfaction with transport services | TÜİK YMA | Conditional | NO | OPTIONAL |
| `justice_service_satisfaction` | Satisfaction with justice services | TÜİK YMA | Conditional | NO | OPTIONAL |
| `security_service_satisfaction` | Satisfaction with security services | TÜİK YMA | Conditional | NO | OPTIONAL |
| `perceived_main_problem` | Reported important societal/personal problem | TÜİK YMA | Conditional | NO | OPTIONAL |
| `generalized_trust` | Generalised interpersonal trust | WVS Türkiye | Conditional | NO | OPTIONAL |
| `social_tolerance` | Survey-grounded social tolerance indicator | WVS Türkiye | Conditional | NO | OPTIONAL |
| `economic_attitudes` | Survey-grounded economic attitudes | WVS Türkiye | Conditional | NO | OPTIONAL |
| `technology_attitudes` | Survey-grounded technology attitudes | WVS Türkiye | Conditional | NO | OPTIONAL |

> **Constraint:** WVS variables require separate licensing and provenance
> review. Older WVS observations must not be presented as current Türkiye
> estimates without temporal qualification.

---

# 6. CONTEXT Variables

CONTEXT variables describe the environment around a persona rather than the
individual directly.

| Variable | Description | Geography | Source | Processing | MVP | Status |
|---|---|---|---|---|---|---|
| `nuts1_region` | İBBS-1 region | NUTS-1 | TÜİK | Geography mapping | YES | DERIVED |
| `nuts2_region` | İBBS-2 region | NUTS-2 | TÜİK | Geography mapping | YES | DERIVED |
| `district` | District of residence | District | ADNKS / administrative data | Mapping | NO | TARGET |
| `population_size` | Local population | Province / district | ADNKS | Direct | NO | SOURCE_VERIFIED |
| `population_density` | Population density | Province / district | TÜİK | Direct / derived | NO | TARGET |
| `median_age_context` | Local median age | Province | ADNKS | Derived | NO | TARGET |
| `young_population_share` | Share of young population | Province / district | ADNKS | Derived | NO | TARGET |
| `elderly_population_share` | Share of elderly population | Province / district | ADNKS | Derived | NO | TARGET |
| `regional_unemployment` | Regional unemployment | Region | TÜİK | Direct / derived | NO | TARGET |
| `regional_employment_rate` | Regional employment rate | Region | TÜİK | Direct / derived | NO | TARGET |
| `regional_income_context` | Regional income environment | Region | TÜİK | Derived | NO | TARGET |
| `housing_cost_context` | Housing cost environment | Region | TÜİK | Derived | NO | TARGET |
| `education_context` | Education profile of area | Province / region | TÜİK / MEB / YÖK | Aggregate | NO | TARGET |
| `internet_access_context` | Regional digital access | NUTS-1 | TÜİK ICT | Aggregate | NO | TARGET |
| `transport_context` | Local transport environment | Local | Municipal/open data | Aggregate | NO | OPTIONAL |
| `poi_context` | Nearby points of interest | Local | Open geographic data | Spatial | NO | OPTIONAL |
| `commercial_density` | Local business density | Local | Open/local data | Spatial | NO | OPTIONAL |
| `local_service_access` | Accessibility of local services | Local | Municipal/open data | Spatial | NO | OPTIONAL |

---

# 7. Variables Excluded from tr-persona-1

The following attributes must **not** be randomly generated merely to make
personas appear more human:

- personality type
- introversion/extroversion
- impulsiveness
- brand loyalty
- political party preference
- football team preference
- unsupported lifestyle preferences

These attributes may only be introduced in a future schema when a defensible,
survey-grounded generation method and appropriate governance rules exist.

---

# 8. Generation Principle

SocietyTwin must not independently randomise persona attributes.

The intended dependency structure is approximately:

```text
province × sex × age
        ↓
urbanisation
        ↓
marital_status
        ↓
education_level
        ↓
labour_status
        ↓
occupation_group / economic_sector
        ↓
household characteristics
        ↓
income
        ↓
digital behaviour
        ↓
consumption behaviour
        ↓
optional survey-grounded overlays
