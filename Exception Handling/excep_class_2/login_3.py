#login_3.py<==treated as module

from excep_class1 import LoginError
def validation(un,pwd):
    if((un!= "kvr") or (pwd!="python")):
        raise LoginError
    else:
        print("-"*50)
        n=int(input("Enter the table u want:"))  #internaly value error is raising
        table(n)
