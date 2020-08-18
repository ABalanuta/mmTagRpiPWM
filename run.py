#!/usr/bin/env python3

# sudo apt-get install pigpio python-pigpio python3-pigpio
# http://abyz.me.uk/rpi/pigpio/python.html#set_PWM_frequency
# sudo killall pigpiod
# sudo pigpiod -s 4

import pigpio
from os import system
from time import sleep


system("sudo pigpiod -s 4")
sleep(2)

pi = pigpio.pi()

######################################

# Inverter Enable
pi.write(27, 1)

# Switch A Enable
pi.write(22, 1)

# Set PWM of Switch A
pi.set_PWM_dutycycle(12, 128) # out of 255

######################################

# Switch B Enable
pi.write(17, 1)

# Set PWM of Switch A
pi.set_PWM_dutycycle(13, 128) # out of 255
######################################

while True:
        sleep(10)
