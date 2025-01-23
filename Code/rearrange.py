import sys
import random

def random_order(words):
    random.shuffle(words)
    return ' '.join(words)

if __name__ == '__main__':
    input_words = sys.argv[1:]
    print(random_order(input_words))