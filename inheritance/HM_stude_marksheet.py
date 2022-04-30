'''
Class Sub =>
Class Internal_Exam => Cim(20),CPPim(20),PYTHONim(20)
Class Exter_Marks => Cm(80),CPPm(80),PYTHONm(80)


Class Student: accept name & Number
                            cal total marks
                            cal total percentage
                            decide grade and display
'''
#HM_stude_marksheet
class sub:
    def get(self):
        print("===Markssheet===")
        print("C Langauge: ")
        print("CPP Langauge: ")
        print("Python Langauge: ")


class intMarks:
    def getIntMrk(self):
        while(True):
            self.cmrk=int(input("Enter the C Langauge marks: "))
            self.cppmrk=int(input("Enter the CPP Langauge marks: "))
            self.pymrk=int(input("Enter the Python Langauge marks: "))
            print("*"*50)
            if (self.cmrk<=20 and self.cppmrk<=20 and self.pymrk<=20):
                self.getExtMrk()
                break
            else:
                print("Plz, Enter The Right Marks : ) ")
            
            
class ExtMarks:
    def getExtMrk(self):
        while(True):
            self.cemrk=int(input("Enter the External C Langauge marks: "))
            self.cppemrk=int(input("Enter the External CPP Langauge marks: "))
            self.pyemrk=int(input("Enter the External Python Langauge marks: "))
            print("*"*50)
            if (self.cemrk<=80 and self.cppemrk<=80 and self.pyemrk<=80):
                self.ttlMrk()
                break
            else:
                print("Plz, Enter The Right Marks : )")
                

class Student(sub,intMarks,ExtMarks):
    def getStudDet(self):
        self.snm=input("Enter the Student Name: ")
        self.sno=int(input("Enter the Student Roll Number: "))
        print("*"*50)
        self.getIntMrk()

    def ttlMrk(self):
        self.imrk=(self.cmrk+self.cppmrk+self.pymrk)
        self.emrk=(self.cemrk+self.cppemrk+self.pyemrk)
        self.perc()
       
    def perc(self):
        self.per = ((self.imrk+self.emrk)/300)*100
        self.dispDet()

    def dispDet(self):
        print("*"*50)
        print("Student Name: {}".format(self.snm))
        print("*"*50)
        print("Student Roll Number: {}".format(self.sno))
        print("*"*50)
        print("Total Internal Marks==> {}".format(self.imrk))
        print("*"*50)
        print("Total External Marks==>{}".format(self.emrk))
        print("*"*50)
        print("Percentage of {} is=>{}".format(self.snm,self.per))
        print("*"*50)
        
        
        
                


    
                
                
                
                
            
