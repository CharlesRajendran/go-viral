import nltk
import fileinput
from nltk.corpus import wordnet as wn
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def increaseAnger(file_name):
    toker = RegexpTokenizer(r'\w+')
    words = toker.tokenize(file_name)

    allowed_types = ["JJ", "JJR", "JJS", "NN", "NNS", "RB", "RBR", "RBS", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]

    filtered_words = []

    #stopwords removal
    for w in words:
        if w not in stop_words:
            filtered_words.append(w)

    pos = nltk.pos_tag(filtered_words)
    allowed_words = []

    for p in pos:
        if p[1] in allowed_types:
            allowed_words.append(p[0].lower())
            

    allowed_words_with_so = [[]]

    for line in fileinput.input(["angerSO.txt", "anticipationSO.txt", "disgustSO.txt", "fearSO.txt", "joySO.txt", "sadnessSO.txt", "surpriseSO.txt", "trustSO.txt"]):
        chunks = line.split()
        if chunks[0] in allowed_words:
            allowed_words_with_so.append([chunks[0], chunks[1]])

    recommended_words = [[]]

    #to remove empty elements
    awwso = list(filter(None, allowed_words_with_so))

    #to remove duplicates
    al = set(tuple(element) for element in awwso)

    for el in al:
        print(el[0])
        syn = wn.synsets(el[0])
        for sy in syn:
            for le in sy.lemmas():
                for line in fileinput.input(["angerSO.txt", "anticipationSO.txt", "disgustSO.txt", "fearSO.txt", "joySO.txt", "sadnessSO.txt", "surpriseSO.txt", "trustSO.txt"]):
                    chunks = line.split()
                    if (chunks[0] == le.name())and (int(chunks[1])<int(el[1])):
                        recommended_words.append([el[0], el[1], le.name(), chunks[1]])
                fileinput.close()

    return recommended_words





#print(increaseAnger(open("23.txt","r").read()))
    
