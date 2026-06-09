from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
import json
import sys
sys.path.insert(0, "../src") 
from models.model import build_model
from models.generate import generate_text


app = Flask(__name__)

with open('char2idx.json', 'r') as f:
    char2idx = json.load(f)
idx2char = np.array([char for char, idx in sorted(char2idx.items(), key=lambda item: item[1])])

model_trained = tf.keras.models.load_model('model_martin_50_256_512.keras')
model_gen = build_model(vocab_size=len(idx2char), embedding_dim=256, rnn_units=512, batch_size=1)
model_gen.set_weights(model_trained.get_weights())
model_gen.build(tf.TensorShape([1, None]))

@app.route("/generate", methods=["POST"])
def generateText():
    prompt = request.json.get('prompt', 'Ned')
    result = generate_text(model_gen, prompt, char2idx, idx2char, num_generate=300, temperature=0.7)
    return jsonify({'text': result})

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)