#14wapp which will accept the distance in km and convert it in miters and cm and miles where km must be the +ve number
km =  int(input("Enter the km==> "))
print("<>"*20)
if km>0:
    mtr = km*1000
    cm = km*100000
    print("<>"*20)
    print("km in meter:==>{}".format(mtr))
    print("<>"*20)    
    print("km in cm:==>{}".format(cm))
    print("<>"*20)
else:
    print("Invalid value")

