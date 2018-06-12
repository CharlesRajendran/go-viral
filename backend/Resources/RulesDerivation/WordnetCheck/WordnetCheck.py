import os
import nltk
import fileinput
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import stopwords


stop_words = set(stopwords.words('english'))


file_handler = open("24.txt","r").read()

#words = word_tokenize(file_handler)
toker = RegexpTokenizer(r'\w+')
words = toker.tokenize(file_handler)

allowed_types = ["JJ", "JJR", "JJS", "NN", "NNS", "RB", "RBR", "RBS", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]


filtered_words = []

#stopwords removal
for w in words:
    if w not in stop_words:
        filtered_words.append(w)

pos = nltk.pos_tag(filtered_words)
allowed_words = []

for p in pos:
    if p[1] in allowed_types:
            allowed_words.append(p[0].lower())

allowed_words_with_so = [[]]

file_handler1 = open("angerSO.txt", "r")


for line in file_handler1:
    chunks = line.split()
    if chunks[0] in allowed_words:
        allowed_words_with_so.append([chunks[0], chunks[1]])
        

#count anticipation
file_handler2 = open("anticipationSO.txt", "r")

for line in file_handler2:
    chunks = line.split()
    if chunks[0] in filtered_words:
        allowed_words_with_so.append([chunks[0], chunks[1]])
               
#count disgust
file_handler3 = open("disgustSO.txt", "r")

for line in file_handler3:
    chunks = line.split()
    if chunks[0] in filtered_words:
        allowed_words_with_so.append([chunks[0], chunks[1]])
            


#count fear
file_handler4 = open("fearSO.txt", "r")

for line in file_handler4:
    chunks = line.split()
    if chunks[0] in filtered_words:
        allowed_words_with_so.append([chunks[0], chunks[1]])
            

#count joy
file_handler5 = open("joySO.txt", "r")

for line in file_handler5:
    chunks = line.split()
    if chunks[0] in filtered_words:
        allowed_words_with_so.append([chunks[0], chunks[1]])
            

#count sadness
file_handler6 = open("sadnessSO.txt", "r")

for line in file_handler6:
    chunks = line.split()
    if chunks[0] in filtered_words:
        allowed_words_with_so.append([chunks[0], chunks[1]])
            

#count surprise
file_handler7 = open("surpriseSO.txt", "r")

for line in file_handler7:
    chunks = line.split()
    if chunks[0] in filtered_words:
        allowed_words_with_so.append([chunks[0], chunks[1]])
            

#count trust
file_handler8 = open("trustSO.txt", "r")

for line in file_handler8:
    chunks = line.split()
    if chunks[0] in filtered_words:
        allowed_words_with_so.append([chunks[0], chunks[1]])
            
        
recommended_words = [[]]

#to remove empty elements
awwso = list(filter(None, allowed_words_with_so))

#to remove duplicates
al = set(tuple(element) for element in awwso)


for el in al:
    print(el[0])
    syn = wn.synsets(el[0])
    for sy in syn:
        for le in sy.lemmas():
            for line in fileinput.input(["angerSO.txt", "anticipationSO.txt", "disgustSO.txt", "fearSO.txt", "joySO.txt", "sadnessSO.txt", "surpriseSO.txt", "trustSO.txt"]):
                chunks = line.split()
                if (chunks[0] == le.name())and (int(chunks[1])>int(el[1])):
                    recommended_words.append([el[0], el[1], le.name(), chunks[1]])
            fileinput.close()
            
    print("===================")



for ele in recommended_words:
    print(ele)

#




    

    


