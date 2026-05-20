import os
import sys

from pathlib import Path

PROJECT_ROOT = Path("/content/drive/MyDrive/Project-PSI")
os.chdir("/content/drive/MyDrive/Project-PSI")
sys.path.insert(0, str(PROJECT_ROOT))

from src.utils.paths import ensure_project_dirs

ensure_project_dirs()