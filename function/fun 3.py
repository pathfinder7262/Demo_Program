#33.wwpp which will multiply 2 numericals values using function
#Approach 1. Taking  i/p =======> From Function Call(outside) 
#                      Process=========>Fun Body(inside)
#                      Result/Output====>Fun Call(outside)


def mul(a,b):
    c = a*b
    return c

x1=float(input("Enter the 1st value"))
x2=float(input("Enter the 2nd value"))
res=mul(x1,x2)
print("mul={}".format(res))
print("*"*60)

#Approach 2  Taking  i/p =======> From Function Body 
#                      Process=========>Fun Body
#                      Result/Output====>Fun Body
def mul1():
    a=23   #or  a = float(input("Enter the number"))
    b=32     #or b = float(input("Enter the number"))                 taking input
    c = a*b
    print("Mul1={}".format(c))   #printing result

mul1()    
print("*"*60)

#Approach 3  Taking  i/p =======> From Function Body 
#                      Process=========>Fun Body
#                      Result/Output====>Fun Body

def mul3(a,b):
                        
