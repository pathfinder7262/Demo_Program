#19.Wapp gen even number from givin number n

n = int(input("Enter the number:==>"))

if n >=0:
    i=0
    while i<=n:
        if i%2==0:
            print("Even number:==>{}".format(i))
        i =  i +1       
else:
    print("Invalid Input=>{}".format(n))
