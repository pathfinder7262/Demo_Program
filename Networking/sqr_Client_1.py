#sqr_Client_1.py

import socket
s = socket.socket()
s.connect(("localhost",9999))
print("*"*50)
print("Client connected")
print("*"*50)
clientdata=input("Enter any val: ")
s.send(clientdata.encode())
print("*"*50)
serverdata = s.recv(1024).decode()
print("Data from server side:  {}".format(serverdata))
print("*"*50)





