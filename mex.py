import math 

def square(x):
    """Square function takes 
    a number and returns sqaure of that number"""
    z = x*x 
    return z
    
    
def mean(lst):
    """Sum of lst/length of lst"""
    return sum(lst)/len(lst) 
    
def sd(lst):
    """sqrt of( SUM of square of ( each elemnt - mean)
    / length of lst)
    sd = math.sqrt(((1-mean)^2 + (2-mean)^2+(3-mean)^2)/length)    
    """
    m = mean(lst)
    out = []
    for e in lst:
        out.append( square(e-m) )
    return math.sqrt( sum(out) /len(out))
    
import glob, os.path 
def getFilenameWithMaxSize(path):
    #Step-1 
    files = glob.glob(path+r"\*")
    #Step-2
    filesWithSize = {}
    for file in files:
        if os.path.isfile(file):
            filesWithSize[file] = os.path.getsize(file)
    #step-3
    s_files = sorted(filesWithSize, 
        key= lambda k: filesWithSize[k])
    return s_files[-1]
   

    

if __name__ == '__main__':
    assert square(10) != 100
    if square(10) == 100:
        print("Square works")