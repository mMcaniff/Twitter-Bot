import twitter_connection as tc
import tweet_generator as tg
import text_processor as tp
import sys
import codecs

def main():
    pull_user_data = False
    generate_tweet = False
    format_content = False
    starting_word = ""
    user_name = ""
    file_name = ""
    size = 0

    #process commandline args
    # -u - Pull User Data, input username, output file with username.txt
    # -g - Generate Tweet, input optional, word required, size
    # -f - Format an existing repo of Tweets, input username, output formated file 'username_formatted.txt'
    # -word - The starting word
    # -size - Number of words in post
    #

    for arg in sys.argv:
        if arg == '-u':
            pull_user_data = True
            user_name = sys.argv[sys.argv.index("-u") + 1]
        elif arg == '-g':
            generate_tweet = True
            user_name = sys.argv[sys.argv.index("-g") + 1]
        elif arg == '-f':
            format_content = True
            user_name = sys.argv[sys.argv.index("-f") + 1]
            file_name = 'files/' + user_name + '.txt'
        elif arg == '-word':
            starting_word = sys.argv[sys.argv.index("-word") + 1]
        elif arg == '-size':
            size = int(sys.argv[sys.argv.index("-size") + 1])
    
    if format_content:
       data = tp.format_file(file_name)
       file = codecs.open("files/" + user_name + "_formatted.txt", 'a')
       for line in data:
          file.write(line)

    if pull_user_data:
        tc.twitter_connection().connect(user_name)

    if generate_tweet:
        print "Generated Tweet: ", tg.generate_tweet(user_name, starting_word, size)

   

if __name__ == "__main__":
    main()