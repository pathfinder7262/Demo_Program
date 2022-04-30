#Telisko_construct_1.py
class Comp:
    def __init__(self):
        self.age="23"
        self.name="cc"

c1=Comp()
c2=Comp()
c2.name="pk"
c2.age=42
print(c1.name)
print(c2.name)
print(c2.age)
print(id(c1))
print(id(c2))
