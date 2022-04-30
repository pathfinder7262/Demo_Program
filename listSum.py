#26.Wapp which will accept no. of values in a list and compute their sum and average

num = int(input("Enter how many number u want to enter:"))
print("="*50)
if num <= 0:
    print("invalid")
else:
    lst = []
    for i in range(0,num+1):
        a = float(input("Enter the list number=>"))
        lst.append(a)
    
    else:
        s = 0
        for a in lst:
            s = s+a
            print(a)
            print("="*50)
        else:
             print("sum=>{}".format(s))
             print("="*50)
             print("average:{}".format(s/len(lst)))
             print("="*50)
      
        

