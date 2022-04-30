#pass manage
from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key) 

def load_key():
    file=open("key.key","rb")
    key=file.read()
    file.close()
    return key


master_pwd = input("What does the master password?  ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open("pass.txt","r") as r:
        for i in r.readlines():
            data=i.rstrip()
            #print(data)
            user,passw = data.split("|")
            print("User:", user, "| pass:",str(fer.decrypt(passw.encode())))
        
def add():
    name = input("Enter Ac name:  ")
    pwd = input("ENter the Password:  ")
    with open("pass.txt", "a") as f:
        f.write(name+"|" + str(fer.encrypt(pwd.encode())))
    print("Name and Pass added")
    

while True:
    mode = input("would you like to add new pass or view existing ones (view,add,q for quit)?  ").lower()
    if mode == "q":
        print("Have a Good Day :)")
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalide")
          
