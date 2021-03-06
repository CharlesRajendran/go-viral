import tweepy as tpy
import tweepy_auth as ta
import re

import sys
import csv
import os
import time

import twitter_intention_classifier as tic

auth = ta.auth()
api = ta.api(auth)

#query = "pirates of the caribbean"
def getTweets(query_list):
    max_tweets = 200
    folder = "data/{0}".format(query_list[0])
    try:
        os.mkdir(folder)
    except:
        pass
    file_name = "data/{0}/{0}.csv".format(query_list[0])
    file_h = open(file_name,"a")
    csv_writer = csv.writer(file_h)
    csv_writer.writerow(('person_id','screen_name','name','tweet','intent','created_at','status_url'))

    tweets = []

    for query in query_list:
        print("wait for ten seconds")
        try:
            for status in tpy.Cursor(api.search, q=query,lang="en").items(max_tweets):
                tweets.append(status)
            time.sleep(5)
            #tweets = searched_tweets = [status for status in tpy.Cursor(api.search,  since="2016-03-20",until="2016-03-30",q=query,lang="en").items()]
        except Exception as ex:
            print(ex)
        #print(api.last_response["server"])
            
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    
    for tweet in tweets:
        user = str(tweet.user.id).translate(non_bmp_map)
        screen_name = str(tweet.user.screen_name).translate(non_bmp_map)
        name = str(tweet.user.name).translate(non_bmp_map)
        tweet_text = tweet.text.translate(non_bmp_map)
        tweet_text = re.sub(r"(RT @.*?:)","",tweet_text)

        intent_n = tic.predict_nbc(str(tweet_text))
        intent_s = tic.predict_svmc(str(tweet_text))
        intent_r = tic.predict_rfc(str(tweet_text))

        created_at = tweet.created_at
        status_url = "https://twitter.com/{0}/status/{1}".format(screen_name,tweet.id) 

        if intent_n == intent_s and intent_n == intent_r:
            csv_writer.writerow((user,screen_name,name,tweet_text,str(intent_n),created_at,status_url))
            
    file_h.close()
    return "File is written"



if __name__ == "__main__":
    print(getTweets(["Wonder Woman","Ajith"]))



