# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:45:30 2015

@author: User
"""

import nltk
import urllib
from urllib import request
from bs4 import BeautifulSoup

fail = False
url = "http://money.cnn.com/data/dow30/"
print( "Attempting to open ", url)
try:
   linecount=0
   page=request.urlopen(url)
except:
   print("\nCould not open URL: ", url)
   fail = True

nohtml = BeautifulSoup(page).get_text()
tokens = nltk.word_tokenize(nohtml)
print(tokens)
