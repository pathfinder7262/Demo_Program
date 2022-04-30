#div3.py
#form 2
try:
    s1 = float(input("Enter the value 1:==>"))
    s2 = float(input("Enter the value 2:==>"))     #---exception state.  
    x1 = int(s1)     ##---exception state. 
    x2 = int(s2)
    x3 = (x1/x2)
    print(x3)
    print("program finished")
except ValueError as cc:
    print(cc)   #it display tech mass related to exception
    #print("don't enter star/alphanumerics/spacial symbol:")
except  NameError as zd:
    print(zd)
except  ZeroDivisionError as pk:
    print(pk)
else:
    print("ELSE BLOCK")
finally:
    print("Finally block")
