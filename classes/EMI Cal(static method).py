#EMI Cal(static method)
#static method
class SBI:
    def sbiloan(self):
        print("SBI Cust Info")
        print("-"*50)
        self.p=float(input("Enter the Amount:"))
        self.t=float(input("Enter the Time:"))
        self.r=float(input("Enter the interest:"))
        self.nom=float(input("Enter the No. of Month:"))
        print("-"*50)
class ICICI:
    def iciciloan(self):
        print("ICICI Cust Info")
        print("-"*50)
        self.p=float(input("Enter the Amount:"))
        self.t=float(input("Enter the Time:"))
        self.r=float(input("Enter the interest:"))
        self.nom=float(input("Enter the No. of Month:"))
        print("-"*50)

class HDFC:
    def hdfcloan(self):
        print("HDFC Cust Info")
        print("-"*50)
        self.p=float(input("Enter the Amount:"))
        self.t=float(input("Enter the Time:"))
        self.r=float(input("Enter the interest:"))
        self.nom=float(input("Enter the No. of Month:"))
        print("-"*50)

class EmiCal:
    @staticmethod
    def calculate(obj):
        #print(obj.__dict__)
        si=(obj.p*obj.t*obj.r)/100
        totamt=obj.p+si
        emiamt=totamt/obj.t
        print("Total amt  after interest cal={}".format(totamt))
        print("Total amt  after interest cal={}".format(emiamt))
        

sb1=SBI()
ic1=ICICI()
hd1=HDFC()

print(sb1.__dict__)
print(ic1.__dict__)
print(hd1.__dict__)

#sb1.sbiloan()
ic1.iciciloan()
#hd1.hdfcloan()

print(sb1.__dict__)
print(ic1.__dict__)
print(hd1.__dict__)


EmiCal.calculate(ic1)

    
