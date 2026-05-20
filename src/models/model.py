from __future__ import annotations

import tensorflow as tf

def build_model(vocab_size: int, embedding_dim: int, rnn_units: int, batch_size: int | None):
    inputs = tf.keras.Input(batch_shape=[batch_size, None] if batch_size is not None else [None, None])
    x = tf.keras.layers.Embedding(vocab_size, embedding_dim)(inputs)
    x = tf.keras.layers.LSTM(
        rnn_units,
        return_sequences=True,
        stateful=batch_size is not None,
        recurrent_initializer="glorot_uniform",
    )(x)
    outputs = tf.keras.layers.Dense(vocab_size)(x)
    return tf.keras.Model(inputs=inputs, outputs=outputs)
