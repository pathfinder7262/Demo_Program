#circle.py===file name module name
class Circle:
    @classmethod
    def getpi(cls):
        cls.pi=3.14
    def __init__(self):
        self.r=float(input("Enter the redious"))

    def calarea(self):
      ac=Circle.pi*self.r**2
      print("Area of circle={}".format(ac))

    def calpar(self):
        pc=2*self.pi*self.r
        print("Perimeter of circle={}".format(pc))


        
