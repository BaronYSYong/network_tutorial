import socket
import sys

class TCP_Client(object):
    def __init__(self, ip = 'localhost', port = 10000):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (ip, port)
        self.sock.connect(server_address)
    
    def send_to_server(self, message):
        self.sock.send(message)            


if __name__ == '__main__':
    client = TCP_Client()
    message = "Random Message"
    client.send_to_server(message)
