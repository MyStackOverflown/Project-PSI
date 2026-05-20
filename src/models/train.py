from __future__ import annotations

import os
from pathlib import Path

import tensorflow as tf

from src.utils.io import read_text, write_json, read_json

def compile_model(model):
    model.compile(
        optimizer="adam",
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    )
    return model

def get_checkpoint_callback(checkpoint_dir: str | Path):
    checkpoint_dir = Path(checkpoint_dir)
    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    checkpoint_prefix = os.path.join(str(checkpoint_dir), "ckpt_{epoch}.weights.h5")
    return tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_prefix, save_weights_only=True)

def train_model(model, dataset, checkpoint_callback, epochs: int = 1):
    history = model.fit(dataset, epochs=epochs, callbacks=[checkpoint_callback])
    return history

def save_final_model(model, path: str | Path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    model.save(path)
    return path

def save_history(history, path: str | Path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    write_json(path / "history.json", history.history)
    return path
