import socket
import sys
import config

class TCP_Client(object):
    def __init__(self, ip = config.ip, port = config.port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (ip, port)
        self.client.connect(server_address)    

    def send_data(self, data='client'):
        data = 'client'
        self.client.send(data)     
        while True:
            data = self.client.recv(255)
            if data:
                break
        print data
