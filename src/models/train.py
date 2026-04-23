import os
import tensorflow as tf

from pathlib import Path

def compile_model(model):
    model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True))
    return model

def get_checkpoint_callback(checkpoint_dir):
    checkpoint_dir = Path(checkpoint_dir)
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    checkpoint_prefix = os.path.join(str(checkpoint_dir), "ckpt_{epoch}.weights.h5")
    
    return tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_prefix, save_weights_only=True)