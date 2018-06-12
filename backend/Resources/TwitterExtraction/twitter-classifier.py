import csv
from nltk.tokenize import word_tokenize as wt
import re
import nltk
from nltk.data import load
from random import shuffle

from sklearn.svm import LinearSVC as ls

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier

def readFile(filename):
    file = filename
    tweets = []
    with open(file,'r') as f:
        reader = csv.reader(f)        
        # read all records and will filter only the tweets
        for row in reader:
            tweets.append({"tweet":row[0],"label":row[1]})            
    return tweets

def removeURLs(unprocessed_dataset_with_label):
    for tweet in unprocessed_dataset_with_label:
        tweet_words_array = wt(tweet["tweet"])        
        for word in list(tweet_words_array):
            if word == 'https' or word == 'https…' or word == 'http' or word == 'http…' or word == ':' or word[:2] == '//':
                tweet_words_array.remove(word)                
        tweet["tweet"] = " ".join(tweet_words_array)
    return unprocessed_dataset_with_label

def removeEmoticons(unprocessed_tweet_array):
    for tweet in unprocessed_tweet_array:
        tweet["tweet"] = re.sub(r"[^A-Za-z0-9 .]","",tweet["tweet"])
        
    return unprocessed_tweet_array     

def get_pos_tag_list():
    tag_dict = load("help/tagsets/upenn_tagset.pickle")
    tag_list = []
    for i in tag_dict.keys():
        tag_list.append(i)

    return tag_list

def pos_list_for_tweet(tweet):
    return nltk.pos_tag(wt(tweet))

def get_all_feature_words(tweet_array):
    all_words = []
    for tweet in tweet_array:
        word_and_tag = nltk.pos_tag(wt(tweet["tweet"]))
        for (w,t) in word_and_tag:
            if t in ["VB","VBD","VBN","VBP","VBZ"]:
                all_words.append(w)
            if t in ["JJ","JJR","JJS"]:
                all_words.append(w)
            if t in ["RB","RBS","RBR"]:
                all_words.append(w)
    return all_words


def feature_extractor(preprocessed_tweet):
    feature = {}
    word_and_tag = nltk.pos_tag(wt(preprocessed_tweet))

    # add pos has a feature too if the accuracy is less
    all_tags = []
    all_words = []

    for (w,t) in word_and_tag:
        all_tags.append(t)
    
    for (w,t) in word_and_tag:
        if t in ["VB","VBD","VBN","VBP","VBZ","VBG"]:
            all_words.append(w)
        if t in ["JJ","JJR","JJS"]:
            all_words.append(w)
        if t in ["RB","RBS","RBR"]:
            all_words.append(w)
        if t in ["WRB","MD","IN","RP","CD","NN","NNP"]:
            all_words.append(w)
            
    for word in feature_bag_of_word:
        feature[word] = (word in all_words)

    for tag in tags:
        feature[tag] = (tag in all_tags)
        
    return feature

def training_data(preprocessed_tweet_array):
    feature_set = []
    for tweet in preprocessed_tweet_array:
        feature_set.append((feature_extractor(tweet["tweet"]),tweet["label"]))
    return feature_set

def naive_bayes(training_set,dev_test_set):
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    accuracy = nltk.classify.accuracy(classifier,dev_test_set)
    return (classifier,accuracy)

def svm(training_set,dev_test_set):
    classifier = nltk.SklearnClassifier(ls()).train(training_set)
    accuracy = nltk.classify.accuracy(classifier,dev_test_set)
    return (classifier,accuracy)

def random_forest(training_set,dev_test_set):
    rf_corpus = []
    rf_label = []

    rf_testing_corpus = []
    rf_testing_label = []
    
    for i in feature_set[:280]:
        rf_corpus.append(" ".join(i["tweet"]))
        rf_label.append(i["label"])

    for i in feature_set[280:]:
        rf_testing_corpus.append(" ".join(i["tweet"]))
        rf_testing_label.append(i["label"])

    vectorizer = CountVectorizer(min_df=1)
    
    X = vectorizer.fit_transform(rf_corpus).toarray()
    X_test = vectorizer.transform(rf_testing_corpus).toarray()

    classifier = RandomForestClassifier()
    classifier.fit(X, rf_label)

    accuracy = classifier.score(X_test, rf_testing_label)

    return (classifier,accuracy)


unprocessed_dataset_with_label = readFile("tweet_data.csv")[1:]
url_removed_tweets_with_label = removeURLs(unprocessed_dataset_with_label)
emoticons_removed_tweets_with_label = removeEmoticons(url_removed_tweets_with_label)

tags = get_pos_tag_list()
all_feature_words = get_all_feature_words(emoticons_removed_tweets_with_label)
feature_bag_of_word  = list(nltk.FreqDist(all_feature_words))[:550]

feature_set = training_data(emoticons_removed_tweets_with_label)
shuffle(feature_set)

training_set = feature_set[:280]
dev_test_data = feature_set[280:]




naive_bayes_classfier = naive_bayes(training_set,dev_test_data)
print("Naive Bayes Accuracy:",naive_bayes_classfier[1])

svm_classfier = svm(training_set,dev_test_data)
print("SVM Accuracy:",svm_classfier[1])


"""
random_forest_classfier = random_forest(training_set,dev_test_data)
print("Random Forest Accuracy:",random_forest_classfier[1])
"""

def predict_nbc(tweet):
    return naive_bayes_classfier[0].classify(feature_extractor(tweet))

def predict_svmc(tweet):
    return svm_classfier[0].classify(feature_extractor(tweet))

for twe in ["can't wait for bahubali","#Bahubali2 is released in 8000 theaters",\
            "#Bahubali2 is will be awesome","#Bahubali2 team photo shoot photos http://tw..."]:    
    print("Naive Bayes",predict_nbc(twe))
    print("SVM",predict_svmc(twe))
    print("\n")


"""

for i in emoticons_removed_tweets_with_label:
    if i["label"] == "0":
        for (word,tag) in nltk.pos_tag(wt(i["tweet"])):
            print(word,tag)
        print("\n")

"""

"""
VBZ WRB MD VB JJ IN VBD VBN VBP RB RP VB NNP NN CD VBG
"""
