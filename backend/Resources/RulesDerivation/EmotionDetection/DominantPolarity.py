import nltk
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


stop_words = set(stopwords.words('english'))

path='/home/thishani/1. Python files/EmotionDetection/popular'

pos_files = []
neg_files = []

#looping through the directory
for filename in os.listdir(path):
    file_handler = open(os.path.join(path,filename), "r").read()
        
    countPositive = 0
    countNegative = 0
    
    
    words = word_tokenize(file_handler)

    filtered_words = []

    #stopwords removal
    for w in words:
        if w not in stop_words:
            filtered_words.append(w)


    #count positive
    file_handler1 = open("positiveSO.txt", "r")

    for line in file_handler1:
        chunks = line.split()
        if chunks[0] in filtered_words:
            #print(chunks[0])
            countPositive = countPositive + 1
                
    #count negative
    file_handler2 = open("negativeSO.txt", "r")
    
    for line in file_handler2:
        chunks = line.split()
        if chunks[0] in filtered_words:
            #print(chunks[0])
            countNegative = countNegative + 1
            
    total = countPositive + countNegative

    try:
        positivePer = (countPositive/total)*100
        negativePer = (countNegative/total)*100
    except ArithmeticError:
        print("================No Polarity======================")
        continue

    file_list = [positivePer,negativePer]

    maxEmotion = max(file_list)

    if(maxEmotion == positivePer):
        pos_files.append(filename)

    if(maxEmotion == negativePer):
        neg_files.append(filename)

#==========================================================================

angerSO = 0
antSO = 0
disgustSO = 0
fearSO = 0
joySO = 0
sadnessSO = 0
surpriseSO = 0
trustSO = 0

angerPer = 0
antPer = 0
disgustPer = 0
fearPer = 0
joyPer = 0
sadnessPer = 0
surprisePer = 0
trustPer = 0


#for each dominant emotions file   
for f in neg_files:
    file_handler = open(os.path.join(path,f), "r").read()
    words = word_tokenize(file_handler)

    filtered_words = []

    #stopwords removal
    for w in words:
        if w not in stop_words:
            filtered_words.append(w)
        
    countAnger = 0
    countAnt = 0
    countDisgust = 0
    countFear = 0
    countJoy = 0
    countSadness = 0
    countSurprise = 0
    countTrust = 0

    #count anger
    file_handler1 = open("angerSO.txt", "r")

    for line in file_handler1:
        chunks = line.split()
        if chunks[0] in filtered_words:
                #print(chunks[0])
                countAnger = countAnger + 1
                angerSO = angerSO + int(chunks[1])

    #count anticipation
    file_handler2 = open("anticipationSO.txt", "r")

    for line in file_handler2:
        chunks = line.split()
        if chunks[0] in filtered_words:
                #print(chunks[0])
                countAnt = countAnt + 1
                antSO = antSO + int(chunks[1])

    #count disgust
    file_handler3 = open("disgustSO.txt", "r")

    for line in file_handler3:
        chunks = line.split()
        if chunks[0] in filtered_words:
                #print(chunks[0])
                countDisgust = countDisgust + 1
                disgustSO = disgustSO + int(chunks[1])


    #count fear
    file_handler4 = open("fearSO.txt", "r")

    for line in file_handler4:
        chunks = line.split()
        if chunks[0] in filtered_words:
                #print(chunks[0])
                countFear = countFear + 1
                fearSO = fearSO + int(chunks[1])

    #count joy
    file_handler5 = open("joySO.txt", "r")

    for line in file_handler5:
        chunks = line.split()
        if chunks[0] in filtered_words:
                #print(chunks[0])
                countJoy = countJoy + 1
                joySO = joySO + int(chunks[1])

    #count sadness
    file_handler6 = open("sadnessSO.txt", "r")

    for line in file_handler6:
        chunks = line.split()
        if chunks[0] in filtered_words:
                #print(chunks[0])
                countSadness = countSadness + 1
                sadnessSO = sadnessSO + int(chunks[1])

    #count surprise
    file_handler7 = open("surpriseSO.txt", "r")

    for line in file_handler7:
        chunks = line.split()
        if chunks[0] in filtered_words:
                #print(chunks[0])
                countSurprise = countSurprise + 1
                surpriseSO = surpriseSO + int(chunks[1])

    #count trust
    file_handler8 = open("trustSO.txt", "r")

    for line in file_handler8:
        chunks = line.split()
        if chunks[0] in filtered_words:
                #print(chunks[0])
                countTrust = countTrust + 1
                trustSO = trustSO + int(chunks[1])

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
    except ArithmeticError:
        print("=========No emotions=============")

size = len(neg_files)

avgAngerSO = angerSO/size
avgAntSO = antSO/size
avgDisgustSO = disgustSO/size
avgFearSO = fearSO/size
avgJoySO = joySO/size
avgSadnessSO = sadnessSO/size
avgSurpriseSO = surpriseSO/size
avgTrustSO = trustSO/size

print("Anger SO: %.2f" %avgAngerSO)
print("Ant SO: %.2f" %avgAntSO)
print("Disgust SO: %.2f" %avgDisgustSO)
print("Fear SO: %.2f" %avgFearSO)
print("Joy SO: %.2f" %avgJoySO)
print("Sadness SO: %.2f" %avgSadnessSO)
print("Surprise SO: %.2f" %avgSurpriseSO)
print("Trust SO: %.2f" %avgTrustSO)
print("")

avgAnger = angerPer/size
avgAnt = antPer/size
avgDisgust = disgustPer/size
avgFear = fearPer/size
avgJoy = joyPer/size
avgSadness = sadnessPer/size
avgSurprise = surprisePer/size
avgTrust = trustPer/size

print("Anger : %.2f" %avgAnger)
print("Ant : %.2f" %avgAnt)
print("Disgust : %.2f" %avgDisgust)
print("Fear : %.2f" %avgFear)
print("Joy : %.2f" %avgJoy)
print("Sadness : %.2f" %avgSadness)
print("Surprise : %.2f" %avgSurprise)
print("Trust : %.2f" %avgTrust)
        



