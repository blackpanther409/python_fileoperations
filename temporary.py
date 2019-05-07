from tempfile import TemporaryFile

# Create a temporary file and write some data to it
fp = TemporaryFile('w+t')       #fp is the file pointer of the temporary file
fp.write('Hello universe!')

# Go back to the beginning and read data from file
fp.seek(0)
data = fp.read()
print(data)

# Close the file, after which it will be removed
fp.close()

import tempfile
with tempfile.TemporaryDirectory() as tmpdir:
  print('Created temporary directory ', tmpdir)
  os.path.exists(tmpdir)

#both the temporary file and directories are deleted once the context manager moves out of the context
'''
What?
Temporary Files in Windows are those junk files whose use is only temporary and become redundant once the task in hand is completed. 
Such temporary file are created to hold data temporarily while a file is being created or processed or used.
Why?
Windows Temporary files are created by the operating system during the normal course of its running when there may not be enough memory 
allocated for the task.

Software which use large amounts of data like Graphics, Video or Media editing software also create temporary files. Such created
temporary files are more often than not, left behind even when the task is over, leading to their wasting disk space.

Temporary Files are also created for backup purposes, by programs. For instance, Microsoft Office saves a Temporary File of the
open document every few minutes. If you save the document and exit, the Temporary File gets deleted.
If the program crashes unexpectedly, the Temporary File is not deleted.
They can thus be useful to help recover lost data if the program or the system crashes.
'''
