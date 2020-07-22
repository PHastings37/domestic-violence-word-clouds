# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 14:04:46 2020

@author: Patrick
"""

def isLineEmpty(entry):
    return len(line.strip()) == 0


from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import string

f = open('TextFiles\post_all_papers.txt', 'r', encoding='utf-8')
text = f.read()
f.close()
linesFinal = []
papers = []

articles = text.split('End of Document', -1)
articles.pop()

for i in range(len(articles)):    
    lines = articles[i].splitlines()  
    for line in lines:
        if not isLineEmpty(line):
            linesFinal.append(line)
    papers.append(linesFinal[1])
    linesFinal.clear()
    
d = {'Paper':papers, 'Articles':articles}
df = pd.DataFrame(data=d)

    
    
