from   __future__  import print_function, division

# a = 1
# f = 1.2
# print("a=", a)
# 
# if a == 1:
#     print("Equal")
#     print("Another line")
#     print("third line")
# elif f < 1:
#     print("f is lower")
# else:
#     print("this is else")
#     print("OK")
    
# if name is "XYZ" 
# and age is below 40, 
# print "suitable" 
# else if age is greater
# than 50, print "old", 
# else print "OK"
# For all other names, 
# print "not known" 
from   __future__  import print_function, division
#name = input("Give Name: ") #raw_input for Python2.7.x
##age_s = input("Give Age: ")
#age = int(input("Give Age: "))
import sys 
#print(sys.argv)  #['first.py', 'XYZ', '20'] 
name = sys.argv[1] if len(sys.argv) >=2 else "XYZ"
age = int(sys.argv[2] if len(sys.argv) >=3 else "30")
#X if Y else Z  ==> If Y is true, then do X else do Z
if name == "XYZ":
    if age < 40:
        print("suitable")
    elif age > 50:
        print("old")
    else:
        print("OK")
else:
    print("not known")



