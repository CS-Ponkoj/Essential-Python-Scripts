# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 00:44:09 2021

@author: csponkoj
"""
!pip install wikipedia


import wikipedia

print("Welcome to the app which find an answer to your question from wikipedia")

while True:
    ques = input("Ask a question or query?")
    wikipedia.set_lang("en") #change "en" to convenient language for example wikipedia.set_lang("es") will set the language to spanish
    print (wikipedia.summary(ques, sentences=3))
