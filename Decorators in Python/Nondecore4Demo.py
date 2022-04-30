#Nondecore4Demo.py

def getval():
    n = float(input("Enter The Value: "))
    return n

def squareRoot():
    n = getval()
    res = n**0.5
    return res

#main program
result = squareRoot()
print("Square root: {}".format(result))
