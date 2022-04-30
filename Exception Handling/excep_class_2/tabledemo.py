#tabledemo.py

user = input("Enter username: ")
pw = input("Enter password: ")

try:
    validation(user,pw)
except LoginError:
    print("wrong input entered")
    
