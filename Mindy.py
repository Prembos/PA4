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


#b(data frames)
Mindy = pd.DataFrame(board2, columns = ['Name','Track','Math','Electronics','GEAS','Communication','Hometown','Gender'])
Mindy['Average'] = Mindy[['Math', 'Electronics', 'GEAS', 'Communication']].mean(axis=1)
Mindy.loc[(Mindy['Average']>=55)&(Mindy['Hometown']=='Mindanao')&(Mindy['Gender']=='Female')]


# In[8]:


#b(visuals)
Mindy['Average'] = Mindy[['Math', 'Electronics', 'GEAS', 'Communication']].mean(axis=1)
Mindy_visuals = Mindy.loc[(Mindy['Average']>=55)&(Mindy['Hometown']=='Mindanao')&(Mindy['Gender']=='Female')]
plt.figure(figsize=(10, 6))
plt.bar(Mindy_visuals['Name'], Mindy_visuals['Average'])
plt.xlabel('Name')
plt.ylabel('Average')
plt.title('Average Scores for Female Students from Mindanao with Average >= 55')
plt.xticks(rotation=45)
plt.show()


# In[ ]:




