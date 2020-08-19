
#Given Path, write code to print filenames with it's size 
# Take Path from commandline 
#   1. Given path, find all files and directory - Use glob 
#       import glob
#       glob.glob(path+"/*")
#   2. Get only files from above by using os.path.isfile 
#   3. create a dict of file and filesize, use os.path.getsize 

#D:\handson>python files_examples.py "d:/handson"
import glob 
import sys 
import os.path 
#D:\handson>python files_examples.py
path = sys.argv[1] if len(sys.argv) >=2 else "."
files = glob.glob(os.path.normpath(os.path.join(path , "*")) )
#files =  glob.glob(path+"/*")
output = {}
for item in files:
    if os.path.isfile(item) :
        output[item] = os.path.getsize(item)
        
print(output)





