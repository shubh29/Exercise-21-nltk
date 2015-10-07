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

def fetchContents(url):
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

fetchContents("http://money.cnn.com/data/dow30/")

def writeToTextFile():
    print('Creating a new text file\n')
    #Name of text file coerced with .txt
    textFileName = input('Enter name of text file: ') + '.txt'
    
    try:
        print('\nWriting to the text file..\n')
        #Trying to create a new file or open one
        writeToTextFile = open(textFileName, "w")
        writeToTextFile.write(str(tokens))
        writeToTextFile.close()
        print('File writing completed!\n')
    except:
        print('Something went wrong while writing to the file!')
        #quit python
        sys.exit(0)
writeToTextFile()

def generatebigrams():
    pairs = nltk.bigrams(tokens)
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    finder = nltk.collocations.BigramCollocationFinder.from_words(pairs)
    finder.apply_freq_filter(3)
    forprint = finder.nbest(bigram_measures.pmi, 10)
    print(forprint)
generatebigrams()


