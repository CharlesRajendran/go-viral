import more_preprocessiong as mpp
import nltk

from nltk.tokenize import word_tokenize as wt

words = []
for f in mpp.words_vector:
    print(f)

try:
    all_words = nltk.FreqDist(mpp.final_feature_vector)
    print(all_words)
except Exception as e:
    print(e)



training_set = mpp.final_feature_vector[:350]
development_test_set = mpp.final_feature_vector[350:]


def trainNaiveBayes():
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    return classifier

def testNaiveBayes(tweet):
    classifier = trainNaiveBayes()
    
    #return classifier.classify(featureExtracter(tweet))

def featureExtracter(tweet):
    tweet = mpp.removeStopWords(tweet)
    tweet = mpp.removeHashTag(tweet)
    tweet = mpp.removeTweeterNames(tweet)
    tweet = mpp.removeURLs(tweet)
    tweet = " ".join(tweet)
    tweet = mpp.removeEmoticons(tweet)
    tweet = mpp.removeNamedEntities(tweet)
    
    return tweet


#print(testNaiveBayes("Waiting for the :-) wonderful #bahubali! -- @ssrajamouli http://twu.com"))
