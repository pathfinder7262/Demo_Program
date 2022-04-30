#
print("="*50)
st = [2,4,7,5,9]
for i in st:
    if i <= 0:
        print("invalid")
    else:
        for p in st:
            print("\n\n")
            k = 0
            while k<=10:
                print("{}*{}={}".format(p,k,p*k)
                k = k+1
#some error
