#!/usr/bin/env python
# coding: utf-8

# # IMP: STEPS to be followed 
# 
# https://github.com/ndas1971/ScalaQs/blob/master/winutils.exe
# 
# delete in windows file exploler d:\tmp
# 
# mkdir d:\tmp
# 
# cd d:\tmp
# 
# mkdir hive
# 
# winutils.exe chmod -R 777 D:/tmp
# 
# 
# Then Use commandline
# 
# d:>handson\pyspark

# In[3]:


spark


# In[2]:


spark.sparkContext.getConf().getAll()


# In[4]:


from pyspark.sql import *
import pyspark.sql.functions as F

file = 'data/spark/Cartier+for+WinnersCurse.csv'
acs = spark.read.format('csv').option('header', 'true')        .option('inferSchema', 'true').load(file)

acs.show()
print(len(dir(acs)), len(dir(F)), len(dir(F.col("bidder"))))


# In[10]:


#basic 
acs.columns
acs.dtypes
acs.printSchema()


# In[19]:


#Note .show() or .collect() is must to either display or collect the data in driver
#filter based whether bidder contains 'o'
acs.filter(F.col("bidder").contains('o'))
#OR 
acs.filter(acs.bidder.contains('o'))
#OR
acs.filter(acs['bidder'].contains('o'))

#Select few columns 
acs.filter(acs['bidder'].contains('o'))   .select("auctionid", "bidder").show()


# In[28]:


acs.select("auctionid", 'bid').where("bid >= 1000")
#Create a new column 
df3 = acs.withColumn("new_price", F.col("price")* 2)
#df3.show()

#aggregations for full table
acs.agg(F.max('bid'), F.count('bidder')) #.show()
#per auctionId 
df4 = acs.groupBy('auctionid').agg(F.max('bid').alias("mb"), F.count('bidder').alias("cb"))                    .select("auctionid", "mb", "cb")
df4.toPandas()


# In[ ]:




