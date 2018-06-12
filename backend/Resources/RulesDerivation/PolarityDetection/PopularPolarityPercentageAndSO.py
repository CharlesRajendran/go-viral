import nltk
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

positivePer = 0
negativePer = 0

avgPosSO = 0
avgNegSO = 0

numFiles = 0

stop_words = set(stopwords.words('english'))

path='/home/thishani/1. Python files/PolarityDetection/popular'

#looping through the directory
for filename in os.listdir(path):
    file_handler = open(os.path.join(path,filename), "r").read()
    numFiles = numFiles + 1
    semanticOrientationPos = 0
    semanticOrientationNeg = 0
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
            print(chunks[0])
            countPositive = countPositive + 1
            semanticOrientationPos = semanticOrientationPos + int(chunks[1])
                
    #count negative
    file_handler2 = open("negativeSO.txt", "r")
    
    for line in file_handler2:
        chunks = line.split()
        if chunks[0] in filtered_words:
            print(chunks[0])
            countNegative = countNegative + 1
            semanticOrientationNeg = semanticOrientationNeg + int(chunks[1])
            
    total = countPositive + countNegative

    try:
        positivePer = positivePer + (countPositive/total)*100
        negativePer = negativePer + (countNegative/total)*100
        avgPosSO = avgPosSO + semanticOrientationPos
        avgNegSO = avgNegSO + semanticOrientationNeg
    except ArithmeticError:
        print("================No Polarity======================")


avgPos = positivePer/numFiles
avgNeg = negativePer/numFiles

overallAvgPosSO = avgPosSO/numFiles
overallAvgNegSO = avgNegSO/numFiles

print("Positive : %.2f" %avgPos)
print("Negative : %.2f" %avgNeg)

print("Average Positive SO : %.2f" %overallAvgPosSO)
print("Average Negative SO : %.2f" %overallAvgNegSO)
