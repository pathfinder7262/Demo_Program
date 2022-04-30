#performance.py
import numpy as np
import sys
lst = [10,20,30,40,50,60,70,80,90,90,8,7,6,5,4,3,2,1,1,12,23,34,45,56,67,78,89,99,98,87,76,65,54,43,32,21,11,23,45,67,89,12]

a=np.array([10,20,30,40,50,60,70,80,90,90,8,7,6,5
       ,4,3,2,1,1,12,23,34,45,56,67,78,89,99,98,87,
       76,65,54,43,32,21,11,23,45,67,89,12])

print("\n Memory space taken by lst obj= {}".format(sys.getsizeof(lst)))
print("\n Memory space taken by ndarray a obj= {}".format(sys.getsizeof(a)))
