import tweepy
import tweet_obj
import codecs
from tweepy import OAuthHandler

class twitter_connection:

    def __init__(self):
        tweet_file = codecs.open("history.txt", 'a', "utf-8")

        consumer_key = 'WzUgBEHTGwKKAF1loDaMYDSQH'
        consumer_secret = 'FIYKkE9EPGBOG1scnu03K9pCmi2D6he1cm8zw8cvSaDMQlLZbi'
        access_token = '925067496473870343-0uOCFGL9zWURefYVl3HyA6Skie51yUa'
        access_secret = '8z4s87KJlGKbls7v8LqBQEyP9Xot4W86HSppP1dpOnu6c'

        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)

        api = tweepy.API(auth)

        #public_tweets = tweepy.Cursor(api.home_timeline, tweet_mode='extended').items()
        #for tweet in public_tweets:
            #self.process_and_store(tweet_file, tweet)
        tweet_file.write("A line")


    def process_and_store(self, file, tweet):
        _tweet = tweet_obj.tweet_obj(tweet)
        print(_tweet.__str__())
        file.write(_tweet.__str__())
