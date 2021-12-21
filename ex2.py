hour = int(input("enter the  hour:"))
try:
    rate = int(input("enter the rate:"))
except:
    print("Error, Please enter  number input!")
    rate = int(input("enter the rate:"))
pay =  hour * rate
print("payable amount:",pay)
