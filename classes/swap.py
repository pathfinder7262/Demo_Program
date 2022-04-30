'''
swap.py
1.wapp which will accept 2 int val and swap them by using classes and obj

'''
class Swap:
    def getint(self):
        self.d1=int(input("Enter the 1st number: "))
        self.d2=int(input("Enter the 2nd number: "))
    def swapVal(self):
        self.d1=self.d1 ^ self.d2
        self.d2=self.d1 ^ self.d2
        self.d1=self.d1 ^ self.d2
        print("After Swaped d1:{} and d2:{}".format(self.d1,self.d2))
        
        

so=Swap()
so.getint()
so.swapVal()
