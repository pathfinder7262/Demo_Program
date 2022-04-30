#div4.py
#form 3
try:
    s1 = float(input("Enter the value 1:==>"))
    s2 = float(input("Enter the value 2:==>"))     #---exception state.  
    x1 = int(s1)     ##---exception state. 
    x2 = int(s2)
    x3 = (x1/x2)
    print(x3)
    print("program finished")
except(ValueError,NameError,ZeroDivisionError): #multi exception handle block
    print("don't enter star/alphanumerics/spacial symbol:")
    print("don't pass 2 parameter")
    print("don't enter 0 for dinominater")
else:
    print("ELSE BLOCK")
finally:
    print("Finally block")


#one doubt
