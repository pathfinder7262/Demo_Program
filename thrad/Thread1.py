#Thread1.py
#this program obtaining current thread

import threading
print("1:")
print("Name of Default Threadin In Python Program:  ",threading.currentThread())
print("I Am CC")
print("This Is My First Program")
print("*"*50)

'''
OUTPUT:
Name of Default Threadin In Python Program:   <_MainThread(MainThread, started 4980)>
I Am CC
This Is My First Program

'''

print("2:")
print("Name of Default Threadin In Python Program:  ",threading.currentThread())
print("Name of Default Threadin In Python Program:  ",threading.currentThread().name)
print("I Am CC")
print("This Is My First Program")
print("*"*50)


'''
OUTPUT:
Name of Default Threadin In Python Program:   <_MainThread(MainThread, started 9880)>
Name of Default Threadin In Python Program:   MainThread
I Am CC
This Is My First Program
*************************************************
'''

print("3:")
print("Name of Default Threadin In Python Program:  ",threading.currentThread())
print("Name of Default Threadin In Python Program:  ",threading.currentThread().name)
print("No. Of Thread Active(At This Time): ",threading.activeCount())
print("I Am CC")
print("This Is My First Program")
print("*"*50)

'''
OUTPUT:
3:
Name of Default Threadin In Python Program:   <_MainThread(MainThread, started 8284)>
Name of Default Threadin In Python Program:   MainThread
No. Of Thread Active(At This Time):  2
I Am CC
This Is My First Program
**************************************************
'''
