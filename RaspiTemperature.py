import os
import time
from time import strftime
import subprocess

#os.system('modprobe w1-gpio')
#os.system('modprobe w1-therm')

temp_sensor = '/sys/bus/w1/devices/28-0014118cfcff/w1_slave'

def temp_raw():

    f = open(temp_sensor, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():

    lines = temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = temp_raw()
    temp_output = lines[1].find('t=')

    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_c = float(temp_string) / 1000.0
       # temp_f = temp_c * 9.0 / 5.0 + 32.0
        return '%.3f' %temp_c
    return "ERROR"

while True:
        temp = read_temp()
        strTime = strftime("%Y-%m-%d %H:%M:%S") 
	with open("/home/pi/RaspiTemperature/index.html", "w") as thefile:
		thefile.write(temp)
		thefile.write(' ' + strTime)


	time.sleep(600)
