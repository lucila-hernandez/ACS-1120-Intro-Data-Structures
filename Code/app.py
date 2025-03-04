"""Main script, uses other modules to generate sentences."""
from flask import Flask
from markov import build_markov_chain, generate_sentence

app = Flask(__name__)

# Step 1: Initialize the Markov chain when the server starts
markov_chain = build_markov_chain("data/corpus.txt")

@app.route("/")
def home():
    """Generate a sentence using the Markov chain."""
    num_words_to_generate = 10 
    return generate_sentence(markov_chain, num_words_to_generate)

if __name__ == "__main__":
    app.run(debug=True)
