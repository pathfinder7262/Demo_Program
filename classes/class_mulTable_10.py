#52.wapp which will accept numerical value and generates its multiplication table.
#class_mulTable_10



class MulTab:
    def setvalue(self):
        self.n=int(input("Enter the number"))
    def table(self):
        if(self.n<=0):
            print("wrong Input")
        else:
            print("="*50)
            print("TABLE OF = {}".format(self.n))
            for i in range(1,11):
                print("\t{}  x  {}  =  {}".format(self.n,i,self.n*i))
            print("="*50)    


#main prog
while(True):
    try:
        mt = MulTab()
        mt.setvalue()
        mt.table()
    except ValueError:
        print("Enter the correct value")
    ch = input("again Y/N")
    if(ch == "n"):
        break
