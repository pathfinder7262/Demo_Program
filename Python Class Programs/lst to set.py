#lst to set


l1 = [10,20,"eds",32.54]
print(l1,type(l1))
print("*"*60)

print("lst to set")
s1= set(l1)
print(s1,type(s1))

print("lst to tuple")
t1= tuple(l1)
print(t1,type(t1))
print("*"*60)

s2={12,32,44,"dsa",65.54,32,"dsa"}
print("set to tuple")
t2 =  tuple(s2)
print(t2,type(t2))

print("set to list")
l2 = list(s2)
print(l2,type(l2))
print("*"*60)

t3 = (90,54.45,"BB",22)
print("tuple to set")
s4 = set(t3)
print(s4,type(s4))

print("tuple to lst")
l4 = list(t3)
print(l4,type(l4))












