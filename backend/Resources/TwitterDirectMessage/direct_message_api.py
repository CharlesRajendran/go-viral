from tweepy_auth import *
import tweepy as tpy

auth = auth()
api = api(auth)

def send():
    api.send_direct_message(screen_name = "goviral_v2", text = "message text here")
    print("Tweeted!")
