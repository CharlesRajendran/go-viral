import csv
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize as wt

from sklearn.svm import LinearSVC as ls



import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets



def readFile(filename):
    file = filename
    tweets = []
    with open(file,'r') as f:
        reader = csv.reader(f)
        
        # read all records and will filter only the tweets
        for row in reader:
            tweets.append({"tweet":row[0],"label":row[1]})
            
    return tweets

def removeStopWords(t):
    stop_words = stopwords.words("english")
    word_feature_vector = []
    for word in wt(t):
        if word not in stop_words:
            word_feature_vector.append(word)
    return word_feature_vector


def removeHashTag(tweet_words):
    for word in tweet_words:
        if word == "#" or word == "," or word == "-" or word == "--" or word == ".":
            tweet_words.remove(word)


    return tweet_words

def removeTweeterNames(tweet_words):
    for word in list(tweet_words):
        if word == '@':
            tweet_words.remove(tweet_words[tweet_words.index(word)+1])
            tweet_words.remove(word)

    return tweet_words    



def removeURLs(tweet_words):
    for word in list(tweet_words):
        if word == 'bahubali' or word == 'Bahubali' or word == 'bahubali2' or word == 'Bahubali2' or word == 'https' or word == 'http' or word == ':' or word[:2] == '//':
            tweet_words.remove(word)

    return tweet_words  
        

def countOneandZero(tweets):
    non_intent = 0
    intent = 0
    
    for word in list(tweets):
        try:
            if word['label'] == "0":
                non_intent+= 1
            elif word['label'] == "1":
                intent+=1
            else:
                word['label'] = "0"
                non_intent+= 1
                
        except Exception as e:
            pass

    
    return (intent,non_intent)


def removeEmoticons(original_string):
    return re.sub(r"[^A-Za-z ]","",original_string)


def removeNamedEntities(tweet):
    nameremovedtweets = []
    try:
        for (word,tag) in nltk.pos_tag(tweet):
            if tag == 'NNP':
                pass
            else:
                nameremovedtweets.append(word)
    except Exception as e:
        pass

    return nameremovedtweets

def makeStrArr(string):
    return string.split()


def preprocess():
    finalTweets = []
    tweets = readFile("tweet_data.csv")
    for t in tweets:
        
        t["tweet"] = removeStopWords(t["tweet"])
        t["tweet"] = removeHashTag(t["tweet"])
        t["tweet"] = removeTweeterNames(t["tweet"])
        t["tweet"] = removeURLs(t["tweet"])
        t["tweet"] = " ".join(t["tweet"])
        t["tweet"] = removeEmoticons(t["tweet"])
        if len(t["tweet"]) > 0 :
            t["tweet"] = makeStrArr(t["tweet"])
            finalTweets.append(t)
    
    return finalTweets

#print(countOneandZero(readFile("tweet_data.csv")))

#tagged = nltk.pos_tag()
final_feature_vector = preprocess()
words_vector = [] 
for t in final_feature_vector:
    t["tweet"] = removeNamedEntities(t["tweet"])
    words_vector.append((" ".join(t["tweet"]),t["label"]))

all_words = []

for f in words_vector[1:]:
    for w in f[0].split():
        all_words.append(w)


all_words_with_frequency = nltk.FreqDist(all_words)

def featureExtracter(tweet):
    features = {}

    tweet = removeStopWords(tweet)
    
    tweet = removeHashTag(tweet)
    tweet = removeTweeterNames(tweet)
    tweet = removeURLs(tweet)
    tweet = " ".join(tweet)
    
    tweet = removeEmoticons(tweet)
    tweet = tweet.split()
    tweet = removeNamedEntities(tweet)
    
    for word in list(all_words_with_frequency.keys())[:900]:
        features[word] = (word in tweet)
    return features


feature_set = []

for (tweet,label) in words_vector[1:]:
    feature_set.append((featureExtracter(tweet),label))


training_set = feature_set[:290]
testing_set = feature_set[290:]


classifier = nltk.NaiveBayesClassifier.train(training_set)
"""
print("Naive Bayes Results")
print(classifier.classify(featureExtracter("can't wait for bahubali")))
print(classifier.classify(featureExtracter("#Bahubali2 is will be awesome")))

print(classifier.classify(featureExtracter("#Bahubali2 is released in 8000 theaters")))
print(classifier.classify(featureExtracter("#Bahubali2 team photo shoot photos http://tw...")))

print("Accuracy :",nltk.classify.accuracy(classifier,testing_set))

print("\nMost Informative Features\n")
classifier.show_most_informative_features(10)
"""
print("Accuracy Naive Bayes",nltk.classify.accuracy(classifier,testing_set))


classifier2 = nltk.classify.SklearnClassifier(ls())
classifier2.train(training_set)

""" 
print("SVM Results")

print(classifier2.classify(featureExtracter("can't wait for bahubali")))
print(classifier2.classify(featureExtracter("#Bahubali2 is will be awesome")))

print(classifier2.classify(featureExtracter("#Bahubali2 is released in 8000 theaters")))
print(classifier2.classify(featureExtracter("#Bahubali2 team photo shoot photos http://tw...")))


"""
print("SVM Accuracy :",nltk.classify.accuracy(classifier2,testing_set))

rf_corpus = []
rf_label = []

rf_testing_corpus = []
rf_testing_label = []

for i in final_feature_vector[:280]:
    rf_corpus.append(" ".join(i["tweet"]))
    rf_label.append(i["label"])

#print("rf_corpus is ",rf_corpus[7])

for i in final_feature_vector[280:]:
    rf_testing_corpus.append(" ".join(i["tweet"]))
    rf_testing_label.append(i["label"])


vectorizer = CountVectorizer(min_df=1)
X = vectorizer.fit_transform(rf_corpus).toarray()

X_test = vectorizer.transform(rf_testing_corpus).toarray()

clf = RandomForestClassifier()
clf.fit(X, rf_label)

print("RF Accuracy :",clf.score(X_test,rf_testing_label))


def predict_nbc(tweet):
    return classifier.classify(featureExtracter(tweet))

def predict_svmc(tweet):
    return classifier2.classify(featureExtracter(tweet))

def predict_rfc(tweet_list):
    return clf.predict(vectorizer.transform(tweet_list).toarray())

for twe in ["can't wait for bahubali","#Bahubali2 is released in 8000 theaters",\
            "#Bahubali2 is will be awesome","#Bahubali2 team photo shoot photos http://tw..."]:    
    print(twe)
    print("Naive Bayes",predict_nbc(twe))
    print("SVM",predict_svmc(twe))
    print("\n")
"""
print(predict_rfc([["can't wait for bahubali","#Bahubali2 is released in 8000 theaters",\
            "#Bahubali2 will be awesome","#Bahubali2 team photo shoot photos http://tw..."]]))
"""

print("Random Forest Results")
print(predict_rfc(["#Bahubali2 is will be awesome","can't wait for bahubali","#Bahubali2 is released in 8000 theaters","#Bahubali2 team photo shoot photos http://tw..."]))
