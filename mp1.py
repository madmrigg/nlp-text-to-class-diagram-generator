# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 11:35:42 2019

@author: Marlom_Bey
"""

"""
    reading the input, tokenizing the words, extracting the parts of speech
"""


import nltk 
#from nltk.parse.corenlp import CoreNLPParser

text = "A system shall allow the users to register by entering their username and password, In order to get an access to the system";
n_list = []

#print(text)
#print(type(text))

tokens = nltk.word_tokenize(text)
#print(tokens)

pos = nltk.pos_tag(tokens)
#print(pos)

for p in pos:
    print(p)
    #q = ''.join(p)
    
    if "VB" in p:
        #verb = q.replace("VB","")
        n_list.append(p)
    elif "NN" in p:
        #noun = q.replace("NN","")
        n_list.append(p)
    elif "NNP" in p:
        #nounp = q.replace("NNP","")
        n_list.append(p)
    elif "NNS" in p:
        n_list.append(p)

print("List: ", n_list)
print("List: ", list(dict.fromkeys(n_list)))
