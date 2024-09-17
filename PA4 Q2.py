#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[78]:


board2 = pd.read_csv('board2.csv')
board2


# In[80]:


#2
nyv = pd.DataFrame(board2, columns = ['Name','Gender','Track','Hometown','Math','Electronics','GEAS','Communication'])
nyv['Average'] = nyv[['Math', 'Electronics', 'GEAS', 'Communication']].mean(axis=1)
#Plot 1
plt.figure(figsize=(14, 6))
plt.subplot(1, 3, 1)
sns.boxplot(x='Track', y='Average', data=nyv)
plt.title('Average Score by Track')
plt.xticks(rotation=45)
#Plot 2
plt.subplot(1, 3, 2)
sns.boxplot(x='Gender', y='Average', data=nyv)
plt.title('Average Score by Gender')
#Plot 3
plt.subplot(1, 3, 3)
sns.boxplot(x='Hometown', y='Average', data=nyv)
plt.title('Average Score by Hometown')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#Plot 4
sns.pairplot(nyv[['Math', 'Electronics', 'GEAS', 'Communication', 'Average']])
plt.suptitle('Pair Plot of Subjects vs. Average', y=1.03)
plt.show()
#Plot 5
corr = nyv[['Math', 'Electronics', 'GEAS', 'Communication', 'Average']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()


# In[ ]:




