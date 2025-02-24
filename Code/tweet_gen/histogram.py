from collections import Counter

def histogram(source_text):
    """Takes text or filename, removes punctuation, and returns a word count dictionary."""
    with open('../data/corpus.txt', 'r', encoding='utf-8') as file:
        source_text = file.read()

    # Step 1: Convert text to lowercase
    source_text = source_text.lower()

    # Step 2: Remove punctuation (replace non-letters/numbers with spaces)
    cleaned_text = ""
    for letter in source_text:
        if letter.isalnum() or letter.isspace():
            cleaned_text += letter
        else:
            cleaned_text += " "

    # Step 3: Split into words
    words = cleaned_text.split()

    # Step 4: Count word frequencies
    return Counter(words)

def unique_words(histogram):
    """Returns the number of unique words in the histogram."""
    return len(histogram)

def frequency(word, histogram):
    """Returns how many times the word appears in the text."""
    return histogram.get(word.lower(), 0)

if __name__ == '__main__':
    hist = histogram('../data/corpus.txt')  

    print("Unique words:", unique_words(hist))
    print("Frequency of 'castle':", frequency('castle', hist))
