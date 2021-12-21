units=int(input("Enter the number of units  consumed :"))

if(units<=100):
    pay_Amount=units*2.25
    surcharge=25.00
elif(units<=200):
    pay_Amount=(100*2.25)+(units-100)*3.75
    surcharge=35.00
elif(units<=300):
    pay_Amount=(100*2.25)+(200-100)*3.75+(units-200)*5.26
    surcharge=55.00
elif(units<=500):
    pay_Amount=(100*2.25)+(200-100)*3.75+(units-200)*5.26+(units-300)*7.75
    surcharge=75.00
elif(units>500):
    pay_Amount=(100*2.25)+(200-100)*3.75+(units-200)*5.26+(units-300)*7.75+(units-500)*9.65
    surcharge=85.00
Total=pay_Amount+surcharge
print("Bill Amount:",Total)

