"""
Resource:
https://pymotw.com/2/socket/tcp.html
"""

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

"""!@brief
Then bind() is used to associate the socket with the server address. 
In this case, the address is localhost, referring to the current server,
and the port number is 10000.
"""
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

"""!@brief
Calling listen() puts the socket into server mode, and accept() waits 
for an incoming connection.
"""
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    
    """!@brief
    accept() returns an open connection between the server and client, 
    along with the address of the client. The connection is actually a 
    different socket on another port (assigned by the kernel). Data is 
    read from the connection with recv() and transmitted with sendall().
    """
    
    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                print >>sys.stderr, 'sending data back to the client'
                connection.sendall(data)
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
            
    finally:
        """!@brief
        When communication with a client is finished, the connection needs to 
        be cleaned up using close(). This example uses a try:finally block to 
        ensure that close() is always called, even in the event of an error.
        """
        connection.close()



