#emp pay slip==module name

class EmpPaySlip:
    @classmethod
    def getcompname(cls):
        compname="Wipro SS Pvt Ltd"
    def __init__(self):
        self.eno=int(input("Enter the emp no==>"))
        self.ename=input("Enter the enp name==>")
        self.basicsal=float(input("Enter the basic sal==>"))
        self.dsg=input("Enter emp desig==>")
    def paycalculation(self):
        self.getcompname()
        if(self.basicsal>20000):
            self.da=sel.basicsal*(15/100)
            self.ta=sel.basicsal*(10/100)
            self.ma=sel.basicsal*(5/100)
            self.hra=sel.basicsal*(20/100)
            self.lic=sel.basicsal*(2/100)
            self.gpf=sel.basicsal*(1/100)
        else:
            self.da=sel.basicsal*(20/100)
            self.ta=sel.basicsal*(15/100)
            self.ma=sel.basicsal*(10/100)
            self.hra=sel.basicsal*(25/100)
            self.lic=sel.basicsal*(2/100)
            self.gpf=sel.basicsal*(1/100)
        #calculate net sal
        self.netsal=(basicsal+da+ta+ma+hra)-(lic+gpf)

    def dispemppayslip(self):
        self/ paycalculation()
        print("*"*60)
        print("Pay slip for moth Sep 2021")            
        print("*"*60)
        print("emp no=={}".format(self.eno))
        print("emp nname=={}".format(self.ename))
        print("emp designation=={}".format(self.dsg))
        print("emp compony name=={}".format(EmpPaySlip.compname)
        print("*"*60)
        print("Emp basic sal=={}".format(self.basicsal))
        print("Emp DA=={}".format(self.da))
        print("Emp basic sal=={}".format(self.ta))
        print("Emp basic sal=={}".format(self.hra))
        print("Emp basic sal=={}".format(self.ma))
        print("Emp basic sal=={}".format(self.lic))
        print("Emp basic sal=={}".format(self.gpf))
        print("*"*60) 
        print("Emp Net Salary=={}".format(self.netsal))       
        print("*"*60)      
        
        
    
