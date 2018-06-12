from nltk.corpus import sentiwordnet as swn


#print(list(swn.senti_synsets('slow')))

slow = list(swn.senti_synsets('slow', 'a'))
for s in slow:
    print(s)
    print(s.neg_score())
