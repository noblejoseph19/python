class employee:
    emp_id=0
    ename=""
    design=""
    addr=""
    ph_num=0
    invalid=""
    
    def getdata(invalue):
        invalue.emp_id=int(input("Enter the employee id:"))
        invalue.ename=input("Enter the employee name:")
        invalue.design=input("Enter the designation:")
        invalue.addr=input("Enter the addr:")
        invalue.ph_num=int(input("Enter the phone number:"))
        if invalue.ph_num>10:
            invalue.invalid="Number Exceed"
        

        
    def printd(pvalue):
        print("Employee id:",pvalue.emp_id)
        print("Employee Name:",pvalue.ename)
        print("Employee designation:",pvalue.design)
        print("Employee address:",pvalue.addr)
        if pvalue.ph_num>10:
            print("Employee Phone number:",pvalue.invalid)
        else:
            print("Employee Phone number:",pvalue.ph_num)

        


ob =employee()
ob.getdata()
ob.printd()