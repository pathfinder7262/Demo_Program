#factorial pp6
s1 = "chetan"


def fact(a):
    f = 1
    for i in range(1,a+1):
        f = f*i
    return f

x1 = int(input("Enter the number==>"))
res = fact(x1)         
print(res)
