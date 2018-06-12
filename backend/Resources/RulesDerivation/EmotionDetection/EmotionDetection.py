import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

countAnger = 0
countAnt = 0
countDisgust = 0
countFear = 0
countJoy = 0
countSadness = 0
countSurprise = 0
countTrust = 0
countPos = 0
countNeg = 0

file_handler = open("1.txt", "r").read()

stop_words = set(stopwords.words('english'))

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

#count anticipation
file_handler2 = open("anticipationSO.txt", "r")

for line in file_handler2:
    chunks = line.split()
    if chunks[0] in filtered_words:
            print(chunks[0])
            countAnt = countAnt + 1

#count disgust
file_handler3 = open("disgustSO.txt", "r")

for line in file_handler3:
    chunks = line.split()
    if chunks[0] in filtered_words:
            print(chunks[0])
            countDisgust = countDisgust + 1


#count fear
file_handler4 = open("fearSO.txt", "r")

for line in file_handler4:
    chunks = line.split()
    if chunks[0] in filtered_words:
            print(chunks[0])
            countFear = countFear + 1

#count joy
file_handler5 = open("joySO.txt", "r")

for line in file_handler5:
    chunks = line.split()
    if chunks[0] in filtered_words:
            print(chunks[0])
            countJoy = countJoy + 1

#count sadness
file_handler6 = open("sadnessSO.txt", "r")

for line in file_handler6:
    chunks = line.split()
    if chunks[0] in filtered_words:
            print(chunks[0])
            countSadness = countSadness + 1

#count surprise
file_handler7 = open("surpriseSO.txt", "r")

for line in file_handler7:
    chunks = line.split()
    if chunks[0] in filtered_words:
            print(chunks[0])
            countSurprise = countSurprise + 1

#count trust
file_handler8 = open("trustSO.txt", "r")

for line in file_handler8:
    chunks = line.split()
    if chunks[0] in filtered_words:
            print(chunks[0])
            countTrust = countTrust + 1

total = countAnger + countAnt + countDisgust + countFear + countJoy + countSadness + countSurprise + countTrust

angerPer = (countAnger/total)*100
antPer = (countAnt/total)*100
disgustPer = (countDisgust/total)*100
fearPer = (countFear/total)*100
joyPer = (countJoy/total)*100
sadnessPer = (countSadness/total)*100
surprisePer = (countSurprise/total)*100
trustPer = (countTrust/total)*100


print("Anger : %.2f" %angerPer)
print("Ant : %.2f" %antPer)
print("Disgust : %.2f" %disgustPer)
print("Fear : %.2f" %fearPer)
print("Joy : %.2f" %joyPer)
print("Sadness : %.2f" %sadnessPer)
print("Surprise : %.2f" %surprisePer)
print("Trust : %.2f" %trustPer)








