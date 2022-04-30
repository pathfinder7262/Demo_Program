#inheritance2.py
class C1:
    def setvalue(self):
        self.a=float(input("Enter the number:="))

class Square(C1):
    def cal(self):
        self.setvalue() #Derived class fun calling base class method
        self.res=self.a**2
        self.getval()
        
    def getval(self):
        print("given value {} and result is {} ".format(self.a,self.res))

class SqRoot(C1):
    def cal(self):
        self.setvalue()
        self.res=self.a**(1/2)
        self.getval()
    def getval(self):
        print("given value {} and result is {} ".format(self.a,self.res))        
        
c=Square()
c.cal()
c=SqRoot()
c.cal()
