import twitter_connection as tc
import tweet_generator as tg
import text_processor as tp
import sys
import codecs

def main():
    pull_user_data = False
    generate_tweet = False
    format_content = False
    starting_word = "health care"
    user_name = ""
    news_name = ""
    file_name = ""
    size = 25

    # process commandline args
    # -p - Pull User Data, input username, output file with username.txt
    # -g - Generate Tweet, input optional, word required, size
    # -f - Format an existing repo of Tweets, input username, output formated file 'username_formatted.txt'
    # -word - The starting word
    # -size - Number of words in post
    #
    for arg in sys.argv:
        if arg == '-p':
            pull_user_data = True
            user_name = sys.argv[sys.argv.index("-u") + 1]
        elif arg == '-n':
            pull_user_data = True
            news_name = sys.argv[sys.argv.index("-n") + 1]
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
    

    if pull_user_data:
       if news_name != "":
          tc.twitter_connection().connect(news_name)
          file_name = 'files/' + news_name + '.txt'
          data = tp.format_file(file_name)
          _file = codecs.open("files/" + news_name + "_formatted.txt", 'a')
          for line in data:
             _file.write(line)
       if user_name != "":
          tc.twitter_connection().connect(user_name)
          file_name = 'files/' + user_name + '.txt'
          data = tp.format_file(file_name)
          _file = codecs.open("files/" + user_name + "_formatted.txt", 'a')
          for line in data:
             _file.write(line)
    
    if format_content:
        data = tp.format_file(file_name)
        _file = codecs.open("files/" + user_name + "_formatted.txt", 'a')
        for line in data:
            _file.write(line)

    if generate_tweet:
       if (news_name != ""):
         content = tp.get_first_line(news_name)
         list = tp.find_possible_subject(content)
         for i in range(len(list)):
            for j in range(i + 1, len(list)):
               print "Generated Tweet for " + list[i] + " " + list[j] + ": ", tg.generate_tweet(user_name, list[i] + " " + list[j], size)
         for noun in list:
            print "Generated Tweet for " + noun + ": ", tg.generate_tweet(user_name, noun, size)
       else:
          print "Generated Tweet for " + noun + ": ", tg.generate_tweet(user_name, starting_word, size)

       


if __name__ == "__main__":
    main()