#polym1.py
class Teacher:
	def study(self):  # original method
		print("Teacher advised to all the student to read 4 hours")
	
class LazyStudent(Teacher):
	def study(self): #overridden method
		print("Lazy student decided to read 30 mins")
		

class PerfectStudent (Teacher):
	def study(self): #overridden method
		print("Perfect student decided to read 4 hours and practice 2 hrs")
		
#main program
lz=LazyStudent()
lz.study()
print("-------------------------------")
ps=PerfectStudent()
ps.study()
print("-------------------------------")

