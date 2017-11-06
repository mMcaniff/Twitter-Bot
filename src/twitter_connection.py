import tweepy
import tweet_obj
import codecs
import file_names as fn
from tweepy import OAuthHandler

class twitter_connection:
    CONSUMER_KEY = 'WzUgBEHTGwKKAF1loDaMYDSQH'
    CONSUMER_SECRET = 'FIYKkE9EPGBOG1scnu03K9pCmi2D6he1cm8zw8cvSaDMQlLZbi'
    ACCESS_TOKEN = '925067496473870343-0uOCFGL9zWURefYVl3HyA6Skie51yUa'
    ACCESS_SECRET = '8z4s87KJlGKbls7v8LqBQEyP9Xot4W86HSppP1dpOnu6c'

    def __init__(self, pull_user_data, pull_news_data):
        history_file = codecs.open(fn.TEMP_FILE, 'a', "utf-8")
        news_file = codecs.open(fn.NEWS_FILE, 'a', 'utf-8')

        auth = OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_SECRET)

        api = tweepy.API(auth)
        public_tweets = tweepy.Cursor(api.home_timeline, tweet_mode='extended').items()
        for tweet in public_tweets:
            if tweet.user.name == "Barack Obama":
                self.process_and_store(history_file, tweet)
            else:
                self.process_and_store(news_file, tweet)


    def process_and_store(self, file, tweet):
        _tweet = tweet_obj.tweet_obj(tweet)
        file.write(_tweet.__str__())