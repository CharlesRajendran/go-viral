
def openFile(file_name2):
	name2 = file_name2 + '.txt'
	file_handler2 = open(name2, "a")
	return file_handler2


def goThroughEmotionFile():
        file_name = "NRC-Emotion-Lexicon-Wordlevel-v0.92.txt"
        file_handler = open(file_name,"r")
        for line in file_handler:
                words = line.split();
                if(words[2]=='1'):
                        file_handler2 = openFile(words[1])
                        file_handler2.write(words[0]+"\n")
			#file_handler2.close()
	#file_handler.close()




def init():
	goThroughEmotionFile()

init()
	


		
			



	
