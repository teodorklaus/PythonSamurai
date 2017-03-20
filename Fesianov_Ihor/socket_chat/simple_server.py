__author__ = 'Ihor'
# -*- coding: utf-8 -*-
import socket

host = 'localhost'
port = 14900

sock = socket.socket()

sock.bind((host, port))
sock.listen(1)

conn, addr = sock.accept()
print('connected:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    data = data.decode()
    print(data)
    data = input()
    data = data.encode()
    conn.send(data)

conn.close()