import sys
import time

title = sys.argv[1]
send_data = open(title.replace(".log", "_SendData.csv"), 'w')

with open(sys.argv[1],'r') as infile:
    for line in infile:
        items = line.split(' ')
        cumulative_time = float(items[3]) - float(items[0])
        elapsed_time = float(items[3]) - float(items[1])  
    
        if items[2] == "send_data":
            send_data.write("%s %f %f\n" %(items[2], cumulative_time, elapsed_time))

send_data.close()

