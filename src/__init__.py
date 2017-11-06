import twitter_connection as tc
import tweet_generator as tg
import sys

def main():
    pull_user_data = False
    pull_news_data = False
    generate_tweet = False

    #process commandline args
    # u - Pull User Data
    # n - Pull News Data
    # t - Generate Tweet
    #
    # python __init__.py u n t
    #
    for arg in sys.argv:
        if arg == 'u':
            pull_user_data = True
        elif arg == 'n':
            pull_news_data = True
        elif arg == 't':
            generate_tweet = True

    if pull_user_data or pull_news_data:
        tc.twitter_connection(pull_user_data, pull_news_data)

    if generate_tweet:
        print "Generated Tweet: ", tg.generate_tweet()



if __name__ == "__main__":
    main()