#39.wapp which will retrieve only the even and odd element separately by
#using filter function (normal/anonymous fun)
#evenoddfltEx2.py

lst=[12,32,534,54,765,32,87,54,76,97,92,45,33,0,53]

evnlst=list(filter(lambda n : n%2==0,lst))
print(evnlst)

oddlst=list(filter(lambda n : n%2!=0,lst))
print(oddlst)
