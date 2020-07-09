# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 12:02:36 2020

@author: Patrick
"""

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from os import path
import pandas as pd
import numpy as np

f = open('pre_quality_papers.txt', 'r', encoding='utf-8')
text = f.read()
f.close()

text = text.lower()

STOPWORDS.update( ['said', 'will', 'BST', 'blocktime', '2020', 'new', 'one',
                   'says', 'publishedtime', 'april', 'may', 'march', 'first',
                   'week', 'last', 'two', 'told', 'day', '•', 'back', 'going', 
                   'including', 'updatedtimeupdated', 'make', 'weeks', 'around', 
                   'take', 'still', 'made', 'go', 'across', 'days', 'per', 
                   'know', 'way', 'year', 'new', 'gmt', 'three', 'rights', 
                   'copyright', 'length','words','byline', 'updatedtimeupdated',
                   'february','document', 'dont', 'reserved', 'loaddate'] )


punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
no_punct = ""
for char in text:
    if char not in punctuations:
        no_punct = no_punct + char
        
text = no_punct

query = text
stopwords = STOPWORDS
querywords = query.split()
resultwords = [word for word in querywords if word.lower() not in stopwords]

df = pd.DataFrame(resultwords, columns = ['words'])
freqs =  df.words.value_counts()

text = ' '.join(resultwords)

wordcloud = WordCloud(max_words=100).generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig("Pre quality")
plt.show()