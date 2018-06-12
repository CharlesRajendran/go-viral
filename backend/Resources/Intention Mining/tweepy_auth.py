import tweepy

def auth():
    # for identifying user
    consumer_key = "TweeterConsumerKey"
    consumer_token = "CustomerToken"

    # for identifying application
    access_token = "AccessToken"
    access_token_secret = "TokenSecret"

    #ouath process
    auth = tweepy.OAuthHandler(consumer_key,consumer_token)
    auth.set_access_token(access_token,access_token_secret)

    return auth


# getting the api
def api(auth):
    api = tweepy.API(auth)
    return api

    
    
"""
Before 2010 it's possible to use api with twitter username and password

but now we need to login using oauth method only
"""

"""
Benifits of OAuth over Basic Authentication

    1. identifies the app which was used.
    2. It doesn’t reveal user password, making it more secure.
    3. It's easier to manage the permissions (read only or read write)
    4. application doesn't reply on a password, so even if the user changes it,
    basic.py the application will still work.
"""


"""
by default, the app has no access to direct messages.

settings and changing the appropriate option to “Read, write and direct messages”,
you can enable your app to have access to every Twitter feature.

"""


"""

Main Model classes in the Twitter API are Tweets, Users, Entities and Places.

"""
