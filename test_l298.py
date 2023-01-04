# Author: Olivier Lenoir - <olivier.len02@gmail.com>
# Created: 2020-06-14 21:05:12
# Project: Test L298 Dual H-bridge, MicroPython
# Description:

from l298n import L298N
from utime import sleep

motor = L298N(2, 4, 5)
motor.speed(500)
motor.forward()
sleep(2)
motor.speed(200)
motor.forward()
sleep(2)
motor.stop()
motor.reverse()
sleep(2)
motor.stop()




from machine import Pin, PWM


class L298N:

	def __init__(self, en, in1, in2, freq=1000):
		self.freq = freq
		self.speed = 0
		self.en = PWM(Pin(en, Pin.OUT), freq = self.freq, duty = self.duty)
		self.in = Pin(in, Pin.OUT)
		sle

