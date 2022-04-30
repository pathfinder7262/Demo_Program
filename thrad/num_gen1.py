#Wa Thread base application which will display 1 to 10 numbers
#after each an every second by using Thread.start
#num_gen1.py
import threading  
import time
def generate():
    print("*\n"*50)
    print("Number Within 10: \n")
    print("*"*50)
    for i in range(1,11):
        print("\t Val: {}".format(i))
        time.sleep(1)
    else:
        print("*\n"*50)

print("I AM From Main program Executing By : {} \n".format(threading.current_thread().name))
st1 = threading.Thread(target=generate)  #child thread create
st2 = threading.Thread(target=generate) 
st3 = threading.Thread(target=generate) 

print("st1 is Running befor start..??",st1.is_alive())
st1.start()
st2.start()
st3.start()
print("sub Thread started by main started\n")
print("Active Thread:{} \n".format(threading.active_count()))
print("st1 is Running befor start..??(Last)\n ",st1.is_alive())
