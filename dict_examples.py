s = "Hello World Hello Earth Hello Everyone"

s2 = s.split() 
#Create an empty dict, output 
output = {}
#Take each word(wd) from s after spliting 
for wd in s2:
    #if wd exists in empty dict, output 
    if wd in output:
        #increment wd's value 
        output[wd] = output[wd] + 1
    else:
        #create wd as key with value as 1
        output[wd] = 1
#print that dict, output 
print(output)

##Open Iris CSV 
f = open(r"D:\handson\data\iris.csv", "rt")
lines = f.readlines()
f.close()
##Unique Names
rows = lines[1:]
out = set()
for e in rows:
    out.add( e.strip().split(",")[-1] )
print(len(out))
#iris["Name"].unique()


#What min SepalLength for each Name 
# output = dict , key=Name, value would be min
#'SepalLength,SepalWidth,PetalLength,PetalWidth,Name\n'
#'5.1,3.5,1.4,0.2,Iris-setosa\n'
output = {}
for name in out:   #name eg Iris-setosa
    el =[]
    for e in rows:
        columns = e.strip().split(",")
        if columns[-1] == name:
            el.append( float(columns[0]) )
    output[name] = min(el)
#{'Iris-setosa': 4.3, 'Iris-versicolor': 4.9, 'Iris-virginica': 4.9}
#iris.groupby('Name').agg({'SepalLength':'min'})
                 SepalLength
Name
Iris-setosa              4.3
Iris-versicolor          4.9
Iris-virginica           4.9

>>> #What min SepalLength for each Name
name = 'Iris-setosa'
#'SepalLength,SepalWidth,PetalLength,PetalWidth,Name\n'
el = []
e = '5.1,3.5,1.4,0.2,Iris-setosa\n'
e.strip().split(",")[0]
if e.strip().split(",")[-1] == name:
    print( float(e.strip().split(",")[0]) )

for e in rows:
    if e.strip().split(",")[-1] == name:
            el.append( float(e.strip().split(",")[0]) )

output = {}
for name in out:
    el = []
    for e in rows:
        columns = e.strip().split(",")
        if columns[-1] == name:
            el.append( float(columns[0]) )
    output[name] = min (el)

>>> output
{'Iris-setosa': 4.3, 'Iris-versicolor': 4.9, 'Iris-virginica': 4.9}

##DB API 
with open(r"D:\handson\data\iris.csv", "rt") as f:
    lines = f.readlines()

rowsd = []
for e in lines[1:]:
    columns = e.strip().split(",")
    rowsd.append( [float(columns[0]), float(columns[1]), 
        float(columns[2]),float(columns[3]),columns[4]] )
 
#DB API 
import sqlite3 
con = sqlite3.connect("iris.db")
cur = con.cursor()
cur.execute(""" create table IF NOT EXISTS iris (sl double, 
    sw double, pl double, pw double, name string)""")
for r in rowsd:
    cur.execute("""insert into iris values(?,?,?,?,?)""", r)

con.commit()
q = cur.execute("""select name, min(sl) from iris group by name""")
res = list(q.fetchall())
print(res)
#[('Iris-setosa', 4.3), ('Iris-versicolor', 4.9), ('Iris-virginica', 4.9)]

##Rest Automation 
#Low level API 
import json, urllib.request  #py3 for p
url = "http://httpbin.org/get"
web = urllib.request.urlopen(url)
data = web.read()
obj = json.loads(data.decode('utf-8'))

#High level API
import requests
r = requests.get(url)
obj = r.json() # Json Ends here, now you have to extract components 
txt = r.text
import xml.etree.ElementTree as ET
tr = ET.fromstring(txt)
root = tr.getroot() #Now extract 

##Builtin libs 
import math
dir(math)
math.sqrt(2)
import time
dir(time)
time.sleep(1)
import datetime
dir(datetime)
datetime.date(2020,8,19)
datetime.date(2020,8,19) + datetime.timedelta(days=365)
import sys
dir(sys)
print("OK")
sys.stdout.write("OK")
import os
dir(os)
import os.path
dir(os.path)
os.path.abspath(os.curdir)

















