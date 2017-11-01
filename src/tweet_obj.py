class tweet_obj:

    id = ""
    text = ""
    user = ""
    timestamp = ""

    def __init__(self, tweet_json):
        self.id = tweet_json.id
        self.text = tweet_json.full_text
        self.user = tweet_json.user.name
        self.timestamp = tweet_json.created_at


    def __str__(self):
        return str(self.id) + " : " + self.user + " : " + self.text + " : " + str(self.timestamp) + "\n"


    def create_tweet_from_str(self, str):
        _tweet = tweet_obj()
        data_set = []
        data_start = 0
        for x in range(len(str)):
            if str[x] == ":":
                data_set.append(str[data_start : x])
                data_start = x + 1

        _tweet.id = data_set[0]
        _tweet.user = data_set[1]
        _tweet.text = data_set[2]
        _tweet.timestamp = data_set[3]



