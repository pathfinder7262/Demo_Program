#cal.py

from Exe_class1 import CcDivisionError
def div(a,b):
    if(b==0):
        raise CcDivisionError
    else:
        c = a/b
        return c

result = div(4,0)
