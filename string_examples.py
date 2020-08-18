# s = "Hello World"
# s = 'Hello World'
# s = """Hello
# World"""
# #s = Hello\nWorld
# len(s) #11
# s[0]   # 'H'
# s[len(s)-1] # 'H'
# s[-1]  #'d'
# s[-len(s)] # 'D'
# "He" in s   #True
# "He" not in s # False
# s == "OK" # True 
# for e in s:
#     print(e)  # e= 'H' , e='e' ...

#Hands On 
s = "Hello World"
# H - 1 
# e - 1
# l - 3
# ...
#Take each char (ch1) from s  #for loop 
s = "Hello World"
for ch1 in set(s):
    #initilize counter
    counter = 0     
    for ch2 in s:
        #if ch1 and ch2 are same  
        if ch1 == ch2:
            #increment counter
            counter = counter + 1
    #print ch1 and counter
    print(ch1, "-", counter)    



#s=[ 1,2,3,4,5,6,7,8]
#    0 1 2 3 4 5 6 7
##start_index:end_index
#s[0:5]  # 1, 2, 3, 4, 5
##start_index:end_index:step 
#s[0:5:1] # 1, 2, 3, 4, 5
#s[0:5:2]# 0, 0+2=2, 2+2=4
##1,3,5
#s[::2] # 0, 0+2=2, 2+2=4,....
##1,3,5,7
#
#s[5:0:-1]  # 5, 5-1=4, 4-1=3, 3-1=2, 2-1=1 #, 1-1=0
#>>> s[5:0:-1]
## [6, 5, 4, 3, 2]
#>>> s[::-1]
#[8, 7, 6, 5, 4, 3, 2, 1]
#
####################################################
# []  list - Duplicates-P, Indexing - P, Insertion Ordered-P, Mutable
# ()      tuple - immutable, ---above---
#   
# {}  set - Duplicates - NP, Indexing-NP, Insertion ordered-NP, Mutable
#       frozenset - immutable, ---above--
# 
# --------------------------
# {k:v} dict - list of (Key, value) pairs
#        all keys are like set - unique 
#        value could be anything 
#        Searching - Given Key , get it's value - O(1), not like O(N)













