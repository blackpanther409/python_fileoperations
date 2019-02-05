#getting the line no. to be displayed by user
num=int(input("Enter the line to be displayed:"))

#opening the file and enumerating(line no.,line) the lines in it
with open("C:\\Users\\sahithi nandyala\\Documents\\here to succeeed\\PYTHON\\test.txt") as fp:
    for i, line in enumerate(fp):
        if i+1 == num:
            print(line)
#tips:            
#be careful about giving the file address correctly
            
