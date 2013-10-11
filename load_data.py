import dictionary 
from itertools import chain, ifilter
from redis import Redis
from collections import Counter
from sys import argv
from util import *

def write_to_bloomfilter(source_file):
    words = get_words_from_file(source_file)
    words = map(lambda word: word.strip('\r\n').lower(), words)
    dictionary.add_words(words)


def write_to_redis(redis, clusters):
    #Can do a mass insertion if I update to Redis 2.4 
    for key,values in clusters.items():
        for item in values:
            redis.zadd(key,*item)
    print "Added"

redis = Redis()

def create_hashes():
    results = []
    for source_file in FILES:
        write_to_bloomfilter(source_file)
        words = get_words_from_file(source_file)
        words = dump_dmeta(words)
        results.extend(words)
    return results

def find_closest(target,centroids):
    collector = []
    for centroid in centroids:
        ratio = fuzz.ratio(target,centroid)
        collector.append((ratio,target,centroid))
    closest = max(collector, key = lambda _ : _[0])
    return closest

def k_clusters(results):
    count = Counter(results)
    most_common = count.most_common(50)
    centroids = map(lambda a : a[0], most_common)
    clusters = {centroid:[] for centroid in centroids} 
    targets = set(count.keys()).difference(set(centroids))
    for target in targets:
        closest = find_closest(target,centroids)
        ratio, target, cluster = closest
        clusters[cluster].append((target,ratio))
    return clusters


def create_cluster():
    hashes = create_hashes()
    clusters = k_clusters(hashes)
    write_to_redis(redis, clusters)



