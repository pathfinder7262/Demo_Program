'''
Banking Stystem using oop 
parent class:=user
hold detail about user
has a function to show user detail
child class 1 bank
Strore detail about the account balance
Strore detail about the account
Allow for deposite ,widrawal and view balance
'''

#parent class
class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender=gender

    def show_user_detail(self):
        print("User detail:")
        print("")
        print("name: ",self.name)
        print("age: ",self.age)
        print("gender: ",self.gender)

#chile class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

#deposit
    def deposit(amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("balance:",self.balance)


cc = User()
cc.show_user_detail()     