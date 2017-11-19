import codecs
import nltk
import os
import re
import string 

def format_file(file_name):
    file = codecs.open(file_name, 'r')
    data = []
    hashtags = []
    lines = file.readlines()

    for line in lines:
        tokens = line.split(':')
        tweet = tokens[2]
        if tweet.strip().startswith("RT"):
           continue
        hashtags += re.findall(r"#(\w+)", tweet)
        words = re.sub(r'\W+ | \s+', ' ', tweet)
        #words = re.sub(r'[^\w]', '', words)
        data.append(words)
    for hash in hashtags:
       data.append(hash)
    return data

def get_formatted_file(user_name):
    file_name = 'files/' + user_name + '_formatted.txt'
    notFormatted = False
    if not os.path.exists(file_name):
       notFormatted = True
       file_name = 'files/' + user_name + '.txt'
    file = codecs.open(file_name, 'a', 'utf8')
    lines = []
    if notFormatted:
        lines = format_file(file_name)
        for line in lines:
          file.write(line)
    else:
       lines = file.readlines()
    data = ""
    for line in lines:
       data += line
    return data

def get_most_common_words(user_name, limit):
    data = get_formatted_file(user_name)

    wordDists = nltk.FreqDist(w.lower() for w in data)
    return wordDists.most_common(limit)
