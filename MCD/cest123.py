# -*- coding: utf-8 -*-


import pickle
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import model_selection
from sklearn import tree, svm, neighbors, linear_model

data = pd.read_csv("data_test.csv")

print(data.info())

for i, text in enumerate(data["content"].isnull()):
    if text:
        data = data.drop(i)

x = data["content"]
y = data["label"]


print(data.info())
print(data.isnull().sum())

tool = pickle.load(open("model/tool.t", "rb"))
x = tool.transform(x)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size = 0.05, random_state = 47)

model = MultinomialNB()
# model = neighbors.KNeighborsClassifier()
# model = tree.DecisionTreeClassifier()
# model = svm.SVC()
# model = linear_model.LogisticRegression()

model.fit(x_train, y_train)

score = model.score(x_test, y_test)

pickle.dump(model, open("model/model_NB.m", "wb"))

print(score)