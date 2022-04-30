#decoratorex1_User_I/p.py
def  square(fun):
        def  cal():
                try:
                        n=fun()
                        res=n*n
                        return res
                except TypeError:
                        print("")
                        exit
        return cal

#normal function
@square
def   getval():
    try:
        n=float(input("Enter any number:"))
        return n
    except ValueError:
            print("Enter the Number: ")
            exit
#main program
res=getval()
print("Rersult",res)
