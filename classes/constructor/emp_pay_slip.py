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
        #self.getcompname()
        if(self.basicsal>20000):
            self.da=self.basicsal*(15/100)
            self.ta=self.basicsal*(10/100)
            self.ma=self.basicsal*(5/100)
            self.hra=self.basicsal*(20/100)
            self.lic=self.basicsal*(2/100)
            self.gpf=self.basicsal*(1/100)
        else:
            self.da=self.basicsal*(20/100)
            self.ta=self.basicsal*(15/100)
            self.ma=self.basicsal*(10/100)
            self.hra=self.basicsal*(25/100)
            self.lic=self.basicsal*(2/100)
            self.gpf=self.basicsal*(1/100)
        #calculate net sal
        self.netsal=(self.basicsal+self.da+self.ta+self.ma+self.hra)-(self.lic+self.gpf)

    def dispemppayslip(self):
        #self.paycalculation()
        print("*"*60)
        print("Pay slip for moth Sep 2021")            
        print("*"*60)
        print("emp no=={}".format(self.eno))
        print("emp nname=={}".format(self.ename))
        print("emp designation=={}".format(self.dsg))
        print("emp compony name=={}".format(self.getcompname))
        print("*"*60)
        print("Emp Basic Salary=={}".format(self.basicsal))
        print("Emp DA=={}".format(self.da))
        print("Emp TA=={}".format(self.ta))
        print("Emp HRA=={}".format(self.hra))
        print("Emp MA=={}".format(self.ma))
        print("Emp LIC=={}".format(self.lic))
        print("Emp GPF=={}".format(self.gpf))
        print("*"*60) 
        print("Emp Net Salary=={}".format(self.netsal))       
        print("*"*60)      
        
        
    
