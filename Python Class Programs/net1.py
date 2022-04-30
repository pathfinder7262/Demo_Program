'''#wapp which will impliment the following
a)WA server side program which will accept a numerical int val
from clint side program square it and sent back to client
b)WA client side program which will send a int numerical val and
obtain the square of it from the servar side program

'''
#this program accept int val from client sode program and
#gives result back to client side program

#SQR_Networking_Servar1.py

import socket

s = socket.socket()
s.bind(("localhost",9999))
s.listen(4) #4 client requst can listen (we can increament it as we want) 
print("\nServer is ready to serve...")
print("*"*60)
while(True):
#more statement
   conn,addr = s.accept()
   print("*"*60)
   print("type of conn: {}".format(type(conn)))
   print("type of addr: {}".format(type(addr)))
   print("*"*60)
   clientdata=conn.recv(1024).decode()
   print("Data From Client: {}".format(clientdata))
   val = float(clientdata)
   result=val*val #process
   conn.send(str(result).encode())
