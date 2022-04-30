'''
You have to create a program where
you have to create a dictionary with key (1 to n)
and value be square of the key.

Sample Run:-
input - 5
output - {1:1 , 2:4 , 3:9 , 4:16 , 5:25}
'''

n = int(input("Enter the Number "))

d1 = {}

for i in range(1,n+1):
    d1[i]=i**2
    
print(d1) 


"""
OUTPUT:

Enter the Number 9
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
"""
