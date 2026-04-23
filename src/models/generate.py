import tensorflow as tf

def reset_model_states(model):
    for layer in model.layers:
        if hasattr(layer, "reset_states"):
            layer.reset_states()

def generate_text(model, start_string, char2idx, idx2char, num_generate=500, temperature=1.0):
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

    return start_string + ''.join(text_generated)