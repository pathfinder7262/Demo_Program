#53.wapp which will find biggest  of 3 numbers with classes and object

#class_big_11.py

class big:
    def readvalues(self):
        self.a= 21
        self.b=54
        self.c=34
    def bigval(self):
        big=self.a  #big is local variable 
        if(self.b>big):
            big = self.b
        if(self.c>big):
             big = self.c
        return big  #returning big local vari
    def dispbig(self,res):
        print(big)



#main
b= big()
b.readvalues()
bv = b.bigval()
b.dispbig(bv)
