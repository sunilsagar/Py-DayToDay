#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World")


# In[2]:


2 + 2


# In[3]:


get_ipython().system('dir')


# In[4]:


get_ipython().run_line_magic('lsmagic', '')


# In[6]:


get_ipython().run_line_magic('pwd', '')


# In[7]:


get_ipython().run_cell_magic('writefile', 'test1.txt', 'Hello World!')


# In[8]:


with open("test1.txt", 'r') as f:
    print(f.read())


# # Python referesher

# In[9]:


a = 1
f = 1.2
b = True
s = "OK"  
s1 = 'OK' #single quote or double quote
#s[0] = 'K' #Error as immutable 
lst = [1,2,3,4] # duplicates-P, indexing-P, Insertion ordered- P
lst[0] = 20 #mutable
print(lst)
t = (1,2)
#t[0] = 1 #Error as immutable 
st = {1,2} #duplicates-NP, indexing-NP, Insertion ordered- NP
ed = { 'ok' : 2, 'nok': 3}


# In[24]:


#length
print(len(s), len(lst), len(t), len(st), len(ed))

#containment checking
print('O' in s, 1 in lst, 1 in t, 3 not in st, 'ok' in ed)

#indexing
print(s[0], lst[-1], t[0]) # NP for set, dict

#adding some element 
lst.append("OK")
st.add(1.2)
ed['new'] = [1,2,3]
print(lst, st, ed)


# In[27]:


#concatenation
s2 = s + " Hello"
lst2 = lst + [30,20]
t2 = t + (3,4)
#set and dict 

#iteration 
for e in st:
    print(e)
for e in lst:
    print(e)
for e in st:
    print(e)
for k in ed:
    print(k, ed[k])


# In[39]:


d = {'ok': 2, 'nok': 3}
c = 0
while c < 3:
    d = {'ok': [d]}
    c += 1
print(d)

print(type(d))
print(d.keys())

d['ok'][0]['ok'][0]['ok'][0]['ok'] = 20
print(d)


# In[40]:


import pprint
pprint.pprint(d)


# # Installing module

# In[46]:


get_ipython().system('pip install requests ')

import requests
r = requests.get("http://httpbin.org/get")
obj = r.json()
obj['origin']


# In[61]:


get_ipython().run_cell_magic('writefile', 'mex.py', 'def my_add(x,y):\n    return x-y\n\ndef my_add2(x, y=20):\n    return x+y')


# In[ ]:


import mex

print(mex.my_add(2,3), #positional based arg passing
mex.my_add(y=3,x=20), #keyword based arg passing
mex.my_add(20, y=30), #constraint: positional comes first 
mex.my_add2(20),
mex.my_add2(20,30))


# In[63]:


import importlib
importlib.reload(mex)


# In[ ]:


help(mex1.my_add)


# In[62]:


dir(str)
help(str.split)


# # numpy introduction

# In[64]:


import random
import numpy as np


# In[65]:


#create
n = 10000
x = [random.random() for _ in range(n)]
y = []
for _ in range(n):
    y.append(random.random())

#check
x[:3], y[0:3] #slicing start:end:step

z = [x[i] + y[i] for i in range(n)]
z[:3]

get_ipython().run_line_magic('timeit', '[x[i] + y[i] for i in range(n)]')


# In[70]:


#numpy
xa = np.array(x)
ya = np.array(y)
z = xa + ya 
z[:3]
get_ipython().run_line_magic('timeit', 'xa + ya')


# In[74]:


#create
x = np.array([1,2,3])
y = np.linspace(2.0, 3.0, num=3)
z = np.arange(12).reshape(2,6)
ru = np.random.random( (2,6) )
rn = np.random.normal(0,1 , (6,4)) #mu, sigma 


# In[80]:


z
z.ndim, z.shape # mostly - rowise = axis=1, colwise , axis=0
np.sum(z, axis=0) #axis=0, columnwise
np.sum(z, axis=1) #axis=1, rowwise sum 


# In[81]:


print("# of methods in numpy", len(dir(np)), "# of methods in np.random", len(dir(np.random)))


# In[82]:


