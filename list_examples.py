
lsw = [ "OK", "NOK", "O"]
#convert this to below output 
#output = [ 2, 3, 1]
#output = [ 4 ]

#Create empty list(output)
output = []
#Take each element of lsw 
for e in lsw:
    #find the length of the element and append to the empty list 
    if len(e) % 2 == 0:
        output.append( len(e) * len(e) )
    
print(output)

ls = "[1,2,3,4]"         #-> [ "1", "2", "3", "4"] 
output = [1,2,3,4]

#strip ls with "[]" and split with "," then store to ls2 variable 
ls1 = ls.strip("[]")
lst2 = ls1.split(",") #-> [ "1", "2", "3", "4"] 
#Create empty list, output 
output = []
#Take each element from ls2 
for e in ls2:
    #convert to int and append to empty list, output 
    output.append( int(e) )
    
print(output)

#Create empty list, output 
output = []
#Take each element from ls2 
for e in ls.strip("[]").split(","):
    #convert to int and append to empty list, output 
    output.append( int(e) )
    
print(output)



