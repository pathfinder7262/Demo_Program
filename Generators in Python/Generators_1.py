def   kvrgen1(x,y):
	while(x<y):  # 10<21
		yield x 
		x=x+1

def  kvrgen2(a,b,c):
	while(a<b):
		yield a
		a=a+c

#main program
kv1=kvrgen1(10,21)   # kv(10,11,12,13,14,15,16,17,18,19,20)
print("type kv var=",type(kv1)) # type kv var= <class 'generator'>
for val in kv1:
	print(val)
print("---------------------------------")
kv2=kvrgen2(50,101,2)
for val in kv2:
	print(val)
