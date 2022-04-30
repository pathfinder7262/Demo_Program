#inheritance1.py
class C1:
    def setvalue(self):
        self.a=float(input("Enter the number:="))

class Square(C1):
    def cal(self):
        self.res=self.a**2
    def getval(self):
        print("given value {} and result is {} ".format(self.a,self.res))
#class SqRoot(C1):pass

        
c=Square()
print("Contain in SqRoot class or c= ",c.__dict__)
c.setvalue()
print("Contain in SqRoot class or c= ",c.__dict__)
c.cal()
c.getval()
