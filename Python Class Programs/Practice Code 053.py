"""
Practice Code: 053

Task:
You have to create a program where a list of numbers is
given and a number of rotation is given. Now you to bring
last number of list in front and swift each number to the right.
Do this till the given number of rotation.

Sample :-
input - [1,2,3,4] , 2
output - [4,1,2,3] -> [3,4,1,2]

l1=[]
sz = int(input("Enter the size of List: "))
for i in range(1,sz+1):
    li = int(input("Enter the list item: "))
    l1.append(li)

print(l1)
"""
l1 = [11,22,33,44,55]
nr = 2

l1[1] = l1[0]
l1[0] =  l1[-1]


    
print(l1)

    

