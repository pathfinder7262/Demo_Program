#decore3Demo.py
def squareroot(fun):
    def docal():
        n = fun()
        res = n**0.5  
        return res
    return docal

@squareroot
def getval():
    n = float(input("Enter the any number: "))
    return n

#main program
result = getval()
print("Square root: {}".format(result))
