# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 22:00:47 2019

@author: Marlom_Bey
"""

import nltk

"""
    format:  
"""
text = "An ordering system. Customer can provide their name, address, phone. Customer can register, edit profile, delete profile."
n_list = []

tokens = nltk.word_tokenize(text)
print(tokens)

pos = nltk.pos_tag(tokens)
print(pos)

for p in pos:
    
    temp = ''.join(p)
    
    if "NN" in p:
        n_list.append(temp.replace("NN",""))
    elif "NNP" in p:
        n_list.append(temp.replace("NNP",""))
    elif "." in p:
        n_list.append(".")
        
print(n_list)
