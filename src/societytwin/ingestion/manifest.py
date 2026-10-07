"""Utilities for loading and validating the SocietyTwin data manifest."""

from pathlib import Path

import yaml


def load_manifest(path: str | Path) -> dict:
    """Load the SocietyTwin dataset manifest from a YAML file."""

    manifest_path = Path(path)

    if not manifest_path.exists():
        raise FileNotFoundError(
            f"Manifest file not found: {manifest_path}"
        )

    with manifest_path.open("r", encoding="utf-8") as file:
        manifest = yaml.safe_load(file)

    if not isinstance(manifest, dict):
        raise ValueError("Manifest must contain a YAML mapping.")

    datasets = manifest.get("datasets")

    if not isinstance(datasets, list):
        raise ValueError(
            "Manifest must contain a 'datasets' list."
        )

    return manifest
