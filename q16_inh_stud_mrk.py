class student:
    rollno=0
    marks=[]
    total=0
    avg=0
    stud_name=""

class mark(student):
    def getdata(inval):
        inval.rollno=int(input("Enter the rollno."))
        inval.stud_name=input("Enter the Student Name:")
        print("Enter the Marks:")
        for mark in range(6):
            m=int(input())
            inval.marks.append(m)


    def manipulate(mani):
        mani.total= sum(mani.marks)
        mani.avg=mani.total/len(mani.marks)
        print("Rollno:",mani.rollno)
        print("Student name:",mani.stud_name)
        print("Total Mark:",mani.total)
        print("Average Mark:",mani.avg)

ob= mark()
ob.getdata()
ob.manipulate()









