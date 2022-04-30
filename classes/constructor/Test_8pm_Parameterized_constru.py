#Test_8pm_Parameterized_constru
class Test:
    def __init__(self,a,b):
        print("-"*50)
        print("I am Parameterized Constructor")
        self.a=a
        self.b=b
        print("-"*50)
        print(self.a)
        print(self.b)
        print("-"*50)

t1 = Test(10,20)
t2 = Test(50,50)
t3 = Test(100,200)

