'''wapp to impliment the following problem 
1.let us assume there exist a university which contains university name
    and location accept and display university detail.
2.let us assume there exist a college having c_name,c_addressaccept and
    display college detail along with university detail.
3..let us assume there exist a student having s_number,s_name,s_course
accept and display student detail along with college and university detail.
multilevel inheritance
'''
#inheritnace61.py
class Univer:
    def setUnivDet(self):
        self.uname=input("Enter The University Name: ")
        self.uloc=input("Enter The University Location: ")

    def getUnivDet(self):
        print("*"*50)
        print("Univ Name: {}".format(self.uname))
        print("*"*50)
        print("Univ Location: {}".format(self.uloc))
        print("*"*50)

class College(Univer):
    def setCollDet(self):
        self.cname=input("Enter The College Name: ")
        self.cloc=input("Enter The College Location: ")

    def getCollDet(self):
        print("*"*50)
        print("College Name: {}".format(self.cname))
        print("*"*50)
        print("College Location: {}".format(self.cloc))
        print("*"*50)

class Student(College):
    def setStuDet(self):
        self.sname=input("Enter The Student Name: ")
        self.sloc=input("Enter The Student Location: ")
        self.scor=input("Enter The Student Course: ")
        #self.setCollDet
        
    def getStuDet(self):
        print("*"*50)
        print("Student Name: {}".format(self.sname))
        print("*"*50)
        print("Student Location: {}".format(self.sloc))
        print("*"*50)
        print("Student Course: {}".format(self.scor))
        print("*"*50)
        

d1=Student()
d1.setStuDet()
d1.getStuDet()
d1.setUnivDet()
d1.getUnivDet()    
d1.setCollDet()
d1.getCollDet()
