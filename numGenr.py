#16.wapp which will generate1 to n numbers where n must be the +ve int value

n =int (input("Enter the number:"))

if n >= 0:
    i=1
    while (i<=n):
        print(i)
        i=i+1
    print("complete")
else:
    print("invalid")
