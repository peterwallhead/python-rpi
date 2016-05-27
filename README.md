## Arduino to Python reference
| Description | Arduino | Python |
| :--- |:---| :---|
| Import library for board pins | - | import RPi.GPIO as GPIO |
| Import time library      | - | import time |
| To use Raspberry Pi board pin numbers | - | GPIO.setmode(GPIO.BOARD) |
| Set pin modes | pinMode(13, OUTPUT); | GPIO.setup(13, GPIO.OUT) |
| Turn pin ON | digitalWrite(13, HIGH); | GPIO.output(13,GPIO.HIGH) |
| Turn pin OFF | digitalWrite(13, LOW); | GPIO.output(13,GPIO.LOW) |
| Wait 1 second before next command | delay(1000); | time.sleep(1) |
