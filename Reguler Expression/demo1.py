#program for obtained only capital letter from string

str="ChetanChaudhari998@Gmail.Com"
noc =0
for i in str:
    if(i >= "A" and i<="Z"):
        print(i)
        noc = noc+1
        print("="*50)
print(noc)    
