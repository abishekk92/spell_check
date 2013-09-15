from pyreBloom import pyreBloom as bloom_filter

dictionary = bloom_filter('dictionary',10000000,0.01)


def add_words(words):
    dictionary.extend(words)

def check_spelling(words):
    correct = set(dictionary.contains(words))
    incorrect = set(words).difference(correct)
    if len(incorrect) is 0:
        return None
    else:
        return incorrect
