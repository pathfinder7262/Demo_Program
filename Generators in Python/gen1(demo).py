#gen1.py
'''
def ctngen(x,y): 
    while(x<y):
        yield x
        x=x+1

def ctngen2(a,b,c):
    while(a<b):
        yield a
        a=a+c

cc = ctngen(10,14)
print(type(cc))
print(next(cc))
print(next(cc))
print(next(cc))
print(next(cc))

    
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
pk = ctngen2(50,10)
for i in pk:
    print(i)

'''    
print("+++++++++++++++++++++++++++++OR+++++++++++++++++++++++++++++")

rv = range("a","e")
for i in rv:
    print(i)

'''   
print("=====================================================================")
rv2 = range(50,101,2)
for i in rv2:
    print(i)


'''
