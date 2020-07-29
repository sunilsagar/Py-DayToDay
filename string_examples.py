

# if "hello" not in s:
#     print("""hello 
#     is not part 
#     of""", s)
#     
# for element in s:
#     print(element)

s = "Hello World"

#Take each character(ch1) from s 
for ch1 in set(s):
    #initialize counter 
    counter = 0
    #Take each character(ch2) from s
    for ch2 in s:
        #if ch1 are ch2 are same 
        if ch1 == ch2:
            #increment counter 
            counter = counter + 1
    #print ch1 and counter 
    print(ch1, "=", counter)



### Data structure 
# []    list - Duplictes - P , Indexing - P, Insertion ordered- P , Mutable
# ()         tuple - immutable list 
    
# {}    set - Duplictes - NP, Indexing - NP, Insertion ordered- NP, Mutable 
       # frozenset - immutable set 
       
# ------------------------
# {} dict -  Key: Value - All Keys are like set , Value can be anything

list searching - O(N)
dict searching - O(1)

