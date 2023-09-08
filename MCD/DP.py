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
    new_string = "".join(new_string)
    return new_string

def remove_JS(text):
    okt = konlpy.tag.Okt()
    clean_words = []
    for word in okt.pos(text, stem=True): #어간 추출
        if word[1] not in ['Josa', 'Eomi', 'Punctuation']: #조사, 어미, 구두점 제외 
            clean_words.append(word[0])
    text = ' '.join(clean_words)
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

text = "예시"
data = remove_Fire(remove_JS(remove_punc(text)))
