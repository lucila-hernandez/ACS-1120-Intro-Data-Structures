"""Main script, uses other modules to generate sentences."""
from flask import Flask
from the_blue_castle import histogram
import random

app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.

hist = histogram('the_blue_castle.txt')

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    words = list(hist.keys()) # get unique word from the hist
    if words:
        random_index = random.randint(0, len(words) - 1) # genrate random indez
        random_word = words[random_index] # pick word
        return random_word

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
