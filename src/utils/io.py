from __future__ import annotations

import json
from pathlib import Path
from typing import Any

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    path = Path(path)
    return path.read_text(encoding=encoding)

def write_text(path: str | Path, text: str, encoding: str = "utf-8") -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding=encoding)
    return path

def read_json(path: str | Path) -> Any:
    path = Path(path)
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def write_json(path: str | Path, data: Any, indent: int = 2) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)
    return path
