# we r clirnt and google is a server,
# the base of the internet or networks is Sockets,we will we using client and server in socket pgming, 2 files here
# 2 concept : port NO and type of connection we want to build ,    0 - 65535 : port no range

import socket

s = socket.socket()               # s for server
print("Socket Created")

# server will bind socket to the port no and client will simply connect it
s.bind(('localhost',4444))          # we have both server and client on this same machine, so lacalhost  AND   9999- port no

s.listen(3)                       # listen only 3 clients
print("Waiting for Connections")

while True:
    c , addr = s.accept()            # c for client , addr is addrress of client
    name = c.recv(1024).decode()
    print("Connected with ", addr,name)

    c.send(bytes("Welcome to telusko ",'utf-8'))    # utf-8 format in which we want to send it

    c.close()