#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time as TT

LED=4	#GPIO 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

for i in range(10):
	GPIO.output(LED, 1)
	TT.sleep(1)
	GPIO.output(LED, 0)
	TT.sleep(1)
GPIO.cleanup()
