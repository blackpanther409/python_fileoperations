import os

src=input("Enter the path of the file to change the name:")
dst=input("Enter the path with new file name:")

os.rename(src,dst)

print("The file is successfully renamed")
