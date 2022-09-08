"""
infact, we can also create chatbot, we can create multiple clients and then they will communicate to each other through server.
when client 1 send data to client 2, it will first go to server and then to c2...........its awesome....
"""

import socket

c = socket.socket()

c.connect(('localhost',4444))           # on different machine/lAPTOP , fill ip address of the server in place of localhost....this is client side
# how to get ip address of the server, use ipconfig as command on cmd

name = input("Enter your name ")         # we will send this name to the server
c.send(bytes(name,'utf-8'))
print(c.recv(1024).decode())                 # receive func and buffer size - 1024
