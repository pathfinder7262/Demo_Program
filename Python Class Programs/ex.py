def  swapvalues(a,b):
	print("Original Value of a:{}".format(a))  # 10
	print("Original Value of b:{}".format(b))   # 20
	#swap logic
	a,b=b,a
	#return the values
	return a,b      # in python , we can return more than one value.


#main program
x1,x2=swapvalues(10,20)   #function call
print("-----------------------------------------------------")
print("Inter changed val of a={}".format(x1))
print("Inter changed val of b={}".format(x2))

