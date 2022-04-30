#lst_Using_Class
class list:
    def __init__(self):
        self.lst = []
    def add(self,a):
        self.lst.append(a)
    def remove(self,a):
        self.lst.remove(a)
    def  desp(self):
        print(self.lst)

obj =list()        

ch = 1
while ch != 0:
    print("0 for Exit")
    print("1 for Add Element")
    print("2 for Remove")
    print("3 for desp")

    ch = int(input("Enter The Option: "))
    if ch == 1:
        val = float(input("Enter the Value To Add: "))
        obj.add(val)
        print("Value Added")
    elif ch == 2:
        obj.desp()
        val = float(input("Enter The Element You Want To Remove: "))
        obj.remove(val)
        print("Element deleted!")
    elif ch == 3:
        print("Your List Is: ")
        obj.desp()
    elif ch == 0:
        print("Thanks...")
    else:
        print("Invalide choice..")
        
        
        
    
        
