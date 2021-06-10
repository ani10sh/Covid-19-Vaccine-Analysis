#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Importing Libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


data = pd.read_csv('country_vaccinations.csv')


# In[5]:


data.head()


# In[7]:


data.columns


# In[8]:


#Exploring the data 


# In[9]:


data.describe()


# In[10]:


data.info()


# In[12]:


pd.to_datetime(data.date)
data.country.value_counts()


# In[24]:


#since UK is made up of England, Scotland, Wales, and Ireland we cannot have the same values twice and we need to exclude them:


# In[25]:


data = data[data.country.apply(lambda x: x not in ["England", "Scotland", "Wales", "Northern Ireland"])]
data.country.value_counts()


# In[26]:


data.vaccines.value_counts()


# In[27]:


# New DataFrame by only selecting the vaccine and the country columns to explore which vaccine is taken by which country


# In[29]:


df = data[['vaccines','country']]
df.head()


# In[33]:


# Determining which countries are taking which Vaccines :

dict_ = {}
for i in df.vaccines.unique():
    dict_[i] = [df['country'][j] for j in df[df['vaccines'] == i].index]

vaccines = {}
for key, value in dict_.items():
    vaccines[key] = set(value)
for i, j in vaccines.items():
    print(f'{i}:>>>>  {j}\n')


# In[36]:


# visualizing this data to have a look at what combination of vaccines every country is using:
import plotly.express as px
import plotly.offline as py

vaccine_map = px.choropleth(data, locations='iso_code', color='vaccines')
vaccine_map.update_layout(height=300, margin={"r": 0, "t": 0, "l": 0, "b": 0})
vaccine_map.show()


# In[ ]:




