# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:28:24 2022

@author: hisecure
"""
import DP
import pickle
import numpy as np

def get_data(text):
    return DP.process_All(text)

def load_model():
    model = pickle.load(open("model/model_NB_867.m","rb"))
    
    return model

def do_service(text):
    x = get_data(text)
    
    model = load_model()
    
    y_pre = model.predict(x)
    
    # print(y_pre)
    
    return y_pre


