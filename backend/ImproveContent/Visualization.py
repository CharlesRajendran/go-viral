import nltk
import fileinput
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def visualize(e_visualization, s_visualization, file_name):
    file_handler = open(file_name,"r").read()

    toker = RegexpTokenizer(r'\w+')
    words = toker.tokenize(file_handler)

    allowed_types = ["JJ", "JJR", "JJS", "NN", "NNS", "RB", "RBR", "RBS", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]

    filtered_words = []

    #stopwords removal
    for w in words:
        if w not in stop_words:
            filtered_words.append(w)

    pos = nltk.pos_tag(filtered_words)
    allowed_words = []
    #print(allowed_words)

    for p in pos:
        if p[1] in allowed_types:
            allowed_words.append(p[0].lower())
            
    e_pos = []
    e_neg = []
    s_pos = []
    s_neg = []

    for d in e_visualization:
        #length = len(d)
        #if(length == 8):
        if('anger' in d and d['anger'] == 0):
            words = findAnger(allowed_words)
            e_neg.append(words)
        else:
            words = findAnger(allowed_words)
            e_pos.append(words)
            

        if('ant' in d and d['ant'] == 0):
            words = findAnt(allowed_words)
            e_neg.append(words)
        else:
            words = findAnt(allowed_words)
            e_pos.append(words)
            

        if('disgust' in d and d['disgust'] == 0):
            words = findDisgust(allowed_words)
            e_neg.append(words)
        else:
            words = findDisgust(allowed_words)
            e_pos.append(words)
            

        if('fear' in d and d['fear'] == 0):
            words = findFear(allowed_words)
            e_neg.append(words)
        else:
            words = findFear(allowed_words)
            e_pos.append(words)


        if('joy' in d and d['joy'] == 0):
            words = findJoy(allowed_words)
            e_neg.append(words)
        else:
            words = findJoy(allowed_words)
            e_pos.append(words)


        if('sadness' in d and d['sadness'] == 0):
            words = findSadness(allowed_words)
            e_neg.append(words)
        else:
            words = findSadness(allowed_words)
            e_pos.append(words)


        if('surprise' in d and d['surprise'] == 0):
            words = findSurprise(allowed_words)
            e_neg.append(words)
        else:
            words = findSurprise(allowed_words)
            e_pos.append(words)


        if('trust' in d and d['trust'] == 0):
            words = findTrust(allowed_words)
            e_neg.append(words)
        else:
            words = findTrust(allowed_words)
            e_pos.append(words)
                
        #if(length == 2):
        if('positivity' in d and d['positivity'] == 0):
            words = findPos(allowed_words)
            e_neg.append(words)
        else:
            words = findPos(allowed_words)
            e_pos.append(words)


        if('negativity' in d and d['negativity'] == 0):
            words = findNeg(allowed_words)
            e_neg.append(words)
        else:
            words = findNeg(allowed_words)
            e_pos.append(words)

    for d in s_visualization:
        #length = len(d)
        #if(length == 8):
        if('anger' in d and d['anger'] == 0):
            words = findAnger(allowed_words)
            s_neg.append(words)
        else:
            words = findAnger(allowed_words)
            s_pos.append(words)
                

        if('ant' in d and d['ant'] == 0):
            words = findAnt(allowed_words)
            s_neg.append(words)
        else:
            words = findAnt(allowed_words)
            s_pos.append(words)
                

        if('disgust' in d and d['disgust'] == 0):
            words = findDisgust(allowed_words)
            s_neg.append(words)
        else:
            words = findDisgust(allowed_words)
            s_pos.append(words)
                

        if('fear' in d and d['fear'] == 0):
            words = findFear(allowed_words)
            s_neg.append(words)
        else:
            words = findFear(allowed_words)
            s_pos.append(words)


        if('joy' in d and d['joy'] == 0):
            words = findJoy(allowed_words)
            s_neg.append(words)
        else:
            words = findJoy(allowed_words)
            s_pos.append(words)


        if('sadness' in d and d['sadness'] == 0):
            words = findSadness(allowed_words)
            s_neg.append(words)
        else:
            words = findSadness(allowed_words)
            s_pos.append(words)


        if('surprise' in d and d['surprise'] == 0):
            words = findSurprise(allowed_words)
            s_neg.append(words)
        else:
            words = findSurprise(allowed_words)
            s_pos.append(words)


        if('trust' in d and d['trust'] == 0):
            words = findTrust(allowed_words)
            s_neg.append(words)
        else:
            words = findTrust(allowed_words)
            s_pos.append(words)

        #if(length == 2):
        if('positivity' in d and d['positivity'] == 0):
            words = findPos(allowed_words)
            s_neg.append(words)
        else:
            words = findPos(allowed_words)
            s_pos.append(words)


        if('negativity' in d and d['negativity'] == 0):
            words = findNeg(allowed_words)
            s_neg.append(words)
        else:
            words = findNeg(allowed_words)
            s_pos.append(words)

    final_visualization = {'e_pos':e_pos, 'e_neg':e_neg, 's_pos':s_pos, 's_neg':s_neg}
    return final_visualization


