from twython import TwythonStreamer
from os import getenv as ENV
from utils import *
import dictionary
class Streamer(TwythonStreamer):

    def on_success(self, data):
        if 'text' in data:
            tweet = extract_noise(data['text'])
            words = normalize_words(tweet) 
            incorrect = dictionary.check_spelling(words)
            if incorrect is not None:
                for word,dmeta in zip(incorrect,dump_dmeta(incorrect)):
                    if is_it_english(word):
                        dictionary.add_words([words])
                    print word,dictionary.confidence_score(dmeta)

    def on_error(self,status_code,data):
        print "Error:%s" % status_code



stream = Streamer(ENV("twitter_cons_key"), ENV("twitter_cons_secret"),
        ENV("twitter_auth_token"), ENV("twitter_auth_secret"))

stream.statuses.filter(track='#help',language='en')
