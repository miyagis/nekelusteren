# http://docs.tweepy.org/en/v3.5.0/streaming_how_to.html

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from time import sleep, time
import json
from _datetime import datetime
from db import create_connection, get_data, tupple_in_list_to_string


class MyStreamListener(StreamListener):

    def on_data(self, data):
        try:
            all_data = json.loads(data)
            t_date = all_data['created_at']
            t_date = datetime.strptime(t_date, "%a %b %d %H:%M:%S %z %Y")  # change to datetime format
            t_id = all_data['id']
            t_followers = all_data['user']['followers_count']
            if 'extended_tweet' in all_data:
                t_text = all_data['extended_tweet']['full_text']
            else:
                t_text = all_data['text']
            t_text = t_text.replace("'", "")  # Gives an error when writing to the db
            t_text = t_text.replace(";", "")  # Is used as delimiter
            t_text = t_text.encode("utf-8")  # Should get rid of unknown characters
            t_user = all_data["user"]['id']

            # hashtags = all_data['entities']['hashtags']

            my_data = str(t_date)+";"+str(t_id)+";"+str(t_followers)+";"+str(t_text)+";"+str(t_user)
            store_data(my_data)
            return True
        except BaseException as e:
            print('failed ondata: ' + str(e) + ' TIME: ' + str(datetime.fromtimestamp(time()).strftime('%Y%m%d_%H%M')))
            sleep(5)
            pass

    def on_error(self, status_code):
        print(status_code)
        if status_code == 420:
            # too many requests
            sleep(61)
            return False


def get_secret():
    with open('secret.json') as f:
        data = json.load(f)
        return data


def store_data(my_data):
    try:
        file_name = 'DATA/DataGatherer_' + str(datetime.fromtimestamp(time()).strftime('%Y%m%d_%H') + '.csv')
        file = open(file_name, 'a')
        file.write(my_data)
        file.write('\n')
        file.close()
    except BaseException as e:
        print('store_data: ' + str(e) + ' TIME: ' + str(datetime.fromtimestamp(time()).strftime('%Y%m%d_%H%M')))
        sleep(5)
        pass


if __name__ == "__main__":
    my_secret = get_secret()
    myListener = MyStreamListener()
    auth = OAuthHandler(my_secret['consumer_key'], my_secret['consumer_secret'])
    auth.set_access_token(my_secret['access_token'], my_secret['access_token_secret'])
    myStream = Stream(auth=auth, listener=myListener)

    # track = keywords; follow = user ID; locations
    # myStream.filter(languages=["nl"], track=["het", "de", "een"])
    myStream.filter(locations=[2.49,49.5,6.35,51.5], languages=["nl"])
    # myStream.filter(follow=['98639150', '951258554', '40634644', '2860510937'])

