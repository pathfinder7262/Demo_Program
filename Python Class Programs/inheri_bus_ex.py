''' Create a child class Bus that will inherit all of the variables and methods
of the Vehicle class
'''
#inheri_bus_ex.py
class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class bus(Vehicle):
    pass


b=bus("MumPun",70,22)
print("Vehicle Name:=",b.name,"  speed=>",b.max_speed,"mph","  Mileage=>",b.mileage,"kmpl")
