import time
def fib(n):
    preno= 0
    currenno= 1
    for i in range(2,n):
        prepreno=preno 
        preno = currenno
        currenno = preno+prepreno
    return currenno


def fibborecursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibborecursive(n-1) + fibborecursive(n-2)


init = time.time()    
print(fib((7)))
print(f"it took for fib {time.time() - init} second")
#print(fibborecursive(35))
print(f"it took for fibbrecur {time.time() - init} second")
