# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:45:30 2015

@author: User
"""

import nltk
import urllib
from nltk import *
from nltk.tokenize import RegexpTokenizer
from urllib import request
from bs4 import BeautifulSoup

def write(url):
    fail = False
    print( "Attempting to open ", url)
    try:
        linecount=0
        page=request.urlopen(url)
    except:
        print("\nCould not open URL: ", url)
        fail = True
    nohtml = BeautifulSoup(page).get_text()
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(nohtml)
    print(tokens)


write("http://money.cnn.com/data/dow30/")
