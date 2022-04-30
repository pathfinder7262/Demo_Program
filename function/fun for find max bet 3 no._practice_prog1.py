#fun for find max bet 3 no._practice_prog

def maxbet3(a,b,c):    #fun defination/formal parameter
    if a>b and a>c:                                     #fun body/logic
        print("{} is big".format(a))
    elif b>c:
        print("{} is big".format(b))
    else:
         print("{} is big".format(c))


#x1 = float(input("Enter the 1st number"))
#x2 = float(input("Enter the 2nd number"))
#x3 = float(input("Enter the 3rd number"))
    
maxbet3(32,54,87)         #fun call/fun argument
maxbet3(32532,514,87)
maxbet3(332,53244,87)
maxbet3(312,354,287)
maxbet3(31,43,32)

