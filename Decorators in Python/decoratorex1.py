#decoratorex1.py
def  square(fun):  # Decorator function
	def  cal():
		n=fun()
		res=n*n
		return res
	return cal

#normal function
def   getval():
	return 5

#main program
result=square(getval)
print("result={}".format(result() ))

