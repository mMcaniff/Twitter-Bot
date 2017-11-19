import nltk
import text_processor as tp
import file_names as fn
from nltk import ngrams
from random import randint
import codecs

def generate_tweet(user_name, starting_word = 'I', size = 10):
   
    file = codecs.open("files/" + user_name + ".txt", 'r', 'utf8')
    lines = file.readlines()
    content = tp.get_formatted_file(user_name)
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+|[^\w\s]+')
    tokens = tokenizer.tokenize(content)

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
