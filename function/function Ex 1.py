#function Ex 1.py
print("Start ==>sum of 2 number using funcion")

def sum(a,b):   #a and b isformal parameter
    """this function cal sum of 2 number"""
    c = a+b         # c is called local variable -used for storing result
    return c        # used to return a value 


print("End ==>sum of 2 number using funcion")

print("inside the functon funcion")
res=sum(10,20)
print(res)
res=sum(100,20)
print(res)
res=sum(10,200)
print(res)
res1=sum(100,200)
print(res1)
