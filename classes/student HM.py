#Student detail In class data member and method
# student 


class Student:
    @classmethod
    def schoolnm(cls):
        cls.schlnm="L.N.S.V.Jalgaon."
        cls.sdiv="A"

    def studinfo(self):
         self.snm=input("Enter the Student Name==>")
         self.srollno=int(input("Enter the Student Roll No.==>"))
         self.cpp=int(input("Enter the Marks in CPP"))
         self.python=int(input("Enter the Marks in PYTHON"))
         self.java=int(input("Enter the Marks in JAVA"))

    def markcal(self):
        if(self.cpp<100 and self.python<100 and self.java<100):
            self.ttl = float(((self.cpp+self.python+self.java)/300))*100
            print("="*50)
            print("Student Name is {}".format(self.snm))
            print("Student Roll No. is {}".format(self.srollno))
            #print("Student Schol Name is {}".format(schoolnm.schlnm))....????
            print("Student Marks is {}".format(self.ttl))
            print("="*50)
        else:
            print("Enter the Right Marks")


#main prog
s1=Student()
#s1.schoolnm()
s1.studinfo()
s1.markcal()
'''
s2=Student()
s2.studinfo()
s2.markcal()

s3=Student()
s3.studinfo()
s3.markcal()
'''  
