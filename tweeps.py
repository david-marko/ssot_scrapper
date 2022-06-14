import os
import mysql.connector
from datetime import datetime, timedelta, timezone
import tweepy
import time, json

# db_host = os.environ['db_host']
# db_user = os.environ['db_user']
# db_pass = os.environ['db_pass']
# db_name = os.environ['db_name']

consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
access_token = os.environ['access_token']
access_secret = os.environ['access_secret']

# def insert(sql):
#     conn = mysql.connector.connect(host=db_host,user=db_user,port=3306, password=db_pass,database=db_name)
#     # Create a cursor to execute the python file
#     cursor = conn.cursor(dictionary=True,buffered=True)
#     try:
#         cursor.execute(sql)
#         conn.commit()
#     except:
#         print("Script couldnt execute")
#         pass

def get_tweets():
    maxTweets = 1 #10000000000
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    tweet_count = 0
    maxId = -1
    while tweet_count < maxTweets:
        if (maxId <= 0):
            newTweets = api.search_tweets(q='South Sudan #SSOT', count=100, result_type="recent", tweet_mode="extended")
        else:
            newTweets = api.search_tweets(q='South Sudan', count=100, max_id=str(maxId - 1), result_type="recent", tweet_mode="extended")
        if not newTweets:
            print("No new Tweets")
            time.sleep(3)
            continue
        for tweet in newTweets:
            # print(tweet.full_text.encode('utf-8'))
            # open('tweet.txt', 'w').write(json.dumps(tweet))
            print(dir(tweet))
        tweet_count += len(newTweets)	
        maxId = newTweets[-1].id

get_tweets()