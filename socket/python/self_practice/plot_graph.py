import matplotlib.pyplot as plt
import sys

elapsed_time = []
times = []
with open(sys.argv[1],'r') as infile:
    i = 1
    for line in infile:
        items = line.split(' ')
        elapsed_time.append(items[2])
        times.append(i)
        i += 1
plt.plot(times, elapsed_time)
plt.title(sys.argv[1])
plt.grid()
plt.show()
    
