
input = [ 3, 5, 2, 10]
#output = [9, 25, 4, 100]
output = [9, 25]
############### MAP Pattern ################
#Create an empty list (output)
output = []
#Take each element(e) from input 
for e in input:
    #if this e is odd 
    if e % 2 == 1:
        #Square that e and append to empty/output list
        output.append( e*e )
#print output list 
print(output)
#-------------------------------------
input = "[1,2,3,4]"
output = [1,2,3,4]

# s2 = Strip with "[]" and then split with ","     # [ "1", "2", "3", "4" ]
# create an empty list (output)
# Take each element from s2:
#     convert to int and then append to output list 
# print output list 


input ="[1,2,3,4]"
output=[]
for e in input.strip("[]").split(','):
  output.append(int(e))
      
print(output)






