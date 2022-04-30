#decore1Demo.py
def square(fun):
    def cal():
        n = fun()
        res = n*n
        return res
    return cal


def getval():
    return 5

#main program
result = square(getval)
print("result: {}".format(result()))
