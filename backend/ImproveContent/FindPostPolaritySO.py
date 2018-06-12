import nltk
import fileinput
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def FindPolaritySO(file_name):
    stop_words = set(stopwords.words('english'))    
    semanticOrientationPos = 0
    semanticOrientationNeg = 0

    words = word_tokenize(file_name)
    filtered_words = []
    #stopwords removal
    for w in words:
        if w not in stop_words:
            filtered_words.append(w)

    #count positive
    for line in fileinput.input("positiveSO.txt"):
        chunks = line.split()
        if chunks[0] in filtered_words:
            semanticOrientationPos = semanticOrientationPos + int(chunks[1])
                

    #count negative
    for line in fileinput.input("negativeSO.txt"):
        chunks = line.split()
        if chunks[0] in filtered_words:
            semanticOrientationNeg = semanticOrientationNeg + int(chunks[1])

    so = {'semanticOrientationPos' : semanticOrientationPos, 'semanticOrientationNeg' : semanticOrientationNeg}
    
    return so

#print (FindPolaritySO(open("23.txt","r").read()))

                
















            
            
