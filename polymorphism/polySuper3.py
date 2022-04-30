#polySuper3.py
class Teacher:
	def study(self):  
		print("Teacher advised to all the student to read 4 hours")
	
class LazyStudent:
	def study(self): 
		print("Lazy student decided to read 30 mins")
		

class PerfectStudent (Teacher,LazyStudent):
	def study(self): #overridden method
		print("Perfect student decided to read 4 hours and practice 2 hrs")
		super().study()
#main program
lz=LazyStudent()
lz.study()
print("-------------------------------")
ps=PerfectStudent()
ps.study()
print("-------------------------------")

