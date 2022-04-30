#17.wapp which will find and generate some of 1 to n number

i = int(input("Enter the number"))
if i<=0:
     print("invalid")
else:
    s = 0
    n= 0
    while n<=i:
        s = s+n
        n= n+1
        #print(n)
    print("*"*60)
    print(s)
    print("*"*60)
       
