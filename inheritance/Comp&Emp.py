'''
60.wapp to implement the following:
	Let us assume there exist a compony which contains compony name and address. Accept and display comp name and address
	Let us assume there exist an emp which contains empNo, empNm, empSal. Accept and display emp details along with compony details 
'''
class Company:
    def setCompVal(self):
        self.cname=input("Enter the compony name:= ")
        self.cadd=input("Enter the compony adrress:= ")

    def getcompval(self):
        print("Compony name:{}".format(self.cname))
        print("Compony address:{}".format(self.cadd))
        print("="*50)

class Emp(Company):
    def setEmpVal(self):
        self.ename=input("Enter the EMP name:= ")
        self.enm=input("Enter the EMP Number:= ")
        self.sal=input("Enter the EMP Salary:= ")

   def getEmpVal(self):
         print(" EMP name:= ".format(self.ename))
         print(" EMP Number:= ".format( self.enm ))
         print(" EMP Salary:= ".format( self.sal ))

        


    
        
            
