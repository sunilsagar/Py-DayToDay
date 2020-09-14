lst = [ 1, 1.2, "OK", [1,2,3]]
el = []
type(el) #<class 'list'>
len(lst)
1.2 in lst
lst == [1,2]
1.3 not in lst
#indexing
lst[0]
lst[-1]
lst[-1] = 30  # mutability
lst  #[1, 1.2, 'OK', 30]
for e in lst:
    print(e)

#slicing 
lst[0:2]  #start:end:step
lst[::2]
lst2 = lst + [ 20,30]
lst2 #[1, 1.2, 'OK', 30, 20, 30]
lst #[1, 1.2, 'OK', 30]
lst.append( 45)
lst #[1, 1.2, 'OK', 30, 45]








