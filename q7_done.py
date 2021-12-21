count=0
sum=0.0
tot=0
while True:
    sval=input("enter a number")
    if sval == "done":
        break
    try:
        ival=int(sval)
    except:
        print("Invalid input")
    count+=1
    tot=tot+ival
print("Total:",tot)
print("Count:",count)
print("Average:",tot/count)

