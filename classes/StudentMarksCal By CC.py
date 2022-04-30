#StudentMarksCal By CC
#wapp to accept the student detail , claculate thair marks and display marks.
#by using instance ,class level ,static method
'''class level =college name
    instance = sname,sroll no,c++marks,javamarks,python marks
    static = call total marks,percentage,grade and display it
'''
class Student:
    @classmethod
    def scollege(cls):
        cls.college="M.J.College"
    def getinfo(self):
        print("*"*60)
        self.sname=input("Enter the Student Name")
        self.srno=int(input("Enter the Student Roll Number"))
        print("*"*60)
    def getmarks(self):
        while(True):
              self.cpp=float(input("Enter the CPP Marks"))
              self.java=float(input("Enter the JAVA Marks"))
              self.python=float(input("Enter the Python Marks"))
              print("*"*60)
              if(self.cpp>100):
                  print("Enter the Valid Marks")
              elif(self.java>100):
                  print("Enter the Valid Marks")
              elif(self.python>100):
                  print("Enter the Valid Marks")
              else:
                  break
        
class Marks:
    @staticmethod
    def calmarks(obj):
        
        ttl=(obj.cpp+obj.java+obj.python)
        perc=((ttl/300)*100)
        if(perc>=95):
            print("A+")
        elif(perc>=85 and perc <=90):
            print("Student Grade:A")
        elif(perc>=70 and perc<=84):
            print("Student Grade B")
        elif(perc>=60 and perc<=69):
            print("Student Grade C")
        elif(perc>=45 and perc<=59):
            print(" Student Grade D")
        else:
            print("Fail")
            
        print("Student Name={}".format(obj.sname))
        print("Student Roll No={}".format(obj.srno))
        print("Student College Name={}".format(Student.scollege))
        print("Student Total Marks={}".format(ttl))
        print("Student Percentage={}".format(perc))
        print("*"*60)

        
Student.scollege
s1=Student()
s1.getinfo()
s1.getmarks()
Marks.calmarks(s1)

        
