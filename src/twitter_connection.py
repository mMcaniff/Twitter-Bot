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

    def process_and_store(self, file, tweet):
        _tweet = tweet_obj.tweet_obj(tweet)
        file.write(_tweet.__str__())

    def connect(self, user_name):
        file = codecs.open("files/" + user_name + ".txt", 'a', "utf-8")

        auth = OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_SECRET)

        api = tweepy.API(auth)
        n = 0
        page_list = []
        for page in tweepy.Cursor(api.user_timeline, screen_name=user_name, include_rts=False, count=200).pages(16):
            page_list.append(page)
            n = n+1
            print n
        for page in page_list:
           for tweet in page:
               self.process_and_store(file, tweet)