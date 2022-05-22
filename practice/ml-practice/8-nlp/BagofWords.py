# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 21:14:44 2020

@author: pandey
"""
import os 
loc = 'G:\\ML-in-Practice\\MLInPractice\\MLAlgorithm\\NLP'
if os.getcwd() == loc:
    pass
else:
    os.chdir(loc)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy

dataset = pd.read_csv('Restaurant_reviews.tsv',delimiter ='\t', quoting=3) # quptations ignore

# Cleaning the text
import re # regular expressions 
firstreview = re.sub('[^a-zA-Z ]',' ',dataset['Review'][0] ) # remove everything except a-z and A-Z i.e keep only letters
# Doing it initialy for first review 
# We keep a space so that the removed character is replaced by a space ' '
# 'Wow    Loved this place '

firstreview = firstreview.lower()
# changing all text to lower case

import nltk
nltk.download('stopwords') # downloaded and updated the list of unimportant words 
firstreview = firstreview.split()
from nltk.corpus import stopwords
firstreview = [word for word in firstreview if not word in set(stopwords.words('english'))]
#firstreview = [word for word in firstreview if word not in stopwords.words('english')]
# Also we want unique words and want to remove duplicate words so better we create a set
# Also sets are faster then list
# removing the non significant words, prepositions, articles etc. 

from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()
firstreview = [ps.stem(word) for word in firstreview]
# This was Stemming. In Stemming we keep the root words, change tensed to root words
# we perform stemming on word not on list so it has to be done in an iterable mannner
# We could have directly used it during previous operation.

firstreview = ' '.join(firstreview)
# It Returned : 'wow love place'
# We Started with 'Wow... loved this place.!!'

"""

###########     Lets do the editing for the entire list
""" 

corpus = []
for i in range(1,1000):
    firstreview = re.sub('[^a-zA-Z ]',' ',dataset['Review'][i] )
    firstreview = firstreview.lower()
    firstreview = firstreview.split()
    firstreview = [ps.stem(word) for word in firstreview if not word in set(stopwords.words('english'))]
    firstreview = ' '.join(firstreview)
    corpus.append(firstreview)
    
    
# Bag of words is where all the unique words form the columns and rows tell whether that nth row has that
# word or not. so number of same words can tell what type of review how many customers has given.
# Basically we try and create a sparse matri
    
    
    
    
    
    