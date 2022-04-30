#wapp which will find bigest of 3 numbers with class and objects.

class big:
    def setno(self,a,b,c):
        if (a>b) and (a>c):
            print(a," is grater")
        elif(b>c):
            print(b, " is grater")
        else:
            print(c," is grater")

a = int(input("Enter the A value"))
b = int(input("Enter the B value"))
c = int(input("Enter the C value"))

g1 = big()
g1.setno(a,b,c)

    
