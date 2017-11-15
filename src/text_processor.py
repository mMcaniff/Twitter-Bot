import codecs
import nltk

def get_stripped_text(file_name):
    file = codecs.open(file_name, 'r', 'utf8')
    data = ""
    lines = file.readlines()

    for line in lines:
        tokens = line.split(':')
        if len(tokens) > 2:
            tweet = tokens[2].replace('https', '')
            data += tweet

    return data


def get_most_common_words(file_name, limit):
    data = get_stripped_text(file_name)

    wordDists = nltk.FreqDist(w.lower() for w in data)
    return wordDists.most_common(limit)
