#Class_Arithmatic_9.3.py

class Test:
    def setvalues(self):
        self.a = float(input("Enter the 1st no."))
        self.b = float(input("Enter the 2nd no."))
        self.calsum()
        self.despresult()

        
    def calsum(self):
        self.c = self.a+self.b
    def despresult(self):
        print("="*50)
        print("RESULT")
        print("="*50)
        print(self.a)
        print(self.b)
        print(self.c)
        print("="*50)

        
#main program
try:
    t1=Test()
    t1.setvalues()
except ValueError:
    print("Don't Enter alpha numeric")
