#fltr_spc_fun1.py
def pos(x):
    if x>0:
        return True
    else:
        return False

def neg(y):
    if y<0:
        return True
    else:
        return False

def diselem(lst):
    print("*"*50)
    for val in lst:
        print(val)
    print("*"*50)    



#main progr
lst=[10,-20,30,-40,-50,60,70,-34,56,0]
diselem(lst) #fun call

print("*"*50)
pobj=filter(pos,lst)   #Syntax = filter(fun_name,itarable_obj_name) and fobj is object of<class,'filter'>
print(pobj)

print("*"*50)
nobj=filter(neg,lst)
print(nobj)

print("*"*50)
polst = list(pobj)
diselem(polst) #fun call

print("*"*50)
negtpl = tuple(nobj)
diselem(negtpl) #fun call
    
