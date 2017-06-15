import socket
import sys

class TCP_Server(object):
    def __init__(self, port=10000):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('', port)
        self.sock.bind(server_address)
        self.sock.listen(1)    

if __name__ == '__main__':
    socket = TCP_Server()
    while True:
        connection, client_address = socket.sock.accept()
        try:
            print "received from ", client_address
            while True:
                data = connection.recv(255)
                if data:
                    print data
                    connection.sendall('server')  
                else:
                    print "break"
                    break
        finally:
            connection.close()        
