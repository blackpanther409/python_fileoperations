list1=[]
list2=[]
i=0
#appending all the lines of the given file to list1
with open('C:\\Users\\sahithi nandyala\\Documents\\here to succeeed\\PYTHON\\test.txt','r')as fin:
    for line in fin:
        list1.append(line)

#taking line and line number to add
list2.append(input("Enter the line to add :")+"\n")
i=int(input("Enter the line number to append given line:"))
j=len(list1)

#if there are lines more than given line number
if(j>=i):
    list1=list1[0:i-1]+list2+list1[i-1:len(list1)+1]        #adding given line to list1
    with open('C:\\Users\\sahithi nandyala\\Documents\\here to succeeed\\PYTHON\\test.txt','w')as fout:
        fout.write("")                                      #clearing old text
    #writing list1 lines to file
    with open('C:\\Users\\sahithi nandyala\\Documents\\here to succeeed\\PYTHON\\test.txt','a')as fout:
        for line in list1:
            fout.write(line)

#appending after all lines
elif(i==j+1):
    with open('C:\\Users\\sahithi nandyala\\Documents\\here to succeeed\\PYTHON\\test.txt','a')as fout:
        fout.write(list2)   
    
#not possible to add case
else:
    print("There are only "+str(j)+" lines,cannot append")    
        

        
