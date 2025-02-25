from collections import defaultdict
import random

def learn_markov_chain(corpus):
    """Learns a Markov chain from the given corpus."""
    markov_chain = defaultdict(list)
    with open(corpus, 'r', encoding='utf-8') as file:
        text = file.read().split()
    for i in range(len(text) - 1):
        markov_chain[text[i]].append(text[i + 1])
    return markov_chain

def random_walk(markov_chain, start_token, steps=10):
    """Generates text by performing a random walk on the Markov chain."""
    current_token = start_token
    output = [current_token]
    for _ in range(steps):
        next_tokens = markov_chain.get(current_token, [])
        if not next_tokens:  # If there are no outgoing transitions
            break
        current_token = random.choice(next_tokens)
        output.append(current_token)
    return ' '.join(output)