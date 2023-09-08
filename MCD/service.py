# -*- coding: utf-8 -*-

import Webcrawl
from flask import Flask, request, render_template
import numpy as np

webserver = Flask(__name__)

@webserver.route("/")
def a():
    msg = "hello"
    
    return msg

@webserver.route("/inputurl")
def index():
    msg = render_template("inputurl.html")
    
    return msg

@webserver.route("/whois", methods=["POST"])
def whois():
    if request.method == "POST":
        url = request.form["url"]
        data, nondata = Webcrawl.crawling_data(url)
        data = np.array(data)
        nick = data[:,0]
        cont = data[:,1]
        msg = render_template("whois.html", nick = nick, 
                              cont = cont)
    else:
        msg = "not support"
    
    return msg
    
webserver.run(host = '0.0.0.0', port = 2022)