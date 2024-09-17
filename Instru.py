#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


board2 = pd.read_csv('board2.csv')
board2


# In[6]:


#a(data frames)
Instru = pd.DataFrame(board2, columns = ['Name','GEAS','Electronics','Track','Hometown'])
Instru.loc[(Instru['Electronics']>70)&(Instru['Track']=='Instrumentation')&(Instru['Hometown']=='Luzon')]


# In[10]:


#a(visuals)
Instru_visuals = Instru.loc[(Instru['Electronics']>70)&(Instru['Track']=='Instrumentation')&(Instru['Hometown']=='Luzon')]
plt.figure(figsize=(10, 6))
plt.bar(Instru_visuals['Name'], Instru_visuals['Electronics'])
plt.xlabel('Name')
plt.ylabel('Electronics Score')
plt.title('Electronics Scores of Instrumentation Students from Luzon')
plt.xticks(rotation=45)
plt.show()

