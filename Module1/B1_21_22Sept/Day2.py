#!/usr/bin/env python
# coding: utf-8

# **Daily attendance of bike tracks**
# 
# *every row contains the number of bicycles on every track of the city(montreal), 
# for every day of the year*
# 
# url = "https://raw.githubusercontent.com/ndas1971/Misc/master/bikes.csv"
# 
# 1. Read 
# 2. Check head 
# 3. Check summary statistics 
# 4. plot the daily attendance of two tracks, 'Berri1', 'PierDup'
# 5. Check index , explore weekday attributes 
# 6. Get sum of all attendance as a function of the weekday
# 7. Display this in figure , what is the inference?

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


url = "https://raw.githubusercontent.com/ndas1971/Misc/master/bikes.csv"
df = pd.read_csv(url, index_col='Date', parse_dates=True, dayfirst=True)


# In[31]:


#2
df.head()

#3
df.describe()


# In[13]:


#4
df[ ['Berri1', 'PierDup']].plot(figsize=(10,6), style=['--','-'], lw=2)

df.index.weekday #Monday=0, Sunday=6

#5,6
df_week = df.groupby(df.index.weekday).sum()
df_week.head()

fig,ax = plt.subplots(1,1, figsize=(8,8))
df_week.plot(kind='bar', style='-o', lw=3, ax=ax)
ax.set_xlabel("Weekday")
ax.set_xticklabels('Mon,Tue,Wed,Thur,Fri,Sat,Sun'.split(","))
ax.set_ylim(0)


# In[15]:


#display all tracks together (stacked or area plot)?
fig,ax = plt.subplots(1,1, figsize=(8,8))
df_week.plot.bar(stacked=True, ax=ax)
ax.set_xlabel("Weekday")
ax.set_xticklabels('Mon,Tue,Wed,Thur,Fri,Sat,Sun'.split(","))


# B. **Titanic-https://www.kaggle.com/c/titanic/data** 
# 
# *Database of whether somebody survived or not*
# 
# 1. Load the data
# 2. Which gender survived more 
# 3. Does it depend on pclass?
# 4. can we see % of survival of each gender and pclass 
# What is your inference? 

# In[16]:


path = 'data/titanic_train.csv'
tt = pd.read_csv(path)


# In[29]:


tt.head()
tt.groupby('sex')['survived'].value_counts()

tt.pclass.unique()
tt.groupby(['pclass', 'sex']).survived.value_counts()


# In[28]:


id = pd.crosstab([tt.pclass, tt.sex], tt.survived.astype(float))
id
id.sum(axis=1)
id.div(id.sum(axis=1).astype(float),0)


# In[30]:


tt.index


# C. **Roger Federer database **
# 
# *Each row corresponds to a ATP match played by Roger Federer*
# 
# player = 'Roger Federer'
# url = "https://raw.githubusercontent.com/ndas1971/Misc/master/federer.csv"
# 
# 1. Read and check data 
# 2. How many % of matched won by our player? ('winner')
# 3. Proportion of double faults wrt total points in each match 
# This number is an indicator of the player's state of mind, his level of self-confidence, 
# his willingness to take risks while serving, and other parameters.
# columns:
# 'player1 double faults' and 'player1 total points total'
# Display simple stats of above 
# 4. Average Win per surface 
# 5. Display the proportion of double faults as a function of the tournament date, 'start date'
# Trend: display average double faults in each year 

# In[ ]:




