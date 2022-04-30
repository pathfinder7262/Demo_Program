#Account.py(constru)
class Account:
    def __init__(self):
        print("I AM FROM CONSTRUCTOR")
        self.bal=500



 #main prog
ac=Account(); #obj created and constructor called and execute__init__(self) method        
print(ac.__dict__)
