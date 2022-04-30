#decore2Demo.py
def square(fun):
    def cal():
        n = fun()
        res = n*n
        return res
    return cal

@square
def getval():
    n = float(input("Enter the any number: "))
    return n

#main program
result = getval()
print("result: {}".format(result))
