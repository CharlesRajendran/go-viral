import csv
import sys

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize as wt

def readFile(filename):
    file = 'movie_tweets/'+filename
    tweets = []
    with open(file,'r') as f:
        reader = csv.reader(f)
        
        # read all records and will filter only the tweets
        for row in reader:
            tweets.append(row[1])
            
    return tweets



def printTweets(tweets):    
    for tweet in tweets:
        print(tweet+"\n=======================================\n")


def writeFile(tweets):
    # for non uniocode characters
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    
    f_h = open("tweet_data.csv","a")
    csv_writer = csv.writer(f_h)

    for tweet in tweets:
        t = tweet.translate(non_bmp_map)
        csv_writer.writerow((t,str(0)))
    print("============= WRITTEN =============")    

def removeStopWords(t):
    stop_words = stopwords.words("english")
    word_feature_vector = []
    for word in wt(t):
        if word not in stop_words:
            word_feature_vector.append(word)
    return word_feature_vector



movies = ["piratesofthecaribbean.csv"]

for movie in movies:
    # base form tweets without any preprocessing
    tweets = readFile(movie)

    # tweets without duplicates
    non_duplicate_tweets = list(set(tweets))

    # write tweets into file
    writeFile(non_duplicate_tweets)


####### Important #########
###### When Fetching Tweets Fetch tweets close to the relese date ######
################## so we can get more intent tweets #################

"""
printTweets(non_duplicate_tweets)
"""


"""
for tweet in non_duplicate_tweets:
    print(removeStopWords(tweet))
"""


"""
# print tweet list
printTweets(non_duplicate_tweets)
"""
