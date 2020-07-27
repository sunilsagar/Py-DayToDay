# if name is "XYZ" 
# and age is below 40, 
# print "suitable" 
# else if age is greater
# than 50, print "old", 
# else print "OK"
# For all other names, 
# print "not known" 

name = input("Give name: ") # raw_input 
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