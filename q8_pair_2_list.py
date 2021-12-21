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

print(dict1)


