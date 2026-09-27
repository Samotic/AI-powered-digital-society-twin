# Data

This folder will hold the data used by SocietyTwin. **No dataset is included in this repository.** The course instructor will provide the dataset at a later stage.

The actual population schema will depend on the variables available in the instructor-provided dataset. No variables are assumed until the dataset has been received and reviewed.

## Folders

| Folder | Purpose |
|---|---|
| `raw/` | Original data exactly as provided by the instructor. Files here are never edited by hand. |
| `processed/` | Cleaned and transformed data produced by the data-processing step, ready for synthetic population generation. |

Both folders contain a `.gitkeep` file only, so that the empty folders are visible on GitHub.

## Data handling rules

- **Do not commit datasets.** `.gitignore` excludes all files in `raw/` and `processed/` (except `.gitkeep` and README files), plus common data formats such as `.csv`, `.xlsx`, `.xls`, `.json` and `.parquet` anywhere under `data/`.
- **Sensitive, private, or restricted data must never be committed to GitHub**, even temporarily. Git history keeps deleted files, so a file that has been committed must be treated as published.
- **Only appropriately anonymized or explicitly permitted data may be version-controlled.** If the instructor confirms that a small file may be shared, add it deliberately with `git add -f` and note the permission below.
- **Keep raw data unchanged.** All cleaning and transformation should be done by code in `src/data_processing/`, so that `processed/` can be regenerated from `raw/`.
- **Share data outside Git.** Team members should obtain the dataset through the channel the instructor specifies, not through this repository.

## Dataset record

Complete this section when the dataset arrives. Record information about the data, not the data itself.

| Field | Value |
|---|---|
| Dataset name | *To be added* |
| Provided by | *To be added* |
| Date received | *To be added* |
| Format and files | *To be added* |
| Level of aggregation | *To be added* |
| Variables included | *To be added* |
| Permitted use and sharing terms | *To be added* |
