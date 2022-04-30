#thread_Ex1.py

import threading
import time
import os

def cube(val1):
    print("cube thread name: {}\n".format(threading.current_thread()))
    print("Cube of {} is: {} \n".format(val1,val1*val1*val1))
    print("Process id of cube fun: {}\n".format(os.getpid()))
    
def sqr(val2):
    print("sqr thread name: {}\n".format(threading.current_thread()))
    print("Square of {} is: {}".format(val2,val2*val2))
    print("Process id of sqr fun: {}".format(os.getpid()))


#main programm
if __name__ == "__main__":
    print("Main thread Id:  {}".format(os.getpid()))
    print("main thread name: {}".format(threading.current_thread()))


print("Number of thread befor start: {}".format(threading.active_count()))
th1 = threading.Thread(target = cube ,args = (2,))
print("\n")
th2 = threading.Thread(target = sqr ,args = (3,))
time.sleep(1)
th1.start()
th2.start()
print("Number of thread After starting: {}".format(threading.active_count()))
th1.join()
th2.join()
