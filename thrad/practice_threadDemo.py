#practice_threadDemo.py

import threading
import time
'''
print("Active thread: ",threading.active_count())
print(threading.currentThread().getName())
print("Hello Python")
print("Active thread: ",threading.activeCount() )
print("*"*65)

OUTPUT:
Active thread:  2
MainThread
Hello Python
Active thread:  2
'''

#how to create sub thread


def cc():
    #print("CC Fun Executed By: ",threading.current_thread())
    print("CC's function: ")
    

def pk(val):
    #print("pk Fun Executed By: ",threading.current_thread())
    print("this is {} function: ".format(val))
    

#main program
print("Curren thread(We R Inside The Main Program) = {} ".format(threading.current_thread().name))
print("Count thread(We R Inside The Main Program): {}".format(threading.active_count()))
t1= threading.Thread(target=cc)
t2 = threading.Thread(target=pk,args=("pk",))
print("Type Of t1 =  ",type(t1))
print("Type Of t2 =  ",type(t2))
print("Count thread(After Creating t1 And t2 thread but Not Start: {} ".format(threading.active_count()))
t1.start()
t2.start()
print("Count thread(After Creating t1 And t2 thread & after Starting: {} ".format(threading.active_count()))
print("name of t1 ={}".format(t1.getName()  ))
print("name of t1 ={}".format(t2.getName()  ))
t1.setName("chetan")
print("name of t1 ={}".format(t1.getName()  ))
