#12.	wapp which will calculate the area of rectangle by accepting length and breath ensure that len and brea must be +ve
print("="*60)
lent = int(input("Enter the length=> "))
bre =  int(input("Enter the breath=>"))
print("="*60)
if (lent > 0 and bre > 0):
    area = (lent * bre)
    print("Area of Rectangle:={}".format(area))
else:
    print("Wrong input")
print("="*60)    
    
