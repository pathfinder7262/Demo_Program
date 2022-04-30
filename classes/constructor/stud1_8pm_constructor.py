#stud1_8pm_constructor.py

class Stud:
    def __init__(self):
        print("I am Constructor")    
        self.sno = int(input("Enter the roll number"))
        self.sname = (input("Enter the Name"))
        self.displval()
    def displval(self):
        print("="*50)
        print(self.sno)
        print(self.sname)

so = Stud()  #obj created
#so.displval()

'''
class Stud:
    def __init__(self, sno, sname):
        self.sno = sno
        self.sname = sname
        self.displval()

    @classmethod
    def create_with_user_input(cls):
        sno = int(input("Enter the roll number"))
        sname = (input("Enter the Name"))
        return cls(sno, sname)

    def displval(self):
        print("="*50)
        print(self.sno)
        print(self.sname)

so = Stud()
so.create_from_user_input()
'''
