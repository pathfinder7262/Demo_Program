#23.Wapp which will number of numbers and add value to the list. display the value of list.

num = int(input("Enter the values:==>"))
print("_-_"*26)
if num >=0:
    lst = []
    for i in range(1,num+1):
        val = float(input("Enter the {} value u store:==>".format(i)))
        lst.append(val)
        print("_-_"*26)
    print("Elemet in list:=>",lst)
     print("Elemet in list:=>",lst)
else:
    print("invalid")
print("_-_"*26)
