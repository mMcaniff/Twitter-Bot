import nltk
import text_processor as tp
import random
from nltk import ngrams
from random import randint

ending_symbols = ['.', '!', "?", "..."]

numGrams = 10
requirement = 1


def generate_tweet(user_name, starting_word, size):
    # Get content from username's file
    content = tp.get_formatted_file(user_name)

    # Tokenize content
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+|[^\w\s]+')
    tokens = tokenizer.tokenize(content)

    # Get all sequences up to ngram size
    forward_sequences = get_sequences(tokens)
    tokens.reverse()
    reverse_sequences = get_sequences(tokens)

    key = tuple(starting_word.split())
    tweet = starting_word.split()

    word = ''

    while word not in ending_symbols:
        word = get_prev_word(reverse_sequences, key)
        if word == None:
            return "I have nothing to say about this"
        #print word
        key = get_prev_key(key, word)
        tweet.insert(0, word)

    tweet.pop(0)
    word = ''
    key = tuple(tweet[-3:])

    while word not in ending_symbols:
        word = get_next_word(forward_sequences, key)
        if word == None:
            return "I have nothing to say about this"
        #print word
        key = get_next_key(key, word)
        tweet.append(word)

    return ' ' + ' '.join(tweet)\
        .replace(' .', '.')\
        .replace(' ,', ',')\
        .replace(" ' ", "'")\
        .replace(' :', ':')\
        .replace('# ', '#')\
        .replace('@ ', "@")\
        .replace(' !', '!')


def get_sequences(tokens):
    grams = {}

    for x in range(2, numGrams + 1):
        dictionary = {}

        for sequence in ngrams(tokens, x):
            key = tuple(sequence[:-1])

            if key in dictionary:
                dictionary[key].append(sequence[x-1])
            else:
                dictionary[key] = [sequence[x-1]]

        grams[x] = dictionary

    return grams


def get_next_word(grams, key):
    for i in range(len(key)):
        if len(key) + 1 in grams and key in grams[len(key)+1]:
            if len(grams[len(key)+1][key]) >= requirement:
                return random.choice(grams[len(key)+1][key])

    # if the length requirement isn't met, shrink the key_id
        if len(key) > 1:
            key = key[1:]
    if key in grams[len(key)+1]:
        return random.choice(grams[len(key)+1][key])
    return

def get_prev_word(grams, key):
    for i in range(len(key)):
        if len(key) + 1 in grams and key in grams[len(key)+1]:
            if len(grams[len(key)+1][key]) >= requirement:
                return random.choice(grams[len(key)+1][key])

    # if the length requirement isn't met, shrink the key_id
        if len(key) > 1:
            key = key[:-1]

    if key in grams[len(key)+1]:
        return random.choice(grams[len(key)+1][key])
    return


def get_next_key(key, res):
    return key + (res, )

def get_prev_key(key, res):
    return (res, ) + key