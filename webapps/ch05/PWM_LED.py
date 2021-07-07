#!/usr/bin/env python
#-*- coding:utf-8 -*-

import RPi.GPIO as GPIO
import time

LED=18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
PwmObj = GPIO.PWM(LED, 50)  #PWM 객체 생성(GPIO 번호:18, 주파수:50)
PwmObj.start(0)				#듀티비 0으로 PWM 발생 시작

try:
	while 1:
		for dc in range(0, 101, 5):
			PwmObj.ChangeDutyCycle(dc)
			time.sleep(0.01)
		for dc in range(100, -1, -5):
			PwmObj.ChangeDutyCycle(dc)
			time.sleep(0.1)
except KeyboardInterrupt:
	pass
PwmObj.stop()
GPIO.cleanup()
