# Data

**No dataset, generated population, or experiment result is included in this repository.**

SocietyTwin v2 uses **official aggregate statistics for Türkiye**, primarily from **TÜİK** (Turkish Statistical Institute). Sources, geographic levels, access, and licence status are described in [docs/data-strategy.md](../docs/data-strategy.md); the attributes generated from them are described in [docs/persona-schema.md](../docs/persona-schema.md). No dataset has been downloaded or approved yet.

## Folders

| Path | Purpose | In Git? |
|---|---|---|
| `raw/` | Original downloads, exactly as published. Never edited by hand. | No (git-ignored) |
| `processed/` | Harmonised constraint tables produced by code for the generator. | No (git-ignored) |
| `populations/` | Generated population builds (Parquet, partitioned). Created when implementation starts. | No (git-ignored) |
| `results/` | Experiment trial records, raw responses, and aggregates. Created when implementation starts. | No (git-ignored) |
| `manifest.yaml` | Metadata for every downloaded dataset: source, URL, reference year, scope, variables, licence, download date, checksum. | **Yes** |

## Rules

- **Never commit data or generated outputs.** `.gitignore` excludes everything in the folders above except placeholder and README files, plus common data formats anywhere under `data/`.
- **Commit metadata, not data.** Record every dataset in [`manifest.yaml`](manifest.yaml).
- **Aggregate data only.** No personal or identifiable data may be added. TÜİK microdata, if ever approved, is used only under TÜİK's access rules and is never copied into this repository.
- **Respect licences.** Record each dataset's licence; reuse terms that are not yet confirmed are an OPEN DECISION.
- **Keep raw data unchanged.** All cleaning and harmonisation is done in code, so processed data can be regenerated.
- **Test fixtures** must be small and clearly artificial, and live in `tests/fixtures/`, not in `data/`.
- Git history keeps deleted files: anything committed must be treated as published.
