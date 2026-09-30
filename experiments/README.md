# Experiments (placeholder)

**Status:** Placeholder from the research phase. No experiments have been run.

In the PROPOSED v2 architecture, experiments are configured in the Playground and recorded in the experiment registry ([experiment-system.md](../docs/experiment-system.md)):

- **Instruments and experiment presets** (versioned, tracked in Git) move to `configs/`.
- **Trial records, raw responses, and aggregates** (generated, git-ignored) are written to `data/results/`.

This folder will be removed once its role has moved ([migration plan](../docs/migration-plan.md)). Generated outputs in `experiments/outputs/` and `experiments/results/` are git-ignored.
