import twitter_connection as tc
import tweet_generator as tg
import sys

def main():
    pull_user_data = False
    pull_news_data = False
    generate_tweet = False
    starting_word = ""
    size = 0

    #process commandline args
    # u - Pull User Data
    # n - Pull News Data
    # g - Generate Tweet
    # -word - The starting word
    # -size - Number of words in post
    #
    # python __init__.py u n t -word The -size 15
    #
    for arg in sys.argv:
        if arg == 'u':
            pull_user_data = True
        elif arg == 'n':
            pull_news_data = True
        elif arg == 'g':
            generate_tweet = True
        elif arg == '-word':
            starting_word = sys.argv[sys.argv.index("-word") + 1]
        elif arg == '-size':
            size = int(sys.argv[sys.argv.index("-size") + 1])

    if pull_user_data or pull_news_data:
        tc.twitter_connection()

    if generate_tweet:
        print "Generated Tweet: ", tg.generate_tweet(starting_word, size)



if __name__ == "__main__":
    main()