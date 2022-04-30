#34wappwhich will calculate the all arethmatic calculation using function


def addfun(a,b):    #fun def
    c = a+b     #fun process(body/logic)
    return c

def subfun (a,b):
    c = a-b
    return c

def mulfun(a,b):
    c = a*b
    return c

def divfun(a,b):
    c = a/b
    return c

def intdivfun(a,b):
    c = a//b
    return c

def modfun(a,b):
    c = a%b
    return c


x1= float(input("Enter the x1 value:=>"))
x2= float(input("Enter the x2 value:=>"))
c = modfun(x1,x2)   #func call(input)
print("Addition is=>{}".format(c))
