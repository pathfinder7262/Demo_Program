#LoanEx.py
class SBI:
    def getSBICustDet(self):
        self.acno=int(input("Enter ac no:="))
        self.cname=input("Name")
        self.loan=float(input("Enter loan amount=>"))

class ICICI:
    def getICICICustDet(self):
        self.acno=int(input("Enter ac no:="))
        self.cname=input("Name")
        self.loan=float(input("Enter loan amount=>"))

class LoanCal:
    @staticmethod
    def loancalculator(obj):pass



sb=SBI()
sb.getSBICustDet()
ic=ICICI()
ic.getICICICustDet()
LoanCal.loancalculator(sb)
print("----------------------")

