# `data_processing`: dataset loading and cleaning

**Status:** Planned. Not implemented yet.

## Purpose

This module will turn the instructor-provided dataset in `data/raw/` into clean, consistently structured tables in `data/processed/` that the synthetic population generator can use.

## Planned responsibilities

- Load the original files without modifying them.
- Check the data for missing values, inconsistent categories, and totals that do not add up.
- Harmonize category labels and units.
- Record every transformation so that the processed data can be regenerated from the raw data.

## Inputs and outputs

- **Input:** original dataset files in `data/raw/`
- **Output:** cleaned aggregate tables in `data/processed/`

The exact steps will be defined after the dataset has been received and reviewed.
