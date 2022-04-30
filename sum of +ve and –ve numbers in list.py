#29.wapp which will accept of number of numbers and
#placed them in list.find sum of +ve and –ve numbers in list separately
#and display them separately.

no = int(input("Enter the size of list:"))
lst = []
for i in range(1,no+1):
    a = float(input("Enter the element:==>"))
    lst.append(a)
print(lst)
print("*"*50)
#separet the +ve and -ve number
nst = []
pst = []
for j  in lst:
    if j < 0:
        nst.append(j)
    else:
        pst.append(j)
print(nst)
print(pst)
print("*"*50)
#addition of number:==>
padd = 0
for p in pst:
    padd = p+padd
print("Addition of positive number:-",padd)    
#addition of -ve number:==>
nadd = 0
for n in nst:
    nadd = n+nadd
print("Addition of Negative number:-",nadd)    


