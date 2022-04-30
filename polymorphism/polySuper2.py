#polySuper2.py
class Circle:
	def  __init__(self):  # original constructor
		print("Drawing Circle:")

class Rect(Circle):
	def __init__(self):   # overridden constructor
		print("drawing Rect")

class Square(Rect):
    def __init__(self):
        super().__init__()  
        print("Drawing Square ")
                                   
		
		#main program
so=Square()# object created
