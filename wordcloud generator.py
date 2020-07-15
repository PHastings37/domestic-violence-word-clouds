# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 12:02:36 2020

@author: Patrick
"""

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import string

f = open('TextFiles\pre_right_papers.txt', 'r', encoding='utf-8')
text = f.read()
f.close()

text = text.lower()
text = text.translate(str.maketrans('', '', string.punctuation))
text = text.translate(str.maketrans('', '', string.digits))

STOPWORDS.update( ['said', 'will', 'BST', 'blocktime', '2020', 'new', 'one',
                   'says', 'publishedtime', 'april', 'may', 'march', 'first',
                   'week', 'last', 'two', 'told', 'day', '•', 'back', 'going', 
                   'including', 'updatedtimeupdated', 'make', 'weeks', 'around', 
                   'take', 'still', 'made', 'go', 'across', 'days', 'per', 
                   'know', 'way', 'year', 'new', 'gmt', 'three', 'rights', 
                   'copyright', 'length','words','byline', 'updatedtimeupdated',
                   'february','document', 'dont', 'reserved', 'loaddate', 
                   'updated', 'timeupdated', 'published', 'bst', 'published-time',
                   'time', 'block', 'date', 'end', 'section', 'date', 'load'
                   'version', 'newspapers', 'ltd', 'associated', 'articles',
                   'co', 'pg', 'version length', 'co uk', '£', 'thing', 'pm',
                   'section news', 'word', 'independent', 'added', 'even', 
                   'month', 'mr', 'edition', 'media', 'mirror', 'plc',
                   'really', 'things', 'didnt', 'im', 'news group', 'every'
                   'june', 'times', 'january', 'mailonline', 'yearold', 
                   'daily mail'] )

query = text
stopwords = STOPWORDS
querywords = query.split()
resultwords = [word for word in querywords if word.lower() not in stopwords]

df = pd.DataFrame(resultwords, columns = ['words'])
freqs =  df.words.value_counts()

text = ' '.join(resultwords)

wordcloud = WordCloud(max_words=100, background_color="white").generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig("Graphics\PreRight")
plt.show()

freqs.to_csv('FrequencyTables\PreRight.csv', index=True)
    
    
                 
    
    