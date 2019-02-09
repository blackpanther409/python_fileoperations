import os

#getting directory path from user
basepath=input('Enter the directory pathname:')

#recursive function definition to print directory tree
def dirs(basepath,a):
    entries=os.listdir(basepath)
    for name in entries:
        if os.path.isfile(os.path.join(basepath, name)):
            print(a+'\t|->'+name) 
        elif os.path.isdir(os.path.join(basepath, name)):
            print(a+'|->'+name)
            dirs(basepath+'\\'+name,a+'\t')
print('PATH')

#calling dirs function
dirs(basepath,'')
