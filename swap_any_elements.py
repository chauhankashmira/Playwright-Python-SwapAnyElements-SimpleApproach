
#Simple approach

mylist = [10,20,30,40,50,60,70]
print(mylist)

pos1,pos2=3,5

mylist[pos1],mylist[pos2]=mylist[pos2],mylist[pos1]
print(mylist)
