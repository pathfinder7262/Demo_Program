#multable_2.py  <==== treated as module
from excep_class1 import invalidInputError
def table(n):
    if(n<=0):
        raise invalidInputError
    else:
        print("*"*50)
        print("multiplication table for:{}".format(n))
        for i in range(1,11):
            print("/t{}x{}={}".format(n,i,n*i))
        else:
            print("="*50)
