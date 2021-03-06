import nltk
import fileinput
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def FindEmotionsSO(file_name):
    stop_words = set(stopwords.words('english'))

    angerSO = 0
    antSO = 0
    disgustSO = 0
    fearSO = 0
    joySO = 0
    sadnessSO = 0
    surpriseSO = 0
    trustSO = 0

    words = word_tokenize(file_name)
    filtered_words = []
    #stopwords removal
    for w in words:
        if w not in stop_words:
            filtered_words.append(w)

    #count anger
    for line in fileinput.input("angerSO.txt"):
        chunks = line.split()
        if chunks[0] in filtered_words:
            angerSO = angerSO + int(chunks[1])
                

    #count anticipation
    for line in fileinput.input("anticipationSO.txt"):
        chunks = line.split()
        if chunks[0] in filtered_words:
            antSO = antSO + int(chunks[1])

            
    #count disgust
    for line in fileinput.input("disgustSO.txt"):
        chunks = line.split()
        if chunks[0] in filtered_words:
            disgustSO = disgustSO + int(chunks[1])

    #count fear
    for line in fileinput.input("fearSO.txt"):
        chunks = line.split()
        if chunks[0] in filtered_words:
            fearSO = fearSO + int(chunks[1])

    #count joy
    for line in fileinput.input("joySO.txt"):
        chunks = line.split()
        if chunks[0] in filtered_words:
            joySO = joySO + int(chunks[1])

    #count sadness
    for line in fileinput.input("sadnessSO.txt"):
        chunks = line.split()
        if chunks[0] in filtered_words:
            sadnessSO = sadnessSO + int(chunks[1])

    #count surprise
    for line in fileinput.input("surpriseSO.txt"):
        chunks = line.split()
        if chunks[0] in filtered_words:
            surpriseSO = surpriseSO + int(chunks[1])

    #count trust
    for line in fileinput.input("trustSO.txt"):
        chunks = line.split()
        if chunks[0] in filtered_words:
            trustSO = trustSO + int(chunks[1])

    so = {'angerSO' : angerSO, 'antSO' : antSO, 'disgustSO' : disgustSO, 'fearSO' : fearSO, 'joySO' : joySO, 'sadnessSO' : sadnessSO, 'surpriseSO' : surpriseSO, 'trustSO': trustSO}
    return so

#print (FindEmotionsPer(open("23.txt","r").read()))

                
















            
            
