"""Main script, uses other modules to generate sentences."""
from flask import Flask
from histogram import histogram
from listogram import Listogram
from dictogram import Dictogram
import random

app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.

hist = histogram("data/corpus.txt")

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    words = list(hist.keys()) # get unique word from the hist
    num_words_to_generate = 5

    random_words = []
    if words:
        for _ in range(num_words_to_generate):
            random_index = random.randint(0, len(words) - 1)  # Generate random index
            random_word = words[random_index]  # Pick word
            random_words.append(random_word)  # Add to the list of random words

    return " " + " ".join(random_words)  # Return the words separated by spaces

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
