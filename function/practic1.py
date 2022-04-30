#swap function using bitwise XOR operater

def swap(a,b):
    a = a^b
    b = a^b
    a= a^b
    return a,b
    

res = swap(10,20)
print(res)    


