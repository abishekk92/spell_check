from twython import TwythonStreamer
from os import getenv as ENV
from utils import *
from redis_wrapper import *
import dictionary
class Streamer(TwythonStreamer):

    def on_success(self, data):
        if 'text' in data:
            tweet = extract_noise(data['text'])
            words = normalize_words(tweet) 
            incorrect = dictionary.check_spelling(words)
            if incorrect is not None:
                error_counts(incorrect)
                for word,dmeta in zip(incorrect,dump_dmeta(incorrect)):
                    score,closest = dictionary.confidence_score(word,dmeta)
                    if score > boost_point:
                        remove_from_incorrect(word)
                        dictionary.add_word(word)
                        add_new(word)
                        print "Number of new words found: %s" % set_cardinality("new")
                    else:
                        add_incorrect(word)
                        print "Number of incorrect words: %s %s" %(set_cardinality("incorrect"),
                                                                   common_mistake()[0])

    def on_error(self,status_code,data):
        print "Error:%s" % status_code



stream = Streamer(ENV("twitter_cons_key"), ENV("twitter_cons_secret"),
        ENV("twitter_auth_token"), ENV("twitter_auth_secret"))

stream.statuses.filter(track='#help',language='en')
