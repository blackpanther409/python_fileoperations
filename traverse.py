import os

path=input("Enter the path of directory for which we need to traverse through directories and process files:")

for dirpath, dirnames, files in os.walk(path):
    print(f'Found directory: {dirpath}')
    for file_name in files:
        print("   "+file_name)
