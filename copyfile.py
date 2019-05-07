import shutil

src=input("Enter the path of the file to copy:")
dst=input("Enter the path of the directory to place the copy of the file:")

shutil.copy2(src, dst)
print("Given file's copy is successfully pasted to the given directory")

#Enter the entire path of the file and also the directory
