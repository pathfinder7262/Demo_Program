#cal2.py

from cal_Exce_class1 import div
from Exec_class1 import CcDivisionError

try:
    div(10,0)
except CcDivisionError:
    print("Dont Enter zeo at Dinominater")
else:
    print("Else")
finally:
    print("Finally block")
