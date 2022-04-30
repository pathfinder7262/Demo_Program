#anonfun1.py

#Normal Function
def sum(a,b):
    c = a+b
    return c

res1 = sum(4,3)
print(res1)
res2 = sum(45,3)
print(res2)
res3 = sum(8,3)
print(res3)
print("*"*60)

print("Annonymous Fun")

addop = lambda a,b,c : a+b+c

res4 = addop(12,-13,14)
print(res4)
