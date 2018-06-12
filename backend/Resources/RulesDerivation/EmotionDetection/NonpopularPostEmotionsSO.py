import nltk
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

angerSO = 0
antSO = 0
disgustSO = 0
fearSO = 0
joySO = 0
sadnessSO = 0
surpriseSO = 0
trustSO = 0

numFiles = 0

stop_words = set(stopwords.words('english'))

path='/home/thishani/1. Python files/EmotionDetection/non-popular'

#looping through the directory
for filename in os.listdir(path):
    file_handler = open(os.path.join(path,filename), "r").read()
    
    numFiles = numFiles + 1
        
    countAnger = 0
    countAnt = 0
    countDisgust = 0
    countFear = 0
    countJoy = 0
    countSadness = 0
    countSurprise = 0
    countTrust = 0
    
    
    words = word_tokenize(file_handler)

    filtered_words = []

    #stopwords removal
    for w in words:
        if w not in stop_words:
            filtered_words.append(w)


    #count anger
    file_handler1 = open("angerSO.txt", "r")

    for line in file_handler1:
        chunks = line.split()
        if chunks[0] in filtered_words:
                print(chunks[0])
                countAnger = countAnger + 1
                angerSO = angerSO + int(chunks[1])

    #count anticipation
    file_handler2 = open("anticipationSO.txt", "r")

    for line in file_handler2:
        chunks = line.split()
        if chunks[0] in filtered_words:
                print(chunks[0])
                countAnt = countAnt + 1
                antSO = antSO + int(chunks[1])

    #count disgust
    file_handler3 = open("disgustSO.txt", "r")

    for line in file_handler3:
        chunks = line.split()
        if chunks[0] in filtered_words:
                print(chunks[0])
                countDisgust = countDisgust + 1
                disgustSO = disgustSO + int(chunks[1])


    #count fear
    file_handler4 = open("fearSO.txt", "r")

    for line in file_handler4:
        chunks = line.split()
        if chunks[0] in filtered_words:
                print(chunks[0])
                countFear = countFear + 1
                fearSO = fearSO + int(chunks[1])

    #count joy
    file_handler5 = open("joySO.txt", "r")

    for line in file_handler5:
        chunks = line.split()
        if chunks[0] in filtered_words:
                print(chunks[0])
                countJoy = countJoy + 1
                joySO = joySO + int(chunks[1])

    #count sadness
    file_handler6 = open("sadnessSO.txt", "r")

    for line in file_handler6:
        chunks = line.split()
        if chunks[0] in filtered_words:
                print(chunks[0])
                countSadness = countSadness + 1
                sadnessSO = sadnessSO + int(chunks[1])

    #count surprise
    file_handler7 = open("surpriseSO.txt", "r")

    for line in file_handler7:
        chunks = line.split()
        if chunks[0] in filtered_words:
                print(chunks[0])
                countSurprise = countSurprise + 1
                surpriseSO = surpriseSO + int(chunks[1])

    #count trust
    file_handler8 = open("trustSO.txt", "r")

    for line in file_handler8:
        chunks = line.split()
        if chunks[0] in filtered_words:
                print(chunks[0])
                countTrust = countTrust + 1
                trustSO = trustSO + int(chunks[1])

    

avgAnger = angerSO/numFiles
avgAnt = antSO/numFiles
avgDisgust = disgustSO/numFiles
avgFear = fearSO/numFiles
avgJoy = joySO/numFiles
avgSadness = sadnessSO/numFiles
avgSurprise = surpriseSO/numFiles
avgTrust = trustSO/numFiles

print("Anger : %.2f" %avgAnger)
print("Ant : %.2f" %avgAnt)
print("Disgust : %.2f" %avgDisgust)
print("Fear : %.2f" %avgFear)
print("Joy : %.2f" %avgJoy)
print("Sadness : %.2f" %avgSadness)
print("Surprise : %.2f" %avgSurprise)
print("Trust : %.2f" %avgTrust)







