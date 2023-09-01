# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 23:41:43 2022

@author: twind
"""

import test
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import re

url = "https://www.fmkorea.com/best2/5234657812"

def crawling_data(url):
    
    data_list = []
    data = list()
    
    html = urlopen(url)
    bs_obj = BeautifulSoup(html.read(),"html.parser")
    div_name_big = bs_obj.find("div",{"id":"bd_capture"})
     # print(div_name)
    div_name_mid = div_name_big.find("div",{"class","top_area ngeb"})
     # print(div_mid)
    div_name =div_name_mid.find("span",{"class":"np_18px_span"})
     
    Title = div_name.text
    Title = Title.replace(" ","")
    Title = Title.replace("\"", "")
    
    # print(Title)
    
    div_big = bs_obj.find("div",{"id":"cmtPosition"})
    ul = div_big.find("ul",{"class":"fdb_lst_ul"})
    li = ul.findAll("li")
    #정규식
    # ^comment\_ == comment_로 시작하는 class 찾아오기
    
    for item in li:
        list_row = []
        div = item.find(attrs={'class':re.compile('^comment\_')})
        div_id = item.find(attrs={'class':re.compile('^member\_')})
        list_row.append(div_id.text)
        list_row.append(div.text)
        data_list.append(list_row)
        nondata = list()
    for i in data_list:
        y = test.do_service(i[1])
        if y == 0:
            data.append(i)
        else:
            nondata.append(i)
        
    data_label = ['악성유저', '악성댓글']   
    with open("data/data_"+Title+".csv","w",encoding = "utf-8")as file:
        writer = csv.writer(file)
        
        writer.writerow(data_label)
        
        for row in data:
            writer.writerow(row)
    file.close()
    
    return data, nondata
    
crawling_data(url)