import numpy as np
import tensorflow as tf

from pathlib import Path

def load_text(path: str | Path, encoding: str = "utf-8") -> str:
    path = Path(path)
    return path.read_text(encoding=encoding)

def build_vocab(text: str) -> list[str]:
    return sorted(set(text))

def build_char_mappings(vocab: list[str]) -> tuple[dict[str, int], np.ndarray]:
    char2idx = {char: idx for idx, char in enumerate(vocab)}
    idx2char = np.array(vocab)
    return char2idx, idx2char

def encode_text(text: str, char2idx: dict[str, int]) -> np.ndarray:
    return np.array([char2idx[c] for c in text], dtype=np.int32)

def split_input_target(chunk: tf.Tensor) -> tuple[tf.Tensor, tf.Tensor]:
    input_text = chunk[:-1]
    target_text = chunk[1:]
    return input_text, target_text

def make_dataset(text_as_int: np.ndarray, seq_length: int = 100, batch_size: int = 64,buffer_size: int = 10000) -> tf.data.Dataset:
    char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)
    sequences = char_dataset.batch(seq_length + 1, drop_remainder=True)

    dataset = sequences.map(split_input_target)
    dataset = dataset.shuffle(buffer_size).batch(batch_size, drop_remainder=True)
    return dataset

def prepare_char_dataset(text_path: str | Path, seq_length: int = 100, batch_size: int = 64, buffer_size: int = 10000) -> tuple[str, list[str], dict[str, int], np.ndarray, np.ndarray, tf.data.Dataset]:
    text = load_text(text_path)
    vocab = build_vocab(text)
    char2idx, idx2char = build_char_mappings(vocab)

    text_as_int = encode_text(text, char2idx)
    dataset = make_dataset(text_as_int, seq_length=seq_length, batch_size=batch_size, buffer_size=buffer_size)
    return text, vocab, char2idx, idx2char, text_as_int, dataset