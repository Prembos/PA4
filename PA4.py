#!/usr/bin/env python
# coding: utf-8

# In[83]:


import pandas as pd
import matplotlib.pyplot as plt


# In[20]:


board2 = pd.read_csv('board2.csv')


# In[22]:


board2


# In[78]:


#EXAMPLE
Vis = pd.DataFrame(board2, columns = ['Name','Gender','Track','Hometown','Math'])
Vis.loc[(Vis['Math']<70)&(Vis['Hometown']=='Visayas')]


# In[76]:


#a(data frames)
Instru = pd.DataFrame(board2, columns = ['Name','GEAS','Electronics','Track','Hometown'])
Instru.loc[(Instru['Electronics']>70)&(Instru['Track']=='Instrumentation')&(Instru['Hometown']=='Luzon')]


# In[99]:


#a(visuals)
Instru_visuals = Instru.loc[(Instru['Electronics'] > 70) & (Instru['Track'] == 'Instrumentation') & (Instru['Hometown'] == 'Luzon')]
plt.figure(figsize=(10, 6))
plt.bar(Instru_visuals['Name'], Instru_visuals['Electronics'])
plt.xlabel('Name')
plt.ylabel('Electronics Score')
plt.title('Electronics Scores of Instrumentation Students from Luzon')
plt.xticks(rotation=45)
plt.show()


# In[93]:


#b(data frames)
Mindy = pd.DataFrame(board2, columns = ['Name','Track','Math','Electronics','GEAS','Communication','Hometown','Gender'])
Mindy.loc[(Mindy['Math']>=55)&(Mindy['Electronics']>=55)&(Mindy['GEAS']>=55)&(Mindy['Communication']>=55)&(Mindy['Hometown']=='Mindanao')&(Mindy['Gender']=='Female')]


# In[ ]:


#b(visuals)