z1 = np.arange(50).reshape( 5,5,2)

np.arange(50).shape


# In[87]:


#Accessing numpy
x[0]
x[0] = 1
print(x)
#2D accesing
z[0,0]
z[0,0] = 2
z[: , 0:2] #sub array syntax 
z[z>2] #boolean accessing syntax 
z[ (z>2) & (z<4)] # & | not 


# In[93]:


#how do you print first row, all columns?
z[0, :]


# In[96]:


#How to introduce dummy dimension
y.reshape(1,3)
y.reshape(3,1)

y[:, None], y[None, :]


# In[99]:


#Operations 
y1 = y.reshape(3,1)

xx = x - x 
zz = z * z
print(zz)


# In[104]:


y.shape, y1.shape
yy = y + y1 #np.tile(y, (3,1)) + np.tile(y1, (1,3))
print(yy) 


# In[111]:


#Stacking
a = np.array([1,2,3])
b = np.array([20,30,40])
np.vstack( (a,b))


# In[112]:


np.hstack( (a,b) )


# In[113]:


np.c_[a,b]


# In[114]:


get_ipython().run_line_magic('run', 'demo_code/0.1.numpy_operations.py')


# ## HandsOn
# Compute ```y = 1-sin(x)/x```  for x = -20, ... +20 (take 1000 data points)

# In[118]:


x = np.linspace(-20.0 , 20.0, 1000)
def f(x):
    return 1 - np.sin(x)/x  #np.info(np.sin)

y = f(x)


# In[126]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

fig, ax = plt.subplots(1,1,figsize=(5,5)) #rows x cols
ax.plot(x,y)
print(len(dir(plt))) # no of methods
fig.savefig("first.png")


# In[134]:


x0 = np.array([0])
f(x0)


# In[135]:


import scipy.optimize as opt
x0 = 3
xmin = opt.minimize(f, x0).x
print(xmin, f(xmin))


# In[136]:


# draw 
fig, ax = plt.subplots(1,1,figsize=(5,5)) #rows x cols
ax.plot(x,y)
ax.scatter(x0, f(x0), marker='o', s=300)
ax.scatter(xmin, f(xmin), marker='v', s =300, zorder=300)
ax.set_xlim(-20,20)


# In[142]:


t = np.arange(0.0, 5.0, 0.2) #step=0.2
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2) #rows x cols
fig.suptitle('multiplot', fontsize=16)
ax1.plot(t, t, "r-")
ax2.scatter(t, t**2, color='b')
ax3.plot(t, t, "r-")
ax4.scatter(t, t**2, color='b', linewidth=2.0)
ax1.set_title("Straight line")
ax2.set_xlabel('x axis')
ax2.set_ylabel('y axis')
ax2.legend(['Square'])
# fig,  axs = plt.subplots(2,2)
# axs[0,0].plot(t, t, "r-")
# ax[0,1].scatter(t, t**2, color='b')
# ax[1,0].plot(t, t, "r-")
# ax[1,1].scatter(t, t**2, color='b')


# In[143]:


get_ipython().run_line_magic('run', 'demo_code/0.2.plt_3dr_plot.py')


# # Pandas introduction

# In[144]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[169]:


iris = pd.read_csv("data/iris.csv") #pd.DataFrame

iris.head() #display head 
iris.columns
iris.dtypes
len(iris) #how many rows 
#Access one or many columns 
names = iris['Name'] # or iris.Name -> pd.Series
np.unique(names)
len(dir(names)), len(dir(iris)), len(dir(pd))  # # of methods of Series, DF

#Further Accessing
iris[ ['SepalLength', 'PetalLength'] ] #multiple columns -> Pd.DataFrame
iris.loc[0:2, 'SepalLength'] #index, column, index starts from 0, end inclusive
#boolean accessing 
iris.loc[iris.Name == 'Iris-setosa', :]

#what is the mini SepalLength for each Name 
iris.groupby('Name').agg({'SepalLength' : ['min', 'max'],
                          'PetalLength' : np.std})
#summary stats
iris.describe()

#plotting
iris[['SepalLength', 'PetalLength']].plot(kind='line')


# In[ ]:




