# Experiment System and Playground (PROPOSED)

> **Status: PROPOSED.** Not implemented. The persona-to-agent activation diagram is in [report §14](societytwin-v2-architecture.md#14-ai-agent-architecture) and the experiment lifecycle diagram in [report §15](societytwin-v2-architecture.md#15-experiment-playground).

The Experiment Playground lets a researcher or student run **reproducible experiments on sampled cohorts** of the synthetic Turkish population. It is inspired by the MatrAIx Playground ([Li et al., 2026](sources.md#reference-systems)), but is much smaller and uses only environments that can be validated in one semester.

## 1. Researcher workflow

| Step | What the user does | System behaviour |
|---|---|---|
| 1 | Choose a population build | Lists builds with schema version, size, seed, and validation status |
| 2 | Filter demographics | Structured filters on record attributes (for example province in NUTS-2 TR51, age 18–29, employed). Filters are data, not free-form SQL. |
| 3 | Choose sample size and sampling method | Simple random or stratified sampling with a seed; shows realised subgroup counts before running |
| 4 | Configure the scenario | Selects an instrument (questionnaire or scenario text) and its version |
| 5 | Choose the experiment type | SURVEY or SCENARIO in the MVP (section 3) |
| 6 | Choose the AI model | Provider-independent model setting; a deterministic stub model is always available for testing |
| 7 | Run | The system validates the configuration, shows a token and cost estimate, and queues the job |
| 8 | Monitor progress | Trial counts by state, errors, cache hits, tokens used |
| 9 | Inspect responses | Browse structured answers and rationales per persona, with the persona card shown alongside |
| 10 | Compare subgroups | Response distributions by subgroup, with weights and uncertainty |
| 11 | Export | CSV or Parquet of trial-level and aggregated results |
| 12 | Reproduce | Re-run from the manifest (replay from cache, or fresh run with a new or same seed) |

## 2. Cohort selection and sampling

- **Filters** are applied to population records with DuckDB queries built from a validated filter specification.
- **Sampling methods (MVP):** simple random sampling without replacement, and stratified sampling (proportional or equal allocation) over chosen attributes. Each uses a recorded seed.
- **Weights.** Every sampled record carries an inclusion weight so that subgroup results can be re-weighted to the population. Equal allocation across strata requires weighting; proportional allocation does not.
- **Realised cohort.** As in MatrAIx, the manifest stores both the *requested* cohort (filters, size, method, seed) and the *realised* cohort (the exact record IDs).

## 3. Environments

| Environment | Description | Validation possible? | Phase |
|---|---|---|---|
| **SURVEY** | Personas answer structured questions (closed-ended options, optional short rationale) | Yes: against published survey aggregates | **MVP** |
| **SCENARIO** | Personas respond to a controlled hypothetical situation with structured response options (for example a change in a public service) | Partly: persona consistency and robustness, not real-world truth | **MVP** |
| CHAT | Personas hold a multi-turn conversation with an AI system under evaluation (MatrAIx "AI Chatbot" type) | Partly: goal completion, persona consistency | STRETCH |
| ABM / SOCIAL INTERACTION | Selected agents interact under explicit rules, or the record population evolves under rule-based dynamics | Yes for rule-based dynamics (historical validation); limited for LLM interaction | STRETCH (rule-based) / FUTURE WORK (LLM interaction) |
| WEB / APP evaluation | Agents operate websites or applications | Requires browser/app sandboxes | FUTURE WORK |

SURVEY and SCENARIO are chosen for the MVP because they are single-trial, parallel, cheap to validate, and map directly to published Turkish survey aggregates.

## 4. Instruments

An **instrument** is a versioned file in `configs/instruments/` (target layout) describing:

- items with an ID, text (in the experiment's interaction language), response options, and an optional rationale field;
- the JSON schema of a valid answer (used for structured outputs);
- metadata: source of the item (for example a published survey question), language, version, and whether real aggregate results exist for validation.

## 5. Agent activation and runtime

- **Activation.** For each trial, a persona card (from [persona-schema.md](persona-schema.md#8-persona-layer-level-2)), the instrument item, and a versioned prompt template are combined into a request. The unknowns statement tells the agent not to invent unmodelled attributes.
- **Model adapter.** A provider-independent interface (`generate_structured(request, schema, params) → result, usage`). Implementations can target hosted APIs or a local model server. Which provider to use is an **OPEN DECISION** (budget, data-protection terms, Turkish-language quality).
- **Structured outputs.** Answers are validated against the item's JSON schema. Invalid outputs are retried a bounded number of times, then recorded as `invalid_output`.
- **Asynchronous execution.** Trials run concurrently in a worker with a configurable concurrency limit, retry with backoff, and rate-limit handling.
- **Cache.** Responses are cached under a key built from the model identifier, prompt template version, persona hash, item, and generation parameters. Replaying an experiment reads from the cache.
- **Budget guard.** Each experiment has a maximum number of calls and tokens. The run stops cleanly when the budget is reached.
- **Stub model.** A deterministic fake model is used in tests and demos, so that the full pipeline runs without any API key.

## 6. Telemetry and result model

**Trial record** (one per persona × item × repetition), following MatrAIx's per-trial record of persona, task, agent, model, and seed:

| Field group | Fields |
|---|---|
| Identity | `experiment_id`, `trial_id`, `build_id`, `record_id`, `item_id`, `repetition` |
| Configuration | environment, instrument ID and version, prompt template version, model provider, name, and version, generation parameters, seed |
| Output | structured answer, optional rationale, validity flag, error |
| Usage | latency, input tokens, output tokens, estimated cost, cache hit |
| Time | created, started, finished |

**Aggregated results** use a long format: `experiment_id`, `item_id`, subgroup keys, response category, weighted share, unweighted count, and interval estimate. Aggregates are stored separately from trial records and are recomputable from them.

The **experiment manifest** records the population build, the requested and realised cohort, the instrument version, the model and adapter version, the prompt template version, the seeds, the budget, and the Git commit ([report §20](societytwin-v2-architecture.md#20-reproducibility)).

## 7. Playground pages (PROPOSED)

| Page | Content |
|---|---|
| Populations | Builds, schema version, size, seed, validation report |
| Cohort builder | Filters, sample size, sampling method, realised subgroup counts |
| Experiment designer | Environment, instrument, model, seeds, budget, cost estimate |
| Run monitor | Progress, errors, tokens, cache hits |
| Results | Subgroup comparison charts, response browser with persona cards |
| Registry | Experiment history, reproduce, export |

Every page that shows persona responses carries the label: *"Synthetic personas and AI-generated responses. Not real people. Not a prediction of real behaviour."*
