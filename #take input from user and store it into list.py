#take input from user and store it into list

n = int(input("Enter the size of list:"))

lst = []
for i in range(0,n+1):
    val = float(input("Enter the items in list:=="))
    lst.append(val)
print(lst)    
