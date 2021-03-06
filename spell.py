from twython import TwythonStreamer
from ConfigParser import ConfigParser
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
                        publish_count("new")
                    else:
                        add_incorrect(word)
                        publish_count("incorrect")
                        publish_mistake()
    def on_error(self,status_code,data):
        pass


config = ConfigParser()
config.read("./conf/app.config")
config = dict(config.items(config.sections()[0]))
stream = Streamer(config["twitter_cons_key"], config["twitter_cons_secret"],
        config["twitter_auth_token"], config["twitter_auth_secret"])

stream.statuses.filter(track='#help',language='en')
