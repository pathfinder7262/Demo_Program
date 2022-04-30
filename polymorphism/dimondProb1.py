#dimondProb1
class c1:
    def m1(self):
        print("C1 - M1()")
class c2(c1):
    def m1(self):
        print("C2 - M1()")
class c3(c1):
    def m1(self):
        print("C3 - M1()")
class c4(c2,c3):
    def m1(self):
        print("C4 - M1()")
        c3.m1(self)
        c2.m1(self)
        c1.m1(self)
o4 = c4()
o4.m1()
        
