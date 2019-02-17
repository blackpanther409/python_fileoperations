import os
from datetime import datetime
from os import scandir

basepath=input('Enter the directory pathname:')

entries=os.listdir(basepath)

#function to get time in desired format
def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

#function to get information about files present in given directory
def get_files():
    dir_entries = scandir(basepath)
    for entry in dir_entries:
        if entry.is_file():
            info = entry.stat()
            print(f'{entry.name}\t\t  {convert_date(info.st_mtime)}\t\t'+str(os.path.getsize(basepath+'\\'+entry.name)/1000)+' KB')
print(f'FILE NAME\t\t  LAST MODIFIED\t\t SIZE')

#function call
get_files()
