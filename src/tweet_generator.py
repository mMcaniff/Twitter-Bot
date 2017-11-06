import file_names as fn
import text_processor as tp

def generate_tweet():
        print tp.get_most_common_words(fn.HISTORY_FILE, 10)
        return "Tweet Tweet"



def read_history_file():
        return

