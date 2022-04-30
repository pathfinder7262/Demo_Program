#32.wapp which will display n number of multiplication table i.e a to b

l = int(input("Enter the lower bound table u want:=> "))
u = int(input("Enter the upper bound table u want:=> "))

if l<=0 and u<=0:
    print("Enter the  +ve number")
else:    
    for i in range(l,u+1):
        print("\nTable of =>{}".format(i))
        print("="*50)
        j=1
        while(j<=10):
            print("\t{}*{}={}".format(i,j,i*j))
            j=j+1
    print("All multiplication table generated")
