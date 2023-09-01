# -*- coding: utf-8 -*-
import pickle
import konlpy
import string
from hanspell import spell_checker as sc
import nltk

def remove_punc(text):
    new_string = []
    for i in text:
        if i not in string.punctuation + "ㅡㅜㅠㅋㅎㄷ":
            new_string.append(i)
            # print(i)
        # print(i)
    new_string = "".join(new_string)
    # print(new_string)
    # print("===================")
    # print(new_string)
    return new_string

def remove_JS(text):
    okt = konlpy.tag.Okt()
    clean_words = []
    for word in okt.pos(text, stem=True): #어간 추출
        if word[1] not in ['Josa', 'Eomi', 'Punctuation']: #조사, 어미, 구두점 제외 
            clean_words.append(word[0])
    # print(clean_words) #['스토리', '진짜', '너무', '노잼']
    text = ' '.join(clean_words)
    # print(document) #스토리 진짜 너무 노잼
    return text
        
def remove_Fire(text):
    stopwords = []
    f = open('model/stopword.txt', 'r', encoding=("UTF-8"))
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        stopwords.append(line)
    f.close()
    clean_words = []
    for word in nltk.tokenize.word_tokenize(text): 
        if word not in stopwords:
            clean_words.append(word)
            
    text = ' '.join(clean_words)
    return text

def process_All(text):
    data = remove_Fire(remove_JS(remove_punc(text)))
    tool = pickle.load(open("model/tool.t", "rb"))
    x = tool.transform([data]).toarray()
    # print(x)
    return x

# process_All("뭐야 시ㅡ발아")

text = "만약에 뭐야 시ㅡ발아"

data = remove_Fire(remove_JS(remove_punc(text)))

print(data)
