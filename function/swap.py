#swap.py

def swap(a,b):#def fun swap with formal parameter a and b 
    print("Original value of a is {}".format(a))
    print("Original value of b is {}".format(b))
    #swap logic
    a,b = b,a
    #return the values
    return a,b

#main program
x1,x2= swap(10,20)   #input for function
print("Inter change value of a is {}".format(x1))
print("Inter change value of b is {}".format(x2))


                                      
