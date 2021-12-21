list1=[]

limit=int(input("Enter the limit:"))
print("Enter the numbers:")
for i in range(limit):
    ival=int(input())
    list1.append(ival)
print("divisible by 5:")
for i in list1:
    if i%5==0:
        print(i)
    else:
        print("No elements are divisible by 5")
