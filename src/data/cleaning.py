from __future__ import annotations

import re
from pathlib import Path

from src.utils.io import read_text, write_text

RE_PAGES = re.compile(r"Page \d+", re.IGNORECASE)
RE_QUOTES_OPEN = re.compile(r'[\u201c\u201d\x93\x94]')
RE_QUOTES_CLOSE = re.compile(r"[\u2018\u2019\x91\x92]")
RE_NEWLINES = re.compile(r"\n{3,}")
RE_BROKEN_LINES = re.compile(r'([^.!?"])\s*\n+\s*([a-zA-Z0-9])')
RE_DASHES = re.compile(r"[\x96\x97\u2013\u2014]")
RE_SPACES = re.compile(r" {2,}")

def clean_text(content: str) -> str:
    content = content.replace("\r\n", "\n").replace("\r", "\n")
    content = RE_PAGES.sub("", content)
    content = RE_QUOTES_OPEN.sub('"', content)
    content = RE_QUOTES_CLOSE.sub("'", content)
    content = RE_NEWLINES.sub("\n", content)
    content = RE_BROKEN_LINES.sub(r"\1 \2", content)
    content = RE_DASHES.sub("-", content)
    content = RE_SPACES.sub(" ", content)
    content = "\n".join(line.strip() for line in content.splitlines())
    return content.strip()

def combine_books(
    raw_dir: str | Path,
    dest_path: str | Path,
    filenames: list[str],
    encoding_in: str = "latin-1",
    encoding_out: str = "utf-8",
) -> Path:
    raw_dir = Path(raw_dir)
    dest_path = Path(dest_path)
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    missing = [name for name in filenames if not (raw_dir / name).exists()]
    if missing:
        raise FileNotFoundError("Brakuje plików w data/raw/: " + ", ".join(missing))

    combined_parts: list[str] = []
    for name in filenames:
        raw_path = raw_dir / name
        raw_content = read_text(raw_path, encoding=encoding_in)
        combined_parts.append(clean_text(raw_content))

    final_text = "\n\n".join(combined_parts).strip() + "\n"
    write_text(dest_path, final_text, encoding=encoding_out)
    return dest_path
