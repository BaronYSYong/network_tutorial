import socket
import sys

class TCP_Server(object):
    def __init__(self, port=10000):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('', port)
        self.sock.bind(server_address)
        self.sock.listen(1)

    def accept_from_client(self):
        connection, client_address = self.sock.accept()        
        try:
            print >>sys.stderr, 'connection from', client_address
            data = connection.recv(255)
            return data                
        finally:
            connection.close()        

if __name__ == '__main__':
    data = TCP_Server()
    print data.accept_from_client()



