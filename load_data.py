import dictionary 
from sys import argv
from utils import *
from redis_wrapper import *

def write_to_bloomfilter(source_file):
    words = get_words_from_file(source_file)
    words = map(lambda word: word.strip('\r\n').lower(), words)
    dictionary.add_words(words)


def create_hashes():
    results = []
    for source_file in FILES:
        write_to_bloomfilter(source_file)
        words = get_words_from_file(source_file)
        words = dump_dmeta(words)
        results.extend(words)
    return results


def k_clusters(results):
    centroids = compute_centroids(results)
    write_centroids(centroids)
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
    write_to_redis(clusters)

create_cluster()

