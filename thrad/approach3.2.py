#approach32.py
import threading
class MulTable:
	def  table(self, n):
		print("-"*50)
		print("Mul table for :{}".format(n))
		print("-"*50)
		for i in range(1,11):
			print("\t{} x {} = {}".format(n,i,n*i))
		else:
			print("-"*50)

#main program
n=int(input("Enterv a Number:"))
st1=threading.Thread(target=MulTable().table , args= (n, ))
st1.start()
