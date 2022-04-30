#stud_class3_self.py
#demon. instance method concept
class Stud:

    def getstuddetain(self):
          print("ID of self in fun ={}".format(id(self)))
          self.stno=int(input("Enter the Roll no."))
          self.name=(input("Enter the Name."))
          self.marks=float(input("Enter the Marks"))

    def dispstuddetail(self):
        print("Stud No:=={}".format(self.stno))
        print("Stud Name:=={}".format(self.name))
        print("Stud Marks:=={}".format(self.marks))
        
#main prog
s1=Stud()
print("Id of s1 in main=={}".format(id(s1)))
s1.getstuddetain()
print("{}\t{}\t{}".format(s1.stno,s1.name,s1.marks))
s1.dispstuddetail()

print("="*60)

s2=Stud()
print("Id of s2 in main=={}".format(id(s2)))
s2.getstuddetain()
print("{}\t{}\t{}".format(s2.stno,s2.name,s2.marks))
s2.dispstuddetail()
