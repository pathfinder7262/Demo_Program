#multiplication all element in set

set1 = {2,5,4}

def mul(set1):
    a = 1
    for i in set1:
        a = i*a
    print(a)
    return a

res  = mul(set1)    
