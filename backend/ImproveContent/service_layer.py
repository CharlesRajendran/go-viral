import MeasuringPopularity as mp
import copy
import Visualization as vn
import Recommend as r

from nltk.tokenize import sent_tokenize as st

file_name = ""
matching_negative_rules = {}
emotion_words = []
sentiment_words = []

def get_popularity(filename):
	global file_name
	file_name = 'content/{0}.txt'.format(filename)

	popularity_value = mp.measurePopularity(file_name)
	
	global matching_negative_rules
	global emotion_words
	global sentiment_words

	matching_negative_rules = copy.deepcopy(mp.getRules())
	emotion_words = mp.e_visualization
	sentiment_words = mp.s_visualization

	return {'p_score':popularity_value,'p_percentage':str(int((popularity_value+1)*50))}


def get_words_from_emotion_list(emotion_list):
	words = []
	for emo_word in emotion_list:
		for word in emo_word:
			words.append(word)
	return list(set(words)) 

def visualise_pos_neg_words():
	rule_word_dict = vn.visualize(emotion_words,sentiment_words,file_name)
	
	e_pos_words = get_words_from_emotion_list(rule_word_dict['e_pos'])	
	s_pos_words = get_words_from_emotion_list(rule_word_dict['s_pos'])

	e_neg_words = get_words_from_emotion_list(rule_word_dict['e_neg'])
	s_neg_words = get_words_from_emotion_list(rule_word_dict['s_neg'])

	pos_words = list(set(e_pos_words+s_pos_words))
	neg_words = list(set(e_neg_words+s_neg_words))

	final_neg_words = []
	for wo in neg_words:
		if wo in pos_words:
			if wo in e_neg_words and wo in s_neg_words:
				final_neg_words.append(wo)
		else:
			final_neg_words.append(wo)

	
	final_pos_words = []

	for wo in pos_words:
		if wo not in final_neg_words:
			final_pos_words.append(wo)
	
	return {'popular_words':final_pos_words,'non_popular_words':final_neg_words}
	

def return_sentence_of_word(word_original):
	content = open(file_name,'r').read()

	final_content_sent = []

	for sentence in st(content):
		try:
			if sentence.index(word_original) != -1:
				final_content_sent.append(sentence)
			print()
		except Exception as ex:
			pass
	return final_content_sent



def recommedation():
	recommendation_dictionary = r.recommend(matching_negative_rules,file_name)
	
	recommedations_final = {}
	recommedations = []
	recommedations_word = []
	original_words_checker = []
	suggestion_words_checker = []
	message_checker = []

	for key in recommendation_dictionary.keys():
		rule_num = key.replace('rule','')
		print(key)
		for recomend_list in recommendation_dictionary[key]:
			if type(recomend_list) == type([]):
				for recommend_word in recomend_list:
					if recommend_word != []:
						if recommend_word[0] != recommend_word[2]:
							if recommend_word[0] not in original_words_checker:
								recommedations.append({'original_word':recommend_word[0],'sugessions':[recommend_word[2]],'sentence':return_sentence_of_word(recommend_word[0]),'rulenum':rule_num})
								original_words_checker.append(recommend_word[0])
								suggestion_words_checker.append(recommend_word[2])
							else:
								for rw in recommedations:
									if rw['original_word'] == recommend_word[0]:
										if recommend_word[2] not in rw['sugessions']:
											rw['sugessions'].append(recommend_word[2])
			else:
				rev_sent = ""
				try:
					if recomend_list.split(' ')[2] == "increase":
						rev_sent = recomend_list.replace('increase','lessen')
					elif recomend_list.split()[2] == "lessen":
						rev_sent = recomend_list.replace('lessen','increase')
				except:
					pass
				
				if recomend_list not in message_checker and rev_sent not in message_checker:
					recommedations_word.append({'message':recomend_list,'rulenum':rule_num})
					message_checker.append(recomend_list)

	recommedations_final = {'list_recommendations':recommedations,'string_recommendations':recommedations_word}
	
	return recommedations_final
	


if __name__ == "__main__":
	print("popularity checking:",get_popularity('Spider Man'))
	print(visualise_pos_neg_words())
	print(recommedation())


	