#!/usr/bin/env python
#-*- coding:utf-8 -*-

import RPi.GPIO as GPIO
import time

SW=17

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
	while 1:
		State = GPIO.input(SW)
		print("상태 : %d" %State)
		time.sleep(0.5)
except KeyboardInterrupt:
	pass

GPIO.cleanup()

