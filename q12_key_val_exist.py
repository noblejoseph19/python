

limit=int(input("Enter the Limit:"))
print("Enter the Key and Value:")
dict1=dict()
for i in range(limit):
    str1=input()
    val=int(input())
    dict1[str1]=val
print("dictionary:",dict1)
key=input("Enter the Key :")
value=int(input("Enter the Value:"))
kval=dict1[key]

if  key in dict1.keys() and value == kval : 
    print("Key Value pair",key,":",value,"exist in the dictionary")
else:
    print("Key Value pair",key,":",value,"not exist")


