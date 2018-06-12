import nltk
import os
import math
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

path='/home/thishani/1. Python files/EmotionDetection/popular'

stop_words = set(stopwords.words('english'))

totalPosts = 1667

importantTerms = []

#if 'enjoy' in file_handler:
#    print ("true")

#looping through the directory
for filename in os.listdir(path):
    file_handler = open(os.path.join(path,filename), "r").read()
    words = word_tokenize(file_handler)

    filtered_words = []

    #stopwords removal
    for w in words:
        if w not in stop_words:
            filtered_words.append(w)

    wordCount = len(filtered_words)
    docCount = 0

    file_handler4 = open("importantTerms.txt", "r").read()
    file_handler2 = open("importantTerms.txt", "a")

    for x in filtered_words:

        xWordCount = filtered_words.count(x)
        
        if x not in file_handler4:
            file_handler2.write(x.rstrip('\n'))

            for filename2 in os.listdir(path):
                file_handler3 = open(os.path.join(path,filename2), "r").read()
                if x in file_handler3:
                    docCount = docCount + 1
            
            tf = xWordCount/wordCount
            idf = math.log(totalPosts/docCount)

            file_handler2.write(" "+str(tf*idf)+"\n")


print("done")
