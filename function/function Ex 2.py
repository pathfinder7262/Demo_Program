#function Ex 2.py
#take input from user
print("Start ==>sum of 2 number using funcion")

def sum(a,b):   #a and b isformal parameter
    """this function cal sum of 2 number"""
    c = a+b         # c is called local variable -used for storing result
    return c        # used to return a value 


print("End ==>sum of 2 number using funcion")

print("inside the functon funcion")
res=sum(10,20)
