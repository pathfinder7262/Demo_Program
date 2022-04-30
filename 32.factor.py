#32.wapp factor for a given number

f =int(input("Enter the number u want to get factor:=>"))
non = 0
for i in range(1,(f//2)+1):
    if f%i==0:
        non = non+1
        print(i)    
    
