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
