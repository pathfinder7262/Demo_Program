#54.wapp which will accept redius of circle and calculate area and circumference

class Circle:
    @classmethod
    def PiVal(cls):
        cls.pi=3.14
    def getval(self):
        self.r = float(input("Enter the Redius of Circle"))
    def ca(self):
        Circle.PiVal()
        self.area=(Circle.pi*self.r**2)
        self.curcum=(2*Circle.pi*self.r)
    def showval(self):
        print("Area of Circle=={}".format(self.area))
        print("Circumference of  circle=={}".format(self.curcum))


a1=Circle()
a1.getval()
a1.ca()
a1.showval()
        
