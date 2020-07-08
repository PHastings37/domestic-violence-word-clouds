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

#STOPWORDS.update( ['said'] )

query = text
stopwords = STOPWORDS
querywords = query.split()
resultwords = [word for word in querywords if word.lower() not in stopwords]

df = pd.DataFrame(resultwords, columns = ['words'])


text = ' '.join(resultwords)

wordcloud = WordCloud().generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()