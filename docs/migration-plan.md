# Repository Migration Plan (v1 → v2)

> **Status: PROPOSED.** Migration is done in two separate steps so that nothing is broken or lost.

## Step 1: documentation migration (this branch)

Done on branch `docs/societytwin-v2-architecture`:

- New v2 documents: [v2 architecture report](societytwin-v2-architecture.md), [persona schema](persona-schema.md), [data strategy](data-strategy.md), [validation strategy](validation-strategy.md), [experiment system](experiment-system.md), [ethics and limitations](ethics-and-limitations.md), this plan.
- Rewritten for v2: README, project overview, architecture reference, methodology, sources, data README.
- Updated: research integration, team responsibilities, placeholder READMEs, `.gitignore`, `requirements.txt`.
- **Superseded, kept for history:** the v1.0 architecture is archived in [archive/architecture-v1-demographic.md](archive/architecture-v1-demographic.md). Earlier documents remain in Git history and on the branch `docs/align-latest-architecture`, which is **not** modified.
- **No source code, placeholder folders, or data were moved or deleted.**

## Step 2: implementation migration (later, separate change)

Carried out when implementation starts, after the v2 architecture is approved. The placeholder folders contain only README files and empty `__init__.py` files, so no code needs to be rewritten.

| Current placeholder | v2 target | Notes |
|---|---|---|
| `src/data_processing/` | `src/societytwin/ingestion/` | Renamed to avoid confusion with the top-level `data/` folder |
| `src/population/` | `src/societytwin/population/` | Now contains the dependency model and generator |
| — | `src/societytwin/persona/` | New: schema definitions and persona rendering |
| — | `src/societytwin/sampling/` | New: cohort selection |
| `src/scenarios/` | `src/societytwin/scenarios/` | Now holds instruments and scenario conditions |
| — | `src/societytwin/experiments/` | New: experiment manager and environments |
| `src/agents/` | `src/societytwin/agents/` | **Meaning changes:** from rule-based simulation agents to LLM agent activation |
| `src/simulation/` | `src/societytwin/simulation/` | Optional population dynamics and Cohort-Component benchmark (STRETCH) |
| `src/validation/` | `src/societytwin/evaluation/` | Validation metrics and reports |
| `src/analysis/` | `src/societytwin/evaluation/` | Subgroup analysis merged with evaluation |
| — | `src/societytwin/registry/` | New: manifests, jobs, provenance |
| — | `src/societytwin/api/` | New: FastAPI application |
| `experiments/` | `configs/` (instruments, experiment presets) and `data/results/` (outputs, git-ignored) | The top-level `experiments/` folder is removed once empty |
| `tests/` | `tests/` (unit, property, integration) and frontend tests | Small artificial fixtures in `tests/fixtures/` |
| — | `frontend/`, `configs/`, `.github/workflows/`, `docker-compose.yml`, `pyproject.toml` | New |

**Procedure.** Use `git mv` so that history is kept; move one module per commit; update imports and README links in the same commit; run the test suite after each move.

## Requirements superseded by v2

| v1 requirement | v2 status |
|---|---|
| Exactly 5,000 synthetic agents (FR-02, TC-01) | Superseded: builds of configurable size; 10K / 100K / 1M are benchmark scales (1M PROPOSED as the largest MVP benchmark); final target size OPEN DECISION |
| 5,000 agents × 10 years within 60 s (NFR-02, TC-10) | Superseded: separate generation, storage, simulation, and AI-activation targets set after benchmarks (OPEN DECISION) |
| Seven-field demographic agent schema | Superseded by persona schema `tr-persona-1` |
| ABM + Cohort-Component / Matrix Projection + ML comparison as the core | Moved to supporting, optional, or future roles ([report §17](societytwin-v2-architecture.md#17-abm--cohort--ml-integration-decision)) |
| LLMs excluded from the core | Superseded: bounded AI-agent activation for sampled cohorts |
| Mesa as the main engine | Superseded: vectorised columnar generation; Mesa optional |
| Unknown instructor-provided dataset (research-phase documents) | Superseded: TÜİK official statistics |
