import nltk
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

totalEmotionPercentage = 0
totalPosts = 0
totalSO = 0

stop_words = set(stopwords.words('english'))

path='/home/thishani/1. Python files/EmotionDetection/popular'

#looping through the directory
for filename in os.listdir(path):
	file_handler = open(os.path.join(path,filename), "r").read()
	
	totalPosts = totalPosts + 1
	filtered_words = []

	words = word_tokenize(file_handler)

	#stopwords removal
	for w in words:
		if w not in stop_words:
			filtered_words.append(w)

	wordCount = len(filtered_words)
	emWordCount = 0
	so = 0

	#count anger
	file_handler1 = open("angerSO.txt", "r")

	for line in file_handler1:
		chunks = line.split()
		if chunks[0] in filtered_words:
			#print(chunks[0])
			emWordCount = emWordCount + 1
			so = so + int(chunks[1])

	#count anticipation
	file_handler2 = open("anticipationSO.txt", "r")

	for line in file_handler2:
		chunks = line.split()
		if chunks[0] in filtered_words:
			#print(chunks[0])
			emWordCount = emWordCount + 1
			so = so + int(chunks[1])

	#count disgust
	file_handler3 = open("disgustSO.txt", "r")

	for line in file_handler3:
		chunks = line.split()
		if chunks[0] in filtered_words:
			#print(chunks[0])
			emWordCount = emWordCount + 1
			so = so + int(chunks[1])

	#count fear
	file_handler4 = open("fearSO.txt", "r")

	for line in file_handler4:
		chunks = line.split()
		if chunks[0] in filtered_words:
			#print(chunks[0])
			emWordCount = emWordCount + 1
			so = so + int(chunks[1])

	#count joy
	file_handler5 = open("joySO.txt", "r")

	for line in file_handler5:
		chunks = line.split()
		if chunks[0] in filtered_words:
			#print(chunks[0])
			emWordCount = emWordCount + 1
			so = so + int(chunks[1])
			
	#count sadness
	file_handler6 = open("sadnessSO.txt", "r")

	for line in file_handler6:
		chunks = line.split()
		if chunks[0] in filtered_words:
			#print(chunks[0])
			emWordCount = emWordCount + 1
			so = so + int(chunks[1])

	#count surprise
	file_handler7 = open("surpriseSO.txt", "r")

	for line in file_handler7:
		chunks = line.split()
		if chunks[0] in filtered_words:
			#print(chunks[0])
			emWordCount = emWordCount + 1
			so = so + int(chunks[1])

	#count trust
	file_handler8 = open("trustSO.txt", "r")

	for line in file_handler8:
		chunks = line.split()
		if chunks[0] in filtered_words:
			#print(chunks[0])
			emWordCount = emWordCount + 1
			so = so + int(chunks[1])

		
	emotionPercentage = (emWordCount/wordCount)*100
	totalEmotionPercentage = totalEmotionPercentage + emotionPercentage
	totalSO = totalSO + so

averageEmotionPercentageOfAPopularPost = totalEmotionPercentage / totalPosts
averageSOOfAPopularPost = totalSO / totalPosts

print("Average Emotion Percentage Of A Popular Post : %.2f" %averageEmotionPercentageOfAPopularPost)
print("Average Semantic Orientation Of A Popular Post : %.2f" %averageSOOfAPopularPost)


