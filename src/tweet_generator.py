import nltk
import text_processor as tp
import file_names as fn
from nltk import ngrams
from random import randint

def generate_tweet(starting_word = 'I', size = 10):
    stripped_content = tp.get_stripped_text(fn.HISTORY_FILE)
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+|[^\w\s]+')
    tokens = tokenizer.tokenize(stripped_content)

    content_model = ngrams(tokens, 2)

    cfd = nltk.ConditionalFreqDist(content_model)

    return generate(cfd, starting_word, size)


def read_history_file():
    return


def generate(cfd, word, num):
    output = word + " "
    for i in range(num):
        arr = []  # an array with the words

        for w in cfd[word]:
            #print w, " ",
            arr.append(w)

        random_word = arr[randint(0, len(arr)-1)]
        output += random_word + " "
        word = random_word
        arr = []

    return output + "."
