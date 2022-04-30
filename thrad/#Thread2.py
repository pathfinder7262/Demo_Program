#Thread2.py
#this program demonstrate how to create sub thread/child thread and
#exicuting the logic of program, whiich is writting in function.


from threading  import *
def hello():
    print("Welcome to Multi Threading:")  
    print("Main Program Statement Executed By: ",active_count())      
def hi(val):
    print("{},elcome to My Class".format(val))
    print("Main Program Statement Executed By: ",current_thread())
    print("Main Program Statement Executed By: ",active_count())  


#main program
print("Main Program Statement Executed By: ",current_thread().name)
hello()
hi("CC")
