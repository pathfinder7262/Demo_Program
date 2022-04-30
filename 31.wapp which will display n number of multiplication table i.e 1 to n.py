#31.wapp which will display n number of multiplication table i.e 1 to n

tbl = int(input("Enter the how many table u want:=> "))

if tbl<=0:
    print("Enter the  +ve number")
else:    
    for i in range(2,tbl+1):
        print("\nTable of =>{}".format(i))
        print("="*50)
        j=1
        while(j<=10):
            print("\t{}*{}={}".format(i,j,i*j))
            j=j+1
    print("All multiplication table generated")
