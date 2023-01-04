# Complete project details at https://RandomNerdTutorials.com/micropython-hc-sr04-ultrasonic-esp32-esp8266/
from hcsr04 import HCSR04
from time import sleep
from machine import I2C
import mpu6050


i2c = I2C(scl=Pin(5), sda=Pin(4))       #initializing the I2C method for ESP8266

# mpu6050 -- gyroscope x accelerometer -- initializing 
mpu= mpu6050.accel(i2c)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

# hcsr40 -- distance sensor -- initializing -- 
hcsr = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=10000)
# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 


while True:

    # hcsr40 -- distance sensor -- get distance 
    distance = hcsr.distance_cm()
    print('Distance:', distance, 'cm')

    # mpu6050 -- gyroscope x accelerometer -- get values
    print(mpu.get_values())

    # sleep for 
    sleep(1)