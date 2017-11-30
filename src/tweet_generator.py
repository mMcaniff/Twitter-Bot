import nltk
import text_processor as tp
import random
from nltk import ngrams
from random import randint

numGrams = 3
requirement = 2


def generate_tweet(user_name, starting_word, size):
    # Get content from username's file
    content = tp.get_formatted_file(user_name)

    # Tokenize content
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+|[^\w\s]+')
    tokens = tokenizer.tokenize(content)

    # Get all sequences up to ngram size
    sequences = get_sequences(tokens)

    key = (starting_word, )
    tweet = []

    for i in range(size):
        word = get_next_word(sequences, key)
        key = get_next_key(key, word)
        tweet.append(word)

    print starting_word + ' ' + ' '.join(tweet)\
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

    return random.choice(grams[len(key)+1][key])


def get_next_key(key, res):
    return key + (res, )
