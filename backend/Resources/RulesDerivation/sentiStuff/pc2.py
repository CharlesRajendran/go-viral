import nltk
import random
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import FreqDist

def readFile(fileName):
	with open(fileName, "r") as file:
		content = file.readlines()
	return content

fileName1 = "rt-polarity.neg"
fileName2 = "rt-polarity.pos"

negative_sentences = sent_tokenize(str(readFile(fileName1)))
positive_sentences = sent_tokenize(str(readFile(fileName2)))

words = []

for w in negative_sentences:
    words = words + word_tokenize(w.lower())

for w in positive_sentences:
    words = words + word_tokenize(w.lower())

unigram_counter = FreqDist(words)
no_of_unigrams = len(unigram_counter)

word_features = list(unigram_counter.keys())[:3000]

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

documents = []

for s in negative_sentences:
	documents.append((s, "negative"))

for s in positive_sentences:
	documents.append((s, "positive"))

featuresets = [(find_features(rev), category) for (rev, category) in documents]

classifier = nltk.NaiveBayesClassifier.train(featuresets)

test_string1 = "Happy and enjoyable movie."
test_string2 = "But for me cannot support this movie due to the bad behavior from Paul."

print (classifier.classify(find_features(test_string1)))
print (classifier.classify(find_features(test_string2)))
