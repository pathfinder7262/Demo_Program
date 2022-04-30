#program to store stno,name,marks and college nm(Dynamically)
#stud_class_2.py(Dynamically)
class Student:pass


Student.cnm="mk Gandi college"  #class level data member 
s1 = Student()  #s1 called object
print("Content of s1(before)=",s1.__dict__)
#add data(data member) in s1
while(True):
    s1.stno=int(input("Enter the Roll no."))
    s1.name=(input("Enter the Name."))
    s1.marks=float(input("Enter the Marks"))
    #print("Content of s1(After)=",s1.__dict__)  or
    print("{}\t{}\t{}\t{}".format(s1.stno,s1.name,s1.marks,s1.cnm))
    ch = input("Again insert Y/N=>")
    if (ch == "n"):
        break

print("="*50)


