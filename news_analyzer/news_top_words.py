import codecs
import json
import re

def get_json_from_file(filename,encod):
	with codecs.open(filename, encoding=encod) as news:
		return json.load(news)

		
def load_available_news_file(filename):
	json = get_json_from_file(filename,'utf8')
	return json['news']


def get_description_from_object(description_object):
	if isinstance(description_object,str):
		return description_object
	else:
		return description_object['__cdata']

def is_word_good(word):
	bad_words = ['votpusk', 'country']
	result = not word.isdigit() and len(word) > 6 and word not in bad_words and 'котор' not in word	and 'тури' not in word
	return result	
		
def get_all_description_words(news_json):
	rss = news_json['rss']
	channel = rss['channel']
	items = channel['item']
	all_words = []
	for item in items:
		description = get_description_from_object(item['description']).lower()
		word_list = re.sub("[^\w]", " ",  description).split()
		all_words += word_list
		
			
	all_news_filtered_words = [word for word in all_words if is_word_good(word)]
	return all_news_filtered_words


def get_popular_words(words_list, top_number):
	word_counter = {}
	for word in words_list:
		if word in word_counter:
			word_counter[word] +=1
		else:
			word_counter[word] = 1
	popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
	return popular_words[0:top_number]
	

	
	
	
print('Введите номер страны, новости о которой нужно проанализировать. Доступны следущие страны:')
file_infos = load_available_news_file('available_news_file_list.json')
country_number = 0
for file_info in file_infos:
	country_number +=1
	print (country_number, '-', file_info['country'])
user_choice = int(input())-1
json_from_file = get_json_from_file( file_infos[user_choice]['file_name'],file_infos[user_choice]['encoding'])
all_news_filtered_words = get_all_description_words(json_from_file)
popular_words = get_popular_words(all_news_filtered_words, 10)
print(popular_words)




