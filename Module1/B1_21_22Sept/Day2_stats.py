#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[4]:


iris = pd.read_csv('data/iris.csv')
iris.iloc[:, 0:4].plot.box()

iris.boxplot(by='Name')


# In[7]:


get_ipython().run_line_magic('run', 'demo_code/1.2.Gaussian_distributions.py')


# In[8]:


iris.head()


# A car manufacturer claims that no more than 10% of their cars are unsafe.
# 15 cars are inspected for safety, 3 were found to be unsafe. Test the
# manufacturer's claim:

# In[9]:


from scipy import stats


# In[10]:


stats.binom_test(3, n=15, p=.1, alternative='greater')


# # pyspark kernels

# In[11]:


get_ipython().system('jupyter kernelspec list')


# In[13]:


get_ipython().run_line_magic('pycat', 'C:\\Anaconda3\\envs\\aiml\\share\\jupyter\\kernels\\PySparkAuto\\kernel.json')


# In[ ]:




