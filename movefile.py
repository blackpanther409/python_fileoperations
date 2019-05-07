import shutil

src=input("Enter the path of the file which is to be moved:")
des=input("Enter the path of destination directory:")

shutil.move(src,des)

print("Your file has been successfully moved to the given directory")
