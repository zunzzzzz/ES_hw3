import matplotlib.pyplot as plt
import numpy as np
import serial
import time

Fs = 100.0; 
Ts = 1.0 / Fs; 
t = np.arange(0, 1, Ts) 
x = np.zeros(int(Fs)) 
y = np.zeros(int(Fs)) 
z = np.zeros(int(Fs)) 
tilt = np.zeros(int(Fs)) 

serdev = '/dev/ttyACM0'
s = serial.Serial(serdev)
count = 0
for i in range(0, int(Fs)):
    line = s.readline() # Read an echo string from K66F terminated with '\n'
    # line = line.replace('\r', ' ')
    # line = line.replace('b', ' ')
    data = line.split()
    print(data)
    x[count] = float(data[0])
    y[count] = float(data[1])
    z[count] = float(data[2])
    tilt[count] = 0
    count += 1

fig, ax = plt.subplots(2, 1)
ax[0].plot(t, x, t, y, t, z)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Vec')
ax[1].plot(t, tilt)
ax[1].set_xlabel('Time')
ax[1].set_ylabel('Tilt')
plt.show()
s.close()