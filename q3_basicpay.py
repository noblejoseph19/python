emp_id = int(input("Enter the Emp id:"))
emp_name = input("Enter the Name:")
basic_pay = int(input("Enter the Basic Pay:"))
if basic_pay >10000:
    hra=basic_pay*.15
    da=basic_pay*.10
    net_pay=basic_pay+hra+da
    print("Total Salary:",net_pay)
elif basic_pay <=10000 or basic_pay> 5000 :
    hra=basic_pay*.10
    da=basic_pay*.05
    net_pay=basic_pay+hra+da
    print("Total Salary:",net_pay)
elif basic_pay <=5000 :
    hra=basic_pay*.05
    da=basic_pay*.03
    net_pay=basic_pay+hra+da
    print("Total Salary:",net_pay)    

