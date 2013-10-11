import re
from fuzzy import DMetaphone 
from fuzzywuzzy.fuzz import ratio as _ratio

FILES = ['british/brit-a-z.txt', 'british/britcaps.txt']

def normalize_words(sentence):
    words = re.findall(r'[a-z]+', sentence, re.IGNORECASE)
    return map(lambda word: word.lower(),words)


def get_words_from_file(source_file):
    return open(source_file,'r').readlines()

def ratio(_str1,_str2):
    return _ratio(_str1,_str2)

def dump_dmeta(words):
    dmeta = DMetaphone()
    return filter(lambda word: word is not None,
            chain(*(map(dmeta, words))))


