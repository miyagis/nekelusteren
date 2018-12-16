from tweepy import OAuthHandler, API, Cursor
import csv
from twitter_actions import get_secret


my_secret = get_secret()
auth = OAuthHandler(my_secret['consumer_key'], my_secret['consumer_secret'])
auth.set_access_token(my_secret['access_token'], my_secret['access_token_secret'])
api = API(auth)

# Open/Create a file to append data
csvFile = open('test.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

d = Cursor(api.search, )


for tweet in Cursor(api.search,q="#ps4",count=100,\
                           lang="en",\
                           since_id=2014-06-12).items():
    print tweet.created_at, tweet.text
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])