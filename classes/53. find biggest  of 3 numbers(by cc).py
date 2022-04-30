#.53.wapp which will find biggest  of 3 numbers with classes and object

class Big:
    def getno(self):
        self.a=int(input("Enter the 1st No"))
        self.b=int(input("Enter the 2nd No"))
        self.c=int(input("Enter the 3rd No"))

    def findbig(self):
        self.big=self.a
        if(self.big<self.b):
            print("{} is big".format(self.b))
        elif(self.big<self.c):
            print("{} is big".format(self.c))
        else:
            print("{} is big".format(self.big))
    
b=Big()
b.getno()
b.findbig()
