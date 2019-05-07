import os
import fnmatch

flag=0
#getting filename to search for from user
filename=input("Enter the filename to search for:")
print("searching...\n")

from pathlib import Path
home = str(Path.home())
 
for root, dirs, files in os.walk(home): 
    for file in files:  
        if fnmatch.fnmatch(file,filename): 
            print (root+'/'+str(file))
            flag=1

if flag==0:
  print("The file you are searching for is not available")
else:
  print("\n*********Searching is over**********")

