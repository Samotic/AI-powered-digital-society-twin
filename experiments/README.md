# Experiments

**Status:** Planned. No experiments have been run yet.

## Purpose

This folder will hold reproducible scenario configurations and the outputs of experiment runs.

## Planned layout

| Path | Contents | Tracked in Git? |
|---|---|---|
| `configs/` | One configuration file per scenario: population settings, scenario parameters, simulation length, and random seed. These will be read and checked by the Scenario Manager (`src/scenarios/`). | Yes |
| `outputs/` | Generated results from each run | No (git-ignored) |

These folders will be created when the first experiment is defined.

## Reproducibility

Each experiment should record enough information to be repeated exactly:

- the scenario configuration file;
- the random seed or seeds;
- the Git commit of the code used;
- the version of the dataset used (see [data/README.md](../data/README.md)).

Running the same configuration with the same seed, code version, and dataset should produce the same results.
