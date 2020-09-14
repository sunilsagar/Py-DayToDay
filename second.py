# if name is "XYZ" and age is below 40, 
# print "suitable" else if age is greater
# than 50, print "old", else print "OK"
# For all other names, print "not known" 

#name = "ABC"
name = input("Give Name:")
#age_1 = input("Give Age:")
age = int(input("Give Age:"))
if name == "XYZ":
    if age < 40:
        print("suitable")
    elif age > 50:
        print("old")
    else:
        print("OK")
else:
    print("not known")
print("END")   
