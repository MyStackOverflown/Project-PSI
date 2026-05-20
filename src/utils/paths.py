from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODELS_DIR = PROJECT_ROOT / "models"
CHECKPOINTS_DIR = MODELS_DIR / "checkpoints"
FINAL_MODELS_DIR = MODELS_DIR / "final"

OUTPUTS_DIR = PROJECT_ROOT / "outputs"
METRICS_DIR = OUTPUTS_DIR / "metrics"
SAMPLES_DIR = OUTPUTS_DIR / "samples"

NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"


def ensure_project_dirs() -> None:
    for path in [
        RAW_DATA_DIR,
        PROCESSED_DATA_DIR,
        CHECKPOINTS_DIR,
        FINAL_MODELS_DIR,
        METRICS_DIR,
        SAMPLES_DIR,
    ]:
        path.mkdir(parents=True, exist_ok=True)
