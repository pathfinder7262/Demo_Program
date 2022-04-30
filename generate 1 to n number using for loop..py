#21.Wapp which will generate 1 to n number using for loop.

a = int(input("Enter the number"))
print("*"*50)
if a >= 0:
    for i in range(1,a+1):
        print("\t\t",i)
else:
    print("Invalid")
print("*"*50)
