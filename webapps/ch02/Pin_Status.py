#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time as TT

LED=3

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

input("Enter..")

GPIO.cleanup()
