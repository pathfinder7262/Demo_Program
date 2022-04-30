#20.Wapp which will generate odd numbers bet 1 to n

n = int(input("Enter the number"))
if n>=0:
    i = 0   #initialize
    while i <= n:   #condition
        if i%2!=0:     #condition for odd number 
            print(i)
        i = i+1    #increment
else:
    print("invalid input")
print("Finished")    

