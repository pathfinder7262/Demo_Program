

def card_guss(lst,no):
    for i in lst:
        if no == i:
            return lst.index(i)
                  

lst=[11,10,9,8,7,6,5,4,3,2,1,0]
no = 10

result = card_guss(lst,no)
print(result)
