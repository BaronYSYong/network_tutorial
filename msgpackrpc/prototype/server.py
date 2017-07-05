import msgpackrpc

class Something(object):
    def ListTest(self, name, position):
        for i in range(len(name)):
            print name[i], position[i]

server = msgpackrpc.Server(Something())
server.listen(msgpackrpc.Address("", 18800))
server.start()
