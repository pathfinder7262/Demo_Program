#empdemo.py
from emp_pay_slip import EmpPaySlip

try:
    eo=EmpPaySlip()
    eo.paycalculation()
    eo.dispemppayslip()
except ValueError:
    print("Error")    
