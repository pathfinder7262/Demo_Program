#polyEx6.py

class Circle:
    def __init__(self,r):
        self.ac=3.14*r*r
        print("Area of Circle:={}".format(self.ac))

class Square:
    def __init__(self,s):
        self.as1=s*s
        print("Area of square:{}".format(self.as1))
        

class Rect(Square,Circle):
    def __init__(self,l,b):
        self.ar = l*b
        print("Area of Rect={}".format(self.ar))
        Square.__init__(self,float(input("Enter square:= ")))
        Circle.__init__(self,float(input("Enter Redius:= ")))


l1 = float(input("Enter the length:  "))
b1 = float(input("Enter the breath:  "))
ro=Rect(l1,b1)

        
