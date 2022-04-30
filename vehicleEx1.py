class vehicle:
    color = "white"
    charges = 100
    def __init__(self,name,mspeed,mileage,capacity):
        self.name= name
        self.mspeed = mspeed
        self.mileage=mileage
        self.capacity = capacity
        

class bus(vehicle):
    def fare(self):
        self.amt = vehicle.charges * self.capacity
        self.famt = self.amt *(10/100)
        return self.famt
        
class car(vehicle):pass
    

        
v1 = bus("Valvo",120,21,50)
print(v1.color,v1.name,v1.mspeed,v1.mileage,v1.charges)
print(bus.fare())
