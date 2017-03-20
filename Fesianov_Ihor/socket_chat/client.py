_author__ = 'Ihor'
# -*- coding: utf-8 -*-
import socket
from threading import Thread


class Client:
    HOST = 'localhost'
    PORT = 14900

    def __init__(self, host=HOST, port=PORT):
        self.sock = socket.socket()
        self.sock.connect((host, port))
        print('Start connection....')

        message_receive = Thread(target=self.message_receive)
        # message_receive.daemon = True
        message_receive.start()

        while True:
            message = input()
            if message != 'exit':
                self.send_message(message)
            else:
                self.sock.close()

    def message_receive(self):
        while True:
            try:
                data = self.sock.recv(1024)
                if data:
                    print(data.decode())
            except:
                pass

    def send_message(self, message):
        self.sock.send(message.encode())

c = Client()