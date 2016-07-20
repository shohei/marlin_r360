import numpy as np
import matplotlib.pyplot as plt
import serial
import re

ser = serial.Serial("/dev/tty.usbserial",115200)

# decimal = re.compile(r"([1-9]\d*|0)(\.\d+)?")
decimal = re.compile(r"-?\d+\.\d*")
# plt.axis([0, 10, 0, 1])
# plt.ion()

# for i in range(10):
#     y = np.random.random()
#     plt.scatter(i, y)
#     plt.pause(0.05)

cnt = 0
cnts = []
vels = []
rs = []
while True:
    line = ser.readline()
    print line,
    velocities = re.findall(decimal,line)
    if not velocities:
        continue
    # if len(velocities) < 2:
    #     continue
    r = float(velocities[0])
    velocity = float(velocities[1])
    # velocity = float(velocities[2])
    cnts.append(cnt)
    vels.append(velocity)
    rs.append(r)
    # print cnt,velocity
    # plt.axis([0, 200, 0, 1500])
    # plt.axis([0, 200, -20, 200])
    plt.axis([0, 200, -20, 500])
    # plt.axis([0, 200, -20, 1500])
    plt.plot(cnts,rs,'r')
    plt.plot(cnts,vels,'b')
    plt.pause(0.05)
    cnt += 1
    if(cnt>200):
        plt.cla()
        cnt = 0
        cnts = []
        vels = [] 
        rs = []

ser.close()
