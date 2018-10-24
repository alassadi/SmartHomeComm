import socket
import time

s = socket.socket()
host = "localhost"
port = 2004                # Reserve a port for your service.
s.bind((host, port)) 

s.listen(5) 

while True:
	c, addr = s.accept() 
	print("Got copnnection", addr)
	length_of_message = int.from_bytes(c.recv(2), byteorder='big')
	msg = c.recv(length_of_message).decode("UTF-8")
	print(msg)
	message_to_send = 'Hello Java! We got your message'.encode("UTF-8")
	c.send(len(message_to_send).to_bytes(2, byteorder='big'))
	c.send(message_to_send)
	c.shutdown(1)
	c.close() 
	 


  






















