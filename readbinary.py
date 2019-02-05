#use 'rb' mode to read and 'wb' mode to write for binary files
with open('grid_racing.jpg','rb') as binary_file:
    b=binary_file.readlines()
    print (b)
