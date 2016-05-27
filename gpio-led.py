# LED common leg to GPIO9
# LED red leg to GPIO11
# LED green leg to GPIO13
# LED blue leg to GPIO15

import RPi.GPIO as GPIO
import time

# Blinking function
def blink(pin1,pin2,pin3,period):
        GPIO.output(pin1,GPIO.HIGH)
        time.sleep(period)
        GPIO.output(pin1,GPIO.LOW)
        GPIO.output(pin2,GPIO.HIGH)
        time.sleep(period)
        GPIO.output(pin2,GPIO.LOW)
        GPIO.output(pin3,GPIO.HIGH)
        time.sleep(period)
        GPIO.output(pin3,GPIO.LOW)
        return

# To use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

# Set up GPIO output channels
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

# Blink GPIO11, GPIO13, GPIO15 5 times, alternating once every second
for i in range(0,5):
        blink(11,13,15,1)

# Reset GPIO state
GPIO.cleanup()
