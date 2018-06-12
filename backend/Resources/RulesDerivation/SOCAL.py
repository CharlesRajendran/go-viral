def socal():
        file1 = "negative.txt"
        file2 = "verb_dictionary1.11.txt"
        file_handler1 = open(file1, "r")
        for line in file_handler1:
                words1 = line.split()
                file_handler2 = open(file2, "r", encoding = "ISO-8859-1")
                for line2 in file_handler2:
                        words2 = line2.split()
                        if(words1[0] == words2[0]):
                                print(words2[0])
                                file_handler3 = open("negativeSO.txt", "a")
                                file_handler3.write(words2[0] + " " + words2[1] + "\n")

def init():
        socal()

init()
