# http://docs.tweepy.org/en/v3.5.0/streaming_how_to.html

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from time import sleep
import json

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""


class MyStreamListener(StreamListener):
    def on_status(self, status):
        print(status.text)

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status_code):
        print(status_code)
        if status_code == 420:
            # too many requests
            sleep(61)
            return False


def get_secret():
    with open('secret.json') as f:
        data = json.load(f)
        print(data)


if __name__ == "__main__":
    get_secret()
    myListener = MyStreamListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    myStream = Stream(auth=auth, listener=myListener)

    # track = keywords; follow = user ID; locations
    myStream.filter(languages=["nl"])

