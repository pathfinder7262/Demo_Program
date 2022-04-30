class comp:
    def conf(self,rm,hd):
        print("CPU RAM: ",rm)
        print("CPU HD: ",hd)

obj1 = comp()

comp.conf(obj1,"12GB","2tb")


obj1.conf("8gb","1TB")
obj1.conf("4GB","500GB")
