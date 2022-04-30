#div5.py
#form 4
try:
    s1 = float(input("Enter the value 1:==>"))
    s2 = float(input("Enter the value 2:==>"))     #---exception state.  
    x1 = int(s1)     ##---exception state. 
    x2 = int(s2)
    x3 = (x1/x2)
    print(x3)
    print("program finished")
except:          #not recomonded but u can write it at last 
    print("Exception occured")
else:
    print("ELSE BLOCK")
finally:
    print("Finally block")


