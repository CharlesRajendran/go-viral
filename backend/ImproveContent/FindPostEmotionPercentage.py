import nltk
import fileinput
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def FindEmotionsPer(file_name):
    stop_words = set(stopwords.words('english'))    
    countAnger = 0
    countAnt = 0
    countDisgust = 0
    countFear = 0
    countJoy = 0
    countSadness = 0
    countSurprise = 0
    countTrust = 0

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
            countAnger = countAnger + 1
                

    #count anticipation
    for line in fileinput.input("anticipationSO.txt"):
        chunks = line.split()
        if chunks[0] in filtered_words:
            countAnt = countAnt + 1

            
    #count disgust
    for line in fileinput.input("disgustSO.txt"):
        chunks = line.split()
        if chunks[0] in filtered_words:
            countDisgust = countDisgust + 1

    #count fear
    for line in fileinput.input("fearSO.txt"):
        chunks = line.split()
        if chunks[0] in filtered_words:
            countFear = countFear + 1

    #count joy
    for line in fileinput.input("joySO.txt"):
        chunks = line.split()
        if chunks[0] in filtered_words:
            countJoy = countJoy + 1

    #count sadness
    for line in fileinput.input("sadnessSO.txt"):
        chunks = line.split()
        if chunks[0] in filtered_words:
            countSadness = countSadness + 1

    #count surprise
    for line in fileinput.input("surpriseSO.txt"):
        chunks = line.split()
        if chunks[0] in filtered_words:
            countSurprise = countSurprise + 1

    #count trust
    for line in fileinput.input("trustSO.txt"):
        chunks = line.split()
        if chunks[0] in filtered_words:
            countTrust = countTrust + 1


    total = countAnger + countAnt + countDisgust + countFear + countJoy + countSadness + countSurprise + countTrust

    
    try:
        angerPer = (countAnger/total)*100
        antPer = (countAnt/total)*100
        disgustPer = (countDisgust/total)*100
        fearPer = (countFear/total)*100
        joyPer = (countJoy/total)*100
        sadnessPer = (countSadness/total)*100
        surprisePer = (countSurprise/total)*100
        trustPer = (countTrust/total)*100
    except ArithmeticError:
        print("=========No emotions=============")

    per = {'angerPer' : angerPer, 'antPer' : antPer, 'disgustPer' : disgustPer, 'fearPer' : fearPer, 'joyPer' : joyPer, 'sadnessPer' : sadnessPer, 'surprisePer' : surprisePer, 'trustPer': trustPer}
    return per

#print (FindEmotionsPer(open("23.txt","r").read()))

                
















            
            
