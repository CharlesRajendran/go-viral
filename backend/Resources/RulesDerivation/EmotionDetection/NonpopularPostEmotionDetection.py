import nltk
import os
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

angerPer = 0
antPer = 0
disgustPer = 0
fearPer = 0
joyPer = 0
sadnessPer = 0
surprisePer = 0
trustPer = 0

avgSO = 0

numFiles = 0

stop_words = set(stopwords.words('english'))

path='/home/thishani/1. Python files/EmotionDetection/non-popular'

#looping through the directory
for filename in os.listdir(path):
    file_handler = open(os.path.join(path,filename), "r").read()
    
    numFiles = numFiles + 1

    semanticOrientation = 0
        
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
                semanticOrientation = semanticOrientation + int(chunks[1])

    #count anticipation
    file_handler2 = open("anticipationSO.txt", "r")

    for line in file_handler2:
        chunks = line.split()
        if chunks[0] in filtered_words:
                print(chunks[0])
                countAnt = countAnt + 1
                semanticOrientation = semanticOrientation + int(chunks[1])

    #count disgust
    file_handler3 = open("disgustSO.txt", "r")

    for line in file_handler3:
        chunks = line.split()
        if chunks[0] in filtered_words:
                print(chunks[0])
                countDisgust = countDisgust + 1
                semanticOrientation = semanticOrientation + int(chunks[1])


    #count fear
    file_handler4 = open("fearSO.txt", "r")

    for line in file_handler4:
        chunks = line.split()
        if chunks[0] in filtered_words:
                print(chunks[0])
                countFear = countFear + 1
                semanticOrientation = semanticOrientation + int(chunks[1])

    #count joy
    file_handler5 = open("joySO.txt", "r")

    for line in file_handler5:
        chunks = line.split()
        if chunks[0] in filtered_words:
                print(chunks[0])
                countJoy = countJoy + 1
                semanticOrientation = semanticOrientation + int(chunks[1])

    #count sadness
    file_handler6 = open("sadnessSO.txt", "r")

    for line in file_handler6:
        chunks = line.split()
        if chunks[0] in filtered_words:
                print(chunks[0])
                countSadness = countSadness + 1
                semanticOrientation = semanticOrientation + int(chunks[1])

    #count surprise
    file_handler7 = open("surpriseSO.txt", "r")

    for line in file_handler7:
        chunks = line.split()
        if chunks[0] in filtered_words:
                print(chunks[0])
                countSurprise = countSurprise + 1
                semanticOrientation = semanticOrientation + int(chunks[1])

    #count trust
    file_handler8 = open("trustSO.txt", "r")

    for line in file_handler8:
        chunks = line.split()
        if chunks[0] in filtered_words:
                print(chunks[0])
                countTrust = countTrust + 1
                semanticOrientation = semanticOrientation + int(chunks[1])

    total = countAnger + countAnt + countDisgust + countFear + countJoy + countSadness + countSurprise + countTrust

    try:
        angerPer = angerPer + (countAnger/total)*100
        antPer = antPer + (countAnt/total)*100
        disgustPer = disgustPer + (countDisgust/total)*100
        fearPer = fearPer + (countFear/total)*100
        joyPer = joyPer + (countJoy/total)*100
        sadnessPer = sadnessPer + (countSadness/total)*100
        surprisePer = surprisePer + (countSurprise/total)*100
        trustPer = trustPer + (countTrust/total)*100

        avgSO = avgSO + semanticOrientation
        print(semanticOrientation/total)
    except ArithmeticError:
        print("=========No emotions=============")

avgAnger = angerPer/numFiles
avgAnt = antPer/numFiles
avgDisgust = disgustPer/numFiles
avgFear = fearPer/numFiles
avgJoy = joyPer/numFiles
avgSadness = sadnessPer/numFiles
avgSurprise = surprisePer/numFiles
avgTrust = trustPer/numFiles

overallAvgSO = avgSO/numFiles

print("Anger : %.2f" %avgAnger)
print("Ant : %.2f" %avgAnt)
print("Disgust : %.2f" %avgDisgust)
print("Fear : %.2f" %avgFear)
print("Joy : %.2f" %avgJoy)
print("Sadness : %.2f" %avgSadness)
print("Surprise : %.2f" %avgSurprise)
print("Trust : %.2f" %avgTrust)

print("Average SO : %.2f" %overallAvgSO)








