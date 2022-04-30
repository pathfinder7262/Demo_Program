#Multiple_thread_1.py

#one thread generate even no another thread will generate odd numbers and
#3rd thread willl generate each and every leter in given sentance

import threading
import time

def even(num1):
    print("Welcome to Even Function:  \n")
    for i in range(1,num1+1):
        if i%2 == 0:
            print("Even Number is: {}\t".format(i))
        


def odd(num2):
    print("Welcome to Odd Function\n")
    for i in range(1,num2+1):
        if i%2 != 0:
           print("Odd Number is: {}\t".format(i))

def letter(str1):
    print("Welcome To Letter Generate: \n")
    for i in str1:
        print("Letter is : {}\t".format(i))
    
        

print("main Thread is : {}\n".format(threading.current_thread().name))
t1 = threading.Thread(target=even,args=(20,))
t2 = threading.Thread(target=odd,args=(10,))
t3= threading.Thread(target=letter,args=("Chetan",))

print("Active No. Of Thread before start: {}".format(threading.active_count()))

print("is t1 Alive: {}\n".format(t1.is_alive()))
print("is t2 Alive: {}\n".format(t2.is_alive()))
print("is t3 Alive: {}\n".format(t3.is_alive()))

t1.start()

t2.start()

t3.start()


print("Name OF Active  Thread after start: {}".format(threading.current_thread().name))
print("Active No. Of Thread after start: {}".format(threading.active_count()))

print("is t1 Alive: {}\n".format(t1.is_alive()))
print("is t2 Alive: {}\n".format(t2.is_alive()))
print("is t3 Alive: {}\n".format(t3.is_alive()))


