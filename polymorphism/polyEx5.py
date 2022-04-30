#polyEx5.py

class Circle:
    def area(self,r):
        self.ac=3.14*r*r
        print("Area of Circle:={}".format(self.ac))

class Square:
    def area(self,s):
        self.as1=s*s
        print("Area of square:{}".format(self.as1))
        

class Rect(Square,Circle):
    def area(self,l,b):
        self.ar = l*b
        print("Area of Rect={}".format(self.ar))
        Square.area(self,float(input("Enter square:= ")))
        Circle.area(self,float(input("Enter Redius:= ")))

ro = Rect()
l1 = float(input("Enter the length:  "))
b1 = float(input("Enter the breath:  "))
ro.area(l1,b1)

        
