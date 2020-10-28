#!/usr/bin/env python
# coding: utf-8

# In[4]:


file=open("covid19_tweets.csv","r")
import pandas as pd
data=pd.read_csv("covid19_tweets.csv")
data.head()
#data.tail()


# In[6]:


import numpy as np
data.describe(include=np.object).transpose()


# In[11]:


data.describe()


# In[12]:


data.describe(columns)


# In[ ]:




