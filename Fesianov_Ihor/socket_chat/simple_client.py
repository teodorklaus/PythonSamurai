__author__ = 'Ihor'
# -*- coding: utf-8 -*-
import socket

sock = socket.socket()

host = 'localhost'
port = 14900
sock.connect((host, port))
print('Start connection....')


def send_message():
    text = input()
    sock.send(text.encode())
    return text


def get_message():
    text = sock.recv(1024)
    return text.decode()


while True:
    send_message()
    print(get_message())

sock.close()
