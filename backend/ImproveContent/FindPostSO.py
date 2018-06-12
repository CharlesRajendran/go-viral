import nltk
import os
import fileinput
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def FindSO(file_name):
    semanticOrientation = 0
    words = word_tokenize(file_name)
    filtered_words = []
    #stopwords removal
    for w in words:
        if w not in stop_words:
            filtered_words.append(w)
    
    for line in fileinput.input(["angerSO.txt", "anticipationSO.txt", "disgustSO.txt", "fearSO.txt", "joySO.txt", "sadnessSO.txt", "surpriseSO.txt", "trustSO.txt"]):
        chunks = line.split()
        if chunks[0] in filtered_words:
            semanticOrientation = semanticOrientation + int(chunks[1])

    return semanticOrientation



        
            
#print (FindSO(open("23.txt","r").read()))
        
