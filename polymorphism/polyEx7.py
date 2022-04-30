#polyEx7.py
class India:
    def lang(self):
        print("Indians can speak diff lang")
    def type(self):
        print("India is developing country")

class America:
    def lang(self):
        print("Indians can speak English lang")
    def type(self):
        print("India is developed country")

io1 = India()
ao1 = America()

for x in [io1,ao1]:  #here an obj x contain reference(id) of io1 and ao1
                                #and x contain polimorpfic nature
    x.lang()
    x.type()

'''OUTPUT:
polyEx7.py
Indians can speak diff lang
India is developing country
Indians can speak English lang
India is developed country
>>> 

'''
    
    
