from __future__ import annotations

from pathlib import Path
import json
import math
from collections import Counter

import numpy as np

from src.utils.io import write_json

def loss_to_perplexity(loss: float) -> float:
    return float(math.exp(loss))

def history_to_metrics(history) -> dict:
    losses = [float(x) for x in history.history.get("loss", [])]
    return {
        "loss": losses,
        "perplexity": [loss_to_perplexity(x) for x in losses],
    }

def text_char_distribution(text: str) -> dict[str, float]:
    counts = Counter(text)
    total = sum(counts.values()) or 1
    return {char: count / total for char, count in counts.items()}

def jensen_shannon_divergence(p: dict[str, float], q: dict[str, float]) -> float:
    keys = set(p) | set(q)
    p_vec = np.array([p.get(k, 0.0) for k in keys], dtype=float)
    q_vec = np.array([q.get(k, 0.0) for k in keys], dtype=float)
    m = 0.5 * (p_vec + q_vec)

    def kl(a, b):
        mask = (a > 0) & (b > 0)
        return float(np.sum(a[mask] * np.log2(a[mask] / b[mask])))

    return 0.5 * kl(p_vec, m) + 0.5 * kl(q_vec, m)

def evaluate_generation(source_text: str, generated_text: str) -> dict:
    src_dist = text_char_distribution(source_text)
    gen_dist = text_char_distribution(generated_text)
    return {
        "generated_length": len(generated_text),
        "generated_unique_chars": len(set(generated_text)),
        "source_unique_chars": len(set(source_text)),
        "js_divergence": jensen_shannon_divergence(src_dist, gen_dist),
    }

def save_metrics(metrics: dict, path: str | Path) -> Path:
    return write_json(path, metrics)