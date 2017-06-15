from tcp_client import TCP_Client
import math
import time
import datetime

strstarttime = datetime.datetime.now().strftime("%Y%m%d%H%M%S.%f")
log = open(strstarttime+'.log', 'a')
start = time.time()

client = TCP_Client()

after = time.time()
log.write("%f %f connection %f\n" %(start, start, after))

for i in range(100):
    before = time.time()
    client.send_data()
    after = time.time()
    log.write("%f %f send_data %f\n" %(start, before, after))
