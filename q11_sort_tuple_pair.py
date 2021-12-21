list1=[]
list2=[]
print("Enter the strings:")
for i in range(5):
    sval=input()
    list1.append(sval)
print("Enter the Numbers:")
for i in range(5):
    ival=int(input())
    list2.append(ival)

dict1=dict()

for i in range(5):
    dict1[list1[i]]=list2[i]

tup=dict1.items()
print("Tuple Before sort:",tup)
tmp=list()
for i,j in dict1.items():
    tmp.append((j,i))
tmp.sort()

tmp1=list()
for i,j in tmp:
    tmp1.append((j,i))

c=tuple(tmp1)
print("After sort:",c)