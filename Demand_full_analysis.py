#!/usr/bin/env python
# coding: utf-8

# # Descriptive Analysis

# #importing library

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


demnd_df = pd.read_excel('Demand_Full Data_data_Raw_Data.xlsx', sheet_name = 'Cleaned', header=0, index_col=None)
demnd_df.head()


# In[3]:


demnd_df.describe()


# In[4]:


demnd_df.info()


# #Changing the datatypes of Date - date, Hourly profile - string, Season - string
# # demnd_df['Date'] = demnd_df['Date'].astype('datetime64')
# # demnd_df['Date']
# 

# # 1. Are there noticeable trends in energy consumption over the years?

# In[5]:


demnd_df.head(13)


# In[15]:


demnd_df.tail()


# In[6]:


demnd_df.iloc[12]


# In[7]:


demnd_df['Date'] = pd.to_datetime(demnd_df['Date'], errors='coerce')


# In[8]:


demnd_df.info()


# In[9]:


demnd_df.set_index('Date',inplace=True)


# In[10]:


demnd_df_numeric = demnd_df.apply(pd.to_numeric, errors='ignore')


# In[13]:


annual_energy_consumption = demnd_df_numeric.resample('Date')


# In[ ]:




