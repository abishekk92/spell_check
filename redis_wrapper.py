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
        redis.zincrby("error_count", str(word), 1)

def add_incorrect(word):
    redis.zincrby("incorrect", str(word), 1)

def add_new(word):
    redis.zadd("new", str(word),0)

def remove_from_incorrect(word):
    redis.zrem("incorrect", word)

def common_mistake():
    return redis.zrange("incorrect",-1,-1)

def publish_count(_set):
    count = set_cardinality(_set)
    channel = "%s_count" % _set
    redis.publish(channel,count)

def publish_mistake():
    mistake  = common_mistake()[0]
    redis.publish("common_mistake",mistake)
