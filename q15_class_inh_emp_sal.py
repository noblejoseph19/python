class employee:
    emp_id=0
    emp_name=""
    basic_pay=0

class childemp(employee):

    def getdata(inval):
        inval.emp_id = int(input("Enter the Emp id:"))
        inval.emp_name = input("Enter the Name:")
        inval.basic_pay = int(input("Enter the Basic Pay:"))

    def salarycal(inval):
        if inval.basic_pay >10000:
            inval.hra=inval.basic_pay*.15
            inval.da=inval.basic_pay*.10
            inval.net_pay=inval.basic_pay+inval.hra+inval.da
            print("Employee ID:",inval.emp_id)
            print("Employee Name:",inval.emp_name)
            print("Total Salary:",inval.net_pay)
        elif inval.basic_pay <=10000 or inval.basic_pay> 5000 :
            inval.hra=inval.basic_pay*.10
            inval.da=inval.basic_pay*.05
            inval.net_pay=inval.basic_pay+inval.hra+inval.da
            print("Employee ID:",inval.emp_id)
            print("Employee Name:",inval.emp_name)
            print("Total Salary:",inval.net_pay)
        elif inval.basic_pay <=5000 :
            inval.hra=inval.basic_pay*.05
            inval.da=inval.basic_pay*.03
            inval.net_pay=inval.basic_pay+inval.hra+inval.da
            print("Employee ID:",inval.emp_id)
            print("Employee Name:",inval.emp_name)
            print("Total Salary:",inval.net_pay)  

ob= childemp()
ob.getdata()
ob.salarycal()
