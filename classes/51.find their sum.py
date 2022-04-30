#51.wapp to accept 2 numerical value and find their sum 1)function 2)class and obj

class sum:

    def getno(self):
        self.a=float(input("Enter the 1st No.:=="))
        self.b=float(input("Enter the 2nd No.:=="))

    def sumno(self):
        self.c = (self.a+self.b)

    def dispsum(self):
        self.sumno()
        print("Sum of {} and {} is= {}".format(self.a,self.b,self.c))

#main
        
s1=sum()
s1.getno()
#s1.sumno()
s1.dispsum()
