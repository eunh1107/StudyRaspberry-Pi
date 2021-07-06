#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time as TT

SW=15

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
	while 1:
		if GPIO.input(SW) == GPIO.HIGH:
			print("버튼 눌림")
		TT.sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()
	print("")
	exit()
