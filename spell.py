from twython import TwythonStreamer
from os import getenv as ENV
import utils

class Streamer(TwythonStreamer):

    def on_success(self, data):
        if 'text' in data:
            tweet = data['text']
            words = utils.normalize_words(tweet) 
            incorrect = dictionary.check_spelling(words)
            ##TODO: Use soundex indexes to figure out if a new word is likely to be English
            if incorrect is not None:
                for word in incorrect:
                    if is_it_english(word):
                        dictionary.add_words([words])

    def on_error(self,status_code,data):
        print status_code



stream = Streamer(ENV("twitter_cons_key"), ENV("twitter_cons_secret"),
                  ENV("twitter_auth_token"), ENV("twitter_auth_secret"))

stream.statuses.filter(track='#help',language='en')
