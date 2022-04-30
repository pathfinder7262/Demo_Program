#desctructor_8pm_sample1.py
import time
class Sample:
    def __init__(self):
        print("I am From Constructor")
        self.a=10
        self.b=20
        print(self.a)
        print(self.b)

    def __del__ (self):
        print("I am From Destructor")
        print("I am here as GC")

print("Program Execution Started")
s1=Sample()
print("Program Execution Ended")
time.sleep(5)
        
