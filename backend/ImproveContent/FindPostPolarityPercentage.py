import nltk
import fileinput
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def FindPolarityPer(file_name):
    stop_words = set(stopwords.words('english'))
    countPositive = 0
    countNegative = 0

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
            countPositive = countPositive + 1
                

    #count negative
    for line in fileinput.input("negativeSO.txt"):
        chunks = line.split()
        if chunks[0] in filtered_words:
            countNegative = countNegative + 1


    total = countPositive + countNegative

    
    try:
        positivePer = (countPositive/total)*100
        negativePer = (countNegative/total)*100
    except ArithmeticError:
        print("=========No emotions=============")

    per = {'positivePer' : positivePer, 'negativePer' : negativePer}
    return per

#print (FindPolarityPer(open("23.txt","r").read()))

                
















            
            
