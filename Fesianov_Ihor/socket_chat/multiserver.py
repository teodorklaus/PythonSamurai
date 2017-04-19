__author__ = 'Ihor'
# -*- coding: utf-8 -*-

import socket
from threading import Thread, Lock
import sys


class Server:
    HOST = 'localhost'
    PORT = 14900
    NUMBER_OF_CLIENTS = 8

    def __init__(self, host=HOST, port=PORT, num_of_cli=NUMBER_OF_CLIENTS):
        self.sock = socket.socket()
        self.sock.bind((host, port))
        self.sock.listen(num_of_cli)
        self.sock.setblocking(0)  # make non-blocking socket
        print('Server is running....')

        self.clients = []

        clients_connector = Thread(target=self.clients_connector)
        main = Thread(target=self.main)

        clients_connector.start()

        main.start()

        # make main thread
        while True:
            message = input('Enter "exit" to exit\n')
            if message == 'exit':
                self.sock.close()
                sys.exit()
            else:
                pass

    def clients_connector(self):
        while True:
            try:
                conn, addr = self.sock.accept()
                conn.setblocking(False)
                lock = Lock()
                lock.acquire()
                self.clients.append({'conn': conn, 'addr': addr})
                lock.release()
                print('connected:', addr)
            except:
                pass

    def main(self):
        """
        Receive messages from each clients and send to all
        """
        while True:
            if len(self.clients) > 0:
                for client in self.clients:
                    try:
                        data = client['conn'].recv(1024)
                        name = '{}: '.format(client['addr']).encode()
                        data = name + data
                        if data:
                            self.message_to_all(data, client)
                    except:
                        pass

    def message_to_all(self, data, client):
        for cli in self.clients:
            if cli['conn'] != client['conn']:
                cli['conn'].send(data)

s = Server()
