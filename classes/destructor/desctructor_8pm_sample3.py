#desctructor_8pm_sample3.py
import time
class Sample:
    def __init__(self):
        print("I am From Constructor")
        self.a=10
        self.b=20
        print(self.a)
        print(self.b)
        print("*"*50)

    def __del__ (self):
        print("I am From Destructor")
        print("I am here as GC")
        print("*"*50)
        
print("Program Execution Started")
s1=Sample()
print("*"*50)
s2=s1
print("*"*50)
s3=s2
print("*"*50)
s4=s3
print("*"*50)
s1=None
s2=None
s3=None
print("Program Execution Ended")
print("*"*50)
time.sleep(5)
        
