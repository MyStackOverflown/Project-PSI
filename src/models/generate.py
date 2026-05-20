from __future__ import annotations

from pathlib import Path

import numpy as np
import tensorflow as tf

from src.models.model import build_model

def reset_model_states(model) -> None:
    for layer in model.layers:
        if hasattr(layer, "reset_states"):
            layer.reset_states()

def build_inference_model(vocab_size: int, embedding_dim: int, rnn_units: int, weights_path: str | Path):
    model = build_model(vocab_size=vocab_size, embedding_dim=embedding_dim, rnn_units=rnn_units, batch_size=1)
    model.load_weights(weights_path)
    return model

def generate_text(
    model,
    start_string: str,
    char2idx: dict[str, int],
    idx2char: np.ndarray,
    num_generate: int = 500,
    temperature: float = 1.0,
):
    input_eval = [char2idx[s] for s in start_string]
    input_eval = tf.expand_dims(input_eval, 0)

    text_generated = []
    reset_model_states(model)

    for _ in range(num_generate):
        predictions = model(input_eval)
        predictions = predictions[:, -1, :]
        predictions = predictions / temperature
        predicted_id = tf.random.categorical(predictions, num_samples=1)[0, 0].numpy()
        input_eval = tf.expand_dims([predicted_id], 0)
        text_generated.append(idx2char[predicted_id])

    return start_string + "".join(text_generated)
