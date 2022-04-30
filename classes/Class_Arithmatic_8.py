#Class_Arithmatic_8.py

class Test:
    def setvalues(self):
        self.a = float(input("Enter the 1st no."))
        self.b = float(input("Enter the 2nd no."))
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
t1=Test()
t1.setvalues()
t1.calsum()
t1.despresult()
