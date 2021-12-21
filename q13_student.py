class student:
    rollno=0
    sname=""
    course=""
    
    def getdata(invalue):
        invalue.rollno=int(input("Enter the roll number:"))
        invalue.sname=input("Enter the student name:")
        invalue.course=input("Enter the course name:")
        
    def printd(pvalue):
        print("Rollno:",pvalue.rollno)
        print("Student Name:",pvalue.sname)
        print("Course Name:",pvalue.course)

ob =student()
ob.getdata()
ob.printd()

    



