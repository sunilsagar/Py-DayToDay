s = "Hello World Hello Earth Hello everyone"

#Create empty dict(out)
out = {}
#Take each word(wd) from s 
for wd in s.split():  # list 
    #if wd does not exist in out 
    if wd not in out:
        #create an element with key as wd, value 1 
        out[wd] = 1
    else: 
        #increment wd's value 
        out[wd] += 1    # out[wd] = out[wd] + 1
        
print(out)

#Find checksum 
input="ABCDEF1234567890"

# Take two two character(one byte) from above (which are in hex digit )
# Convert to int  (Hint: use int function with base)
# Sum all and then find mod with 255, that is your checksum 

out = []
for f,s in zip(input[::2], input[1::2]):
    out.append( int(f+s, base=16) )

checksum = sum(out) % 255
print(checksum)

cksum= sum([ int(f+s, base=16) for f,s in zip(input[::2], input[1::2]) ]) % 255
s = "Hello World Hello Earth Hello everyone"
out = {e: s.count(e)   for e in s.split() }











