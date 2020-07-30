# if name is "XYZ" 
# and age is below 40, 
# print "suitable" 
# else if age is greater
# than 50, print "old", 
# else print "OK"
# For all other names, 
# print "not known" 

#name = input("Give name: ") # raw_input 
import sys 
name = sys.argv[1] if len(sys.argv) >=2 else "XYZ"

s_age = input("Give age: ") 
age = int(s_age)

if name == "XYZ":
    if age < 40 :
        print("suitable")
    elif age > 50:
        print("old")
    else:
        print("OK")
else:
    print("not known")