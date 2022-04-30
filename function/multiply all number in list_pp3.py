#multiply all number in list

def mulelem(for_param):
    mul = 1
    for i in [8,2,3,-1,7]:
        mul = i*mul
    return mul   

mul = mulelem([8,2,3,-1,7])
print(mul)
