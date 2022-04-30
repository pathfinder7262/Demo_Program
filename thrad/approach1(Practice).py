#approach1.py
#which will display 1 to 10 numbers after each and every sec


import threading
import time

def dis():
    for i in range(1,11):
        print(i)
        time.sleep(2)
    else:
        print("*"*50)

print("Main Program")
print("Name OF thread before Sub Thread Start: {}\n".format(threading.current_thread().name))
print("No. of Thread Before started: {}\n".format(threading.activeCount()))
t1 = threading.Thread(target=dis)
print("T1 Is alive before started: {}".format(t1.is_alive()))
t1.start()
print("T1 Is alive After started: {}".format(t1.is_alive()))
print("Sub Thread started:  ")
print("Name OF thread after Sub Thread Start: {}\n".format(threading.current_thread()))
print("No. of Thread after started: {}\n".format(threading.activeCount()))
print("T1 Is alive at the last: {}".format(t1.is_alive()))
