#approach_1.py
from threading import *

def hello():
    print("Welcome")
    print("Hello Method Executed by sub Thread")
    print("*"*50)

#main program
print("I am From Main Program Executed by:  {}".format(current_thread().name))
st1 = Thread(target=hello)#child Thread created by Main Thread
st1.start() #sub thread started
print("Main Thread Started Sub Thread")
    
