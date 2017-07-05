import msgpackrpc

client = msgpackrpc.Client(msgpackrpc.Address("localhost", 18800))
name = ['a','b','c','d']
position = [[1,2,3], [2,3,4], [3,4,5], [4,5,6]]
result = client.call('ListTest', name, position)
