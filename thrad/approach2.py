#approach2.py
from threading import *    #------------(1)Importing threading
	 
class Kvr(Thread):  #create class kvr which is inherited from Thread
	def   run(self):   # overriding run()---(4)
		print("i am from run()")
		print("run() executed by sub thread")

#main program
k=Kvr()  # crating an object of Kvr is nothing but creating an object Thread class
k.start()  # here start() is internally calling run()
