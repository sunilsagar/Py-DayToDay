s5 = "Name:ABC,age=20;Name=XYZ,age=40"
#output = "Name:ABC,age=22;Name=XYZ,age=42"
import re
#1. Split s5 with ;
s6 = s5.split(";")
o = []
#2. For each segment 
for segment in s6: #Loop1: segment --> Name:ABC,age=20
    #3. Use regex r"age=(\d+) and re.findall 
    age = re.findall(r"age=(\d+)", segment) # Loop1: ['20']
    #4. Increase the result by 2 
    tmp2 = int(age[0]) + 2  #Loop1: 22
    tmp3 = re.sub(age[0], str(tmp2), segment)
    #5. Create a new list and append above result
    o.append(tmp3)
#6. Use str.join on above list ie join with ; seperator 
output = ";".join(o)
print(output)