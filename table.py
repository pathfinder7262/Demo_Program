#31.wapp which will display n number of multiplication table i.e 1 to n
a = int(input("Enter the number:=>"))

for i in range(1,a+1):
    print("Table of {}:=>".format(i))
    for j in range(1,11):
        print("table of  1 to {} =>{}".format(a,i*j))
    print(" ")
        
        
