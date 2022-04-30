#program to store stno,name,marks and college nm
#stud_class_1.py
class Student:pass


Student.cnm="mk Gandi college"  #class level data member 
s1 = Student()  #s1 called object
print("Content of s1(before)=",s1.__dict__)
#add data(data member) in s1
s1.stno=10
s1.name="Rossum"
s1.marks=78.87
#print("Content of s1(After)=",s1.__dict__)  or
print("{}\t{}\t{}\t{}".format(s1.stno,s1.name,s1.marks,s1.cnm))

print("="*50)

s2 = Student()  #s2 called object
print("Content of s1(before)=",s2.__dict__)
#add data(data member) in s2
s2.stno=11
s2.name="gosling"
s2.marks=87.87
print("{}\t{}\t{}\t{}".format(s2.stno,s2.name,s2.marks,s2.cnm))
#OR
#print("Content of s1(After)=",s2.__dict__)
print("="*50)
