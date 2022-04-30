'''
class armstrongFind:
    def armstr(n):
        n = int(input("Enter the number: "))
        sum = 0
        copy_n = n
        order = len(str(n))

        while(n>0):
            digit = n % 10
            sum += digit **order
            n = n//10

        if (sum == copy_n):
            print("Number is Armstrong ")
        else:
            print("Number is not Armstrong ")    

arm = armstrongFind()
arm.armstr()    



n = int(input("Enter the Number: "))
sum = 0
order = len(str(n))
n_no = n
while(n>0):
    digit = n%10
    sum += digit**order
    n = n//10
    

if(n_no == sum):
    print("Armstrong") 
else:
    print("Not")
'''    
def fib(n):
    preno= 0
    currenno= 1
    for i in range(1,n):
        prepreno=preno 
        preno = currenno
        currenno = preno+prepreno
        return currenno

fib(5)