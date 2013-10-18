from pyreBloom import pyreBloom as bloom_filter
from utils import *
from redis_wrapper import *
dictionary = bloom_filter('dictionary',10000000,0.01)


def add_words(words):
    dictionary.extend(words)

def add_word(word):
    dictionary.extend(word)

def check_spelling(words):
    correct = set(dictionary.contains(words))
    incorrect = set(words).difference(correct)
    if len(incorrect) is 0:
        return None
    else:
        return filter(lambda a : len(a)>2,incorrect)

def confidence_score(word,dmeta):
    score = get_score("error_count",word)/set_cardinality("error_count")
    closest = find_closest(dmeta, get_centroids())
    return score*closest[0],closest[0]
 
