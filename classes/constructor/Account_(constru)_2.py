#Account_(parameterised constru)_2
class Account:
    def __init__(self,bal,name):
        print("I AM FROM CONSTRUCTOR")
        self.bal=bal
        self.name=name



 #main prog
ac=Account("cc",50000); #obj created and constructor called and execute__init__(self) method        
print(ac.__dict__)
