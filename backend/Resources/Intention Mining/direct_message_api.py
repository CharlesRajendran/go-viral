from tweepy_auth import *
import tweepy as tpy

import csv

auth = auth()
api = api(auth)

def takeIntentTweets(file):
    tweets = []
    with open(file,'r') as f:
        reader = csv.reader(f)

        tweet_list = []
        for row in reader:
            if row[4] == str(1):
                if row[3] not in tweet_list:                
                    tweets.append({'screen_name':row[1],'tweet':row[3],'intent':row[4],'created_at':row[5],'status_url':row[6]})
                    tweet_list.append(tweets[-1]["tweet"])
                    print(tweet_list[-1])
                    
    return tweets
            
def send(name,content):
    try:
        api.send_direct_message(screen_name = name, text = content)
    except:
        return "Error"
    
    return "Tweeted"

if __name__ == "__main__":
    #takeIntentTweets("data/Wonder Woman/Wonder Woman.csv")
    print(send('goviral_v2','this is awesome!'))
