num=int(input("Enter the line to be displayed:"))
with open("C:\\Users\\sahithi nandyala\\Documents\\here to succeeed\\PYTHON\\test.txt") as fp:
    for i, line in enumerate(fp):
        if i+1 == num:
            print(line)
         
