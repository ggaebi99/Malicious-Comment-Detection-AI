# -*- coding: utf-8 -*-

"""
Spyder Editor

This is a temporary script file.
"""


import pickle
import konlpy
import pandas as pd
import matplotlib.pyplot as plt
import string
from hanspell import spell_checker as sc
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv("../Dataset.csv")
df = pd.DataFrame(columns = ['content', 'label'])

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

def remove_punc(x):
    new_string = []
    for i in x:
        if i not in string.punctuation + "ㅡㅜㅠㅋㅎㄷ":
            new_string.append(i)
    new_string = "".join(new_string)
    return new_string

def get_data():
    list1 = list()
    list2 = list()
    list3 = list()
    
    for i in data["content\tlable"]:
        list1.append(i.split("\t"))

    for i in range(len(list1)):
        list1[i][0] = remove_punc(list1[i][0])
        result = sc.check(list1[i][0])
        print(result)
        dict_result = result.as_dict()
        text = remove_JS(dict_result["checked"])
        text = remove_Fire(text)
        list2.append(text)
        list3.append(int(list1[i][1]))

    df['content'] = list2
    df['label'] = list3
    df.to_csv("data_test.csv", index = False) # 일단 최종 형태 저장
    
    x = df['content']
    y = df['label']
        
    #툴 만들기
    tool = CountVectorizer()
    tool.fit(x)
    x = tool.transform(x)
    
    pickle.dump(tool, open("tool.t", "wb"))
    
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size = 0.05)
    
    return x_train, x_test, y_train, y_test

def make_model():
    model = MultinomialNB()
    
    return model

def do_learn():
    x_train, x_test, y_train, y_test = get_data()
    
    model = make_model()
    
    model.fit(x_train, y_train)
    
    score = model.score(x_test, y_test)
    
    print(score)
    
    pickle.dump(model, open("model_10000.m", "wb"))
    
do_learn()