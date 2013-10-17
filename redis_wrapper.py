from redis import Redis

redis = Redis()

def set_cardinality(_set):
    return float(redis.zcard(_set))

def get_score(_set,word):
    return redis.zscore(_set,word)

def write_to_redis(clusters):
    #Can do a mass insertion if I update to Redis 2.4 
    for key,values in clusters.items():
        for item in values:
            redis.zadd(key,*item)

def write_centroids(centroids):
    for centroid in centroids:
        redis.lpush("centroid",centroid)


def get_centroids():
    return redis.lrange("centroid",0,-1)

def error_counts(words):
    for word in words:
        if len(word) > 2 :
            redis.zincrby("error_count", str(word), 1)
            #print word

