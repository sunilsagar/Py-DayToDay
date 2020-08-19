""" This is my first module """

def square(x):
    """ Squaring the input 
    number"""
    z = x*x 
    return z
    
def mean(lst):
    """Sum of lst/length of lst"""
    m = sum(lst)/len(lst)
    return m
    
import math 
def sd(lst):
    """sqrt of( SUM of square of 
    ( each elemnt - mean)  / length of lst  )
    eg #sqrt((1-m)^2+(2-m)^2+(3-m)^2)/3) """
    m = mean(lst)
    o = []
    for item in lst:
          o.append( square(item - m) )
    result = math.sqrt(sum(o)/len(o))
    return result

    
    
    
if __name__ == '__main__':
    z = square(10)
    print(z)

#Join at 15:02 