str1=input("Enter the string:")
up=0
lo=0
for i in str1:
    if i.isupper():
        up+=1
    if i.islower():
        lo+=1
print("No. of uppercase charecter:",up)
print("No. of uppercase charecter:",lo)