def findAnger(allowed_words):
    anger_words = []
    for line in fileinput.input("angerSO.txt"):
        chunks = line.split()
        if chunks[0] in allowed_words:
            #print(chunks[0])
            anger_words.append(chunks[0])
    return anger_words
                               

def findAnt(allowed_words):
    ant_words = []
    for line in fileinput.input("anticipationSO.txt"):
        chunks = line.split()
        if chunks[0] in allowed_words:
            #print(chunks[0])
            ant_words.append(chunks[0])
    return ant_words
                               

def findDisgust(allowed_words):
    disgust_words = []
    for line in fileinput.input("disgustSO.txt"):
        chunks = line.split()
        if chunks[0] in allowed_words:
            #print(chunks[0])
            disgust_words.append(chunks[0])
    return disgust_words
                               

def findFear(allowed_words):
    fear_words = []
    for line in fileinput.input("fearSO.txt"):
        chunks = line.split()
        if chunks[0] in allowed_words:
            #print(chunks[0])
            fear_words.append(chunks[0])
    return fear_words

def findJoy(allowed_words):
    joy_words = []
    for line in fileinput.input("joySO.txt"):
        chunks = line.split()
        if chunks[0] in allowed_words:
            #print(chunks[0])
            joy_words.append(chunks[0])
    return joy_words
                              

def findSadness(allowed_words):
    sadness_words = []
    for line in fileinput.input("sadnessSO.txt"):
        chunks = line.split()
        if chunks[0] in allowed_words:
            #print(chunks[0])
            sadness_words.append(chunks[0])
    return sadness_words

                                 
def findSurprise(allowed_words):
    surprise_words = []
    for line in fileinput.input("surpriseSO.txt"):
        chunks = line.split()
        if chunks[0] in allowed_words:
            #print(chunks[0])
            surprise_words.append(chunks[0])
    return surprise_words

                                 
def findTrust(allowed_words):
    trust_words = []
    for line in fileinput.input("trustSO.txt"):
        chunks = line.split()
        if chunks[0] in allowed_words:
            #print(chunks[0])
            trust_words.append(chunks[0])
    return trust_words

                                 
def findPos(allowed_words):
    pos_words = []
    for line in fileinput.input("positiveSO.txt"):
        chunks = line.split()
        if chunks[0] in allowed_words:
            #print(chunks[0])
            pos_words.append(chunks[0])
    return pos_words

                                 
def findNeg(allowed_words):
    neg_words = []
    for line in fileinput.input("negativeSO.txt"):
        chunks = line.split()
        if chunks[0] in allowed_words:
            #print(chunks[0])
            neg_words.append(chunks[0])
    return neg_words


if __name__ == "__main__":
    e_visualization = [{'fear': 1, 'sadness': 1, 'trust': 1, 'anger': 1, 'disgust': 1}, {'fear': 0, 'sadness': 0, 'surprise': 0, 'joy': 0, 'disgust': 0, 'anger': 0, 'ant': 0}, {'negativity': 0, 'positivity': 0}]
    s_visualization = [{'negativity': 1}, {'so': 1}, {'sadness': 0, 'disgust': 0, 'ant': 0, 'fear': 0, 'joy': 0, 'surprise': 0, 'anger': 0}]
    print(visualize(e_visualization, s_visualization, "89.txt"))
            





                
