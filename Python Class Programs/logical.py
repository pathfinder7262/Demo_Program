#6 demons logical operaters.

a = int(input("Enter the 1st values"))
b = int(input("Enter the 2nd values"))
c = int(input("Enter the 3rd values"))

#apply the Logical operaters

print("="*100)

print("({}<{}) and ({}<{})= {}".format(a,b,b,c,(a<b) and (b<c)))
print("({}<{}) or ({}<{})= {}".format(a,b,b,c,(a<b) or (b<c)))
print("not(({}<{}) and ({}<{}))= {}".format not((a,b,b,c,(a<b) and (b<c))))
print("not(({}<{}) or ({}<{}))= {}".format not(((a,b,b,c,(a<b) and (b<c))))