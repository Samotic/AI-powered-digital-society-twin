# `validation`: comparison with reference and historical data

**Status:** Planned. Not implemented yet.

## Purpose

This module will measure how well the synthetic population and the simulation outputs agree with reference statistics or historical observations.

## Planned responsibilities

- **Population validation:** compare the synthetic population's distributions with the source statistics.
- **Output validation:** compare simulated aggregate indicators with known aggregate or historical data, where such data is available.
- Calculate agreed goodness-of-fit measures and report them together with the model's known limitations.

## Inputs and outputs

- **Input:** the synthetic population, analysis outputs, and reference data from `data/processed/`
- **Output:** validation reports and fit measures

The validation approach is described in [docs/methodology.md](../../docs/methodology.md), and the supporting literature in [docs/sources.md](../../docs/sources.md).
