#cal.py

from Exec_class1 import CcDivisionError
def div(a,b):
    if(b==0):
        raise CcDivisionError
    else:
        c = a/b
        print(c)


