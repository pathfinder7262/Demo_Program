#58.wapp which will accept any +ve numerical value and find its factorial. using oops.
class Fact():
    def getval(self):
        self.val=int(input("Enter the No=>"))
        self.f = 1
    def facto(self):
        for i in range(1,self.val+1):     #here 'i' is local veriable and no need write it with 'self'
            self.f=self.f*i
    def disp(self):
        print("Factorial of {} is {}".format(self.val,self.f))
f1=Fact()
f1.getval()
f1.facto()
f1.disp()
    