"""
Status(retweeted=False, retweet_count=737, geo=None, lang='en',
retweeted_status=Status(retweet_count=737, geo=None, lang='en',
retweeted=False, _json={'retweet_count': 737, 'geo': None, 'lang': 'en',
'retweeted': False, 'in_reply_to_status_id_str': None, 'truncated': False,
'in_reply_to_screen_name': None, 'favorited': False, 'is_quote_status': False,
'in_reply_to_status_id': None, 'source': '<a href="http://twitter.com/download/iphone"
rel="nofollow">Twitter for iPhone</a>', 'favorite_count': 3125,
'user': {
'profile_sidebar_fill_color': 'DDFFCC', 'id': 16264006, 'utc_offset': -18000,
'location': 'jet lag city.',
'profile_background_image_url': 'http://pbs.twimg.com/profile_background_images/496472227408121856/qjRSluB1.png',
'lang': 'en', 'contributors_enabled': False, 'notifications': False,
'screen_name': 'petewentz', 'profile_use_background_image': True,
'statuses_count': 17680, 'geo_enabled': False,
'profile_background_image_url_https': 'https://pbs.twimg.com/profile_background_images/496472227408121856/qjRSluB1.png',
'default_profile_image': False, 'friends_count': 392, 'following': False,
'profile_background_tile': True,
'profile_image_url': 'http://pbs.twimg.com/profile_images/502883858279170048/AcxPK-Om_normal.jpeg',
'profile_link_color': '0084B4', 'translator_type': 'none',
'profile_background_color': '9AE4E8',
'has_extended_profile': False, 'is_translator': False,
'is_translation_enabled': True, 'listed_count': 15991,
'favourites_count': 54,'protected': False, 'time_zone': 'Quito',
'profile_banner_url': 'https://pbs.twimg.com/profile_banners/16264006/1354306133',
'name': 'prestige worldwide',
'description': 'i headbang in the rock and roll band fall out boy. snapchat: peteweezy follow it � https://t.co/dgp6GakaCp',
'verified': True, 'followers_count': 5138278, 'profile_text_color': '333333',
'profile_image_url_https': 'https://pbs.twimg.com/profile_images/502883858279170048/AcxPK-Om_normal.jpeg',
'url': 'https://t.co/3iKEkcEBNj', 'profile_sidebar_border_color': 'FFFFFF',
'follow_request_sent': False,
'entities': {'description': {'urls': [{'display_url': 'bit.ly/2dEjbyJ',
'indices': [83, 106], 'expanded_url': 'http://bit.ly/2dEjbyJ',
'url': 'https://t.co/dgp6GakaCp'}]}, 'url': {'urls': [{'display_url':
'petewentz.com', 'indices': [0, 23], 'expanded_url': 'http://www.petewentz.com',
'url': 'https://t.co/3iKEkcEBNj'}]}}, 'id_str': '16264006', 'created_at': 'Fri Sep 12 21:34:37 +0000 2008',
'default_profile': False}, 'id': 833197177425973250, 'place': None,
'contributors': None, 'in_reply_to_user_id': None,
'text': "I'm a Britney Spears lifetime movie away from figuring myself out ��",
'coordinates': None, 'in_reply_to_user_id_str': None,
'metadata': {'result_type': 'recent', 'iso_language_code': 'en'},
'entities': {'hashtags': [], 'symbols': [], 'urls': [], 'user_mentions': []},
'id_str': '833197177425973250', 'created_at': 'Sun Feb 19 06:11:01 +0000 2017'},
author=User(profile_sidebar_fill_color='DDFFCC', favourites_count=54,
utc_offset=-18000, location='jet lag city.', lang='en', screen_name='petewentz',
profile_use_background_image=True, statuses_count=17680,
profile_background_image_url_https='https://pbs.twimg.com/profile_background_images/496472227408121856/qjRSluB1.png',
_json={'profile_sidebar_fill_color': 'DDFFCC', 'id': 16264006,
'utc_offset': -18000, 'location': 'jet lag city.',
'profile_background_image_url': 'http://pbs.twimg.com/profile_background_images/496472227408121856/qjRSluB1.png',
'lang': 'en', 'contributors_enabled': False, 'notifications': False,
'screen_name': 'petewentz', 'profile_use_background_image': True,
'statuses_count': 17680, 'geo_enabled': False,
'profile_background_image_url_https': 'https://pbs.twimg.com/profile_background_images/496472227408121856/qjRSluB1.png',
'default_profile_image': False, 'friends_count': 392, 'following': False,
'profile_background_tile': True,
'profile_image_url': 'http://pbs.twimg.com/profile_images/502883858279170048/AcxPK-Om_normal.jpeg',
'profile_link_color': '0084B4', 'translator_type': 'none', 'profile_background_color': '9AE4E8',
'has_extended_profile': False, 'is_translator': False, 'is_translation_enabled': True,
'listed_count': 15991, 'favourites_count': 54, 'protected': False,
'time_zone': 'Quito',
'profile_banner_url': 'https://pbs.twimg.com/profile_banners/16264006/1354306133', 'name': 'prestige worldwide', 'description': 'i headbang in the rock and roll band fall out boy. snapchat: peteweezy follow it � https://t.co/dgp6GakaCp', 'verified': True, 'followers_count': 5138278, 'profile_text_color': '333333', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/502883858279170048/AcxPK-Om_normal.jpeg', 'url': 'https://t.co/3iKEkcEBNj', 'profile_sidebar_border_color': 'FFFFFF', 'follow_request_sent': False, 'entities': {'description': {'urls': [{'display_url': 'bit.ly/2dEjbyJ', 'indices': [83, 106], 'expanded_url': 'http://bit.ly/2dEjbyJ', 'url': 'https://t.co/dgp6GakaCp'}]}, 'url': {'urls': [{'display_url': 'petewentz.com', 'indices': [0, 23], 'expanded_url': 'http://www.petewentz.com', 'url': 'https://t.co/3iKEkcEBNj'}]}}, 'id_str': '16264006', 'created_at': 'Fri Sep 12 21:34:37 +0000 2008', 'default_profile': False}, default_profile_image=False, friends_count=392, profile_image_url='http://pbs.twimg.com/profile_images/502883858279170048/AcxPK-Om_normal.jpeg', profile_link_color='0084B4', translator_type='none', notifications=False, profile_image_url_https='https://pbs.twimg.com/profile_images/502883858279170048/AcxPK-Om_normal.jpeg', protected=False, description='i headbang in the rock and roll band fall out boy. snapchat: peteweezy follow it � https://t.co/dgp6GakaCp', listed_count=15991, url='https://t.co/3iKEkcEBNj', _api=<tweepy.api.API object at 0x7fb815c30be0>, name='prestige worldwide', created_at=datetime.datetime(2008, 9, 12, 21, 34, 37), profile_background_image_url='http://pbs.twimg.com/profile_background_images/496472227408121856/qjRSluB1.png', is_translation_enabled=True, profile_background_tile=True, contributors_enabled=False, geo_enabled=False, following=False, follow_request_sent=False, profile_background_color='9AE4E8', has_extended_profile=False, is_translator=False, profile_sidebar_border_color='FFFFFF', id=16264006, profile_text_color='333333', time_zone='Quito', profile_banner_url='https://pbs.twimg.com/profile_banners/16264006/1354306133', verified=True, followers_count=5138278, entities={'description': {'urls': [{'display_url': 'bit.ly/2dEjbyJ', 'indices': [83, 106], 'expanded_url': 'http://bit.ly/2dEjbyJ', 'url': 'https://t.co/dgp6GakaCp'}]}, 'url': {'urls': [{'display_url': 'petewentz.com', 'indices': [0, 23], 'expanded_url': 'http://www.petewentz.com', 'url': 'https://t.co/3iKEkcEBNj'}]}}, id_str='16264006', default_profile=False), in_reply_to_status_id_str=None, truncated=False, favorited=False, in_reply_to_screen_name=None, in_reply_to_status_id=None, metadata={'result_type': 'recent', 'iso_language_code': 'en'}, source='Twitter for iPhone', favorite_count=3125, user=User(profile_sidebar_fill_color='DDFFCC', favourites_count=54, utc_offset=-18000, location='jet lag city.', lang='en', screen_name='petewentz', profile_use_background_image=True, statuses_count=17680, profile_background_image_url_https='https://pbs.twimg.com/profile_background_images/496472227408121856/qjRSluB1.png', _json={'profile_sidebar_fill_color': 'DDFFCC', 'id': 16264006, 'utc_offset': -18000, 'location': 'jet lag city.', 'profile_background_image_url': 'http://pbs.twimg.com/profile_background_images/496472227408121856/qjRSluB1.png', 'lang': 'en', 'contributors_enabled': False, 'notifications': False, 'screen_name': 'petewentz', 'profile_use_background_image': True, 'statuses_count': 17680, 'geo_enabled': False, 'profile_background_image_url_https': 'https://pbs.twimg.com/profile_background_images/496472227408121856/qjRSluB1.png', 'default_profile_image': False, 'friends_count': 392, 'following': False, 'profile_background_tile': True, 'profile_image_url': 'http://pbs.twimg.com/profile_images/502883858279170048/AcxPK-Om_normal.jpeg', 'profile_link_color': '0084B4', 'translator_type': 'none', 'profile_background_color': '9AE4E8', 'has_extended_profile': False, 'is_translator': False, 'is_translation_enabled': True, 'listed_count': 15991, 'favourites_count': 54, 'protected': False, 'time_zone': 'Quito', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/16264006/1354306133', 'name': 'prestige worldwide', 'description': 'i headbang in the rock and roll band fall out boy. snapchat: peteweezy follow it � https://t.co/dgp6GakaCp', 'verified': True, 'followers_count': 5138278, 'profile_text_color': '333333', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/502883858279170048/AcxPK-Om_normal.jpeg', 'url': 'https://t.co/3iKEkcEBNj', 'profile_sidebar_border_color': 'FFFFFF', 'follow_request_sent': False, 'entities': {'description': {'urls': [{'display_url': 'bit.ly/2dEjbyJ', 'indices': [83, 106], 'expanded_url': 'http://bit.ly/2dEjbyJ', 'url': 'https://t.co/dgp6GakaCp'}]}, 'url': {'urls': [{'display_url': 'petewentz.com', 'indices': [0, 23], 'expanded_url': 'http://www.petewentz.com', 'url': 'https://t.co/3iKEkcEBNj'}]}}, 'id_str': '16264006', 'created_at': 'Fri Sep 12 21:34:37 +0000 2008', 'default_profile': False}, default_profile_image=False, friends_count=392, profile_image_url='http://pbs.twimg.com/profile_images/502883858279170048/AcxPK-Om_normal.jpeg', profile_link_color='0084B4', translator_type='none', notifications=False, profile_image_url_https='https://pbs.twimg.com/profile_images/502883858279170048/AcxPK-Om_normal.jpeg', protected=False, description='i headbang in the rock and roll band fall out boy. snapchat: peteweezy follow it � https://t.co/dgp6GakaCp', listed_count=15991, url='https://t.co/3iKEkcEBNj', _api=<tweepy.api.API object at 0x7fb815c30be0>, name='prestige worldwide', created_at=datetime.datetime(2008, 9, 12, 21, 34, 37), profile_background_image_url='http://pbs.twimg.com/profile_background_images/496472227408121856/qjRSluB1.png', is_translation_enabled=True, profile_background_tile=True, contributors_enabled=False, geo_enabled=False, following=False, follow_request_sent=False, profile_background_color='9AE4E8', has_extended_profile=False, is_translator=False, profile_sidebar_border_color='FFFFFF', id=16264006, profile_text_color='333333', time_zone='Quito', profile_banner_url='https://pbs.twimg.com/profile_banners/16264006/1354306133', verified=True, followers_count=5138278, entities={'description': {'urls': [{'display_url': 'bit.ly/2dEjbyJ', 'indices': [83, 106], 'expanded_url': 'http://bit.ly/2dEjbyJ', 'url': 'https://t.co/dgp6GakaCp'}]}, 'url': {'urls': [{'display_url': 'petewentz.com', 'indices': [0, 23], 'expanded_url': 'http://www.petewentz.com', 'url': 'https://t.co/3iKEkcEBNj'}]}}, id_str='16264006', default_profile=False), id=833197177425973250, place=None, contributors=None, in_reply_to_user_id=None, created_at=datetime.datetime(2017, 2, 19, 6, 11, 1), source_url='http://twitter.com/download/iphone', coordinates=None, _api=<tweepy.api.API object at 0x7fb815c30be0>, in_reply_to_user_id_str=None, is_quote_status=False, entities={'hashtags': [], 'symbols': [], 'urls': [], 'user_mentions': []}, id_str='833197177425973250', text="I'm a Britney Spears lifetime movie away from figuring myself out ��"), _json={'retweeted': False, 'retweet_count': 737, 'geo': None, 'lang': 'en', 'retweeted_status': {'retweet_count': 737, 'geo': None, 'lang': 'en', 'retweeted': False, 'in_reply_to_status_id_str': None, 'truncated': False, 'in_reply_to_screen_name': None, 'favorited': False, 'is_quote_status': False, 'in_reply_to_status_id': None, 'source': '<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>', 'favorite_count': 3125, 'user': {'profile_sidebar_fill_color': 'DDFFCC', 'id': 16264006, 'utc_offset': -18000, 'location': 'jet lag city.', 'profile_background_image_url': 'http://pbs.twimg.com/profile_background_images/496472227408121856/qjRSluB1.png', 'lang': 'en', 'contributors_enabled': False, 'notifications': False, 'screen_name': 'petewentz', 'profile_use_background_image': True, 'statuses_count': 17680, 'geo_enabled': False, 'profile_background_image_url_https': 'https://pbs.twimg.com/profile_background_images/496472227408121856/qjRSluB1.png', 'default_profile_image': False, 'friends_count': 392, 'following': False, 'profile_background_tile': True, 'profile_image_url': 'http://pbs.twimg.com/profile_images/502883858279170048/AcxPK-Om_normal.jpeg', 'profile_link_color': '0084B4', 'translator_type': 'none', 'profile_background_color': '9AE4E8', 'has_extended_profile': False, 'is_translator': False, 'is_translation_enabled': True, 'listed_count': 15991, 'favourites_count': 54, 'protected': False, 'time_zone': 'Quito', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/16264006/1354306133', 'name': 'prestige worldwide', 'description': 'i headbang in the rock and roll band fall out boy. snapchat: peteweezy follow it � https://t.co/dgp6GakaCp', 'verified': True, 'followers_count': 5138278, 'profile_text_color': '333333', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/502883858279170048/AcxPK-Om_normal.jpeg', 'url': 'https://t.co/3iKEkcEBNj', 'profile_sidebar_border_color': 'FFFFFF', 'follow_request_sent': False, 'entities': {'description': {'urls': [{'display_url': 'bit.ly/2dEjbyJ', 'indices': [83, 106], 'expanded_url': 'http://bit.ly/2dEjbyJ', 'url': 'https://t.co/dgp6GakaCp'}]}, 'url': {'urls': [{'display_url': 'petewentz.com', 'indices': [0, 23], 'expanded_url': 'http://www.petewentz.com', 'url': 'https://t.co/3iKEkcEBNj'}]}}, 'id_str': '16264006', 'created_at': 'Fri Sep 12 21:34:37 +0000 2008', 'default_profile': False}, 'id': 833197177425973250, 'place': None, 'contributors': None, 'in_reply_to_user_id': None, 'text': "I'm a Britney Spears lifetime movie away from figuring myself out ��", 'coordinates': None, 'in_reply_to_user_id_str': None, 'metadata': {'result_type': 'recent', 'iso_language_code': 'en'}, 'entities': {'hashtags': [], 'symbols': [], 'urls': [], 'user_mentions': []}, 'id_str': '833197177425973250', 'created_at': 'Sun Feb 19 06:11:01 +0000 2017'}, 'in_reply_to_status_id_str': None, 'truncated': False, 'in_reply_to_screen_name': None, 'favorited': False, 'is_quote_status': False, 'in_reply_to_status_id': None, 'favorite_count': 0, 'source': '<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>', 'user': {'profile_sidebar_fill_color': '000000', 'id': 727625054872309760, 'utc_offset': -28800, 'location': 'yo momma ass', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'lang': 'en-gb', 'contributors_enabled': False, 'notifications': False, 'screen_name': 'babiespook', 'profile_use_background_image': False, 'statuses_count': 1318, 'geo_enabled': False, 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'default_profile_image': False, 'friends_count': 237, 'following': False, 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/815647382889230338/w_bwLa_z_normal.jpg', 'profile_link_color': 'ECCEF5', 'translator_type': 'none', 'profile_background_color': '000000', 'has_extended_profile': True, 'is_translator': False, 'is_translation_enabled': False, 'listed_count': 0, 'favourites_count': 1753, 'protected': False, 'time_zone': 'Pacific Time (US & Canada)', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/727625054872309760/1483300466', 'name': 'alex \U0001f940', 'description': "hi i'm alex and i like girls and crying and art @dunclone is a bab", 'verified': False, 'followers_count': 33, 'profile_text_color': '000000', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/815647382889230338/w_bwLa_z_normal.jpg', 'url': None, 'profile_sidebar_border_color': '000000', 'follow_request_sent': False, 'entities': {'description': {'urls': []}}, 'id_str': '727625054872309760', 'created_at': 'Tue May 03 22:25:06 +0000 2016', 'default_profile': False}, 'id': 833245421594091520, 'place': None, 'contributors': None, 'in_reply_to_user_id': None, 'text': "RT @petewentz: I'm a Britney Spears lifetime movie away from figuring myself out ��", 'coordinates': None, 'in_reply_to_user_id_str': None, 'metadata': {'result_type': 'recent', 'iso_language_code': 'en'}, 'entities': {'hashtags': [], 'symbols': [], 'urls': [], 'user_mentions': [{'id_str': '16264006', 'indices': [3, 13], 'id': 16264006, 'name': 'prestige worldwide', 'screen_name': 'petewentz'}]}, 'id_str': '833245421594091520', 'created_at': 'Sun Feb 19 09:22:44 +0000 2017'}, author=User(profile_sidebar_fill_color='000000', favourites_count=1753, utc_offset=-28800, location='yo momma ass', lang='en-gb', screen_name='babiespook', profile_use_background_image=False, statuses_count=1318, profile_background_image_url_https='https://abs.twimg.com/images/themes/theme1/bg.png', _json={'profile_sidebar_fill_color': '000000', 'id': 727625054872309760, 'utc_offset': -28800, 'location': 'yo momma ass', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'lang': 'en-gb', 'contributors_enabled': False, 'notifications': False, 'screen_name': 'babiespook', 'profile_use_background_image': False, 'statuses_count': 1318, 'geo_enabled': False, 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'default_profile_image': False, 'friends_count': 237, 'following': False, 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/815647382889230338/w_bwLa_z_normal.jpg', 'profile_link_color': 'ECCEF5', 'translator_type': 'none', 'profile_background_color': '000000', 'has_extended_profile': True, 'is_translator': False, 'is_translation_enabled': False, 'listed_count': 0, 'favourites_count': 1753, 'protected': False, 'time_zone': 'Pacific Time (US & Canada)', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/727625054872309760/1483300466', 'name': 'alex \U0001f940', 'description': "hi i'm alex and i like girls and crying and art @dunclone is a bab", 'verified': False, 'followers_count': 33, 'profile_text_color': '000000', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/815647382889230338/w_bwLa_z_normal.jpg', 'url': None, 'profile_sidebar_border_color': '000000', 'follow_request_sent': False, 'entities': {'description': {'urls': []}}, 'id_str': '727625054872309760', 'created_at': 'Tue May 03 22:25:06 +0000 2016', 'default_profile': False}, default_profile_image=False, friends_count=237, profile_image_url='http://pbs.twimg.com/profile_images/815647382889230338/w_bwLa_z_normal.jpg', profile_link_color='ECCEF5', translator_type='none', notifications=False, profile_image_url_https='https://pbs.twimg.com/profile_images/815647382889230338/w_bwLa_z_normal.jpg', protected=False, description="hi i'm alex and i like girls and crying and art @dunclone is a bab", listed_count=0, url=None, _api=<tweepy.api.API object at 0x7fb815c30be0>, name='alex \U0001f940', created_at=datetime.datetime(2016, 5, 3, 22, 25, 6), profile_background_image_url='http://abs.twimg.com/images/themes/theme1/bg.png', is_translation_enabled=False, profile_background_tile=False, contributors_enabled=False, geo_enabled=False, following=False, follow_request_sent=False, profile_background_color='000000', has_extended_profile=True, is_translator=False, profile_sidebar_border_color='000000', id=727625054872309760, profile_text_color='000000', time_zone='Pacific Time (US & Canada)', profile_banner_url='https://pbs.twimg.com/profile_banners/727625054872309760/1483300466', verified=False, followers_count=33, entities={'description': {'urls': []}}, id_str='727625054872309760', default_profile=False), in_reply_to_status_id_str=None, truncated=False, favorited=False, is_quote_status=False, in_reply_to_status_id=None, metadata={'result_type': 'recent', 'iso_language_code': 'en'}, favorite_count=0, source='Twitter for iPhone', user=User(profile_sidebar_fill_color='000000', favourites_count=1753, utc_offset=-28800, location='yo momma ass', lang='en-gb', screen_name='babiespook', profile_use_background_image=False, statuses_count=1318, profile_background_image_url_https='https://abs.twimg.com/images/themes/theme1/bg.png', _json={'profile_sidebar_fill_color': '000000', 'id': 727625054872309760, 'utc_offset': -28800, 'location': 'yo momma ass', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'lang': 'en-gb', 'contributors_enabled': False, 'notifications': False, 'screen_name': 'babiespook', 'profile_use_background_image': False, 'statuses_count': 1318, 'geo_enabled': False, 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'default_profile_image': False, 'friends_count': 237, 'following': False, 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/815647382889230338/w_bwLa_z_normal.jpg', 'profile_link_color': 'ECCEF5', 'translator_type': 'none', 'profile_background_color': '000000', 'has_extended_profile': True, 'is_translator': False, 'is_translation_enabled': False, 'listed_count': 0, 'favourites_count': 1753, 'protected': False, 'time_zone': 'Pacific Time (US & Canada)', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/727625054872309760/1483300466', 'name': 'alex \U0001f940', 'description': "hi i'm alex and i like girls and crying and art @dunclone is a bab", 'verified': False, 'followers_count': 33, 'profile_text_color': '000000', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/815647382889230338/w_bwLa_z_normal.jpg', 'url': None, 'profile_sidebar_border_color': '000000', 'follow_request_sent': False, 'entities': {'description': {'urls': []}}, 'id_str': '727625054872309760', 'created_at': 'Tue May 03 22:25:06 +0000 2016', 'default_profile': False}, default_profile_image=False, friends_count=237, profile_image_url='http://pbs.twimg.com/profile_images/815647382889230338/w_bwLa_z_normal.jpg', profile_link_color='ECCEF5', translator_type='none', notifications=False, profile_image_url_https='https://pbs.twimg.com/profile_images/815647382889230338/w_bwLa_z_normal.jpg', protected=False, description="hi i'm alex and i like girls and crying and art @dunclone is a bab", listed_count=0, url=None, _api=<tweepy.api.API object at 0x7fb815c30be0>, name='alex \U0001f940', created_at=datetime.datetime(2016, 5, 3, 22, 25, 6), profile_background_image_url='http://abs.twimg.com/images/themes/theme1/bg.png', is_translation_enabled=False, profile_background_tile=False, contributors_enabled=False, geo_enabled=False, following=False, follow_request_sent=False, profile_background_color='000000', has_extended_profile=True, is_translator=False, profile_sidebar_border_color='000000', id=727625054872309760, profile_text_color='000000', time_zone='Pacific Time (US & Canada)', profile_banner_url='https://pbs.twimg.com/profile_banners/727625054872309760/1483300466', verified=False, followers_count=33, entities={'description': {'urls': []}}, id_str='727625054872309760', default_profile=False), id=833245421594091520, place=None, contributors=None, in_reply_to_user_id=None, created_at=datetime.datetime(2017, 2, 19, 9, 22, 44), source_url='http://twitter.com/download/iphone', coordinates=None, _api=<tweepy.api.API object at 0x7fb815c30be0>, in_reply_to_user_id_str=None, in_reply_to_screen_name=None, entities={'hashtags': [], 'symbols': [], 'urls': [], 'user_mentions': [{'id_str': '16264006', 'indices': [3, 13], 'id': 16264006, 'name': 'prestige worldwide', 'screen_name': 'petewentz'}]}, id_str='833245421594091520', text="RT @petewentz: I'm a Britney Spears lifetime movie away from figuring myself out ��") 
"""
