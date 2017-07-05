import msgpackrpc

client = msgpackrpc.Client(msgpackrpc.Address("localhost", 18800))
result = client.call('sum', 1, 2)  # = > 3
print result
