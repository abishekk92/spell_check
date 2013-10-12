import re
from fuzzy import DMetaphone 
from fuzzywuzzy.fuzz import ratio 
from itertools import chain 
from collections import Counter

FILES = ['british/brit-a-z.txt', 'british/britcaps.txt']

def normalize_words(sentence):
    words = re.findall(r'[a-z]+', sentence, re.IGNORECASE)
    return map(lambda word: word.lower(),words)

def user(word):
    return word.startswith("@")

def hashtag(word):
    return word.startswith("#")

def url(word):
    return word.startswith("http://") or word.startswith("https://")

def rt(word):
    return word.lower() == "rt"

def noise(word):
    word = str(word)
    return url(word) or hashtag(word) or \
           user(word) or rt(word) 

def extract_noise(tweet):
    words = tweet.split() 
    return " ".join(filter(lambda word : not noise(word), 
                           words))

def get_words_from_file(source_file):
    return open(source_file,'r').readlines()

def _ratio(_str1,_str2):
    return ratio(_str1,_str2)

def compute_centroids(results):
    count = Counter(results)
    return map(lambda a : a[0], count.most_common(50))

def find_closest(target,centroids):
    collector = []
    for centroid in centroids:
        __ratio = ratio(target,centroid)
        collector.append((__ratio,target,centroid))
    closest = max(collector, key = lambda _ : _[0])
    return closest

def dump_dmeta(words):
    dmeta = DMetaphone()
    return filter(lambda word: word is not None,
            chain(*(map(dmeta, words))))


