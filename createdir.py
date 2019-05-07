import os

basepath=os.getcwd()
print('current directory is: '+basepath)

#getting new directory name from user
newdir=input('Enter the new directory name:')

#creating that directory and throwing error if it already exists
try:
    os.mkdir(newdir)
except FileExistsError as exc:
    print(exc)

'''
To create subdirectory we need to enter the tree of dirs that we want to create
for example
on entering
parentdir/childdir
this creates childdir inside parentdir which is already present in the current dir
so here we created a subdirectory(childdir here)
'''
