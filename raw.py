from machine import I2C
from machine import Pin
from machine import sleep
import mpu6050
i2c = I2C(scl=Pin(22), sda=Pin(21))     #initializing the I2C method for ESP32
#i2c = I2C(scl=Pin(5), sda=Pin(4))       #initializing the I2C method for ESP8266
mpu= mpu6050.accel(i2c)
while True:
 mpu.get_values()
 print(mpu.get_values())
 sleep(500)


 # module for piezzo buzzer 



import machine 




class Piezzo():

    def __init__(self, pin):
        self.pin = pin 

    def init(self, pin):




