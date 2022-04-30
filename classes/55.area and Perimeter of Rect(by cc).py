#55.wapp which will accept length and breath of rectangle and find its area and Perimeter

class rectArea():
    def getVal(self):
        self.l = float(input("Enter the Length:=="))
        self.w = float(input("Enter the Width:=="))
    def cal(self):
        self.ar=(self.l*self.w)
        self.pm=(2*(self.l+self.w))
    def disp(self):
        print("Area of Rectangle:=={}".format(self.ar))
        print("Perimeter of Rectangle:=={}".format(self.pm))

r=rectArea()
r.getVal()
r.cal()
r.disp()

    
        
