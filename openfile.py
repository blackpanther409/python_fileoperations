#opening a file named 'test.txt' using with
with open('test.txt')as local_toread:
    a=local_toread.read()
print (a)

#opening a file named 'test.txt' without using with
local_toread=open('test.txt')
a=local_toread.read()
print (a)
local_toread.close()

