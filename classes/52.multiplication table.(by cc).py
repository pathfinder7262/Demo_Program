#52.wapp which will accept numerical value and generates its multiplication table.

class multbl:
    def tblcal(self):
        self.a=int(input("Enter the no.==>"))
        print("Table of  {}==>".format(self.a))
        for i in range(1,11):
            print(self.a * i)


t1=multbl()
t1.tblcal()

help(multbl)

