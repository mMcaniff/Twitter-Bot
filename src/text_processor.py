import codecs
import nltk
import os
import re
import string 
import spacy

def format_file(file_name):
    print "Formatting data and dumping: " + file_name
    file = codecs.open(file_name, 'r')
    data = []
    mentions = [] # stores all mentions but doesn't do anything with
    hashtags = [] # stores all hashtags but doesn't do anything with
    lines = file.readlines()

    for line in lines:
        tokens = line.split(' &&& ')
        if len(tokens) > 1:
            tweet = tokens[1]
        else:
           tweet = tokens[0]
        if tweet.strip().startswith("RT"):
           continue
        stripped_words = ''
        words = tweet.split(' ')
        for word in words:
            if '&amp;' in word:
               word = word.replace('&amp;', '&')
            if not 'http' in word:
               stripped_words += word + ' '
            elif '\n' in word:
               stripped_words += '\n'
        mentions += re.findall(r'@(\w+ | \d+)', tweet)
        hashtags += re.findall(r"#(\w+)", tweet)
        data.append(stripped_words)
    print "Finished Formatting data: " + file_name
    return data

def get_first_line(user_name):
    file_name = 'files/' + user_name + '_formatted.txt'
    file = codecs.open(file_name, 'r')
    return file.readlines()[0]

def get_formatted_file(user_name):
    file_name = 'files/' + user_name + '_formatted.txt'
    file = codecs.open(file_name, 'r')
    notFormatted = False
    if not os.path.exists(file_name):
        notFormatted = True
        file_name = 'files/' + user_name + '.txt'
        file = codecs.open(file_name, 'w')
    lines = []
    if notFormatted:
        print (file_name)
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

def find_possible_subject(text):
   subject = None
   direct_object = None
   nlp = spacy.load('en')
   parsed_text=nlp(unicode(text.decode('unicode_escape').encode('ascii','ignore')))
   #get token dependencies
   for text in parsed_text:
       #subject would be
       if text.dep_ == "nsubj":
           subject = text.orth_
       #dobj for direct object
       if text.dep_ == "dobj":
           direct_object = text.orth_
   list = []
   for nc in parsed_text.noun_chunks:
      list.append(str(nc.text))
   list.append(subject)
   list.append(direct_object)
   return list
